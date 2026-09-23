---
name: wipex-blog-generation
title: Wipex Blog Generation
version: '3.1.2'
date_created: '2026-09-22'
date_updated: '2026-09-23'
owner: Guilherme (Wipex automation lead)
description: "Use when producing a Wipex blog post end to end."
tags: [wipex, blog, content-factory, seo, aeo, geo, cro, compliance, google-trends, shopify]
---

# Wipex Blog Generation — v3.1.2

Research, copy, SEO/AEO/GEO, CRO and claims compliance in one evidence-driven flow.
Written so the only thing you supply is an input form; everything else is researched,
measured, checked and delivered.

**v2.1 corrects v1.0 with measured data**, not assumptions. The structure below is derived
from the 21 most recent live Wipex blogs (see `references/08-house-patterns.md`), not from a
sensible-sounding template. Where the two disagreed, the live site won.

> **SELF-CONTAINED (v2.9).** This skill is the single source: the class-level method, the brand
> instance, the claims envelope, the gates and the delivery tooling all live here. The generic
> methodology that used to sit in a separate skill (`ecommerce-blog-generation-framework`) was
> absorbed into `references/11` (Trends extraction), `references/12` (measurement discipline) and
> `references/13` (the generic method), and its probe is now `scripts/google-trends-probe.js`.
> Keep the generic technique generic and the Wipex specifics specific — but keep both here, so
> nothing depends on a second skill being installed.

---

## LOAD THIS FIRST

Everything is in `references/`. Read in flow order; don't preload all of it.

| Step | Load |
|---|---|
| **Start here — the whole process on one page** | **`references/00-master-workflow.md`** |
| You are about to take an input form | `references/01-inputs-and-modes.md` |
| Phase 1 — research | `references/02-agent-1a-research.md` |
| Phase 1 — claims envelope | `references/03-compliance-claims-filter.md` |
| Phase 1 — audience/FAQ | `references/04-agent-1c-audience-faq.md` |
| Phase 2A — copy | `references/05-agent-2a-copy-architecture.md` |
| Phase 2B — SEO/AEO/GEO/CRO | `references/06-agent-2b-seo-aeo-geo-cro.md` |
| Phase 2D — images + Shopify | `references/07-agent-2d-images-shopify.md` |
| Section engineering (build or judge a section file) | `references/10-section-engineering.md` |
| Fetching Trends (the method that works from this host) | `references/11-trends-extraction.md` |
| Any number you are about to trust | `references/12-measurement-discipline.md` |
| The de-branded method behind phases 1–2 | `references/13-generic-method.md` |
| The H2 registry of the 21 recent posts (angle delta) | `references/08b-house-outline.md` |
| Before reintroducing a rule "we already decided" | `references/14-superseded-rules.md` |
| Always (the measured house blueprint) | `references/08-house-patterns.md` |
| Gates, escalation, learning loop | `references/09-gates-escalation-learning.md` |
| Tools | `scripts/trends_fetch.py`, `scripts/google-trends-probe.js`, `scripts/audit_blog_patterns.py`, `scripts/build_content_calendar.py`, `scripts/build_shopify_paste.py` |

---

## THE SIX NON-NEGOTIABLES

1. **Compliance is upstream, not a review.** The claims envelope is settled in Phase 1
   (`references/03`) and the copy is written inside it. A blog that needs its claims
   removed at the end was written wrong. Zero BLOCKING findings is the bar to publish.
2. **No invented facts.** No fabricated search volume, no invented SKU, no made-up
   statistic, no cover-stat without a source and a date checked. If a number cannot be
   sourced, it does not go in. Published third-party figures must be cited with source
   name + date checked.
3. **Claims come from Part 4 of the Claims Filter, per SKU.** A product's claim codes
   decide what the copy may say. Never transfer a claim from a sibling product or a
   formulation. `P = —` means no numbers and no comparisons about cleaning performance.
4. **Same product, new angle, chosen date.** Reusing a product across posts is normal and
   expected — the catalogue is finite and the audiences repeat. What must never repeat is the
   **angle**, and what must always be deliberate is the **date**. Search the archive for the
   angle, not just the keyword (`references/02` §5), then target the term's next demand peak
   rather than today (`references/02` §6). A duplicate is a laziness failure, not a
   keyword failure.
