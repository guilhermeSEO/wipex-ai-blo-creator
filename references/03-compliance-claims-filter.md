# 03 — THE CLAIMS ENVELOPE (COMPLIANCE, UPSTREAM)

This is the step that decides whether the blog is publishable. Do it in Phase 1, before a
single line of copy exists.

**Source of truth (read-only):**
`C:\Users\guilh\AppData\Local\hermes\workdir\wipex\01-compliance\`

| File | Use |
|---|---|
| `Wipex-Claims-Filter-AI-Review-Pack-v1.1-ACTIVE.docx` | Parts 1–11 + Annex A. **Never edit** |
| `Never-Say-Prohibitions.csv` | 18 prohibited claims with why + correction |
| `Approved-Surface-Claims-16-Sentences.csv` | 16 pre-approved sentences by tier |
| `TURI-Results-Reference-v1.0.csv` | which cells are claimable, per soil/surface |
| `Wipex-Surface-Claims-Guide-Annex-A-v1.0.pdf` | the surface claims guide |

The .docx is a zip; extract text with:
```python
import zipfile, re, html
x = zipfile.ZipFile(path).read('word/document.xml').decode('utf8','ignore')
x = html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'</w:p>', '\n', x)))
```

---

## Part 4 — the SKU register, column order

The table flattens to one field per line. Columns, in order:

```
Canonical name | Cat. | SKU codes | Aliases | Substrate |
  N | Skin | Germ | Disinf. | P | C | E | Eco | Key restrictions
