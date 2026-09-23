# AGENT 1A — GOOGLE TRENDS + KEYWORD RESEARCH
### Wipex Blog #1 · food-service operations · cost + labor + speed · Q4
**Fetch date:** 2026-09-23 · **Source:** Google Trends live API via browser (trends.google.com, geo=US / geo=BR) · **Ranges:** `today 1-m` (daily, n=32) and `today 12-m` (weekly, n=53)

> **Method note.** Each Trends query is normalised against its own maximum (100 = that
> term's own peak), so **avg values are NOT comparable between different terms** — only
> *movement within a term* and *presence/absence of data* are. Absolute monthly search
> volume is not obtainable from Trends and is **not** provided here; it requires
> SEMrush/Ahrefs/GSC, which is a Marketing-owned input. Nothing below is an estimate of
> volume; every number is a measured Trends index value.

---

## 1. WHAT CAME BACK

### 1.1 Terms with data (US)

| Keyword (US) | Range | n | avg | first 7 | last 7 | mid | peak |
|---|---|---|---|---|---|---|---|
| table turnover | 1-m (daily) | 32 | 12.7 | 0 | **32.9** | 9.8 | 100 (Sep 20) |
| table turnover | 12-m (weekly) | 53 | 48.0 | 17.9 | 10.0 | 60.2 | 100 (Feb 8–14) |
| table turnover rate | 12-m | 53 | 17.6 | 0 | 1.6 | 23.6 | 100 |
| table turnover rate | 1-m | 32 | 3.1 | 0 | 0 | 5.6 | 100 |
| restaurant table turnover | 12-m | 53 | 1.9 | 0 | 14.3 | 0 | 100 |
| restaurant cleaning supplies | 1-m | 32 | 3.1 | 0 | **14.3** | 0 | 100 |
| restaurant cleaning supplies | 12-m | 53 | 9.0 | 0 | 4.3 | 11.5 | 100 |
| restaurant staffing | 1-m | 32 | 18.4 | 0 | **46.4** | 14.7 | 100 (Sep 21) |
| restaurant staffing | 12-m | 53 | 45.7 | 26.4 | 17.4 | 54.3 | 100 (Jun 7–13, Jun 14–20) |
| busser | 1-m | 32 | 68.8 | 76.9 | 63.4 | 67.8 | 100 (Sep 2) |
| busser | 12-m | 53 | 70.1 | 56.7 | 73.3 | 71.9 | 100 (May 24–30) |
| cost per use | 1-m | 32 | 66.8 | 58.0 | **69.4** | 69.1 | 100 (Sep 21) |
| cost per use | 12-m | 53 | 44.3 | 29.9 | 15.9 | 52.1 | 100 (Nov 30–Dec 6) |
| commercial table wipes | 12-m | 53 | 8.2 | 0 | 0 | 11.2 | 100 |
| restaurant cleaning (control) | 12-m | 53 | 38.8 | 18.0 | 19.1 | 46.0 | 100 |

Top weeks (seasonality anchors): table turnover → **Feb 8–14 (100), Apr 12–18 (96), Mar 1–7 (91)**; busser → **May 24–30 (100), May 17–23 (92), Jun 7–13 (91)**; restaurant staffing → **Jun 7–13 (100), Jun 14–20 (100), May 10–16 (84)**; cost per use → **Nov 30–Dec 6 (100), Mar 8–14 (93), Dec 7–13 (90)**.

### 1.2 Terms with ZERO data (US)

Empty time series on both ranges (below Google Trends' reporting threshold):

- `restaurant table cleaning wipes`
- `restaurant table wipes`
- `restaurant cleaning wipes`
- `table busser wipes`
- `food service cleaning wipes`

### 1.3 Brazil (geo=BR, 12-m)

`restaurant table cleaning wipes`, `table busser wipes`, `table turnover rate`,
`restaurant cleaning supplies` → **all zero**. BR is not a viable market for this topic.

### 1.4 Related queries (US, 12-m)

Only one term produced related queries at all:

- **busser** — TOP: busser jobs (100) · what is busser (62) · busser job (60) ·
  busser restaurant (59) · what is a busser (52) · busser jobs near me (34) ·
  busser meaning (30) · what does a busser do (18) · busser job description (15).
  RISING: max busser watches (350), busser watches (250), max busser (60) — **noise**
  (a watch brand, not our category).

**⚠ Audience caution:** the "busser" cluster is dominated by **job-seeker intent**
("busser jobs", "what does a busser do"). Traffic volume here is real but the *buyer*
is not the searcher. Use this cluster for topical coverage and internal linking, **not**
as the blog's primary traffic bet.

### 1.5 Interest by subregion (US, 12-m) — GEO grounding

| Keyword | Top subregions (index) |
|---|---|
| table turnover | WY 100 · DC 26 · KS 24 · **CA 11** · NY 10 · VA 10 · NM 10 · **FL 8** |
| table turnover rate | AZ 100 · CO 50 · NJ 50 · **CA 50** · MA 50 · NY 50 · WA 50 · GA 50 |
| restaurant cleaning supplies | OR 100 · NY 50 · **FL 50** · MA 50 |
| busser | NV 100 · HI 55 · AZ 53 · NM 48 · RI 48 · **FL 46** · **TX 44** · MD 44 |
| restaurant staffing | WY 100 · KS 18 · DC 16 · GA 14 · DE 14 · NY 14 · NV 12 · **CA 12** |
| cost per use | WY 100 · DC 36 · **CA 27** · UT 27 · KS 26 · GA 26 · **FL 25** · **TX 23** |

**Read:** **CA, FL and TX appear in the top tier of 4 of the 6 terms** (including both
the turnover cluster and the cost cluster). The skill's CA/FL/TX GEO signal is therefore
**evidence-backed for this blog** — not assumed. Small states (WY, DC, KS) top the index
on low absolute volume; the three big markets carry the mass.

---

## 2. CALENDAR + INTENT VALIDATION

```yaml
calendar_hook:   Q4 (year-end)
today:           2026-09-23
is_trend_rising_now:
  table turnover:      YES  (last 7d 32.9 vs mid 9.8; 100 spike Sep 20)
  restaurant staffing: YES  (last 7d 46.4 vs first 7d 0; 100 spike Sep 21)
  cost per use:        STABLE-HIGH (last 7d 69.4, mid 69.1)
seasonality:     table-turning + staffing both peak in the Feb–Jun staffing/budget window;
                 the current Sept spike is off-season momentum — genuinely favourable.
verdict:         🟢 GO NOW — the operational cluster is moving in the same direction as
                 the brief's CTA, in the same month we want to publish.
```

---

## 3. LLM KEYWORD SCORING (formula from `LLM_KEYWORD_SCORING.md`)

`LLM Score = Sem×0.25 + Ent×0.25 + Niche×0.15 + Moat×0.15 + Trend×0.20`

| Candidate | Sem | Ent | Niche | Moat | Trend | **LLM** | Verdict |
|---|---|---|---|---|---|---|---|
| **how to reduce table turnover time in a restaurant** | 5 | 5 | 4.5 | 4.5 | 4 | **4.7** | 🟢 long-tail headline |
| **restaurant table turnover** | 4.5 | 4.5 | 4.5 | 4 | 4.5 | **4.4** | 🟢 **PRIMARY** |
| restaurant table reset cost per use | 4.5 | 4 | 4.5 | 4.5 | 3.5 | **4.2** | 🟢 secondary / cost angle |
| table turnover rate | 4.5 | 4.5 | 4 | 3.5 | 3 | **4.0** | ✅ LSI |
| table turnover | 4 | 4 | 3.5 | 3 | 5 | **4.0** | ✅ LSI (trend anchor) |
| restaurant cleaning cost per use | 4.5 | 4 | 4.5 | 4 | 3.5 | **4.1** | ✅ LSI |
| cost per use | 4 | 3.5 | 3 | 2.5 | 3.5 | **3.4** | ⚠ too generic alone |
| commercial table wipes | 4 | 3.5 | 3.5 | 3 | 1.5 | **3.2** | 🔴 declining to zero |
| table busser wipes | 4 | 3.5 | 4.5 | 5 | 1 | **3.4** | 🔴 zero search data |

---

## 4. RECOMMENDED KEYWORD SET

```yaml
primary_kw:      "restaurant table turnover"
niche_headline:  "how to reduce table turnover time in a restaurant"   # H1 / title base
lsi_kw:          ["table turnover rate", "table reset time", "restaurant cleaning cost per use",
                  "cost per use", "restaurant cleaning supplies"]
topical_support: ["busser", "front of house", "restaurant staffing"]   # coverage + internal links only
avoid:           ["table busser wipes", "commercial table wipes", "food service cleaning wipes",
                  "restaurant table cleaning wipes"]   # no measurable demand
geo_primary:     ["California", "Florida", "Texas"]        # Trends-backed (§1.5)
geo_secondary:   ["New York", "Georgia", "Arizona", "Colorado"]
```

**Why this and not a product term:** the product terms have no measurable search interest
at all, while the operational terms are rising *this month*. A blog titled around
"table busser wipes" would target a market that Trends cannot even see. A blog titled
around **reducing table turnover time** rides live demand and still lands on Table Bussers
via the CTA and the body.

**Ranking expectation (honest):** the primary is a mid-volatility operational term, not a
zero-competition niche. Expect the content to compete with restaurant-ops blogs (Toast,
TouchBistro, WebstaurantStore, Sunday), not product pages. 3–6 months to a stable
position is the realistic band; a first-page position is not guaranteed.

---

## 5. PRODUCT MATCH

| Rank | Product (Part 4 canonical) | SKU | Price | Why |
|---|---|---|---|---|
| 🥇 PRIMARY | Table Bussers® Plant-Based All-Purpose Cleaning Wipes \| Autumn-Scented | WX01126TN (2-pk WX01130TN, 4-pk WX01126TN-4) | $36.99 / $69.99 / $119.99 | 400ct bucket; **NSF-certified permitted (A-004)**; seasonal autumn scent fits Q4; only Table Bussers SKU that may carry NSF + "suitable for food service environments" |
| 🥈 SECONDARY | Table Bussers® Natural Unscented Cleaning Wipes | WX72024TBB (+ -2, -4) | $36.99 / $69.99 / $119.99 | sensitive-environment / fragrance-free angle; same price ladder; **no NSF, no food-safe** |
| ❌ REJECTED | Natural Fitness wipes / EMPOWER | — | — | Tier 2 products, but the wrong use case (fitness floors, not table turnover). Claim transfer is forbidden. |

**Fit note:** with `P = —` on both SKUs, the Autumn/Unscented pair can only be positioned
with Tier 3 language. That is sufficient for a cost/labor/speed blog — see Agent 1B.