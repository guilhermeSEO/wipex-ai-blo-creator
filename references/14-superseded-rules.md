# Superseded rules — the register that stops regressions

This file exists because the skill was consolidated from loose documents written at different stages
of the project. Some of their rules are still right, some were measured wrong, and two would be
actively harmful today (an invented certification claim and a performance promise).

**How to use it:** before reintroducing anything "we already decided", check here first. Each row
says what the old document claimed, what governs now, and where the governing rule lives. When a
rule changes again, edit the row — do not delete it, or the old version will come back.

---

## 1. Content shape

| Old claim | Governing rule now | Where |
|---|---|---|
| Body 1,800–2,200 words; "5–6 sections" | 3,000–4,500 words (measured mean 3,576); 14–22 H2s; 16 recurring modules | `08`, `SKILL.md` §house architecture |
| FAQ is one section among others (~7 topics) | FAQ is **mandatory**, 6–10 long-form Q&As | `08`, `SKILL.md` |
| 3 internal links total; "2–3 per 500 words" | 4–10 to `/products/` **and** 4–8 to `/blogs/` | `08` |
| "Case Study" listed as a blog type | the house publishes no case studies (21/21); restrict the intake to the measured types | `01`, `08b` |

## 2. Data honesty

| Old claim | Governing rule now | Where |
|---|---|---|
| "Estimated: 400–600 searches/month (US)" | Trends returns no absolute volume; volume comes from Marketing (SEMrush/Ahrefs/GSC) or is reported as **not captured** | `02` §2, `13` §6 |
| "Trend: ↑ +8.3%" presented as measured; windows "last 4 weeks / last 1 week" | relative index 0–100; windows `today 1-m` and `today 12-m`; momentum computed from the series | `02`, `11` |
| Illustrative volumes and conversion rates (18,200/mo, 12–18%, +18-25% CTR, "interest 58/100", "CA 23%") | usable as **shape**, never as values; label them illustrative or drop them | `02` §9, `12`, `13` §3 |
| Invented social proof: "200+ studios", "4.8/5 (247 reviews)", "92% reorder rate", `aggregateRating.reviewCount: 247` | never invent a rating, review, testimonial or count; `aggregateRating` only when real | `SKILL.md` non-negotiable 2, `06` |
| Expected gains as deliverables: CTR 8–18%, conversion 15–25%, "revenue lift 5–10x", "positions 1–5 in 60–90 days" | a projection is labelled as a projection and stays out of the copy | `06` §CRO guardrails |
| "CA, FL, TX mentioned? ✅" as the GEO check | GEO comes from the **measured** sub-regions in 1A; no geo-stuffing | `02` §2, `06` §GEO |

## 3. Claims and compliance

| Old claim | Governing rule now | Where |
|---|---|---|
| "APPROVED TIER 2: Removes 147% more residue than traditional quat-based wipes" on a SKU whose `P = —` | Tier 2 wording requires code `P`; without it there are **no numbers and no performance comparisons** | `03`, `SKILL.md` non-negotiable 3 |
| Meta title "Plant-Based Yoga Mat Wipes: 147% Better Cleaning" | "Better" is an unsupported comparative, and the 147% figure belongs to the fitness/EMPOWER formulations — it does not transfer | `03`, `13` |
| Product names used loosely (two different names for one SKU) | one canonical name per SKU, from Part 4 | `03` |
| "Don't transfer P" mentioned only as a footnote | a standing rule: identical-looking SKUs do not share codes | `03` §8 |
| Scented/unscented treated as interchangeable wording | `NSF` and the food-service sentence attach to the scented family only | `03` §8 |

## 4. Timing and gates

| Old claim | Governing rule now | Where |
|---|---|---|
| "publish ASAP", "in the next 2 weeks" because the trend is rising | **QUEUE until 2–4 weeks before the measured peak** (min 2 weeks, default ~1 month); occasion posts publish 7 days before | `02` §6, `09` |
| Timeline 1.5–4 days / "48 h" from brief to publish | the date is derived from the peak window and approved at Gate 2; the work is scheduled backwards from it | `02` §6, `00` |
| One human stop ("YOU REVIEW + APPROVE, 15 min") | Gate 1 (brief) + Gate 2 (compulsory: keyword, products, angle, **date**) + Gate 3 (publish) + the machine gate | `00` §3 |
| Models A/B/C = review cadence | models A/B/C = **stop points** (A: publish only · B: gates 2+3 · C: gates 1+2+3); red flags force C | `01` §8 |
| No cannibalisation check | mandatory ANGLE DELTA against the corpus, with the H2 registry as the instrument, plus a reciprocal link | `02` §5, `14`, `08b` |
| No zero-data branch (volume assumed to exist) | zero data is a first-class path with a STOP and an escalation | `02` §2, `13` §6 |