```

**Claim codes:** `N` natural-ingredients wording · `S3` full skin-safety set · `S1` skin-safe
only · `G` BZK skin germ-kill · `D` EPA disinfectant · `P` performance and
material-compatibility · `C` cloth compostability (page-verified) · `E` EWG Verified
(page-verified) · `Eco` plant-based-cloth sustainability. `—` = no claim of that type.
`v` after `C`/`E` = seen in page text on the crawl date.

**Rule of precedence:** (1) Filter Parts 2–7 → (2) Part 4 SKU register → (3) the product page
(as evidence a badge was granted, never as a source of wording) → (4) escalate.

### Worked rows (the test products)

| Field | Table Bussers Autumn (scented) | Table Bussers Unscented |
|---|---|---|
| Cat. | NAT-SURF | NAT-SURF |
| SKUs | WX01126TN, WX01130TN (+`-4`) | WX72024TBB (+`-2`, `-4`) |
| Substrate | viscose | viscose |
| N | ✅ | ✅ |
| Skin | S3 | S3 |
| Germ / Disinf. | — / — | — / — |
| **P** | **—** | **—** |
| C | `C v` | `C v` |
| **E** | **—** | **—** |
| Eco | ✅ | ✅ |
| Restrictions | NSF permitted (A-004); **no bare "Sustainable"**; "suitable for food service environments" | no NSF, no food-safe |

**→ Both are Tier 3 only. No numbers, no percentages, no "lab-tested", no "outperforms",
no "better than" about cleaning performance. That is the whole envelope.**

---

## The three tiers

- **Tier 1 — regulated:** disinfect, sanitize, antibacterial, antimicrobial, kills germs;
  hypoallergenic, dermatologically tested, safe on sensitive skin; EWG Verified, TÜV, EPA,
  NSF, FDA. Product-by-product, governed by Parts 3, 4, 6.3, 6.4.
- **Tier 2 — substantiated:** outperformed, removed X% more, lab-tested, lab-verified,
  independently tested, proven, material-compatible, any number/ratio/comparison. Only
  where a test says exactly that, for exactly that product, on exactly that surface.
  Today that is **the two fitness formulations (Lavender; Lemongrass & Eucalyptus) and
  EMPOWER — nothing else.**
- **Tier 3 — qualitative:** descriptive, non-comparative, non-numeric. Permitted on every
  non-BZK, non-EPA surface product, no test required. *"This is where the flexibility
  lives."*

One sentence can drift between tiers: *"gentle on vinyl"* is Tier 3; *"gentle on vinyl —
lab-verified"* is Tier 2 and needs the test.

---

## Word rules that break most drafts

| Never | Instead |
|---|---|
| "safe on [surface]", "safe for all", "won't damage" | "gentle on [material]", "designed for [material]", "tailored for [material]" |
| "all / any / every" surface, finish, floor | name the material; or "most" |
| "outperforms", "better than", "X% more" without a study | Tier 3 only: "cuts through", "removes residue", "leaves a clean finish" |
| "lab-tested / proven / clinically" on Table Bussers, AutoWipes, floor, screen, IPA, Handy Jack | nothing — wait for a test to exist |
| "hygienic clean", "sanitary", "kills what's on…" | "clean", "fresh", "removes sweat and body oil" |
| "best / safest / strongest / #1 / ultimate" | substantiated test-specific comparison only |
| "non-toxic", "chemical-free", "harmless", "kid & pet safe" | the exact designation or intended-use wording |
| "food-safe / food-grade / food-contact approved" | "suitable for food service environments" (**scented Table Bussers only**) |
| bare "compostable" | the full cloth sentence: *"The cloth fibers are TÜV certified (OK COMPOST HOME and INDUSTRIAL). This applies to the cloth substrate only, not the finished wipe, formula or packaging."* |
| "100% natural" / "X% natural" | "made with natural ingredients" (code N) |
| benchmark brand names | "traditional quat-based disinfecting wipes" / "traditional citric-acid-based disinfecting wipes" |

Every material list in body copy or instructions carries the patch-test line:
**"If in doubt, test on a small, inconspicuous area first."**

**Never transfer.** A Lavender result is not a Lemongrass result; a fitness-wipe result is
not a Table Bussers result "even though the bucket looks the same".

---

## Special cases that bite

- **"Comparison intent" is not permission to compare performance.** If the brief asks for a
  comparison and the SKU has no `P`, the comparison must be **cost, format, coverage or
  labour** — our prices and third-party operational statistics. Not efficacy.
- **Cost-per-use arithmetic is allowed** (it is arithmetic on our own list prices), but no
  cost figure may sit beside a cleaning-performance claim, a percentage, or the word "safe".
- **Outcome CTAs** ("Reduce Table Turnover Time") are an untested operational claim →
  **MEDIUM finding, needs Dean**. Frame as an objective, never as a measured result:
  ✅ "Reduce Table Turnover Time" / ❌ "Cuts reset time by 30% — proven".
- **Health/illness topics** need the compliance block (house pattern: an "Important Health &
  Product Information" note). Never imply germ-kill on a non-registered product.

---

## The review (Agent 2C) — run on the written draft

Part 1's seven steps, in order:

1. Identify every product named or pictured → resolve to a Part 4 row. No row = escalate.
2. Determine mode (proactive for marketing copy).
3. Pull each product's claim set from Part 4. Never carry a claim across SKUs.
4. Scan controlled terms (Part 3) in **title, meta, H1–H3, table headers, bullet labels,
   captions, alt text, badges, cross-sell blocks** — all in scope, checked before body copy.
5. Check placement and adjacency (Part 7).
6. Check certifications and evidence (Part 6): every badge must be in Part 4 **and** on the
   page. Never state pending/submitted/expected status.
7. Apply the never-say list (6.9) and special-population rules (6.10).

Report by severity: **BLOCKING → HIGH → MEDIUM → LOW**, each with location, exact text,
rule cited (Part, item), and the fix in approved wording. Then a "passed" section, then the
compliance note.

### Compliance note format (Part 9.3)

```yaml
products_named: <canonical names, Part 4>
controlled_terms_used_and_permitting_code:
  - "<phrase>" -> <code>
