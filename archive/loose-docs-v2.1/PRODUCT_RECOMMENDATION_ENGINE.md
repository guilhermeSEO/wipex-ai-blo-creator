# PRODUCT RECOMMENDATION ENGINE v2 — Trends + Calendar + Intent

**New intelligent product recommendation system:**

Agent 1A now matches trend + calendar + content intent → Perfect Wipex product

---

## THE 3-LAYER DECISION FRAMEWORK

```
LAYER 1: TREND ANALYSIS
  ├─ Google Trends: Rising? Falling? Seasonal?
  ├─ Geographic focus: USA primary vs Brazil
  └─ Momentum: How fast is trend growing?

LAYER 2: CALENDAR + INTENT ALIGNMENT
  ├─ Calendar hook: Q1-Q4 budget/seasonal cycle
  ├─ Blog intent: Buying guide / How-to / Educational
  ├─ CRO goal: E-commerce / Lead gen / Brand awareness
  └─ Decision: Does trend match intent + calendar?

LAYER 3: PRODUCT MATCHING
  ├─ Extract keywords from trend research
  ├─ Cross-reference with Wipex product attributes
  ├─ Score product fit: 1-5
  └─ Recommend TOP 3, you pick one
```

---

## AGENT 1A PRODUCT RECOMMENDATION LOGIC

### When Agent 1A analyzes your blog topic, it runs this logic:

```yaml
INPUT:
  topic: "Summer cleaning for yoga studios"
  calendar_hook: "Q2"
  blog_intent: "buying_guide"
  cro_goal: "e_commerce"
  target_market: "US"

STEP 1: GOOGLE TRENDS RESEARCH
  ├─ Keyword variants found: "plant-based yoga mat wipes" ↑ +26%
  ├─ Geographic: USA primary (58/100), Brazil secondary (35/100)
  ├─ Trend attributes: "plant-based", "eco", "sustainable"
  └─ Commercial intent: HIGH (buying guide + rising search)

STEP 2: EXTRACT PRODUCT SIGNALS FROM TREND
  Keyword signals in trend data:
  • "plant-based" → Natural product positioning
  • "eco-friendly" → Sustainability angle
  • "yoga studios" → B2B bulk buyers
  • "summer" → Q2 seasonal peak
  • "cleaning" (not disinfecting) → Tier 3 claims OK

STEP 3: SEARCH WIPEX PRODUCT CATALOG (via Shopify API)
  Query: Find products matching [plant-based + eco + yoga + bulk]
  
  Results:
  ├─ Natural Gym Wipes Buckets (2,000ct)
  │  ├─ Attributes: ✅ Plant-based, ✅ Eco, ✅ Bulk, ✅ Tier 2 (TURI)
  │  └─ Fit score: 4.8/5 (EXCELLENT)
  │
  ├─ EMPOWER Hot Yoga Mat Wipes (25ct canister)
  │  ├─ Attributes: ✅ Premium, ✅ Yoga-specific, ✅ Eco packaging
  │  └─ Fit score: 4.2/5 (VERY GOOD - upsell tier)
  │
  ├─ Sustainable Gym Wipes Rolls
  │  ├─ Attributes: ✅ Eco, ✅ Bulk, ⚠️ Generic (not yoga-focused)
  │  └─ Fit score: 3.5/5 (OK - secondary)
  │
  ├─ Handy Jack Disinfecting Wipes
  │  ├─ Attributes: ✅ Bulk, ❌ EPA (overkill for yoga studios), ❌ Not eco
  │  └─ Fit score: 1.2/5 (WRONG - don't recommend)

STEP 4: VALIDATE PRODUCT FIT vs CLAIMS MATRIX
  Selected product: Natural Gym Wipes Buckets
  
  Claim codes (Part 4): N, S3, C, Eco
  ├─ N (natural-ingredients) → Can say "plant-based" ✅
  ├─ S3 (skin-safe) → Can say "hypoallergenic" ✅
  ├─ C (compostable cloth) → Can say "eco-friendly" ✅
  ├─ Eco → Can use sustainability messaging ✅
  
  No EPA claims: ✅ Correct (yoga mat cleaning, not disinfecting)

STEP 5: VALIDATE CALENDAR + INTENT
  Calendar: Q2 (Apr-Jun) = summer fitness season ✅
  Trend: ↑ +26% (rising NOW) ✅
  Blog intent: Buying guide (commercial) ✅
  CRO: E-commerce (buying wipes online) ✅
  
  All aligned? YES ✅
  
STEP 6: RANK TOP 3 RECOMMENDATIONS
  
  🥇 PRIMARY: Natural Gym Wipes Buckets
     Reason: Matches trend (plant-based) + calendar (Q2 bulk) + intent (buying guide)
     Expected conversion: 12-18%
     Product page: https://wipex.co/products/natural-gym-wipes-buckets
  
  🥈 SECONDARY: EMPOWER Hot Yoga Mat Wipes
     Reason: Premium upsell, yoga-specific positioning, eco packaging
     Expected conversion: 5-8% (smaller audience, higher price)
     Product page: https://wipex.co/products/empower-yoga-mat-wipes
  
  🥉 TERTIARY: Sustainable Gym Wipes Rolls
     Reason: Eco-angle backup, but less yoga-specific
     Expected conversion: 3-5% (generic)
     Product page: https://wipex.co/products/sustainable-gym-wipes

STEP 7: OUTPUT TO USER
  
  PRODUCT RECOMMENDATIONS:
  
  ✅ PRIMARY (100% recommended): Natural Gym Wipes Buckets
     Why: Plant-based + bulk + Q2 seasonal + buying intent
     Product page: [URL]
     Blog positioning: "Plant-Based Yoga Mat Wipes for Studios"
  
  🔄 SECONDARY (upsell option): EMPOWER Hot Yoga Mat Wipes
     Why: Premium tier, yoga-specific, ecosystem play
  
  💡 TERTIARY (backup): Sustainable Gym Wipes Rolls
     Why: Generic eco angle if primary unavailable
  
  Your choice: [Radio button: PRIMARY / SECONDARY / BOTH / CUSTOM]
```

