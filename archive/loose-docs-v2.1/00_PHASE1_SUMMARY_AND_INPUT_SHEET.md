# WIPEX BLOG #1 — PHASE 1 DELIVERABLES (Agent 1A + 1B + 1C)

**Test run of Wipex Blog Generation Skill v2.1 — Model A (auto-everything)**
Run date: 2026-09-22/23 · Filter version: v1.1 · Market: US
Data provenance: Google Trends (live fetch, trends.google.com, geo=US and geo=BR) + live wipex.co product JSON + Claims Filter v1.1

---

## BRIEF (locked by owner)

```yaml
theme:            cost + labor + speed
target_buyer:     food-service operations
products:         Table Bussers Autumn (scented) + Table Bussers Unscented
seo_angle:        comparison intent + cost-per-use + operational efficiency
cta:              "Reduce Table Turnover Time"
calendar_hook:    Q4 (year-end)
model:            A (auto-everything)
```

---

## THE HEADLINE FINDING (changes the plan)

**Every product-level search term for this category has zero measurable Google Trends
volume in the US.** "restaurant table cleaning wipes", "restaurant table wipes",
"restaurant cleaning wipes", "table busser wipes" and "food service cleaning wipes"
all returned an empty time series (below Google Trends' minimum threshold) for both
`today 1-m` and `today 12-m`, and the same terms returned zero in Brazil.

The demand that *does* exist is **operational**, not product-driven:

| Live cluster | US trend now | Signal |
|---|---|---|
| "table turnover" | rising sharply | 1-m last 7d mean **32.9** vs prior mean 9.8; spike to **100 on Sep 20, 2026** |
| "restaurant staffing" | rising sharply | 1-m last 7d mean **46.4** vs first 7d 0; spike to **100 on Sep 21, 2026** |
| "cost per use" | stable-high | 1-m avg **66.8**, last 7d 69.4 — no seasonality loss |
| "busser" | high, seasonal | 12-m avg **70.1**, peaks late May–June (hiring season) |
| "table turnover" 12-m | seasonal | peaks Feb 8–14 (**100**), Apr 12–18 (96), Mar 1–7 (91) |

**Consequence:** the brief's CTA ("Reduce Table Turnover Time") is demand-aligned — it sits
on the only cluster that is actually moving. The blog must therefore **target the
operational cluster and pull readers to Table Bussers**, not target a product term that
nobody searches. This is the niche-specificity strategy working as designed, only more
extreme than the skill's own examples assumed.

---

## PHASE 1 DELIVERABLES IN THIS FOLDER

| File | Agent | Contents |
|---|---|---|
| `00_PHASE1_SUMMARY_AND_INPUT_SHEET.md` | — | this file: brief, findings, filled input sheet, GO/NO-GO |
| `01_AGENT_1A_TRENDS_KEYWORD.md` | 1A | Trends data (US + BR), LLM keyword scoring, recommended keyword set |
| `02_AGENT_1B_CLAIMS_PREFLIGHT.md` | 1B | claims matrix for the two SKUs, what IS and IS NOT usable, escalations |
| `03_AGENT_1C_AUDIENCE_FAQ.md` | 1C | food-service ops audience profile + FAQ outline |
| `raw/trends_*.json` | — | raw Google Trends payloads (evidence) |

---

## FILLED INPUT SHEET

```yaml
topic:            "How to reduce restaurant table turnover time"
                  (cost + labor + speed for food-service operations)
calendar_hook:    Q4 (year-end) — plus evergreen operational demand
blog_intent:      comparison  (comparison intent per brief)
cro_goal:         e_commerce
target_action:    Add to cart  (Table Bussers bucket / 2-pack / 4-pack case)
target_market:    US
primary_kw:       "restaurant table turnover"
secondary_kw:     ["table turnover rate", "table reset time", "restaurant cleaning cost per use"]
long_tail:        ["how to reduce table turnover time in a restaurant",
                   "restaurant table reset cost per use",
                   "front of house cleaning labor cost per table"]
primary_product:  Table Bussers® Plant-Based All-Purpose Cleaning Wipes | Autumn-Scented
sku_primary:      WX01126TN   ($36.99 / 400ct bucket; 2-pack WX01130TN $69.99; 4-pack WX01126TN-4 $119.99)
sku_secondary:    Table Bussers® Natural Unscented Cleaning Wipes  (WX72024TBB, same price ladder)
claim_codes:      primary N, S3, C v, Eco + NSF (scented only) · secondary N, S3, C v, Eco
                  → NEITHER SKU has code P (performance). Tier 3 only. No numbers. No comparisons.
cro_goal_note:    cost-per-use math from Wipex list prices only — no performance benchmark
publish_target:   2026-09-30
geo_primary:      CA, FL, TX (supported by Trends subregion data — see 1A)
```

---

## GO / NO-GO

**🟢 GO — with three conditions**

1. **Keyword pivot (automatic, Model A).** Primary keyword is the operational cluster,
   not a product term. Approved by the data; no owner action needed.
2. **Copy envelope is Tier 3 only.** Because neither Table Bussers SKU carries code `P`,
   the blog may contain **no number, no percentage, no "lab-tested", no "outperforms",
   no "better than"** about cleaning performance. "Comparison intent" is served through
   **cost and format comparison**, not efficacy comparison. See `02_AGENT_1B...`.
3. **Two live-site conflicts need Dean** before this blog ships (they also constrain our
   own product links). See `02_AGENT_1B...` §Escalations — summarised:

   - **EWG Verified®** is asserted on both Table Bussers product pages, but Part 4 v1.1
     shows `E = —` for both rows. Part 4 governs the copy; the rows need a v1.2 amendment
     or the pages need correcting.
   - **"Sustainable"** appears in the scented product title, which the Part 4 restriction
     column explicitly forbids ("no bare 'Sustainable'").

Neither is caused by this blog. Both affect what we can link to and repeat.

---

## WHAT I NEED FROM YOU (15 min — Phase 1 approval gate)

```yaml
approve_keyword:   accept "restaurant table turnover" as primary? (Y / override)
approve_products:  Autumn as primary + Unscented as secondary? (Y / override)
approve_angle:     cost-per-use + operational efficiency, comparison via cost/format only? (Y / override)
escalate_to_dean:  EWG + "Sustainable" findings — send now or batch at end? (now / batch)
```

On approval, Phase 2 starts (Model A = automatic): 2A copy → 2B SEO → 2C compliance → 2D images.