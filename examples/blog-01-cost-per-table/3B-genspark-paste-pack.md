# 3B — GENSPARK PASTE PACK · Blog #1 "Cost per table"
### Tudo o que se copia e cola, na ordem. Companion de `3A-video-prompt.md`.

---

## 0. ANTES DE COLAR — 3 decisões que definem o resultado

| Decisão | Valor | Porquê |
|---|---|---|
| **Imagens de produto** | **NÃO USAR** | A seção é *editorial media only* (consta no `SECTION-VALIDATION.txt`); os cards do artigo renderizam sem `<div class="…__card-media">` e o config dos SKUs tem `"image": ""`. Produto entra por **link**, não por imagem. |
| Modo no Genspark | **Text-to-Video** (1º clipe) → depois **Image-to-Video** | A continuidade entre clipes só se consegue reusando o mesmo still como start frame. |
| Aspect Ratio | **16:9** | O slot força `aspect-ratio:16/9` + `object-fit:cover`. |
| With Audio | **OFF** | O slot roda `muted:true`. Áudio é peso morto (e o MP4 final sai sem faixa de áudio). |
| Texto na tela | **no editor/timeline do Genspark**, nunca pedido ao modelo | IA erra letra. Os textos estão na §4. |

**Fluxo recomendado (o que dá continuidade):**
1. Gere o **STILL MESTRE** (§2) — é o plano 1 e também o *fallback image* do slot.
2. Para cada clipe, use esse still como **start frame** (Image-to-Video) e cole o prompt do clipe.
3. Monte na timeline do Genspark: corte para 22–25 s, adicione as cartelas da §4.
4. Exporte e confira o loop (1º frame = último).

---

## 1. BLOCO DE CENA (repetido literalmente em todo prompt)

Não edite este bloco — a repetição literal é o que mantém o mesmo salão entre os clipes:

```
a busy American casual-dining room during evening service, about 20 four-top tables with dark
wood tops and brass trim, warm practical pendant-lamp light, staff in plain dark aprons, no
customers in frame, an open unbranded white cleaning-wipe bucket on the server station at the
edge of the room
```

---

## 2. STILL MESTRE / FALLBACK (coloque no gerador de imagem)

**Config:** 16:9 · 1600×900 · realista, não ilustração.

```
Photorealistic editorial photograph, 16:9 landscape. A busy American casual-dining room during
evening service: about 20 four-top tables with dark wood tops and brass trim, warm practical
pendant-lamp light, a busser in a plain dark apron resetting one table in the middle distance
while the room keeps moving behind, an open unbranded white cleaning-wipe bucket on the server
station at the edge of the room. No customers in frame. Warm neutrals, dark wood, soft
mint-white highlights on linen. 35mm lens, shallow depth of field, natural grain, documentary
reportage look. No text, no logos, no watermark, no lorem ipsum, no captions.
```

O still aprovado vira **fallback image** do slot (alt: `Busser resetting a table in a busy
restaurant dining room during service`) **e** o start frame dos 6 clipes.

---

## 3. OS 6 PROMPTS DE VÍDEO (um por geração)

Cada prompt é autossuficiente. Cole o bloco de cena (§1) dentro, como está.

### CLIPE 1 — abertura da sala (0.0–2.5 s)
```
Cinematic editorial brand film, real in-service documentary feel, not a glossy ad. [SCENE].
Slow push-in on the dining room while one table is being vacated. Two guests stand and leave
frame left as the table empties. 35mm lens, shallow depth of field, subtle handheld movement,
24fps, warm natural light. No text, no logos, no customers' faces, no cleaning close-up.
```

### CLIPE 2 — o "fetch" (2.5–6.5 s)
```
Cinematic editorial brand film, real in-service documentary feel. [SCENE]. A busser in a plain
dark apron walks from the dining room to the server station at the edge of the room and reaches
for a wipe from the open unbranded bucket — the walk is the subject, not the product. Follow shot
from behind at chest height. 35mm lens, shallow depth of field, subtle handheld, 24fps. No text,
no logos, no product close-up, no brand on the bucket.
```

### CLIPE 3 — o reset em plano único (6.5–13.0 s) ← a peça-chave
```
Cinematic editorial brand film, real in-service documentary feel. [SCENE]. One continuous take,
no cuts: a busser arrives at a vacated four-top with plates and glasses still on it, clears the
plates and glassware, wipes the tabletop once in a single smooth pass, sets the top back with
cutlery and a small candle, then nods to the host. Camera holds on the table at chest height,
slight handheld drift. 35mm lens, shallow depth of field, 24fps. No text, no logos, no
cleaning-performance implication, no slow motion.
```