---

## REAL PRODUCT MATCHING EXAMPLES

### Example 1: Q1 Procurement Cycle (B2B Budget Planning)

```
INPUT:
  Topic: "Cost-effective office cleaning supplies"
  Calendar: Q1 (budget planning)
  Intent: buying_guide
  CRO: lead_gen (contact sales)
  Market: US

GOOGLE TRENDS:
  Keyword: "bulk disinfecting wipes office" ↑ +15% (seasonal Q1)
  Trend signals: "bulk", "office", "disinfecting", "cost-effective"
  
PRODUCT MATCHING:
  ✅ EPA-Registered Disinfecting Wipes Roll (WX71989SDR)
     Reason: Trend says "disinfecting" + "bulk" + "office"
     Claim code: D (EPA disinfectant)
     Fit score: 4.6/5
  
  ⚠️ Natural Gym Wipes Buckets
     Reason: Bulk OK, but "natural" ≠ "disinfecting" intent
     Claim code: N (natural, no EPA)
     Fit score: 2.1/5 (WRONG)
  
  ❌ Table Bussers Surface Wipes
     Reason: Too small scale for "bulk office"
     Fit score: 1.0/5 (AVOID)

OUTPUT:
  PRIMARY: EPA-Registered Disinfecting Wipes Roll
  Blog angle: "Industrial-Grade Disinfection on a Budget"
  CTA: "Request a Facilities Demo"
```

### Example 2: Evergreen Education (Long-Tail, No Season)

```
INPUT:
  Topic: "Electronics cleaning: IPA vs disinfectant"
  Calendar: Evergreen (no seasonal hook)
  Intent: educational / comparison
  CRO: brand_awareness
  Market: US + BR

GOOGLE TRENDS:
  Keyword: "isopropyl alcohol vs disinfectant wipes" → stable 32/100
  Trend signals: "IPA", "comparison", "electronics", "cleaning" (not sanitizing)
  
PRODUCT MATCHING:
  ✅ Isopropyl Alcohol Wipes 70% (1000ct bucket)
     Reason: IPA angle, tech use, no seasonal need
     Claim code: — (no claims, cleaning only)
     Fit score: 4.8/5
  
  ✅ EPA-Registered Disinfecting Wipes Roll
     Reason: Comparison angle ("vs"), shows difference
     Claim code: D (EPA disinfectant)
     Fit score: 3.5/5 (secondary, for comparison)
  
  ❌ Gym Wipes
     Reason: Electronics ≠ fitness use case
     Fit score: 0.5/5 (AVOID)

OUTPUT:
  PRIMARY: IPA Wipes 1000ct (educational, comparison angle)
  SECONDARY: EPA Roll (to show difference)
  Blog angle: "Why IPA Wipes Are Better for Electronics Than Disinfectants"
  CTA: "Shop Electronics-Grade IPA Wipes"
```

### Example 3: Trend-Following (Micro-Moment Opportunity)

