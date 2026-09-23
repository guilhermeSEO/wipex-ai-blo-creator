#!/usr/bin/env python3
"""
Wipex — content calendar builder.

Turns a list of occasions, measured demand peaks and evergreen topics into a dated calendar,
then VALIDATES it instead of trusting it.

DATE RULES (owner-set, see references/02 §6)
  occasion post  -> publish 7 days before the occasion (accepted band 5-10)
  measured peak  -> publish 14-28 days before the peak window opens (use 18-24 in practice)
  evergreen post -> fills the remaining capacity, max 4 posts/week, max 1 post/day

The script refuses to place a post whose derived date is already in the past, de-collides
same-day collisions (a peak beats an occasion), and prints an ISSUES list at the end. If
ISSUES is empty, the calendar is internally consistent.

EDIT AT THE TOP, not in the body:
  TODAY / YEAR_END   the window
  OCCASIONS          (occasion_date, name, title, keyword cluster, product family, note)
  PEAK_POSTS         (next peak date, lead days, name, title, keyword, product)
  LATER_PEAKS        peaks whose window falls outside this calendar
  EVERGREEN          (title, keyword, product, rationale)

Then: python build_content_calendar.py
Writes CALENDAR_<year>_Q<n>.md and .csv into the workdir's 04-data folder.
Re-verify the occasion dates against a calendar each quarter — they move.
"""
import csv, os
from datetime import date, timedelta
from collections import Counter, defaultdict

OUT = r"C:\Users\guilh\AppData\Local\hermes\workdir\wipex\04-data"
TODAY = date(2026, 9, 22)
YEAR_END = date(2026, 12, 31)
OCC_LEAD = 7      # dias antes da ocasiao (regra: 5-10)
PEAK_LEAD = 21    # dias antes do inicio do pico (regra: 14-28)
issues = []       # coletados durante a construcao e a validacao

