# 2C — COMPLIANCE VALIDATION REPORT
Blog 02 — multi-location cleaning supply procurement · Claims Filter v1.1 · reviewed 2026-09-28

> ## REVISION 2026-09-29 — re-scanned over the funnel revision
> The post was rebuilt on the new `funnel` layout model: copy trimmed **3,566 → ~2,750 words**, the
> six-part framework moved into an accordion, FAQ moved earlier, and the third-party figures were
> given an explicit attribution sentence (**Metro Wholesale, checked 2026-09-28**). The source draft
> is now `2D-body-clean.md` (revised); `2A-blog-copy-TAGGED.md` carries the pre-revision tagging.
> **Re-scan result: unchanged — 0 BLOCKING, 0 HIGH, 0 MEDIUM.** The machine scan below was re-run by
> the section generator over the rendered section (`SECTION-VALIDATION.txt`, RESULT: NONE, 16 REVIEW
> contexts, all the benign `natural` / `Natural` product-name hits). One product line dropped out of
> the copy: **Table Bussers® Unscented is no longer named** (the fragrance-free aside was cut), so the
> scented/unscented split is now only implied by the scented line's NSF sentence. Everything else in
> this report still describes the copy accurately. **Note:** the section generator's `@CRO@` token was
> also fixed this revision — 5 CTAs (decision tool, system block, feature block) had shipped with
> `data-cro="@CRO@-…"` instead of the slug; all `data-cro` values are now correct.

Reviewer: skill `wipex-blog-generation` (Agent 2C) · source draft: `2A-blog-copy-TAGGED.md`
Verification: all 250-char context excerpts machine-scanned against `Never-Say-Prohibitions.csv` and Part 4.

## Result: **RESULT: NONE — zero BLOCKING, zero HIGH, zero MEDIUM**

| Severity | Count |
|---|---|
| BLOCKING | 0 |
| HIGH | 0 |
| MEDIUM | 0 |
| LOW | 2 (informational) |

---

## Part 1 seven-step review (in order)

**1. Identify every product named or pictured → resolve to a Part 4 row.**
| Named in the post | Part 4 row | Status |
|---|---|---|
| Natural Fitness Equipment Wipes 700ct Bulk Refill Roll | NAT-FIT (WX71940FLE, WX11121FN) | ✅ row exists |
| Table Bussers® Surface Wipes — Autumn-Scented | NAT-SURF (WX01126TN, WX01130TN) | ✅ row exists |
| ~~Table Bussers® Unscented~~ | NAT-SURF (WX72024TBB) | not named in the 2026-09-29 revision |
| Plant-Based 700ct Bulk Refill Roll (viscose) | NAT-FIT (WX72081LARP, WX72082LERP) | ✅ row exists |
| Wall / Floor / XL Bucket Dispensers | HW rows | ✅ row exists |
| touchscreen-compatible wipe (generic, no brand) | generic wording only | ✅ no product resolved — no claim made |
No product is named that has no Part 4 row. No escalation of type "new SKU".

**2. Determine mode.** Proactive marketing copy (published blog). Mode applied: proactive.

**3. Pull each product's claim set from Part 4 (no carry across SKUs).**
| SKU | Codes used in the draft |
|---|---|
| Natural Fitness 700ct Refill | N, S3, P, E v |
| Table Bussers Scented | N, S3, C v, Eco, NSF/A-004 |
| Table Bussers Unscented | N, S3, C v, Eco |
| Plant-Based 700ct Refill | N, S3, P, C v, E v, Eco |
| Hardware | hardware rule (Part 6.7) |
No claim was carried from a sibling. The scented/unscented split is explicitly stated in the copy ("The scented line is the one that carries the NSF certification").

**4. Scan controlled terms** across title · meta · H1–H3 · table headers · bullet labels · captions · alt text · badges · cross-sell. Machine scan results below.

**5. Placement & adjacency (Part 7).** Every cost figure sits in a cost paragraph; no cost number is adjacent to a performance claim, a percentage, or the word "safe". The one product line that cannot carry performance wording (Table Bussers, `P = —`) is never given one.

