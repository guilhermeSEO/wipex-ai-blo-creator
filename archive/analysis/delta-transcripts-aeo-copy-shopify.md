# Deltas — documentos soltos v2.0/v2.1 vs skill `wipex-blog-generation` v2.9

Base comparada: `SKILL.md` + `references/01, 02, 03, 05, 06, 07, 09, 10`.

## 1. Status por documento

| Documento | Status | Justificativa (1 linha) |
|---|---|---|
| `AGENT_2B_MASTER_PROMPT.md` | **parcialmente coberto** | Todo o eixo de 2B (título 65, meta 155, JSON-LD, links, readability, AEO/GEO/CRO, alt text) já está em `references/06`, mas o scaffold E-E-A-T, a lista de citation triggers e a regra de escolha de título/CTR não existem em lugar nenhum. |
| `WIPEX_BLOG_V2.1_COMPLETE_WORKFLOW.md` | **parcialmente coberto** | O fluxo Phase 0→2D já é `SKILL.md` §THE FLOW + `references/01/02/05/06/07`, porém a especificação executável do *calculator*, os campos de image brief e o exemplo "códigos de claim → pode/não pode dizer" não estão replicados. |
| `00_START_HERE.txt` | **obsoleto** | Onboarding do build v2.0 ("your 5 decisions", "I rebuild skill") — o estado de espera já foi resolvido; único item vivo é o modelo **D "test all three"**. |
| `SKILL_READY_CHECKLIST.txt` | **obsoleto** | Checklist pré-build v2.0 (A/B/C/D, "waiting on your model choice"); a taxonomia de entradas que ele contém já é `references/01`. |
| `FINAL_CHECKLIST_v2.1.txt` | **obsoleto** (1 item a dobrar) | Resumo de marketing do v2.1: quase toda a tabela de "expected improvements" é projeção/promessa; único instrumento reutilizável é o orçamento de horas por fase + SLAs de revisão. |

## 2. Conteúdo a dobrar (condensado)

**De `AGENT_2B_MASTER_PROMPT.md` → `references/06-agent-2b-seo-aeo-geo-cro.md`** (nova seção "E-E-A-T audit"):
- Scaffold de 4 categorias com *onde inserir*: `experience` = 2 casos de uso reais + citação externa de operador ("where_to_insert: body depois da seção de prova"); `expertise` = byline + credenciais; `authoritativeness` = 2 links externos + referências de estudo; `trustworthiness` = preço, garantia e prazo transparentes antes dos CTAs. Regra dura: cada sinal só entra se for real (ver §3-H).
- Citation triggers literais a usar no corpo: `"According to [source]…"`, `"Testing showed that…"`, `"[N] operators / [N]% …"`, `"Wipex lab testing methodology:"`. O 06 já tem os dois primeiros; faltam os dois últimos e a instrução de posicionamento ("before data claims").
- Featured-snippet: template de resposta em 5 bullets com o formato `• <eixo>: <micro-prova + fonte>` (ex. `• Better cleaning: 147% more residue removal vs traditional wipes (TURI tested)`), colocado "early body section (after intro)" — mesma posição que o 06 exige, mas com o molde.
- Regra de escolha de título por sinal disponível: `if has_pricing_promotion → option com "Save X%"; else if has_strong_data → option com o número; else → option com social proof` — decisão auditável em vez de gosto.
- Alt text com faixa de caracteres por slot (115–122 no exemplo) — casa com `references/07` ("100–125 chars"); dobrar apenas a exigência de reportar a contagem por imagem.

**De `WIPEX_BLOG_V2.1_COMPLETE_WORKFLOW.md` → `references/07` (§2 interactive) e `references/03`**:
- Especificação executável do calculator, hoje só descrita em prosa: campos `inputs[] (label, type, default)`, `calculation: "mats * classes_per_day * 30 * 2 wipes per mat"`, `output: "You'll need X wipes per month. That's Y buckets."`, `cta`. Isso dá a `references/07 §2` o molde input→fórmula→output→CTA que falta, mantendo a guarda já existente ("pode calcular custo/consumo, nunca performance").
- Image brief: acrescentar aos campos do 07 os dois que faltam — `overlay_text` (só rótulo sem claim) e `mood_notes` (notas de execução: "sunlit studio, real action, diverse founder").
- Formato de relatório de claims por SKU (`CAN say` / `CANNOT say` / `Recommended angle` / `FILTER VERSION`), útil como template em `references/03` §review — **desde que recalculado**, porque os códigos do exemplo estão errados (ver §3-L).

**De `FINAL_CHECKLIST_v2.1.txt` → `SKILL.md` §DELIVERY CONTRACT (rodapé)**:
- Orçamento de horas por fase como instrumento de planejamento (1A 2h · produto 1h · 1B 1.5h · 1C 2h · 2A 4–6h · 2B 2–3h · 2C 2–3h · 2D 2–3h; revisão humana 15 min no Gate 2 + 20–30 min no publish). Útil para responder "quando fica pronto"; **as colunas de ganho (CTR, conversão, ranking) não devem ser dobradas** — são projeções sem medição.

