# CLAIMS REVIEW — live page text (Blog 02)
Multi-Location Cleaning Supply Procurement · Claims Filter v1.1 (Annex A A-009)
Reviewed 2026-09-29 · reviewer: skill `wipex-claims-compliance-review`
Source of truth for the scan: `_live-page-audit-2026-09-29.txt` (the page text as supplied by the owner)

---

## 1. Executive summary

**The post itself is clean.** Every one of the 18 Never-Say prohibitions was probed over the live
text: **0 hits** on the copy. No T1 claim (nothing regulated), **no T2 claim** (no performance
number, no comparison, no lab wording), no certification asserted outside its Part 4 row, no
benchmark brand named, no priced promise.

**But the review cannot sign off on the page**, for two reasons found outside the post's copy:

1. **"Plant a Tree & Save 10%" is on the page and is not in Dean's approved claim set** — an
   eco/sustainability claim plus a discount offer. It is a site-wide element (it sits after the
   sticky CTA, not in the blog section), but Part 7 reviews the page, not the module.
2. **The live copy contains two strings the cleared artifact does not produce** —
   *"is not necessary a bigger order"* and *"Our average cost per wipe…"*. The compliance clearance
   covers the generated artifact; where the live text differs, **the clearance no longer covers what
   is live** (and the first one is broken English).

| Severity | Count |
|---|---|
| BLOCKING | 0 |
| HIGH | 0 |
| MEDIUM | 2 |
| LOW / advisory | 3 |
| In scope but **not supplied** | 4 surfaces |

**Publication-ready?** The blog section: yes. The page: after (a) re-pasting the artifact so the
live copy matches the cleared one, and (b) Dean being made aware of the site-wide
"Plant a Tree & Save 10%" element.

---

## 2. Violations & findings

### F1 — MEDIUM · eco + discount claim, site-wide, outside the approved set
- **Location:** bottom of the page, after the sticky CTA (`Subscribe now → ×`). **Not** produced by
  the blog section — 0 occurrences in `sections/wipex-section-multi-location-procurement-2026.liquid`.
