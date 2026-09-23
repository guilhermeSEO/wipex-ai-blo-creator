# 04 — AGENT 1C: AUDIENCE, OBJECTIONS, FAQ

Agent 1C exists so the copy is written to a real person with a real budget, not to a
keyword. Output it as a short brief, not an essay.

---

## 1. Persona block (fill it, don't gesture at it)

```yaml
primary_persona:
  title:            GM / FOH manager / facilities manager / studio owner / procurement
  segment:          the actual industry slice
  team_they_control: who they schedule or instruct
  budget_lines:     the P&L lines they own (labour hours, disposables, supplies)
  patches_they_care_about: cost-per-use, labour minutes, downtime, compliance paper trail
secondary_persona: the smaller buyer who converts fastest (owner-operator)

top_3_pains:
  1: "..."   # in their words, operational not emotional
  2: "..."
  3: "..."

buying_criteria_ranked:
  - <the first thing they actually check>
  - ...

decision_timeline:
  - planned path (budget/season) → typical lead time
  - urgent path (audit, breakdown, opening) → typical lead time

where_they_research:
  - <queries>, <communities>, <distributor sites>, <vendor blogs = the SERP competition>

objections:
  - objection → the only honest answer
```

**Rule:** every objection must be answered with either our own price/format fact, an approved
claim, or a cited third-party figure. "Great question, we're the best" is not an answer.

---

## 2. FAQ mining (ranked by usefulness)

1. Google People Also Ask / related searches for the primary keyword (real query language)
2. The house's own past posts — pull FAQ headings from the last 21 and see what recurs
3. Distributor and competitor Q&A (Amazon Q&A, WebstaurantStore), industry forums
4. Support tickets / chatbot logs if Marketing can supply them
5. Sales objections heard on calls

Each FAQ row: **Question | Pain trigger | Product benefit | Claim used (compliant) | Bridge CTA**

FAQ rules: 6–10 questions; the question in the reader's own words; the first sentence answers
it directly (this is the AEO payload); long-form answers are fine — the house writes them
long; never let an FAQ answer make a claim the body could not make.

---

## 3. Citable third-party data (the "no fabrication" rule applied)

Everything in the copy that is not our own price or an approved claim must be traceable.
Collect it here with source + date checked, and hand the table to 2A.

### Real table from the test run (food-service / table turnover, checked 2026-09-23)

| Figure | Source | Date checked |
|---|---|---|
| Table reset target **under 90 seconds** | Lavu, *How to Optimize Restaurant Table Turnover Rate* | 2026-09-23 |
| Full reset target **3–5 minutes**, casual dining | FlipMenu, *How to Reduce Table Turnover Time with Technology* | 2026-09-23 |
| Casual dining averages **1.5 turns/hour**; labour 30–35% of expenses | Worldmetrics, Restaurant Management Industry Statistics 2026 | 2026-09-23 |
| **+0.3 turns** on a 60-seat room ≈ **$275,000/yr** | KwickBook, *Optimize Table Turnover Rate* | 2026-09-23 |
| **+20–35% more covers** without hurting satisfaction | KwickBook | 2026-09-23 |
| Paper towels ≈ **5¢/sheet** | The Zero Store, *Wipes vs Paper Towels* | 2026-09-23 |
| A dedicated busser can **halve** reset time | Restaurant Booking System, Academy | 2026-09-23 |
| Linen cleaning can cost **upwards of $200,000/yr** | Berkwiper, distributor guide | 2026-09-23 |

**These are context about the reader's operation. They are never converted into a Wipex
product claim.**

---

## 4. Own-price arithmetic for the cost block

Pull live prices from `https://wipex.co/products/<handle>.json` (works; the store's
`/blogs/.../articles.json` does not). Recompute — never copy a stale figure.

Example (test run):

| SKU | Price | Count | $/wipe |
|---|---|---|---|
| WX01126TN (Autumn, 1 bucket) | $36.99 | 400 | ≈ $0.092 |
| WX01130TN (2-pack) | $69.99 | 800 | ≈ $0.087 |
| WX01126TN-4 (4-pack case) | $119.99 | 1,600 | ≈ $0.075 |
| WX72024TBB (Unscented, 1 bucket) | $36.99 | 400 | ≈ $0.092 |

The house already uses this device in production (a live meta title reads
"…1000ct | 70% & 96% | ~$0.09/Wipe"). Match that style.

---

## 5. Output template

```markdown
# 1C — AUDIENCE, OBJECTIONS, FAQ

## Persona (filled block)
## Buying criteria, ranked
## Objections → honest answers
## FAQ outline (6–10 rows, pain → benefit → claim → CTA)
## Citable external data (table: figure | source | date checked)
## Own-price arithmetic (recomputed from live product JSON, dated)
## Recommended structure for THIS post
   <module list from the house pattern, reordered to fit the angle>
```

---

## 5. Objections → answers, and where the answer lives

The template gains a column the earlier version did not have: every objection is answered **somewhere
specific** in the article, because an objection answered nowhere is an objection still standing.

| Objection | The only honest answer | Where it lives |
|---|---|---|
| "A pre-mixed wipe costs more per unit than a spray and a cloth" | It moves the cost from the consumable to the minute, and the minute is the larger term | cost block |
| "We already clean, we just do it cheaply" | The cheaper routine usually takes a second trip per table | cost block + calculator |
| "Our team will not change how they reset" | The change is one less walk, not one more rule | reset framework |
| "Do we need the scented one?" | Scent is a room decision: guest-facing vs back of house | differentiation section |
| "Can we put one bucket in the middle of the floor?" | Placement decides whether the cleaning step starts at the table | FAQ |
| "How do we know we are buying enough?" | Par level from resets per week, not from a guess | checklist + FAQ |

## 6. The consumption formula the reader keeps

```
tables × turns per service × wipes per reset × services per week  =  resets per week
resets per week × $/wipe                                          =  weekly consumable cost
```

Hand it over with the reader's own numbers in mind, not with our price — the arithmetic is the
argument, the price is the invoice.

## 7. Worked example: the eight mined FAQs (food service)

1. cost per table vs cost per wipe · 2. how to calculate it · 3. what a good reset time is
(<90 s target; 3–5 min typical) · 4. how many wipes a reset takes · 5. cost per cover vs cost per
 table · 6. scented or unscented, by room · 7. what to check before switching supplies ·
 8. whether labour minutes belong in the cleaning cost.

That set is the model: each question is a decision the reader is about to make, and each answer can
be given honestly inside the envelope.

## 8. Three decision paths, not two

Beyond "what should I buy" and "how do I use it", there is a third path: **new location or
opening**. A buyer fitting out a room has no incumbent routine, so the post's system framing (formats,
station placement, par level, replenishment) is the whole answer. Do not lose it when the other two
paths dominate the outline.

