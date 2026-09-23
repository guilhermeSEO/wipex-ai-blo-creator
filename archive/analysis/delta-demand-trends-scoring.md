# Deltas — pesquisa de demanda / Trends / scoring

## 1. Status por documento

| Documento | Status | Nota |
|---|---|---|
| `03-scripts/PRODUCT_RECOMMENDATION_ENGINE.md` | **parcialmente coberto** | As 3 camadas existem em `02 §4` e o `fit` em `13 §5`, mas faltam os âncoras de calibração e a validação de claim codes dentro do matching. |
| `03-scripts/LLM_KEYWORD_SCORING.md` | **parcialmente coberto** | Fórmula, escalas 1/3/5 e bandas já estão em `02 §3` e `13 §3`; faltam o espectro de especificidade e a matriz calendar×trend×niche. |
| `03-scripts/GOOGLE_TRENDS_INTEGRATION.md` | **única em 15% / obsoleta em 85%** | O método de fetch (URL direta, "last 4 weeks + 1 week") foi superado por `11`; só a tabela sinal→família de produto e o decision tree têm valor. |
| `04-data/01_AGENT_1A_TRENDS_KEYWORD.md` | **já coberto** (evidência) | É literalmente o run que gerou `02 §2/§6`; único resíduo: a tabela de sub-regiões por termo (§1.5). |
| `04-data/blog-01-cost-per-table/1A-demand-keyword-product.md` | **parcialmente coberto** | Ângulo/dataset/date já em `02 §5/§6`, mas a auditoria de poluição semântica e a contagem de saturação do corpus não estão sistematizadas. |

---

## 2. Conteúdo a dobrar

**→ `references/02` §3 (LLM scoring) — espectro de especificidade.** Tabela de 5 faixas com volume/competição/conversão declaradamente **ilustrativos** (não medidos): broad "cleaning wipes" 18.200/mo, comp VERY HIGH, conv 1–2% → ❌; medium-niche "eco-friendly yoga mat wipes" 720/mo, MEDIUM, 8–12% → ✅; niche "plant-based… for boutique studios" 210/mo, LOW, 18–25% → 🟢 melhor se há demanda sazonal; ultra-niche 45/mo, NONE, 35–50% mas público minúsculo → 🔴 test only. Regra a reter: **o ganho de conversão é monotônico com a especificidade; o volume cai mais rápido que a conversão sobe.**

**→ `references/02` §3 — matriz de decisão calendar × trend × niche.** `Q2 + ↑+25% + niche 4.5+ → GO NOW (publish ASAP)` · `Q2 + ↑+10% + 4.0+ → PLAN FOR APR` · `Q2 + estável + 3.5+ → SECONDARY (evergreen)` · `Q2 + ↓−15% → SKIP` · `Evergreen + ↑+15% + 4.0+ → GO ANYTIME` · `Evergreen + estável + 4.5+ → ALWAYS VALID` · `Evergreen + ↓ + <3.5 → SKIP`. Complementa (não substitui) a derivação de janela de pico de `§6`.

**→ `references/02` §4 (product matching) — âncoras de calibração do fit 1–5.** `4.8 = material do trend + bulk + intenção comercial` · `4.2 = premium/upsell tier` · `3.5 = eco genérico, não vertical` · `2.1 = bulk certo, posicionamento errado ("natural" ≠ "disinfecting")` · `1.0–1.2 = escala/uso incompatível` · `0.5 = vertical errada`. E o passo que falta em `02 §4`: **validar os claim codes do SKU ANTES de rankear** (ex.: N→"plant-based", S3→"hypoallergenic", C/Eco→"eco-friendly", D→EPA; ausência de EPA correto para limpeza de superfície).

**→ `references/13` §5/`references/02` §4 — tabela sinal→família (de GOOGLE_TRENDS_INTEGRATION §4).** `"plant-based"→Natural Gym Wipes` · `"premium"→EMPOWER` · `"eco"→Plant-Based Bulk Rolls` · `"budget"→Table Bussers / Handy Jack` · `"sanitizing"→EPA Roll (só se compliance permitir)`. É a curadoria de catálogo que falta antes do passo "query the catalogue".

**→ `references/02` §2 — poluição semântica (de 1A-cost-per-table §3).** Teste objetivo: ler as RELATED_QUERIES do termo de maior média; se o cluster é de outro intento (*cost per use* → "what is a use case" 100 · "openai news" 59 · "how to use apple pay" 35 / rising "openai news today" 24.100), o volume é real e o leitor é errado → **rejeitar como primary mesmo com média 66,2/1-m**. Contraste de controle: *janitorial supplies* tem related puramente comerciais ("janitorial supplies near me" 100 · "wholesale" 47) mas pico em junho.

**→ `references/02` §5 — saturação do corpus por contagem (de 1A-cost-per-table §5).** Método: varrer os N posts mais recentes e contar quantos já possuem o território. Medido: `cost per wipe` em **16 de 21 posts** (inclusive H2 literal nos dois posts de formato) → território saturado; e esse termo tem a **menor demanda medida do cluster (avg 13,9; 1-m 3,1)**. Delta obrigatório = mudança de unidade (wipe → mesa/cover).

