# 2B — SEO / AEO / GEO / CRO SPECIFICATION
### Blog #1 · "Cost per table" · food-service · Q4 · target publish 2026-11-08

Compliance note: nothing in this spec asserts a product performance claim. The only numbers
permitted are our own prices, and third-party restaurant-operations figures with source + date.

---

## 1. META FIELDS (counted character-by-character)

```
TITLE (65 chars, exact)
Cost Per Table for Restaurants: Cut Cost, Not the Standard, in Q4
```
- primary keyword "Cost Per Table" in words 1–3 ✅
- benefit/hook: "Cut Cost, Not the Standard" · urgency: "Q4"

```
META DESCRIPTION (155 chars, exact)
Cost per table, not per wipe. Calculate your restaurant reset cost, add the labour minute, and cut Q4 spend without lowering standards. Read the guide now.
```
- problem ("cost per table, not per wipe") + method ("add the labour minute") + CTA ("Read the guide now")

```
SLUG
cost-per-table-restaurant
```
Lowercase, hyphens only, no ® or special characters (Part 7).

**Title candidates considered and rejected:** "…How to Calculate Yours Before Q4" (64) ·
"…Cut the Cost, Raise the Turn Rate" (65, rejected — "Turn Rate" is jargon the buyer does not
search) · "Restaurant Cost Per Table: How to Calculate and Cut It in Q4" (60).

---

