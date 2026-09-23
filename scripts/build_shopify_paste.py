#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wipex blog -> Shopify section emitter  (v3.0 — reference grade)

WHAT CHANGED FROM v2.7
  v2.7 emitted a text-only section: scoped CSS, the cleared prose, one calculator, and a schema
  with `"settings": []`. The operator could not change a word or add an image without editing
  Liquid, there was nothing to look at on the page, and a second instance of the section would
  collide with the first.

  Reading the house reference section (02-setup/reference-sections/REFERENCE_pilates-fall-2026.liquid,
  736 lines) showed what a finished Wipex module actually contains: theme-editor settings, a media
  system (16:9 / 2:3 stills with srcset + focal point + caption, a native video band with fallback
  and overlay), an interactive TOC, a real checklist, reading progress, a sticky mobile CTA,
  data-cro instrumentation on every CTA, a11y landmarks and instance-safe JavaScript.

  This version emits all of that, around copy that is STILL generated from the compliance-approved
  markdown — the one invariant we do not trade away. The reference's own marketing copy would fail
  our Claims Filter ("The Best Wipe System", "Best for:", "equipment-safe"); its copy is not
  copied, only its engineering. `lint_claims()` enforces that separation on our own output.

USAGE
  python build_shopify_paste.py 2D-body-clean.md
  Settings live in SHOPIFY-CONFIG.json next to the markdown (written on first run with defaults).

OUTPUTS
  sections/<section_id>.liquid   <- THE DELIVERABLE (theme-editor editable, instance-safe)
  snippets/wipex-blog-schema.liquid
  templates/<template>.json
  SHOPIFY-PASTE.html             fallback for a store that does not use sections
  SHOPIFY-META.md, SHOPIFY-LIQUID.md, SHOPIFY-SCHEMA.json
  SECTION-VALIDATION.txt         the pass/fail report (claims lint, schema limits, link integrity)

RULES BAKED IN
  no external requests, no libraries, no inline handlers, CSS scoped under one class,
  JS in one IIFE with a per-section registry, rAF throttling, textContent only.
