# 3A — VIDEO PROMPT PACK · Blog #1 "Cost per table"
### Destino: slot de vídeo da seção `wipex-section-cost-per-table-2026` · `video_anchor: before_faq`

---

## 0. RESTRIÇÕES DO SLOT (não são preferências — são o que o código faz)

Medido no `SHOPIFY-CONFIG.json` + `sections/wipex-section-cost-per-table-2026.liquid`:

| Item | Valor real | Consequência para o vídeo |
|---|---|---|
| Tipo | `video_tag` nativo Shopify (`lifestyle_video`) | tem de ser **hospedado na Shopify** (arquivo .mp4 enviado ao admin) |
| Proporção | `aspect-ratio: 16/9` com `object-fit: cover` | enquadre tudo no **centro** (as bordas podem ser cortadas em telas pequenas) |
| Áudio | `muted: true` | **roda 100% mudo** → nada de narração; toda a mensagem é **texto na tela** |
| Reprodução | `autoplay, loop: true, controls: false` | tem de funcionar **sem ninguém clicar** e **fechar em loop** |
| Posição | antes do FAQ (`video_anchor: before_faq`) | o leitor já viu preço, cálculo e checklist → o vídeo **consolida**, não explica |
| Mídia | *"editorial media only: product imagery stays out of the section"* | **não é demo de produto**; é cena em serviço (restaurante real) |
| Overlay | `video_heading` / `video_text` / `video_cta` — **hoje vazios** | o gancho de conversão vai no overlay, não no vídeo |
| Fallback | `video_fallback_image` (16:9) + alt | precisa de 1 still 16:9 para celular/autoplay bloqueado |

**Duração-alvo: 22–25 s** (mín. 20 / máx. 30). Loop sem corte perceptível: o **frame final tem de
casar com o primeiro** (mesma cena, mesmo enquadramento).

---

## 1. O PROMPT MESTRE (copiar/colar)

> Use um único prompt por clipe (a maioria das ferramentas não aceita multi-cena). Os 6 shots
> estão na §2; a montagem está na §3.

```
Cinematic 16:9 editorial brand film for a US restaurant-supply brand. Real, warm, in-service
documentary feel — not a glossy studio ad. Shot on a full-frame camera, 35mm lens, shallow
depth of field, natural warm restaurant light with practical pendant lamps, 24fps, subtle
handheld movement, no on-screen text, no logos, no captions.

Scene: a busy American casual-dining room during evening service, about 20 four-top tables,
wood-and-brass finishes, two staff in plain dark aprons — a busser and a host — no customers
in frame. A server station at the edge of the room holds an open white 400-count cleaning-wipe
bucket with a stack of white wipes visible.

Action, one continuous reset, no cuts: a busser walks to a table that has just been vacated —
plates and glasses still on it — and does the four moves in one smooth pass: clears the plates
and glassware, wipes the tabletop once with a single wipe lifted from the bucket at the
station, sets the tabletop back with cutlery and a candle, and gives the host a short nod.
The host seats two guests at the reset table and the room keeps moving behind them.

Mood: efficient, calm, under control at peak service. Colour: warm neutrals, dark wood, soft
mint-white highlights on linen. No slow-motion, no lens flares, no text, no product close-up,
no cleaning-performance implication.
```

---

## 2. SHOT LIST / TIMELINE (25 s, montagem final)

Cada linha = clipe separado a gerar (ou a filmar). O tempo é o da **timeline de edição**.

