#!/usr/bin/env python3
"""
Wipex — Google Trends fetcher (validated 2026-09-23).

WHY THIS SCRIPT LOOKS ODD
  curl to trends.google.com returns HTTP 429 from this host, so the fetch must run inside a
  real browser session. And the browser harness used here does not return stdout reliably,
  so the in-browser code WRITES ITS RESULT TO A FILE in the workspace and we read it back.
  That is why the shell is a string and the output is a file.

WHAT IT DISCOVERED (do not rediscover)
  1. widgetdata needs the widget's `token`, or you get HTTP 401.
  2. The endpoint is named by widget TYPE, not id:
        TIMESERIES        -> widgetdata/multiline
        RELATED_QUERIES*  -> widgetdata/relatedsearches
        GEO_MAP*          -> widgetdata/comparedgeo
     Calling widgetdata/TIMESERIES returns 404.
  3. Responses start with `)]}'` + newline. Strip it or JSON.parse throws on an HTML page.
  4. An EMPTY timelineData means the term is below Trends' reporting threshold == no
     measurable demand. That is a finding, not an error. See references/02 zero-data branch.

USAGE
  python trends_fetch.py code     # prints the browser_exec block to run
  python trends_fetch.py report <path/to/trends_*.json>
"""
import json
import sys

KEYWORDS_A = ['restaurant table cleaning wipes', 'table busser wipes',
              'food service cleaning wipes', 'commercial table wipes']
KEYWORDS_B = ['restaurant table turnover', 'table turnover rate',
              'restaurant labor cost', 'restaurant cleaning supplies']

BROWSER_CODE = '''# Google Trends fetch (US). Result is written to a workspace file.
import os, json, time
goto_url("https://trends.google.com/trends/explore?geo=US&date=today%201-m&q=cleaning&hl=en-US")
wait_for_load()
time.sleep(4)

JS = r"""
window.__out=null; window.__log=[];
(async () => {
 const base='/trends/api/';
 const EP={TIMESERIES:'multiline',GEO_MAP:'comparedgeo'};
 const ep=id=>EP[id]||(id.startsWith('RELATED_QUERIES')?'relatedsearches':(id.startsWith('GEO_MAP')?'comparedgeo':null));
 const clean=t=>{ if(t.startsWith(")]}\'")){ const i=t.indexOf('\\n'); return t.slice(i+1);} return t; };
 const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 async function fetchT(url,ms){ const c=new AbortController(); const to=setTimeout(()=>c.abort(),ms);
   try{ const r=await fetch(url,{credentials:'include',signal:c.signal}); const t=await r.text(); clearTimeout(to);
     window.__log.push(url.replace(base,'').split('?')[0]+'->'+r.status); return {status:r.status,text:t}; }
   catch(e){ clearTimeout(to); window.__log.push('ERR '+url.replace(base,'').split('?')[0]); return null; } }
 async function explore(kws,geo,tm){
   const req={comparisonItem:kws.map(k=>({keyword:k,geo:geo,time:tm})),category:0,property:''};
   const e=await fetchT(base+'explore?hl=en-US&tz=-180&req='+encodeURIComponent(JSON.stringify(req)),15000);
   if(!e||!e.text.startsWith(")]}\'")) return null; return JSON.parse(clean(e.text)); }
 async function wdata(name,w){ return fetchT(base+'widgetdata/'+name+'?hl=en-US&tz=-180&req='+encodeURIComponent(JSON.stringify(w.request))+(w.token?('&token='+encodeURIComponent(w.token)):''),15000); }
 const mean=a=>a.length?Math.round(a.reduce((x,y)=>x+y,0)/a.length*10)/10:null;
 async function probe(kw,geo,tm){
   const e=await explore([kw],geo,tm);
   if(!e) return {kw:kw,geo:geo,time:tm,error:'explore'};
   const w=e.widgets.find(x=>x.id==='TIMESERIES'); if(!w) return {kw:kw,geo:geo,time:tm,error:'no_widget'};
   const d=await wdata('multiline',w);
   if(!d||d.status!==200||!d.text.startsWith(")]}\'")) return {kw:kw,geo:geo,time:tm,error:'widget'};
   const td=(JSON.parse(clean(d.text)).default||{}).timelineData||[];
   const vals=td.map(p=>p.value[0]);
   return {kw:kw,geo:geo,time:tm,n:vals.length,avg:mean(vals),
     first7:mean(vals.slice(0,7)),last7:mean(vals.slice(-7)),
     mid:mean(vals.slice(7,Math.max(7,vals.length-7))),peak:vals.length?Math.max(...vals):null,
     top:td.map(p=>({l:p.formattedTime,v:p.value[0]})).sort((a,b)=>b.v-a.v).slice(0,3)}; }
 async function geoOf(kw,geo,tm){
   const e=await explore([kw],geo,tm); if(!e) return {kw:kw,error:'explore'};
   const g=e.widgets.find(x=>x.id==='GEO_MAP_0')||e.widgets.find(x=>x.id==='GEO_MAP');
   if(!g) return {kw:kw,error:'no_geo'};
   const d=await wdata('comparedgeo',g);
   if(!d||d.status!==200||!d.text.startsWith(")]}\'")) return {kw:kw,error:'widget'};
   const j=JSON.parse(clean(d.text));
   return {kw:kw,geo:((j.default&&j.default.geoMapData)||[]).filter(r=>r.value&&r.value[0]>0)
     .sort((a,b)=>b.value[0]-a.value[0]).slice(0,8).map(r=>r.geoName+':'+r.value[0])}; }
 const A=__A__, B=__B__;
 const out=[];
 for(const k of A.concat(B)){ out.push(await probe(k,'US','today 1-m')); await sleep(350);
                              out.push(await probe(k,'US','today 12-m')); await sleep(350); }
 for(const k of A.slice(0,3)){ out.push(await probe(k,'BR','today 12-m')); await sleep(350); }
 for(const k of A.slice(0,3)){ out.push(await geoOf(k,'US','today 12-m')); await sleep(350); }
 window.__out=JSON.stringify({when:new Date().toISOString(),data:out,log:window.__log});
})(); 'go'
"""
print(js(JS))
for _ in range(160):
    time.sleep(3)
    if js("window.__out"): break
v = js("window.__out")
ws = os.environ.get("BH_AGENT_WORKSPACE", ".")
path = os.path.join(ws, "trends_%s.json" % time.strftime("%Y%m%d_%H%M"))
open(path, "w", encoding="utf-8").write(v or "NULL")
print("WROTE", path)
'''