5. **Measure the draft against the house pattern before delivery.** Run
   `scripts/audit_blog_patterns.py` on the draft. A blog that is 1,900 words with no FAQ
   and 2 product links is not a Wipex blog.
6. **The section is validated, not eyeballed.** Run `scripts/build_shopify_paste.py` and read
   `SECTION-VALIDATION.txt` before anything is pasted into Shopify. `RESULT: NONE` is the bar; a
   BLOCKING claims finding stops the delivery even when the copy passed 2C. Details in
   `references/10-section-engineering.md`.

---

## THE HOUSE ARCHITECTURE (measured, 21 most recent blogs)

| Dimension | Measured range | Mean | Target for a new post |
|---|---|---|---|
| Words in body | 2,578 – 4,762 | **3,576** | **3,000 – 4,500** |
| H2 sections | 13 – 26 | 18.5 | 14 – 22 |
| H3 subsections | 4 – 36 | 17.2 | 8 – 24 |
| Paragraphs | 39 – 89 | 64.7 | 50 – 80 |
| Avg paragraph | 35 – 72 words | 45.8 | 35 – 55 |
| FAQ block | present in 20 of 21 | — | **mandatory, 6–10 questions** |
| Comparison table | 14 of 21 | — | include when choosing between formats |
| Bulleted lists | 21 of 21 | — | mandatory |
| Links to `/products/` in body | 0 – 16 | 6.5 | 4 – 10 |
| Links to `/blogs/` in body | 4 – 13 | 4.7 | 4 – 8 |
| Meta description length | 133 – 166 chars | 146 | 155 exact (owner standard) |
| JSON-LD present | 14 of 21 | — | standard, not optional |

**v1.0 said 1,800–2,200 words.** The live house writes 3,000+. That single line was the
biggest gap between the old skill and the real output.

### The recurring section modules

Not every post uses all of them, but these are the modules the house actually repeats:

1. **Hero + promise** — H1 keyword-forward, 2 paragraphs, then "By the end you will know…"
2. **Quick answer / key takeaways** — 4–6 bullets, each carrying a real number
3. **On this page** — jump-link TOC
4. **Direct-answer definition** — the paragraph an LLM would quote
5. **Stat cards** — 3–4 value + label pairs (`20–40%`, `Typical increase in wipe consumption`)
6. **Why now / problem framing** — the seasonal or operational trigger
7. **Framework** — a named system with H3 steps (e.g. the four-step turnover workflow)
8. **Numbered value list** — "5 ways…", "6 areas to reset…"
9. **Cost-per-use block** — the house's signature device; see `references/05`
10. **Format chooser + comparison table** — "Which X fits your operation?"
11. **Self-assessment / calculator** — interactive or checklist form
12. **Readiness checklist** — printable, season-bound
13. **FAQ** — 6–10 Q&As, long-form answers
14. **Keep Reading** — 3–4 internal blog links
15. **Closing CTA** — restates the operation outcome, 2–4 arrow-anchored links
16. **Compliance blocks when health-related** — disclaimer / health-information note

---

## THE FLOW

### PUBLISH TIMING — the runway principle

Posts are not published when they are ready; they are published **2–4 weeks before the
moment their demand arrives** (minimum 2 weeks, default ~1 month). The runway does two jobs:

1. **Authority maturation** — by the time the peak hits, the post has been live, crawled and
   linked for weeks, so it competes for the peak instead of arriving with it.
2. **Conversion readiness** — there is time to verify stock, price, offer and links, so the
   traffic that lands can actually buy.

The target date comes from the term's 12-month peak, not from the calendar quarter and not
from the day the draft is finished (`references/02` §6, checklist in `references/09`).

### PHASE 0 — INPUT (you, ~5 minutes)

Fill the form in `references/01-inputs-and-modes.md`. Minimum viable input:

```yaml
topic:           "<what the blog is about>"
calendar_hook:   Q1 | Q2 | Q3 | Q4 | Evergreen
target_buyer:    "<who has the budget>"
angle:           "<the argument the post makes>"
products:        "<exact Part 4 names> or auto"
cta:             "<the action, in operational terms>"
```

Pick an operational model (A auto / B hybrid / C human-led) — default B.

**→ GATE 1: brief locked.** Restate the brief as you understood it in one block. Do not
start research on an ambiguous brief; the last test run lost a whole session to an
unresolved topic line.