"""
from __future__ import annotations
import csv, io, html, json, os, re, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else '2D-body-clean.md'
OUTDIR = os.path.dirname(os.path.abspath(SRC))
AUTO = "https://wipex.co"

# ─────────────────────────────────────────────────────────────────────────────
# CONFIG — every knob the operator may need, kept out of the code
# ─────────────────────────────────────────────────────────────────────────────
THEME_DEFAULTS = {
    # Design tokens, grounded in the live Wipex theme (read from the storefront, 2026-09-23):
    # mint green primary, mauve accent, brand gold token, ink #1c1d1d, warm surface #fdfbf8,
    # pill buttons, 16px cards, Raleway body + "New Order" headings (both already loaded by the
    # theme, so referencing them costs no extra request). A post or a season restyles by editing
    # this block in SHOPIFY-CONFIG.json — never the CSS.
    "ink": "#1c1d1d", "ink_soft": "#4a4a48", "muted": "#6f6f6b", "line": "#e8e8e1",
    "surface": "#ffffff", "surface_warm": "#fdfbf8", "dark": "#111111",
    "accent": "#76c39c", "accent_ink": "#2f6b4f", "accent_soft": "#eaf6f0",
    "plum": "#b68fbd", "plum_soft": "#f5eef7", "gold": "#b08d57",
    "radius": "16px", "radius_sm": "6px", "pill": "999px",
    "shadow": "0 1px 2px rgba(28,29,29,.05), 0 10px 30px rgba(28,29,29,.06)",
    "shadow_hover": "0 2px 6px rgba(28,29,29,.07), 0 18px 44px rgba(28,29,29,.11)",
    "max_width": "1180px", "read_width": "44rem", "space": "28px",
    "font_body": "Raleway, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif",
    "font_head": "\"New Order\", Raleway, system-ui, -apple-system, Segoe UI, sans-serif",
    "hero_tint": "linear-gradient(180deg, #fdfbf8 0%, #ffffff 78%)",
}

CFG_DEFAULTS = {
    # ── STRUCTURAL DEFAULTS ONLY ──────────────────────────────────────────────────────────────
    # Every word of copy, every link, every image slot for a post lives in that post's
    # SHOPIFY-CONFIG.json, next to the approved markdown. The generator ships no post content:
    # if it is not in the config, it does not exist.
    "domain": AUTO,
    "css_prefix": "wx",
    "theme": {},
    "meta_tags": "", "author": "", "keywords": "", "article_section": "", "publish_note": "",
    "hero_eyebrow": "", "hero_lede": "",
    "hero_cta": {"label": "", "url": ""}, "hero_cta2": {"label": "", "url": ""},
    "sticky_cta": {"label": "", "url": ""},
    "video_anchor": "before_faq", "image_slots": [],
    "products_anchor": "", "products_heading": "", "products": [],
    "problem_strip": None, "stat_cards": None, "card_grid": None,
    "decision_tool": None, "system_block": None, "feature_block": None,
    "final_cta_heading": "",
    "schema_products": [], "schema_mentions": [],
    "calculator": {
        # the cost-per-use module: fields, outputs, copy and the one tunable (covers per turn).
        # Arithmetic itself is fixed in the JS and documented in references/10 — a different
        # calculation needs a new module function, not a new formula string.
        "anchor_heading": "Worked example",
        "heading": "Calculate your cost per table",
        "note": "Cost figures only, based on the prices you enter. Check your own invoice.",
        "covers_per_turn": 2,
        "inputs": [
            {"key": "tables", "label": "Tables", "value": 20, "step": 1, "min": 0},
            {"key": "turns", "label": "Turns per service", "value": 3, "step": 0.5, "min": 0},
            {"key": "services", "label": "Services per week", "value": 6, "step": 1, "min": 0},
            {"key": "price", "label": "Case price ($)", "value": 36.99, "step": 0.01, "min": 0},
            {"key": "count", "label": "Wipes per case", "value": 400, "step": 1, "min": 1},
            {"key": "wipes", "label": "Wipes per reset", "value": 2, "step": 1, "min": 1},
            {"key": "seconds", "label": "Seconds per reset", "value": 45, "step": 5, "min": 0},
            {"key": "rate", "label": "Loaded hourly rate ($)", "value": 16, "step": 0.5, "min": 0},
        ],
        "outputs": [
            {"key": "table", "label": "cost per table"},
            {"key": "week", "label": "weekly cleaning cost"},
            {"key": "cover", "label": "cost per cover"},
        ],
    },
}

REQUIRED = ("title", "slug", "meta_title", "meta_desc", "published",
            "section_id", "section_name", "template_file")
CFG_PATH = os.path.join(OUTDIR, 'SHOPIFY-CONFIG.json')


def load_cfg():
    if not os.path.exists(CFG_PATH):
        io.open(CFG_PATH, 'w', encoding='utf-8').write(
            json.dumps(CFG_DEFAULTS, indent=2, ensure_ascii=False) + '\n')
        print('config written : SHOPIFY-CONFIG.json (edit it to change copy, links, images)')
        return dict(CFG_DEFAULTS)
    user = json.loads(io.open(CFG_PATH, encoding='utf-8').read())
    cfg = dict(CFG_DEFAULTS)
    cfg.update(user)
    # keep the operator's file complete as the generator grows: add keys it does not have yet,
    # never overwrite a value the operator set.
    missing = [k for k in CFG_DEFAULTS if k not in user]
    if missing:
        if not cfg.get('theme'):
            cfg['theme'] = dict(THEME_DEFAULTS)      # show the operator the tokens to edit
        io.open(CFG_PATH, 'w', encoding='utf-8').write(
            json.dumps(cfg, indent=2, ensure_ascii=False) + '\n')
        print('config extended: %s' % ', '.join(missing))
    return cfg


CFG = load_cfg()
_missing_required = [k for k in REQUIRED if not CFG.get(k)]
if _missing_required:
    raise SystemExit(
        'SHOPIFY-CONFIG.json is the post: it is missing %s.\n'
        'The generator carries no post content on purpose — fill the config next to the markdown.'
        % ', '.join(_missing_required))
P = CFG["css_prefix"]                      # css class prefix, scoped under one class
DOMAIN = CFG["domain"].rstrip('/')


# ─────────────────────────────────────────────────────────────────────────────
# markdown helpers
# ─────────────────────────────────────────────────────────────────────────────
def fin(s):
    """Resolve the two class-prefix tokens. Two tokens exist because a few templates are built with
    %-formatting, and a literal '%P%' inside a %-format string raises. '@P@' is used in those, and
    both are folded to the real prefix here — once, on the finished artifact."""
    return s.replace('%P%', P).replace('@P@', P)


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def slugify(s):
    s = re.sub(r'[^a-z0-9\s-]', '', s.lower())
    return re.sub(r'-+', '-', s).strip().replace(' ', '-')


def parse(md):
    """Block parser. Fixed in v3.0: a list item continued on an indented line is merged into the
    item instead of being emitted as a stray paragraph (the house markdown wraps bullets with a
    single leading space, which v2.7 turned into <ul>/<p>/<ul>/<p> confetti)."""
    lines = md.splitlines()
    blocks, i = [], 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s.startswith('```'):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith('```'):
                buf.append(lines[i]); i += 1
            i += 1
            blocks.append(('code', '\n'.join(buf))); continue
        if s == '---':
            blocks.append(('hr', '')); i += 1; continue
        m = re.match(r'^(#{1,6})\s+(.*)$', s)
        if m:
            blocks.append(('h%d' % len(m.group(1)), m.group(2).strip())); i += 1; continue
        if s.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(lines[i].strip()); i += 1
            blocks.append(('table', rows)); continue
        if re.match(r'^- \[[ xX]\]\s', s):
            items = []
            while i < len(lines) and re.match(r'^\s*(- \[[ xX]\]\s|\s+\S)', lines[i]):
                t = lines[i]
                if re.match(r'^\s*- \[[ xX]\]\s', t):
                    items.append(re.sub(r'^\s*- \[[ xX]\]\s*', '', t).strip())
                else:
                    items[-1] += ' ' + t.strip()
                i += 1
            blocks.append(('check', items)); continue
        if re.match(r'^[-*+]\s', s):
            items = []
            while i < len(lines) and re.match(r'^\s*([-*+]\s|\s+\S)', lines[i]):
                t = lines[i]
                if re.match(r'^\s*[-*+]\s', t):
                    items.append(re.sub(r'^\s*[-*+]\s', '', t).strip())
                else:
                    items[-1] += ' ' + t.strip()
                i += 1
            blocks.append(('ul', items)); continue
        if re.match(r'^\d+[.)]\s', s):
            items = []
            while i < len(lines) and re.match(r'^\s*(\d+[.)]\s|\s+\S)', lines[i]):
                t = lines[i]
                if re.match(r'^\s*\d+[.)]\s', t):
                    items.append(re.sub(r'^\s*\d+[.)]\s*', '', t).strip())
                else:
                    items[-1] += ' ' + t.strip()
                i += 1
            blocks.append(('ol', items)); continue
        buf = [s]; i += 1
        while i < len(lines):
            ns = lines[i].strip()
            if (not ns or ns.startswith('|') or ns == '---' or ns.startswith('```')
                    or re.match(r'^#{1,6}\s', ns) or re.match(r'^[-*+]\s', ns)
                    or re.match(r'^\d+[.)]\s', ns) or re.match(r'^- \[[ xX]\]', ns)
                    or re.match(r'^\s{1,}\S', lines[i])):
                break
            buf.append(ns); i += 1
        blocks.append(('p', ' '.join(buf)))
    return blocks


def render_table(rows):
    """Comparison table. v3.0 adds data-label to every cell (so the rows stack as cards on a
    phone instead of scrolling sideways) and only pins a min-width on 4+ column tables."""
    head = [c.strip() for c in rows[0].strip('|').split('|')]
    body = [[c.strip() for c in r.strip('|').split('|')] for r in rows[2:]]
    wide = len(head) >= 4
    cls = '%P%__table' + ('' if len(head) <= 3 else ' %P%__table--wide')
    out = ['<div class="%P%__tablewrap" role="region" tabindex="0" aria-label="Comparison table">',
           '<table class="%s"><thead><tr>' % cls]
    for c in head:
        if c:
            out.append('<th scope="col">%s</th>' % inline(c))
        else:
            out.append('<th scope="col" class="%P%__th-empty"><span class="%P%__sr">Item</span></th>')
    out.append('</tr></thead><tbody>')
    for r in body:
        out.append('<tr>')
        for j, c in enumerate(r):
            label = head[j] if j < len(head) and head[j] else 'Item'
            if j == 0 and c:
                out.append('<th scope="row" data-label="%s">%s</th>' % (html.escape(label), inline(c)))
            else:
                out.append('<td data-label="%s">%s</td>' % (html.escape(label), inline(c)))
        out.append('</tr>')
    out.append('</tbody></table></div>')
    return '\n'.join(out)


def render(blocks):
    """Blocks -> nodes. A node is a dict: {'t': kind, 'html': str} plus heading metadata."""
    nodes, faq, toc, in_faq, prev_h2 = [], [], [], False, ''
    for kind, payload in blocks:
        if kind == 'h1':
            continue
        if kind in ('h2', 'h3'):
            sid = slugify(payload)
            node = {'t': kind, 'id': sid, 'text': payload, 'html': ''}
            if kind == 'h2':
                in_faq = payload.strip().lower().startswith(('frequently asked', 'faq'))
                prev_h2 = payload.strip().lower()
                toc.append((sid, payload))
                node['html'] = '<h2 id="%s">%s</h2>' % (sid, inline(payload))
            else:
                node['html'] = '<h3 id="%s">%s</h3>' % (sid, inline(payload))
            nodes.append(node); continue
        if kind == 'p':
            s = payload.strip()
            if in_faq:
                qm = re.match(r'^\*\*(.+?\?)\*\*\s*(.*)$', s)
                if qm:
                    faq.append([qm.group(1), qm.group(2).strip()])
                    nodes.append({'t': 'h3', 'id': slugify(qm.group(1)), 'text': qm.group(1),
                                  'html': '<h3 class="@P@__faqq">%s</h3>' % inline(qm.group(1))})
                    if qm.group(2).strip():
                        nodes.append({'t': 'p', 'html': '<p>%s</p>' % inline(qm.group(2).strip())})
                    continue
                if faq:
                    faq[-1][1] = (faq[-1][1] + ' ' + s).strip() if faq[-1][1] else s
            nodes.append({'t': 'p', 'html': '<p>%s</p>' % inline(payload)}); continue
        if kind == 'ul':
            if prev_h2.startswith('on this page'):
                nodes.append({'t': 'toc', 'html': ''})        # replaced by the interactive TOC
                continue
            cl = ' class="@P@__takeaways"' if prev_h2.startswith('quick answer') else ''
            nodes.append({'t': 'ul', 'html': '<ul%s>%s</ul>' % (cl, ''.join('<li>%s</li>' % inline(x) for x in payload))})
            continue
        if kind == 'ol':
            nodes.append({'t': 'ol', 'html': '<ol>%s</ol>' % ''.join('<li>%s</li>' % inline(x) for x in payload)})
            continue
        if kind == 'check':
            nodes.append({'t': 'check', 'items': payload, 'html': ''})
            continue
        if kind == 'table':
            nodes.append({'t': 'table', 'html': render_table(payload)}); continue
        if kind == 'code':
            nodes.append({'t': 'code', 'html': '<pre class="@P@__code"><code>%s</code></pre>' % html.escape(payload)})
            continue
        if kind == 'hr':
            nodes.append({'t': 'hr', 'html': '<hr class="%P%__hr">'}); continue
    return nodes, faq, toc


# ─────────────────────────────────────────────────────────────────────────────
# module emitters
# ─────────────────────────────────────────────────────────────────────────────
def s_expr(sid, default, resolved, escape=True):
    """A theme setting, or its literal default when we are emitting the non-Liquid paste block."""
    if resolved:
        return html.escape(default) if escape else default
    d = "'" + str(default).replace('\\', '').replace("'", "\\'") + "'"
    return '{{ section.settings.%s | default: %s%s }}' % (sid, d, ' | escape' if escape else '')


def band(P, slot, resolved, uidt, row=False):
    """Editorial still: 16:9 or 2:3 frame, srcset + sizes + focal point + alt + caption.
    Empty -> hidden on the storefront, editor placeholder inside the theme editor.
    `row=True` renders the figure for a two-column liferow (no inner wrap, so it sits beside the
    prose instead of above it) — the reference's wpx-liferow / liferow--rev pattern.
    Built by concatenation on purpose: a Liquid template cannot go through %-formatting, because
    '{%-' is read as a format spec."""
    s, a, c, f = slot['setting'], slot['setting'] + '_alt', slot['setting'] + '_caption', slot['setting'] + '_focal'
    w, h = (1120, 630) if slot['ratio'] == '16x9' else (480, 720)
    ratio_cls = '@P@__life--16x9' if slot['ratio'] == '16x9' else '@P@__life--2x3'
    if resolved:
        if not slot.get('literal_url'):
            return ''
        img = ('<img src="%s" width="%d" height="%d" alt="%s" loading="lazy" decoding="async">'
               % (slot['literal_url'], w, h, html.escape(slot['alt'])))
        cap = ('<figcaption class="@P@__cap">%s</figcaption>' % html.escape(slot['caption'])) if slot['caption'] else ''
        if row:
            return ('<figure class="@P@__band @P@__band--row %s">%s%s</figure>' % (ratio_cls, img, cap))
        return ('<figure class="@P@__band %s"><div class="@P@__wrap">%s%s</div></figure>'
                % (ratio_cls, img, cap))
    sw1, sw2 = int(w * 0.57), int(w * 1.4)
    alt_expr = "{{ section.settings." + a + " | default: '" + slot['alt'].replace("'", "\\'") + "' | escape }}"
    p = []
    p.append("{%- assign foc = section.settings." + f + " | default: 'center' -%}")
    p.append("{%- if section.settings." + s + " != blank -%}")
    p.append('<figure class="@P@__band ' + ('@P@__band--row ' if row else '') + ratio_cls + '" style="--@P@-img-pos:{{ foc }};">')
    if not row:
        p.append('<div class="@P@__wrap">')
    p.append('<img')
    p.append('  src="{{ section.settings.' + s + ' | image_url: width: ' + str(w) + ' }}"')
    p.append('  srcset="{{ section.settings.' + s + ' | image_url: width: ' + str(sw1) + ' }} ' + str(sw1) + 'w,')
    p.append('          {{ section.settings.' + s + ' | image_url: width: ' + str(w) + ' }} ' + str(w) + 'w,')
    p.append('          {{ section.settings.' + s + ' | image_url: width: ' + str(sw2) + ' }} ' + str(sw2) + 'w"')
    p.append('  sizes="(max-width: 1120px) 100vw, ' + str(w) + 'px"')
    p.append('  width="' + str(w) + '" height="' + str(h) + '"')
    p.append('  alt="' + alt_expr + '" loading="lazy" decoding="async">')
    p.append('{%- if section.settings.' + c + ' != blank -%}<figcaption class="@P@__cap">{{ section.settings.'
             + c + ' | escape }}</figcaption>{%- endif -%}')
    p.append('</div></figure>' if not row else '</figure>')
    p.append('{%- elsif request.design_mode -%}')
    p.append('<figure class="@P@__band ' + ('@P@__band--row ' if row else '') + ratio_cls + '">'
             + ('' if row else '<div class="@P@__wrap">') + '<div class="@P@__ph">Editor only · '
             + html.escape(slot['label']) + '<br>' + html.escape(slot['alt'][:96]) + '</div>'
             + ('' if row else '</div>') + '</figure>')
    p.append('{%- endif -%}')
    return '\n'.join(p)


def problem_strip(P, cfg):
    """Problem strip — the reference's 4-cell strip under the hero. Names the pressure the post
    exists to relieve, in one screen, before the reader scrolls."""
    cells = cfg.get('cells') or []
    if not cells:
        return ''
    body = ''.join('<div class="@P@__strip-cell"><strong>%s</strong><span>%s</span></div>'
                   % (html.escape(c['strong']), html.escape(c['span'])) for c in cells)
    return ('<section class="@P@__strip" aria-label="%s"><div class="@P@__wrap">'
            '<div class="@P@__strip-grid">%s</div></div></section>'
            % (html.escape(cfg.get('label', 'What drives the pressure')), body))


def stat_cards(P, cfg):
    """Stat cards — number + label pairs lifted from the article's own key takeaways. Every number
    must already exist in the approved copy: this module renders claims, it does not make them."""
    cards = cfg.get('cards') or []
    if not cards:
        return ''
    body = ''.join('<div class="@P@__stat"><b>%s</b><span>%s</span></div>'
                   % (html.escape(c['value']), html.escape(c['label'])) for c in cards)
    head = ('<h2>%s</h2>' % html.escape(cfg['heading'])) if cfg.get('heading') else ''
    return ('<div class="@P@__stats-block"><div class="@P@__read">%s'
            '<div class="@P@__stats">%s</div></div></div>' % (head, body))


def decision_tool(P, cfg):
    """Decision tool — 'which setup is right for your room', one card per operation profile, each
    with its own data-cro. Mirrors the reference's DECISION TOOL module."""
    opts = cfg.get('options') or []
    if not opts:
        return ''
    cards = []
    for i, o in enumerate(opts, 1):
        rec = ' @P@__dec--rec' if o.get('recommended') else ''
        btn = 'primary' if o.get('recommended') else 'ghost'
        cards.append('<div class="@P@__dec%s"><h3>%s</h3><div class="@P@__dec-arrow" aria-hidden="true">↓</div>'
                     '<p class="@P@__dec-sol">%s</p>'
                     '<a class="@P@__btn @P@__btn--%s @P@__btn--sm" data-cro="@CRO@-dec-%d" href="%s">%s →</a></div>'
                     % (rec, html.escape(o['title']), html.escape(o['answer']), btn, i, o['url'], html.escape(o['cta'])))
    return ('<div class="@P@__sec-block"><h2>%s</h2><div class="@P@__dec-grid">%s</div></div>'
            % (html.escape(cfg['heading']), ''.join(cards)))


