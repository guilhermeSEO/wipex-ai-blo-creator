# 07 — AGENT 2D: IMAGES, INTERACTIVE SECTION, SHOPIFY PASTE

Comes after 2A (and after 2C has cleared the copy), because alt text is in scope for the
claims review and the interactive section must not promise anything the Filter forbids.

---

## 1. Image briefs — 5–8, designed to be executed without questions

| Field | Requirement |
|---|---|
| Section / context | where it sits (hero above H1, after the cost block, inside CHOOSE…) |
| Subject | specific enough for a photographer or stock search — "busser wiping a four-top in a busy dining room between covers" |
| Mood | professional / operational / seasonal |
| Dimensions | hero 1200×800 · body 600×400 · stat/inline 400×300 |
| Overlay text | only if it is a claim-free label |
| Source | product photography, custom brief, stock library |
| Alt text | descriptive + keyword-bearing, 100–125 chars |

**Alt-text rules:** describe what is visible; include the product or the surface, not a
claim; no "safe", no superlatives, no "best". Alt text is checked by 2C like any other copy.

---

## 2. Interactive section — the house uses one per post

Pick from: calculator, comparison toggle, checklist, quiz/score, timeline, format chooser.

| Field | Content |
|---|---|
| Type | e.g. "cost-per-table calculator" |
| User input | what they enter (tables, turns/day, current consumable) |
| Output | what they learn (cost per reset, cost per month, comparison to current) |
| Benefit | why it earns the interaction |
| Implementation | custom Liquid section, or an existing app |

**Guard:** a calculator may compute cost, coverage and consumption. It may **not** output a
cleaning-performance comparison, a time-saving promise, or a "safe" verdict.

---

## 3. Shopify Liquid skeleton

```liquid
{%- comment -%} Wipex blog module: <name>. Rate-limited inputs only; no promises in output. {%- endcomment -%}
<div class="wipex-module wipex-module--{{ section.id }}">
  <h2 class="wipex-module__title">{{ section.settings.title }}</h2>
  <div class="wipex-module__body">
    {%- for block in section.blocks -%}
      <div class="wipex-module__item" {{ block.shopify_attributes }}>
        <span class="wipex-module__value">{{ block.settings.value }}</span>
        <span class="wipex-module__label">{{ block.settings.label }}</span>
      </div>
    {%- endfor -%}
  </div>
</div>

{% schema %}
{
  "name": "Wipex Module",
  "settings": [
    { "type": "text", "id": "title", "label": "Title", "default": "" }
  ],
  "blocks": [
    { "type": "stat", "name": "Stat", "settings": [
      { "type": "text", "id": "value", "label": "Value" },
      { "type": "text", "id": "label", "label": "Label" }
    ]}
  ],
  "presets": [{ "name": "Wipex Module" }]
}
{% endschema %}
```

---

## 4. The delivery artifact — generated, never hand-written

### ⚠ FIRST: this store renders blog content from a CUSTOM SECTION, not the post body

Verified on the live site 2026-09-22: the article page carries **no `article__body` and no `.rte`
container**, and the live Table Bussers post (2026-08-31) is a section named
`wipex-section-table-bussers-2026` containing the whole article — its 18 `<h2>`s live inside it.
The theme is **Impulse 7.4.0**, heavily customised (`cstm-style.css`, `custom-style.css`).

**Therefore the primary artifact is a `.liquid` section**, not a post-body paste:

```
sections/wipex-section-<slug>-<year>.liquid     scoped CSS + article HTML + JS + JSON-LD + schema
templates/article.<name>.json                   assigns the section to that one post
```

The whole content sits inside `{% raw %} … {% endraw %}` so Liquid cannot try to parse the CSS/JS
braces, with the `{% schema %}` block **outside** the raw tag. Verify before delivering:
- exactly one `{% raw %}` / `{% endraw %}` pair, one comment pair, one schema pair
- **zero** `{{` or `{%` inside the raw block
- the schema block parses as JSON
- the post body is left **empty**, so the article cannot render twice

### Why not the post body

A body paste would render — the theme styles tables inside `.rte`. But the theme applies
`table-layout: fixed` with 6px/8px padding, so wide comparison tables get cramped; and the body
cannot run JavaScript, so the interactive module cannot live there at all. The section is also the
convention this team already works in.

`SHOPIFY-PASTE.html` is still emitted as a **fallback** for a store that does not use sections.

Run `python scripts/build_shopify_paste.py <blog>/2D-body-clean.md`.

It reads the **compliance-approved markdown** and emits the section plus the supporting files.
Generating the markup instead of retyping it is the point: a hand-written second version can
silently disagree with what Agent 2C cleared, and nothing would catch it.