### PHASE 1 — RESEARCH (Agents 1A, 1B, 1C)

Run 1A and 1C in parallel; 1B needs 1A's product choice.

- **1A — Demand & keyword** (`references/02`): Google Trends via browser, LLM keyword
  scoring, product matching, angle delta against the existing archive, the **zero-data
  branch** when a product term has no measurable demand, and the **peak window → publish
  date** derivation.
- **1B — Claims envelope** (`references/03`): SKU rows from Part 4, tier classification,
  codes granted, hard exclusions, escalations.
- **1C — Audience & FAQ** (`references/04`): persona, buying criteria, objections, FAQ
  outline, citable third-party data points with dates.

**→ GATE 2: approve keyword + products + angle + publish date.** This is the only compulsory
human stop. The date is part of the approval because it comes from the peak window, not from
whatever week the draft happens to be finished in.

### PHASE 2 — PRODUCTION (2A → 2B → 2C → 2D)

- **2A Copy** (`references/05`) — full draft against the house architecture, inside the
  claims envelope, all facts sourced.
- **2B SEO/AEO/GEO/CRO** (`references/06`) — title 65 exact, meta 155 exact, slug, merged
  JSON-LD (BlogPosting + FAQPage + Product + BreadcrumbList), internal link map, readability,
  GEO signals, 4 CTAs, featured-snippet answer, citation-ready wording.
- **2C Compliance validation** (`references/03` §review) — 7-step Part 1 review over the
  written draft. Zero BLOCKING required.
- **2D Images + Shopify** (`references/07`) — 5–8 image briefs, alt text, interactive
  section, Liquid skeleton, paste-ready formatting.

Run `scripts/audit_blog_patterns.py` over the draft and attach the report.

**→ GATE 3: publish.** Paste into Shopify, set the meta fields, order images.

### PHASE 3 — LEARNING LOOP (`references/09` §retro)

At 30 / 60 / 90 days: GSC impressions, position, CTR, add-to-carts from the post. Record
what worked. Deltas go into the next brief and, if structural, back into this skill with a
version bump. **This is the "cada vez melhor" mechanism — without it the skill is static.**

---

## DELIVERY CONTRACT

Every completed blog ships as files. **`SHOPIFY-PASTE.html` is the one the operator pastes** —
a single self-contained block, generated from the compliance-approved copy by
`scripts/build_shopify_paste.py`, never hand-written (hand-written HTML drifts from what Agent 2C
cleared).

| File | Purpose |
|---|---|
| **`sections/<slug>.liquid`** | **the deliverable** — the whole article as a theme-editor editable, instance-safe section: scoped CSS, module markup, native video band, interactive TOC/checklist/calculator, sticky CTA, progress bar. JSON-LD is NOT in it (see `references/10`) |
| `SHOPIFY-CONFIG.json` | the per-post knobs: hero copy, CTAs, image slots + alt/caption/focal, video anchor, product cards, slug/section name. Written on first run; edit it, don't edit the Liquid |
| `SECTION-VALIDATION.txt` | the receipt — schema limits, Liquid balance, Liquid-safe prose, link integrity, CTA instrumentation, FAQ integrity, claims lint. `RESULT: NONE` is the bar |
| `templates/article.<name>.json` | assigns the section to that one post |
| `SHOPIFY-README.md` | install path, pre-publish verification, troubleshooting table |
| `SHOPIFY-META.md` | admin fields: title, slug, meta title, meta description, tags, author |
| `SHOPIFY-SCHEMA.json` | the JSON-LD alone, if the theme already emits Article schema |
| `SHOPIFY-PASTE.html` | fallback body paste, for a store that does not use sections |
| `SHOPIFY-LIQUID.md` | the calculator as a standalone reusable section |
| `2D-body-clean.md` | the plain text, for reading/review |
| `blog-copy-TAGGED.md` | the claim-tagged working copy (the compliance trail) |
| `seo-spec.md` | title/meta/slug, schema, link map, readability, GEO, CRO audit |
| `compliance-report.md` | findings by severity, zero BLOCKING required |
| `image-briefs.md` | briefs + alt text with character counts |
| `pattern-audit.md` | the draft scored against the house table in §THE HOUSE ARCHITECTURE |
| `published_ledger.md` | the Phase 3 baseline, one entry per post |

---

## ESCALATION (never soften, never guess)