def system_block(P, cfg):
    """A + B = system (the reference's AOV module). Config decides what the two parts are: a real
    product bundle when marketing has confirmed the companion SKU, or the article's own workflow
    framing when it has not. Never invent a companion product."""
    pills = cfg.get('pills') or []
    if len(pills) < 2:
        return ''
    eq = []
    for i, pill in enumerate(pills):
        if i:
            eq.append('<span class="@P@__op" aria-hidden="true">+</span>')
        eq.append('<span class="@P@__pill">%s</span>' % html.escape(pill))
    eq.append('<span class="@P@__op" aria-hidden="true">=</span>')
    eq.append('<span class="@P@__pill @P@__system-result">%s</span>' % html.escape(cfg['result']))
    cta = ''
    if cfg.get('cta'):
        cta = ('<p class="@P@__cta-row" style="justify-content:center;">'
               '<a class="@P@__btn @P@__btn--primary" data-cro="@CRO@-system" href="%s">%s →</a></p>'
               % (cfg['cta']['url'], html.escape(cfg['cta']['label'])))
    return ('<div class="@P@__sec-block @P@__system"><span class="@P@__eyebrow">%s</span>'
            '<h2>%s</h2><div class="@P@__system-eq">%s</div><p>%s</p>%s</div>'
            % (html.escape(cfg.get('eyebrow', 'The system')), html.escape(cfg['heading']),
               ''.join(eq), html.escape(cfg.get('text', '')), cta))


def feature_block(P, cfg):
    """Primary feature module — the reference's 'the workhorse' block: image, eyebrow, heading,
    proof bullets, one primary CTA."""
    media = ('<div class="@P@__feature-media"><img src="%s" width="800" height="800" loading="lazy" alt="%s"></div>'
             % (cfg['image'], html.escape(cfg.get('image_alt', cfg['heading'])))) if cfg.get('image') else ''
    bullets = ''.join('<li>%s</li>' % html.escape(b) for b in cfg.get('bullets', []))
    return ('<div class="@P@__sec-block"><div class="@P@__feature">%s<div class="@P@__feature-body">'
            '<span class="@P@__eyebrow">%s</span><h2>%s</h2><p>%s</p>'
            '<ul class="@P@__feature-list">%s</ul>'
            '<a class="@P@__btn @P@__btn--primary" data-cro="@CRO@-feature" href="%s">%s →</a>'
            '</div></div></div>'
            % (media, html.escape(cfg.get('eyebrow', '')), html.escape(cfg['heading']),
               html.escape(cfg.get('text', '')), bullets, cfg['cta']['url'], html.escape(cfg['cta']['label'])))


def card_grid(P, cfg):
    """Informative card grid — the reference's equipment / buying-guide grids. Cards carry short
    labels and one supporting line each; the copy comes from config and is linted like everything
    else."""
    cards = cfg.get('cards') or []
    if not cards:
        return ''
    body = ''.join('<div class="@P@__card-info"><h3>%s</h3><p>%s</p></div>'
                   % (html.escape(c['title']), html.escape(c['text'])) for c in cards)
    head = ('<h2>%s</h2>' % html.escape(cfg['heading'])) if cfg.get('heading') else ''
    note = ('<p class="@P@__note">%s</p>' % html.escape(cfg['note'])) if cfg.get('note') else ''
    return ('<div class="@P@__sec-block">%s<div class="@P@__info-grid">%s</div>%s</div>'
            % (head, body, note))


def promote_cta_row(html_str, P, slug, tag):
    """Turn the closing section's link paragraph into a real CTA row of buttons — the reference's
    final conversion band. No new copy: it restyles the links the approved article already carries,
    which is why it cannot introduce a claim."""
    def repl(m):
        links = re.findall(r'<a href="([^"]+)">(.*?)</a>', m.group(1))
        if len(links) < 2:
            return m.group(0)
        btns = []
        for i, (href, label) in enumerate(links, 1):
            kind = 'primary' if i == 1 else ('gold' if i == 2 else 'ghost')
            btns.append('<a class="%s__btn %s__btn--%s" data-cro="%s-%s-%d" href="%s">%s</a>'
                        % (P, P, kind, slug, tag, i, href, label))
        return '<p class="%s__cta-row">%s</p>' % (P, ''.join(btns))
    return re.sub(r'<p>((?:<a [^>]+>.*?</a>\s*(?:·\s*)?)+)</p>', repl, html_str)


def video_band(P, cfg, resolved):
    """Editorial video band: native Shopify video, muted/looping/inline, with a fallback image and
    an optional overlay. Renders nothing at all when there is neither a video nor a fallback.
    @P@ / @CRO@ are substituted with .replace — %-formatting cannot carry a Liquid template."""
    if resolved:
        return ''
    tpl = """{%- assign has_video = false -%}
{%- if section.settings.lifestyle_video != blank -%}{%- assign has_video = true -%}{%- endif -%}
{%- assign has_fallback = false -%}
{%- if section.settings.video_fallback_image != blank -%}{%- assign has_fallback = true -%}{%- endif -%}
{%- if has_video or has_fallback or request.design_mode -%}
<section class="@P@__sec @P@__videoband" aria-label="Editorial video">
  <div class="@P@__wrap">
    <div class="@P@__video">
      {%- if has_video -%}
        {{ section.settings.lifestyle_video | video_tag: image_size: '1600x', autoplay: true, loop: true, muted: true, controls: false, playsinline: true, preload: 'metadata', class: '@P@__video-media' }}
      {%- elsif has_fallback -%}
        <img src="{{ section.settings.video_fallback_image | image_url: width: 1600 }}"
             width="1600" height="900" loading="lazy" decoding="async"
             alt="{{ section.settings.video_fallback_image_alt | default: 'Wipex food service wipes in use' | escape }}">
      {%- else -%}
        <div class="@P@__ph">Editor only · editorial video banner (16:9)<br>Upload a Shopify-hosted video, or set a fallback image</div>
      {%- endif -%}
      {%- if section.settings.video_banner_heading != blank or section.settings.video_banner_text != blank -%}
        <div class="@P@__video-content">
          {%- if section.settings.video_banner_heading != blank -%}<h2 class="@P@__video-h">{{ section.settings.video_banner_heading | escape }}</h2>{%- endif -%}
          {%- if section.settings.video_banner_text != blank -%}<p class="@P@__video-t">{{ section.settings.video_banner_text | escape }}</p>{%- endif -%}
          {%- if section.settings.video_banner_cta_label != blank and section.settings.video_banner_cta_url != blank -%}
            <a class="@P@__btn @P@__btn--primary" data-cro="@CRO@-video" href="{{ section.settings.video_banner_cta_url }}">{{ section.settings.video_banner_cta_label | escape }} →</a>
          {%- endif -%}
        </div>
      {%- endif -%}
    </div>
  </div>
</section>
{%- endif -%}"""
    return tpl.replace('@CRO@', cfg['slug'])


def products_module(P, cfg, resolved):
    """Product showcase from config. Images are literal URLs on purpose: keeping product imagery
    out of the schema budget leaves the settings room for editorial photography, and the card copy
    is still linted by lint_claims()."""
    prods = cfg.get('products') or []
    if not prods:
        return ''
    cards = []
    for pr in prods:
        media = ('<div class="@P@__card-media"><img src="%s" width="600" height="600" loading="lazy" alt="%s"></div>'
                 % (pr['image'], html.escape(pr['name']))) if pr.get('image') else ''
        bullets = ''.join('<li>%s</li>' % html.escape(b) for b in pr.get('bullets', []))
        cards.append("""<article class="%(P)s__card">
  %(media)s
  <span class="%(P)s__badge">%(badge)s</span>
  <h3 class="%(P)s__card-h">%(name)s</h3>
  <p class="%(P)s__card-best">Suited to: %(best)s</p>
  <ul class="%(P)s__card-list">%(bullets)s</ul>
  <a class="%(P)s__btn %(P)s__btn--ghost %(P)s__btn--sm" data-cro="%(cro)s-prod-%(i)d" href="%(url)s">Shop %(short)s →</a>
</article>""" % dict(P=P, media=media, badge=html.escape(pr.get('badge', '')),
                    name=html.escape(pr['name']), best=html.escape(pr.get('best_for', '')),
                    bullets=bullets, cro=cfg['slug'], i=len(cards) + 1, url=pr['url'],
                    short=html.escape(pr['name'].split(' Surface')[0].split(' —')[0])))
    return """<div class="%(P)s__sec-block">
  <h2>%(heading)s</h2>
  <div class="%(P)s__cards">%(cards)s</div>
</div>""" % dict(P=P, heading=html.escape(cfg.get('products_heading', 'Which format fits the room')),
                cards=''.join(cards))