**→ `references/02` §6 — linhas de pico em falta na tabela medida.** `cost per table` 12-m avg 46,5 · top weeks Mar 1–7 (100) · **Nov 30–Dec 6 (95)**, 1-m 49,4 / last7 52,6 · janela Nov 1–20. `cost per cover` avg 38,2 · **Nov 30–Dec 6 (100)**, Dec 7–13 (77) · 1-m 45,0. `cleaning supplies cost` avg 50,9 · Nov 30–Dec 6 (93) · 1-m 19,3→35,1 (subindo). `table reset time`, `labor cost restaurant`, `janitorial supplies`, `restaurant operating costs` → sazonalidade errada para Q4. `commercial table wipes` avg 8,2 decaindo a 0. Observação: `cost per table` e `cost per cover` são quase equivalentes (46,5 vs 38,2) — usar como par, não como aposta única.

**→ `references/02` §7 (template) — encadeamento do método de extração que funciona.** Ordem verificada: consultar variante de produto → se série vazia nos dois ranges e em US e BR, **aplicar o zero-data branch** → pivotar para o cluster operacional → extrair related queries do operacional para validar intento → derivar pico → publicar. O raw JSON em `raw/trends_*.json` é o que sustenta a afirmação "zero demand".

---

## 3. Contradições com a skill atual

1. **Fórmula de scoring duplicada e divergente.** `GOOGLE_TRENDS_INTEGRATION` §4 define `(LLM-friendly×0.4) + (low-competition×0.3) + (rising-trend×0.3)`; a canônica é `Sem×.25 + Ent×.25 + Niche×.15 + Moat×.15 + Trend×.20`. A antiga deve ser marcada como **superada** em `13 §3` para não ser reintroduzida.
2. **Números inventados apresentados como medidos.** `LLM_KEYWORD_SCORING` (volumes 18.200/4.800/720/210/45, conversões 12–18%, "+26%"), `PRODUCT_RECOMMENDATION_ENGINE` (CTR "+18-25%", "expected conversion 12-18%", "search volume 400-600/mo") e `GOOGLE_TRENDS_INTEGRATION` ("interest 58/100", "peak regions CA 23%") violam o não-negociável #2 e a disciplina de `12`. Podem entrar apenas como **fatores de forma**, nunca como valores.
3. **Timing de publicação.** Os três docs mandam "publish ASAP / in the next 2 weeks" por o trend estar subindo no momento; a regra vigente é **QUEUE até 14–28 dias antes do pico** (`02 §6`, `09`). O exemplo Q2/yoga publicado em setembro é o caso que a v2.3 corrigiu explicitamente.
4. **Niche 5/5 penalizado vs promovido.** `LLM_KEYWORD_SCORING` marca ultra-niche 5/5 como "🔴 TOO NARROW (test only)"; `13 §3` trata especificidade de nicho como **a estratégia**. Conciliar: 5/5 em niche é desejável, desde que o termo tenha série medida — o que decide é o trend momentum medido, não a estreiteza.
5. **Fetch de Trends.** Ambos os docs de Trends assumem busca de `trends.google.com/explore?q=…` / `.com.br/explore?geo=BR` por fetch direto. `11` prova que isso dá 429 e que o explore é app JS; a URL `.com.br` nunca foi validada. Marcar como superado.
6. **BR como mercado secundário.** Os docs mantêm BR como secundário viável; as duas medições mostram **zero em todos os termos** nos dois clusters (e `02 §2` já diz "BR is not a market"). Os rótulos `geo_secondary`/BR devem sair do template.
7. **Nomes canônicos divergentes entre os dois docs soltos.** O mesmo SKU aparece como "Table Bussers® Plant-Based All-Purpose Cleaning Wipes | Autumn-Scented" (WX01126TN) e "Table Bussers Surface Wipes (scented, cinnamon-clove)". A skill exige o nome canônico do Part 4 — usar um só, o de Part 4, e eliminar o outro.
8. **Escopo de Agent 1A.** `PRODUCT_RECOMMENDATION_ENGINE` define YAML de input próprio (`topic/calendar_hook/blog_intent/cro_goal/target_market`), sobreposto a `references/01` — substituído pelo formulário único de `01`.

---

### Resumo
- Li os 5 documentos soltos inteiros e as 4 referências-alvo (`SKILL.md`, `02`, `11`, `13`).
- **Nenhum arquivo criado ou modificado** (conforme instruído).
- A maior parte do material solto é redundante com a skill ou mede números que a skill proíbe tratar como dados. O que ainda não está dobrado e vale dobrar é: espectro de conversão por especificidade, matriz calendar×trend×niche, âncoras de fit e pré-checagem de claim codes no matching, tabela sinal→família, **teste de poluição semântica**, contagem de saturação do corpus, e 4 linhas de pico medidas (cost per table/cover, cleaning supplies cost) para `02 §6`.
- 8 contradições registradas; as três com risco real de reincidência são a fórmula antiga 0.4/0.3/0.3, os números apresentados como medidos, e o "publish ASAP" contra a regra de runway.