# (titulo, keyword cluster, familia de produto, nota)
# ---- OCASIAO: data verificada + 7 dias de antecedencia
OCCASIONS = [
 ("2026-10-02","National Custodial Workers Day","The Custodial Team Carries the Building: A Frontline Readiness Guide","custodial staff / cleaning protocol","dispensers + all-purpose wipes","occasion: workforce recognition"),
 ("2026-10-04","Fire Prevention Week","Fire Prevention Week: What Wipes Can and Cannot Do in a Kitchen","kitchen safety / surface cleaning","Table Bussers (NSF-listed SKU)","occasion: compliance-safe framing, no germ-kill"),
 ("2026-10-12","Indigenous Peoples' Day","Holiday Roster, Full Standard: Running a Facility With Skeleton Staff","holiday staffing / readiness","refill rolls + dispensers","occasion: US federal holiday"),
 ("2026-10-15","Global Handwashing Day","Global Handwashing Day: Hygiene That Holds Up in Busy Facilities","handwashing / hygiene","EMBODY + skin wipes","occasion: skin-compliant wording only"),
 ("2026-10-16","World Food Day","World Food Day: Front-of-House Cleaning in Food Service Environments","food service surfaces","Table Bussers Autumn + Unscented","occasion: NSF wording on Autumn only"),
 ("2026-10-20","Cybersecurity Awareness Month","What to Use on Shared Devices: A Facility Guide to Screens and Keyboards","touchscreen / electronics","touchscreen + 70% IPA wipes","occasion: October is Cybersecurity Awareness Month"),
 ("2026-10-31","Halloween","Halloween Recovery: Sticky Surfaces, Spills and the Morning After","event cleanup","all-purpose + floor wipes","occasion: high-traffic event"),
 ("2026-11-01","Daylight Saving ends","Falling Back: The Weekend the Clocks Change and Facilities Reset","DST / seasonal reset","floor + surface wipes","occasion: operational reset"),
 ("2026-11-02","Dia de los Muertos","Dia de los Muertos Hospitality: Preparing Guest-Facing Spaces","hospitality surfaces","Table Bussers Autumn","occasion: LatAm tradition, CA/TX/FL"),
 ("2026-11-03","US Election Day","Election Day Facility Plan: Traffic, Staffing and Reset","event traffic / staffing","all-purpose + dispensers","occasion: midterms"),
 ("2026-11-08","Diwali","Diwali Hospitality: Preparing Guest Spaces for the Festival of Lights","hospitality surfaces","Table Bussers Autumn","occasion: religious, seasonal scent fit"),
 ("2026-11-11","Veterans Day","Veterans Day Roster: Standards That Hold With a Short Crew","holiday staffing","refill rolls + dispensers","occasion: US federal holiday"),
 ("2026-11-15","America Recycles Day","America Recycles Day: Cutting Wipe Waste Without Cutting Coverage","waste reduction / refills","refill + dispenser system","occasion: environmental, Eco wording"),
 ("2026-11-19","World Toilet Day","World Toilet Day: Washroom Standards in Commercial Facilities","washroom / sanitation","floor wipes + EPA disinfecting","occasion: EPA label wording only"),
 ("2026-11-26","Thanksgiving","Thanksgiving Week: What Hospitality Actually Burns Through","food service demand","Table Bussers + bulk","occasion: peak hospitality volume"),
 ("2026-11-27","Buy Nothing Day","Buy Nothing Day: Buying Less, Using Better (a Refill Case Study)","consumption / refills","refill rolls + dispensers","occasion: environmental counter-position"),
 ("2026-11-28","Small Business Saturday","Small Business Saturday: A Cleaning Plan That Fits One Store","SMB buying","buckets + bundles","occasion: SMB buyer"),
 ("2026-11-30","Cyber Monday","Cyber Monday Logistics: Getting Supplies Delivered Before the Holidays","delivery / lead times","bulk cases","occasion: e-commerce"),
 ("2026-12-01","Handwashing Awareness Week","Handwashing Awareness Week: Hygiene Stations That Actually Get Used","hygiene stations","EMBODY + skin wipes + dispensers","occasion: health-compliant"),
 ("2026-12-04","Hanukkah begins","Hanukkah-Ready Hospitality: Preparing Guest Spaces for Eight Nights","hospitality surfaces","Table Bussers + floor wipes","occasion: religious"),
 ("2026-12-08","Bodhi Day","Bodhi Day and the Calmer Space: Studio Hygiene as Practice","studio / wellness","EMPOWER + odor eliminator","occasion: religious, studio buyer"),
 ("2026-12-16","Las Posadas","Las Posadas Season: Hospitality Cleaning in CA, TX and FL Venues","hospitality / GEO","Table Bussers + all-purpose","occasion: religious, GEO-native (CA/TX/FL)"),
 ("2026-12-21","Winter Solstice","Winter Solstice: The Longest Night and the Deepest Clean","year-end deep clean","floor + surface + full range","occasion: seasonal"),
 ("2026-12-25","Christmas","Christmas Week Operations: Skeleton Crews, Full Standards","holiday operations","dispensers + refills","occasion: US federal holiday"),
 ("2026-12-26","Boxing Day / Kwanzaa","Kwanzaa and Ujamaa: Cooperative Economics for Small Operators","values / SMB","bundles + buckets","occasion: Kwanzaa Dec 26-Jan 1"),
 ("2026-12-31","New Year's Eve","Year-End Close: What to Log So Next Q4 Is Easier","records / planning","all families","occasion: calendar close"),
]

# ---- PICO medido: (data do PROXIMO pico, lead em dias dentro da faixa 14-28)
PEAK_POSTS = [
 ("2026-11-16",21,"office cleaning 2nd peak","Office Cleaning Reset: High-Touch Surfaces in Shared Workspaces","office cleaning / high-touch","IPA + touchscreen wipes"),
 ("2026-11-30",24,"cost per use peak","Cost Per Use, Recomputed for 2027: The Number Your Budget Needs","cost per use","buckets / rolls / cases"),
 ("2026-11-30",21,"holiday cleaning peak","Holiday Cleaning Program: A 6-Week Front-of-House Plan","holiday cleaning","Table Bussers + floor wipes"),
 ("2026-12-28",24,"new year gym peak","January Is Coming: The Facility Reset Nobody Schedules","new year gym / resolution","fitness family + refreshes"),
 ("2026-12-28",21,"flu season peak (Dec 28 - Jan 10)","Flu Season Readiness: A Surface Routine That Survives the Peak","flu season / high-touch","EPA disinfecting + all-purpose"),
 ("2026-12-28",18,"new year resolution peak","The New-Year Reset: A 30-Day Facility Plan for January Traffic","resolution / january traffic","fitness + floor + surface"),
]