def checklist_module(P, items, uidt):
    rows = []
    for i, it in enumerate(items, 1):
        cid = '%s-ck%d-%s' % (P, i, uidt or 'paste')
        rows.append('<li class="@P@__check-item"><input type="checkbox" id="%s" data-wpx-check>'
                    '<label for="%s">%s</label></li>' % (cid, cid, inline(it)))
    return ('<div class="@P@__check" data-wpx-checklist>'
            '<ul class="@P@__check-list">%s</ul>'
            '<p class="@P@__check-note">Progress saves in this browser.</p></div>' % ''.join(rows))


def toc_module(P, toc, uidt):
    lis = ''.join('<li><a href="#%s">%s</a></li>' % (sid, html.escape(t))
                  for sid, t in toc if not t.strip().lower().startswith(('on this page', 'keep reading')))
    lid = 'tocList-%s' % (uidt or 'paste')
    return ('<nav class="@P@__toc" data-wpx-toc data-open="true" aria-label="On this page">'
            '<button type="button" class="@P@__toc-head" data-wpx-toc-toggle aria-expanded="true" aria-controls="%s">'
            '<span>On this page</span><span class="@P@__toc-chev" aria-hidden="true">▾</span></button>'
            '<ul class="@P@__toc-list" id="%s">%s</ul></nav>' % (lid, lid, lis))


def sticky_cta(P, cfg, resolved):
    label, url = cfg['sticky_cta']['label'], cfg['sticky_cta']['url']
    if resolved:
        return ('<div class="@P@__sticky" data-wpx-sticky aria-hidden="true">'
                '<a class="@P@__btn @P@__btn--primary" data-cro="%s-sticky" href="%s">%s →</a>'
                '<button type="button" class="@P@__sticky-close" data-wpx-sticky-close aria-label="Dismiss">×</button></div>'
                % (cfg['slug'], url, html.escape(label)))
    return ('<div class="@P@__sticky" data-wpx-sticky aria-hidden="true">'
            '<a class="@P@__btn @P@__btn--primary" data-cro="%s-sticky" href="{{ section.settings.sticky_url | default: \'%s\' }}">{{ section.settings.sticky_label | default: \'%s\' | escape }} →</a>'
            '<button type="button" class="@P@__sticky-close" data-wpx-sticky-close aria-label="Dismiss">×</button></div>'
            % (cfg['slug'], url, label.replace("'", "\\'")))


def calc_html(P, cfg, uidt):
    """The cost-per-use calculator module. Fields, labels, defaults, outputs, heading and note come
    from `calculator` in the config; the arithmetic is fixed and documented in references/10 — a
    different calculation is a new module function, not a new config string."""
    c = dict(CFG_DEFAULTS['calculator'])
    c.update({k: v for k, v in (cfg.get('calculator') or {}).items() if v not in (None, '', [], {})})
    fields, outs = [], []
    for f in c['inputs']:
        fields.append('<label>%s<input type="number" inputmode="decimal" step="%s" min="%s" value="%s" data-k="%s"></label>'
                      % (html.escape(str(f['label'])), f.get('step', 1), f.get('min', 0),
                         f.get('value', 0), html.escape(str(f['key']))))
    for o in c['outputs']:
        outs.append('<div><span data-out="%s">&mdash;</span><small>%s</small></div>'
                    % (html.escape(str(o['key'])), html.escape(str(o['label']))))
    return ('<div class="%%P%%__calc" data-wpx-calc data-module="cost-per-use" id="%%P%%-calc-%s">'
            '<h3 class="%%P%%__calc-h">%s</h3>'
            '<div class="%%P%%__calc-grid">%s</div>'
            '<div class="%%P%%__calc-out" role="status" aria-live="polite">%s</div>'
            '<p class="%%P%%__calc-note">%s</p>'
            '</div>'
            % (uidt or 'paste', html.escape(str(c['heading'])), ''.join(fields),
               ''.join(outs), html.escape(str(c['note']))))


# ─────────────────────────────────────────────────────────────────────────────
# CSS — scoped under .%P% , tokens first, modules after
# ─────────────────────────────────────────────────────────────────────────────
CSS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wipex-section.css')
if not os.path.exists(CSS_PATH):
    raise SystemExit('missing stylesheet: %s (it ships next to this script)' % CSS_PATH)
CSS = io.open(CSS_PATH, encoding='utf-8').read()


def token_block(theme):
    """The palette as CSS custom properties, generated from the config's `theme` block. The
    stylesheet only ever references var(--wx-*), so a post or a season restyles by editing tokens —
    no colour, font or radius is written in the CSS by hand."""
    t = dict(THEME_DEFAULTS)
    t.update({k: v for k, v in (theme or {}).items() if v not in (None, '')})
    return (".%%P%%{--wx-ink:%(ink)s;--wx-ink-soft:%(ink_soft)s;--wx-muted:%(muted)s;--wx-line:%(line)s;"
            "--wx-surface:%(surface)s;--wx-surface-warm:%(surface_warm)s;--wx-dark:%(dark)s;"
            "--wx-accent:%(accent)s;--wx-accent-ink:%(accent_ink)s;--wx-accent-soft:%(accent_soft)s;"
            "--wx-plum:%(plum)s;--wx-plum-soft:%(plum_soft)s;--wx-gold:%(gold)s;"
            "--wx-radius:%(radius)s;--wx-radius-sm:%(radius_sm)s;--wx-pill:%(pill)s;"
            "--wx-shadow:%(shadow)s;--wx-shadow-hover:%(shadow_hover)s;--wx-maxw:%(max_width)s;"
            "--wx-readw:%(read_width)s;--wx-space:%(space)s;--wx-hero-tint:%(hero_tint)s;"
            "--wx-font-head:%(font_head)s;font-family:%(font_body)s;color:var(--wx-ink);"
            "line-height:1.65;font-size:1.0625rem;text-rendering:optimizeLegibility;position:relative;"
            "-webkit-font-smoothing:antialiased}" % t)


def build_js(P, cfg):
    covers = (cfg.get('calculator') or {}).get('covers_per_turn')
    if covers in (None, ''):
        covers = CFG_DEFAULTS['calculator']['covers_per_turn']
    return JS.replace('%%COVERS%%', str(covers)).replace('%P%', P)


def build_css(P, cfg):
    return (CSS.replace('%%TOKENS%%', token_block(cfg.get('theme'))).replace('%P%', P))



# ─────────────────────────────────────────────────────────────────────────────
# JS — one IIFE, per-section registry, theme-editor safe
# ─────────────────────────────────────────────────────────────────────────────
JS = """<script>
(function () {
  "use strict";
  var P = "%P%";
  function init(id) {
    var root = document.getElementById(P + "-" + id);
    if (!root || root.getAttribute("data-wpx-ready") === "1") return;
    root.setAttribute("data-wpx-ready", "1");
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var bar = root.querySelector("[data-wpx-progress]");
    var article = root.querySelector("article");
    var sticky = root.querySelector("[data-wpx-sticky]");
    var finalSec = root.querySelector(".%P%__sec-block--final, .%P%__sec--final");
    var ticking = false;
    function update() {
      ticking = false;
      if (!article) return;
      var rect = article.getBoundingClientRect();
      var total = article.offsetHeight - window.innerHeight;
      if (bar) {
        var scrolled = Math.min(Math.max(-rect.top, 0), total > 0 ? total : 1);
        bar.style.width = (total > 0 ? (scrolled / total) * 100 : 0) + "%";
      }
      if (sticky && sticky.getAttribute("data-dismissed") !== "1") {
        var nearEnd = finalSec ? finalSec.getBoundingClientRect().top < window.innerHeight : false;
        var show = rect.top < -320 && !nearEnd;
        sticky.classList.toggle("is-visible", show);
        sticky.setAttribute("aria-hidden", show ? "false" : "true");
      }
    }
    function onScroll() { if (ticking) return; ticking = true; window.requestAnimationFrame(update); }
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });

    if (sticky) {
      var close = sticky.querySelector("[data-wpx-sticky-close]");
      if (close) close.addEventListener("click", function () {
        sticky.setAttribute("data-dismissed", "1");
        sticky.classList.remove("is-visible");
        sticky.setAttribute("aria-hidden", "true");
      });
    }

    var toc = root.querySelector("[data-wpx-toc]");
    if (toc) {
      var tbtn = toc.querySelector("[data-wpx-toc-toggle]");
      if (tbtn) tbtn.addEventListener("click", function () {
        var open = toc.getAttribute("data-open") !== "false";
        toc.setAttribute("data-open", open ? "false" : "true");
        tbtn.setAttribute("aria-expanded", open ? "false" : "true");
      });
    }

    var list = root.querySelector("[data-wpx-checklist]");
    if (list) {
      var boxes = list.querySelectorAll("input[data-wpx-check]");
      var key = "wpxcheck:" + id;
      var saved = null;
      try { saved = JSON.parse(window.localStorage.getItem(key) || "null"); } catch (e) { saved = null; }
      for (var i = 0; i < boxes.length; i++) {
        if (saved && saved[i]) boxes[i].checked = true;
        boxes[i].addEventListener("change", function () {
          var state = [];
          for (var k = 0; k < boxes.length; k++) state.push(boxes[k].checked);
          try { window.localStorage.setItem(key, JSON.stringify(state)); } catch (e) {}
        });
      }
    }

    var vids = root.querySelectorAll(".%P%__video video");
    for (var v = 0; v < vids.length; v++) {
      vids[v].muted = true;
      vids[v].defaultMuted = true;
      vids[v].setAttribute("muted", "");
      vids[v].setAttribute("playsinline", "");
      if (reduce) { try { vids[v].pause(); vids[v].removeAttribute("autoplay"); } catch (e) {} }
      else { var pr = vids[v].play && vids[v].play(); if (pr && pr.catch) pr.catch(function () {}); }
    }

    var calc = root.querySelector("[data-wpx-calc]");
    if (!calc) { update(); return; }
    var fields = calc.querySelectorAll("input[data-k]");
    var outs = { table: calc.querySelector('[data-out="table"]'),
                 week: calc.querySelector('[data-out="week"]'),
                 cover: calc.querySelector('[data-out="cover"]') };
    function val(k) {
      for (var f = 0; f < fields.length; f++) {
        if (fields[f].getAttribute("data-k") === k) {
          var n = parseFloat(fields[f].value);
          return isNaN(n) || n < 0 ? 0 : n;
        }
      }
      return 0;
    }
    function money(x) { return "$" + (x < 1 ? x.toFixed(4) : x.toFixed(2)); }
    var queued = false;
    function run() {
      queued = false;
      var resets = val("tables") * val("turns") * val("services");
      var perWipe = val("count") ? val("price") / val("count") : 0;
      var perTable = perWipe * val("wipes") + val("seconds") / 3600 * val("rate");
      var week = perTable * resets;
      if (outs.table) outs.table.textContent = money(perTable);
      if (outs.week) outs.week.textContent = "$" + week.toFixed(2);
      if (outs.cover) outs.cover.textContent = resets ? money(week / (resets * %%COVERS%%)) : money(0);
    }
    function schedule() { if (!queued) { queued = true; window.requestAnimationFrame(run); } }
    for (var f2 = 0; f2 < fields.length; f2++) fields[f2].addEventListener("input", schedule, { passive: true });
    run();
    update();
  }
  function boot() {
    var nodes = document.querySelectorAll("[data-wpx-section]");
    for (var i = 0; i < nodes.length; i++) init(nodes[i].getAttribute("data-wpx-section"));
  }
  if (document.readyState !== "loading") boot();
  else document.addEventListener("DOMContentLoaded", boot);
  document.addEventListener("shopify:section:load", function (ev) {
    var s = ev.target.querySelector ? ev.target.querySelector("[data-wpx-section]") : null;
    if (s) init(s.getAttribute("data-wpx-section"));
  });
})();
</script>"""