**To Dean Tansman (compliance, Dutch Harbor Brands)** — any BLOCKING finding; a product
with no Part 4 row; a certification asserted where Part 4 shows `—`; a Tier 2 claim on a
product without code `P`; a benchmark brand named; "safe" applied to a surface; a conflict
between the Filter and a live page; a request for legal/regulatory interpretation.

**To Wipex marketing** — no internal link map; target audience outside the known personas;
calendar hook outside the publishing window; a CRO goal that conflicts with standing strategy.

**To the owner (Guilherme)** — brief ambiguity; a keyword that no data supports; a
product/audience override; anything that would change this skill's rules.

---

## PROVENANCE

- Claim rules: `wipex/01-compliance/Wipex-Claims-Filter-AI-Review-Pack-v1.1-ACTIVE.docx`
  plus `Never-Say-Prohibitions.csv`, `Approved-Surface-Claims-16-Sentences.csv`,
  `TURI-Results-Reference-v1.0.csv`, `Wipex-Surface-Claims-Guide-Annex-A-v1.0.pdf`.
  **That document is not editable by us** — changes go to Dean for Part 11 and a new version.
- House structure: measured from 21 live posts, 2026-09-23. The metrics are in
  `references/08-house-patterns.md`, the measured table in `assets/evidence/blog_patterns_21.csv`,
  and the H2 registry of every post in `references/08b-house-outline.md`. The skill no longer
  depends on a loose file in the project workdir for any of it.
- Trends method: validated 2026-09-23. curl is blocked with HTTP 429 from this host; the
  browser path works. Widget data requires the widget's `token`, and endpoints are named
  `multiline` / `relatedsearches` / `comparedgeo`, not by widget id.

## CHANGELOG

**v3.1.2 (2026-09-23)** — three small corrections found by cross-checking the worked SEO spec
(`2B-seo-spec.md`) against `references/06`: title candidates must record the **rejected** options with
the stated reason ("Turn Rate" was rejected as buyer jargon) so a rejection is reviewable instead of
taste; readability adds **Flesch Reading Ease 60–70** alongside FK 6–8, measured on paragraph text
only. No rule changed — the instruments got sharper.

**v3.1.1 (2026-09-23)** — closes the four loose ends the audit left open: `references/07` was still
describing the v2.7 delivery (everything inside `{% raw %}`, "settings declares 0") and now matches
the v3 generator — Liquid-parsed prose with raw only around `<style>`/the JS, `SHOPIFY-CONFIG.json`
and `SECTION-VALIDATION.txt` in the artifact table, and a verification list that asserts what the
build actually asserts (35 settings, uid-suffixed ids, ≥ 4 `data-cro`, FAQ parity, tag balance); the
image brief gains execution notes and a reported alt-text count; the calculator gains the executable
`inputs / calculation / output_template / cta` mold. `references/03` §9 adds the shape of a per-SKU
claims report (`CAN SAY / CANNOT SAY / RECOMMENDED ANGLE / FILTER VERSION` — dated, because a claim
set without a date cannot be defended). `references/01` §10 records model D (test all three), which
is meaningful once, on three posts, and never as a standing mode.

**v3.1 (2026-09-23)** — **the consolidation itself: the 13 loose documents were audited against the
skill, item by item, and everything still true was folded in.** Eight parallel delta analyses
covered the research, claims, audience, copy, SEO/CRO/GEO/CTR and input layers; the surviving content
landed as `references/01` §5–§9 (audience segments, the `products: auto` engine, the 12-field
pre-flight, the red flags that force Model C, the `your_edit` form format), `references/02` §9–§15
(the specificity spectrum, the calendar×trend×niche matrix, fit calibration anchors, the signal→
family table, the **semantic-pollution test**, the **corpus-saturation count**, and the measured peak
rows for cost per table / per cover / cleaning-supplies cost), `references/03` §7–§8 (the six-block
envelope template, the adjudications that are ours — the cost-figure rule, the adjacency guardrail,
the exact food-service phrase, the no-transfer rule, the recomputed $/wipe→$/table arithmetic, and
the Tier-3-only envelope model), `references/04` §5–§8 (the objection table with a "where it lives"
column, the consumption formula, the mined FAQ set as a worked example, the third decision path),
and `references/06` §11–§16 (E-E-A-T scaffold with insertion points, the full citation-trigger set,
the snippet/PAA molds, the title-choice rule, CTA copy + friction reducers). Two new files exist
because the audit found things a reference alone could not hold: `references/08b-house-outline.md`
(the H2 registry of the 21 posts — the actual angle-delta instrument, with the one contaminated
record and the boilerplate caveat measured and documented) and `references/14-superseded-rules.md`
(the register of every claim in those documents that this skill now denies, so a superseded rule
cannot be reintroduced by accident — including the dangerous one: a Tier 2 performance claim on a
SKU whose `P = —`). `blog_patterns_21.csv` moved into `assets/evidence/`, so no rule in this skill
points at a loose workdir file. Measured house metrics, claims rules and the pipeline are unchanged;
what changed is that the reasoning behind them is now written down where the next run can read it.

