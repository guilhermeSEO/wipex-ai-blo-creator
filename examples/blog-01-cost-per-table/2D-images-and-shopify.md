# 2D — IMAGE BRIEFS, INTERACTIVE SECTION, SHOPIFY PACKAGE
### Blog #1 · "How to Calculate Cost Per Table for a Restaurant"

---

## 1. IMAGE BRIEFS (6)

| # | Section / context | Subject | Mood | Dimensions | Overlay | Source | Alt text |
|---|---|---|---|---|---|---|---|
| 1 | Hero, above the H1 | A busser wiping a four-top in a busy dining room between covers, pre-mixed wipe bucket at the station, no guests in frame | operational, warm, in-service | 1200×800 | none | product photography + location shoot | Busser wiping a four-top table in a busy dining room between covers, premixed wipe bucket at the service station |
| 2 | After the quick-answer bullets (stat card row) | Overhead: service station with an open 400-count bucket, gloved hand lifting one wipe | clean, clinical, close | 1200×800 | none | studio product | Open 400-count table wipe bucket on a restaurant service station, a hand lifting one wipe from the stack |
| 3 | H2 "The four-step reset" | Four-panel sequence: clear, one-pass wipe, reset settings, host seated | process, documentary | 600×400 each | "Clear · Clean · Reset · Seat" | location shoot | Four-panel sequence of a table reset: clearing plates, wiping the top, setting the table, seating guests |
| 4 | H2 cost block | Clipboard worksheet with two columns filled: consumable cents and labour minutes per reset | practical, editorial | 600×400 | none | design brief (custom graphic) | Cost per table worksheet on a clipboard showing consumable cost per wipe and labour minutes added per table reset |
| 5 | H2 "Which Table Bussers fits your room" | Two buckets side by side on a bar top: cinnamon-clove scented and fragrance-free unscented | product comparison | 600×400 | "Scented · Unscented" | studio product | Two table busser buckets side by side on a bar top: cinnamon and clove scented, and fragrance-free unscented |
| 6 | H2 self-assessment | Manager and busser over a printed checklist at the pass before service, stopwatch on the counter | teamwork, real | 600×400 | none | location shoot | Restaurant manager and busser reviewing a printed front-of-house reset checklist at the pass before service |

**Alt-text rules applied:** describe what is visible; name the product or the action, never a
claim; no "safe", no superlative, no "best". Alt text was included in the 2C scan.

---

## 2. INTERACTIVE SECTION — cost-per-table calculator

| Field | Content |
|---|---|
| Type | Calculator |
| User input | tables · turns per service · services per week · case price · wipes per case · wipes per reset · seconds per reset · loaded hourly rate |
| Output | cost per wipe · cost per table (consumable) · cost per table (with labour) · weekly cleaning cost · cost per cover |
| Benefit | converts the article from an argument into the reader's own number |
| Implementation | custom Liquid section (below), no app |
| **Compliance guard** | the calculator may compute **cost, coverage and consumption only.** It must not output a cleaning-performance comparison, a time-saving promise, or a "safe" verdict. |

---

## 3. SHOPIFY LIQUID SECTION

