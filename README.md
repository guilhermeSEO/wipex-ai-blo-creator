# Wipex AI Blog Creator

One skill, end to end: research → copy → SEO/AEO/GEO/CRO → claims compliance → a
reference-grade Shopify section, with the gates and the tooling that make the output
repeatable. The repository root **is** the skill (`SKILL.md` + `references/` + `scripts/`), so a
clone can be dropped straight into an agent's skills directory.

Version: skill v2.9 (2026-09-23).

---

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | the skill itself — flow, gates, delivery contract, escalation, changelog |
| `references/01`–`09` | the phases: inputs, demand/keyword research, claims envelope, audience/FAQ, copy architecture, SEO/AEO/GEO/CRO, images + Shopify, the measured house pattern, gates + learning loop |
| `references/10` | section engineering — the anatomy of the Shopify section, the schema budget, the JS/a11y/media contract, the validation gates, the pitfalls |
| `references/11`–`13` | the absorbed generic method: how Trends is actually fetched, measurement discipline, the class-level methodology (scoring, gates, product matching) |
| `scripts/` | `build_shopify_paste.py` (the section emitter), `audit_blog_patterns.py`, `build_content_calendar.py`, `trends_fetch.py`, `google-trends-probe.js` |
| `assets/compliance/` | the reference data the claims lint runs against: prohibited claims, approved surface-claim sentences, TURI results |
| `examples/blog-01-cost-per-table/` | a complete worked post — the phase documents, the config, the generated section + snippet + template, the fallback paste block, and the validation receipt |
| `archive/` | provenance: the 13 loose v2.1 documents the skill was compiled from, the evidence used to measure the house pattern (21 live posts + raw scrape), and the reference section that `references/10` was derived from |

---

## Install (Hermes)

```bash
git clone https://github.com/guilhermeSEO/wipex-ai-blo-creator.git
cp -r wipex-ai-blo-creator ~/AppData/Local/hermes/skills/wipex-blog-generation
```

Then load it with `skill_view(name='wipex-blog-generation')`. The skill is self-contained: it
depends on no other skill.

## Run it

```bash
# 1. research → 2. claims envelope → 3. copy (see references/01–06)
# 4. build the deliverable from the compliance-approved markdown:
python scripts/build_shopify_paste.py 2D-body-clean.md
```

The generator writes next to the markdown:

| Output | Purpose |
|---|---|
| `sections/<section_id>.liquid` | **the deliverable** — the whole article as a theme-editor editable, instance-safe section |
| `SHOPIFY-CONFIG.json` | per-post knobs: hero copy, CTAs, image slots (alt/caption/focal), video anchor, product cards, slug, section name |
| `snippets/wipex-blog-schema.liquid` | the JSON-LD (never inside the section — see `references/10` §7) |
| `templates/article.<name>.json` | assigns the section to that post |
| `SHOPIFY-PASTE.html` | fallback for a store that does not use sections |
| `SHOPIFY-README.md`, `SHOPIFY-META.md`, `SHOPIFY-LIQUID.md`, `SHOPIFY-SCHEMA.json` | install path, admin fields, the Liquid variant, the schema alone |
| `SECTION-VALIDATION.txt` | the receipt |

## The bar

`SECTION-VALIDATION.txt` must read `RESULT: NONE` before anything is pasted into Shopify. It
checks, among others:

- Shopify's schema limits (name ≤ 25 chars, ≤ 40 settings, zero `@type` in the section);
- Liquid tag balance and **Liquid-safe prose** (the copy may not contain `{{` or `{%`);
- no external request in `<style>`/`<script>`, no inline handler, every link canonical;
- instance safety (no static id, `section.id` registry), ≥ 4 `data-cro` annotations;
- FAQ integrity (visible Q&A == FAQPage entities);
- **claims lint** against `assets/compliance/Never-Say-Prohibitions.csv` — a BLOCKING finding
  stops the build, even when the copy already passed the compliance phase.

---

## Compliance boundary — what is NOT in this repository

This repository is public, so the internal source documents are deliberately excluded:

- the Wipex Claims Filter review pack (`.docx`) and the Surface Claims Guide / Annex A (`.pdf`);
- the extracted plain-text copy of that pack;
- any internal contact, legal or regulatory correspondence.

What **is** published is the derived reference data the automation needs (`assets/compliance/*.csv`)
and the skill's own summary of the rules (`references/03`). The Claims Filter document itself is
not editable by this team: rule changes go to the compliance owner and return as a new version.

Similarly, `examples/blog-01-cost-per-table/` contains our own working documents derived from the
approved copy (claim envelope, compliance report). Delete that folder if the derived envelopes
should not be public either — nothing in the skill depends on it.

## Confidentiality of credentials

No credentials exist in this repository, by design: the generator is config-driven and the
per-post config carries only copy and public URLs.