# 1C — AUDIENCE, OBJECTIONS, FAQ

## Persona (filled block)
```yaml
primary_persona:
  title:            Procurement manager / Operations director / Multi-unit (franchise) owner
  segment:          multi-location operators across MIXED facility types (fitness, food service, office)
  team_they_control: site managers and the staff who reorder; a facilities/BSC vendor they hold to a spec
  budget_lines:     consumables (supplies), OPEX per site, vendor contracts, freight
  patches_they_care_about: cost per wipe/use, spend visibility across sites, reorder discipline,
                           one approved SKU list, vendor leverage, compliance paper trail
secondary_persona: single-site owner-operator who wants the same discipline without the committee
top_3_pains:
  1: "Every location buys its own wipes from whoever is cheapest that week — no two sites run the same SKU."
  2: "We can't see what we spend or what we consume per site until the invoices pile up."
  3: "Emergency/reactive reorders cost more and we carry the wrong stock at the wrong sites."
buying_criteria_ranked:
  - unit cost at the volume tier the whole footprint unlocks
  - one SKU list that works across facility types (format + dispenser fit)
  - reorder that runs itself (par level / recurring delivery)
  - a vendor that invoices and ships across all locations
decision_timeline:
  - planned path (Q4 budget / annual contract) -> 4-8 weeks
  - urgent path (opening, audit, stockout) -> same week
where_they_research:
  - "commercial cleaning supplies", "bulk / wholesale janitorial supplies", "supplier account setup"
  - distributor sites (Grainger, ULine, WebstaurantStore, Zogics, FSIoffice) = the SERP competition
  - peer/BSC recommendations; procurement templates
objections:
  - "A pre-mixed wipe costs more per unit than concentrate + cloth." -> per-unit is the wrong denominator; count the labour minute and the reorder failure, and (for us) the wipe is the standard across every site.
  - "We're too small for volume pricing." -> volume tier is unlocked by cumulative footprint + standardization across sites, not one order (Opora: standardize SKUs across sites to capture volume pricing without one large order).
  - "Our sites are different, so they need different products." -> different rooms, one approved list per category; formats vary by site or consolidation fails (The Cleaning Station).
  - "Changing suppliers mid-year is disruptive." -> the program is additive: standardize the list first, reorder discipline second, vendor leverage third.
  - "How do I know a site is running the program?" -> visible signal: one dispenser format + labelled par levels per site.
```

## Buying criteria, ranked
1. Landed unit cost at the footprint's volume tier 2. One cross-vertical SKU/dispenser standard 3. Self-running reorder (par level) 4. Footprint-wide invoicing/shipping 5. Compliance/claims paper trail.

## Objections -> honest answers, and where the answer lives
| Objection | The only honest answer | Where it lives |
|---|---|---|
| "Per-unit a wipe is dearer than concentrate" | It moves cost from the consumable to the minute, and the minute is the larger term; the wipe also standardises every site | cost block |
| "We're too small for volume pricing" | Volume tier is unlocked by footprint + SKU standardisation, not one big order | volume-tiers section |
| "Our sites are too different to standardise" | Standardise one list per category; if formats vary by site, consolidation fails | SKU-consolidation section |
| "We don't know what we spend per site" | Par levels + one invoice give spend visibility; consolidation is the lever | reorder-planning section |
| "Do we need scented or unscented?" | Room decision: guest-facing vs back of house | product section |
| "What do we ask for in a quote?" | Footprint, SKU list, dispenser standard, delivery cadence, invoicing | purchasing-workflow section |

## FAQ outline (8 rows: pain -> benefit -> claim used -> CTA)
1. What is a multi-location cleaning supply procurement program? — direct definition (AEO payload) — Tier 3 — quote CTA
2. How do we get volume pricing if we can't place one huge order? — standardise SKUs across sites — cited (Opora) — volume-section CTA
3. How do we consolidate SKUs without breaking the sites? — audit, one per category, par levels by site — cited (Cleaning Station) — SKU-section CTA
4. How do we set reorder points/par levels? — formula (Daily Usage × Lead Time) + Safety Stock — cited (Cleaning Station) — reorder CTA
5. Should every location run the same dispenser? — one dispenser format is what makes the reorder run itself — hardware — dispenser CTA
6. What is a volume tier and how is it reached? — cumulative footprint tiering — our own ladder — quote CTA
7. What does a wipe procurement quote request need to include? — footprint, SKU list, cadence, invoicing — quote CTA
8. How do we measure whether the program is working? — cost per wipe/use per site + stockout rate — cost block CTA

