# SKILL DECISION MODELS — Visual Trade-Off Matrix

Você pediu para ver "os modelos para troca" (trade-offs).  
Aqui estão seus 3 cenários com pontos positivos e riscos:

---

## MODELO A: "AUTO-EVERYTHING" (Máxima Velocidade)

| Aspecto | Configuração | ✅ PRO | ❌ CON |
|---------|--------------|--------|--------|
| **Product Selection** | AI auto-recommends | Não precisa escolher; match perfeito com calendar | Pode indicar produto novo demais (baixo volume) |
| **Meta Title/Description** | AI auto-genera | Ganha 15 minutos | Precisa revisar tom de marca |
| **Claims** | AI puxa Claims Matrix | Tudo aprovado automaticamente | Sem escolha de positioning (Tier 1 vs 3) |
| **Audience** | Auto-detect por topic + hook | Rápido, acertado | Pode errar subtle audience (studios vs trainers) |
| **Images** | Auto-brief com stock suggestions | Pronto em 30 min | Imagens podem ser genéricas |
| **CTA** | Auto-select por CRO goal | Alinhado com KPI | Sem teste A/B |
| **Timeline** | 1.5 dias | ⏱️ MAIS RÁPIDO | Menos controle criativo |
| **LLM Ranking** | Skill otimiza direto | Visible, semântica limpa | Sem toque humano na tone |

**Use MODELO A when:**
- Você confia cegamente no skill
- Timeline crítico (<48h)
- Tema genérico (não diferenciado)
- Budget baixo (sem review cycles)

---

## MODELO B: "HYBRID" (Balanceado) ← **RECOMENDADO**

| Aspecto | Configuração | ✅ PRO | ❌ CON |
|---------|--------------|--------|--------|
| **Product Selection** | Você escolhe de TOP 3 | Você tem voz, AI suggests 3 melhores | 15 min deliberation |
| **Meta Title/Description** | AI gera, você ajusta | AI faz trabalho pesado; você refina tom | 30 min review |
| **Claims** | AI puxa matriz, você prioriza tier | Você elege positioning agressivo vs conservador | 20 min escolha |
| **Audience** | Auto-detect, você confirma/refina | Skill propõe, você corrige se errado | 10 min confirm |
| **Images** | AI brief, você escolhe entre 3 styles | Consistent brand, opções rápidas | 30 min selection |
| **CTA** | Auto-select, você refine copy | Botão correto, copy customizado | 15 min refine |
| **Timeline** | 2 dias | ⏱️ BALANCEADO |  1–2 hrs review total |
| **LLM Ranking** | Skill base + human tone polish | Visible, humanizado, personality | Pequena overhead |

**Use MODELO B when:**
- Você quer qualidade + velocidade
- Produto diferenciado (precisa de voice)
- Público específico (studio owners vs facilities)
- Tempo disponível: 1–2 hrs review

---

## MODELO C: "HUMAN-LED" (Máximo Controle)

| Aspecto | Configuração | ✅ PRO | ❌ CON |
|---------|--------------|--------|--------|
| **Product Selection** | Você especifica exato | Domínio total, zero surpresa | Você precisa conhecer catálogo |
| **Meta Title/Description** | Você escreve, skill valida | Seu branding, sua voz, seu KPI | 1 hr writing |
| **Claims** | Você escolhe claims explicitamente | Messaging agressivo possível | Risco de non-compliance |
| **Audience** | Você define persona detalhada | Matching cirúrgico, super específico | 30 min profiling |
| **Images** | Você cria brief ou links custom | Totalmente on-brand | Custo de design |
| **CTA** | Você escreve copy e escolhe ação | Teste A/B direto em blog | 45 min copywriting |
| **Timeline** | 3–4 dias | ❌ MAIS LENTO | Overhead significativo |
| **LLM Ranking** | Seu branding 100% + AI polish | Audiência específica, super relevante | Você é bottleneck |

**Use MODELO C when:**
- Campanha de lançamento (novo produto)
- Audience VIP/específica (case study)
- Você quer tone of voice consistente
- Tempo não é constraint

---

## QUICK DECISION TABLE

```
Timeline Pressure?
├─ < 48h → Modelo A (AUTO-EVERYTHING)
├─ 2-3 days → Modelo B (HYBRID) ← MOST TEAMS
└─ 3+ days → Modelo C (HUMAN-LED)

Product Knowledge?
├─ Low → Modelo B (AI suggests 3)
├─ Medium → Modelo B (you pick from 3)
└─ High → Modelo C (you specify exact)

Brand Differentiation?
├─ Generic (cleaning) → Modelo A
├─ Moderate (eco-positioning) → Modelo B ← BEST FOR WIPEX
└─ High (luxury brand, DTC) → Modelo C

LLM Ranking Priority?
├─ Secondary → Modelo A
├─ Primary → Modelo B (skill + tone polish)
└─ Mission-critical → Modelo C (you own voice)
```

---

## WHAT ACTUALLY HAPPENS IN EACH MODEL

### MODELO A: Auto-Everything