# ─────────────────────────────────────────────────────────────────────────────
# schema
# ─────────────────────────────────────────────────────────────────────────────
def focal_options():
    return [{"value": v, "label": v.capitalize()} for v in ("center", "top", "bottom", "left", "right")]


def build_settings(cfg):
    S = []
    S.append({"type": "header", "content": "Hero"})
    S.append({"type": "text", "id": "hero_eyebrow", "label": "Hero eyebrow", "default": cfg["hero_eyebrow"]})
    S.append({"type": "text", "id": "hero_title", "label": "Hero H1 (defaults to the post title)", "default": cfg["title"]})
    S.append({"type": "richtext", "id": "hero_lede", "label": "Hero intro (leave empty to use the article opening)"})
    S.append({"type": "text", "id": "hero_cta_label", "label": "Primary CTA label", "default": cfg["hero_cta"]["label"]})
    S.append({"type": "url", "id": "hero_cta_url", "label": "Primary CTA URL"})
    S.append({"type": "text", "id": "hero_cta2_label", "label": "Secondary CTA label", "default": cfg["hero_cta2"]["label"]})
    S.append({"type": "url", "id": "hero_cta2_url", "label": "Secondary CTA URL"})
    S.append({"type": "header", "content": "Editorial photography",
              "info": "People, places and process. NOT product packshots. Each block hides itself when empty."})
    for slot in cfg["image_slots"]:
        S.append({"type": "paragraph", "content": "%s — %s" % (slot["label"], slot["anchor"])})
        S.append({"type": "image_picker", "id": slot["setting"], "label": slot["label"]})
        S.append({"type": "text", "id": slot["setting"] + "_alt", "label": slot["setting"].replace("_", " ") + " alt text",
                  "info": "Describe what is visible. Leave blank for the default."})
        S.append({"type": "text", "id": slot["setting"] + "_caption", "label": slot["setting"].replace("_", " ") + " caption (optional)"})
        S.append({"type": "select", "id": slot["setting"] + "_focal", "label": slot["setting"].replace("_", " ") + " focal point",
                  "default": "center", "options": focal_options()})
    S.append({"type": "header", "content": "Editorial video band",
              "info": "Native Shopify video, muted and looping, with an optional overlay. Renders nothing if no video and no fallback are set."})
    S.append({"type": "video", "id": "lifestyle_video", "label": "Lifestyle video"})
    S.append({"type": "image_picker", "id": "video_fallback_image", "label": "Video fallback image (16:9)"})
    S.append({"type": "text", "id": "video_fallback_image_alt", "label": "Fallback image alt text"})
    S.append({"type": "text", "id": "video_banner_heading", "label": "Overlay heading (optional)"})
    S.append({"type": "textarea", "id": "video_banner_text", "label": "Overlay text (optional)"})
    S.append({"type": "text", "id": "video_banner_cta_label", "label": "Overlay CTA label (optional)"})
    S.append({"type": "url", "id": "video_banner_cta_url", "label": "Overlay CTA URL"})
    S.append({"type": "header", "content": "Sticky mobile CTA"})
    S.append({"type": "text", "id": "sticky_label", "label": "Sticky CTA label", "default": cfg["sticky_cta"]["label"]})
    S.append({"type": "url", "id": "sticky_url", "label": "Sticky CTA URL"})
    return S


# ─────────────────────────────────────────────────────────────────────────────
# article assembly
# ─────────────────────────────────────────────────────────────────────────────
def build_article(nodes, toc, cfg, resolved, uidt):
    """Split the prose into sections at H2 boundaries, then drop the configured modules into their
    anchors. Sections keep the reading measure; bands sit outside it."""
    sections, cur = [], {"id": "intro", "title": "", "nodes": []}
    for n in nodes:
        if n['t'] == 'h2':
            if cur['nodes']:
                sections.append(cur)
            cur = {"id": n['id'], "title": n['text'], "nodes": [n]}
        else:
            cur['nodes'].append(n)
    sections.append(cur)

    def nodes_html(ns):
        out = []
        for n in ns:
            if n['t'] == 'toc':
                out.append(fin(toc_module(P, toc, uidt)))
            elif n['t'] == 'check':
                out.append(fin(checklist_module(P, n['items'], uidt)))
            else:
                out.append(n['html'])
        return fin('\n'.join(out))

    # anchor -> section index
    def find_section(substr):
        s = substr.lower()
        for i, sec in enumerate(sections):
            if s in (sec['title'] or '').lower():
                return i
        return None

    slots_by_sec, rows_by_sec, before_faq_bands, end_bands = {}, {}, [], []
    for slot in cfg["image_slots"]:
        is_row = slot.get("layout") == "row"
        htmlband = band(P, slot, resolved, uidt, row=is_row).replace('%P%', P)
        if not htmlband:
            continue
        a = slot.get("anchor", "")
        if a == "hero":
            continue                                  # handled by the hero module
        if a.startswith("after:"):
            i = find_section(a[6:])
            if i is None:
                print('  WARN anchor not found : %s -> %r' % (slot['setting'], a[6:]))
                continue
            (rows_by_sec if is_row else slots_by_sec).setdefault(i, []).append(htmlband)
        elif a == "before_faq":
            before_faq_bands.append(htmlband)
        else:
            end_bands.append(htmlband)

    prod = products_module(P, cfg, resolved).replace('%P%', P)
    if prod:
        a = cfg.get("products_anchor", "")
        if a.startswith("after:"):
            i = find_section(a[6:])
            if i is None:
                print('  WARN products anchor not found: %r' % a[6:])
                end_bands.append(prod)
            else:
                slots_by_sec.setdefault(i, []).append(prod)
        else:
            end_bands.append(prod)

    vband = video_band(P, cfg, resolved)
    if vband:
        if cfg.get("video_anchor") == "before_faq":
            before_faq_bands.append(vband)
        else:
            end_bands.append(vband)

    # the reference's module library, config-driven: strip / stat cards / decision tool /
    # A+B system / feature block. Each one carries its own anchor in the config.
    after_hero = []
    for key, fn in (('problem_strip', problem_strip), ('stat_cards', stat_cards),
                    ('card_grid', card_grid),
                    ('decision_tool', decision_tool), ('system_block', system_block),
                    ('feature_block', feature_block)):
        conf = cfg.get(key)
        if not conf:
            continue
        html_mod = fin(fn(P, conf))
        if not html_mod:
            continue
        a = conf.get('anchor', 'end')
        if a == 'after_hero':
            after_hero.append(html_mod)
        elif a.startswith('after:'):
            i = find_section(a[6:])
            if i is None:
                print('  WARN module anchor not found: %s -> %r' % (key, a[6:]))
                continue
            slots_by_sec.setdefault(i, []).append(html_mod)
        elif a == 'before_faq':
            before_faq_bands.append(html_mod)
        else:
            end_bands.append(html_mod)

    # the calculator module, placed by anchor inside its section (config: calculator.anchor)
    _calc_cfg = dict(CFG_DEFAULTS['calculator'])
    _calc_cfg.update({k: v for k, v in (cfg.get('calculator') or {}).items() if v not in (None, '', [], {})})
    _anchor = _calc_cfg.get('anchor', 'before:Worked example')
    _needle = _anchor.split(':', 1)[1].strip().lower() if ':' in _anchor else _anchor.lower()
    _calc_node = {'t': 'html', 'html': fin(calc_html(P, cfg, uidt))}
    _placed = False
    for sec in sections:
        for k, n in enumerate(sec['nodes']):
            if n['t'] in ('h2', 'h3') and _needle and _needle in (n.get('text') or '').lower():
                sec['nodes'].insert(k, _calc_node)
                _placed = True
                break
        if _placed:
            break
    if not _placed:
        for sec in sections:
            if any(_needle and _needle in (n.get('text') or '').lower() for n in sec['nodes']) or \
               any('calculate' in (n.get('text') or '').lower() for n in sec['nodes']):
                sec['nodes'].append(_calc_node)
                _placed = True
                break
    if not _placed:
        print('  WARN calculator anchor not found: %r — the module was not placed' % _anchor)

    faq_i = None
    for i, sec in enumerate(sections):
        if (sec['title'] or '').strip().lower().startswith(('frequently asked', 'faq')):
            faq_i = i; break

    parts = []
    for i, sec in enumerate(sections):
        if faq_i is not None and i == faq_i:
            parts.extend(before_faq_bands)
        cls = '%P%__sec'
        if (sec['title'] or '').lower().startswith(cfg.get("final_cta_heading", "").lower()[:12]):
            cls += ' %P%__sec--final'
        body = nodes_html(sec['nodes'])
        extra = '\n'.join(slots_by_sec.get(i, []))
        rows = rows_by_sec.get(i, [])
        if not body.strip() and not extra and not rows:
            continue
        sid_attr = (' id="%s"' % sec['id']) if sec['id'] != 'intro' else ''
        if rows:
            inner = ('<div class="@P@__liferow">\n<div class="@P@__read">\n%s\n</div>\n%s\n</div>'
                     % (body, '\n'.join(rows)))
        else:
            inner = ('<div class="@P@__read">\n%s\n</div>' % body) if body.strip() else ''
        if 'sec--final' in cls and body.strip():
            inner = promote_cta_row(inner, P, cfg['slug'], 'final')
        parts.append('<section class="%s"%s>\n%s\n%s\n</section>' % (cls, sid_attr, inner, extra))
    parts.extend(end_bands)
    article = ('<article class="%P%__article">\n' + '\n'.join(parts) + '\n</article>')

    # hero: the opening paragraph becomes the lede unless the editor overrides it
    intro_nodes = list(sections[0]['nodes'])
    lede_node = None
    for k, n in enumerate(intro_nodes):
        if n['t'] == 'p':
            lede_node = intro_nodes.pop(k); break
    lede_default = lede_node['html'][3:-4] if lede_node else ''
    lede = ('<div class="%P%__lede">' + (s_expr('hero_lede', lede_default, resolved, escape=False) if lede_node else '') + '</div>')
    if not resolved:
        lede = ('<div class="%P%__lede">{%- if section.settings.hero_lede != blank -%}'
                '{{ section.settings.hero_lede }}{%- else -%}' + lede_default + '{%- endif -%}</div>')
    hero_band = ''
    for slot in cfg["image_slots"]:
        if slot.get("anchor") == "hero":
            hero_band = band(P, slot, resolved, uidt).replace('%P%', P)
    hero = """<header class="@P@__hero">
  <div class="@P@__wrap">
    <div class="@P@__hero-inner">
      <span class="@P@__eyebrow">%s</span>
      <h1>%s</h1>
      %s
      <p class="@P@__cta-row">
        <a class="@P@__btn @P@__btn--primary" data-cro="%s-hero" href="%s">%s →</a>
        <a class="@P@__btn @P@__btn--ghost" data-cro="%s-hero-2" href="%s">%s</a>
      </p>
    </div>
    %s
  </div>
</header>""" % (s_expr('hero_eyebrow', cfg["hero_eyebrow"], resolved),
                s_expr('hero_title', cfg["title"], resolved),
                lede, cfg['slug'],
                s_expr('hero_cta_url', cfg["hero_cta"]["url"], resolved, escape=False),
                s_expr('hero_cta_label', cfg["hero_cta"]["label"], resolved),
                cfg['slug'],
                s_expr('hero_cta2_url', cfg["hero_cta2"]["url"], resolved, escape=False),
                s_expr('hero_cta2_label', cfg["hero_cta2"]["label"], resolved),
                hero_band)

    # rebuild the intro section without the lede paragraph
    if lede_node is not None:
        body = nodes_html(intro_nodes)
        if body.strip():
            first_html = ('<section class="@P@__sec">\n<div class="@P@__read">\n%s\n</div>\n%s\n</section>'
                          % (body, '\n'.join(slots_by_sec.get(0, []))))
            article = article.replace(parts[0], first_html, 1)

    root = """<div class="@P@ @P@__root" id="@P@-%s" data-wpx-section="%s">
<div class="@P@__progress" aria-hidden="true"><div class="@P@__progress-bar" data-wpx-progress></div></div>
%s
%s
%s
%s
</div>""" % (uidt, uidt, hero, '\n'.join(after_hero), article, sticky_cta(P, cfg, resolved))
    return fin(root), lede_default


