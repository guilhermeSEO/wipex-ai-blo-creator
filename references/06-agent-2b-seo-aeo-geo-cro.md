# 06 — AGENT 2B: SEO + AEO + GEO + CRO/CTR

One specification sheet, produced from the finished draft. Nothing here may contradict the
claims envelope from `references/03`.

---

## 1. Meta title — 65 characters EXACTLY

Formula: `[primary keyword in the first 5 words] + [benefit or hook] + [emotion/urgency]`

- Count every character. Exactly 65, not "about 65".
- Primary keyword first. No brand name unless there is room last.
- Never use absolutes ("best") without the test to back it — and on a `P = —` product, never.
- Produce 2–3 candidates, show the live character count for each, and **record the rejected ones
  with the reason** (e.g. "rejected: 'Turn Rate' is jargon the buyer does not use"). A rejection
  with a stated reason is reviewable; a rejection by taste is not.

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

- Flesch-Kincaid 6–8 and **Flesch Reading Ease 60–70** (plain); passive <10%; average sentence
  <15 words; average paragraph 35–55 words.
- Measure on **paragraph text only** — tables, lists, headings and captions are excluded, or the
  grade reports the layout instead of the prose (`references/12`).
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

---

## 11. E-E-A-T scaffold — four signals, four places, all of them real

Score each signal with a yes/no before delivery. **If the signal is not real, it does not appear** — a
fabricated trust marker is a compliance finding, not a CRO win.

| Signal | What it looks like | Where it goes |
|---|---|---|
| **Experience** | two concrete use cases from the reader's own operation | body, right after the proof/data section |
| **Expertise** | author byline + the credentials actually held | byline block |
| **Authoritativeness** | two external references, one of them a study | body, next to the data they support |
| **Trustworthiness** | price, availability, freight/lead time, and what is *not* claimed | immediately before the first CTA and again at the close |

## 12. Citation triggers — the complete set

Use them **before** the data claim they introduce, not after:

1. `According to [source]…`
2. `Testing showed that…`
3. `[N] operators / [N]% of …` — only with a real count, and only if the source is named
4. `Wipex lab testing methodology: …` — only on a product whose envelope carries the test

Trigger 3 with an invented count is the single most common way a draft breaks the no-invented-facts
rule. If the count is not in hand, drop the trigger and state the claim qualitatively.

## 13. The snippet and PAA molds

**Featured-snippet answer** — five bullets, each `• <axis>: <micro-proof + source>`, placed early
(after the intro, before the argument):

```
• Cost: <the unit this post manages> — <figure and source>
• Time: <reset/consumption figure> — <source>
• Labour: <share of expense> — <source>
• Format: <what changes operationally>
• Proof: <certification or test, in its exact approved wording>
```

**People-also-ask questions** — use the question format a searcher types, and answer it inside the
first 40 words of the FAQ answer (the rest of the answer can develop the point).

**Rich snippets:** Shopping and rating snippets only when the data is real. A product schema without
data still earns the plain result; an invented `aggregateRating` earns a penalty.

## 14. Choosing the title by the signal you actually have

Auditable decision, not taste:

1. if there is a **real price promotion** → the title carries the saving ("Save X%")
2. else if there is a **strong measured figure the envelope allows** → the title carries the number
3. else → the title carries the operational benefit or the audience
4. never a superlative in place of a signal (see §1)

Record which branch was taken in the spec, so the choice can be reviewed later.

## 15. CTA copy and friction reduction

**CTA copy answers two questions:** what do I get, and why now. "Shop now" and "Learn more" are not
copy. "Build the par level for your room", "Compare the two formats", "Get the bulk case rate" are.

A CTA that is specific about the next step converts better than a louder one. Friction reducers,
each only if the offer genuinely exists:

- a one-page business case the buyer can hand to whoever approves spend
- the format chooser / par-level checklist
- a starter or sample format for a first order
- the freight term and the lead time stated next to the price
- bulk case rate on request

**Do not** promise a consultation, a demo, a trial or a discount that is not live at publish time —
the pre-peak readiness pass (Phase 3 checklist, `references/09`) verifies every one of them.

## 16. GEO variants and geo schema — considered and rejected

Two tactics from the earlier strategy documents are **not** used, and the reason is recorded in
`references/14-superseded-rules.md`: publishing the same post as state-by-state variants (duplicate
content and cannibalisation, on top of the angle-delta rule), and page-level `ServiceArea` /
`geo_shape` schema (a blog post does not serve a geographic area; the signal belongs in prose drawn
from measured sub-regions, per §8).

