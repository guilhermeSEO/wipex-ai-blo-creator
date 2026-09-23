# AGENT 1A — DEMAND, KEYWORD, PRODUCT, ANGLE DELTA, DATE
### Blog #1 · food-service · cost + labor + speed · Q4 · run 2026-09-22

**Method:** Google Trends via browser session (geo=US), ranges `today 12-m` (weekly, n=53) and
`today 1-m` (daily, n=32). Raw evidence: `04-data/raw/trends_costcluster.json`,
`raw/trends_calendar.json`, `raw/trends_probe.json`. Corpus scan for cannibalisation:
21 most recent live posts (`raw/blog_bodies.json`).

> Trends returns a **relative index** per term, normalised to that term's own peak. Averages are
> **not comparable between terms** — only movement within a term and presence/absence of data.
> **Absolute search volume is not obtainable from this source** and is not estimated anywhere below.

---

## 1. DEMAND — what actually exists

| Term | 12-m avg | 12-m top weeks (index) | 1-m avg | 1-m last 7d | Read |
|---|---|---|---|---|---|
| **cost per table** | 46.5 | Mar 1–7 (100) · **Nov 30–Dec 6 (95)** · Mar 8–14 (92) | 49.4 | 52.6 | stable-high, **Q4 secondary peak** |
| **cost per cover** | 38.2 | **Nov 30–Dec 6 (100)** · Dec 7–13 (77) · Mar 1–7 (71) | 45.0 | 47.6 | **Q4 peak**, stable |
| **cost per use** | 43.4 | **Nov 30–Dec 6 (100)** · Dec 7–13 (88) · Mar 1–7 (81) | 66.2 | 68.0 | **Q4 peak**, but see §3 |
| cleaning supplies cost | 50.9 | Mar 8–14 (100) · **Nov 30–Dec 6 (93)** · Mar 1–7 (90) | 19.3 | 35.1 | Q4 secondary, rising |
| table reset time | 41.5 | Mar 1–7 (100) · Apr 5–11 (88) · Jun 7–13 (83) | 15.5 | 38.0 | not a Q4 theme; rising now |
| labor cost restaurant | 52.2 | Mar 8–14 (100) · Mar 1–7 (99) · Mar 15–21 (93) | 36.1 | 70.3 | not Q4; surging now |
| janitorial supplies | 62.1 | Jun 7–13 (100) · Jul 5–11 (98) | 21.5 | 37.3 | highest 12-m avg, **wrong season** |
| restaurant operating costs | 40.9 | May 31–Jun 6 (100) · Feb 1–7 (99) | 16.0 | 24.1 | wrong season |
| **cost per wipe** | 13.9 | Nov 30–Dec 6 (100) | 3.1 | 0.0 | **low volume — see §5** |

**Zero-data terms (empty series, 1-m and 12-m, US):** `restaurant table cleaning wipes`,
`restaurant table wipes`, `table busser wipes`, `food service cleaning wipes`, `restaurant
cleaning wipes`, `jenitorial`. `commercial table wipes` exists at avg 8.2 and is decaying to 0.

### Calendar + intent validation

- Hook is **Q4**. The cost-per-X family peaks **Nov 30 – Dec 13**, so the publish window with a
  2–4 week runway is **Nov 1 – Nov 20**. 🟢 **GO** — the hook and the measured peak agree.