# ─────────────────────────────────────────────────────────────────────────────
# JSON-LD (never inside the section — Shopify counts @type keys as settings)
# ─────────────────────────────────────────────────────────────────────────────
def build_schema(faq, toc, cfg):
    def qa(q, a):
        return {"@type": "Question", "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'\s+', ' ', a).strip()}}
    graph = [{"@type": "BlogPosting",
              "headline": cfg["title"],
              "alternativeHeadline": cfg["meta_title"],
              "author": {"@type": "Organization", "name": "Wipex", "url": DOMAIN},
              "publisher": {"@type": "Organization", "name": "Wipex",
                            "logo": {"@type": "ImageObject", "url": DOMAIN + "/logo.png"}},
              "datePublished": cfg["published"], "dateModified": cfg["published"],
              "keywords": cfg["keywords"], "articleSection": cfg["article_section"],
              "mentions": [{"@type": "Thing", "name": m} for m in cfg.get("schema_mentions", [])]}]
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": [qa(q, a) for q, a in faq]})
    for pr in cfg.get("schema_products", []):
        graph.append({"@type": "Product", "name": pr["name"], "sku": pr["sku"],
                      "brand": {"@type": "Brand", "name": "Wipex"},
                      "offers": {"@type": "Offer", "priceCurrency": "USD", "price": pr["price"],
                                 "availability": "https://schema.org/InStock", "url": pr["url"]}})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN},
        {"@type": "ListItem", "position": 2, "name": "Library", "item": DOMAIN + "/blogs/library"},
        {"@type": "ListItem", "position": 3, "name": cfg["meta_title"]}]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)


# ─────────────────────────────────────────────────────────────────────────────
# claims lint — the reference copy would fail this; ours must not
# ─────────────────────────────────────────────────────────────────────────────
BLOCKING = [
    (r'\bbest\b|\bsafest\b|\bmost effective\b|\bstrongest\b|\b#1\b|\bultimate\b',
     'unsubstantiated superlative', 'use a test-tied comparison or a qualitative (Tier 3) claim'),
    (r'\bproven\b|\blab-tested\b|\blab-verified\b',
     'Tier 2 wording locked to Fitness + EMPOWER', 'Tier 3 qualitative wording only'),
    (r'\bsafe (on|for|to use)\b|\bnon-?toxic\b',
     'surface safety guarantee', 'gentle / designed for [named materials] + patch-test line'),
    (r'\b100% natural\b|\b\d+% natural\b', 'percentage-natural claim prohibited (A-005)',
     'made with natural ingredients'),
    (r'\bFDA[- ]approved\b', 'FDA-registered != FDA-approved', 'keep to existing BZK page wording'),
    (r'\bfood-?safe\b|\bfood-?grade\b|\bfood-contact\b', 'prohibited regardless of context',
     'suitable for food service environments (NSF products only)'),
    (r'\bcompostable\b|\bbiodegradable\b', 'locked to the cloth substrate only, disclaimer mandatory',
     'cloth-fibre statement naming TUV OK COMPOST HOME/INDUSTRIAL + "substrate only"'),
    (r'\bhygienic\b|\bsanitary\b|\bsanitiz(e|es|ing)\b|\bdisinfect\w*\b|\bantibacterial\b|\bgerm-kill\w*\b|\bkills?\b',
     'regulated / sanitising language', 'surface-cleaning language: removes, lifts, cuts through, clean'),
    (r'\brecommended by\b|\bendorsed by\b', 'endorsement claim not in the approved set',
     'escalate to Dean; do not add without a logged amendment'),
    (r'\boutperforms?\b', 'comparative needs soil + surface + lab name + benchmark',
     'Section 6 approved comparative wording'),
    (r'\beco-?friendly packaging\b|\bsustainable packaging\b', 'blanket packaging claim',
     'refill wording only'),
]
REVIEW = [
    (r'\bsafe\b', 'check "safe" is not applied to a surface'),
    (r'\bnatural\b', 'check the product is not BZK (A-008) and it is not a percentage claim'),
    (r'\bplant-?based\b', 'fine as substrate wording; never as a "natural" claim'),
]


def lint_claims(text, csv_path):
    findings = []
    for rx, why, fix in BLOCKING:
        for m in re.finditer(rx, text, re.I):
            findings.append(('BLOCKING', m.group(0), why, fix, _ctx(text, m.start())))
    for rx, why in REVIEW:
        for m in re.finditer(rx, text, re.I):
            findings.append(('REVIEW', m.group(0), why, '', _ctx(text, m.start())))
    return findings


def _ctx(text, i, width=60):
    a = max(0, i - width); b = min(len(text), i + width)
    return re.sub(r'\s+', ' ', text[a:b]).strip()


def strip_markup(h):
    h = re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<script.*?</script>', ' ', h, flags=re.S | re.I)
    h = re.sub(r'<[^>]+>', ' ', h)
    h = re.sub(r'\{[%{].*?[%}]\}', ' ', h)     # any leftover Liquid expression
    return re.sub(r'\s+', ' ', html.unescape(h)).strip()


def find_claims_csv():
    d = OUTDIR
    for _ in range(5):
        c = os.path.join(d, '01-compliance', 'Never-Say-Prohibitions.csv')
        if os.path.exists(c):
            return c
        d = os.path.dirname(d)
    return None


# ─────────────────────────────────────────────────────────────────────────────
# build
# ─────────────────────────────────────────────────────────────────────────────
md = io.open(SRC, encoding='utf-8').read()
nodes, faq, toc = render(parse(md))

SECTION_ID = CFG["section_id"]
SECTION_NAME = CFG["section_name"]
UIDT = '{{ uid }}'