# peaks whose next occurrence falls OUTSIDE this calendar (their publish window is Jan-Mar 2027)
LATER_PEAKS = [
 ("winter cleaning", "Feb 15-21 (100) / Feb 8-14 (96)", "Feb", "Jan 11 - Jan 25", "Winter Floor Care: Salt, Slush and the Damage Window"),
 ("salt stains", "Jan 25-31 (100) / Feb 1-7 (88)", "late Jan - Feb", "Jan 4 - Jan 18", "winter floor prep (same post)"),
 ("mold prevention", "Apr 5-11 (100) / Mar 15-21 (99)", "Mar - Apr", "Feb 15 - Mar 15", "Mold Prevention Before the Spring Thaw"),
]

# ---- EVERGREEN / COMERCIAL: termos de base alta, aceitam qualquer mes
EVERGREEN = [
 ("Facility Cleaning Par Levels: How to Stop Running Out Mid-Shift","facility cleaning / par level","Natural Gym Wipes 400ct buckets + 700ct refills","operational, high baseline"),
 ("Wipes vs Paper Towels vs Reusable Cloths: The Coverage Math","coverage per wipe / cost per table","Table Bussers + bulk rolls","cost math, no performance claim"),
 ("Q4 Facility Reset: The 6-Point Program Review Before Budgets Close","facility cleaning program","fitness + food-service families","operational, Q4 trigger"),
 ("One Wipe Per Station: Designing a Floors-and-Surfaces Route","surface cleaning route","all-purpose + floor wipes","operational, evergreen"),
 ("Where Facilities Actually Overspend on Cleaning Supplies (and the Fix)","overspend / procurement","buckets vs rolls vs refills","commercial, evergreen"),
 ("Choosing Between Buckets, Refills and Dispensers: A Format Decision Matrix","format choice","bucket / 700ct roll / dispenser","commercial, evergreen"),
 ("Q4 Procurement Calendar: Order Dates That Beat the Holiday Crunch","procurement timing","all families","commercial, seasonal"),
 ("Restaurant Supplies in Volume: What Front-of-House Really Consumes","restaurant supplies","Table Bussers + bulk","commercial, highest baseline (60.3)"),
 ("Car Care in Detail: Wipes for Interiors Through the Winter","car detailing","AutoWipes","evergreen, highest 1-m avg (80.4)"),
 ("The October Restock Window: Why Q4 Orders Should Land This Month","bulk ordering / restock","bulk rolls + dispensers","commercial, seasonal"),
 ("Deep Cleaning Without Downtime: Sequencing a Busy Facility","deep cleaning","floor + surface + full range","operational, high baseline (60.6)"),
 ("Damp Corners and Cold Weather: Preventing Moisture Problems","mold prevention / damp","EPA disinfecting + all-purpose","operational, high baseline (57.6)"),
]

# ---------------------------------------------------------------- build
planned = []
for occ, name, title, kw, prod, note in OCCASIONS:
    d = date.fromisoformat(occ) - timedelta(days=OCC_LEAD)
    if d < TODAY:
        d = date.fromisoformat(occ) - timedelta(days=5)   # tighten rather than lose it
    if d < TODAY:
        continue
    planned.append({"date": d, "track": "S", "title": title, "kw": kw, "prod": prod,
                    "hook": f"{name} ({occ})", "why": note, "occ": date.fromisoformat(occ)})
for pk, lead, name, title, kw, prod in PEAK_POSTS:
    d = date.fromisoformat(pk) - timedelta(days=lead)
    if d < TODAY:
        issues.append(f"peak lead pushes before today: {title[:40]}")
        continue
    if d > YEAR_END:
        continue
    planned.append({"date": d, "track": "P", "title": title, "kw": kw, "prod": prod,
                    "hook": name, "why": f"peak {pk}, published {lead}d ahead", "occ": None})
for title, kw, prod, why in EVERGREEN:
    planned.append({"date": None, "track": "E", "title": title, "kw": kw, "prod": prod,
                    "hook": "evergreen", "why": why, "occ": None})

planned.sort(key=lambda x: (x["date"] or date(2099, 1, 1)))

# place evergreen posts into weeks with free capacity (max 4/week, prefer Mon/Wed)
cap = defaultdict(int)
for p in planned:
    if p["date"]:
        ws = p["date"] - timedelta(days=p["date"].weekday())
        cap[ws] += 1
