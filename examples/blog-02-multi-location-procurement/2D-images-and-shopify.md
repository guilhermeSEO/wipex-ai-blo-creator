# 2D — IMAGES, INTERACTIVE, SHOPIFY
Blog 02 — multi-location cleaning supply procurement · generated 2026-09-28 · **revised 2026-09-29**

> **Revision 2026-09-29 — layout model `funnel`.** The post was rebuilt on the new conversion
> layout model (see `sections/` and `SHOPIFY-CONFIG.json → layout_model`). Copy trimmed
> 3,566 → ~2,750 words, the six-part framework collapsed into an accordion, the conversion
> modules moved above the fold. Image anchors and the module map below reflect that.

> **Revision 2026-09-29 (b) — visual/conversion pass.** Wider reading column (funnel overrides
> `--wx-maxw:1320px` / `--wx-readw:50rem`, reading column ≈ 800px, tighter section spacing), hover
> states, table product links, **FAQ as one `<details>` per question with a `+`**, **Keep Reading as
> link cards**, and an illuminated closing band. The dark bands no longer use neutral black: the
> `band` / `band_alt` tokens are set to a plum-derived aubergine (`#3a2740` / `#251730`).
> **Two page-visible defects were fixed in this pass:** relative markdown links (`/products/…`,
> `/blogs/…`) had never been converted and were rendering as literal markdown text — the reason the
> Keep Reading list had no clickable links — and the closing band, which the copy ends as a
> markdown list, had no buttons at all.

> **Revision 2026-09-29 (c) — the bands take the closing band's colouring.** On the owner's call
> ("gostei da coloração usada nessa sessão … utilizar no resto do blog"), the value strip, the A+B
> system block, the sticky CTA and the code block now use the **same illuminated gradient as the
> closing band** — `accent-soft → surface → plum-soft` + mint→plum accent bar, with ink text — and
> the plum-black fill is gone. The video letterbox keeps `band`, the one surface behind media.

## Layout model
`SHOPIFY-CONFIG.json` sets **`layout_model: "funnel"`**. Same design tokens, same typography, same
prose contract as the editorial model — a different arrangement and reading rhythm:

