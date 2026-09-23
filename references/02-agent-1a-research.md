# 02 — AGENT 1A: DEMAND, KEYWORD, AND PRODUCT

Agent 1A answers three questions with evidence: **is anyone searching for this**, **what
exactly are they searching**, and **which SKU does that demand belong to**.

Run `scripts/trends_fetch.py` for the Google Trends half.

---

## 1. Google Trends — how to actually get the data

**This host cannot reach the Trends API with curl (HTTP 429).** The working path is a real
browser session. Three things took time to discover — do not rediscover them:

1. **Widget data needs the widget's `token`.** Without it you get HTTP 401. The token is
   returned in each widget object from the `explore` call.
2. **The data endpoint is named by *type*, not by widget id.**
   `TIMESERIES → widgetdata/multiline` · `RELATED_QUERIES* → widgetdata/relatedsearches` ·
   `GEO_MAP* → widgetdata/comparedgeo`. Calling `widgetdata/TIMESERIES` returns 404.
3. **Responses are prefixed with `)]}'` and a newline.** Strip that before parsing, or you
   will get "Unexpected token <" from an HTML error page and misdiagnose it as a block.

Fetch for both ranges: `today 1-m` (daily, n≈32) and `today 12-m` (weekly, n≈53), geo `US`
and geo `BR`.

### Reading the numbers honestly

- Trends returns a **relative index 0–100 normalised to each term's own peak**. Averages are
  **not comparable between different terms** — only within one term's own series.
- Trends does **not** return absolute search volume. Never present a volume figure as if it
  were measured. If the brief needs volume, that is a Marketing input (SEMrush/Ahrefs/GSC)
  — state it as unavailable and ask, rather than estimating.
- Compute momentum from the series: mean of the last 7 points vs the prior block, plus the
  peak date. Report the peak date literally (e.g. "100 on Sep 20, 2026").

---

## 2. THE ZERO-DATA BRANCH (mandatory)

Product terms in a niche B2B category are frequently **below Trends' reporting threshold**,
which returns an *empty* series, not a low one. Absence of data is a finding, not a failure.

```
For each candidate keyword:
  series has points?
  ├─ YES → read momentum (§1) and continue
  └─ NO  → this term has no measurable demand. Do NOT keep it as primary.
           ├─ Is there an OPERATIONAL cluster around the job to be done?
           │    (e.g. the outcome the product produces, not the product name)
           │    ├─ YES → pivot primary to the operational term; keep the product term
           │    │        only as an on-page entity, never as the ranking bet
           │    └─ NO  → STOP. Escalate to the owner: no demand signal exists for this
           │             topic and the post would have no entry point.
           └─ Record it explicitly in the report ("zero data on 1-m and 12-m, US and BR").
```

### Real result from the test run (2026-09-23, geo US)

| Term | 1-m | 12-m |
|---|---|---|
| restaurant table cleaning wipes | **empty** | **empty** |
| restaurant table wipes | **empty** | **empty** |
| table busser wipes | **empty** | **empty** |
| food service cleaning wipes | **empty** | **empty** |
| restaurant cleaning wipes | **empty** | **empty** |
| commercial table wipes | empty | avg 8.2, decaying to 0 |
| **table turnover** | last 7d **32.9** vs prior 9.8, peak **100** Sep 20 | avg 48, peaks Feb/Apr/Mar |
| **restaurant staffing** | last 7d **46.4** vs first 7d 0, peak **100** Sep 21 | avg 45.7, peaks Jun |
| cost per use | avg 66.8, stable-high | avg 44.3, peaks Nov–Dec |
| busser | avg 68.8 | avg 70.1, peaks May–Jun |

Brazil: all four probed terms returned zero. BR is not a market for this topic.

**Warning on "busser":** its related queries are job-seeker intent (`busser jobs` 100,
`what is a busser` 62, `busser job description` 15). Real volume, wrong reader. Use for
topical coverage, never as the traffic bet.

---

## 3. LLM keyword scoring

`LLM = Semantic×0.25 + Entity×0.25 + Niche×0.15 + Moat×0.15 + Trend×0.20`

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Semantic clarity | ambiguous noun | topic clear, use vague | product + material + use + test |
| Entity recognition | one generic entity | three entities, clear relation | product + spec + proof named |
| Niche positioning | "anyone cleaning" | "studio owners" | named buyer + budget band |
| Competition moat | top-10 is Wirecutter/Amazon | mixed authority + niche | top-10 all product/brand pages |
| Trend momentum | falling | flat, evergreen | rising now AND season-aligned |