**v3.0 (2026-09-23)** — **consolidated: everything aligned in the workdir now lives in this one
skill, and it is published.** `references/00-master-workflow.md` is the operating manual — the
schematic of all three phases, roles and owners, the three gates plus the machine gate, the
artifact contract and the workdir convention, naming conventions, the validation matrix, the
escalation routes, and the **consolidation map** that records where each of the 13 original loose
documents landed (folded or superseded, never dropped silently). The reference section was also
used as more than documentation: its module library is now emitted by the generator — problem
strip, stat cards, decision tool, A+B system block and the primary feature block, all config-driven
with their own anchors, all linted (stat cards render numbers that already exist in the approved
copy; the A+B blocks refuse to invent a companion SKU and fall back to the article's own workflow
framing). The canonical file ships at `assets/reference/` so the pattern is never re-guessed.
`data-cro` annotations on the cost-per-table post went from 6 to 11 with the new modules.

The de-branded
framework (`ecommerce-blog-generation-framework`) was absorbed rather than referenced:
`references/11-trends-extraction.md` (how Trends is actually fetched from this host — in-browser
internal API, widget→endpoint map, the per-widget `token`, zero-data semantics),
`references/12-measurement-discipline.md` (verify the instrument before believing a number) and
`references/13-generic-method.md` (phases, LLM scoring, niche specificity, calendar/intent gates,
product matching, demand reality check, the 14 generic pitfalls), plus
`scripts/google-trends-probe.js`. One skill, no cross-skill dependency. The whole package is
mirrored to `github.com/guilhermeSEO/wipex-ai-blo-creator` (root = the skill) with `README.md`,
`assets/compliance/` (prohibition + approved-claims + TURI CSVs only — the Claims Filter .docx and
Annex A .pdf are deliberately NOT published), `examples/blog-01-cost-per-table/` and
`archive/` (the 13 loose v2.1 documents the skill was compiled from, the source briefs, the
reference section and the raw evidence).

**v2.8 (2026-09-23)** — **the section is now reference grade, and it is validated rather than
assumed.** The house reference section was read line by line and its engineering adopted: theme-editor
settings (35: hero copy/CTAs, three editorial stills with alt + caption + focal point, a native
Shopify video band with fallback and overlay, sticky CTA), a media system that hides itself when
empty, an interactive TOC, a real checklist with `localStorage`, reading progress, `data-cro` on
every CTA, a11y landmarks, and instance-safe JavaScript (registry keyed by `section.id`, re-init on
`shopify:section:load`, rAF-throttled, reduced-motion aware). Per-post settings moved to
`SHOPIFY-CONFIG.json`, so changing copy/links/images is a config edit, not a Liquid edit. The copy
is still generated from the compliance-approved markdown — that invariant is not traded.
Three of the reference's patterns are deliberately NOT adopted: its JSON-LD-inside-the-section
(breaks the 40-setting cap), its copy ("The Best Wipe System", "Best for:" — prohibited
superlatives, caught by the new claims lint), and its static ids. New gates that fail the build:
schema name/settings limits, Liquid tag balance, Liquid-safe prose (no `{{`/`{%` in the copy),
external-request and inline-handler scan, canonical-link check, static-id/instance-safety check,
FAQ-integrity check (visible Q&A == FAQPage), and a claims lint against `Never-Say-Prohibitions.csv`.
`SECTION-VALIDATION.txt` publishes every one of them. Method in `references/10-section-engineering.md`.

