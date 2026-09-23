# GOOGLE TRENDS INTEGRATION — Agent 1A Enhanced

**When Agent 1A runs, it now:**
1. Researches keyword in Google Trends (Brazil + USA, last 4 weeks + 1 week)
2. Cross-references trending topics with calendar hook + blog intent
3. Validates search volume + trend direction
4. Scores keyword for LLM visibility + niche positioning
5. Recommends product based on trend match + calendar

---

## AGENT 1A: ENHANCED KEYWORD & TREND RESEARCH

### Input (From You)

```yaml
target_keyword: "yoga mat cleaner wipes"
calendar_hook: "Q2"  # Apr-Jun summer fitness season
blog_intent: "buying_guide"  # not just informational — SALES angle
target_market: "US"  # OR "BR" (Brazil)
```

### Agent 1A Workflow (Now with Trends)

```
┌─────────────────────────────────────────────────────────┐
│ STEP 1: QUERY EXPANSION                                  │
├─────────────────────────────────────────────────────────┤
│ Primary KW: "yoga mat cleaner wipes"                     │
│ LSI variants (semantic):                                 │
│  • eco-friendly yoga mat wipes                           │
│  • sustainable gym wipes                                 │
│  • plant-based yoga mat cleaning                         │
│  • studio cleaning supplies                              │
│  • yoga equipment care                                   │
└─────────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────────┐
│ STEP 2: GOOGLE TRENDS SEARCH                             │
├─────────────────────────────────────────────────────────┤
│ URLs to fetch:                                           │
│ 🇺🇸 https://trends.google.com/explore?q=...&geo=US      │
│    └─ Time range: Last 4 weeks + Last 1 week            │
│    └─ Region: United States                             │
│    └─ Interest level: 0-100 scale                        │
│                                                          │
│ 🇧🇷 https://trends.google.com.br/explore?geo=BR         │
│    └─ Time range: Last 4 weeks + Last 1 week            │
│    └─ Region: Brazil                                    │
│    └─ Interest level: 0-100 scale                        │
│                                                          │
│ 📊 https://trends.google.com/trending?geo=US            │
│    └─ Real-time trending topics (USA)                    │
└─────────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────────┐
│ STEP 3: TREND ANALYSIS                                   │
├─────────────────────────────────────────────────────────┤
│ For each KW variant, get:                                │
│  • Trend direction (↑ rising / ↓ falling / → stable)    │
│  • Peak dates (when searches spike?)                     │
│  • Geographic hotspots (where in US/BR?)                │
│  • Related queries (what else are people searching?)    │
│                                                          │
│ Example output:                                         │
│ "yoga mat cleaner wipes":                               │
│   Last week trend: ↑ +25% (rising)                      │
│   Last 4 weeks trend: ↑ +18% (rising)                   │
│   Peak region: Florida, California (summer)             │
│   Related: mat cleaning, yoga studio supplies            │
│   Interest level: 45/100 (moderate)                     │
└─────────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────────┐
│ STEP 4: CALENDAR + INTENT VALIDATION                     │
├─────────────────────────────────────────────────────────┤
│ Calendar hook: "Q2" (Apr-Jun, summer fitness season)    │
│ Current date: Mid-September (NOT Q2!)                    │
│                                                          │
│ ⚠️ DECISION POINT:                                       │
│  Is trend rising NOW or only seasonal?                  │
│                                                          │
│  ✅ IF rising NOW + evergreen angle exists              │
│     → Use it (buy 12 months out, studios prep summer)   │
│  ❌ IF only seasonal (won't spike until Apr)             │
│     → Flag for April publication, not now               │
│                                                          │
│ Blog intent: "buying_guide" (commercial)                │
│  • User is in problem-solution mindset                  │
│  • High purchase intent                                 │
│  • Trend rising = PERFECT timing                        │
└─────────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────────┐
│ STEP 5: NICHE SPECIFICITY SCORING                        │
├─────────────────────────────────────────────────────────┤
│ Broad KW:      "yoga mat wipes" (too generic)          │
│ Medium KW:     "eco yoga mat wipes" (OK)                │
│ Niche KW:      "plant-based yoga mat wipes studios"    │
│                (BEST for LLMs + less competition)       │
│                                                          │
│ Scoring:                                                │
│  Broad: 2/5 (high volume, high competition)             │
│  Medium: 3.5/5 (balanced)                               │
│  Niche: 4.5/5 (LLM-visible, low competition)           │
│                                                          │
│ Recommendation: Use "plant-based yoga mat wipes"        │
│  Reason: Rising trend + niche + LLM-friendly            │
└─────────────────────────────────────────────────────────┘
        ↓
┌─────────────────────────────────────────────────────────┐
│ STEP 6: PRODUCT RECOMMENDATION                           │
├─────────────────────────────────────────────────────────┤
│ Trend found: ↑ "plant-based yoga mat wipes" (+25%)      │
│ Intent: "buying_guide" (commercial) ✅                   │
│ Calendar alignment: Q2 summer (next quarter) ✅          │
│ Search volume: Rising now + seasonal spike = ✅ PERFECT │
│                                                          │
│ Recommended product:                                    │
│  🥇 Natural Gym Wipes Buckets (plant-based)            │
│     → Trend matches "plant-based" positioning           │
│     → Rising trend + buying guide = high conversion     │
│  🥈 EMPOWER Yoga Mat Wipes (premium tier)               │
│     → Secondary: upsell to affluent studios             │
│                                                          │
│ Blog positioning:                                       │
│  "Plant-Based Yoga Mat Wipes for Studios"               │
│  (Niche KW, trending, product-aligned)                  │
└─────────────────────────────────────────────────────────┘
```