## Citable external data (figure | source | date checked)
| Figure | Source | Date checked |
|---|---|---|
| Emergency orders to cover stockouts cost **20–30% more** than planned replenishment | Metro Wholesale, *Affordable Cleaning Supplies for Businesses* | 2026-09-28 |
| Centralised procurement spend **$4.92 per $1,000 revenue** vs **$6.10** decentralised | Metro Wholesale | 2026-09-28 |
| One org cut facility SKUs **from 300 to 60 core items** | Metro Wholesale | 2026-09-28 |
| Spend visibility through consolidation can cut costs **by up to 43%** | Metro Wholesale | 2026-09-28 |
| Departments paid **>23% above market** for MRO products without consolidated negotiation | Metro Wholesale (govt procurement study) | 2026-09-28 |
| Consolidating **80–90% of SKUs with one primary distributor** turns **$40k** of split spend into negotiating leverage | Opora Supply, *Bulk Buying Industrial Cleaning Supplies* | 2026-09-28 |
| Par Level = **(Daily Usage Rate × Lead Time) + Safety Stock** | The Cleaning Station, *Bulk Janitorial Supply Buying Guide* | 2026-09-28 |
| Large enterprises = **51.7%** of the contract cleaning-chemicals market (2025) — standardised high-volume operations | Grand View Research | 2026-09-28 |
| Janitorial equipment & supplies market **USD 67.3B (2025) → 98.8B (2033)** | OpenPR | 2026-09-28 |

**Rule:** these are context about the reader's operation. They are NEVER converted into a Wipex product claim.

## Own-price arithmetic (recomputed from live product JSON, 2026-09-28)
| SKU | Variant | Price | Count | $/wipe |
|---|---|---|---|---|
| Natural Gym Wipes Bulk Refill Roll 700ct (WX11121FN) | Single roll | $42.99 | 700 | ≈ $0.0614 |
| Natural Gym Wipes Bulk Refill Roll 700ct | 4-pack | $142.99 | 2,800 | ≈ $0.0511 |
| Plant-Based Bulk Rolls 700ct (WX72081LARP) | Full pallet (140 rolls) | $4,585.00 | 98,000 | ≈ $0.0468 |
| Table Bussers® (WX01126TN / WX72024TBB) | 1 bucket | $36.99 | 400 | ≈ $0.0925 |
| Table Bussers® | 4-pack case | $119.99 | 1,600 | ≈ $0.0750 |
| XL Bucket Dispenser (WX72134BKT) | Single | $12.99 | — | one-time hardware |
| Wall Dispenser (WX72244BWD) | Single | $119.99 | — | one-time hardware |
| Floor Dispenser (WX72192BFD) | Single | $249.99 | — | one-time hardware |

Adjacency guardrail: cost figures stay in cost paragraphs, never beside a performance claim, a percentage, or the word "safe".

## Consumption / reorder formula the reader keeps
```
Par level per site  = (daily wipes used × days of lead time) + safety stock
Footprint demand    = sum of site par levels
Footprint $/period  = footprint demand × $/wipe at the footprint's volume tier
```
Hand it over with the reader's own numbers; the arithmetic is the argument, the price is the invoice.

## Recommended structure for THIS post (reordered to the operate/govern angle)
Hero+promise · key takeaways (numbers) · on this page · direct-answer definition ·
stat cards · **why now (Q4 budget cycle)** · the 6-part program framework (H3 each):
1 reorder planning (par levels) · 2 volume tiers · 3 dispenser standardization ·
4 SKU consolidation · 5 recurring delivery · 6 cost-per-wipe · cost-per-use calculator ·
format/transport comparison table · readiness checklist (printable, Q4-bound) ·
FAQ (8) · keep reading (bilateral links to the two sourcing posts) · closing CTA band (quote).