**v2.7 (2026-09-23)** — **Shopify platform limits, learned by a failed save.** Two real errors on
install: the schema `name` was 27 characters (limit **25**), and the validator reported **41
settings** on a schema that declared `"settings": []`. Cause of the second: Shopify's validator
scans the **whole file**, and the JSON-LD's 31 `@type` keys were counted as settings. Consequence
adopted as a rule: **structured data never ships inside a section** — it moves to
`snippets/wipex-blog-schema.liquid`, rendered from `theme.liquid` behind an `article.handle`
condition. The generator now asserts name length, the settings count and the absence of `@type`/
`application/ld+json` in the section, and raises rather than declaring a broken artifact clean.
Section name is now `Wipex Cost per Table` (20 chars).

**v2.6 (2026-09-23)** — **the store convention is now recorded, and it changes the deliverable.**
Verified on the live site: this store renders blog content from a **custom section**, not the post
body — the article page has no `article__body`/`.rte` container, and the live Table Bussers post is
`wipex-section-table-bussers-2026` holding the whole article. Theme is **Impulse 7.4.0**, heavily
customised. The generator now emits `sections/<slug>.liquid` (content wrapped in `{% raw %}`, schema
outside it) plus `templates/article.<name>.json` as the primary artifact, with the body paste kept
only as a fallback. Records why: the body cannot run JavaScript, so the interactive module cannot
live there, and the theme's `table-layout: fixed` cramps wide tables. Adds the section verification
list and the section-per-post vs module-section reuse rule.

**v2.5 (2026-09-23)** — the **paste pipeline**. `scripts/build_shopify_paste.py` converts the
compliance-approved markdown into `SHOPIFY-PASTE.html`: a single self-contained artifact carrying
scoped CSS, semantic HTML, the interactive calculator and the JSON-LD, with zero external requests.
The HTML is generated from the cleared copy rather than retyped, so it cannot drift from the
compliance report. Adds the Liquid fallback for themes that sanitise post bodies, the meta-fields
file, and the performance rules (no libraries, `passive` listeners, `requestAnimationFrame`,
`textContent`, scoped CSS, `overflow-x` tables). Delivery contract now names the paste artifact.

**v2.4 (2026-09-23)** — adds the **content calendar** layer: `scripts/build_content_calendar.py`
builds a dated calendar from occasions + measured peaks + evergreen topics and *validates* it
(no past dates, no same-day collisions, max 4/week, occasion lead inside 5–10 days). Establishes
the **occasion lead rule** — occasion posts publish **7 days before** the date — alongside the
existing 14–28 day peak lead (`references/02` §6). Adds the calendar-reading rules: weeks are
left light on purpose rather than filled for symmetry, and a week with no occasion and no peak
gets no post.

**v2.3 (2026-09-23)** — owner-set lead time replaces the 6–8 week figure I had put in:
**minimum 2 weeks, default ~1 month** before the target peak. The runway is reframed as
**authority maturation** (a post with weeks of history competes better for the peak) plus a
pre-peak **conversion-path verification** step, so arriving demand meets a working checkout.
Adds the before-the-peak checklist (`references/09`) and the pre-peak readiness rule in the
CRO spec (`references/06`). This also corrects the food-service date projection: the
cost-per-use target is the **Nov 1–20** window, so it is a QUEUE with a target date — not
"publish this week", as v2.2 implied.

**v2.2 (2026-09-23)** — policy change from the owner: **reusing a product across posts is
allowed and expected**; what must differ is the angle, and the publish date must be targeted
at the term's next peak rather than at the day the draft is ready. Adds the six angle-delta
axes and the mandatory ANGLE DELTA + reciprocal-link statement (`references/02` §5), adds
the peak-window → publish-window method with the measured food-service peaks
(`references/02` §6), moves the date into Gate 2, and updates the calendar rule in
`references/01`.

**v2.1 (2026-09-23)** — compiled from the 13 loose v2.1 documents plus measured evidence.
Corrects word count to 3,000–4,500; makes FAQ mandatory; adds the cannibalisation check;
adds the zero-Trends-data branch as a first-class path; adds the LLM scoring formula with
its limits stated; adds AEO/GEO/CRO/CTR as one specification; adds the pattern-audit step;
adds the Phase 3 learning loop; records the live-site compliance conflicts found on the
Table Bussers pages.

**v1.0 (2026-09-22)** — initial skill: 2-phase workflow, 7 agent prompts, Claims Filter v1.1.