```liquid
{%- comment -%}
  Wipex blog module: Cost Per Table calculator.
  Computes COST ONLY (consumable, labour, per-cover). No performance or time-saving output.
{%- endcomment -%}
<div class="wipex-module wipex-module--cpt" id="cpt-{{ section.id }}">
  <h2 class="wipex-module__title">{{ section.settings.title | escape }}</h2>
  <div class="wipex-module__grid">
    {%- assign fields = "tables,turns,services,price,count,wipes,seconds,rate" | split: "," -%}
    {%- assign labels = "Tables,Turns per service,Services per week,Case price ($),Wipes per case,Wipes per reset,Seconds per reset,Loaded hourly rate ($)" | split: "," -%}
    {%- assign defaults = "20,3,6,36.99,400,2,45,16" | split: "," -%}
    {%- for f in fields -%}
      <label class="wipex-module__field">
        <span>{{ labels[forloop.index0] }}</span>
        <input type="number" step="any" id="cpt-{{ f }}" value="{{ defaults[forloop.index0] }}"
               inputmode="decimal" aria-label="{{ labels[forloop.index0] | escape }}">
      </label>
    {%- endfor -%}
  </div>
  <div class="wipex-module__out" role="status" aria-live="polite">
    <span class="wipex-module__value" id="cpt-out-table">—</span>
    <span class="wipex-module__label">cost per table (consumable + labour)</span>
    <span class="wipex-module__value" id="cpt-out-week">—</span>
    <span class="wipex-module__label">weekly cleaning cost</span>
    <span class="wipex-module__value" id="cpt-out-cover">—</span>
    <span class="wipex-module__label">cost per cover</span>
  </div>
  <p class="wipex-module__note">
    Prices are {{ section.settings.price_note | escape }}. Cost figures only.
  </p>
</div>

<script>
(function () {
  var ids = ['tables','turns','services','price','count','wipes','seconds','rate'];
  var el = function (n) { return document.getElementById(n); };
  var num = function (id) { var v = parseFloat((el('cpt-' + id) || {}).value); return isNaN(v) ? 0 : v; };
  var money = function (v) { return '$' + v.toFixed(v < 1 ? 4 : 2); };
  function calc() {
    var resets = num('tables') * num('turns') * num('services');
    var perWipe = num('count') ? num('price') / num('count') : 0;
    var consumable = perWipe * num('wipes');
    var labour = num('seconds') / 3600 * num('rate');
    var perTable = consumable + labour;
    var week = perTable * resets;
    var cover = resets ? week / (resets * 2) : 0;   /* assumes 2 covers per turn by default */
    el('cpt-out-table').textContent = money(perTable);
    el('cpt-out-week').textContent = '$' + week.toFixed(2);
    el('cpt-out-cover').textContent = money(cover);
  }
  ids.forEach(function (id) {
    var i = el('cpt-' + id);
    if (i) { i.addEventListener('input', calc); }
  });
  calc();
})();
</script>

{% schema %}
{
  "name": "Cost Per Table calculator",
  "settings": [
    { "type": "text", "id": "title", "label": "Title", "default": "Calculate your cost per table" },
    { "type": "text", "id": "price_note", "label": "Price note", "default": "the current published case rate — check your invoice" }
  ],
  "presets": [{ "name": "Cost Per Table calculator" }]
}
{% endschema %}
```

**Where it goes:** immediately after the H2 "How to calculate your own cost per table", before the
worked example, so the reader can run their own numbers against the article's.

---

## 4. SHOPIFY PASTE PACKAGE

Deliver in this order. The clean body is `2D-body-clean.md` (3,389 words, markers stripped,
12 links).

```
1  TITLE
   How to Calculate Cost Per Table for a Restaurant (and Cut It Without Cutting Standards)

2  SLUG
   cost-per-table-restaurant

3  META TITLE  (65 chars, counted)
   Cost Per Table for Restaurants: Cut Cost, Not the Standard, in Q4

4  META DESCRIPTION  (155 chars, counted)
   Cost per table, not per wipe. Calculate your restaurant reset cost, add the labour minute,
   and cut Q4 spend without lowering standards. Read the guide now.

5  BODY
   paste 2D-body-clean.md into the Shopify blog editor (markdown/HTML block)

6  TOC
   the "On this page" list is already in the body; wire the anchors if the theme supports it

7  SCHEMA
   paste the JSON-LD from 2B §2 into the theme's custom-code slot or the SEO app.
   Fill <HERO_URL> with image 1's CDN URL and expand the truncated FAQ answer texts.

8  LIQUID
   add the section in §3 to the blog post template, above the FAQ

9  CHECKLIST  see §5
```

---

## 5. OPERATOR CHECKLIST (what is still manual)

- [ ] paste the body, set the title and the slug
- [ ] set the meta title and meta description, then **re-count the characters after pasting** (the
      CMS sometimes trims trailing spaces)
- [ ] upload the 6 images with the alt text supplied, in section order
- [ ] add the JSON-LD, expanding the FAQ answer placeholders with the real FAQ text
- [ ] add the Liquid section and preview it on mobile — check the number inputs and the output
- [ ] verify the 12 internal links resolve (5 product, 5 blog, 2 collection)
- [ ] **add the reciprocal link on the 2026-08-31 post** pointing back to this one
- [ ] confirm the Autumn bucket is in stock and the price in the copy still matches
- [ ] publish on the target date (**2026-11-08**, the Nov 1–20 window), not before
- [ ] submit for indexing
- [ ] log the post in `04-data/published_ledger.md` for the 30/60/90-day retro