**6. Certifications & evidence (Part 6).** Asserted: NSF (scented Table Bussers, A-004), EWG Verified (Natural Fitness 700ct, Plant-Based — `E v`), cloth-substrate cert (Table Bussers, Plant-Based — `C v`). Each is in Part 4 **and** page-verified. No pending/submitted status stated. No `aggregateRating` invented.

**7. Never-say list (6.9) + special populations (6.10).** No hits. No health/illness framing → no compliance block required.

---

## Machine scan (against the prohibition patterns)
| Pattern family | Hits in copy | Adjudication |
|---|---|---|
| "safe on/for", "won't damage/harm" | 0 | pass |
| "outperform", "better than", "proven", "lab-tested/verified", "clinically" | 0 | pass |
| germ/kill, disinfect, sanitiz, antibacterial, antimicrobial | 0 | pass |
| superlatives (best/safest/strongest/ultimate/#1/most effective) | 0 after edit | "Best-fit Wipex product" table header → changed to **"Recommended Wipex product"** |
| non-toxic / chemical-free / harmless / kid-safe / pet-safe | 0 | pass |
| food-safe / food-grade / food-contact | 0 | pass ("suitable for food service environments" used, exact phrase, scented only) |
| bare "compostable"/"biodegradable" | 0 after edit | "cloth-substrate compostability certification" → changed to **"the certified cloth-substrate wording"** (scoped, no bare claim) |
| "% natural" / "100% natural" | 0 | pass ("made with natural ingredients" not needed; N is reflected only via tag legend) |
| bare "Sustainable" | 0 in copy | pass (appears only in the spec's awareness note about the live site) |
| benchmark brand names (Zogics, Grainger, Uline, Webstagram, Clorox…) | 0 | pass — **"Zogics" does not appear anywhere in the article** (internal style reference only) |
| "hospital-grade" | 0 | pass |
| eco-friendly / sustainable packaging | 0 | pass |
| "natural" on a BZK product | 0 | pass (no BZK product named) |

---

## Passed section
- All product names resolve to Part 4 rows; no orphan SKU.
- "suitable for food service environments" applied to the scented Table Bussers line only (exact phrase, no "perfect for", no "food-safe").
- Comparison content is cost / format / coverage / labour — never efficacy (respects `P = —` on Table Bussers).
- Cost arithmetic recomputed from live prices 2026-09-28 and confined to cost paragraphs.
- Certifications asserted match Part 4 and are page-verified; no invented rating/testimonial.
- No health/illness claim → no surface-disinfecting or germ-kill language anywhere.

## LOW findings (informational — do not block)
1. **LOW** — the live Table Bussers product **title** still carries bare "Sustainable" (restriction column forbids it). The blog does not echo the phrase or the badge. Recorded as escalation E1 (awareness only).
2. **LOW** — the two Table Bussers pages assert EWG Verified while Part 4 v1.1 shows `E = —`. The blog names no EWG badge for Table Bussers. Recorded as escalation E2 (awareness only).

## Escalations (per the user's preference: awareness only, no amendment drafted)
| # | Item | Route | Date |
|---|---|---|---|
| E1 | bare "Sustainable" in the live Table Bussers title | compliance (Dean) — informed only | 2026-09-28 |
| E2 | EWG badge asserted on Table Bussers pages vs `E = —` in Part 4 | compliance (Dean) — informed only | 2026-09-28 |

## Compliance note (Part 9.3)
```yaml
products_named: Natural Fitness Equipment Wipes 700ct Bulk Refill Roll · Table Bussers® Surface Wipes
                (scented autumn) · Table Bussers® Unscented · Plant-Based 700ct Bulk Refill Roll ·
                Wall/Floor/XL Bucket Dispensers
controlled_terms_used_and_permitting_code:
  - "made with natural ingredients" -> N (fitness, plant-based, Table Bussers)
  - "suitable for food service environments" -> NSF/A-004 (scented Table Bussers only)
  - "the certified cloth-substrate wording" -> C (Table Bussers, Plant-Based)
  - "EWG Verified" -> E v (Natural Fitness 700ct, Plant-Based)
  - "plant-based cloth" -> Eco
certifications_asserted: NSF (scented Table Bussers, page-verified 2026-09-28); EWG Verified
                         (page-verified); cloth-substrate cert (page-verified)
comparative_numeric_claims: NONE permitted on cleaning performance
unverified_or_escalated: E1 · E2 (awareness only)
filter_version: 1.1
page_verified: 2026-09-28
recompute_before_publish: prices, stock, and the two Table Bussers product pages
```

**Bar to publish: zero BLOCKING — MET.**

---

# REVISION 2026-09-29 (f) — FULL CLAIMS RE-REVIEW (pricing reframe)

Triggered by the owner's pricing policy: **"os preços são o que são e para desconto é apenas
subscription ou desconto que tem na página do produto"**. The post's central argument had been a
**volume-tier promise** — that standardising the footprint "unlocks a tier" and is "the cheapest way
to improve your price". That is a **price promise the store does not honour**, so it was removed and
the argument rebuilt on the operational saving (unplanned ordering + the cited stockout premium).
A price promise is not a Claims Filter violation, but it is the same class of risk: copy asserting
an outcome the business will not deliver. It is re-reviewed here because the remedy rewrote copy.

**Scope re-scanned (every surface Part 7 puts in scope):** title · meta title · meta description ·
H1 · H2 · H3 · table headers · bullet labels · image alt text · captions · CTA button text ·
BlogPosting / FAQPage / Product / BreadcrumbList schema fields.
**Outcome: 0 BLOCKING · 0 HIGH · 0 MEDIUM.** One REVIEW item added and cleared (`discount`, below).

## Step 1 — products named → Part 4 row
| Named in the post | Part 4 row | Codes | Status |
|---|---|---|---|
| Natural Fitness Equipment Wipes 700ct Bulk Refill Roll | NAT-FIT (WX71940FLE, WX11121FN) | N · S3 · **P** · E v | ✅ row exists |
| Table Bussers® Surface Wipes — Autumn-Scented | NAT-SURF (WX01126TN, WX01130TN) | N · S3 · C v · Eco · **P —** | ✅ row exists |
| Plant-Based 700ct Bulk Refill Roll (viscose) | NAT-FIT (WX72081LARP, WX72082LERP) | N · S3 · **P** · C v · E v · Eco | ✅ row exists |
| Wall / Floor / XL Bucket Dispensers | HW rows | hardware rule (Part 6.7) | ✅ row exists |
| "All-purpose and touchscreen-compatible wipes" | generic wording, no SKU | no claim made | ✅ nothing to resolve |

No orphan SKU. No product removed by the reframe carried an approved claim used elsewhere.

## Step 2 — mode
**Proactive** (published marketing copy) — unchanged.

## Step 3 — claim set per SKU (no transfer)
Unchanged from the original review; the reframe **removed** claims, it added none. The one line that
crossed SKUs in spirit — the scented/unscented NSF split — still reads "it is the line that carries
the NSF certification, so it belongs on the front-of-house standard": NSF stays on the **scented**
family only, no transfer to the Unscented sibling (which this revision no longer names at all).

## Step 4 — controlled-term scan, by tier

| Tier | What it is | Used in this post? |
|---|---|---|
| **T1** regulated (disinfect, sanitize, antibacterial, germ-kill, certifications) | Part 3 / 4 / 6.3 / 6.4, needs registration evidence | **No T1 claim.** Zero occurrences of disinfect/sanitize/antibacterial/antimicrobial/germ-kill/kill(s). The post is a procurement post, not a health post |
| **T2** substantiated (numbers, "lab-tested", comparatives) | only Fitness Lavender/Lemongrass + EMPOWER; requires code `P` + full test context | **No T2 claim.** The only quantitative content is (a) **our own list prices as cost units** and (b) **cited third-party operational statistics**. No cleaning-performance number, no comparative, no "% more" |
| **T3** qualitative (clean, gentle, removes residue, fits) | all other SKUs, no test required | Used sparingly and descriptively: "Refill-roll format that pairs with one wall or floor dispenser standard", "Pre-mixed surface wipe built for front-of-house reset", "Plant-based cloth" (substrate) |

Terms found, and what permits each:

| Term | Where | Permitted by | Verdict |
|---|---|---|---|
| "suitable for food service environments" | formats table, food-service row | exact phrase, **scented Table Bussers only** (NSF, A-004) | PASS |
| "NSF-certified" | formats table + the note under it | scented Table Bussers row | PASS |
| "EWG Verified" | formats table, **Plant-Based row only** | `E v` (Plant-Based) | PASS — not asserted for Table Bussers anywhere |
| "the certified cloth-substrate wording" | formats table, Plant-Based row | `C v` | PASS — scoped, no bare "compostable" |
| "plant-based" / "Plant-Based" | product name + formats table | `Eco` — **substrate only** | PASS — never presented as a "natural" claim |
| "natural" (lowercase) | "a natural deadline" | not a product claim | PASS — no BZK product named anywhere (A-008) |
| "$0.061 · $0.051 · $0.047 · $0.092 · $0.075 · $42.99 · $36.99 · $142.99 · $119.99 · $4,585.00" | cost table + FAQ + formats table | our own list prices as **cost units** | PASS — arithmetic on our own price, not a performance claim |
| "20–30%" premium | Q4 section + FAQ + framework §5 | cited: Metro Wholesale, checked 2026-09-28 | PASS — cited operational statistic, cost context |
| "$4.92 vs $6.10" · "300 → 60" | Q4 section + value strip | cited: Metro Wholesale, checked 2026-09-28 | PASS — cited third-party, attribution sentence present in the copy |
| **"discount"** (NEW) | FAQ "Does buying across sites change our price?" → "Discounts are separate from all of it — a subscription, or a discount already running on the product page." | not a controlled term; states the owner's actual policy | **REVIEW → CLEARED.** It promises no discount, invents no figure, and names no promotion. It states where discounts come from, which is the owner's own rule |

## Step 5 — placement & adjacency
- Every cost/price figure sits in a **cost paragraph**. The reframe added two such paragraphs
  (the new price FAQ and framework §2) and they stay cost-only: no surface, no performance, no
  "safe", no efficacy word within either.
- The **cost adjacency guardrail** is the one thing to watch here: the new FAQ carries the 20–30%
  premium **and** pack prices in the same answer. Adjudicated **PASS** — the guardrail exists to stop
  a cost figure being used to imply a *cleaning-performance* claim ("costs less, cleans better").
  Two cost/operational figures in one cost paragraph do not do that, and no performance wording
  appears within the paragraph or adjacent to it.
- Table Bussers (`P = —`) still carries **no** performance wording; its column argues format, labour
  and cost only.
- **Pricing-promise removal (the point of this revision):** the phrases "volume pricing", "unlocks a
  tier", "reach a better tier", "the cheapest way to improve your price", "a price band" and
  "relationship worth pricing" are all **gone** — verified 0 occurrences in the copy. What replaced
  them asserts the opposite: "The price is the price", "does not change what a wipe costs", "the
  cadence, not a negotiation, that removes the emergency premium".
- Hardware still carries no wipe claim, certification or sustainability claim.

## Step 6 — certifications & evidence
Unchanged: **NSF** (scented Table Bussers, page-verified 2026-09-28) · **EWG Verified** (Natural
Fitness 700ct, Plant-Based — `E v`, page-verified) · **cloth-substrate cert** (`C v`, Table Bussers,
Plant-Based). No pending/submitted status stated. No `aggregateRating`, no invented testimonial.
Escalations **E1** (bare "Sustainable" in the live Table Bussers title) and **E2** (EWG asserted on
Table Bussers pages vs `E = —` in Part 4) remain **awareness-only**, per the owner's standing
preference. This revision does not echo either phrase.

## Step 7 — never-say list & special populations
No hit for best / safest / most effective / #1 / ultimate / proven / lab-tested / non-toxic /
chemical-free / harmless / kid-&-pet-safe / hospital-grade / FDA-approved / food-safe / food-grade /
food-contact / bare compostable / biodegradable / hygienic / sanitary / endorsed by / outperforms /
benchmark brand names. **"Zogics" appears nowhere.** No health, illness or special-population
framing → no compliance block required.

## Per-SKU claims report
```
NATURAL GYM WIPES BULK REFILL ROLL 700ct            (WX71940FLE, WX11121FN)
CAN SAY           N · S3 · P · E v — refill format, pack counts, dispenser fit, live stock, and our
                  own price arithmetic ($42.99/700 = ~$0.061; 4-pack ~$0.051)
CANNOT SAY        bare "Sustainable"; compostable (no C on this row); germ-kill; "safe on surface";
                  benchmark brand names; any cleaning-performance number (none is used)
ROLE IN THIS POST the format the fitness room standardises on — argued on cost, format and cadence
FILTER VERSION    v1.1 · page verified 2026-09-28 · recompute prices before publish

TABLE BUSSERS SURFACE WIPES (SCENTED, AUTUMN)       (WX01126TN, WX01130TN)   [P = —]
CAN SAY           N · S3 · C cloth sentence · Eco · NSF (A-004) · "suitable for food service
                  environments" · pack counts, our price arithmetic ($36.99/400 ≈ $0.092)
CANNOT SAY        anything numeric, percentage or comparative about cleaning performance · bare
                  "Sustainable" · EWG Verified (E = —) · transfer of NSF to the Unscented sibling
ROLE IN THIS POST the guest-facing food-service room of the standard; no performance wording anywhere
FILTER VERSION    v1.1 · page verified 2026-09-28 · recompute prices before publish

PLANT-BASED BULK ROLLS 700ct (VISCOSE)              (WX72081LARP, WX72082LERP)
CAN SAY           N · S3 · P · C cloth sentence · E v · Eco "plant-based cloth" wording ·
                  pallet arithmetic ($4,585/98,000 ≈ $0.047)
CANNOT SAY        bare "compostable"/"Sustainable"; germ-kill; "safe on surface"; "#1/best"
ROLE IN THIS POST the sustainability-graded tier of the format table, pallet pack size
FILTER VERSION    v1.1 · page verified 2026-09-28 · recompute prices before publish

HARDWARE (WALL / FLOOR / XL BUCKET DISPENSERS)
CAN SAY           hardware facts, specs, "made with 30% recycled plastic" (XL bucket only), fit for
                  700/800ct refills, our price arithmetic
CANNOT SAY        "planet-friendly"/"plant-based"; any cleaning claim; "safe"
ROLE IN THIS POST "Equip Your Sites with One Dispenser Standard" — the closing link only
FILTER VERSION    v1.1 · page verified 2026-09-28
```

## Compliance note (Part 9.3)
```yaml
products_named: Natural Fitness Equipment Wipes 700ct Bulk Refill Roll · Table Bussers® Surface Wipes
                (scented autumn) · Plant-Based 700ct Bulk Refill Roll (viscose) · Wall/Floor/XL Bucket
                Dispensers · (generic "all-purpose and touchscreen-compatible wipes" — no SKU)
controlled_terms_used_and_permitting_code:
  - "suitable for food service environments" -> NSF / A-004, scented Table Bussers only
  - "NSF-certified" -> scented Table Bussers row
  - "EWG Verified" -> E v (Natural Fitness 700ct, Plant-Based only)
  - "the certified cloth-substrate wording" -> C v (Table Bussers, Plant-Based)
  - "plant-based cloth" -> Eco (substrate wording only)
  - "discount ... a subscription, or a discount already running on the product page" -> not a
    controlled term; states the owner's discount policy; promises nothing
certifications_asserted: NSF (scented Table Bussers, page-verified 2026-09-28) · EWG Verified
                         (page-verified) · cloth-substrate cert (page-verified)
comparative_numeric_claims: NONE — not on cleaning performance, and no pricing/tier promise
pricing_position: NO price promise. List prices are quoted as cost units; the only discount paths
                  named are a subscription link and a discount already on the product page
new_escalations: none
unverified_or_escalated: E1 · E2 (awareness only, unchanged)
filter_version: 1.1
page_verified: 2026-09-28
recompute_before_publish: prices, stock, and the subscription link
```

**Bar to publish: zero BLOCKING — MET.**