| Output | Purpose |
|---|---|
| `sections/<slug>.liquid` | **the deliverable** — paste into Edit code > Sections |
| `templates/article.<name>.json` | assigns the section to that one post |
| `SHOPIFY-README.md` | install path, verification list, troubleshooting table |
| `SHOPIFY-META.md` | title, slug, meta title (65), meta description (155), tags, author, date |
| `SHOPIFY-SCHEMA.json` | the JSON-LD alone (for themes that already emit Article schema) |
| `SHOPIFY-PASTE.html` | fallback body paste for a store without the section convention |
| `SHOPIFY-LIQUID.md` | the calculator as a standalone reusable section |

### Reuse across posts

- **Section per post** (this store's current pattern): one `.liquid` per article, named
  `wipex-section-<slug>-<year>`. Full control, no collision risk.
- **Module section** (better once a block repeats): extract the calculator into
  `wipex-cost-per-table-calculator` and include it from any post that needs it. Worth the
  indirection only from the **third** post that uses it — before that it is needless abstraction.

### Performance rules the generator enforces

Reviewers ask "will it lag?" — these are the rules that answer it:

| Rule | Implementation |
|---|---|
| No external request | no third-party font, script, stylesheet or image; everything is inline |
| No library | no jQuery, no framework; the calculator is ~40 lines of vanilla JS |
| CSS scoped | every rule under one class prefix (`.wx-cpt`) so it cannot collide with the theme |
| JS non-blocking | one IIFE, no globals, listeners with `{ passive: true }` |
| No reflow per keystroke | arithmetic runs inside `requestAnimationFrame`, not on every input event |
| No `innerHTML` | `textContent` only; no `document.write`; no inline `on*` handlers (CSP-safe) |
| Mobile safe | every table sits in an `overflow-x:auto` container; `contain: content` on the module |
| Accessible | `role="status"` + `aria-live` on the calculator output, `scope` on header cells, real `<label>`s |
| Printable | `@media print` keeps the checklist and tables intact |

### Verify the artifact before delivering it

```
[ ] 0 external requests (grep for http(s) outside your own domain and schema.org)
[ ] 0 inline on* handlers, 0 innerHTML / document.write
[ ] block tags balanced (div, table, ul, ol, p, h1-h3, style, script, thead, tbody, tr, th, td)
[ ] exactly one H1; H2/H3 counts inside the house range
[ ] the JSON-LD parses and its FAQPage entities match the on-page FAQ verbatim
[ ] the generator reports title = 65 and meta = 155
[ ] compliance regression: grep the HTML for food-safe / safe on / beats / lab-tested /
    hygienic / "Best" / 100% natural — all must be 0
[ ] the patch-test line count is unchanged from the approved copy
[ ] Shopify: schema name (and preset names) <= 25 characters
[ ] Shopify: settings <= 40 per section/block (ours declares 0)
[ ] Shopify: ZERO `@type` keys inside the section file — the JSON-LD lives in a snippet
```

### Shopify platform limits (learned in production, 2026-09-22)

Both of these were rejected on save the first time the section was installed:

| Limit | Value | What happened |
|---|---|---|
| schema `name` and preset names | **25 characters** | `Wipex — Cost per table 2026` is 27 and was refused |
| settings per section/block | **40** | exceeded, even though the schema declared `"settings": []` |
| validator scope | **the whole file**, not just the `{% schema %}` block | 31 `@type` keys in a body-level JSON-LD were counted as settings, tripping the 40 cap |

**Rule that follows: structured data never ships inside a section.** It goes in a snippet
(`snippets/wipex-blog-schema.liquid`) rendered from `theme.liquid` behind an `article.handle`
condition, so it loads on that one post and nothing else:

```liquid
{%- if template.name == 'article' and article.handle == '<post-handle>' -%}
  {%- render 'wipex-blog-schema' -%}
{%- endif -%}
```

The generator now asserts all three limits and refuses to report the artifact as clean if any
fails — the check runs before declaration, not after a failed save.

The compliance regression grep matters: the HTML is a second representation of the cleared text, so
it is re-checked rather than assumed.

### What the operator still does by hand

- paste the body; set the title, the slug and the meta fields (then **recount** the characters)
- upload the images with the supplied alt text
- paste or install the JSON-LD, and run the Rich Results test once for duplicate schema
- install the Liquid section if the theme needed it, and preview on mobile
- add the **reciprocal link** on the older cluster post
- confirm stock and that the price in the copy still matches
- publish on the target date, then log it in `published_ledger.md`

---

## 5. Output template

```markdown
# 2D — IMAGES, INTERACTIVE, SHOPIFY
## Image briefs (table, 5–8 rows)
## Alt text (list, 100–125 chars each, counted)
## Interactive section (type / input / output / benefit / implementation / guard)
## Liquid section (code)
## Paste file (blocks 1–9 above)
## Operator checklist
- [ ] paste body, set title + slug
- [ ] set meta fields (verify counts after paste)
- [ ] upload images with alt text
- [ ] add the JSON-LD in the theme / SEO app
- [ ] add the Liquid section, then preview mobile
- [ ] publish, then submit for indexing
```
