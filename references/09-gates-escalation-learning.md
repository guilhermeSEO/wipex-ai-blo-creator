# 09 — GATES, ESCALATION, AND THE LEARNING LOOP

---

## 1. The three gates

### GATE 1 — brief locked (before any research)
Restate the brief, name the conflicts you can already see, then stop. Template in
`references/01`. Do not research against an ambiguous brief.

### GATE 2 — research approved (compulsory, the only always-on human stop)
Present one block. The owner answers in under a minute.

```
PHASE 1 COMPLETE
  keyword:      <primary> — LLM <score>/5 — trend <measured>
  zero-data:    <terms with no measurable demand and what was done about it>
  products:     <primary + secondary, Part 4 names, SKUs, prices>
  envelope:     Tier <n> — <codes granted> — <the headline exclusion>
  cannibalisation: <existing post, product overlap, ANGLE DELTA on which axis>
  date:         <peak window> -> publish window <months> -> GO NOW / QUEUE <date> / NEXT CYCLE
  audience:     <persona + top pain>
  FAQ:          <count> questions
  escalations:  <items needing Dean / Marketing / you>
  APPROVE?      keyword / products / angle / publish date   (Y / override)
```

### GATE 3 — publish
Draft + SEO spec + compliance report + audit attached. The operator pastes and publishes.

**Any model stops at any gate when the evidence contradicts the brief.** Autonomy is about
not asking needless questions, not about overriding a contradiction.

---

## 2. Escalation routing

| Trigger | Route | Never |
|---|---|---|
| Any BLOCKING compliance finding | Dean Tansman | soften the wording to pass |
| Product absent from Part 4 | Dean | invent a row or a claim |
| Certification asserted where Part 4 shows `—` | Dean | assume the badge is fine |
| Tier 2 claim on a product without `P` | Dean | borrow a sibling product's test |
| Benchmark brand named | Dean | paraphrase it as "leading brand" |
| "safe" applied to a surface | Dean | swap in "safe-ish" wording |
| Untested outcome claim (e.g. a time-saving CTA) | Dean | publish it as "designed to" and hope |
| Filter conflicts with a live page | Dean | decide which wins — Part 4 wins, page gets fixed |
| Legal / regulatory / medical interpretation | the owner | give an opinion |
| No internal link map | Marketing | publish without links |
| Audience outside the known personas | Marketing | guess a persona |
| Brief ambiguous | the owner | start research anyway |
| Keyword the data cannot support | the owner | rank on a term with zero demand |

Contacts: **Dean Tansman** — President, Dutch Harbor Brands (compliance). **Wipex marketing**
— internal team. **Owner** — Guilherme.

---

## 3. The learning loop — this is "cada vez melhor"

A skill that never ingests its own results is a template, and templates decay. The loop runs
on every published post.

### Before the peak — verify the conversion path

Because posts are published **2–4 weeks ahead of a peak** (min 2 weeks, default ~1 month), the
runway is spent building authority — and confirming the post can actually convert when the
traffic lands. Run this list 2 weeks before the target window:

- [ ] product in stock, and the size/format the copy recommends
- [ ] price in the copy matches the live price (recompute, do not trust an old figure)
- [ ] the offer / sample / bulk-pricing route is live and reachable
- [ ] every internal link in the post resolves (no 404, no redirect to the wrong collection)
- [ ] meta title + meta description still match the published page
- [ ] the reciprocal link from the older cluster post exists

Any unchecked box is a reason to fix before the peak, not to delay the peak. Ranking into a
dead checkout wastes the entire runway.

### At day 0 — record the baseline
Append to a ledger (`wipex/04-data/published_ledger.md`):

```yaml
- handle: <url handle>
  published: <date>
  keyword: <primary>
  products: <SKUs>
  words: <n>
  modules_used: [..]
  faq_count: <n>
  cta: <the brief's CTA>
  escalations_open: [..]
```

### At day 30 / 60 / 90 — measure and decide

| Metric | Source | What it tells you |
|---|---|---|
| Impressions | Search Console | whether the keyword was reachable at all |
| Average position | Search Console | whether the structure competes |
| CTR | Search Console | whether title + meta earn the click |
| Queries it ranks for | Search Console | whether the LSI cluster worked |
| Add-to-carts / revenue attributed | Shopify / GA4 | whether the CTA ladder converts |
| LLM citation presence | ask the assistants the target question | whether AEO is landing |

### The decision rules

| Signal | Action |
|---|---|
| Impressions high, CTR low | rewrite title + meta only; keep the body |
| Impressions low, all else equal | the keyword bet was wrong — re-target from the operational cluster |
| Position 8–20 and rising | add internal links from newer posts; wait |
| Position stuck >30 at day 90 | consolidate with the cluster post instead of maintaining two |
| Clicks but no conversions | the CTA ladder or the friction step is the problem; fix page-side next |
| A module correlates with conversions | promote it into the standard order in `references/05` |
| A module is always weak | drop it from the order and say so in the changelog |

### When to change the skill itself

Change the skill when the finding is **structural**, not when one post underperforms:

1. Re-measure the corpus (`scripts/audit_blog_patterns.py --corpus`).
2. If the house has genuinely moved, update the measured table in `references/08` **and** the
   summary table in `SKILL.md`.
3. Patch the affected reference file.
4. Bump `version` in the frontmatter and add a CHANGELOG line in `SKILL.md` naming the
   evidence that forced the change — no silent edits.

### Quarterly

- Re-run the corpus audit; refresh the cannibalisation map in `references/08`.
- Re-read the Claims Filter version. If it has been reissued (v1.2+), re-derive the SKU
  envelopes and update `references/03` before the next brief.
- Re-check the live-site conflicts listed in `references/03` — a fixed page should be
  removed from that list.
