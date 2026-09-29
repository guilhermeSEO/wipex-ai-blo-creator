# 3C — PROMPT ÚNICO (Genspark) · Blog #1 "Cost per table"
### Um prompt → um vídeo de 25 s pronto. Sem cortes, sem montagem, sem 6 gerações.

---

## 0. NO PAINEL, ANTES DE COLAR

| Campo | Valor |
|---|---|
| Modelo | o de **maior duração** disponível (Sora / Veo 3 / Kling) |
| Aspect Ratio | **16:9** |
| With Audio | **OFF** (o slot roda mudo — áudio é peso morto) |
| Duração | o máximo que o modelo aceitar (se der 10 s, gere e use **Extend** até 20–30 s) |
| Imagens de produto | **nenhuma** — a seção é editorial e o balde tem de sair sem marca |

**Por que um plano único:** os 6 clipes pediam continuidade entre gerações, que IA não garante.
Num único take contínuo o problema desaparece — e o reset já era, no roteiro, um plano só.

---

## 1. O PROMPT (copiar tudo, colar de uma vez)

```
A single continuous 25-second cinematic shot, 16:9, photorealistic editorial brand film for a
restaurant-supply brand. Real in-service documentary feel, not a glossy studio ad. Shot on a
full-frame camera, 35mm lens, shallow depth of field, warm practical pendant-lamp light, 24fps,
gentle handheld drift, natural film grain. No cuts, no camera whips, no slow motion, no lens
flares.

SETTING: a busy American casual-dining room during evening service — about 20 four-top tables
with dark wood tops and brass trim, staff in plain dark aprons, no customers' faces in frame, and
an open unbranded white cleaning-wipe bucket on the server station at the edge of the room. Warm
neutrals, dark wood, soft mint-white highlights on linen.

THE SHOT, in one continuous take, camera slowly drifting forward and then settling:
Beat 1 (0–3s): wide of the full dining room at peak service; a table is vacated as two guests
stand and leave frame left.
Beat 2 (3–7s): the camera follows a busser in a plain dark apron as he walks from the dining room
to the server station at the edge of the room and lifts one white wipe from the open bucket — the
walk is the subject, not the product.
Beat 3 (7–14s): he returns to the vacated four-top, clears the plates and glassware, wipes the
tabletop once in a single smooth pass, sets the top back with cutlery and a small candle, and
nods to the host. This is the heart of the shot: calm, practised, one pass, no second trip.
Beat 4 (14–18s): the camera settles into a static medium-wide; several tables are being reset
around him and the room keeps moving, efficient and under control. Keep the lower third of the
frame visually quiet.
Beat 5 (18–22s): close but editorial — the busser's hands set the tabletop back with cutlery;
no face, no product demo, no cleaning close-up.
Beat 6 (22–25s): the camera settles back into the opening wide framing with the reset table now
occupied by two seated guests, the host walking away, the room still moving behind.

CAPTIONS: small clean white sans-serif captions, letter-spaced, in the lower third, fading in and
out gently, one at a time, no boxes or backgrounds:
"Every dirty minute is a seat you already paid for." (0–3s)
"The cost isn't the wipe. It's the trip." (3–7s)
"Clear · Clean · Reset · Seat" (7–14s)
"$0.09 a wipe · $0.29 a table · under 90 seconds" (14–18s)
"One consumable. Already at the table." (18–22s)
"Reduce Table Turnover Time." (22–25s)

Must NOT contain: any text or logo on the bucket or packaging; any spray bottle, cloth or
cleaning-product close-up; water droplets, sparkle or streak effects; any implication of cleaning
performance or hygiene; any on-screen superlative such as "best", "safe" or "food-safe". The last
frame must match the framing of the first frame so the video loops seamlessly. Muted, no audio.
```

---

## 2. DEPOIS DE GERAR — 3 conferências (2 minutos)

1. **A letra das cartelas.** Se as legendas saírem deformadas (comum), gere de novo com o prompt
   **sem o bloco `CAPTIONS:`** e adicione os 6 textos na timeline do Genspark em ~2 min — fonte
   Raleway, branco, terço inferior. O vídeo sai igual; só o texto fica limpo.
2. **O rótulo do balde.** Se o modelo inventou uma marca na embalagem, regenere — nenhuma imagem
   de marca nossa é autorizada no blog (a seção é *editorial media only*).
3. **O loop.** O último frame tem de casar com o primeiro. Se não casar, peça "end on the same wide
   framing as the opening" ou ajuste o corte final na timeline.

---

## 3. EXPORT & UPLOAD

- 16:9 · 1920×1080 · **sem faixa de áudio** · **< 30 MB** · 22–25 s
- Upload: Shopify → Content → Files → MP4 → theme editor → seção *Wipex Cost Per Table* → campo
  **Lifestyle video**
- Fallback 16:9: exporte um still do primeiro frame em 1600×900 e suba em **Video fallback image**
  (alt: `Busser resetting a table in a busy restaurant dining room during service`)
- Overlay do editor (hoje vazio): heading `Reduce Table Turnover Time` · texto `Set your cost per
  table first, then decide what to change.` · CTA `Shop Table Bussers®` →
  `https://wipex.co/products/table-bussers-surface-wipes`

---

*Wipex — Facility Supply Team · prompt único · blog #1 "Cost per table" · 2026*
