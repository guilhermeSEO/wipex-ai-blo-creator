# 06 — AGENT 2B: SEO + AEO + GEO + CRO/CTR

One specification sheet, produced from the finished draft. Nothing here may contradict the
claims envelope from `references/03`.

---

## 1. Meta title — 65 characters EXACTLY

Formula: `[primary keyword in the first 5 words] + [benefit or hook] + [emotion/urgency]`

- Count every character. Exactly 65, not "about 65".
- Primary keyword first. No brand name unless there is room last.
- Never use absolutes ("best") without the test to back it — and on a `P = —` product, never.
- Produce 2–3 candidates, pick one, show the live character count for each.

## 2. Meta description — 155 characters EXACTLY

Formula: `[problem] + [solution] + [proof] + [CTA]`

House reality: live metas run 133–166 chars (mean 146). The owner standard is 155 exact —
follow the standard and note the house variance in the spec.

## 3. URL slug

Lowercase, hyphens only, keyword-forward, no ® or special characters
(Part 7: "handles carry no ® or special characters").

---

## 4. JSON-LD — merged, always

```json
{
  "@context": "https://schema.org",
  "@type": ["BlogPosting", "FAQPage", "Product", "BreadcrumbList"],
  "headline": "<the H1>",
  "alternativeHeadline": "<angle variant>",
  "author": {"@type": "Organization", "name": "Wipex", "url": "https://wipex.co"},
  "publisher": {"@type": "Organization", "name": "Wipex",
                "logo": {"@type": "ImageObject", "url": "https://wipex.co/logo.png"}},
  "datePublished": "<YYYY-MM-DD>", "dateModified": "<YYYY-MM-DD>",
  "image": [{"@type": "ImageObject", "url": "<hero>", "width": 1200, "height": 800}],
  "mainEntity": {"@type": "FAQPage", "mainEntity": [<every FAQ Q&A>]},
  "offers": {"@type": "Product", "name": "<Part 4 canonical>", "sku": "<SKU>",
             "priceCurrency": "USD", "price": "<live price>"},
  "keywords": "<primary, lsi, intent>"
}
```

Rules: it must validate as JSON; prices must match the live product JSON; only include
`aggregateRating` if real ratings exist (never invent a rating or review count); the FAQ
entities must be the actual FAQ questions on the page.

---

## 5. Internal link map

| Rule | Target |
|---|---|
| Links to `/products/` in body | 4 – 10 |
| Links to `/blogs/` in body | 4 – 8 |
| Placement | hero, after the cost block, and one per major section |
| Anchor text | commercial and descriptive — `Shop Table Bussers® Autumn-Scented →`, never "click here" |
| Collection support | the house links heavily to collections (`/collections/food-service-commercial`, `all-purpose-wipes`, `plant-based-collection`) |
| Cluster | link the nearest existing post (see the cannibalisation result) both ways |

Deliver as a table: `anchor text | destination | placement | why`.

---

## 6. Readability + entity clarity

- Flesch-Kincaid 6–8; passive <10%; average sentence <15 words; average paragraph 35–55 words.
- Report the measured numbers, not adjectives.
- **Entity clarity:** every key statement = exact product + specification + benefit + proof.
  ✘ "our wipes clean well" → ✔ "Table Bussers® (400-count, plant-based viscose) lift residue
  from tables and counters" + patch-test line.

---

## 7. AEO — how to be the paragraph an LLM quotes

- Direct answer in the first 40–50 words after the H1, and again as the ANSWER module.
- **Citation triggers:** "According to [source]…", "Testing showed…", "[N] operators / [N]%".
- **Data density:** minimum 3 specific sourced figures per post.
- **Structured answers:** the FAQPage entities mirror the on-page FAQ exactly.
- **Featured snippet:** one bulleted answer to the primary question, early, tightly worded.
- Every claim that an LLM might quote must be one the claims envelope actually allows.

---

## 8. GEO — geographic signals from evidence, not habit

Use the Trends subregion data from 1A. For the test run, **CA, FL and TX appeared in the top
few subregions of 4 of 6 probed terms** (cost per use: CA 27, FL 25, TX 23; busser: FL 46,
TX 44; table turnover: CA 11, FL 8). Place them naturally:

- a sentence naming regions ("from coastal studios to inland operators")
- one concrete geographic example (climate, density, season)
- no forced geo-stuffing; a paragraph that reads like a brochure defeats the purpose

Caveat to state in the spec: small states over-index on normalised Trends data; the big
markets carry the absolute mass.

---

## 9. CRO and CTR

- **4 CTAs** per the ladder in `references/05` §4.
- **Urgency, 2–3 tactics, never pushy:** seasonal window, stock/par level, pricing/format
  advantage. No fake countdowns, no invented scarcity.
- **Social proof, 3–4 types,** each with a real number: reorder/retention if known, ratings
  only if real, certifications, published third-party stats. **Never invent a testimonial.**
- **Objection handling:** the FAQ plus one proactive mention in body copy.
- **Friction reduction:** make the next step concrete (checklist download, format chooser,
  bulk pricing request, sample).
- **Pre-peak readiness (the whole point of the runway):** the post scores a click only to hand
  the reader to a page that must work. Before the peak window opens, confirm product in stock,
  price matching the copy, the offer/sample/bulk route live, and every internal link resolving.
  A ranked post pointing at a dead checkout converts nothing.
- **CTR:** the title carries the keyword plus a specific benefit; the meta carries problem +
  proof + action. No superlatives.

---

## 10. Output — SEO specification sheet

```markdown
# SEO SPECIFICATION
meta_title:      <65 chars exact>   (chars: 65)
meta_description: <155 chars exact> (chars: 155)
slug:             <lowercase-hyphens>
json_ld:          <full block, validated>
internal_links:   <table>
readability:      FK grade / passive% / avg sentence / avg paragraph / reading time
keyword_coverage: primary in H1+title+meta+first 100 words; LSI 2–3× each; intent in CTA
image_alt_text:   <list with char counts>
geo_signals:      <where and why>
cro_audit:        CTAs 4 · urgency 2–3 · social proof 3–4 · objections ≥4 · friction steps
                   ae o: citation triggers · data points · snippet answer
honest_limits:    <what is NOT claimed and why>
```

**Never publish an expectation as a promise.** Anything of the form "8–12% CTR",
"15–25% conversion" is a projection. Label it as a projection and keep it out of the copy.