---

## GOOGLE TRENDS RESEARCH MATRIX

### What Agent 1A Will Fetch

| Data Point | Source | Time Range | Metric |
|-----------|--------|-----------|--------|
| **Search Volume** | Google Trends | Last week + 4 weeks | Interest level (0-100) |
| **Trend Direction** | Google Trends | Last week vs 4 weeks | % change (↑/↓/→) |
| **Geographic Hotspots** | Google Trends | Regional breakdown | Which states/regions peak? |
| **Related Queries** | Google Trends | Auto-generated | What else are they searching? |
| **Real-time Trending** | Google Trending Topics | Today | What's viral right now? |
| **Commercial Intent** | Google Trends | Intent filters | How many searches are "buy" related? |
| **Seasonality** | Google Trends | 12-month view | Is it evergreen or seasonal? |

### Example Output (What You'll See)

```
GOOGLE TRENDS REPORT — "yoga mat cleaner wipes"

🇺🇸 USA MARKET:
  Last 4 weeks: 52/100 (moderate interest)
  Last 1 week: 58/100 (↑ +15% rising)
  Trend: ↑ RISING (strong upward momentum)
  Peak regions: California (23%), Florida (18%), Texas (12%)
  Related queries: mat cleaning solution, eco wipes, gym supplies
  Seasonality: Peaks Apr-Jun (Q2 summer) ← MATCHES YOUR CALENDAR

🇧🇷 BRAZIL MARKET:
  Last 4 weeks: 32/100 (low interest)
  Last 1 week: 35/100 (↑ +10% rising)
  Trend: ↑ RISING (slower than US)
  Peak regions: São Paulo (40%), Rio de Janeiro (25%)
  Related queries: limpeza yoga, wipes sustentável
  Seasonality: Less seasonal than US

💡 RECOMMENDATION:
  ✅ PRIMARY: Target USA market (higher interest + rising)
  ⚠️ SECONDARY: Brazil possible but lower volume
  
🎯 FINAL KW RECOMMENDATION:
  "Plant-based yoga mat wipes for studios" 
  (niche, trending, LLM-visible)
  
  Why: 
  • Keyword is rising (not declining)
  • Matches calendar hook (Q2 fitness season)
  • Buying guide intent aligns with trend
  • "Plant-based" differentiator = niche + LLM-friendly
  • Studios are commercial buyers (higher LTV)
```

---

## AGENT 1A DECISION TREE

```
START: Agent 1A gets keyword + calendar hook + intent

  ↓

GOOGLE TRENDS CHECK:
  Is keyword rising this week?
  ├─ YES → Continue
  └─ NO → Is it seasonal (matches calendar)?
          ├─ YES → Plan publication for peak month
          └─ NO → Flag: weak keyword, suggest alternatives

  ↓

TREND VS CALENDAR ALIGNMENT:
  Does trend peak align with calendar hook?
  ├─ EXACT MATCH (trend rising + Q2 selected) → 🟢 GO
  ├─ CLOSE (trend rising, Q2 is next) → 🟡 PLAN FOR NEXT MONTH
  └─ MISMATCH (trend falling or wrong season) → 🔴 RECONSIDER

  ↓

INTENT VALIDATION:
  Blog intent = buying_guide?
  ├─ YES + trend rising → 🟢 HIGH CONVERSION EXPECTED
  ├─ YES + trend stable → 🟡 OK, EVERGREEN PLAYS
  └─ NO (info only) → Adjust expectations

  ↓

NICHE SPECIFICITY SCORING:
  Primary KW: "yoga mat cleaner wipes" (score: 3/5)
  Niche KW: "eco-friendly yoga mat wipes studios" (score: 4.5/5)
  
  Recommendation: Use niche KW if:
  • Trend visible in niche variant too
  • Product positioning matches (eco/plant-based)
  • Target audience narrow (studios, not consumers)

  ↓

PRODUCT RECOMMENDATION:
  Match trend keywords → Wipex product family
  ├─ Trend mentions "eco/plant-based" → Natural Gym Wipes
  ├─ Trend mentions "premium" → EMPOWER
  ├─ Trend mentions "budget" → Table Bussers / Handy Jack
  └─ Trend mentions "sanitizing" → EPA Roll (if allowed)

  ↓

FINAL OUTPUT:
  "Based on Google Trends (USA, +25% this week),
   I recommend 'plant-based yoga mat wipes' as your blog KW.
   Primary product: Natural Gym Wipes Buckets.
   Publish ASAP (trend is rising now).
   Accept? Or override?"
```