**Decision bands:** ≥4.5 green light · 4.0–4.4 good, take it · 3.5–3.9 acceptable only if
the trend is rising · <3.5 reject and re-derive.

**State the formula's limit in the report:** it scores the *keyword*, not the market. A 4.7
keyword with a zero-data series is still a zero-traffic keyword. Trend momentum must come
from measured data, never from an assumed "+25%".

---

## 4. Product matching (3 layers)

1. **Demand** — what signals the trend actually contains (material, format, buyer, season).
2. **Fit** — does a Wipex SKU genuinely serve that job? Score 1–5 and justify.
3. **Envelope** — pull the SKU's Part 4 row (`references/03`). A product whose claim codes
   cannot support the angle is the wrong product, however well it fits the demand.

Rules: never propose a product with no Part 4 row (escalate: new SKU). Never propose an
EPA/BZK product for a surface-cleaning context. Never carry a claim across SKUs.

---

## 5. Same product, new angle (the cannibalisation check)

Fetch the recent archive and search it for the target intent — not just the exact keyword.

```bash
# article index (atom has titles + dates, no bodies)
curl -s -A '<UA>' 'https://wipex.co/blogs/library.atom?page=1'   # and page=2,3
curl -s -A '<UA>' 'https://wipex.co/blogs/wipex-studio-library.atom?page=1'
# note: /blogs/<h>/articles.json returns 404 on this store — use the atom feeds
```

Then fetch the candidate URLs and strip the body (the container is
`<div class="rte text-spacing">`; `scripts/audit_blog_patterns.py` does this).

Outcome when a post already covers the same product: **that is fine.** Products are meant to
be reused — the catalogue is finite and the buyers repeat. What is *not* fine is reusing the
**angle**. The check exists to force a different angle, not to veto the product.

State a one-line **ANGLE DELTA** in the 1A output, and name the reciprocal internal link:

```
ANGLE DELTA: <existing post> covers <its angle>.
             This post covers <new angle>, for <buyer/stage/format>.
RECIPROCAL LINK: new post -> existing post (and add the reverse link in the old post)
```

### The six axes you can change (pick at least one, ideally two)

| Axis | Example on the same product |
|---|---|
| Stage of the job | plan → source → operate → audit (procurement vs daily operation) |
| Buyer | owner-operator vs multi-unit ops vs procurement vs front-line staff |
| Format / pack | bucket vs refill roll vs dispenser vs sachet vs bundle |
| Season / trigger | Q4 year-end vs Q2 summer vs flu season vs audit |
| Comparison axis | cost-per-use vs reset speed vs waste vs compliance paper trail |
| Vertical | food service vs office vs studio vs lab (same family, different room) |

If you cannot state a real delta on at least one axis, the post does not exist — either
refresh the old post instead, or find another topic.

**Real case:** `table-busser-restaurant-efficiency` (published 2026-08-31) already covers
"How Table Bussers Improve Restaurant Efficiency and Table Turnover", including a four-step
turnover workflow, a five-way efficiency list and an Autumn-vs-Unscented product split. The
test brief was ~85% overlapping. The new post must therefore be a **cost-and-labour
economics** post (cost per use, par levels, labour minutes) and must link into the August
post as the operational how-to — not a rewrite of it.

---

## 6. Targeting future volume (date optimisation)

A rising-today signal is not the only reason to publish. The stronger play is to land the
post **before the term's recurring peak**, using the 12-month series as the map.

**Owner-set lead time: minimum 2 weeks, default ~1 month.** The runway is not only for
indexing. It is for **authority maturation** — a post that has been live, linked and crawled
for a few weeks competes for the peak far better than one published the same week the demand
arrives. Aim a month ahead when you can; never less than two weeks.

### Method

1. From the `today 12-m` series, list the **top 3 weeks** by index and convert them to months.
2. Take the **publish window** = peak month **minus 2–4 weeks** (2 weeks floor, ~4 weeks default).
3. Compare with today:

