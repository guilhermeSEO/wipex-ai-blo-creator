// Google Trends probe — inject into a live trends.google.com tab.
//
// Usage (browser_exec):
//   goto_url("https://trends.google.com/trends/explore?geo=US&q=seed&hl=en-US"); wait_for_load()
//   print(js(open("<skill>/scripts/google-trends-probe.js").read()))
//   then poll js("window.__done") until 999, and read js("JSON.stringify(window.__res)")
// Adjust TERMS / GEO / RANGE below, then persist the result to $BH_AGENT_WORKSPACE.
//
// Verified working 2026-09: explore -> widgetdata needs the per-widget token; endpoint is
// named by widget KIND (multiline / relatedsearches / comparedgeo), not by the widget id.
window.__res = [];
window.__done = 0;
window.__log = [];

(async () => {
  const TERMS = ['table turnover', 'restaurant staffing', 'cost per use'];
  const GEO = 'US';            // 'BR' etc. for the secondary market
  const RANGES = ['today 1-m', 'today 12-m'];
  const base = '/trends/api/';

  const clean = t => t.startsWith(")]}'") ? t.slice(t.indexOf('\n') + 1) : t;
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const mean = a => a.length ? Math.round(a.reduce((x, y) => x + y, 0) / a.length * 10) / 10 : null;

  async function fetchT(url, ms) {
    const c = new AbortController();
    const to = setTimeout(() => c.abort(), ms || 15000);
    try {
      const r = await fetch(url, { credentials: 'include', signal: c.signal });
      const t = await r.text();
      clearTimeout(to);
      window.__log.push(url.replace(base, '').split('?')[0] + '->' + r.status);
      return { status: r.status, text: t };
    } catch (e) {
      clearTimeout(to);
      window.__log.push('ERR ' + url.replace(base, '').split('?')[0]);
      return null;
    }
  }

  const json = r => (r && r.status === 200 && r.text.startsWith(")]}'")) ? JSON.parse(clean(r.text)) : null;

  async function explore(kws, geo, tm) {
    const req = {
      comparisonItem: kws.map(k => ({ keyword: k, geo: geo, time: tm })),
      category: 0, property: ''
    };
    return json(await fetchT(base + 'explore?hl=en-US&tz=-180&req=' +
      encodeURIComponent(JSON.stringify(req))));
  }

  async function widget(kind, w) {
    return json(await fetchT(base + 'widgetdata/' + kind + '?hl=en-US&tz=-180&req=' +
      encodeURIComponent(JSON.stringify(w.request)) +
      (w.token ? '&token=' + encodeURIComponent(w.token) : '')));
  }

  const KIND = id => id === 'TIMESERIES' ? 'multiline'
    : id.startsWith('RELATED_QUERIES') ? 'relatedsearches'
    : (id.startsWith('GEO_MAP')) ? 'comparedgeo' : null;

  // One term at a time: a bundled call masks which term has no data.
  async function probe(kw, geo, tm) {
    const out = { kw: kw, geo: geo, time: tm };
    const e = await explore([kw], geo, tm);
    if (!e) { out.error = 'explore'; return out; }

    const ts = e.widgets.find(w => w.id === 'TIMESERIES');
    if (ts) {
      const j = await widget('multiline', ts);
      const td = (j && j.default && j.default.timelineData) || [];
      const vals = td.map(p => p.value[0]);
      out.n = vals.length;
      out.avg = mean(vals);
      out.first7 = mean(vals.slice(0, 7));
      out.last7 = mean(vals.slice(-7));
      out.mid = mean(vals.slice(7, Math.max(7, vals.length - 7)));
      out.peak = vals.length ? Math.max.apply(null, vals) : null;
      out.topPeriods = td.map(p => ({ l: p.formattedTime, v: p.value[0] }))
        .sort((a, b) => b.v - a.v).slice(0, 3);
    }
    await sleep(400);

    // single-keyword queries use the bare id; multi-keyword uses the _0 suffix
    const rq = e.widgets.find(w => w.id === 'RELATED_QUERIES' || w.id === 'RELATED_QUERIES_0');
    if (rq) {
      const j = await widget('relatedsearches', rq);
      const rl = (j && j.default && j.default.rankedList) || [];
      out.related = rl.map(g => (g.rankedKeyword || []).slice(0, 10).map(x => ({ q: x.query, v: x.value })));
    }
    await sleep(400);

    const gm = e.widgets.find(w => w.id === 'GEO_MAP' || w.id === 'GEO_MAP_0');
    if (gm) {
      const j = await widget('comparedgeo', gm);
      const rows = (j && j.default && j.default.geoMapData) || [];
      out.geo = rows.filter(r => r.value && r.value[0] > 0)
        .sort((a, b) => b.value[0] - a.value[0]).slice(0, 10)
        .map(r => r.geoName + ':' + r.value[0]);
    }
    return out;
  }

  for (const k of TERMS) {
    for (const tm of RANGES) {
      window.__res.push(await probe(k, GEO, tm));
      await sleep(350);
      window.__done = window.__res.length;   // incremental: survives a timeout
    }
  }
  window.__done = 999;
})();
'started'
