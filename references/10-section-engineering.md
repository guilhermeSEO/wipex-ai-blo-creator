# Section engineering — the reference-grade module (v2.8)

Read this before touching `scripts/build_shopify_paste.py`, and before judging a delivered
section. The house reference is `workdir/wipex/02-setup/reference-sections/REFERENCE_pilates-fall-2026.liquid`
(736 lines, hand-built); the gap list between it and our v2.7 output is
`workdir/wipex/03-scripts/REFERENCE_SECTION_GAP_ANALYSIS.md`.

**Adopt its engineering, never its copy.** The reference's own headings ("The Best Wipe System",
"Best for:", "equipment-safe") fail Claims Filter v1.1. The generator lints its own output for
exactly those words and refuses to declare the artifact clean when it finds one.

---

## 1. What is emitted, in order

| # | Part | Notes |
|---|---|---|
| 1 | `{%- comment -%}` header | names the files in the theme, states that the prose is generated and must not be retyped |
| 2 | `{%- assign uid = section.id -%}` | every id in the file is suffixed with it |
| 3 | `<style>` inside `{% raw %}` | tokens + modules, all scoped under `.<css_prefix>` |
| 4 | root `<div class="<prefix>__root" id="<prefix>-{{ uid }}" data-wpx-section="{{ uid }}">` | the JS entry point |
| 5 | progress bar | `[data-wpx-progress]` |
| 6 | hero `<header>` | settings-driven eyebrow / H1 / lede / two CTAs + first editorial still |
| 7 | `<article>` → `<section>` per H2 | each section: `.…__read` column + any bands anchored to it |
| 8 | sticky mobile CTA | `[data-wpx-sticky]` + dismiss |
| 9 | `<script>` inside `{% raw %}` | one IIFE, per-section registry |
| 10 | `{% schema %}` | settings + presets. Never JSON-LD (see §7) |

## 2. Schema budget (Shopify hard limits, learned by failed saves)

- `name` and every preset name: **≤ 25 chars**.
- **≤ 40 settings.** `header` and `paragraph` grouping blocks count toward the number.
- Shopify's validator scans the **whole file**: JSON-LD counted 31 `@type` keys as settings.
- Current layout: hero 7 · photography 12 (3 slots x image/alt/caption/focal) · video 7 · sticky 2 · 7 group blocks = **35**.
- Inspector, not a guess: `build_settings()` in the generator + `SECTION-VALIDATION.txt`.

## 3. Media system (three tiers — do not blur them)

- **A — editorial stills.** `image_picker` + alt + caption + focal `select`. 16:9 for bands
  (`1120x630`), 2:3 for portrait slots (`480x720`). Always `srcset` + `sizes` + `loading="lazy"`
  + `decoding="async"`; hero image is `fetchpriority="high" loading="eager"`. Focal point is a
  CSS variable on the figure (`--<prefix>-img-pos`), consumed by `object-position`.
- **B — video band.** Native `video_tag`, `autoplay loop muted playsinline`, no controls, plus a
  fallback image and an optional overlay (eyebrow/heading/text/CTA). The whole band emits nothing
  when there is neither a video nor a fallback.
- **C — product photography.** Deliberately NOT in the section: product imagery comes from config
  literal URLs, so the settings budget stays with editorial media.
- Every image block hides itself when empty and shows an editor-only placeholder under
  `request.design_mode` instead of an empty frame.

## 4. Module inventory (where each one sits)

| Module | Anchor | Purpose |
|---|---|---|
| hero | first | H1 + promise + two CTAs |
| problem strip | `after_hero` | the reference's 4-cell strip: names the pressure the post relieves |
| quick-answer callout | `## Quick answer` list | the LLM-quotable key numbers |
| stat cards | `after:<H2>` | number + label pairs lifted from the article's own takeaways (the module renders claims, it never makes them) |
| interactive TOC | `## On this page` | collapsible, `aria-expanded`/`aria-controls` |
| editorial stills | config `image_slots[].anchor` = `hero`, `after:<H2>`, `before_faq` | proof and place |
| video band | config `video_anchor` (default `before_faq`) | editorial break, away from the final CTA |
| comparison table | markdown table | `data-label` on every cell → rows stack as cards ≤640px |
| product cards | config `products_anchor` | 2–3 formats, `Suited to:` (not "Best for") |
| feature block | `after:<H2>` | the reference's "workhorse" block: image, eyebrow, heading, proof bullets, one CTA |
| A+B system block | `after:<H2>` | the reference's AOV device. Config decides what the two parts are — a real bundle only when marketing has confirmed the companion SKU, otherwise the article's own workflow framing. **Never invent a companion product** |
| decision tool | `after:<H2>` | "which setup fits your room", one card per operation profile, each with its own `data-cro` |
| calculator | injected before the worked example | cost only, never a performance claim |
| checklist | markdown `- [ ]` run | real checkboxes + `localStorage` persistence |
| FAQ | `## Frequently asked questions` | visible Q&A whose text IS the FAQPage JSON-LD |
| sticky CTA | always | appears past the hero, hides over the final CTA, dismissible |
| progress bar | always | rAF-throttled scroll |

