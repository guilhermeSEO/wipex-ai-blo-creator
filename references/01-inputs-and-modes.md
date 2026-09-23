# 01 — INPUTS, MODES, AND THE BRIEF GATE

## The input form

Only the first block is compulsory. Anything left blank is researched or auto-proposed.

```yaml
# ── COMPULSORY ─────────────────────────────────────────────
topic:            "what the post is about, in one line"
calendar_hook:    Q1 | Q2 | Q3 | Q4 | Evergreen
target_buyer:     "who signs the purchase order"
angle:            "the argument the post makes"
cta:              "the action, phrased as an operational outcome"

# ── OPTIONAL (auto-proposed if blank) ──────────────────────
products:         "exact Part 4 canonical names" | auto
primary_keyword:  "..." | auto-research
secondary_kw:     [..] | auto
blog_intent:      buying_guide | how_to | comparison | educational
blog_type:        checklist | guide | comparison | seasonal | procurement
cro_goal:         e_commerce   | lead_gen | brand_awareness
target_action:    add_to_cart   | request_quote | download | email_signup
target_market:    US (default) | BR | BOTH
publish_target:   YYYY-MM-DD
audience_override: "..."
angle_override:    "..."
model:            A | B | C        # default B
```

## Operational models

| | Model A — auto | Model B — hybrid (default) | Model C — human-led |
|---|---|---|---|
| Your time | ~5 min | ~20–30 min | 1–2 h |
| Products | auto-chosen | auto-proposed, you approve | you specify |
| Keyword | auto | auto-proposed, you approve | you specify |
| Stop points | Gate 3 only | Gates 2 + 3 | Gates 1, 2, 3 |
| Use when | deadline is the constraint | normal case | high-stakes or off-template |

Model A is not "skip the gates" — it is "no gate 2 unless the research contradicts the
brief". If 1A cannot support the brief (no demand, product mismatch, compliance conflict),
**any** model stops and asks. Autonomy never overrides a contradiction.

## Calendar strategy

| Quarter | Trigger | Framing that works | Buyer |
|---|---|---|---|
| Q1 | budget cycle (Jan–Mar) | procurement guide, cost comparison, par levels | facilities, procurement |
| Q2 | summer prep (Apr–Jun) | seasonal prep, high-touch cleaning, sweat season | fitness, offices |
| Q3 | back-to-school / back-to-office (Jul–Sep) | reset, onboarding, readiness checklist | offices, schools, IT |
| Q4 | year-end (Oct–Dec) | inventory planning, stockouts, year-end reset, seasonal scents | facilities, e-commerce |

Calendar is a *claim on the reader's attention*, not decoration. The hook must appear in
why-now framing, in the checklist deadline and in the CTA.

### The date is chosen from the data, not from the calendar

The quarter is the *theme*; the publish date is a **runway to a peak**.

**Lead time: minimum 2 weeks, default ~1 month** (owner-set). The runway buys two things:
**authority maturation** — the post has been live and crawled for weeks before the demand
arrives — and time to make sure the **conversion path is actually live** (stock, price,
offer, links) so the arriving traffic can buy.

So: queue the brief with its target date, publish inside the window, and never publish early
"because the draft is ready" or late and miss the peak. The peak window comes from Agent 1A's
12-month series (`references/02` §6).

The `calendar_hook` in the input form sets the angle; `publish_target` is derived by the
research and only then approved at Gate 2.

## What the skill does automatically

From the compulsory inputs it derives: keyword candidates, product candidates, audience
persona, FAQ outline, cost-per-use block inputs, internal link map, image briefs, meta
fields, JSON-LD, CTA ladder. You approve by exception, not by default.

---

## GATE 1 — restate the brief before any research

Post this block and wait. Do not research on an ambiguous brief.

```
BRIEF AS UNDERSTOOD
  topic:        ...
  buyer:        ...
  angle:        ...
  products:     ...        (or "auto — to be proposed in Gate 2")
  calendar:     ...
  cta:          ...
  model:        ...
  publish:      ...
CONFLICTS I ALREADY SEE
  - ...                    (or "none")
```

**Why this gate exists:** in the first live test, the session opened with "let's start the
test" and the topic line was never resolved — the run died on a model switch with the brief
still open. One paragraph here prevents that.

---

## Worked example (real, 2026-09-23)

The test brief, and what it produced at Gate 1:

```
topic:        cost + labour + speed in restaurant table turnover
buyer:        food-service operations (GM / FOH manager, multi-unit or owner-operator)
angle:        cost-per-use + operational efficiency, comparison via cost and format
products:     Table Bussers® Autumn-Scented + Table Bussers® Unscented (specified, not auto)
calendar:     Q4 (year-end)
cta:          "Reduce Table Turnover Time"
model:        A
publish:      ~2026-09-30
CONFLICTS SEEN: (1) every product-level keyword has zero Google Trends volume, so the
                  keyword must be the operational cluster, not the product;
                (2) a blog published 2026-08-31 already targets table turnover with Table
                  Bussers — cannibalisation risk, differentiate or plan an update;
                (3) the requested CTA is an untested outcome claim → MEDIUM, needs Dean.
```

All three conflicts were real and all three were found *before* any copy was written.
That is the value of the gate.

---

## 5. Audience segments — auto-detected, you confirm

Between the persona and the calendar sits the segment. Pick it in the brief; it decides the angle,
the proof and the CTA tone.

| Segment | Buying pattern | What moves them | Hook |
|---|---|---|---|
| Fitness studios | B2B bulk, supply-chain and compliance cost | total cost of ownership | bundle + ROI |
| Yoga instructors | individual purchase, sustainability guilt, premium price sensitivity | materials and certifications | plant-based + certification |
| Office managers | Q1 budget cycle, employee wellbeing | skin safety, volume discount | volume pricing |
| Facilities managers | procurement, cost first | measured data | TURI data + performance metrics |

## 6. Product recommendation when `products: auto` — five steps

1. extract the hook's attributes; 2. match product families; 3. cross the claims matrix (what each
SKU may say); 4. rank by commercial intent (primary / premium upsell / cross-sell); 5. present the
**top 3 with the reason for each**.
The skill proposes three and the owner chooses or overrides — that is what gives Gate 2 content.

## 7. Pre-generation checklist (12 fields, each takes `auto`)

topic/keyword · calendar hook · CRO goal · blog type · products · audience · meta title ·
meta description · primary CTA · internal links · images · interactive section.

## 8. Red flags that force Model C (human-led)

A new SKU launch · competitor targeting · a "custom" post requested by an executive · a VIP customer
case study · regulatory or claims-audit sensitivity. Any of these and the human stops being the
reviewer and becomes the author of record.

## 9. The filled-form format (what makes Gate 2 auditable)

```yaml
<field>: <what the skill proposes>
  your_edit: ACCEPT | EDIT | OVERRIDE
  reason:   <required when EDIT or OVERRIDE>
```

The `your_edit` line is the difference between an approval and an assumption. A Gate 2 record
without it is not an approval.
