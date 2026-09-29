# 1A — DEMAND, KEYWORD, PRODUCT
Blog: Multi-location wipe procurement program · measured 2026-09-28 · geo US + BR
Raw evidence: `raw/trends_2026-09-28.json`

## Demand (measured, geo US, 2026-09-28)
Index is relative per term; averages are NOT comparable across terms. No absolute volume exists here.

| Term | 1-m avg | 1-m last7 | 12-m avg | Top weeks (index) | Verdict |
|---|---|---|---|---|---|
| wholesale cleaning wipes | ZERO | — | 1.9 | (single spike Nov 9–15 2025) | **dead** |
| multi-location cleaning supplies | ZERO | — | ZERO | — | **no demand** |
| facility cleaning supplies | 10.0 | 9.3 | 2.8 | Sep 28–Oct 4 2025 (100) | **thin** (one-off spike) |
| wholesale cleaning supplies | 13.0 | 19.1 | 41.5 | Apr 12–18 (100), Feb 15–21 (95), Jan 25–31 (90) | solid, spring |
| commercial cleaning supplies | 15.8 | 27.7 | **61.1** | Apr 26–May 2 (100), Mar 1–7 (99), Apr 12–18 (99) | **strong baseline** |
| bulk cleaning supplies | 17.5 | 38.0 | 35.0 | Feb 22–28 (100), Apr 5–11 (97) | rising now |
| bulk wipes | 33.0 | 60.3 | 30.5 | Apr 12–18 (100), Apr 5–11 (98), May 17–23 (85) | rising now (Sep 15 = 100) |
| janitorial supplies | 24.9 | 29.6 | **57.7** | Jul 5–11 (100), Jun 7–13 (94) | strong |
| commercial wipes | 22.2 | 35.6 | 24.3 | Apr 12–18 (100), May 17–23 (100) | rising now |
| cleaning supplies cost | 27.8 | **63.6** | 50.2 | Mar 8–14 (100), Dec 7–13 (86), Nov 30–Dec 6 (85) | **Q4-seasonal, rising now** |
| cost per use | 67.4 | 68.3 | 41.6 | Nov 30–Dec 6 (100), Dec 7–13 (83) | **polluted** (see below) |
| office cleaning | 40.8 | 28.4 | 51.7 | Jun 14–20 (100), Nov 16–22 (86) | service intent, not procurement |

**Related-query clusters (intent check):**
- `commercial cleaning supplies` → "commercial cleaning supplies near me:100" — commercial, clean.
- `janitorial supplies` → near me:100 · wholesale janitorial supplies:44/49 · commercial janitorial supplies:40/56 · **bulk janitorial supplies:90 (rising)** — clean commercial cluster.
- `wholesale cleaning supplies` → "wholesale cleaning supplies near me:110 (rising)" — clean commercial.
- `bulk cleaning supplies` → "bulk cleaning supplies near me:100 / 40 (rising)" — clean commercial.
- `cost per use` → "what is a use case:100 · ai news today:70 · openai news:61 · how to use airpods" — **SEMANTIC POLLUTION. Rejected as a ranking bet** (references/02 §13). It is the highest-average term in the set and it fails the test.

**Brazil:** all five probed terms returned zero (or 1.9 for wholesale cleaning wipes / bulk wipes). BR is not a market for this topic. US-only.

## Zero-data terms (explicit — apply the pivot branch, references/02 §2)
- `wholesale cleaning wipes` — empty 1-m, ~0 12-m.
- `multi-location cleaning supplies` — empty 1-m AND 12-m (US and BR).
- `facility cleaning supplies` — thin (avg 2.8; a single historical spike).

## Recommended keyword set
```
primary:        commercial cleaning supplies     LLM 3.8/5   trend: 12-m avg 61.1, stable-high baseline
niche headline: multi-location / franchise wipe procurement program  (no measurable demand -> NOT the ranking bet; it is the differentiator in H1/body)
secondary:      bulk cleaning supplies · janitorial supplies · wholesale cleaning supplies · bulk wipes · commercial wipes
LSI:            reorder point / par level · MOQ · volume tier · SKU consolidation · recurring delivery · dispenser standardization · cost per wipe · cost per use
topical only:   cost per use (highest avg BUT polluted + saturated -> coverage, never the bet)
avoid:          wholesale cleaning wipes (dead) · multi-location cleaning supplies (zero) · facility cleaning supplies (thin)
```
**LLM formula limit (stated):** scores the keyword, not the market. A keyword with a live series but a small absolute base is still small; absolute volume is a Marketing input (SEMrush/GSC) we do not have.

## Corpus saturation + semantic-pollution tests
- `cost per wipe` appears in **16 of 21** live posts (references/02 §14) — saturated. The delta is the **unit and the stage**, not a new adjective.
- `cost per use` fails the pollution test (related = AI/tech) → not a primary.

## Calendar + intent validation
```
trend now: commercial cleaning supplies stable-high; cost cluster rising into Nov (last7 63.6)
hook:      Q4 (fiscal/budget year-end procurement cycle)
verdict:   GO / PLAN -> QUEUE toward the Q4 window (see Date targeting)
```