```
INPUT:
  Topic: "Back-to-school cleaning for classrooms"
  Calendar: Q3 (Aug-Sep, back-to-school peak)
  Intent: buying_guide (teachers + admin buying)
  CRO: e_commerce
  Market: US

GOOGLE TRENDS:
  Keyword: "eco-friendly classroom cleaning supplies" ↑ +42% (RISING FAST!)
  Peak: Aug-Sep (back-to-school)
  Trend signals: "eco", "classroom", "school", "sustainable"
  
PRODUCT MATCHING:
  ✅ Natural Gym Wipes Buckets (claim code: N, S3, Eco)
     Why: Eco angle, schools buying bulk, sustainable cloth
     Fit score: 4.7/5
  
  ✅ Sustainable Gym Wipes Rolls (claim code: Eco)
     Why: Eco-focused, individual rolls for classrooms
     Fit score: 4.2/5
  
  ⚠️ Wipex Yoga Mat Wipes
     Why: Yoga ≠ classroom, wrong audience
     Fit score: 1.5/5 (AVOID)

OUTPUT:
  PRIMARY: Natural Gym Wipes Buckets
  SECONDARY: Sustainable Gym Wipes Rolls
  Blog angle: "Eco-Friendly Back-to-School Cleaning (Safe for Kids)"
  CTA: "Order Your School's Eco-Wipes Kit"
  Urgency: HIGH (trend peak in 2 weeks, publish ASAP)
```

---

## THE RECOMMENDATION MATRIX

**Agent 1A uses this matrix to decide product ranking:**

| Trend Signal | Claim Code Match | Calendar Alignment | Blog Intent | Product Fit Score |
|--------------|-------------------|-------------------|-------------|-------------------|
| "plant-based" | N ✅ | Q2 summer ✅ | buying_guide ✅ | 4.8/5 |
| "disinfecting" | D ✅ | Q1 budget ✅ | buying_guide ✅ | 4.6/5 |
| "eco-friendly" | Eco ✅ | Q3 back-to-school ✅ | buying_guide ✅ | 4.7/5 |
| "IPA" | — (cleaning) ✅ | Evergreen ✅ | educational ✅ | 4.8/5 |
| "premium" | P ✅ | Q2/Q4 ✅ | buying_guide ✅ | 4.2/5 |
| "antibacterial skin" | G ✅ | Any ✅ | how_to ✅ | 3.5/5 |
| "generic wipes" | ❌ | Any | Any | <2.0/5 |

---

## HOW THIS CONNECTS TO YOUR WORKFLOW

### Your Input Form (Updated)

```yaml
BLOG GENERATION INPUT

# Basic info (you provide)
topic: "Summer cleaning for yoga studios"
calendar_hook: "Q2"
blog_intent: "buying_guide"
cro_goal: "e_commerce"
target_market: "US"

# Agent 1A produces (automatically)
recommended_keyword: "plant-based yoga mat wipes for studios"
google_trends_data:
  trend_direction: "↑ +26%"
  peak_timing: "May-Jun"
  search_volume: "400-600/mo"

recommended_products:
  primary:
    product_id: "WX71960NATURAL"
    name: "Natural Gym Wipes Buckets"
    reason: "Plant-based (trend match) + bulk (calendar) + commercial (intent)"
    fit_score: 4.8/5
  secondary:
    product_id: "WX00089EMPOWER"
    name: "EMPOWER Hot Yoga Mat Wipes"
    reason: "Premium upsell, yoga-specific"
    fit_score: 4.2/5

# Your decision
your_choice: "PRIMARY"  # or SECONDARY, or BOTH, or CUSTOM

# Blog continues with your choice
```

---

## WHAT YOU APPROVE IN 30 SECONDS

When Agent 1A finishes, you see:

```
📊 PRODUCT RECOMMENDATION

🥇 PRIMARY CHOICE: Natural Gym Wipes Buckets
   Trend match: ✅ "plant-based" signal
   Calendar: ✅ Q2 (May-Jun peak)
   Blog angle: "Plant-Based Yoga Mat Wipes for Studios"
   Expected CTR: +18-25%
   [✅ ACCEPT] [🔄 SHOW ALTERNATIVES] [❌ CUSTOM CHOICE]

🥈 SECONDARY: EMPOWER Hot Yoga Mat Wipes
   (Optional upsell in blog)
   
💡 Search volume: 400-600/month
💡 Competition: LOW (niche keyword)
💡 Expected ranking: 60 days (good authority signals)
```

**You click "ACCEPT" → Blog continues with chosen product**

**Total decision time: 20 seconds**

---

## BENEFITS OF THIS SYSTEM

✅ **Trend-aligned products** (not guessing)
✅ **Calendar-optimized timing** (publish when search volume peaks)
✅ **Intent-matched messaging** (buying guide = commercial product)
✅ **Compliance pre-validated** (claim codes already checked)
✅ **Faster decision** (Agent 1A does research, you just approve)
✅ **Higher conversion** (product matches exactly what people search for)

---

## NEXT: This output flows directly to Agent 1B

Agent 1B (Claims Validation) receives:
- Chosen product (e.g., Natural Gym Wipes Buckets)
- Product claim codes (N, S3, C, Eco)
- Blog intent (buying_guide)
- Calendar hook (Q2)

Then Agent 1B validates:
- What claims are allowed?
- What never-say terms apply?
- What Tier 2 evidence is needed?

**Result: Blog copy will be 100% compliant from day 1**