| # | Entrada–Saída | Cena (o que a câmera vê) | Texto na tela (EN) |
|---|---|---|---|
| 1 | 0.0 – 2.5 s | Amplo da sala cheia durante o serviço; uma mesa é desocupada | `Every dirty minute is a seat you already paid for.` |
| 2 | 2.5 – 6.5 s | Busser caminha do balcão até a mesa (o "fetch") | `The cost isn't the wipe. It's the trip.` |
| 3 | 6.5 – 13.0 s | O reset em **um plano contínuo**: limpar → passar 1x → repor → assentar | `Clear · Clean · Reset · Seat` |
| 4 | 13.0 – 17.5 s | Card de números sobre o mesmo ambiente (ver §4) | `$0.09 a wipe · $0.29 a table · under 90 seconds` |
| 5 | 17.5 – 21.5 s | Balcão de estação: mão pega **uma** toalha do balde aberto; mesa volta a ser posta | `One consumable. Already at the table.` |
| 6 | 21.5 – 25.0 s | Mesa posta, host acomoda 2 convidados, sala cheia atrás; logo entra no fim | `Reduce Table Turnover Time.` · `wipex.co` |

**Fechamento de loop:** o plano 6 deve terminar **exatamente no enquadramento do plano 1** (mesmo
amplo da sala). Assim o `loop: true` não pisca.

---

## 3. TEXTO NA TELA — regras de composição

- Fonte: **Raleway** (a do tema) — ou "New Order" no logo final. Peso 600–700.
- Cor: branco `#FFFFFF` sobre o gradiente escuro do slot (`--wx-dark: #111111`); sem sombra dura.
- Posição: **terço inferior** (o slot tem `background: linear-gradient(180deg, transparent → rgba(17,17,17,.72))` no rodapé) — o texto baixo fica legível e não briga com o overlay do editor.
- Máx. **7 palavras** por cartela · **1 cartela por shot** · entrada/saída com fade de 0,25 s.
- **Zero texto dentro do clipe gerado** (IA gera letra errada). Todo o texto entra na edição.
- Números: **só os nossos preços** e as figuras de terceiros **com fonte + data**, como no blog
  (Lavu, 23 Sep 2026; Worldmetrics, 2026). Nunca um número de desempenho de limpeza.

---

## 4. CARTELA DE NÚMEROS (shot 4) — desenho aprovado

Fundo: foto do shot 4 a 20% de opacidade + película ink `rgba(17,17,17,.72)`.
Três números em linha (stacks no mobile), separados por hairline `#e8e8e1`:

```
$0.09                          $0.29                        under 90 seconds
per wipe, 400-count bucket     cost per table, 20-table     target reset time
                               room, consumable + labour    (Lavu, checked 23 Sep 2026)
```

Rodapé pequeno: `Consumable + labour. Prices: 400-count Table Bussers® bucket, current published rate.`
(esta é a mesma nota de compliance da calculadora — **"Cost figures only"**)

**Preços verificados ao vivo a 2026-09-28** (`/products/<handle>.js`): Autumn $36.99/400 → **$0.0925**,
$69.99/800 → $0.0875, $119.99/1,600 → **$0.075**; Unscented idem. Todos os três variant de cada SKU
`available: true`. Os rótulos `$0.09` e `$0.075` são o arredondamento de casa — **reconferir no dia do
upload**.

---

## 5. BRIEF DE FILMAGEM REAL (se for gravar, não gerar)

Se houver verba para uma diária, este é o plano de rodagem — mais barato e mais autêntico que IA
para cena de sala (IA erra mãos, talheres e movimento de pessoas).

- **Locação:** salão casual-dining real, 20 mesas, 1 estação com o balde aberto visível. Luz prática da casa + 1 softbox quente de reforço.
- **Elenco:** 3 — busser, host, 2 figurantes de sala (sem close de rosto de convidado).
- **Planos (6 setups, ~1h de captação):** amplo sala · busser caminhando · reset em plano único (a peça-chave, 3 takes) · detalhe mão + balde · mesa sendo posta · host acomodando.
- **NÃO filmar:** close de embalagem como herói, produto girando, "antes/depois" de superfície, mão limpando com close dramático. Não é demo.
- **Roupa/marca:** aventais lisos escuros, sem logos de terceiros.
- Exposição para o rodapé receber texto → deixar a parte de baixo do quadro sem detalhe importante.

---