- **Current text:** `Plant a Tree & Save 10%`
- **Issue:** "Plant a Tree" is an environmental/sustainability claim. The Filter prohibits **bare**
  sustainability claims (Never-Say #19 pattern: bare "Sustainable") and the approved set
  (`Approved-Surface-Claims-16-Sentences.csv`) contains **no** eco or tree-planting claim for any SKU.
  "Save 10%" is a promotional discount claim — permitted only if it is a real, current offer.
- **Rule cited:** Never-Say #17/#19 (bare packaging/sustainability claims) · approved set has no
  eco-claim row · owner pricing rule (a discount comes from a subscription or a discount already live
  on the product page).
- **Fix:** route to **compliance (Dean) for awareness** and to whoever owns the site-wide banner.
  Do not echo the phrase inside the post.
- **Who fixes it:** not this deliverable. It is a theme/app element.

### F2 — MEDIUM · live copy ≠ cleared artifact
- **Location:** the closing section, and the value strip.
- **Current text (live):**
  - `A multi-location program is not necessary a bigger order.` — artifact has `is not a bigger order`
  - `Our average cost per wipe on the bulk refill roll` — artifact has `Our cost per wipe on the bulk refill roll`
- **Issue:** the cleared copy is the **generated artifact**. Retyped or edited copy stops matching the
  compliance report, which is the one invariant the workflow exists to protect. The first string is
  also ungrammatical ("not necessary a bigger order" — the original meaning was "not a bigger order").
- **Evidence:** `not a bigger order` ×1 in the section, ×0 `not necessary`; `average` ×0 in both the
  config and the section.
- **Fix:** re-paste the artifact, or clear the edit wherever it was introduced. Both strings are
  **not claims**, so this is an integrity defect, not a Filter violation.
- **Who fixes it:** the operator.

### F3 — LOW · comparative cost figure
- **Location:** key takeaway 6.
- **Current text:** `…the pallet pack about $0.05 — roughly half a bucket's unit cost.`
- **Issue:** a comparative numeric — but it compares **our own cost per wipe across our own pack
  sizes**, not cleaning performance. Cost arithmetic is permitted (envelope §2 "Cost figures as price
  units"). No performance wording is adjacent.
- **Verdict: keep.** Flagged only so the next reviewer does not read "half a bucket's cost" as an
  efficacy comparison. No "X% over" construction is used (Never-Say #4 clean).

### F4 — LOW · "Sustainability-graded sites" as a label
- **Location:** decision tool card 3, and the formats table row 3.
- **Issue:** "sustainability" here is a **site-category descriptor** (a site that grades
  sustainability), not a claim about a product. As written it is not a product claim.
- **Verdict: keep — with awareness.** A naive scanner will trip on it, and escalation **E1** (the live
  Table Bussers *title* carries bare "Sustainable", which the Part 4 restriction column forbids)
  makes the word sensitive site-wide right now. The wording does not repeat or endorse that badge.

### F5 — LOW · default video-fallback alt text does not fit this post
- **Location:** alt text under the video band: `Wipex food service wipes in use`
- **Issue:** not a claim (and "food service" is not "food-safe"). But this is a **mixed** multi-location
  post; the alt text describes food service only.
- **Fix (optional):** set a footprint-neutral alt for this post when the media is filled.

---

## 3. In scope but NOT supplied — cannot be certified from this paste
Per Part 7 these are in scope and are routinely left out of a paste. Our artifact's values are cleared
(2C REVISION f), but **what is live was not supplied**:

| Surface | Status |
|---|---|
| Meta title | not supplied |
| Meta description | not supplied |
| URL handle | not supplied |
| FAQ **answer** bodies (8) | not supplied — the accordion shows only the questions |

Say so in any sign-off: this review certifies the visible body, not those four surfaces.

---

## 4. Sections that passed

- **Never-Say list — 0 hits** across all 18 rows: no "safe on/for", "proven", "outperforms", "X% over",
  "lab-tested/verified", kills/hygienic/sanitary/disinfect/antibacterial/antimicrobial/germ wording,
  "won't damage", "% natural", superlatives (best/safest/most effective/strongest/#1/ultimate),
  "recommended by/used by/endorsed by", FDA-approved, hospital-grade, food-safe/food-grade/
  food-contact, bare compostable/biodegradable, eco-friendly/sustainable packaging, bare "Sustainable".
- **"Zogics" (and every benchmark brand) appears nowhere.**
- **No T1 claim.** The piece is procurement copy, not health copy — nothing regulated.
- **No T2 claim.** No cleaning-performance number, no comparative, no lab wording. The TURI §6
  approved sentences are **not** used (correct — Table Bussers has `P = —`).
- **Certifications scoped exactly:** NSF → scented Table Bussers only; EWG Verified → Plant-Based row
  only (never Table Bussers, whose `E = —`); cloth-substrate (`C`) → "the certified cloth-substrate
  wording", scoped, no bare "compostable".
- **"suitable for food service environments"** used verbatim, scented line only, no "perfect for",
  no "food-safe".
- **Cost figures stay in cost paragraphs**, recomputed from list prices, with the source sentence for
  the third-party statistics present in the copy (Metro Wholesale, checked 2026-09-28).
- **The patch-test line is present:** *"If in doubt, test on a small, inconspicuous area first."*
- **No pricing promise** — 0 occurrences of the removed volume-tier argument; the copy now states
  "The price is the price on the product page".
- **No `aggregateRating`, no invented testimonial, no pending/submitted certification status.**

---

## 5. Compliance note (Part 9.3)

```yaml
products_named: Natural Fitness Equipment Wipes 700ct Bulk Refill Roll · Table Bussers® Surface
                Wipes (scented autumn) · Plant-Based 700ct Bulk Refill Roll (viscose) ·
                Wall/Floor/XL Bucket Dispensers · (generic "all-purpose and touchscreen-compatible
                wipes" — no SKU, no claim)
controlled_terms_used_and_permitting_code:
  - "suitable for food service environments" -> NSF / A-004, scented Table Bussers only
  - "NSF-certified" -> scented Table Bussers row
  - "EWG Verified" -> E v (Plant-Based row only; not asserted for Table Bussers)
  - "the certified cloth-substrate wording" -> C v
  - "plant-based" / "Plant-Based" -> Eco (substrate wording only)
certifications_asserted: NSF (scented Table Bussers, page-verified 2026-09-28) · EWG Verified
                         (page-verified) · cloth-substrate cert (page-verified)
comparative_numeric_claims: NONE on cleaning performance. The only comparatives are our own cost
                            per wipe across our own pack sizes, and the cited third-party cost stats
pricing_position: no price promise; pack size is the stated lever; discount paths named are a
                  subscription and a discount already on the product page
page_level_findings_not_in_the_post: "Plant a Tree & Save 10%" (site-wide element, F1)
live_copy_drift: 2 strings the cleared artifact does not produce (F2)
not_supplied_in_scope_surfaces: meta title · meta description · URL handle · 8 FAQ answers
new_escalations: F1 -> compliance (Dean), awareness only (the element is not ours to change)
standing_escalations: E1 (bare "Sustainable" in the live Table Bussers title) · E2 (EWG asserted on
                      Table Bussers pages vs E = —) — awareness only, unchanged
filter_version: 1.1
page_verified: 2026-09-28
reviewed_live_text: 2026-09-29
```

**Bar to publish: zero BLOCKING — MET for the post.** Page-level: see F1 and F2.
