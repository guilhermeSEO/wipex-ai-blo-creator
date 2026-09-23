# Wipex Blog Generation Skill v2.0 — COMPLETE INPUT MATRIX
**All Required Inputs + Decision Options for AI-Powered Blog Generation**

---

## PART 1: MANDATORY INPUTS (User Must Provide)

### 1.1 Blog Metadata & Calendar Hook

| Input | Type | Options | Default | Example |
|-------|------|---------|---------|---------|
| **Blog Topic / Title** | Text | Freeform | None | "Yoga Mat Care Guide for Studios" |
| **Target Keyword** | Text | SEO keyword (primary) | None | "yoga mat cleaner wipes" |
| **LSI Keywords (secondary)** | List | 3-5 long-tail variants | Auto-discover | ["gym mat cleaning", "sustainable mat care", "studio supplies"] |
| **Search Intent** | Select | I (info) \| C (commercial) \| T (transact) | Auto-detect | "I" (user wants info) |
| **Calendar Hook** | Select | □ None □ Seasonal □ Event □ Trend | None | "Q2 Summer Fitness Season (Apr-Jun)" |
| **Target Market** | Select | □ USA only (USA) | USA | "USA" |
| **CRO Goal** | Select | □ E-commerce □ Lead-gen □ Brand awareness □ Contact | E-commerce | "E-commerce (add to cart)" |
| **Blog Type** | Select | □ Buying Guide □ How-To □ Educational □ Case Study □ Comparison | Buying Guide | "Buying Guide" |
| **Publishing Timeline** | Date | YYYY-MM-DD | Today +7 | "2026-10-15" |

---

### 1.2 Product Selection (AI Auto-Recommends, You Choose)