weeks = []
cur = TODAY - timedelta(days=TODAY.weekday())
while cur <= YEAR_END:
    weeks.append(cur); cur += timedelta(days=7)

def monday_of(d): return d - timedelta(days=d.weekday())

# de-collide fixed posts: at most one post per weekday, peaks win over occasions
used = defaultdict(list)
for p in planned:
    if p["date"]:
        used[p["date"]].append(p)
for d, lst in list(used.items()):
    if len(lst) > 1:
        lst.sort(key=lambda x: 0 if x["track"] == "P" else 1)
        for extra in lst[1:]:
            nd = d + timedelta(days=1)
            while nd.weekday() > 4 or nd in used:
                nd += timedelta(days=1)
            extra["date"] = nd
            used[nd].append(extra)
            issues.append(f"de-collided {d} -> {nd}: {extra['title'][:38]}")

fixed_by_week = defaultdict(list)
for p in planned:
    if p["date"]:
        fixed_by_week[monday_of(p["date"])].append(p)

def week_capacity(w):
    used_days = {p["date"] for p in fixed_by_week.get(w, [])}
    free = sum(1 for off in range(5)
               if TODAY <= w + timedelta(days=off) <= YEAR_END
               and (w + timedelta(days=off)) not in used_days)
    return max(0, min(4 - len(fixed_by_week.get(w, [])), free))

# interleave evergreen posts: one per week per pass, chronological, so they spread evenly
pending = [p for p in planned if p["date"] is None]
while pending:
    progressed = False
    for w in weeks:
        if not pending:
            break
        if week_capacity(w) <= 0:
            continue
        p = pending[0]
        used_days = {x["date"] for x in fixed_by_week[w]}
        for off in range(5):
            d = w + timedelta(days=off)
            if TODAY <= d <= YEAR_END and d not in used_days:
                p["date"] = d
                fixed_by_week[w].append(p)
                pending.pop(0)
                progressed = True
                break
    if not progressed:
        break
planned = [p for p in planned if p["date"]]
planned.sort(key=lambda x: x["date"])

by_week = defaultdict(list)
for p in planned:
    by_week[monday_of(p["date"])].append(p)

# ---------------------------------------------------------------- validation
for p in planned:
    if p["occ"]:
        lead = (p["occ"] - p["date"]).days
        if not (5 <= lead <= 10):
            issues.append(f"lead {lead}d: {p['title'][:45]}")
    if not (TODAY <= p["date"] <= YEAR_END):
        issues.append(f"date out of range {p['date']}: {p['title'][:45]}")
titles = [p["title"] for p in planned]
if len(set(titles)) != len(titles):
    issues.append("duplicate titles")
for w in weeks:
    n = len(by_week.get(w, []))
    if n > 4:
        issues.append(f"{w} has {n} posts (cap 4)")

# ---------------------------------------------------------------- write md
md = []
md.append("# WIPEX — CALENDARIO DE CONTEUDO: OUT–DEZ 2026\n")
md.append(f"Gerado {TODAY} · {len(planned)} posts em {len(by_week)} semanas · regra de data aplicada por calculo, nao por olho\n")
md.append("**Regras de data usadas:** post de **ocasiao** publica **7 dias antes** da data (faixa 5–10); post de\n**pico** publica **21 dias antes** do inicio da janela de pico (faixa 14–28); post **evergreen/comercial**\npreenche as lacunas, maximo 2 por dia e 4 por semana.\n")
md.append("Toda data-alvo nasce de **pico medido no Google Trends** ou de **data verificada**. Dias comemorativos\nentram como *ocasiao* (vendem pelo momento) e estao marcados como tal — nao fingem ser demanda de busca.\n")
md.append("---\n")
md.append("## 1. Calendario\n")
md.append("| Sem | Data | Track | Titulo de trabalho | Cluster | Familia | Gatilho | Por que |")
md.append("|---|---|---|---|---|---|---|---|")
for w in weeks:
    for p in sorted(by_week.get(w, []), key=lambda x: x["date"]):
        wk = weeks.index(w) + 1
        md.append(f"| W{wk:02d} | {p['date']} | {p['track']} | {p['title']} | {p['kw']} | {p['prod']} | {p['hook']} | {p['why']} |")
