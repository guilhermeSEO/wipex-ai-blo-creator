## 1. Status por documento

| Documento | Status | Linha |
|---|---|---|
| `03-scripts/SKILL_INPUTS_MASTER.md` | **parcialmente coberto** | O formulário YAML de `refs/01` cobre metadata/modelos, mas faltam a tabela de segmentos de audiência, o motor de recomendação de produto em 5 etapas, a checklist final de 12 campos e as regras de formatação para LLM. |
| `03-scripts/DECISION_MODELS.md` | **parcialmente coberto** | A matriz A/B/C por fases e tempos está superada pela tabela de modelos de `refs/01` (tempo do owner, stop points/gates); o único conteúdo vivo é a lista de red flags que forçam o Modelo C. |
| `03-scripts/FILLED_FORM_EXAMPLES.md` | **parcialmente coberto** | Ex.1 (yoga) e Ex.2 (facilities) são casos do que `refs/01` já define em abstrato; o Ex.3 (IPA/electronics, `tier_3_only`, `blocked_terms`) é o único modelo para SKU sem TURI/EPA. |
| `04-data/02_AGENT_1B_CLAIMS_PREFLIGHT.md` | **parcialmente coberto / duplicado** | ~90% duplicado por `blog-01/1B-claims-envelope.md`, que é a versão final; guarda só a nota `Do not transfer P` e "page-verified 2026-09-23". |
| `04-data/blog-01-cost-per-table/1B-claims-envelope.md` | **parcialmente coberto** | Regras já em `refs/03`; ficam de fora o **template de envelope por post** e a adjudicação "cost-per-table é unidade de preço, não claim de performance". |
| `04-data/03_AGENT_1C_AUDIENCE_FAQ.md` | **já coberto** | Tabela de dados citáveis é idêntica a `refs/04` §3; template de persona equivalente. |
| `04-data/blog-01-cost-per-table/1C-audience-faq.md` | **parcialmente coberto** | `refs/04` dá o template mas não as 8 FAQs mineradas, a fórmula de consumo nem a tabela objeção→resposta com coluna "onde vive". |
| `04-data/21_blogs_outline.md` | **parcialmente coberto** | `refs/08` tem métricas e 5 sobreposições; o **registro dos H2 reais dos 21 posts** (usado para delta de ângulo) não está na skill. |
| `04-data/blog_patterns_21.csv` | **já coberto** (mas dependência externa) | Dados idênticos a `refs/08` §1; a skill só cita o CSV solto na PROVENANCE em vez de o embutir. |

## 2. Conteúdo a dobrar (condensado)

**→ `references/01-inputs-and-modes.md`**

**(a) Segmentos de audiência (auto-detect, você confirma) — substitui o vazio entre persona e calendar:**

```yaml
audience_segments:
  fitness_studios:    {pattern: B2B bulk, custo de supply chain/compliance, gancho: bundle + ROI}
  yoga_instructors:   {pattern: compra individual, culpa de sustentabilidade/preço premium, gancho: plant-based + certificações}
  office_managers:    {pattern: ciclo de budget Q1, bem-estar do funcionário, gancho: skin-safety + desconto por volume}
  facilities_mgrs:    {pattern: procurement, custo primeiro, gancho: dados TURI + métricas de performance}
```

**(b) Motor de recomendação de produto (quando `products: auto`)** — 5 passos: extrair hook → casar famílias de produto → cruzar matriz de claims → ranquear por intent comercial (🥇 primário, 🥈 upsell premium, 🥉 cross-sell) → apresentar TOP 3 com o motivo. Regra do loose doc que ainda vale: **o skill propõe 3 e o owner escolhe ou sobrescreve** — é o que dá conteúdo ao Gate 2.

**(c) Checklist final antes de gerar** (12 campos, todos com opção `auto`): topic/keyword, calendar hook, CRO goal, blog type, produtos, audiência, meta title, meta description, CTA primário, internal links, imagens, secção interativa.

**(d) Regras de redação LLM-friendly** (activa, número específico, dor do leitor, tom conversacional, entidades semânticas, JSON-LD) — hoje espalhadas em `refs/05/06`; consolidar como regra de estilo.

**(e) Red flags → Modelo C** (único sobrevivente de `DECISION_MODELS.md`): lançamento de SKU novo · targeting de concorrente · blog "custom" pedido por executivo · case study de cliente VIP · sensibilidade regulatória/auditoria de claims.

**(f) Formulário preenchido — modelo YAML com campos `your_edit`** (tirar do `FILLED_FORM_EXAMPLES`): o formato `output + your_edit: ACCEPT|EDIT|OVERRIDE` é o que torna o Gate 2 auditável.

**→ `references/03-compliance-claims-filter.md`**

**(g) Template do envelope por post (Agent 1B)** — a sequência em 6 blocos: (1) tabela de linhas Part 4 dos SKUs deste post; (2) "o envelope deste post" — tabela de exclusões aplicáveis, incluindo *title, meta, H1–H3, headers de tabela, labels de bullet, captions, alt text, texto do botão CTA*; (3) o que pode usar (frases Tier 3 + certificações com forma exacta); (4) adjudicação das tensões do brief; (5) escalações; (6) nota Part 9.3 em YAML.