- `table turnover` (the CTA's subject) peaks **Feb–Apr**; it is *not* a Q4 term. This is why the
  CTA frames the post rather than leading the keyword (decided at Gate 1).
- Brazil: not measured for this cluster; the earlier run showed all BR terms empty. US only.

---

## 2. THE ZERO-DATA BRANCH APPLIED

Every **product-level** term in this category returns an empty series. Applying the branch from
`references/02` §2: there is a live *operational* cluster (cost per table/cover, cleaning supplies
cost), so the post pivots to it — the product names appear as on-page entities, never as the
ranking bet. Had the operational cluster also been empty, the correct action would have been to
stop and escalate, not to write.

---

## 3. ⚠ SEMANTIC POLLUTION — the finding that changes the keyword

`cost per use` has the highest 1-m average (66.2) **and the wrong audience**. Its related
queries are:

```
TOP:    what is a use case:100 · openai news:59 · new york times:41 · how to use apple pay:35
        how to use google flights:28 · how to use google drive:25 · how to use zoom:22
RISING: openai news today:24100 · how to use google authenticator:10300
        how to use google scholar:8600 · how to use obs studio:5700
```

The word "use" carries the intent, not the cleaning context. A post ranking on `cost per use`
attracts general "how do I use X" traffic — **not** operators computing a cleaning cost. High
volume, wrong reader.

By contrast `janitorial supplies` related queries are pure commercial intent
(`janitorial supplies near me` 100 · `commercial janitorial supplies` 56 ·
`janitorial supplies wholesale` 47 · `bulk janitorial supplies` 17) — but it peaks in **June**.

---

## 4. LLM KEYWORD SCORING

`LLM = Sem×0.25 + Entity×0.25 + Niche×0.15 + Moat×0.15 + Trend×0.20`

| Candidate | Sem | Ent | Niche | Moat | Trend | **LLM** | Verdict |
|---|---|---|---|---|---|---|---|
| **cost per table** | 4.5 | 4.5 | 4.5 | 4.5 | 4.0 | **4.4** | 🟢 **PRIMARY** |
| **cost per cover** | 4.5 | 4.5 | 4.5 | 4.0 | 4.5 | **4.4** | 🟢 #1 LSI / co-primary |
| how to calculate cost per table for a restaurant | 5 | 5 | 4.5 | 4.5 | 4.0 | **4.65** | 🟢 long-tail headline |
| cleaning supplies cost | 4.5 | 4 | 4 | 3.5 | 4.0 | **4.0** | ✅ LSI |
| cost per use | 3.0 | 3.0 | 3.0 | 2.5 | 4.5 | **3.2** | 🔴 reject as primary — polluted intent (§3) |
| cost per wipe | 4.5 | 4.5 | 3.5 | 1.0 | 3.5 | **3.6** | 🔴 saturated in-corpus (§5) + low volume |
| janitorial supplies | 4.5 | 4.5 | 3 | 3 | 2.0 | **3.6** | 🔴 wrong season for Q4 |
| table busser wipes | 4.0 | 3.5 | 4.5 | 5.0 | 1.0 | **3.4** | 🔴 zero measured demand |

---

## 5. ANGLE DELTA (mandatory — the corpus already owns "cost per wipe")

Corpus scan across the 21 most recent posts:

| Territory | Already owned by | Mentions |
|---|---|---|
| cost per wipe | **16 posts**, incl. the literal H2 *"How to Calculate Your True Cost Per Wipe"* in `gym-wipe-dispenser-vs-bucket` and `bulk-isopropyl-alcohol-wipes-buyers-guide` | 16/21 |
| cost per wipe & monthly usage calculator | `buy-cleaning-wipes-in-bulk` (H3) | 18 mentions |
| table turnover + Table Bussers + four-step workflow | `table-busser-restaurant-efficiency` (2026-08-31) | 4 |

```
ANGLE DELTA
  Existing posts cover:  cost PER WIPE, at facility/gym scale, as a
                         format-choice argument (bucket vs roll vs dispenser).
  This post covers:      cost PER TABLE and PER COVER, at
                         front-of-house scale, as a table-turnover economics
                         argument — the unit the operator is actually paid in.
RECIPROCAL LINK: new post -> table-busser-restaurant-efficiency (the operational
                 how-to) ; add the reverse link on that post to this one.
```

**The unit change is the delta:** wipe → table/cover. It is food-service native, it is the unit
the CTA ("Reduce Table Turnover Time") is denominated in, and the corpus has never used it. Note
also that `cost per wipe` — the term the house writes 16 times — has **the lowest measured demand
of the whole cluster (13.9 avg, 3.1 in 1-m).** The house is optimising for a term nobody searches.

---

## 6. RECOMMENDED KEYWORD SET

```yaml
primary_kw:      "cost per table"
lsi_kw:          ["cost per cover", "cleaning supplies cost", "table reset time",
                  "restaurant cleaning cost"]
niche_headline:  "how to calculate cost per table for a restaurant"
avoid:           ["cost per wipe"   # saturated in-corpus + lowest volume measured
                  "cost per use"    # semantically polluted (related queries are 'how to use …')
                  "janitorial supplies"  # peaks June, not Q4
                  "table busser wipes" / "food service cleaning wipes"  # zero demand]
topical_support: ["table turnover", "restaurant staffing"]   # framing + internal links only
geo_primary:     ["California", "Florida", "Texas"]
geo_secondary:   ["Georgia", "Utah", "New York"]
```

**GEO evidence (12-m, US):** `cost per use` subregions → WY 100 · DC 35 · **CA 27** · UT 27 ·
GA 26 · KS 26 · **FL 24** · **TX 23**. CA/FL/TX in the top tier again. Caveat: small states
over-index on thin absolute volume; the big markets carry the mass.

---

## 7. PRODUCT MATCH (fixed at Gate 1, envelope validated in 1B)

| Rank | Product (Part 4 canonical) | SKU | Price ladder | Why |
|---|---|---|---|---|
| 🥇 PRIMARY | Table Bussers Surface Wipes (scented, cinnamon-clove; autumn variant) | WX01126TN · WX01130TN · WX01126TN-4 | $36.99 / $69.99 / $119.99 | 400ct bucket; **NSF-certified permitted (A-004)**; **only** Table Bussers SKU allowed "suitable for food service environments"; Q4 seasonal scent |
| 🥈 SECONDARY | Table Bussers Unscented | WX72024TBB (+`-2`,`-4`) | $36.99 / $69.99 / $119.99 | fragrance-free rooms; **no NSF, no food-safe** |
| ❌ rejected | cost-per-wipe format posts (bucket vs dispenser) | — | — | would repeat `gym-wipe-dispenser-vs-bucket` |

---

## 8. DATE TARGETING

```yaml
term:            cost per table (co-term: cost per cover)
peak_window:     Nov 30 - Dec 13  (12-m top weeks: Nov 30-Dec 6 = 95/100)
publish_window:  Nov 1 - Nov 20   (2-4 weeks runway, owner-set)
today:           2026-09-22
verdict:         QUEUE with target date ~2026-11-08
```

**QUEUE, not "publish this week".** The runway exists for authority maturation (the post has
weeks of crawl history when the peak lands) and to verify the conversion path is live before the
window opens (`references/09` before-the-peak list). Publishing now would be ~6 weeks early.

---

## 9. LIMITS AND ESCALATIONS

- **Absolute search volume: NOT obtained.** Trends cannot supply it. Requires SEMrush/Ahrefs/GSC
  (Marketing). Nothing in the copy may present an estimated volume as measured.
- **`cost per table` and `cost per cover` are near-equivalent** in demand (46.5 vs 38.2 avg).
  They should be used as a pair, not as a bet on one.
- Escalations carried from 1B: the live-site EWG Verified® conflict and the bare "Sustainable"
  title on the scented SKU, plus the MEDIUM finding on the CTA.