md.append("")
md.append("Track: **S** sazonal/ocasiao · **P** pico medido · **E** evergreen/comercial\n")
md.append("### Semanas leves (≤2 posts) — capacidade intencional\n")
md.append("| Sem | Posts | Motivo |")
md.append("|---|---|---|")
for w in weeks:
    n = len(by_week.get(w, []))
    if n <= 2:
        wk = weeks.index(w) + 1
        span = f"{w} a {w + timedelta(days=6)}"
        if w.month == 12 and w.day >= 21:
            why = "semana de feriado — o runway de janeiro ja foi publicado em 4-10/dez"
        elif n == 0:
            why = "sem ocasiao nem pico; nao se inventa post para preencher"
        else:
            why = "folga proposital: janela para revisao de compliance em lote"
        md.append(f"| W{wk:02d} ({span}) | {n} | {why} |")
md.append("")
md.append("---\n")
md.append("---\n")
md.append("## 2. Datas verificadas (out–dez 2026)\n")
md.append("| Data | Ocasiao | Escopo | Eixo | Publicacao calculada | Lead |")
md.append("|---|---|---|---|---|---|")
seen = set()
for p in sorted([x for x in planned if x["occ"]], key=lambda x: x["occ"]):
    if p["hook"] in seen: continue
    seen.add(p["hook"])
    lead = (p["occ"] - p["date"]).days
    md.append(f"| {p['occ']} | {p['hook'].split(' (')[0]} | calendario | ocasiao | {p['date']} | {lead}d |")
md.append("")
md.append("Fonte: OPM (federal: Columbus/Indigenous 12/out, Veterans 11/nov, Thanksgiving 26/nov, Christmas 25/dez),\ncalendarios de dias de consciencia (America Recycles 15/nov, Handwashing 15/out, Food Day 16/out, Toilet Day 19/nov),\ncalendarios religiosos (Diwali 8/nov, Hanukkah 4–12/dez, Bodhi 8/dez, Kwanzaa 26/dez, Solsticio 21/dez, Las Posadas 16–24/dez),\nvarejo (Black Friday 27/nov, SBS 28/nov, Cyber Monday 30/nov), civico (midterms 3/nov).\n")
md.append("---\n")
md.append("## 3. Picos medidos usados (Google Trends, geo US, 2026-09-22)\n")
md.append("| Termo | avg 12-m | Semanas de pico | Meses | Janela de publicacao | Post do calendario |")
md.append("|---|---|---|---|---|---|")
PEAKS = [
 ("flu season",26.9,"Jan 4-10 (100), Dec 28-Jan 3 (95)","late Dec - mid Jan","Nov 20 - Dec 15","Flu Season Readiness"),
 ("new year gym",13.0,"Dec 28-Jan 3 (100)","Dec 28 - Jan 10","Dec 5 - Dec 20","January Is Coming"),
 ("new year resolution",10.5,"Dec 28-Jan 3 (100), Jan 4-10 (66)","late Dec - mid Jan","Dec 5 - Dec 20","The New-Year Reset"),
 ("holiday cleaning",39.9,"Dec 21-27 (84), Nov 30-Dec 6 (73)","Nov 30 - Dec 27","Nov 2 - Nov 16","Holiday Cleaning Program"),
 ("cost per use",44.3,"Nov 30-Dec 6 (100), Dec 7-13 (90)","late Nov - mid Dec","Nov 1 - Nov 20","Cost Per Use, Recomputed"),
 ("office cleaning",52.8,"Jun 14-20 (100), Nov 16-22 (86)","mid Nov (2nd peak)","Oct 19 - Nov 2","Office Cleaning Reset"),
 ("deep cleaning",60.6,"Apr 5-11 (100)","Mar - Apr","Feb 15 - Mar 15","Deep Cleaning Without Downtime (evergreen slot)"),
 ("restaurant supplies",60.3,"Jun 14-20 (100)","Jun","year-round baseline","Restaurant Supplies in Volume (evergreen slot)"),
 ("car detailing",64.7,"Jun 14-20 (100)","Jun","year-round baseline","Car Care in Detail (evergreen slot)"),
]
for t, avg, top, pk, win, post in PEAKS:
    md.append(f"| {t} | {avg} | {top} | {pk} | {win} | {post} |")