def emit_code():
    code = BROWSER_CODE.replace("__A__", json.dumps(KEYWORDS_A)).replace("__B__", json.dumps(KEYWORDS_B))
    print("# Paste the following into browser_exec (single call).")
    print("# Edit KEYWORDS_A / KEYWORDS_B at the top of this file first.")
    print("# Then read the written JSON back with: python trends_fetch.py report <path>")
    print("-" * 78)
    print(code)


def report(path):
    raw = open(path, encoding="utf-8").read()
    payload = raw.split("\n---LOG---")[0]
    d = json.loads(payload)
    rows = d if isinstance(d, list) else d.get("data", [])
    if isinstance(d, dict):
        print("when:", d.get("when", "?"))
    print(f"{'keyword':34} {'geo':3} {'range':11} {'n':>4} {'avg':>6} {'first7':>7} {'last7':>7} {'mid':>6} {'peak':>5}  note")
    print("-" * 112)
    zero = []
    for r in rows:
        # records produced by the extras() helpers carry a 'kind' tag; they are not probes
        if r.get("kind") == "related":
            lists = r.get("lists") or []
            print(f"RELATED [{r.get('kw')}]")
            for i, l in enumerate(lists):
                label = "TOP:" if i == 0 else "RISING:"
                print(f"    {label:8} " + ", ".join(str(x) for x in l))
            continue
        if r.get("kind") == "geo":
            top = r.get("top") or r.get("geo") or []
            print(f"GEO     [{r.get('kw')}] -> " + ", ".join(str(x) for x in top))
            continue
        # geoOf() rows have no 'time' key and carry a list of 'State:index' strings
        if "time" not in r and isinstance(r.get("geo"), list):
            print(f"GEO  {str(r.get('kw',''))[:34]:34} -> {r.get('geo')}")
            continue
        n = r.get("n")
        note = r.get("error", "")
        if n == 0:
            note = (note + " ZERO DATA - below Trends threshold").strip()
            zero.append(r.get("kw"))
        elif n is None:
            if r.get("error"):
                note = "fetch failed: " + str(r["error"])
            else:
                zero.append(r.get("kw"))
        print(f"{str(r.get('kw',''))[:34]:34} {str(r.get('geo',''))[:3]:3} {str(r.get('time',''))[:11]:11} {str(n):>4} "
              f"{str(r.get('avg')):>6} {str(r.get('first7')):>7} {str(r.get('last7')):>7} "
              f"{str(r.get('mid')):>6} {str(r.get('peak')):>5}  {note}")
        for t in r.get("top") or []:
            if isinstance(t, dict) and "v" in t:
                print(f"{'':>12}top: {t.get('l')} = {t.get('v')}")
    print()
    print("ZERO-DATA TERMS (no measurable demand -> apply the pivot branch in references/02):")
    for k in sorted({k for k in zero if k}):
        print("  -", k)
    print()
    print("REMINDERS")
    print("  * index is relative per keyword; averages are NOT comparable across terms")
    print("  * absolute search volume is NOT available here. Say so; do not estimate.")
    print("  * a peak of 100 is normalisation, not popularity")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "code":
        emit_code()
    elif len(sys.argv) >= 3 and sys.argv[1] == "report":
        report(sys.argv[2])
    else:
        print(__doc__)
