# Master workflow — Wipex blog, end to end

This is the operating manual for the skill and the single map of the whole process: who does what,
in which order, with which artifact, behind which gate. Everything else in `references/` is the
detail of one box below.

---

## 0. The one-line contract

**In:** an input form (topic, angle, buyer, hook, products, CTA).
**Out:** a validated Shopify section the operator pastes, plus the evidence trail behind every
claim, number and link in it.

Nothing in the output is invented: the copy is generated from the compliance-approved markdown,
the numbers are either measured or cited with a source and a date checked, and the claims are
tested by a lint that refuses to pass its own operator's copy.

---

## 1. The schematic

```
  YOU (5 min)                                                   ┌── GATE 1: brief locked
      │  input form (references/01)                             │   restated in one block
      ▼                                                        │   ambiguity stops here
  ┌────────────────────────────────────────────────────────────┴──┐
  │ PHASE 1 — RESEARCH (agents 1A, 1B, 1C)                        │
  │                                                               │
  │  1A demand & keyword        1B claims envelope   1C audience   │  1A ∥ 1C, 1B after 1A
  │  · Trends (ref 02, 11)       · SKU rows (ref 03)  · persona    │
  │  · LLM scoring (ref 02,13)   · tier + codes       · objections │
  │  · angle delta vs archive    · exclusions         · FAQ outline│
  │  · peak window → date        · escalations        · citations  │
  └───────────────────────────────┬───────────────────────────────┘
                                  │
                    ┌── GATE 2: approve keyword + products + angle + PUBLISH DATE
                    │   (the only compulsory human stop; the date comes from the peak window)
                    ▼
  ┌───────────────────────────────────────────────────────────────┐
  │ PHASE 2 — PRODUCTION                                          │
  │                                                               │
  │  2A copy         → 2B SEO/AEO/GEO/CRO → 2C compliance → 2D section
  │  (ref 05)          (ref 06)             (ref 03 §review)  (ref 07, 10)
  │  house shape       title 65 / meta 155  zero BLOCKING     config + generator
  │  inside envelope   JSON-LD + links      over the WRITTEN   sections/*.liquid
  │  facts sourced     CRO/CTR plan         draft              + snippet + template
  └───────────────────────────────┬───────────────────────────────┘
                                  │
              ┌── the machine gate: build_shopify_paste.py → SECTION-VALIDATION.txt
              │   RESULT: NONE required. A BLOCKING claims finding stops the delivery
              │   even when 2C passed.
              │
              │   ┌── GATE 3: paste into Shopify, set meta fields, order images,
              │   │   verify in the theme editor (SHOPIFY-README.md checklist)
              ▼   ▼
  ┌───────────────────────────────────────────────────────────────┐
  │ PHASE 3 — LEARNING LOOP (ref 09 §retro)                        │
  │  30 / 60 / 90 days: GSC impressions, position, CTR, ATC        │
  │  → published_ledger.md → next brief → (if structural) a skill   │
  │    version bump with the measured evidence attached            │
  └───────────────────────────────────────────────────────────────┘
```

## 2. Who does what

| Role | Owns |
|---|---|
| **You (owner / automation lead)** | the brief, Gate 2 decisions, product/audience overrides, anything that changes a rule in this skill, the publish |
| **The agent (this skill)** | phases 1–2, the generator run, the validation report, the escalation draft |
| **Compliance (Dean Tansman, Dutch Harbor Brands)** | the Claims Filter itself, a BLOCKING finding, a product with no Part 4 row, legal/regulatory interpretation |
| **Wipex marketing** | internal link map, audiences outside the known personas, calendar hooks outside the window, CRO goals that conflict with standing strategy |
| **Operator (paste duty)** | the Shopify admin steps: section, snippet, template, meta fields, images, publish date |

## 3. Gates