```
You fill out:
├─ Topic: "Yoga Mat Care"
├─ Calendar: "Q2"
└─ CRO: "E-commerce"

Skill does:
├─ 🤖 Recommends: Natural Gym Wipes + EMPOWER
├─ 🤖 Generates title: "Yoga Mat Wipes: Plant-Based Cleaning..."
├─ 🤖 Builds audience: "Yoga studio owners"
├─ 🤖 Pulls claims: Tier 2 + Tier 3 (all approved)
├─ 🤖 Brief images: "Hero: product shot + mat", "Body: hands cleaning", etc.
└─ 🤖 Generates blog + schema + internal links

You review:
└─ ☑ Approve OR ❌ Flag issues

Timeline: 1.5 days
```

### MODELO B: Hybrid (RECOMMENDED)

```
You fill out:
├─ Topic: "Yoga Mat Care"
├─ Calendar: "Q2"
├─ CRO: "E-commerce"
├─ ⚠️ Audience: "Auto-detect, I'll confirm"
└─ ⚠️ Product: "Show me top 3, I'll choose"

Skill proposes:
├─ 🤖 TOP 1: Natural Gym Wipes Buckets (TURI tested, Q2 spike)
├─ 🤖 TOP 2: EMPOWER Yoga Mat Wipes (premium, new)
└─ 🤖 TOP 3: Plant-Based Bulk Rolls (eco angle)

You decide:
├─ ✅ "I'll go with #1 + #2"
└─ 💬 "Use EMPOWER as primary (better for boutique studios)"

Skill adjusts:
├─ 🤖 Regenerates title: "EMPOWER Hot Yoga Mat Wipes: Premium Plant-Based..."
├─ 🤖 Reorders claims: Premium tier first, then Tier 2 performance
└─ 🤖 Rebuilds positioning: "boutique studio owners" instead of "all studios"

You review final:
├─ ☑ Meta title (65 chars) — "Looks good, keep it"
├─ ☑ Meta desc (155 chars) — "Change 'plant-based' to 'sustainable' for better CTR"
├─ ☑ CTA copy — "Make it say 'Shop Premium Mat Wipes' instead of generic"
└─ ✅ Approve for generation

Timeline: 2 days + 1–2 hrs your time
```

### MODELO C: Human-Led

```
You fill out:
├─ Topic: "Yoga Mat Care for Boutique Studios"
├─ Calendar: "Q2 summer launch"
├─ CRO: "E-commerce + Email list for VIP studios"
├─ ⚠️ Product: "EMPOWER only (not natural)"
├─ ⚠️ Audience: "Owner-operators of 5–25 person studios, $30k+ annual budget"
├─ ⚠️ Meta Title: "You write it yourself"
│   "Premium Yoga Mat Care for Studio Operators: The EMPOWER Difference"
├─ ⚠️ Meta Desc: "You write it"
│   "Discover how premium plant-based wipes protect high-use yoga mats. EMPOWER removes 147% more sweat. Used by 200+ studios. Start your trial."
├─ ⚠️ CTA: "Make it multi-step"
│   Primary: "Request Studio Trial"
│   Secondary: "Download Mat Care Guide (email capture)"
└─ ⚠️ Images: "You provide shot list"
   ├─ Hero: Studio owner + mats (lifestyle, aspirational)
   ├─ Product: EMPOWER box close-up on yoga mat
   ├─ Data: TURI chart (147% comparison, branded)
   └─ Testimonial: Headshot + quote from real studio owner

Skill role:
├─ 🤖 Validates claims (all your wording checked)
├─ 🤖 Builds copy structure (you review line-by-line)
├─ 🤖 Generates schema + internal links
└─ 🤖 Fact-checks all stats vs Claims Matrix

You review:
├─ Line-by-line copy edit (15 min)
├─ Image brief coordination (30 min)
└─ Final tone/voice polish (30 min)

Timeline: 3–4 days
```

---

## FOR WIPEX: RECOMMENDED STARTING APPROACH

Given your constraints (speed + professionalism + LLM ranking):

### **Start with MODELO B (Hybrid)**

Why?
- ✅ You keep creative control (product choice, positioning)
- ✅ AI handles grunt work (research, claims, SEO)
- ✅ 2 days timeline (not 1.5, not 4)
- ✅ 1–2 hrs of your time (totally manageable)
- ✅ Humanized tone (LLM-visible, not robot-generated)
- ✅ Scalable (do 2–3 blogs/week this way)

### **Graduation Path**

```
Week 1–2: Modelo B (you learn skill's recommendations)
  ↓ (trust builds)
Week 3–4: Modelo B but faster (you auto-approve 70% of choices)
  ↓ (confident)
Week 5+: Mix Modelo A (generic topics) + Modelo B (differentiated)
```

### **Red Flags That Trigger Modelo C**

- 🚨 Product launch (new SKU)
- 🚨 Competitor targeting (specific messaging)
- 🚨 Executive asking for "custom" blog
- 🚨 VIP customer case study
- 🚨 Regulatory sensitivity (claims audit)

---

## YOUR CALL

**Which model do you want to start with?**

A) AUTO-EVERYTHING (trust the AI, I'm busy)
B) HYBRID (I'll review 2–3 key choices) ← I SUGGEST THIS
C) HUMAN-LED (I own every decision)
D) TEST ALL THREE (run one blog per model, compare output)

**And:**
- When do you want the first test blog?
- Which topic? (Give me a real example from your calendar)