---

## IMPLEMENTATION: Agent 1A Prompt (Updated)

```yaml
AGENT 1A: KEYWORD RESEARCH + GOOGLE TRENDS

Input:
  target_keyword: [KW]
  calendar_hook: [Q1/Q2/Q3/Q4]
  blog_intent: [buying_guide / how_to / educational / comparison]
  target_market: [US / BR]
  publish_date: [YYYY-MM-DD]

Research Protocol:

1. EXPAND KEYWORD:
   - Primary: [KW]
   - LSI variants (3-5): Generate semantic variations
   
2. GOOGLE TRENDS RESEARCH:
   a) Fetch https://trends.google.com/explore?q=[KW]&geo=[US/BR]
      - Last 4 weeks interest level
      - Last 1 week interest level
      - Calculate trend: (week1 - week4) / week4 * 100 = % change
      
   b) Extract from Trends:
      - Trend direction (↑ rising / ↓ falling / → stable)
      - Geographic hotspots
      - Related queries
      - Seasonality pattern (if visible)
      
   c) Check Google Trending (https://trends.google.com/trending?geo=[US])
      - Is this keyword in real-time trending?
      - If YES: High priority
      
3. CALENDAR + INTENT VALIDATION:
   - Calendar hook: [Q2] (Apr-Jun)
   - Today's date: [current]
   - Is trend rising NOW? ✅ or only seasonal?
   - Does buying intent match trend direction?
   
4. NICHE SPECIFICITY SCORING:
   For primary KW and niche variants, score 1-5:
   - Score formula: (LLM-friendly * 0.4) + (low-competition * 0.3) + (rising-trend * 0.3)
   - Recommend highest-scoring variant
   
5. PRODUCT RECOMMENDATION:
   Match trend keywords → Wipex product:
   - "plant-based" → Natural Gym Wipes
   - "premium" → EMPOWER
   - "eco" → Plant-Based Bulk Rolls
   - "budget" → Table Bussers
   - "sanitizing" → EPA Roll (validate compliance)
   
6. OUTPUT:
   Deliverables:
   ├─ Recommended keyword + score + trend analysis
   ├─ Trend direction (↑/↓/→) + % change
   ├─ Calendar alignment status (🟢 GO / 🟡 PLAN / 🔴 RECONSIDER)
   ├─ Recommended product + reasoning
   └─ Search volume estimate + competition level

Format: Markdown, one-page report with:
  • Trend data (chart-ready)
  • Calendar alignment check
  • Product recommendation with rationale
  • Niche KW recommendation (if score > 4)
```

---

## WHAT CHANGES IN YOUR INPUT FORM

**Old version:**
```yaml
target_keyword: "yoga mat cleaner wipes"  # You guess
```

**New version:**
```yaml
target_keyword: "yoga mat cleaner wipes"  # You guess (or Agent 1A researches)
google_trends_research: "auto"  # Agent 1A always runs Google Trends
calendar_hook: "Q2"  # Agent validates: does trend match?
blog_intent: "buying_guide"  # Agent validates: is trend commercial?

# Agent 1A OUTPUT:
recommended_keyword: "plant-based yoga mat wipes for studios"  # REFINED
trend_status: "↑ +25% this week (rising)"
calendar_match: "🟢 Perfect match (peaks Apr-Jun)"
recommended_product: "Natural Gym Wipes Buckets (plant-based)"

# You approve/override
approval: "✅ Accept recommendation"
```

---

## WHY THIS MATTERS

### Before (Old Agent 1A)
```
"yoga mat cleaner wipes" 
  → Generic, high competition
  → 8,100 searches/month (broad)
  → Hard for LLMs to differentiate
  → Might not be trending NOW
```

### After (New Agent 1A + Google Trends)
```
"plant-based yoga mat wipes for studios"
  → Niche, low competition
  → Rising 25% this week + peaks Q2 = PERFECT timing
  → LLM-visible (semantic clarity: plant-based + studios)
  → Matches your calendar hook + product positioning
  → Higher conversion (commercial intent + trend alignment)
```

**Result:** Better blogs, better LLM ranking, better product fit.

---

## NEXT INTEGRATION POINT

This connects to the **Product Recommendation Engine v2** (next document) which uses:
- Trend direction (↑ rising?)
- Calendar alignment (Q2 match?)
- Blog intent (buying guide → commercial)
- Niche specificity (LLM-visible keyword)

Together: **Trend + Calendar + Intent + Keyword = Perfect Product Choice**