## 5. JavaScript contract

- ONE IIFE. No libraries, no inline handlers, no `<script src>`.
- Per-section registry: `init(id)` returns early unless `getElementById(prefix + '-' + id)` exists
  and has not been initialised, so **two instances on one page are safe**.
- Boot on `DOMContentLoaded` and again on `shopify:section:load` (theme editor re-render).
- Scroll work is rAF-throttled with `passive: true` listeners.
- `prefers-reduced-motion` pauses the background video instead of autoplaying it.
- Output via `textContent` only; no `innerHTML`.
- Data attributes are the contract: `data-wpx-section`, `data-wpx-progress`, `data-wpx-toc`,
  `data-wpx-toc-toggle`, `data-wpx-checklist`, `data-wpx-check`, `data-wpx-calc`,
  `data-wpx-sticky`, `data-wpx-sticky-close`.

## 6. Accessibility + conversion instrumentation

- Landmarks: `aria-label` on the TOC nav and the video band; `role="region" tabindex="0"` on every
  scrollable table; `aria-hidden` on decorative furniture; `sr-only` for label-less table headers;
  `:focus-visible` outline; dismiss button has an `aria-label`.
- `data-cro` on **every** CTA: `<slug>-hero`, `-hero-2`, `-prod-N`, `-video`, `-sticky`. Under 4 in
  the artifact is a validation failure.
- Instance safety: nothing static. Ids `{{ uid }}`-suffixed, heading anchors too
  (`<h2 id="slug-{{ uid }}">`), so the validator rejects any literal id.

## 7. The two divergences we keep from the reference

1. **Structured data never ships inside the section.** It lives in
   `snippets/wipex-blog-schema.liquid`, rendered from `theme.liquid` behind an `article.handle`
   condition. The reference ships Article/Breadcrumb/FAQ inside the section — copying that breaks
   the 40-setting cap (v2.7).
2. **FAQPage answers are the visible answers.** The generator compares the visible question count
   to the JSON-LD entity count and fails on a mismatch, so the two cannot drift.

## 8. Validation gates (the generator refuses to be clean)

`SECTION-VALIDATION.txt` in the post folder is the receipt. Every line is a real check:

- schema name ≤ 25, settings ≤ 40, one `{% schema %}` block, unique setting ids;
- zero `@type` / `application/ld+json` in the section;
- **Liquid tag balance** (`if/endif`, `raw/endraw`, `for/endfor` …) — a missing `endif` is
  otherwise invisible until the theme errors on save;
- **Liquid-safe prose**: the copy may not contain `{{` or `{%`, because the section is parsed;
- no external URL inside `<style>`/`<script>`, no inline handler;
- every `href` canonical (`https://wipex.co`) or an in-page anchor;
- ≥ 4 `data-cro`, no static id, `section.id` present;
- **claims lint** against `Never-Say-Prohibitions.csv`: BLOCKING stops the build, REVIEW is printed
  for the operator with the context line.

## 9. Config — `SHOPIFY-CONFIG.json` (per post)

Written next to the markdown on first run. Keys: `title`, `slug`, `meta_title`, `meta_desc`,
`meta_tags`, `author`, `published`, `publish_note`, `keywords`, `domain`, `css_prefix`,
`section_id`, `section_name`, `template_file`, `hero_eyebrow`, `hero_cta`, `hero_cta2`,
`sticky_cta`, `video_anchor`, `image_slots[]` (`setting`, `anchor`, `ratio`, `label`, `alt`,
`caption`, `literal_url`), `products_anchor`, `products_heading`, `products[]`, `final_cta_heading`,
`schema_products[]`, `schema_mentions[]`.

Anchor syntax: `after_hero` | `hero` | `after:<H2 text substring>` | `before_faq` | `end`. An anchor
that matches no heading prints a WARN line instead of dropping the module silently.

Five modules are pure config (`problem_strip`, `stat_cards`, `decision_tool`, `system_block`,
`feature_block`): each entry carries its own `anchor`, so placement is an editorial decision, not a
code change. Their copy is linted exactly like the article copy — the stat cards especially: every
number in them must already exist in the approved article.

## 10. Pitfalls (each one cost a build)

- **A Liquid template cannot go through Python `%`-formatting** — `{%-` is read as a format spec.
  Long Liquid fragments are built by concatenation or with `@P@`/`@CRO@` tokens resolved by `fin()`.
- The house markdown continues bullets on a single-space indented line. A parser that only merges
  2+ spaces emits `<ul>/<p>/<ul>/<p>` confetti. Handled in `parse()`.
- Static heading ids break instance safety; `uid_anchors()` suffixes every heading id.
- "Best for:" is a prohibited superlative (Never-Say #13) — the product card says `Suited to:`.
- Product copy in the config is linted like the article copy: certifications only where Part 4
  shows them, `plant-based` only as substrate wording, never as a "natural" claim.