md.append("")
md.append("Indice relativo por termo; medias nao comparaveis entre linhas. Volume absoluto nao existe no Trends.\n")
md.append("---\n")
md.append("## 4. O limite real desta janela\n")
md.append(f"Dos temas medidos, **apenas ~6 tem pico em out–dez**. Os outros picam em **mar–jun** (deep cleaning,\nmold prevention, gym cleaning, gym wipes, food safety, restaurant supplies, car detailing) ou **jan–fev**\n(winter cleaning, salt stains). Publicar tema de abril em outubro violaria a regra de runway.\n")
md.append(f"Por isso os {len(planned)} posts se dividem em:\n")
md.append("| Track | N | Como se sustenta |")
md.append("|---|---|---|")
md.append(f"| S sazonal/ocasiao | {sum(1 for p in planned if p['track']=='S')} | vende pelo momento; sem pico de busca proprio |")
md.append(f"| P pico medido | {sum(1 for p in planned if p['track']=='P')} | casa com a janela medida |")
md.append(f"| E evergreen/comercial | {sum(1 for p in planned if p['track']=='E')} | termos de base alta e estavel |")
md.append("")
md.append("## 5. Decisao pendente: 3 ou 4 por semana\n")
md.append(f"- Este calendario esta em **~3/semana** ({len(planned)} posts). **4/semana** exigiria ~15 posts a mais,\ne o material honesto para isso seria: (a) variantes GEO dos posts de ocasiao (Las Posadas CA/TX/FL),\n(b) refreshes de posts antigos de 2025 em vez de novos, (c) recortes verticais do mesmo tema.\n- **Gargalo:** cada post passa pelo Dean. 45–60 revisoes em 15 semanas pede **revisao em lote**.\n- **Semana de feriado (W10 Thanksgiving, W14 Christmas):** 2 posts em vez de 3 e ganho real de folga.\n")
md.append("## 6. Fora da janela (agendar depois)\n")
md.append("| Tema | Pico | Publicar em |")
md.append("|---|---|---|")
md.append("| table turnover (angulo novo: economia) | fev–abr | meados de janeiro |")
md.append("| deep cleaning, mold prevention | mar–abr | meados de fevereiro |")
md.append("| gym cleaning, gym wipes | abr (+ jun) | inicio de marco |")
md.append("| food safety, restaurant supplies, car detailing | jun | inicio de maio |")
md.append("| table turnover (angulo novo: economia) | fev–abr | meados de janeiro |")
for t, top, pk, win, post in LATER_PEAKS:
    md.append(f"| {t} | {pk} | **{win}** → _fora deste calendario_ |")
md.append("")
md.append("## 7. Como cada slot entra no skill\n")
md.append("Para cada post: preencher `references/01` com `topic` + `calendar_hook` + `target_buyer` + `angle` +\n`products` + `cta`, e deixar o `publish_target` ser **derivado** pelo Agent 1A. Gate 2 aprova\nkeyword + produto + angulo + data. Declarar o `ANGLE DELTA` contra os posts de ago–set e obrigatorio\n— em especial contra `table-busser-restaurant-efficiency`, `gym-wipe-dispenser-vs-bucket` e\n`buy-cleaning-wipes-in-bulk`.\n")

open(os.path.join(OUT, "CALENDAR_2026_Q4.md"), "w", encoding="utf-8").write("\n".join(md))
with open(os.path.join(OUT, "CALENDAR_2026_Q4.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["week","publish_date","track","title","keyword_cluster","product_family","hook","rationale","occasion_date","lead_days"])
    for p in planned:
        wk = weeks.index(monday_of(p["date"])) + 1
        lead = (p["occ"] - p["date"]).days if p["occ"] else ""
        w.writerow([f"W{wk:02d}", p["date"], p["track"], p["title"], p["kw"], p["prod"], p["hook"], p["why"], p["occ"] or "", lead])

print("posts:", len(planned), "| semanas com conteudo:", len(by_week))
print("tracks:", dict(Counter(p["track"] for p in planned)))
print("por semana:", {weeks.index(w)+1: len(by_week.get(w, [])) for w in weeks})
print("first:", planned[0]["date"], planned[0]["title"][:45])
print("last :", planned[-1]["date"], planned[-1]["title"][:45])
print("\nISSUES:", issues if issues else "nenhuma")
print("WROTE", OUT)