#!/usr/bin/env python3
"""
Wipex — house-pattern audit.

  python audit_blog_patterns.py --corpus                 # re-measure the live corpus
  python audit_blog_patterns.py --draft path/to/draft.md # score one draft against the house

--corpus  pulls the Shopify atom feeds (the articles.json endpoint 404s on this store),
          takes the 21 most recent posts, fetches each page, slices the body out of
          <div class="rte text-spacing"> by <div> depth, and writes metrics to
          <workdir>/04-data/blog_patterns_21.csv and 21_blogs_outline.md

--draft   accepts markdown, computes the same dimensions, and prints PASS / FAIL against the
          targets recorded in references/08-house-patterns.md
"""
import csv
import html
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter

UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/124.0 Safari/537.36'}
OUT = r"C:\Users\guilh\AppData\Local\hermes\workdir\wipex\04-data"
NS = {'a': 'http://www.w3.org/2005/Atom'}
FEEDS = ['https://wipex.co/blogs/library.atom',
         'https://wipex.co/blogs/wipex-studio-library.atom']

# targets for a new post (references/08-house-patterns.md)
TARGET = {'words': (3000, 4500), 'h2': (14, 22), 'h3': (8, 24),
          'paras': (50, 80), 'avg_para': (35, 55),
          'products': (4, 10), 'blogs': (4, 8)}


def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read().decode('utf-8', 'ignore')