## GEO signals
Top subregions (caveat: small states over-index on thin absolute volume): commercial cleaning supplies → WY, RI, DC, ID; janitorial supplies → FL, NY, CA, LA; bulk cleaning supplies → KS, IA, LA, AL. Concentrated in high-density commercial states (NY/CA/FL) once size-adjusted — consistent with a multi-location buyer.

## Product match (mixed-facility program)
| Layer | Part 4 canonical | SKU | Codes | Price ladder | Fit | Why |
|---|---|---|---|---|---|---|
| primary | Natural Gym Wipes Bulk Refill Roll 700ct — Original XL (meltblown) | WX71940FLE, WX11121FN | N · S3 · **P** · E v | $42.99/700 · $142.99/2,800 (4-pk) | 4.6 | the refill-roll format that IS a program; `P` lets material-compatibility/most surfaces be named |
| food service | Table Bussers® Surface Wipes (scented, autumn) | WX01126TN, WX01130TN | N · S3 · C v · Eco · **P —** | $36.99/400 · $69.99/800 · $119.99/1,600 | 4.4 | NSF permitted (A-004); "suitable for food service environments" |
| sustainability tier | Plant-Based Bulk Rolls 700ct (viscose) | WX72081LARP, WX72082LERP | N · S3 · **P** · C v · E v · Eco | $42.99/700 · **pallet $4,585 / 140 rolls = 98,000 wipes** | 4.5 | the EWG Verified + compostable-cloth option for a sustainability-graded program |
| hardware (dispenser standardization) | Wall Dispenser · Floor Dispenser · XL Bucket Dispenser | WX72244BWD · WX72192BFD · WX72134BKT | hardware rule Part 6.7 | $119.99 · $249.99 · $12.99 | — | the "dispenser standardization" required element; XL bucket = "30% recycled plastic" only |

Rejected: Table Bussers **Unscented** (no NSF, no food-safe → cannot carry the food-service line); BZK/EPA SKUs (facilities-not-surfaces constraint clashes with a surface-cleaning procurement story).

## Cannibalisation -> ANGLE DELTA
- `buy-cleaning-wipes-in-bulk` (2026-08-25) — already owns: bulk economics, **wholesale pricing / volume & case quantities**, **MOQ**, **cost-per-wipe calculator**, **facility account setup (centralized purchasing, recurring replenishment, standardized products)**, **single-location vs multi-location purchasing** (incl. "Enterprise / large org"), **"what to ask during your quote"**, best-bulk-by-facility-type, procurement checklist.
- `bulk-gym-cleaning-wipes-supplies` (2026-08-31) — already owns: gym procurement framework, bulk-vs-individual, cost & value, **multi-location and franchise standardization**, procurement model, procurement checklist.
- Overlap of the brief's 8 required elements vs those two posts: **~6 of 8 are already published** (volume tiers, recurring delivery, cost-per-wipe, purchasing workflow, multi-location, SKU standardization). Only "dispenser standardization as a governance lever" and "reorder planning as an operating routine" are genuinely uncovered.

```
ANGLE DELTA: buy-cleaning-wipes-in-bulk = SOURCING/deciding to buy in bulk (setup stage, single decision).
             bulk-gym-cleaning-wipes-supplies = single-vertical (gym) procurement.
             THIS POST = OPERATING & GOVERNING a live program across MIXED-vertical, multi-location
             sites: par-level/reorder triggers per site, one approved SKU list enforced store-to-store,
             dispenser standardization, and usage variance between locations. Stage = operate/audit,
             not source; vertical = mixed (fitness + food-service + office), not gym-only.
RECIPROCAL LINK: new post -> buy-cleaning-wipes-in-bulk (the sourcing how-to) AND -> bulk-gym-cleaning-wipes-supplies;
             add the reverse links in both old posts.
```
**Owner decision required:** if a real 2-axis delta (stage + vertical) is not accepted, the honest alternative is to **refresh `buy-cleaning-wipes-in-bulk`** rather than publish a near-duplicate. This is flagged at Gate 2, not buried.

## Date targeting
- Q4 peaks in this cluster: `cleaning supplies cost` Nov 30–Dec 6 · `cost per use` Nov 30–Dec 6 · `office cleaning` 2nd peak Nov 16–22.
- Publish window = peak minus 2–4 weeks → **Nov 1–20**; recommended **~Nov 2–9 (≈4 weeks lead)**.
- Today 2026-09-28 → **35 days to Nov 2**.
```
peak window: late Nov–mid Dec   derived publish window: Nov 1–20
today: 2026-09-28   verdict: QUEUE (target publish ~2026-11-02)
```
(The primary term `commercial cleaning supplies` is stable year-round; its own peak is spring. The Q4 timing is chosen from the cost/office cost cluster and the fiscal-year procurement cycle, which is the actual trigger for this buyer.)

## Limits and escalations
- Absolute search volume: NOT obtained (needs Marketing / SEMrush-GSC).
- Primary `commercial cleaning supplies` LLM 3.8 (band 3.5–3.9) — acceptable **because** its 12-m baseline is high and stable and the buyer intent is commercially clean; the rising Q4 term (`cleaning supplies cost`) is the timing anchor, not the ranking bet.
- No new audience / no CRO conflict -> no Marketing escalation needed yet.