certifications_asserted: <list, each page-verified on DATE>
comparative_numeric_claims: <sentence used, Part 6 reference> | NONE permitted
unverified_or_escalated: <items + the decision needed>
filter_version: 1.1
```

**Zero BLOCKING findings required. If any BLOCKING appears: stop, do not soften, escalate.**

---

## Live-site conflicts found during the test (send to Dean)

Recording these here so they are not rediscovered:

1. **EWG Verified® asserted where Part 4 grants `E = —`.** Both Table Bussers product pages
   and the EWG landing page name Table Bussers Unscented and Autumn as EWG Verified, while
   Part 4 v1.1 shows a dash on both rows. Part 4 governs the copy, the page gets corrected —
   or a Part 11 amendment grants `E v`. Until then the badge may not be repeated in our copy.
2. **Bare "Sustainable"** in the scented product title, which the row's restriction column
   forbids.
3. Fail-the-Filter language on those same pages: "kid-safe", "no harsh chemicals",
   "the only wipe", "safe for your family and the planet", "superior cleanliness",
   "perfect for food service environments", and an unqualified compostable claim without the
   cloth-substrate disclaimer.

Until corrected, the blog may link to those URLs but must not echo the phrases.

---

## 7. The per-post envelope (template — fill it, don't gesture at it)

Six blocks, in this order. Blocks 1–3 come from Part 4 of the Filter; blocks 4–6 are our judgement
and must be dated.

```
1  Part 4 rows for the SKUs this post may mention   (SKU | codes | source page | date checked)
2  THE ENVELOPE OF THIS POST — the exclusions that apply, applied to every surface of the
   article, not just the body: title · meta title · meta description · H1 · H2 · H3 · table
   headers · bullet labels · image captions · alt text · CTA button text · schema fields
3  What the copy MAY use: Tier 3 qualitative sentences + certifications, in their exact form
4  Adjudication of the tensions the brief creates (see §8)
5  Escalations opened, with the route and the date
6  Part 9.3 note (YAML): filter_version, page_verified, recompute_before_publish
```

## 8. Adjudications that are ours, not the Filter's

These are the calls that keep recurring. Each was decided by the owner or by compliance; none of them
is in the Filter document itself, so they live here with the reason attached.

- **A cost figure is a price unit, not a performance claim.** "Cost per table" may be used even
  when the SKU has no `P` code, because it prices the consumable; it is not a cleaning claim. Use it
  as the differentiator precisely because "cost per wipe" is saturated (16 of 21 posts, see
  `references/08b`).
- **Adjacency guardrail.** A cost or price number must never sit next to a performance claim, a
  percentage, or the word "safe". Cost paragraphs stay cost paragraphs.
- **"suitable for food service environments" is an exact phrase.** Never "perfect for", never
  "food-safe", never "food-grade". `NSF` attaches to the scented family only — it does not travel to
  the unscented sibling.
- **Do not transfer `P` between visually identical SKUs.** Two buckets can look the same and carry
  different codes; the claim belongs to the SKU row, not the bucket.
- **Arithmetic is recomputed, never inherited.** Cost per wipe → cost per table, dated, from live
  prices:

| SKU | Case price | Count | $/wipe | $/table (2 wipes/reset) |
|---|---|---|---|---|
| WX01126TN / WX72024TBB | $36.99 | 400 | ≈$0.092 | ≈$0.18 |
| WX01130TN | $69.99 | 800 | ≈$0.087 | ≈$0.17 |
| WX01126TN-4 | $119.99 | 1,600 | ≈$0.075 | ≈$0.15 |

- **Tier-3-only envelope (a worked model).** For a product outside TURI and EPA — isopropyl alcohol
  is the example — the envelope is: `tier: tier_3_only`,
  `blocked_terms: [disinfecting, sanitizing, germ-kill]`, and an explicit note that the story is the
  IPA use case, **not** a natural/fitness positioning, with a different audience. When a product has
  no test data, the envelope is what stops the copy from drifting into a claim.

## 9. The per-SKU claims report (the shape the reviewer expects)

“What can I say about this product?” is answered in four blocks, always in this order, always with
the filter version and the verification date attached:

```
CAN SAY           <each permitted claim, with the code that permits it>
CANNOT SAY        <each prohibited phrasing and, in one line, why>
RECOMMENDED ANGLE <the honest framing that survives CANNOT SAY>
FILTER VERSION    <vX.Y, page verified YYYY-MM-DD, recompute before publish>
```

Rules for the report: every line is derived from Part 4 for **that** SKU (never from a sibling or a
visually identical bucket); the codes in an old report are assumptions, not evidence, and are
re-derived before reuse; and the `FILTER VERSION` line is dated, because a claim set without a date
cannot be defended later.


