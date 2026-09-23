# The generic method (absorbed) — trend-driven blog production

This is the class-level, de-branded methodology that used to live in a separate skill
(`ecommerce-blog-generation-framework`). It was absorbed here so this skill is
**self-contained**: one skill holds the technique, the brand instance, the claims envelope, the
gates and the delivery tooling. Nothing here is Wipex-specific — the Wipex instance of every
rule is in `references/02` through `references/09`.

---

## 1. The shape

Three research phases (automated discovery) + four production phases (automated execution), which
takes blog creation from roughly 48–60 manual hours to 20–30 automated + 1–1.5 human hours.

| Phase | Work | Time |
|---|---|---|
| 1A | Google Trends research, multi-region, multi-timeframe | 2 h |
| 1B | LLM keyword scoring (5 dimensions) | 1 h |
| 1C | Product recommendation + audience mining | 3.5 h |
| **gate** | human: approve keyword + product + angle + date | 15 min |
| 2A | Copy against the measured house architecture | 4–6 h |
| 2B | SEO/AEO/GEO/CRO: title, meta, schema, links, readability | 2–3 h |
| 2C | Compliance re-check, zero BLOCKING | 2–3 h |
| 2D | Image briefs + the Shopify section | 2–3 h |
| **gate** | human: publish | 15 min |

## 2. Multi-region, multi-timeframe Trends

Probe the primary market (US) and the secondary market (BR) with the same timeframes — last
4 weeks and last 12 months — and read the direction, not just the level: rising now, seasonal
only, or declining. Real-time viral checks come from `trends.google.com/trending`.

Decision gate: **rising now → go; seasonal → queue for the peak; declining → skip.**
How to actually fetch it (the explore page is a JS app; the internal API needs a per-widget
`token`) is in `references/11-trends-extraction.md`, with a re-runnable probe in
`scripts/google-trends-probe.js`.

## 3. LLM keyword scoring — 1–5, five dimensions

| Dimension | Weight | 1/5 | 5/5 |
|---|---|---|---|
| Semantic clarity | 25% | "wipes" | "plant-based yoga mat wipes for studios" |
| Entity recognition | 25% | generic entities | product + material + use case |
| Niche positioning | 15% | "anyone" | "boutique studios, eco-conscious buyers" |
| Competition moat | 15% | top 10 all major brands | top 10 mostly niche blogs |
| Trend momentum | 20% | falling −20% | rising +25% |

`score = semantic×.25 + entity×.25 + niche×.15 + moat×.15 + momentum×.20` — **proceed at 3.5+**.
Worked examples: "yoga wipes" 2.3 (skip) · "eco yoga mat wipes" 3.8 (ok evergreen) ·
"plant-based yoga mat wipes for studios" 4.7 (proceed).

**Niche specificity is the strategy**, not a preference: broad terms have the volume and none of
the conversion; the niche long tail has lower volume, easier ranking, better LLM citation and
several times the conversion rate.

## 4. Two gates before production

**Calendar alignment** (Q1 budget/procurement · Q2 fitness/summer · Q3 back-to-school ·
Q4 year-end planning · evergreen). Rising now + peak in Q2 + Q2 selected → go now; rising now +
peak Q2 but Q4 selected → plan for Q2. Falling −15% or more → skip.

**Intent alignment**: buying guide + rising = high conversion · how-to + evergreen = long tail ·
comparison + rising = good.

## 5. Product recommendation logic

Extract keyword attributes → query the catalogue → validate which claim codes the SKU actually
carries → confirm the seasonal peak → rank with
`fit = trend×.4 + claims_valid×.3 + calendar×.3` → return the top 3 (or auto-select rank 1).

## 6. Demand reality check (run before committing to a keyword)

- Probe each candidate term **singly** across `today 1-m` and `today 12-m`; a multi-term
  comparison hides which term is empty.
- An empty series on both ranges means no measurable interest. **Never** replace it with an
  estimate presented as data.
- Trends normalises to each term's own peak (100 = that term's max), so averages are **not
  comparable between terms**. Absolute volume needs GSC/SEMrush/Ahrefs — a Marketing-owned input;
  mark it "not captured".
- When product terms are empty, pivot to the **operational / job-to-be-done cluster** (the problem
  the buyer solves) instead of the product noun.
- Check intent in adjacent clusters: high volume can be the wrong audience entirely (job-seeker
  queries dominate many product nouns).
- Report the honest ranking band. A mid-volatility operational term competes with established
  publishers; do not promise the first page.

## 7. Quality gates

| Metric | Target | Gate |
|---|---|---|
| Keyword score | 3.5+/5 | 1B — auto-block below |
| Compliance | zero BLOCKING | 2C — escalate on any |
| Meta title | 65 chars exact | 2B |
| Meta description | 155 chars exact | 2B |
| Readability | FK 6–8 | 2B |
| CTAs | 3+ placed | 2A |
| Calendar | trend peak = hook | 1A |

## 8. Pitfalls (the generic half)

1. Generic keywords kill ranking → the 3.5 threshold.
2. Trend validation skipped → 1A is mandatory, both regions, both timeframes.
3. Calendar misalignment → 1A checks the peak against the hook.
4. Claim violations → 1C validates codes, 2C re-checks.
5. Compliance re-check skipped → 2C is a separate pass, zero BLOCKING.
6. LLM visibility forgotten → scoring in 1B, semantic markup in 2B.
7. Product-term demand assumed → probe singly; an empty series is evidence, not a failed fetch.
8. Trends explore URL fetched headlessly → 429; fetch inside a real browser with the widget token.
9. Long extraction loses partial results → append each result to a JSON file in the workspace as
   you go; an appended file survives a timeout and doubles as evidence.
10. House length assumed instead of measured → measure the target library first.
11. Draft written without links or the structural modules → write the modules and the real anchors
    on the first pass.
12. Meta length estimated by eye → count candidate strings in code.
13. **The measuring script trusted over the output** → a checker that miscounts headings as
    paragraphs, splits a wrapped bullet into a 5-word paragraph or counts auxiliary records as
    zero-data probes reports confident nonsense. Verify the instrument before believing a
    surprising number: a false FAIL costs a rewrite, a false PASS ships a defect.
    See `references/12-measurement-discipline.md`.
14. Compliance scanned only in prose → prohibited terms hide in table headers, row labels and
    bullet labels, and are inherited by copying the library's own house patterns. A prohibited
    word inside a negation is still prohibited. Scan structure, not just body copy.