## 5. Technical

| Old claim | Governing rule now | Where |
|---|---|---|
| JSON-LD with `@type: [BlogPosting, FAQPage, Product]` + `geo: GeoShape` inside the section | BlogPosting + FAQPage + Product + BreadcrumbList, **never inside the section** (the validator counts `@type` keys as settings and breaks the 40 cap); prices from live product JSON; FAQ entities = the visible FAQ | `06`, `10` §7 |
| Section template with a 32-char name and a `richtext blog_content` setting | name ≤ 25 chars, ≤ 40 settings, config-driven, Liquid balanced — learned from a real failed save | `10` §2 |
| Fetch Trends by `GET trends.google.com/explore?q=…` (and `.com.br`) | the explore page is a JS app; server-side fetches return 429; use the in-browser internal API with the widget token; BR is not a market (measured zero) | `11`, `02` |
| `https://wipex.co/products.json` as the catalogue endpoint | does not exist; use `/products/<handle>.json` | `04` §4 |
| Scoring formula `(LLM-friendly×.4) + (low-competition×.3) + (rising×.3)` | canonical formula: semantic .25 + entity .25 + niche .15 + moat .15 + momentum .20 | `02` §3, `13` §3 |
| Chatty filler tolerated (5 forbidden terms) | 8 forbidden AI-isms (adds "game-changer", "in the realm of", "it's important to note") | `05` |

## 6. CRO, CTR and GEO claims that are not carried

| Old claim | Governing rule now | Where |
|---|---|---|
| Per-tactic uplift figures: "+8-12%", "+15-20%", "+4-7%" conversion boost per urgency element; "3x conversion rate"; "CTR 8–15%" | no uplift figure is quoted as a reason to do anything; projections are labelled and stay out of the copy | `06` §CRO guardrails |
| Invented proof: "200+ studios", "4.8/5 stars (247 reviews)", "92% reorder rate", "150+ studios verified", "Growing 35% YoY" | only counts, ratings and retention figures that exist, with their source | `06` §9, `SKILL.md` non-negotiable 2 |
| Authority by association: "Recommended by Yoga Alliance certified studios" | no endorsement claim without a logged amendment from compliance | `03`, `SKILL.md` escalation |
| The 147% figure used as a title hook and as an objection answer | the figure belongs to specific formulations and needs soil + surface + lab + benchmark; it is not a general proof | `03` §8, `14` §3 |
| State-by-state "GEO variants" of one post | rejected: duplicate content and self-cannibalisation, and each variant would need its own angle delta | `06` §16, `02` §5 |
| `geo_shape` / `ServiceArea` schema, "CA, FL, TX mentioned ✅" as the geo check | GEO = prose drawn from the measured sub-regions; no geo schema on a blog post | `06` §8, §16 |

## 7. Content shape


Everything here is preserved verbatim in the repository's `archive/` for provenance. The register,
not the archive, is what governs.

---

## 8. Documents that are now history

| Document | Status |
|---|---|
| `00_START_HERE.txt` | obsolete — onboarding for a build that finished; only "Model D — test all three" survives, as an intake variant |
| `SKILL_READY_CHECKLIST.txt` | obsolete — pre-build checklist; its input taxonomy is in `01` |
| `FINAL_CHECKLIST_v2.1.txt` | superseded except the per-phase hour budget (now in `00` §1); its "expected improvements" columns are projections and are not carried |
| `AGENT_2B_MASTER_PROMPT.md` | source of instruments, not of numbers — its E-E-A-T scaffold, citation triggers and snippet mold were folded into `06` §11–§13; every statistic in it must be re-derived |
| `SENIOR_SEO_AEO_STRATEGY.md` | same status — the frameworks are folded into `06`; the metric expectations in its dashboard are projections |
| `GEO_CRO_CTR_STRATEGY.md` | frameworks folded into `06` §11–§16; its uplift figures, invented proof and geo schema are rejected, and the reasons are recorded above |
| `WIPEX_BLOG_V2.1_COMPLETE_WORKFLOW.md` | the calculator spec is folded into `07`, the claim-report format into `03`; its claim codes are wrong |
| `GOOGLE_TRENDS_INTEGRATION.md` | 85% superseded by `11`; the signal→family curation table survives in `02` §12 |