## 6. EXPORT & UPLOAD (Shopify)

| Item | Valor |
|---|---|
| Master | MP4 · H.264 · **1920×1080** · 24 fps · ~8–10 Mbps |
| Áudio | **faixa de áudio vazia** (o slot muta de qualquer forma; arquivo menor) |
| Duração | 22–25 s |
| Peso | **< 30 MB** (autoplay em 4G precisa ser leve) |
| 1º frame | = último frame (loop limpo) |
| Poster/fallback | still 16:9 do shot 1 (mesmo enquadramento), 1600×900, `image_url` |
| Alt do fallback | `Busser resetting a table in a busy restaurant dining room during service` |

Upload: admin Shopify → Content → Files → subir o MP4 → no editor do tema, seção *Wipex Cost Per
Table* → campo **Lifestyle video**. Sem o fallback o slot **não renderiza nada** fora do editor.

---

## 7. OVERLAY DO EDITOR — preencher (hoje vazio)

Para o vídeo virar CTA (é o enquadramento "editorial", o link faz a venda):

| Campo do tema | Valor sugerido |
|---|---|
| **Overlay heading** (`video_heading`) | `Reduce Table Turnover Time` |
| **Overlay text** (`video_text`) | `Set your cost per table first, then decide what to change.` |
| **Overlay CTA label** (`video_cta.label`) | `Shop Table Bussers®` |
| **Overlay CTA URL** (`video_cta.url`) | `https://wipex.co/products/table-bussers-surface-wipes` |

O heading é o **mesmo** da faixa de conversão final — repetição proposital, é o objetivo da peça,
não um resultado medido. Não escrever "cuts reset time by X%" (ver §8).

---

## 8. GUARDRAILS DE COMPLIANCE (Claims Filter v1.1 · `P = —` nos dois SKUs)

Isto vale para **texto na tela, overlay, alt text, título do arquivo e legenda**.

**Proibido em qualquer forma:** qualquer número/percentual de **desempenho de limpeza** ·
`safe/safe on` (superfície) · `best/safest/ultimate/#1` · `food-safe/food-grade` ·
`non-toxic/chemical-free/harmless` · `kid & pet safe` · **bare "compostable"** ·
**bare "Sustainable"** · `100% natural` · `lab-tested/proven/clinically` ·
`outperforms/better than/more effective` · **EWG Verified®** (bloqueado até o Dean resolver) ·
`hygienic clean / sanitary / kills what's on the table`.

**Permitido:** a aritmética de **custo** (nossos preços) · `one wipe, one pass` · `removes the
fetch` · `a reset that never needs a second trip` · `designed for tables and counters` ·
`NSF-certified` **só no Autumn** · `suitable for food service environments` **só no Autumn** ·
`Reduce Table Turnover Time` **como objetivo imperativo**, nunca como resultado medido.

**Adjacência (Part 3):** nenhum número de custo pode ficar ao lado de claim de desempenho,
percentual ou da palavra "safe". A cartela de números (§4) é **tabela de preço**, e só.

---

## 9. CHECKLIST DE ENTREGA

- [ ] MP4 1920×1080, sem faixa de áudio, < 30 MB, 22–25 s
- [ ] loop fecha (1º frame = último frame) conferido na própria página
- [ ] todo texto na tela em EN, Raleway, terço inferior
- [ ] números conferidos contra a página do produto no dia do upload (hoje: $36.99/400 → $0.09)
- [ ] overlay (heading/text/CTA) preenchido no editor
- [ ] fallback 16:9 enviado + alt descritivo
- [ ] lint de compliance: 0 BLOCKING (rodar a varredura de termos do §8 no texto na tela)
- [ ] preview mobile: o vídeo autoplay, mudo, sem controles, e reaparecendo após o FAQ
- [ ] registrar no `04-data/published_ledger.md` junto com o post

---

*Wipex — Facility Supply Team · pacote de produção de vídeo · blog #1 "Cost per table" · 2026*