| | editorial (blog 01) | funnel (this post) |
|---|---|---|
| hero | full hero + lede | short hero, tighter padding |
| first band | problem strip (4 cells) | **value strip** (one row of the post's own numbers + CTA) |
| conversion modules | mid/late page | **right after the hero**: decision tool → product cards |
| calculator | late | early (inside the cost section) |
| FAQ | near the end | early, before the deep framework |
| long sections | open prose | **accordion** (`<details>`, closed by default) |
| TOC | open | collapsed |

## Image briefs (5–8)
| # | Section / context | Subject | Mood + execution notes | Dimensions | Overlay | Alt text (chars) |
|---|---|---|---|---|---|---|
| 1 | Hero (above H1) | A supply-room shelf at a multi-site operator with one labelled bin per room type | Professional, operational; shoot real shelving in service, not styled stock; neutral light; no posed staff | 1120×630 (16:9) | none | Multi-location cleaning supply procurement: one wipe program across every site (75) |
| 2 | Beside "Why this matters in Q4" (`layout: row`) | A labelled par level printed and taped on a supply-room shelf: product, case qty, par number | Documentary; close on the label so the number is legible; the point is the routine, not the product | 480×720 (2:3) | none | Labelled par level on a supply-room shelf: product name, case quantity, reorder point (85) |
| 3 | Before FAQ (16:9 band) | One wall dispenser mounted, matching units visible in the same frame across a gym floor | Clean, wide, consistent hardware; show standardisation, not one hero product | 1120×630 (16:9) | none | One wall dispenser standard installed across a fitness facility footprint (71) |

**Alt-text rule reminder:** describe what is visible; no "safe", no superlative, no "best". Alt text is in scope for the 2C review. Counts reported above.

## Alt text (list)
- hero_image — `Multi-location cleaning supply procurement: one wipe program across every site` (75)
- still1_image — `Labelled par level on a supply-room shelf: product name, case quantity, reorder point` (85)
- still2_image — `One wall dispenser standard installed across a fitness facility footprint` (71)

## Interactive section (the house uses one per post)
```yaml
module_type: calculator          # cost/consumption only — no performance verdict
anchor:     "before:Cost-per-use calculator"
inputs:
  - Sites in the footprint             (default 10)
  - Wipes used per site per week       (default 500)
  - Weeks in the period                (default 1)
  - Case price ($)                     (default 42.99)
  - Wipes per case                     (default 700)
  - Wipes per use event                (default 1)
  - Seconds of labour per wipe (opt.)  (default 0)
  - Loaded hourly rate ($, optional)   (default 0)
calculation: fixed module arithmetic (references/10 §4) — cost per wipe, footprint cost per period, cost per two-wipe reset
output_template: "cost per wipe · footprint cost per period · cost per two-wipe reset"
cta: none inside the module (the page CTAs carry the conversion)
guard: outputs a count/cost/coverage only — never a cleaning-performance comparison, a time-saving promise, or a "safe" verdict
```
Verified in a real browser: 8 inputs compute `$0.0614 / $307.07 / $0.0307` from the defaults, and
`$0.1000 / $500.00 / $0.0500` after editing the case price to 70.

## Module map (funnel model)
| Module | Anchor | Note |
|---|---|---|
| hero | first | short; H1 + promise + two CTAs |
| value strip | `after_hero` | 4 numbers from the approved copy + one CTA |
| decision tool | `after_hero` | "Match the format to the room", 3 cards, each with its own `data-cro` |
| product cards | `after_hero` | "Formats on the approved list", 3 cards |
| calculator | `before:Cost-per-use calculator` | early |
| liferow still | `after:Why this matters in Q4` | 2:3 figure beside the prose |
| accordion | `The six-part program framework` | `<details>`, closed by default |
| card grid | `after:Where a multi-location program leaks money` | 5 cards; no heading (the H2 carries it) |
| system block | `after:Where a multi-location program leaks money` | the dark A+B card + CTA |
| video band | `before_faq` | editorial break |
| FAQ | markdown H2 | 8 questions, **one `<details>` each, `+` beside the question**; 8 Q&As == 8 FAQPage entities |
| Keep Reading | markdown H2 | **5 link cards** (whole card clickable, `data-cro …-keep-N`) |
| checklist | markdown `- [ ]` | 9 items, `localStorage` |
| TOC | `On this page` | collapsed by default (`toc_open: false`) |
| sticky CTA / progress | always | sticky shows past the hero, hides over the final CTA |

## Generated artifacts
| Output | Status |
|---|---|
| `sections/wipex-section-multi-location-procurement-2026.liquid` | **the deliverable** — 1,084 lines, 81,155 chars |
| `SHOPIFY-CONFIG.json` | written (`layout_model: funnel`, value_strip, accordion, anchors) |
| `SECTION-VALIDATION.txt` | **RESULT: NONE** — 0 BLOCKING, 16 REVIEW (context) |
| `templates/article.multi-location-procurement.json` | generated |
| `snippets/wipex-blog-schema.liquid` | generated (JSON-LD lives here, not in the section) |
| `SHOPIFY-README.md` · `SHOPIFY-META.md` · `SHOPIFY-SCHEMA.json` · `SHOPIFY-PASTE.html` · `SHOPIFY-LIQUID.md` | generated |
| `2D-body-clean.md` | the approved source the section was generated from (revised 2026-09-29) |

## Rendered verification (Chrome headless, real engine — not a static assertion)
| Check | Value | Verdict |
|---|---|---|
| root class | `wx-mlp wx-mlp__root wx-mlp__model wx-mlp__model--funnel` | model applies |
| H1 font / size | "New Order" / 48px | on-brand |
| primary button | bg rgb(118,195,156) · text white · radius 999px | on-brand |
| accordion | 1 `<details>`, id `the-six-part-program-framework`, closed, 6 H3 inside, `+` marker | renders |
| accordion on hash jump | `details.open = true` | opens |
| calculator | 8 inputs → `$0.0614 / $307.07 / $0.0307`; reacts to input edits | computes |
| value strip / decision / products / leaks cards | 4 / 3 / 3 / 5 | modules render |
| TOC | collapsed (`data-open=false`), 10 links, toggles | renders |
| sticky CTA | hidden at top → visible after 1500px scroll (`aria-hidden` correct) | renders |
| tables / checklist / FAQ | 2 / 9 items / 8 Q&A | modules render |
| CSS leaked as page text | none | clean |
| layout tokens | `--wx-maxw:1320px` · `--wx-readw:50rem`; reading column 800px | wider, less scroll |
| band colour | every band (value strip, system, sticky, code) = the closing band's gradient `rgb(234,246,240) → rgb(255,255,255) → rgb(245,238,247)`; text `rgb(28,29,29)` | brand-toned, no dark bar |
| accent bars | value strip 4px · sticky 3px · closing 4px (mint→plum) | renders |
| FAQ accordion | 8 `<details>`; marker `+` closed → `–` open; answer body renders | opens |
| Keep Reading | 5 cards, every one an `<a>`, all hrefs `https://wipex.co/…` | clickable |
| table links | 6 anchors, all canonical `/products/` URLs | clickable |
| closing band | 3 buttons (`primary`/`gold`/`ghost`) + 4px accent bar | renders |
| raw markdown visible on page | none | fixed |

## Operator checklist
- [ ] re-paste `sections/wipex-section-multi-location-procurement-2026.liquid` (Edit code > Sections)
- [ ] install `snippets/wipex-blog-schema.liquid` and add the render line to `theme.liquid` behind the article.handle condition
- [ ] assign `templates/article.multi-location-procurement.json`; leave the post body EMPTY
- [ ] fill the 3 image slots in the theme editor (or set `literal_url` in the config) and check alt text
- [ ] set title, slug and meta fields in admin; **recount** title = 65 / meta = 155 after pasting
- [ ] preview mobile: accordion opens, calculator, checklist persistence, sticky CTA, table stacking
- [ ] add the reciprocal link on `buy-cleaning-wipes-in-bulk` and on `bulk-gym-cleaning-wipes-supplies`
- [ ] confirm stock + that every price in the copy still matches the live product JSON
- [ ] confirm `/pages/contact-us` carries a working B2B/quote route
- [ ] publish on the target date (~2026-11-02), then log it in `published_ledger.md`