```
today is inside the publish window      -> GO NOW
peak is >2 weeks but <=6 weeks out      -> QUEUE with the target date; re-check weekly
peak is >6 weeks out                    -> QUEUE; do not publish early "because it's ready"
peak just passed (<6 weeks ago)         -> target the next cycle, or run an evergreen angle
term is flat across 12 months           -> evergreen: publish once the angle is ready
```

4. Report the peak window and the derived publish date in the 1A output. The **date** is
   approved at Gate 2 alongside the keyword — it is a research output, not a preference.
5. **Before the peak lands, verify the conversion path is live** — product in stock, price
   correct, offer/sample/bulk-pricing route working, links resolvable. Ranking into a dead
   checkout wastes the whole runway. See `references/09` §before-the-peak.

### Measured peaks (food-service family, geo US, 2026-09-23)

| Term | 12-m avg | Top weeks (index) | Peak months | Publish window (2–4 wks lead) |
|---|---|---|---|---|
| cost per use | 44.3 | Nov 30–Dec 6 (100) · Mar 8–14 (93) · Dec 7–13 (90) | **late Nov–mid Dec** | **~Nov 1–20** |
| table turnover | 48.0 | Feb 8–14 (100) · Apr 12–18 (96) · Mar 1–7 (91) | **Feb–Apr** | ~mid-Jan to mid-Mar |
| restaurant staffing | 45.7 | Jun 7–13 (100) · Jun 14–20 (100) · May 10–16 (84) | **May–Jun** | ~late Apr to late May |
| busser | 70.1 | May 24–30 (100) · May 17–23 (92) · Jun 7–13 (91) | **May–Jun** | ~late Apr to late May |
| restaurant cleaning (control) | 38.8 | broad mid-year plateau | flat May–Sep | evergreen |

Read together with today (2026-09-22): the **cost-per-use** target is the Nov 1–20 window —
roughly 6 weeks out, so it is a **QUEUE with a target date**, not a "publish this week". The
table-turnover window opens in January. Publication is then timed so the post has weeks of
history behind it when the volume actually arrives.

### Occasion posts follow a different lead rule

A date-driven post (holiday, awareness day, religious festival, retail moment) is **not**
chased by its peak, because it often has no measurable search peak at all. It is timed to be
**live 7 days before the date** (band 5–10), so it exists — and is indexed — while people
search around the occasion. Publishing on the day itself is too late; publishing 3 weeks early
is forgotten by the time the date arrives.

The two rules together:

| Post type | Lead before its target | Band |
|---|---|---|
| Measured-peak post | peak window opening | 14–28 days (18–24 in practice) |
| Occasion / date post | the occasion date | 5–10 days (7 default) |
| Evergreen post | nothing — it fills capacity | max 4/week, max 1/day |

Use `scripts/build_content_calendar.py` to build and validate the whole plan at once: it
refuses past dates, de-collides same-day collisions (a peak beats an occasion), and reports
any week over capacity.

**Caveat:** a 12-month peak is a seasonal pattern, not a promise. A term can be seasonal and
still dead if its absolute volume is tiny (see the zero-data branch, §2).

---

## 7. Agent 1A output template

```markdown
# 1A — DEMAND, KEYWORD, PRODUCT

## Demand (measured, geo US + BR, <date>)
<table of terms: 1-m momentum, 12-m shape, peak date, verdict>
Zero-data terms (explicit): ...

## Recommended keyword set
primary:        ...      LLM <score>/5   trend <measured>
niche headline: ...      LLM <score>/5
LSI:            ...
long tail:      ...
avoid:          ...      (with the reason: no measurable demand)
topical support: ...     (coverage only, not the traffic bet)

## Calendar + intent validation
trend now: ...   hook: ...   verdict: GO / PLAN / RECONSIDER

## GEO signals
<subregion data, with the caveat about small-state over-indexing>

## Product match
primary:   <Part 4 canonical> | SKU | price ladder | why
secondary: ...
rejected:  ... | why

## Cannibalisation -> ANGLE DELTA
existing post(s): <handle, date>   product overlap: yes/no   angle overlap: %
ANGLE DELTA: <the axis changed + the new buyer/stage/format>
RECIPROCAL LINK: <new -> old, and the reverse link to add>

## Date targeting
peak window: <months> from top weeks <list>   derived publish window: <months>
today: <date>   verdict: GO NOW / QUEUE (target <date>) / NEXT CYCLE / EVERGREEN

## Limits and escalations
- absolute search volume: NOT obtained (needs Marketing)
- ...
```