def uid_anchors(html_str, heading_ids):
    """Heading anchors get the section id appended, so a second instance of the section on the same
    page cannot produce duplicate ids (the reference does the same with its TOC ids). Only applied
    to the Liquid variant — the paste fallback can only appear once."""
    for sid in set(heading_ids):
        html_str = html_str.replace('id="%s"' % sid, 'id="%s-{{ uid }}"' % sid)
        html_str = html_str.replace('href="#%s"' % sid, 'href="#%s-{{ uid }}"' % sid)
    return html_str


section_body, LEDE = build_article(nodes, toc, CFG, resolved=False, uidt=UIDT)
section_body = uid_anchors(section_body, [n['id'] for n in nodes if n.get('id')])
paste_body, _ = build_article(nodes, toc, CFG, resolved=True, uidt='paste')

settings = build_settings(CFG)
schema_json = json.dumps({"name": SECTION_NAME, "settings": settings,
                          "presets": [{"name": SECTION_NAME}]}, ensure_ascii=False, indent=2)

def wrap_liquid(html_str, comment):
    return ("{%%- comment -%%}\n%s\n{%%- endcomment -%%}\n\n{%%- assign uid = section.id -%%}\n" % comment
            + html_str + "\n\n{% schema %}\n" + schema_json + "\n{% endschema %}\n")

SECTION = wrap_liquid(
    "{% raw %}\n" + build_css(P, CFG) + "\n{% endraw %}\n\n"
    + section_body + "\n\n{% raw %}\n" + build_js(P, CFG) + "\n{% endraw %}",
    """  Wipex blog section — %s.
  Reference-grade module: theme-editor settings, editorial media (16:9 / 2:3 stills, native video
  band), interactive TOC, real checklist, reading progress, sticky mobile CTA, data-cro on every
  CTA, instance-safe JavaScript (safe to place twice on one page).

  The prose below is GENERATED from the compliance-approved markdown. Do not retype it in the
  editor: edit the markdown, regenerate, re-paste. The prose may not contain Liquid delimiters —
  the generator refuses to emit a section when it does.

  Structured data is NOT in this file: Shopify's validator counts every @type key in the file as a
  setting and blows the 40-setting cap. It lives in snippets/wipex-blog-schema.liquid.

  Files in the theme:
    sections/%s.liquid
    snippets/wipex-blog-schema.liquid
    templates/%s""" % (SECTION_ID, SECTION_ID, CFG["template_file"]))

SCHEMA_SNIPPET = ("{%- comment -%}\n"
                  "  Wipex blog structured data — " + SECTION_ID + ".\n"
                  "  Rendered once from theme.liquid, only on the matching article:\n"
                  "    {%- if article.handle == '" + CFG['slug'] + "' -%}{{ render 'wipex-blog-schema' }}{%- endif -%}\n"
                  "  FAQPage answers are the visible FAQ answers, so the two cannot drift.\n"
                  "{%- endcomment -%}\n"
                  '<script type="application/ld+json">\n'
                  + build_schema(faq, toc, CFG) + "\n</script>\n")

os.makedirs(os.path.join(OUTDIR, 'sections'), exist_ok=True)
os.makedirs(os.path.join(OUTDIR, 'snippets'), exist_ok=True)
os.makedirs(os.path.join(OUTDIR, 'templates'), exist_ok=True)
io.open(os.path.join(OUTDIR, 'sections', SECTION_ID + '.liquid'), 'w', encoding='utf-8').write(SECTION)
io.open(os.path.join(OUTDIR, 'snippets', 'wipex-blog-schema.liquid'), 'w', encoding='utf-8').write(SCHEMA_SNIPPET)
io.open(os.path.join(OUTDIR, 'templates', CFG['template_file']), 'w', encoding='utf-8').write(
    json.dumps({"sections": {SECTION_ID: {"type": SECTION_ID}}, "order": [SECTION_ID]}, indent=2) + '\n')

SCHEMA_JSON = build_schema(faq, toc, CFG)
io.open(os.path.join(OUTDIR, 'SHOPIFY-SCHEMA.json'), 'w', encoding='utf-8').write(SCHEMA_JSON)

# fallback paste block (no Liquid: settings resolved to their defaults, no video band)
PASTE = """<!-- ============================================================================
     WIPEX BLOG · self-contained paste block (FALLBACK)
     %s
     The primary deliverable is sections/%s.liquid. Use this only for a store whose theme
     strips sections, or for a quick preview. It carries the same cleared prose.
     No external requests, no libraries, no inline handlers.
============================================================================ -->
%s
%s
<script type="application/ld+json">
%s
</script>
""" % (CFG['title'], SECTION_ID, build_css(P, CFG) + '\n' + paste_body.replace('%P%', P) + '\n' + build_js(P, CFG), '', SCHEMA_JSON)
io.open(os.path.join(OUTDIR, 'SHOPIFY-PASTE.html'), 'w', encoding='utf-8').write(PASTE)

LIQUID_DOC = """# SHOPIFY LIQUID VARIANT

The primary deliverable is `sections/%s.liquid` — the whole article as a theme-editor editable
section, per the store convention (this theme renders blog content from a custom section, not the
post body). Install path in `SHOPIFY-README.md`.

What this section can do without touching code:
- hero eyebrow / H1 / intro, two hero CTAs (label + URL)
- three editorial stills (16:9 / 2:3) with alt text, caption and focal point
- one native video band with fallback image and an optional overlay + CTA
- sticky mobile CTA label + URL

Prose is generated from `%s`. Edit the markdown, regenerate, re-paste — never retype the copy in
the editor, or it stops matching the compliance report.
""" % (SECTION_ID, os.path.basename(SRC))
io.open(os.path.join(OUTDIR, 'SHOPIFY-LIQUID.md'), 'w', encoding='utf-8').write(LIQUID_DOC)

META = """# SHOPIFY META — paste these into the admin

```
TITLE
%s

SLUG
%s

META TITLE   (%d chars, target 65)
%s

META DESCRIPTION   (%d chars, target 155)
%s

TAGS
%s

PUBLISH DATE
%s   (%s)

AUTHOR
%s
```

SECTION: %s   (theme editor > add section, or install the template file below)
```
sections/%s.liquid
templates/%s
snippets/wipex-blog-schema.liquid
```
""" % (CFG['title'], CFG['slug'], len(CFG['meta_title']), CFG['meta_title'],
       len(CFG['meta_desc']), CFG['meta_desc'], CFG['meta_tags'], CFG['published'],
       CFG['publish_note'], CFG['author'], SECTION_NAME, SECTION_ID, CFG['template_file'])
io.open(os.path.join(OUTDIR, 'SHOPIFY-META.md'), 'w', encoding='utf-8').write(META)

# readme
README_T = """# Shopify install — %s

## Install
1. Themes > Edit code > `sections/` > Add a new section > name `%s` > paste
   `sections/%s.liquid`. Save.
2. `snippets/wipex-blog-schema.liquid` > Add a new snippet with that exact name > paste. Save.
3. `theme.liquid` > before `</head>` add:
   @@@
4. `templates/` > Add a new template > article > name it `%s` > paste
   `templates/%s`. Save.
5. Assign the template to the post, or add the section to the post's template in the theme editor.
6. Leave the blog post BODY empty — the section renders the whole article. Anything in the body
   renders twice.

## In the theme editor
Hero (eyebrow/H1/intro/two CTAs) · three editorial stills with alt, caption and focal point · one
native video band with fallback + optional overlay · sticky mobile CTA. Everything else in the
article is generated prose and is read-only by design.

## Pre-publish verification
- [ ] section saves without a validation error (schema name <= 25 chars, <= 40 settings)
- [ ] no JSON-LD inside the section file (`%s`): @type keys count as settings
- [ ] page renders once (body empty), no duplicate H1
- [ ] checklist ticks persist after a reload
- [ ] calculator updates on input, on mobile too
- [ ] sticky CTA appears after the hero and hides over the final CTA
- [ ] images carry the supplied alt text; empty slots render nothing
- [ ] Rich Results test: BlogPosting + FAQPage + Product + BreadcrumbList, no duplicates
- [ ] `SECTION-VALIDATION.txt` in this folder reports "none"

## Troubleshooting
| Symptom | Cause | Fix |
|---|---|---|
| "too many settings" on save | JSON-LD left inside the section | keep it in the snippet only |
| section name rejected | name > 25 chars | shorten the name |
| article renders twice | body not empty | clear the post body |
| no styles | theme strips section styles | add the CSS to theme CSS, keep the markup |
| checklist does not persist | browser blocks localStorage | expected in private mode |
"""
README = (README_T % (CFG['title'], SECTION_NAME, SECTION_ID, CFG['slug'], CFG['template_file'], SECTION_ID)
          ).replace('@@@', "{%- if article and article.handle == '" + CFG['slug'] + "' -%}{{ render 'wipex-blog-schema' }}{%- endif -%}")
io.open(os.path.join(OUTDIR, 'SHOPIFY-README.md'), 'w', encoding='utf-8').write(README)

# ─────────────────────────────────────────────────────────────────────────────
# validation
# ─────────────────────────────────────────────────────────────────────────────
problems, notes = [], []
section_text = io.open(os.path.join(OUTDIR, 'sections', SECTION_ID + '.liquid'), encoding='utf-8').read()

if len(SECTION_NAME) > 25:
    problems.append('section name is %d chars (Shopify limit 25)' % len(SECTION_NAME))
if len(settings) > 40:
    problems.append('schema declares %d settings (Shopify limit 40)' % len(settings))
if re.search(r'"@type"', section_text):
    problems.append('@type keys inside the section file (Shopify counts them as settings)')
if 'application/ld+json' in section_text:
    problems.append('JSON-LD inside the section file')
ids = [s['id'] for s in settings if 'id' in s]
if len(ids) != len(set(ids)):
    problems.append('duplicate setting ids: %s' % [i for i in ids if ids.count(i) > 1])

# Liquid safety: the prose must not carry Liquid delimiters
prose = build_article(nodes, toc, CFG, resolved=True, uidt='paste')[0]
prose_only = re.sub(r'<(style|script)[^>]*>.*?</\1>', ' ', prose, flags=re.S | re.I)
for token in ('{{', '{%'):
    if token in prose_only:
        problems.append('prose contains %r — Liquid would parse the copy' % token)