**De `00_START_HERE.txt` → `references/01`**: registrar o modelo **D — "test all three"** (rodar A/B/C em 3 posts e comparar) como variante de entrada, com a nota de que só faz sentido uma vez.

## 3. Contradições (regra antiga → regra vigente)

Item por item, o que os documentos afirmam e a skill hoje nega:

| # | Documentos soltos | Skill v2.9 |
|---|---|---|
| A | Corpo 1,800–2,200 / 1,950 palavras; "5-6 sections" | 3,000–4,500 (média medida 3,576), 14–22 H2 / 16 módulos |
| B | FAQ = uma seção entre outras, ~7 tópicos | FAQ **obrigatório**, 6–10 Q&As longo-formato |
| C | Links internos: "3 total" (`AGENT_2B`), "2-3 per 500 words" (`FINAL_CHECKLIST`) | 4–10 para `/products/` **e** 4–8 para `/blogs/` |
| D | `Estimated: 400-600 searches/month (US)` | Trends não devolve volume absoluto; volume só via Marketing (SEMrush/Ahrefs/GSC) — declarar indisponível |
| E | `Trend: ↑ +8.3%` apresentado como medido; janelas "last 4 weeks / last 1 week" | Índice relativo 0–100, janelas `today 1-m` e `today 12-m`, momentum calculado da série (média últimos 7 vs bloco anterior) |
| F | Promessas: CTR 8–12% / 8–18%, conversão 15–25% / 12–18%, "revenue lift 5–10x", "Positions 1–5 within 60–90 days" | `references/06`: "Never publish an expectation as a promise" — projeção rotulada, fora da copy |
| G | Social proof inventado: "200+ studios", "4.8/5 (247 reviews)", "92% reorder rate", "150+ studios tested", `aggregateRating.reviewCount: 247` | Nunca inventar rating/review/testemunho; `aggregateRating` só se real |
| H | GEO por hábito: "CA, FL, TX mentioned? ✅ Yes" | GEO a partir dos subregiões medidas em 1A, sem geo-stuffing |
| I | JSON-LD com `@type: [BlogPosting, FAQPage, Product]` + `geo: GeoShape` | `+ BreadcrumbList`; preços = JSON live do produto; FAQ entities = FAQ visível; **structured data nunca dentro da seção** (v2.7 — quebra o teto de 40 settings) |
| J | Shopify section template: `"name": "Blog Post - Plant-Based Yoga Wipes"` (32 chars), `richtext blog_content` | `name` ≤ 25 chars, ≤ 40 settings, `SHOPIFY-CONFIG.json`, Liquid balanceado — regra vinda de falha real de save |
| K | Data: hook Q2 + `publish 2026-10-15`, "publish in next 2 weeks for Q4 positioning" | Data derivada do pico de 12 meses (`references/02 §6`): 2–4 semanas antes do pico, min. 2; ocasião = 7 dias antes; aprovada no Gate 2 |
| L | Claims do SKU "N, S3, C, Eco" com `APPROVED TIER 2: "Removes 147% more residue than traditional quat-based wipes"` | `references/03`: Tier 2 exige código **`P`**; na tabela do SKU `P = —` → **sem número e sem comparação de performance**. Contradição real: o exemplo do doc não pode ser reaproveitado como está |
| M | Gates: um único stop ("YOU REVIEW + APPROVE, 15 min") | Gate 1 (brief) + Gate 2 (obrigatório: keyword/produtos/ângulo/**data**) + Gate 3 (publish) |
| N | Sem checagem de canibalização | ANGLE DELTA obrigatório em 1A + link recíproco |
| O | Sem branch de zero-dado (assume volume existente) | Zero-data é caminho de primeira classe, com STOP e escalação ao owner |
| P | AI-isms: 5 termos | 8 (acrescenta "game-changer", "in the realm of", "it's important to note") |

## 4. Descarte registrado

`00_START_HERE.txt`, `SKILL_READY_CHECKLIST.txt` e o corpo de `FINAL_CHECKLIST_v2.1.txt` descrevem um estado de projeto já encerrado (v2.0 em build, à espera de 5 decisões de operador) e não contêm regra vigente. `AGENT_2B_MASTER_PROMPT.md` e `WIPEX_BLOG_V2.1_COMPLETE_WORKFLOW.md` devem ser marcados como **fonte de instrumentos, não de números**: qualquer estatística, código de claim, promessa de desempenho ou bloco JSON-LD deles precisa ser re-derivado de `references/03` e das medições atuais antes do uso. Vários já estão no `archive/` do repositório da skill, o que cobre o registro histórico.