| Gate | Position | Entry criteria | Exit criteria |
|---|---|---|---|
| **1 — brief** | after the form | form filled, mode chosen (A/B/C) | brief restated in one block and confirmed; no ambiguity left |
| **2 — research** | after phase 1 | 1A/1B/1C delivered, keyword scored ≥ 3.5, angle delta stated, peak window → date | keyword + products + angle + publish date approved |
| **build gate** | after 2D | `build_shopify_paste.py` ran | `SECTION-VALIDATION.txt` = `RESULT: NONE`, zero BLOCKING claims |
| **3 — publish** | after the build gate | meta fields set, images uploaded, links verified | post live inside the runway window (≥ 2 weeks before the peak) |

## 4. Artifacts — the per-post folder

```
04-data/<blog-slug>/
  1A-demand-keyword-product.md   demand, scoring, product match, angle delta, target date
  1B-claims-envelope.md          allowed codes, exclusions, escalations
  1C-audience-faq.md             persona, objections, FAQ outline, cited data
  2A-blog-copy-TAGGED.md         the draft with its claims tagged
  2B-seo-spec.md                 title/meta/slug, JSON-LD, link map, readability, GEO
  2C-compliance-report.md        findings by severity (zero BLOCKING)
  2D-body-clean.md               the approved markdown — THE source of the deliverable
  2D-images-and-shopify.md       image briefs + install notes
  SHOPIFY-CONFIG.json            per-post knobs (copy, links, media, module anchors)
  SECTION-VALIDATION.txt         the build receipt
  pattern-audit.md               draft vs the measured house pattern
  published_ledger.md            the phase-3 baseline
  sections/<section_id>.liquid   THE DELIVERABLE
  snippets/wipex-blog-schema.liquid
  templates/article.<name>.json
  SHOPIFY-PASTE.html             fallback block
  SHOPIFY-README.md · SHOPIFY-META.md · SHOPIFY-LIQUID.md · SHOPIFY-SCHEMA.json
```

Nothing in the process is retyped by hand between artifacts: 2D-body-clean.md → generator →
section. The copy exists once.

## 5. Workdir convention

```
workdir/wipex/
  01-compliance/   the Claims Filter pack + the CSV reference data (not editable by us)
  02-setup/        theme reference sections and setup notes
  03-scripts/      the generator and the analysis scripts
  04-data/         per-post data, the measured patterns, the content calendar
  05-output/       nothing yet — the deliverables currently ship inside each post folder
```

## 6. Naming conventions

| Thing | Convention | Example |
|---|---|---|
| post slug | lowercase, hyphens, buyer stage | `cost-per-table-restaurant` |
| section file | `wipex-section-<topic>-<year>.liquid` | `wipex-section-cost-per-table-2026` |
| schema name | ≤ 25 chars, title case | `Wipex Cost per Table` |
| CSS prefix | short, from the slug | `wx-cpt` |
| CRO event | `<slug>-<placement>` | `cost-per-table-restaurant-hero` |
| image setting | `<placement>_image` + `_alt` + `_caption` + `_focal` | `hero_image_alt` |
| checklist id | `<prefix>-ck<N>-{{ uid }}` | `wx-cpt-ck1-{{ uid }}` |

## 7. Validation matrix

| Check | Caught by | Failure semantics |
|---|---|---|
| schema name ≤ 25 · settings ≤ 40 · one schema block | generator assertion | build stops |
| zero `@type` / JSON-LD inside the section | generator assertion | build stops |
| Liquid tag balance (`if/endif`, `raw/endraw`) | generator assertion | build stops |
| prose contains no `{{` / `{%` | generator assertion | build stops |
| no external request in style/script, no inline handler | generator assertion | build stops |
| every link canonical or in-page | generator assertion | build stops |
| no static id, `section.id` present, ≥ 4 `data-cro` | generator assertion | build stops |
| visible FAQ == FAQPage entities | generator assertion | build stops |
| prohibited claim wording | `lint_claims()` vs `Never-Say-Prohibitions.csv` | BLOCKING stops the build; REVIEW is printed with context |
| house pattern (words, H2s, FAQ, links) | `audit_blog_patterns.py` | rewrite before delivery |
| a rule that was already superseded coming back | `references/14-superseded-rules.md` | read it before "we already decided…" |