### CLIPE 4 — chão para a cartela de números (13.0–17.5 s)
```
Cinematic editorial brand film, real in-service documentary feel. [SCENE]. Static medium-wide of
the dining room at peak service, tables being reset in several places at once, calm and under
control. Minimal camera movement. 35mm lens, warm natural light, 24fps. Leave the lower third of
the frame visually quiet (plain tabletop or floor) — a caption will be laid over it. No text, no
logos, no faces.
```

### CLIPE 5 — balde e mesa sendo posta (17.5–21.5 s)
```
Cinematic editorial brand film, real in-service documentary feel. [SCENE]. Close but editorial,
not a product shot: a hand lifts a single white wipe from the open unbranded bucket on the server
station; cut to the same hand setting the tabletop back with cutlery. Hands and forearms only, no
face. 35mm lens, shallow depth of field, warm light, 24fps. No text, no logos, no brand name, no
label on the bucket, no water droplets, no spray bottle.
```

### CLIPE 6 — fecho, casa com o clipe 1 (21.5–25.0 s)
```
Cinematic editorial brand film, real in-service documentary feel. [SCENE]. Wide shot of the
dining room at full service with the reset table now occupied by two seated guests and the host
walking away; the room continues behind. Camera settles into a still, matching wide of the opening
frame. 35mm lens, warm natural light, 24fps. Leave clean space at the bottom centre of the frame
for a logo. No text, no logos, no faces.
```

**Consistência:** se um clipe sair de outro salão/luz, regenere-o usando o **start frame** do still
mestre outra vez — não tente corrigir por texto.

---

## 4. CARTELAS DE TEXTO (adicione na timeline, §4 de `3A`)

Fonte Raleway 600–700 · branco `#FFFFFF` · **terço inferior** · fade 0,25 s · máx. 7 palavras ·
1 cartela por clipe · entra sobre o gradiente escuro que o slot já aplica no rodapé.

| Sobre o clipe | Texto na tela |
|---|---|
| 1 | `Every dirty minute is a seat you already paid for.` |
| 2 | `The cost isn't the wipe. It's the trip.` |
| 3 | `Clear · Clean · Reset · Seat` |
| 4 | `$0.09 a wipe · $0.29 a table · under 90 seconds` |
| 5 | `One consumable. Already at the table.` |
| 6 | `Reduce Table Turnover Time.` + `wipex.co` |

Nota pequena na cartela 4 (a mesma da calculadora):
`Consumable + labour. Prices: 400-count Table Bussers® bucket, current published rate.`

---

## 5. O QUE NÃO PEDIR AO MODELO (o gerador vai entregar errado)

- ❌ **Texto ou logo gerado** — sai com letra deformada. Texto só na timeline.
- ❌ **Marca na embalagem** — o modelo inventa um rótulo falso. Por isso *"unbranded"* no prompt.
- ❌ **Frasco de spray / pano de pano** — o argumento é "sem fetch". O spray reintroduz o problema.
- ❌ **Close dramático de limpeza, gotas, brilho de superfície** — vira claim de desempenho.
- ❌ Qualquer coisa que implique desempenho: não use nas cartelas nem no título do arquivo as
  palavras do §8 de `3A` (safe, best, food-safe, kills, proven, EWG…).

---

## 6. CHECKLIST DE EXPORT (Genspark → Shopify)

- [ ] timeline com 22–25 s (corte a mais, não a menos)
- [ ] 16:9 mantido no export
- [ ] "With Audio" OFF → MP4 **sem faixa de áudio**
- [ ] < 30 MB · 1920×1080
- [ ] 1º frame = último frame (loop limpo)
- [ ] still mestre exportado 1600×900 como **fallback image** do slot
- [ ] upload: Shopify → Content → Files → MP4; theme editor → seção *Wipex Cost Per Table* →
      campo **Lifestyle video**; e o **Video fallback image (16:9)** + alt
- [ ] overlay do editor preenchido (§7 de `3A`)
- [ ] preço reconferido no dia do upload (hoje $36.99/400 → $0.09)

---

*Wipex — Facility Supply Team · pacote Genspark · blog #1 "Cost per table" · 2026*
