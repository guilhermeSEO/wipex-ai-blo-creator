# 08 — THE HOUSE PATTERN (measured from 21 live posts, 2026-09-23)

This file is the reason v2.1 exists. It records what Wipex actually publishes, so a draft
can be scored against reality instead of against a plausible template.

**Method:** Shopify blog atom feeds (`/blogs/library.atom`, `/blogs/wipex-studio-library.atom`,
3 pages each) → 37 unique entries → 21 most recent by `published` → each article page fetched
→ body sliced from `<div class="rte text-spacing">` by `<div>` depth counting → metrics computed.

> `/blogs/<handle>/articles.json` returns **404** on this store. Use the atom feeds; the atom
> `<entry>` carries title, author and date but **no content** — the body must come from the
> article page itself.

---

## 1. Per-post measurements (21 most recent)

| # | Date | Words | H2 | H3 | Paras | Avg ¶ | Imgs | Tables | FAQ | Prod links | Blog links | Meta chars | JSON-LD | Title |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-21 | 3,918 | 20 | 19 | 60 | 43 | 52 | 0 | ✔ | 4 | 39 | 150 | 3 | Fall Facility Readiness 2026 |
| 2 | 2026-09-17 | 4,561 | 23 | 25 | 83 | 40 | 54 | 1 | ✔ | 9 | 33 | 151 | 2 | World Cleanup Day 2026: Gym Cleaning Routine |
| 3 | 2026-09-14 | 3,080 | 19 | 14 | 53 | 44 | 54 | 1 | ✔ | 7 | 29 | 162 | 3 | 70% IPA Wipes: When Facilities Use Them |
| 4 | 2026-09-10 | 4,053 | 21 | 11 | 52 | 53 | 53 | 1 | ✔ | 5 | 32 | 133 | 0 | Flu Season Preparedness |
| 5 | 2026-09-03 | 2,846 | 13 | 4 | 65 | 38 | 50 | 0 | ✔ | 8 | 30 | 0 | 1 | US Labor Day → Fall Reset |
| 6 | 2026-08-31 | 3,977 | 20 | 11 | 74 | 46 | 53 | 1 | ✔ | 7 | 29 | 155 | 1 | Gym Cleaning Procurement |
| 7 | 2026-08-31 | 3,416 | 18 | 15 | 78 | 35 | 51 | 1 | ✔ | 5 | 29 | 154 | 3 | **How Table Bussers Improve Restaurant Efficiency and Table Turnover** |
| 8 | 2026-08-27 | 3,878 | 18 | 6 | 71 | 49 | 53 | 1 | ✔ | 10 | 29 | 155 | 1 | Commercial Gym Cleaning Supplies |
| 9 | 2026-08-25 | 4,011 | 22 | 27 | 74 | 38 | 56 | 1 | ✔ | 9 | 40 | 156 | 3 | Buying Wipes in Bulk |
| 10 | 2026-08-25 | 3,729 | 26 | 34 | 89 | 36 | 53 | 1 | ✔ | 0 | 29 | 152 | 3 | Yoga Studio Hygiene Standards |
| 11 | 2026-08-24 | 3,728 | 19 | 36 | 82 | 39 | 53 | 1 | ✔ | 14 | 33 | 147 | 3 | Smarter Cleaning System, High-Traffic Fitness |
| 12 | 2026-08-21 | 2,707 | 13 | 4 | 60 | 41 | 46 | 0 | ✔ | 0 | 29 | 161 | 1 | Reduce Wipe Waste with a Refill Roll |
| 13 | 2026-08-19 | 3,016 | 18 | 16 | 54 | 43 | 55 | 1 | ✔ | 14 | 29 | 158 | 3 | Pilates Fall 2026 Guide |
| 14 | 2026-08-18 | 3,536 | 18 | 27 | 62 | 44 | 48 | 1 | ✔ | 2 | 29 | 154 | 3 | Fall Gym Cleaning Checklist |
| 15 | 2026-08-14 | 3,812 | 18 | 12 | 54 | 52 | 51 | 1 | ✔ | 7 | 29 | 162 | 0 | Bulk IPA Wipes Buyer's Guide |
| 16 | 2026-08-12 | 4,762 | 20 | 20 | 70 | 49 | 51 | 1 | ✔ | 7 | 29 | 135 | 3 | Gym Wipe Dispensers vs. Buckets |
| 17 | 2026-07-28 | 2,738 | 16 | 10 | 39 | 64 | 58 | 0 | ✔ | 4 | 31 | 156 | 0 | Back-to-Office Cleaning Checklist |
| 18 | 2026-07-28 | 3,843 | 19 | 24 | 78 | 42 | 55 | 1 | ✔ | 6 | 33 | 148 | 0 | Team Health, Flu Season |
| 19 | 2026-07-23 | 3,262 | 14 | 8 | 48 | 57 | 59 | 0 | ✘ | 4 | 29 | 158 | 0 | Member Confidence, Cleaner Fitness |
| 20 | 2026-07-20 | 3,650 | 19 | 33 | 72 | 36 | 60 | 0 | ✔ | 16 | 29 | 166 | 0 | Cyclosporiasis & Surface Sanitation |
| 21 | 2026-07-14 | 2,578 | 15 | 6 | 40 | 72 | 57 | 0 | ✔ | 3 | 31 | 154 | 0 | Back-to-School Cleaning Checklist |