## 2. JSON-LD (merged — BlogPosting + FAQPage + Product + BreadcrumbList)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BlogPosting",
      "headline": "How to Calculate Cost Per Table for a Restaurant (and Cut It Without Cutting Standards)",
      "alternativeHeadline": "Cost Per Table for Restaurants: Cut Cost, Not the Standard, in Q4",
      "author": { "@type": "Organization", "name": "Wipex", "url": "https://wipex.co" },
      "publisher": {
        "@type": "Organization",
        "name": "Wipex",
        "logo": { "@type": "ImageObject", "url": "https://wipex.co/logo.png" }
      },
      "datePublished": "2026-11-08",
      "dateModified": "2026-11-08",
      "image": [{ "@type": "ImageObject", "url": "<HERO_URL>", "width": 1200, "height": 800 }],
      "keywords": "cost per table, cost per cover, restaurant cost per table, restaurant cleaning cost, table reset time",
      "articleSection": "Food Service",
      "mentions": [
        { "@type": "Thing", "name": "Table Bussers Autumn-Scented" },
        { "@type": "Thing", "name": "Table Bussers Unscented" }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "What is cost per table, and how is it different from cost per wipe?",
          "acceptedAnswer": { "@type": "Answer", "text": "<the first two sentences of FAQ 1, verbatim>" } },
        { "@type": "Question", "name": "How do I calculate my own cost per table?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 2, verbatim>" } },
        { "@type": "Question", "name": "What is a good table reset time?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 3, verbatim>" } },
        { "@type": "Question", "name": "How many wipes does one reset take?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 4, verbatim>" } },
        { "@type": "Question", "name": "How does cost per cover relate to cost per table?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 5, verbatim>" } },
        { "@type": "Question", "name": "Should I use scented or unscented across the dining room and the bar?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 6, verbatim>" } },
        { "@type": "Question", "name": "What should I check before switching table-cleaning supplies?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 7, verbatim>" } },
        { "@type": "Question", "name": "Should labour minutes count in my cleaning cost?",
          "acceptedAnswer": { "@type": "Answer", "text": "<FAQ 8, verbatim>" } }
      ]
    },
    {
      "@type": "Product",
      "name": "Table Bussers Surface Wipes (scented, cinnamon-clove; autumn variant)",
      "sku": "WX01126TN",
      "brand": { "@type": "Brand", "name": "Wipex" },
      "offers": { "@type": "Offer", "priceCurrency": "USD", "price": "36.99",
                  "availability": "https://schema.org/InStock",
                  "url": "https://wipex.co/products/table-bussers-surface-wipes" }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://wipex.co" },
        { "@type": "ListItem", "position": 2, "name": "Library", "item": "https://wipex.co/blogs/library" },
        { "@type": "ListItem", "position": 3, "name": "Cost Per Table for Restaurants" }
      ]
    }
  ]
}
```

**Deliberately omitted:**
- `aggregateRating` / `reviewCount` — no real review data was supplied, and inventing a rating is
  forbidden. Add it later only if genuine reviews exist.
- `EWG Verified` in any form — Part 4 shows `E = —` for both SKUs and the conflict is with Dean.
- Any `Review` / `Testimonial` block — we have no verified testimonial, and the skill forbids
  inventing proof.

---

## 3. INTERNAL LINK MAP (12 links: 5 product, 5 blog, 2 collection)

| Anchor text | Destination | Placement |
|---|---|---|
| 400-count Table Bussers® bucket | `/products/table-bussers-surface-wipes` | hero / Step 1 of the cost block |
| Table Bussers® Autumn-Scented | `/products/table-bussers-surface-wipes` | bar/patio section |
| Table Bussers® Unscented | `/products/table-bussers-unscented` | bar/patio section |
| Shop Table Bussers® Autumn-Scented → | `/products/table-bussers-surface-wipes` | closing CTA |
| Shop Table Bussers® Unscented → | `/products/table-bussers-unscented` | closing CTA |
| food service and commercial collection | `/collections/food-service-commercial` | price ladder |
| Browse the food service collection → | `/collections/food-service-commercial` | closing CTA |
| how table bussers improve restaurant efficiency and table turnover | `/blogs/library/table-busser-restaurant-efficiency` | four-step reset **+ Keep reading** |
| Gym wipe dispensers vs buckets | `/blogs/library/gym-wipe-dispenser-vs-bucket` | Keep reading |
| Buying wipes in bulk | `/blogs/library/buy-cleaning-wipes-in-bulk` | Keep reading |
| Commercial gym cleaning supplies | `/blogs/library/bulk-gym-cleaning-wipes-supplies` | Keep reading |

**Reciprocal link to add on the 2026-08-31 post:** in its "The Cleaning Step Is Part of the
Workflow" section, link the phrase *"cost per table"* to this post. Without the reverse link the
cluster does not consolidate.

---

## 4. READABILITY (measured on the paragraph text, excluding tables/lists)

| Metric | Measured | Target | Verdict |
|---|---|---|---|
| Flesch-Kincaid grade | **7.8** | 6–8 | ✅ |
| Flesch Reading Ease | 69.4 | 60–70 (plain) | ✅ |
| Words per sentence | 16.9 | <15 (house) | ⚠️ slightly over; the two longest sentences were split (54w → 4 sentences, 50w → 3) |
| Passive voice | 3.1% | <10% | ✅ |
| Avg paragraph | 38 words | 35–55 | ✅ |
| Paragraph count | 59 | 50–80 | ✅ |
| Reading time | ~13 min | — | |

---

## 5. KEYWORD COVERAGE

| Position | Content |
|---|---|
| Primary `cost per table` | H1 ✅ · meta title ✅ · meta description ✅ · first 100 words ✅ · H2 "What cost per table means" ✅ · repeated naturally |
| LSI `cost per cover` | H2 "Bar, patio and private room" ✅ · FAQ 5 ✅ · self-assessment ✅ |
| LSI `cleaning supplies cost` | cost block ✅ (expressed as spend/consumable, not as a stuffed phrase) |
| LSI `table reset time` | H2 "The four-step reset" ✅ · FAQ 3 ✅ · self-assessment ✅ |
| Intent keyword `cost per table restaurant` | meta title, slug, FAQ 2 ✅ |
| Density | primary ~1.1% — natural, no stuffing |
| **Explicitly absent** | `cost per wipe` (saturated in-corpus), `cost per use` (polluted intent), `food-safe`, `safe on` |

---

## 6. GEO SIGNALS

Trends 12-m subregions for `cost per use` (the closest measured proxy): **CA 27 · GA 26 · FL 24 ·
TX 23**, with WY/DC over-indexing on thin volume.

- named in the bar/patio section through climate logic ("partly open to the street") rather than
  as a list of states
- **Las Posadas / CA-TX-FL** is *not* used here — that belongs to the December occasion post, not
  to a cost-per-table guide. Forcing it would read like a brochure.
- secondary markets for internal linking: Georgia, Utah, New York

---

## 7. CRO AUDIT (4-rung CTA ladder)

| Rung | Placement | Copy | Type |
|---|---|---|---|
| 1 | after the cost block | "400-count Table Bussers® bucket" (inline product link) | soft, informational |
| 2 | after the price ladder | browse the food service collection | consideration |
| 3 | after the checklist / FAQ | measured self-assessment → product links | action |
| 4 | closing | **"Reduce Table Turnover Time"** + 3 arrow anchors | per brief |

- **Urgency (2 tactics, not pushy):** the Q4 volume window and the year-end par-level decision.
  No countdowns, no invented scarcity.
- **Social proof (honest, thin by design):** three certification facts only — NSF (Autumn),
  TÜV-certified cloth (both), plant-based viscose cloth (both). **No testimonials, no customer
  counts, no ratings** — none were supplied and the skill forbids inventing them. This is a
  deliberate gap to fill when Marketing can supply real review data.
- **Objection handling:** 4 objections in body copy + 8 in the FAQ.
- **Friction reduction:** the self-assessment worksheet, the par-level arithmetic, the printable
  checklist.

⚠️ **A rejected proof point.** The live product pages carry *"Winner of Food & Beverage Magazine
Editor's Top Picks Summer 2025"*. It is **not used in this copy**: an award is a badge, and Part 4
does not grant an award claim for either SKU. It goes to Dean as a possible v1.2 addition — see 2C.

---

## 8. FEATURED SNIPPET / AEO TARGET

- **Target question:** "how to calculate cost per table for a restaurant"
- **Direct answer, first 40 words:** *"Cost per table is the total cost of returning one table to
  service — the consumable, the labour minutes, and the share of supplies a single reset consumes —
  divided by how many times the table turns."*
- **Structured answers:** the 8 FAQPage entities mirror the on-page FAQ verbatim.
- **Data density:** 6 sourced third-party figures + own price arithmetic.

---

## 9. HONEST LIMITS OF THIS SPEC

- **No absolute search volume.** Not obtainable from Trends; requires SEMrush/Ahrefs/GSC.
- **Expectations are projections, not promises.** Any CTR or conversion figure would be a guess and
  is therefore omitted. The realistic band for a mid-volatility operational term against
  restaurant-tech incumbents (Toast, TouchBistro, WebstaurantStore) is 3–6 months to a stable
  position, first page not guaranteed.
- **Social proof is thin** (§7) — by policy, not by oversight.