**The Skill will:**
1. Analyze the topic + calendar hook + intent
2. Fetch current Wipex products from `https://wipex.co/products.json`
3. Cross-reference with Claims Matrix (Dean's file) to suggest perfect fit
4. Present you with TOP 3 recommended products

**You choose: Accept recommendation OR override**

#### **If you PROVIDE product names:**

| Input | Type | Constraint | Example |
|-------|------|-----------|---------|
| **Primary Product (exact name)** | Select from Wipex catalog | Must exist in inventory + have active claims | "Natural Gym Wipes Buckets (plant-based, lavender)" |
| **Secondary Products (optional, up to 2)** | Select from Wipex catalog | Different formulation or SKU | "EMPOWER Hot Yoga Mat Wipes 25ct" |
| **Tertiary Products (optional)** | Select from Wipex catalog | Cross-sell or educational context | "Handy Jack Heavy Duty Wipes" |

#### **If you DON'T provide (RECOMMENDED):**

The Skill will **automatically** search the catalog based on:

```
Topic: "Yoga Mat Care Guide"
Calendar Hook: "Q2 Summer Fitness"
CRO Goal: "E-commerce"
  ↓ (Skill logic)
Best Fit Product: "Natural Gym Wipes Buckets (plant-based, lavender)"
  Reason: "Q2 spike for fitness studios, natural positioning for eco-conscious yoga communities"
  
Second Option: "EMPOWER Hot Yoga Mat Wipes 25ct"
  Reason: "Premium tier, premium audience positioning, newer product = promotional angle"
  
Third Option: "Table Bussers Surface Wipes"
  Reason: "Cross-sell for studio equipment cleaning, diversify product range"
```

---

### 1.3 Claims & Compliance Rules (AI Auto-Pulls, You Review)

**The Skill will:**
1. Load `Claims & Guidelines.xlsx` (the file you provided)
2. Extract all APPROVED claims for your product(s)
3. Filter by Tier (Regulated / Substantiated / Qualitative)
4. Present options; you review

#### **Claim Tier Options (Auto-Selected):**

| Tier | When Applicable | Example Claims | Your Decision |
|------|-----------------|---------------|----|
| **Tier 1: Regulated** | EPA roll only | "Disinfects surfaces", "kills 99.9% germs" | ☐ Include |
| **Tier 2: Substantiated** | Fitness products with TURI tests | "Removes 90% synthetic sweat" (147% more than quat-based) | ☐ Include |
| **Tier 3: Qualitative** | All non-EPA surface products | "Gentle on yoga mats", "designed for sensitive skin" | ☐ Include (default: YES) |

#### **Never-Say List (Auto-Enforced by Skill):**

```
The skill WILL NOT allow these (hardcoded block):
- "biodegradable" (whole product)
- "100% natural" or "all natural"
- "safe for all surfaces"
- "best", "safest", "strongest" (absolute claims)
- "kills all germs" (use "99.9%" only)
- "BZK products for surface cleaning" (skin/hand only)
```

---

### 1.4 SEO & CRO Positioning (AI Auto-Proposes, You Refine)

| Input | Type | Skill's Auto-Proposal | Your Override |
|-------|------|----------------------|-----------------|
| **Meta Title (65 chars exact)** | Text | "Yoga Mat Care: Plant-Based Wipes for Eco-Studios" | ☐ Accept ☐ Edit |
| **Meta Description (155 chars exact)** | Text | "Learn studio yoga mat cleaning best practices. Discover why plant-based wipes outperform traditional methods by 147%. Plant-based, dermatologically tested." | ☐ Accept ☐ Edit |
| **URL Slug** | Auto-generated | "yoga-mat-care-guide-eco-studios" | ☐ Accept ☐ Edit |
| **Primary CTA** | Select | □ "Add to Cart" □ "Download Guide" □ "Contact Sales" □ "Email Signup" | E-commerce default: "Add to Cart" |
| **CTA Copy (result-focused)** | Text | "Get Plant-Based Wipes for Your Studio" | ☐ Accept ☐ Edit |
| **Internal Link Strategy** | Auto-mapped | Links to: Product page, Related blog, FAQ, Category | ☐ Accept ☐ Customize |

---

### 1.5 Content Audience & Persona (AI Auto-Segments, You Confirm)

**Skill detects from calendar hook + topic:**

| Audience Segment | Buying Pattern | Pain Points | Skill Maps To | You Confirm? |
|------------------|-----------------|------------|---------------|-------------|
| **Fitness Studios** | B2B bulk purchase, Q2 spike | Supply chain cost, compliance | "Buy bundles, emphasize ROI" | ☐ Yes ☐ No, different |
| **Yoga Instructors** | Individual purchase, eco-conscious | Sustainability guilt, premium price | "Emphasize plant-based, certifications" | ☐ Yes ☐ No, different |
| **Office Managers** | Q1 budget cycle, bulk subscription | Employee wellness, compliance | "Highlight skin-safety, bulk discount" | ☐ Yes ☐ No, different |
| **Facilities Managers** | Procurement-driven, cost-first | Inventory management, supplier trust | "Lead with TURI data, performance metrics" | ☐ Yes ☐ No, different |

**You can override:** Specify audience if you know better than skill's auto-detect.

---

## PART 2: OPTIONAL INPUTS (Skill Can Auto-Discover)

### 2.1 Internal Link Map (Auto-Built, You Verify)

**Skill will:**
1. Fetch Wipex product URLs from `https://wipex.co/products.json`
2. Fetch blog archive (if exists)
3. Suggest 2-3 relevant internal links per 500 words

**Example auto-suggestion:**

```
Topic: "Yoga Mat Care Guide"
  ↓
Suggested links:
  - "Natural Gym Wipes Buckets" (product page)
  - "Fitness Studio Cleaning Best Practices" (related blog)
  - "Sustainable Business Supplies" (category page)
```

**You can:** ☐ Accept ☐ Override ☐ Add more links

---

### 2.2 Image Briefs (Auto-Suggested, You Refine)

**Skill will propose:**

| Placement | Subject | Mood | Dimensions | Your Choice |
|-----------|---------|------|-----------|-------------|
| Hero | Yoga mat + wipes product shot | Professional + approachable | 1200x800px | ☐ Accept ☐ Swap for stock photo |
| Body (Section 1) | Hands cleaning yoga mat | Action-oriented | 600x400px | ☐ Accept ☐ Custom brief |
| Body (Section 2) | Product lineup comparison | Clean, minimal | 600x400px | ☐ Accept ☐ Custom brief |
| Testimonial callout | Yoga instructor testimonial graphic | Lifestyle | 400x300px | ☐ Accept ☐ Custom brief |

---

### 2.3 Interactive Section (Auto-Proposed, You Enable/Disable)

**Skill will suggest:**

```
Type: "Quick Checklist"
User Input: "Studio size (small/medium/large)"
Output: "Recommended product + quantity + cost estimate"
Benefit: "Helps readers right-size their purchase"
```

**You choose:** ☐ Include ☐ Skip

---

## PART 3: PRODUCT RECOMMENDATION ENGINE (How Skill Chooses)

**When you DON'T specify a product, the skill runs this logic:**

```
Step 1: Extract calendar hook (Q1, Q2, Q3, Q4)
  Topic: "Yoga Mat Care"
  Hook: "Q2 Summer Fitness Season"
  Spike: 12,100 searches/mo (from reference table)

Step 2: Match to Wipex product families
  Natural Gym Wipes (Fitness)? → YES (perfect for Q2 spike)
  EMPOWER Yoga Mat Wipes? → YES (premium, new product)
  Plant-Based Bulk Rolls? → YES (eco-angle for studios)
  
Step 3: Cross-ref Claims Matrix
  Natural Gym Wipes → "Hypoallergenic", "Dermatologically tested", "TURI tested (147% vs quat-based)"
  EMPOWER → Same + "Premium positioning"
  Plant-Based → Same + "Eco-friendly" + "TÜV-certified cloth"

Step 4: Rank by business intent
  🥇 PRIMARY: Natural Gym Wipes Buckets (highest volume, proven TURI data)
  🥈 SECONDARY: EMPOWER (premium upsell, newer product)
  🥉 TERTIARY: Table Bussers (cross-sell for equipment managers)

Step 5: Present to you
  "Based on Q2 Summer Fitness spike + Yoga Mat Care topic,
   I recommend Natural Gym Wipes Buckets as primary product.
   Accept? Or override?"
```

---

## PART 4: FINAL INPUT CHECKLIST (Before Blog Generation Starts)

```
□ Blog Topic / Keyword (or: "Auto-recommend")
□ Calendar Hook (Q1/Q2/Q3/Q4 or specific date)
□ CRO Goal (E-commerce / Lead-gen / Brand awareness / Contact)
□ Blog Type (Buying Guide / How-To / Educational / Comparison)
□ Product(s) (Specify by name OR "Auto-recommend")
□ Audience (Fitness studios / Yoga instructors / Office / Facilities OR "Auto-detect")
□ Meta Title (or: "Auto-generate")
□ Meta Description (or: "Auto-generate")
□ Primary CTA (Add to Cart / Download / Contact OR "Auto-select")
□ Internal Links (Accept auto-map OR customize)
□ Images (Accept auto-briefs OR customize)
□ Interactive Section (Include / Skip)
```

**Ready to Generate?** 
- ☑️ All checked → YES, generate blog
- ❌ Some unchecked → NO, skill asks clarifying questions

---

## PART 5: WHAT SKILL WILL DO WITH THESE INPUTS

### Phase 0: Pre-Generation (Automated)
1. ✅ Load Claims Matrix (from Dean's file)
2. ✅ Fetch live product data from Shopify API
3. ✅ Auto-recommend products (if you didn't specify)
4. ✅ Build internal link map
5. ✅ Generate SEO title + meta + slug (if you didn't provide)
6. ✅ Extract approved claims for selected products
7. ✅ Build audience persona
8. ✅ Map calendar trends (search volume, seasonality, intent)

### Phase 1: Research (8–12 hrs, agents in parallel)
- **Agent 1A:** Keyword research + competitor analysis
- **Agent 1B:** Claims pre-flight + compliance matrix
- **Agent 1C:** Audience + FAQ mining

### Phase 2: Production (12–16 hrs, agents in series)
- **Agent 2A:** Blog copy (hero + body + CTA) using approved claims ONLY
- **Agent 2B:** SEO optimization (title 65 chars, meta 155 chars, schema, readability)
- **Agent 2C:** Compliance validation (Claims Filter v1.1, zero BLOCKING)
- **Agent 2D:** Image briefs + Shopify section template

### Phase 3: Delivery
- ✅ **Blog Copy:** Markdown, HTML-ready for Shopify
- ✅ **SEO Spec:** Title, meta, URL, schema.json, internal links, readability score
- ✅ **Compliance Report:** Zero BLOCKING findings, all claims verified
- ✅ **Image Briefs:** 4–6 images with subject, mood, dimensions, alt text
- ✅ **Shopify Section:** Liquid template ready to drop into blog post template

---

## PART 6: LLM-FRIENDLY FORMATTING (For AI Visibility)

**The skill will ensure all copy:**
- ✅ Uses active voice ("You'll clean better" not "Better cleaning happens")
- ✅ Includes numbers/specifics ("147% more sweat removal" not "much better")
- ✅ Addresses reader pain directly ("Studio owners spend $3,000/year on cleaning wipes" vs. generic intro)
- ✅ Uses conversational tone (sounds like person, not bot)
- ✅ Includes semantic entities (product names, benefit keywords, verified claims)
- ✅ Optimized for LLM indexing (structured data, JSON-LD schema, clean HTML)

**To rank well for LLMs:**
- Natural mention of product benefits (not forced keyword stuffing)
- Real pain points → Wipex solution bridges
- Social proof (TURI test, TÜV certifications) embedded early
- Clear CTA (LLMs reward directness: "Add to Cart" vs. vague "Learn More")

---

## PART 7: EXAMPLE FILLED FORM (What You'll Actually Submit)

```
# Blog Input Form — Submitted by User

Blog Topic: "Eco-Friendly Gym Cleaning: Why Studios Are Switching to Plant-Based Wipes"
Target Keyword: yoga mat cleaner wipes
LSI Keywords: [auto-generate]
Calendar Hook: Q2 (Apr-Jun summer fitness season)
CRO Goal: E-commerce (Add to Cart)
Blog Type: Buying Guide
Publishing Timeline: 2026-10-15

Products:
  □ Auto-recommend (I trust AI)
  ☑ Manual:
    Primary: Natural Gym Wipes Buckets (plant-based, lavender)
    Secondary: EMPOWER Hot Yoga Mat Wipes 25ct

Audience:
  ☑ Auto-detect (Calendar + topic suggests fitness studios)
  Confirmed personas: Yoga studio owners, boutique fitness brands, equipment managers

SEO & CRO:
  Meta Title: [AUTO-GENERATE] → Output: "Yoga Mat Wipes: Plant-Based Cleaning for Studios (147% Better)"
  Meta Description: [AUTO-GENERATE] → Output: "Studio gym cleaning guide. Discover plant-based yoga mat wipes that remove 147% more sweat than traditional quat-based wipes. TÜV-certified, eco-friendly."
  URL Slug: [AUTO-GENERATE] → Output: "yoga-mat-wipes-plant-based-eco-studios"
  Primary CTA: Add to Cart ("Shop Plant-Based Yoga Mat Wipes")

Internal Links:
  [AUTO-MAP] → Suggested:
    - Natural Gym Wipes Buckets (product page)
    - Sustainable Business Supplies (category)
    - Gym Equipment Care Best Practices (related blog)
  ☑ Accept

Images:
  [AUTO-BRIEF] → 4 suggested images
  ☑ Accept

Interactive Section:
  [AUTO-PROPOSE] → "Studio Size Calculator" (determine wipe quantity + cost)
  ☑ Include

Claims Tier:
  ☑ Include all (Tier 1 regulated, Tier 2 TURI, Tier 3 qualitative)
  Never-say list: [AUTO-ENFORCED]

Ready? ☑ YES → Generate Blog
```

---

## NEXT STEPS

**Guilherme, you now have:**
1. ✅ Complete input matrix (what skill needs)
2. ✅ Decision options (what you can choose or auto)
3. ✅ Product recommendation logic (how skill suggests products)
4. ✅ Example filled form (what submission looks like)

**Ready to:**
- 🚀 Rebuild the skill with this v2.0 logic?
- 📝 Test with a real blog topic (example: Q2 "Yoga Studio Cleaning")?
- 🔄 Or review/refine the inputs first?

**Which option?**