"Prod links" = anchors to `/products/` inside the body. The raw link totals (~520–560) are
dominated by theme chrome (nav, footer, currency, cross-sell) and are not a useful target.

---

## 2. Real examples of the modules (verbatim from the corpus)

**Quick answer / key takeaways** — 5 bullets, each with a number:
```
Quick answer / key takeaways
• Restock in August. Order 4–6 weeks ahead of the September traffic spike, not after it.
• Budget 1.5–2.5 wipes per check-in and add a 25% seasonal buffer for fall.
• Hold a 60-day par level of bulk refill rolls at every location.
• Two-product system: plant-based wipes for member self-service, EPA-registered disinfecting
  wipes for staff cleaning cycles.
• One dispenser per 800–1,000 sq ft so no member walks more than 15 feet for a wipe.
```

**On this page** — jump-link TOC with short labels:
```
On this page · Which system fits your facility? · How Cost Per Wipe Works · Buckets: Best
Use Cases · Dispenser + Refill: Best Use Cases · Product Tools · Side-by-Side Comparison ·
Wall vs. Floor Standing · Build Your System · FAQ
```

**Stat cards** — value + label pairs rendered as cards:
```
2–3×      Cost premium on emergency retail restocks vs. bulk
20–40%    Typical increase in wipe consumption during fall onboarding
15 sec    Kill time for Wipex EPA-registered disinfecting wipes
```

**Direct-answer opener** (the AEO payload):
```
Bulk isopropyl alcohol wipes are the workhorse of facility cleaning — fast-drying,
residue-free, and cost-efficient at volume.
…By the end, you will know exactly which bulk configuration fits your facility, how to
compare wholesale pricing accurately, and where alcohol wipes end and EPA-Registered
disinfecting wipes begin.
```

**Cost-per-wipe module** — appears in 4 of the recent posts, twice as the literal H2
"How to Calculate Your True Cost Per Wipe". Companion copy uses the format
`~$0.09/Wipe` directly in meta titles.

**Reviewer byline:**
```
Wipex — Facility Supply Team
Industrial & medical cleaning specialists · Reviewed August 14, 2026
```

**CTA anchor style** (verb + product/collection + arrow):
```
Shop Table Bussers® Autumn-Scented →      Shop Autumn-Scented →
Shop Table Bussers® Unscented →           Equip Your Service Stations →
See how Table Bussers® simplify the cleaning step →
Browse Cleaning Wipes →
```

**Recurring H2 labels worth reusing:** "How to Calculate Your True Cost Per Wipe" ·
"Which Setup Is Right for Your Facility?" · "Find your system" · "Keep Reading" ·
"Frequently Asked Questions" · "Your <season> <place> Readiness Checklist" ·
"Ordering 1 pallet or more?" · "What operators say" · "A <thing> isn't done when…"

---

## 3. Authors of record

`Lívia Schlemmer` (16 of 21) and `guilherme@rjl.com.br User` (5 of 21). Match the byline to
the author actually responsible before publishing.

---

## 4. Cannibalisation map (build this before every brief)

The 21 recent posts cluster into: seasonal resets (fall/back-to-school/back-to-office),
procurement and bulk buying, cost-per-use and format choice (bucket vs dispenser vs refill),
compliance and health events (flu, cyclosporiasis), and verticals (yoga, pilates, gym,
office, lab, food service).

Known overlaps to respect:

| Territory | Already owned by |
|---|---|
| Table Bussers + table turnover + four-step workflow | `table-busser-restaurant-efficiency` (2026-08-31) |
| Cost per wipe + bucket vs dispenser vs refill | `gym-wipe-dispenser-vs-bucket` (2026-08-12), `bulk-isopropyl-alcohol-wipes-buyers-guide` (2026-08-14), `bulk-wipe-refill-rolls-800ct` (2026-08-21), `buy-cleaning-wipes-in-bulk` (2026-08-25) |
| Bulk buying, MOQs, facility accounts | `buy-cleaning-wipes-in-bulk` (2026-08-25) |
| Gym procurement / supply systems | `bulk-gym-cleaning-wipes-supplies` (2026-08-31), `commercial-gym-cleaning-supplies` (2026-08-27) |
| Yoga studio hygiene standards | `yoga-studio-hygiene-standards` (2026-08-25) |

A new post enters as a **new angle or a new stage of the job**, and links both ways with the
nearest existing post. Reusing the product is expected — the same SKU legitimately appears in
several posts with different angles (see the Table Bussers and bulk-buying rows above). What
must never repeat is the angle, and the publish date should land **2–4 weeks before** the
term's next peak (min 2 weeks, default ~1 month — `references/02` §6).

---

## 5. Re-measure quarterly (or after a design change)

```bash
python scripts/audit_blog_patterns.py --corpus        # refresh the 21-post table
python scripts/audit_blog_patterns.py --draft <file>  # score one draft
```

If the house drifts (length, module set, meta length), update the table in this file and in
`SKILL.md`, and bump the skill version with a changelog line. The pattern file going stale is
how a skill quietly starts producing off-brand work.
