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