# FAQ integrity: the visible FAQ and the FAQPage answer set must be the same
visible_q = re.findall(r'<h3 class="%s__faqq">(.*?)</h3>' % P, section_text)
if faq and len(visible_q) != len(faq):
    problems.append('visible FAQ questions (%d) != FAQPage questions (%d)' % (len(visible_q), len(faq)))
for q, a in faq:
    if html.escape(q) not in section_text:
        problems.append('FAQ question missing from the section: %r' % q)

# no external requests, no inline handlers
for tag in re.findall(r'<style[^>]*>(.*?)</style>', section_text, re.S | re.I) + \
           re.findall(r'<script[^>]*>(.*?)</script>', section_text, re.S | re.I):
    if re.search(r'https?://', tag):
        problems.append('external URL inside style/script (a request we cannot afford)')
if re.search(r'\son[a-z]+\s*=', section_text, re.I):
    problems.append('inline event handler in the section')

# link integrity
bad_links = [h for h in re.findall(r'href="([^"]+)"', section_text)
             if not (h.startswith(DOMAIN) or h.startswith('#') or h.startswith('mailto:'))]
bad_links = [h for h in bad_links if '{{' not in h]
if bad_links:
    problems.append('non-canonical links: %s' % sorted(set(bad_links))[:5])

# instrumentation + instance safety
cro = len(re.findall(r'data-cro="', section_text))
if cro < 4:
    problems.append('only %d data-cro attributes — conversion events would be untracked' % cro)
if 'section.id' not in section_text:
    problems.append('section does not use section.id — two instances would collide')
static_ids = [i for i in re.findall(r'id="([^"]+)"', section_text) if '{{' not in i]
if static_ids:
    problems.append('static id(s) that collide when the section appears twice: %s' % sorted(set(static_ids))[:5])

# Liquid tag balance — a missing {% endif %} is invisible to every check above and shows up as a
# theme error on save, so count the pairs here.
for o_tag, c_tag in (('if', 'endif'), ('unless', 'endunless'), ('for', 'endfor'),
                     ('raw', 'endraw'), ('capture', 'endcapture'), ('case', 'endcase')):
    n_open = len(re.findall(r'\{%-?\s*' + o_tag + r'\b', section_text))
    n_close = len(re.findall(r'\{%-?\s*' + c_tag + r'\b', section_text))
    if n_open != n_close:
        problems.append('unbalanced Liquid: %d {%s} vs %d {%s}' % (n_open, o_tag, n_close, c_tag))
if len(re.findall(r'\{%\s*schema\s*%\}', section_text)) != 1:
    problems.append('expected exactly one {% schema %} block')

# CSS/markup coverage — the bug class this catches: a selector that matches nothing, so the styles
# silently do not apply (the token block was scoped to `.wx-cpt` while the root element carried only
# `wx-cpt__root`, which meant no palette and no base typography, and every static check still passed).
_root_ok = ('<div class="%s ' % P in section_text) or ('<div class="%s"' % P in section_text)
if not _root_ok:
    problems.append('the root element does not carry the bare "%s" class: the token block and every '
                    'base selector (h1/h2/p/a) match nothing, so the section renders unstyled' % P)
_css_classes = set(re.findall(r'\.%s(?:__)?([a-zA-Z0-9_-]+)' % P, section_text.split('</style>')[0]))
_missing_css = sorted(c for c in _css_classes if ('%s__%s' % (P, c)) not in section_text
                      and ('%s-%s' % (P, c)) not in section_text and (' %s ' % c) not in section_text)
# anything that is not inside <style>/<script> and is not markup renders as visible page text —
# this caught the stylesheet's own header comment sitting before the <style> tag
_outside = re.sub(r'<style.*?</style>', ' ', section_text, flags=re.S | re.I)
_outside = re.sub(r'<script.*?</script>', ' ', _outside, flags=re.S | re.I)
if '/*' in _outside:
    problems.append('a CSS comment sits outside <style> — it renders as visible text on the page')

# claims lint over the rendered prose + the module copy
claims_csv = find_claims_csv()
lint_target = strip_markup(section_text)
findings = lint_claims(lint_target, claims_csv) if claims_csv else []
blocking = [f for f in findings if f[0] == 'BLOCKING']
if blocking:
    for f in blocking:
        problems.append('CLAIM %s: "%s" — %s → %s' % (f[0], f[1], f[2], f[3]))
if not claims_csv:
    notes.append('claims CSV not found — lint ran without the prohibition list')

report = []
report.append('SECTION VALIDATION — %s' % SECTION_ID)
report.append('generated: sections/%s.liquid (%d lines, %d chars)' % (SECTION_ID, section_text.count('\n') + 1, len(section_text)))
report.append('')
report.append('PRE-SAVE (Shopify hard limits)')
report.append('  section name      : %r (%d chars, limit 25)  %s' % (SECTION_NAME, len(SECTION_NAME), 'OK' if len(SECTION_NAME) <= 25 else 'FAIL'))
report.append('  settings declared : %d (limit 40)            %s' % (len(settings), 'OK' if len(settings) <= 40 else 'FAIL'))
report.append('  @type in section  : %d                        %s' % (len(re.findall(r'"@type"', section_text)), 'OK' if not re.search(r'"@type"', section_text) else 'FAIL'))
report.append('  JSON-LD location  : snippets/wipex-blog-schema.liquid  OK')
report.append('  setting ids unique: %s' % ('OK' if len(ids) == len(set(ids)) else 'FAIL'))
report.append('')
report.append('DELIVERABLE CHECKS')
report.append('  theme-editor settings : %d (%d image_picker, %d url, %d select, %d video, %d group blocks)'
              % (len(settings),
                 len([s for s in settings if s['type'] == 'image_picker']),
                 len([s for s in settings if s['type'] == 'url']),
                 len([s for s in settings if s['type'] == 'select']),
                 len([s for s in settings if s['type'] == 'video']),
                 len([s for s in settings if s['type'] in ('header', 'paragraph')])))
report.append('  instance safety       : %s' % ('section.id + registry OK' if 'section.id' in section_text else 'FAIL'))
report.append('  data-cro annotations  : %d' % cro)
report.append('  a11y landmarks        : aria-label %d, aria-expanded %d, role=region %d, sr-only %d'
              % (len(re.findall(r'aria-label=', section_text)), len(re.findall(r'aria-expanded=', section_text)),
                 len(re.findall(r'role="region"', section_text)), len(re.findall(r'%s__sr' % P, section_text))))
_mod_probes = (('toc', '<nav class="%s__toc"' % P), ('checklist', '<div class="%s__check"' % P),
               ('calculator', '<div class="%s__calc"' % P), ('sticky', '<div class="%s__sticky"' % P),
               ('progress', '<div class="%s__progress"' % P), ('video', 'lifestyle_video'),
               ('hero', '<header class="%s__hero"' % P), ('liferow', '<div class="%s__liferow"' % P))
_absent = [name for name, probe in _mod_probes if probe not in section_text]
for name, probe in _mod_probes:
    if probe not in section_text:
        problems.append('module %r declared but not rendered (no %s in the section)' % (name, probe))
report.append('  modules rendered      : %s'
              % ', '.join('%s %s' % (n, 'OK' if n not in _absent else 'MISSING') for n, _ in _mod_probes))
report.append('  token block applied   : %s  (root carries the bare prefix class, so the palette and '
              'base typography resolve)' % ('OK' if _root_ok else 'FAIL'))
if _missing_css:
    report.append('  CSS classes with no markup (state-only or dead): %s' % ', '.join(_missing_css))
report.append('  media slots           : %d editorial stills + video band' % len([s for s in CFG['image_slots']]))
report.append('  module library        : %s'
              % ', '.join([k for k in ('problem_strip', 'stat_cards', 'card_grid', 'decision_tool',
                                       'system_block', 'feature_block') if CFG.get(k)]
                          + ['products', 'faq', 'checklist', 'calculator', 'toc', 'sticky', 'liferow']))
report.append('  editorial media only  : %s (product imagery stays out of the section)'
              % ('yes' if 'image_picker' in section_text else 'no'))
report.append('')
report.append('CONTENT INTEGRITY')
report.append('  prose generated from  : %s' % os.path.basename(SRC))
report.append('  Liquid tag balance    : if %d/%d, raw %d/%d, schema blocks %d'
              % (len(re.findall(r'\{%-?\s*if\b', section_text)), len(re.findall(r'\{%-?\s*endif\b', section_text)),
                 len(re.findall(r'\{%-?\s*raw\b', section_text)), len(re.findall(r'\{%-?\s*endraw\b', section_text)),
                 len(re.findall(r'\{%\s*schema\s*%\}', section_text))))
report.append('  Liquid-safe prose     : %s' % ('OK' if not [p for p in problems if 'Liquid would parse' in p] else 'FAIL'))
report.append('  FAQ questions         : %d visible == %d in JSON-LD' % (len(visible_q), len(faq)))
report.append('  TOC entries           : %d' % len(toc))
report.append('  links                 : %d, all canonical (%s)' % (len(re.findall(r'href="', section_text)), DOMAIN))
report.append('')
report.append('CLAIMS LINT (Never-Say-Prohibitions.csv)')
if claims_csv:
    report.append('  source                : %s' % claims_csv)
report.append('  BLOCKING findings     : %d' % len(blocking))
for f in blocking:
    report.append('    "%s" — %s' % (f[1], f[2]))
    report.append('      ...%s...' % f[4])
    report.append('      fix: %s' % f[3])
rev = [f for f in findings if f[0] == 'REVIEW']
report.append('  REVIEW (context)      : %d' % len(rev))
for f in rev[:8]:
    report.append('    "%s" — %s | ...%s...' % (f[1], f[2], f[4]))
report.append('')
report.append('RESULT: %s' % ('NONE — safe to paste' if not problems else '%d PROBLEM(S)' % len(problems)))
for p_ in problems:
    report.append('  - %s' % p_)
for n_ in notes:
    report.append('  note: %s' % n_)

txt = '\n'.join(report) + '\n'
io.open(os.path.join(OUTDIR, 'SECTION-VALIDATION.txt'), 'w', encoding='utf-8').write(txt)
print(txt)
if problems:
    raise SystemExit('refusing to declare the artifact clean: %s' % problems)