## 8. Escalation

| Trigger | Route |
|---|---|
| BLOCKING claim · missing Part 4 row · asserted certification · Tier 2 wording on a product without `P` · benchmark brand named · "safe" on a surface · Filter vs live page conflict | compliance (Dean) |
| no internal link map · new audience · calendar hook outside the window · CRO conflict | Wipex marketing |
| brief ambiguity · keyword with no data · product/audience override · any change to this skill's rules | the owner |

## 9. The consolidation map — where every original document now lives

This skill was compiled from 13 loose documents plus the generated artifacts. Nothing was dropped
silently: each one is either folded into a reference below or superseded with the reason recorded.

| Original document | Destination |
|---|---|
| `SKILL_INPUTS_MASTER.md`, `FILLED_FORM_EXAMPLES.md` | `references/01` §5–§9 (segments, product engine, 12-field checklist, red flags, the `your_edit` form format) |
| `01_AGENT_1A_TRENDS_KEYWORD.md`, `GOOGLE_TRENDS_INTEGRATION.md`, `LLM_KEYWORD_SCORING.md` | `references/02` §2–§15, `references/11`, `references/13` |
| `PRODUCT_RECOMMENDATION_ENGINE.md` | `references/02` §11–§12, `references/13` §5 |
| `02_AGENT_1B_CLAIMS_PREFLIGHT.md`, `1B-claims-envelope.md` | `references/03` §7–§8 (envelope template + adjudications) |
| `03_AGENT_1C_AUDIENCE_FAQ.md`, `1C-audience-faq.md` | `references/04` §5–§8 (objection table with "where it lives", consumption formula, mined FAQ set, third decision path) |
| `AGENT_2B_MASTER_PROMPT.md`, `2B-seo-spec.md` | `references/06` |
| `SENIOR_SEO_AEO_STRATEGY.md`, `GEO_CRO_CTR_STRATEGY.md` | `references/06` |
| `DECISION_MODELS.md` | `references/01` §8 (the red flags that force Model C); the cadence table is superseded |
| `WIPEX_BLOG_V2.1_COMPLETE_WORKFLOW.md`, `00_START_HERE.txt` | this document + `references/07` (calculator spec) |
| `SKILL_READY_CHECKLIST.txt`, `FINAL_CHECKLIST_v2.1.txt` | §3 gates + §7 validation matrix; the phase hour budget is in §1 |
| `21_blogs_outline.md` | `references/08b-house-outline.md` (the H2 registry — the angle-delta instrument) |
| `blog_patterns_21.csv` | `assets/evidence/` in the repository, so the skill no longer points at a loose workdir file |
| `CALENDAR_2026_Q4.*` | `references/09` (calendar rules) |
| `REFERENCE_pilates-fall-2026.liquid` | `assets/reference/` + `references/10` (the module library now emitted by the generator) |
| `REFERENCE_SECTION_GAP_ANALYSIS.md` | `references/10` §1, `archive/reference/` |
| every contradiction between those documents and this skill | `references/14-superseded-rules.md` — the register, so a superseded rule cannot be reintroduced |
| the 13 documents themselves and the raw evidence | `archive/` in the repository, for provenance |

Rule for the future: a document that stops being a source becomes an archive entry **and** a row in
`references/14`. Nothing is dropped silently, and nothing superseded is left loose.

## 10. Changing this skill

- A rule that a live post or a measurement contradicts → change the rule **and** the evidence line
  that produced it, and bump the version.
- A rule that a stakeholder sets (compliance, marketing, the owner) → record who set it and when in
  the changelog of `SKILL.md`.
- A generated artifact that needed hand-editing to be correct → that edit is a bug in the generator,
  not in the artifact. Fix the generator and re-run, so the next post inherits the fix.