def strip(b):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', b or '', flags=re.S | re.I)
    t = re.sub(r'<br\s*/?>', ' ', t, flags=re.I)
    t = re.sub(r'</(p|div|li|h[1-6]|tr|td)>', ' \n ', t, flags=re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    return html.unescape(re.sub(r'[ \t]+', ' ', t)).strip()


def slice_div(h, start):
    i, depth, n = start, 0, len(h)
    pat = re.compile(r'<(/?)div\b[^>]*>', re.I)
    while i < n:
        m = pat.search(h, i)
        if not m:
            break
        depth += -1 if m.group(1) else 1
        i = m.end()
        if depth == 0:
            return h[start:m.start()]
    return h[start:start + 200000]


def metrics(body):
    text = strip(body)
    links = re.findall(r'href="([^"]+)"', body)
    hs = re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>', body, flags=re.S | re.I)
    heads = [(int(l), strip(re.sub(r'<[^>]+>', '', t))) for l, t in hs]
    paras = [p for p in re.findall(r'<p[^>]*>(.*?)</p>', body, flags=re.S | re.I) if strip(p)]
    pw = [len(strip(p).split()) for p in paras]
    return {
        'words': len(text.split()),
        'h2': sum(1 for l, _ in heads if l == 2),
        'h3': sum(1 for l, _ in heads if l == 3),
        'paras': len(paras),
        'avg_para': round(sum(pw) / len(pw)) if pw else 0,
        'max_para': max(pw) if pw else 0,
        'imgs': len(re.findall(r'<img', body, re.I)),
        'tables': len(re.findall(r'<table', body, re.I)),
        'lists': len(re.findall(r'<ul|<ol', body, re.I)),
        'faq': bool(re.search(r'frequently asked|\bFAQ\b', text, re.I)),
        'qm': len(re.findall(r'\?', text)),
        'products': sum(1 for l in links if '/products/' in l),
        'blogs': sum(1 for l in links if '/blogs/' in l),
        'colls': sum(1 for l in links if '/collections/' in l),
        'heads': heads,
        'h2_list': [t for l, t in heads if l == 2],
    }


def corpus():
    entries, seen = [], set()
    for feed in FEEDS:
        for page in range(1, 4):
            url = feed + (f'?page={page}' if page > 1 else '')
            try:
                root = ET.fromstring(get(url))
            except Exception as e:
                print('ERR', url, e)
                break
            es = root.findall('a:entry', NS)
            if not es:
                break
            for e in es:
                lk = e.find('a:link', NS).get('href')
                if lk in seen:
                    continue
                seen.add(lk)
                entries.append({'url': lk, 'handle': lk.rstrip('/').split('/')[-1],
                                'title': (e.findtext('a:title', default='', namespaces=NS) or '').strip(),
                                'published': e.findtext('a:published', default='', namespaces=NS),
                                'author': (e.find('a:author/a:name', NS).text
                                           if e.find('a:author/a:name', NS) is not None else '')})
    entries.sort(key=lambda x: x['published'], reverse=True)
    last = entries[:21]
    os.makedirs(OUT, exist_ok=True)
    rows, outlines = [], []
    for i, e in enumerate(last, 1):
        try:
            h = get(e['url'])
        except Exception as ex:
            print('FETCH FAIL', e['url'], ex)
            continue
        m = re.search(r'<div[^>]*class="[^"]*rte text-spacing[^"]*"[^>]*>', h, re.I)
        body = slice_div(h, m.end()) if m else h
        met = metrics(body)
        met.update({'n': i, 'date': e['published'][:10], 'handle': e['handle'],
                    'title': e['title'], 'author': e['author']})
        rows.append(met)
        outlines.append((i, e['published'][:10], e['title'], e['handle'], met['h2_list']))
    if not rows:
        print('no rows collected')
        return
    cols = ['n', 'date', 'handle', 'title', 'author', 'words', 'h2', 'h3', 'paras', 'avg_para',
            'max_para', 'imgs', 'tables', 'lists', 'faq', 'qm', 'products', 'blogs', 'colls']
    with open(os.path.join(OUT, 'blog_patterns_21.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    with open(os.path.join(OUT, '21_blogs_outline.md'), 'w', encoding='utf-8') as f:
        f.write('# Wipex - 21 blogs mais recentes (base de padrao)\n\n')
        for n, d, t, hd, h2 in outlines:
            f.write(f'## {n}. {d} - {t}\n- handle: `{hd}`\n- H2s ({len(h2)}):\n')
            for x in h2:
                f.write(f'  - {x}\n')
            f.write('\n')
    print(f"{'#':>2} {'date':10} {'words':>6} {'h2':>3} {'h3':>3} {'par':>4} {'avgP':>4} {'img':>4} {'tbl':>3} {'ul':>3} {'faq':>4} {'prod':>4} {'blog':>4}  title")
    for r in rows:
        print(f"{r['n']:>2} {r['date']:10} {r['words']:>6} {r['h2']:>3} {r['h3']:>3} {r['paras']:>4} "
              f"{r['avg_para']:>4} {r['imgs']:>4} {r['tables']:>3} {r['lists']:>3} {str(r['faq']):>4} "
              f"{r['products']:>4} {r['blogs']:>4}  {r['title'][:52]}")
    for k in ['words', 'h2', 'h3', 'paras', 'avg_para', 'imgs', 'products', 'blogs']:
        v = [r[k] for r in rows]
        print(f"{k:10} min {min(v):>6}  mean {round(sum(v) / len(v), 1):>7}  max {max(v):>6}")
    print(f"FAQ present: {sum(1 for r in rows if r['faq'])}/{len(rows)}   "
          f"tables: {sum(1 for r in rows if r['tables'])}/{len(rows)}   "
          f"lists: {sum(1 for r in rows if r['lists'])}/{len(rows)}")
    c = Counter()
    for *_, h2 in outlines:
        for x in h2:
            c[x] += 1
    print('\nRecurring H2 headings (theme chrome included):')
    for k, v in c.most_common(40):
        print(f'{v:>2}x  {k}')
    print('\nWROTE', OUT)


def draft(path):
    src = open(path, encoding='utf-8').read()
    # convert markdown-ish draft to the same shape the corpus metrics expect,
    # PRESERVING heading levels so H2/H3 counts are meaningful
    body = re.sub(r'^(#{1,6})\s*(.+)$',
                  lambda m: '<h%d>%s</h%d>' % (len(m.group(1)), m.group(2).strip(), len(m.group(1))),
                  src, flags=re.M)
    body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', body)
    body = re.sub(r'^\s*[-*+]\s+', '<li>', body, flags=re.M)
    met = metrics(body)
    # Markdown has no <p>/<ul> tags, and the HTML conversion above erases the '#' markers.
    # Parse the RAW source with a small state machine: a list item keeps swallowing its
    # continuation lines (soft-wrapped markdown), so a wrapped bullet does not become a
    # 5-word "paragraph". Headings, table rows, quotes and code fences are not paragraphs.
    blocks, cur_type, cur_lines, in_code = [], None, [], False

    def _flush():
        nonlocal cur_type, cur_lines
        if cur_lines and cur_type:
            blocks.append((cur_type, ' '.join(cur_lines)))
        cur_type, cur_lines = None, []

    for line in src.splitlines():
        s = line.strip()
        if s.startswith('```'):
            in_code = not in_code
            _flush()
            continue
        if in_code:
            continue
        if not s:
            _flush()
            continue
        if re.match(r'^[-*+]\s|^\d+[.)]\s|^\[ \]|^\[[xX]\]', s):
            _flush()
            cur_type, cur_lines = 'list', [s]
            continue
        if re.match(r'^(#{1,6}\s|\||>)', s):
            _flush()
            continue
        if cur_type is None:
            cur_type = 'para'
        cur_lines.append(s)
    _flush()

    paras = [t for k, t in blocks if k == 'para' and len(t.split()) >= 5]
    pw = [len(p.split()) for p in paras]
    if pw:
        met['paras'] = len(pw)
        met['avg_para'] = round(sum(pw) / len(pw))
        met['max_para'] = max(pw)
    met['lists'] = 1 if any(k == 'list' for k, _ in blocks) else 0
    met['words'] = len(strip(body).split())
    met['faq'] = bool(re.search(r'frequently asked|\bFAQ\b', src, re.I)) or '?\n' not in src and len(re.findall(r'\?', src)) >= 6
    lines = ['# PATTERN AUDIT — <name>', f'source: {path}', '']
    print(f"{'dimension':12} {'draft':>8} {'target':>13}  verdict")
    print('-' * 52)
    fails = []
    for k, (lo, hi) in TARGET.items():
        v = met.get(k, 0)
        ok = lo <= v <= hi
        if not ok:
            fails.append(k)
        print(f"{k:12} {v:>8} {f'{lo}-{hi}':>13}  {'PASS' if ok else 'FAIL'}")
        lines.append(f"{k}: {v} (target {lo}-{hi}) {'PASS' if ok else 'FAIL'}")
    for k, want in [('faq', 'required'), ('tables', 'when comparing formats'), ('lists', 'required')]:
        v = met.get(k)
        ok = bool(v) if k in ('faq', 'lists') else True
        print(f"{k:12} {str(v):>8} {want:>13}  {'PASS' if ok else 'FAIL'}")
        lines.append(f"{k}: {v} ({want}) {'PASS' if ok else 'FAIL'}")
        if not ok:
            fails.append(k)
    print()
    if fails:
        print('NOT DELIVERABLE — off-pattern on:', ', '.join(fails))
        print('See references/08-house-patterns.md for the measured house numbers.')
    else:
        print('ON PATTERN — dimensions within the measured house range.')
    print('\nReminder: this audit is structural only. Compliance is checked separately by the')
    print('7-step review in references/03. Passing this audit is not a compliance clearance.')
    out = os.path.join(os.path.dirname(os.path.abspath(path)), 'pattern-audit.md')
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print('\nWROTE', out)


if __name__ == '__main__':
    if '--corpus' in sys.argv:
        corpus()
    elif '--draft' in sys.argv:
        draft(sys.argv[sys.argv.index('--draft') + 1])
    else:
        print(__doc__)
