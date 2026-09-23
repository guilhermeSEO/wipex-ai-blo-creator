# Wipex AI Blog Creator

One skill, end to end: research → copy → SEO/AEO/GEO/CRO → claims compliance → a reference-grade
Shopify section, with the gates, the tooling and the measured evidence that make the output
repeatable. The repository root **is** the skill (`SKILL.md` + `references/` + `scripts/`), so a
clone can be dropped straight into an agent's skills directory.

Version: skill v3.1 (2026-09-23). Start reading at **`references/00-master-workflow.md`** — it is the
whole process on one page: schematic, roles, gates, artifact contract, naming, validation matrix,
escalation and the consolidation map.

---

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | the skill itself — flow, the six non-negotiables, delivery contract, escalation, changelog |
| `references/00-master-workflow.md` | **the operating manual**: phases, roles, gates, artifacts, conventions, validation matrix, escalation, consolidation map |
| `references/01` | inputs, the brief gate, audience segments, the `products: auto` engine, the 12-field pre-flight, models A/B/C |
| `references/02` | demand and keyword research: Trends semantics, LLM scoring, specificity spectrum, calendar×trend matrix, fit anchors, semantic-pollution test, corpus-saturation count, peak windows |
| `references/03` | the claims envelope: tiers, codes, the six-block per-post envelope template and the adjudications that are ours |
| `references/04` | audience, objections (with "where it lives"), the FAQ set, consumption formula |
| `references/05` | copy architecture against the measured house shape |
| `references/06` | SEO/AEO/GEO/CRO/CTR: meta, JSON-LD, link map, readability, E-E-A-T, citation triggers, snippet molds, CTA copy |
| `references/07` | image briefs + the interactive section |
| `references/08` · `08b` | the measured house pattern · the H2 registry of the 21 posts (the angle-delta instrument) |
| `references/09` | gates, escalation, the 30/60/90 learning loop |
| `references/10` | section engineering: module library, schema budget, media tiers, JS/a11y contracts, validation gates |
| `references/11`–`13` | the absorbed generic method: Trends extraction, measurement discipline, the class-level method |
| `references/14-superseded-rules.md` | the register of rules these documents used to carry and this skill no longer allows — read before "we already decided…" |
| `scripts/` | `build_shopify_paste.py` (the section emitter), `audit_blog_patterns.py`, `build_content_calendar.py`, `trends_fetch.py`, `google-trends-probe.js` |
| `assets/compliance/` | the reference data the claims lint runs against (prohibited claims, approved sentences, TURI cells) + the boundary notice |
| `assets/reference/` | the hand-built reference section the module library was derived from |
| `assets/evidence/` | the measured house table (`blog_patterns_21.csv`) |
| `examples/blog-01-cost-per-table/` | a complete worked post: phase documents, config, generated section + snippet + template, fallback paste block, validation receipt |
| `archive/` | provenance: the loose v2.1 documents, the delivered audit (delta reports), the reference section, the raw scrape |

---

## Install (Hermes)

```bash
git clone https://github.com/guilhermeSEO/wipex-ai-blo-creator.git
cp -r wipex-ai-blo-creator ~/AppData/Local/hermes/skills/wipex-blog-generation
```

Then load it with `skill_view(name='wipex-blog-generation')`. The skill is self-contained: it depends
on no other skill and on no loose file outside itself.

## Run it

```bash
# phases 1–2 per references/00..06, then, from the compliance-approved markdown:
python scripts/build_shopify_paste.py 2D-body-clean.md
```

| Output | Purpose |
|---|---|
| `sections/<section_id>.liquid` | **the deliverable** — the whole article as a theme-editor editable, instance-safe section (35 settings: hero copy/CTAs, three editorial stills with alt/caption/focal, native video band, sticky CTA) |
| `SHOPIFY-CONFIG.json` | per-post knobs, including the module anchors (problem strip, stat cards, decision tool, A+B system block, feature block) |
| `snippets/wipex-blog-schema.liquid` | the JSON-LD (never inside the section — see `references/10` §7) |
| `templates/article.<name>.json` | assigns the section to that post |
| `SHOPIFY-PASTE.html` | fallback for a store that does not use sections |
| `SHOPIFY-README.md`, `SHOPIFY-META.md`, `SHOPIFY-LIQUID.md`, `SHOPIFY-SCHEMA.json` | install path, admin fields, the Liquid variant, the schema alone |
| `SECTION-VALIDATION.txt` | the receipt |

## The bar

`SECTION-VALIDATION.txt` must read `RESULT: NONE` before anything is pasted into Shopify. It checks:

- Shopify's limits (section name ≤ 25 chars, ≤ 40 settings, zero `@type` in the section);
- Liquid tag balance and **Liquid-safe prose** (the copy may not contain `{{` or `{%`);
- no external request in `<style>`/`<script>`, no inline handler, every link canonical;
- instance safety (no static id, `section.id` registry), ≥ 4 `data-cro` annotations;
- FAQ integrity (visible Q&A == FAQPage entities);
- **claims lint** against `assets/compliance/Never-Say-Prohibitions.csv` — a BLOCKING finding stops
  the build, even when the copy already passed the compliance phase.

---

## Compliance boundary — what is NOT in this repository

This repository is public, so the internal source documents are deliberately excluded: the Wipex
Claims Filter review pack (`.docx`), the Surface Claims Guide / Annex A (`.pdf`) and the extracted
plain-text copy of either. What is published is the derived reference data the automation needs
(`assets/compliance/*.csv`, boundary explained in its `NOTICE.md`) and the skill's own summary of the
rules (`references/03`). The Filter itself is owned by compliance and is not editable by this team:
rule changes go to compliance and return as a new version.

`examples/blog-01-cost-per-table/` contains our own working documents derived from the approved copy
(claim envelope, compliance report). Delete that folder if derived envelopes should not be public
either — nothing in the skill depends on it.

No credentials exist in this repository, by design: the generator is config-driven and the per-post
config carries only copy and public URLs.