**(h) Regras de adjudicação ainda ausentes de `refs/03`:**
- **"Cost per table" é unidade de preço, não claim** — permitido mesmo sem código `P`; usar como diferenciador porque "cost per wipe" já aparece em 16 posts.
- **Guardrail de adjacência**: nenhum número de custo ao lado de claim de performance, percentagem ou a palavra "safe".
- **"suitable for food service environments" é frase exacta**, nunca "perfect for"; `NSF` só na família scented.
- **"Do not transfer P"** entre SKUs visualmente idênticos (buckets iguais).
- Arithmetic próprio — custo por wipe → custo por mesa (2 wipes/reset: $0,15–0,18):

| SKU | Preço | Ct | $/wipe | $/mesa |
|---|---|---|---|---|
| WX01126TN / WX72024TBB | $36.99 | 400 | ≈$0.092 | ≈$0.18 |
| WX01130TN | $69.99 | 800 | ≈$0.087 | ≈$0.17 |
| WX01126TN-4 | $119.99 | 1 600 | ≈$0.075 | ≈$0.15 |

**(i) Exemplo IPA (Ex.3):** `tier: tier_3_only`; `blocked_terms: [disinfecting, sanitizing, germ-kill]`; nota "IPA story, NÃO posicionamento natural/fitness, audiência diferente" — o único modelo de envelope para produto fora de TURI/EPA.

**→ `references/04-agent-1c-audience-faq.md`**

**(j) Formato da tabela objeção→resposta com coluna "onde vive"** (cost block / FAQ / differentiation section) — `refs/04` só tem `objection → the only honest answer`. Exemplo real (6 objeções food-service) serve de modelo.

**(k) Fórmula de consumo a entregar ao leitor:** `tables × turns per service × wipes per reset × services per week`.

**(l) FAQ minerado (8 linhas) como exemplo trabalhado**, não só a regra "6–10 questões": cost per table vs cost per wipe · como calcular · reset time benchmark (<90 s Lavu; 3–5 min FlipMenu) · wipes por reset · cost per cover vs per table · scented vs unscented por sala · checklist pré-compra · minutos de mão-de-obra.

**(m) Caminho de decisão "nova localização/abertura"** (a versão final perdeu-o; o `03_AGENT_1C` tem 3 caminhos, o `1C-audience-faq` só 2).

**→ `references/08-house-patterns.md`** (+ `assets/`)

**(n) Registro de ângulos = H2s literais dos 21 posts** (as 21 listas de H2). É o instrumento de delta de ângulo/canibalização; `refs/08` só resume taxonomias e 5 sobreposições. Embutir como anexo `references/08b-house-outline.md` e **mover `blog_patterns_21.csv` para dentro da skill** (`assets/`), parando a dependência de `wipex/04-data/` que a PROVENANCE ainda admite.

**(o) Caveat de dados:** no outline, o post #12 (`bulk-wipe-refill-rolls-800ct`) repete exactamente os H2 do #5 (Labor Day) e as métricas (13 H2 / 4 H3) coincidem com as do #5 — a extracção desse post está contaminada. Corrigir antes de tratar o outline como fonte.

## 3. Contradições com a skill actual

1. **Endpoint inventado:** `SKILL_INPUTS_MASTER` manda buscar catálogo em `https://wipex.co/products.json`. Não existe; `refs/04` §4 diz `/products/<handle>.json` (`articles.json` = 404). Dobrar nada — registar como erro corrigido.
2. **Timeline:** `DECISION_MODELS` (1,5–4 dias) e `FILLED_FORM_EXAMPLES` ("48 h / 36 h") contradizem v2.3+: **lead mínimo 2 semanas, default ~1 mês antes do pico**, com o post em fila e data-alvo no Gate 2. Superado.
3. **Meta title com comparativo proibido:** Ex.1 propõe *"Plant-Based Yoga Mat Wipes: 147% Better Cleaning (Eco Studios)"* — **"Better"** é comparativo sem estudo, e o **147% pertence aos SKUs fitness/EMPOWER**, não a pomposo genérico de yoga. Contradiz `refs/03` (never-say + never transfer). Não dobrar; usar como contra-exemplo.
4. **Prova social inventada:** "200+ yoga studios" no meta description do Ex.1 — viola a regra "no invented facts" (SKILL.md #2). O próprio loose doc a corrige para "leading boutique studios", o que continua sem fonte.
5. **Versão do Filter / datas:** `02_AGENT_1B` diz page-verified **2026-09-23**; `1B-claims-envelope` §6 diz **2026-09-22** e §4 manda recomputar de JSON live. Manter o mais recente e sempre datar a verificação.
6. **Modelos A/B/C redefinidos:** nos loose docs são cadência de revisão humana; na skill são **stop points** (A = só Gate 3, B = Gates 2+3, C = Gates 1,2,3). A definição da skill prevalece; só as red flags (2e) sobrevivem.
7. **`blog_intent` vs `blog_type`:** o loose doc lista "Case Study" como tipo; a casa (21/21) não publica case studies — restringir a checklist/intake aos tipos medidos.