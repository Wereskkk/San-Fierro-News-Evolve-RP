#!/usr/bin/env python3
"""SFN: сборщик выпуска 03.10.2026 (v7, композиционная правка harbor-poster).
Дизайн: SFN-DESIGN-029, слаг graphite-press (бриф главреда от 04.10.2026:
графитовый фон сайта vs кремовые листы с границей и тенью; намеренное свободное пространство;
КПП — полноценный боковой материал с цветной полосой вместо пунктирной рамки;
асимметричные сетки, у каждой полосы своя композиция; секционные заголовки НЕ тронуты).
Содержание импортируется из сборщика v6 без правок. Фото: width:100% + height:auto.
Выход: anna-malboro/daily-03-10-2026.html (очередь подшивки).
Запуск из корня:  python3 worktmp/build_daily_0310_state_v7.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V6 = os.path.join(ROOT, 'worktmp', 'build_daily_0310_state_v6.py')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')

src = open(V6, encoding='utf-8').read()
src = src.replace("OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')",
                  "OUT = os.devnull")
ns = {'__name__': 'sfn_v6_data', '__file__': V6}
exec(compile(src, V6, 'exec'), ns)
IMG, A = ns['IMG'], ns['A']

IDX = {'fallen': '01', 'crash': '02', 'gas': '03', 'kpp': '04', 'truck': '05', 'square': '06',
       'stop': '07', 'hwy': '08', 'dragons': '09', 'caligula': '10', 'heli': '11', 'yacht': '12'}

CSS = """/* SFN-DESIGN-029: graphite-press · 03.10.2026 */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=PT+Sans:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%}
:root{--field:#16324f;--field2:#1d3f61;--paper:#f5f0e4;--tint:#e7e1d2;--ink:#14181c;
--mut:#6b665c;--amber:#d97b29;--line:#cfc7b4;--grafit:#37332c}
body{background:var(--grafit);color:var(--ink);font-family:"PT Serif",Georgia,serif;
-webkit-font-size-adjust:100%;padding:36px 14px 74px;
background-image:radial-gradient(rgba(255,255,255,.035) 1px,transparent 1px);background-size:24px 24px}
.be{font-family:"Bebas Neue","Oswald",Arial,sans-serif;font-weight:400;letter-spacing:.015em}
.sv{font-family:"PT Sans",Arial,sans-serif}
/* ---- лист: физическая бумага на графите ---- */
.sheet{max-width:1120px;margin:0 auto 46px;background:var(--paper);padding:0 0 38px;
border:1px solid #b9b09c;box-shadow:0 22px 48px rgba(12,10,8,.55),0 4px 12px rgba(12,10,8,.35);
position:relative}
.inner{padding:0 46px}
/* ---- folio ---- */
.folio{display:flex;justify-content:space-between;gap:14px;align-items:baseline;
padding:10px 46px;border-bottom:1px solid var(--line);
font-family:"PT Sans",sans-serif;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--mut)}
.folio b{color:var(--field);font-weight:700}
.folio .pgno{font-family:"Bebas Neue",sans-serif;font-size:16px;letter-spacing:.08em;color:var(--amber)}
/* ---- цветовое поле обложки ---- */
.field{background:var(--field);color:var(--paper);padding:34px 46px 40px;margin-bottom:30px}
.field .kicker{color:var(--amber)}
.field .stand{color:#c8d2dc}
.field figcaption{color:#aeb9c4}
.mast{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;margin-bottom:26px}
.brand{font-family:"Bebas Neue",sans-serif;line-height:.86;color:var(--paper)}
.brand .l1{display:block;font-size:clamp(52px,8vw,92px)}
.brand .l2{display:block;font-size:clamp(52px,8vw,92px);color:var(--amber)}
.mastmeta{text-align:right;font-family:"PT Sans",sans-serif;font-size:10.5px;line-height:1.75;
letter-spacing:.14em;text-transform:uppercase;color:#c8d2dc}
.mastmeta b{color:var(--amber)}
/* ---- заголовки (система v6, без изменений) ---- */
.kicker{font-family:"PT Sans",sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.26em;
text-transform:uppercase;color:var(--amber);margin-bottom:8px}
.kicker .idx{color:var(--field);background:var(--tint);padding:1px 6px;margin-right:8px;
font-family:"Bebas Neue",sans-serif;font-size:13px;letter-spacing:.1em}
.field .kicker .idx{background:var(--field2);color:var(--amber)}
h1,h3{font-family:"Bebas Neue",sans-serif;font-weight:400;line-height:.94;letter-spacing:.01em}
h1{font-size:clamp(40px,6vw,74px);margin-bottom:12px}
h1 .md{display:block;font-size:.62em}
h1 .xl{display:block;font-size:1em;color:var(--amber)}
h3{font-size:clamp(21px,2.4vw,30px);line-height:1;margin-bottom:8px}
.stand{font-style:italic;color:var(--mut);font-size:14px;line-height:1.55;margin-bottom:10px}
.txt p{margin:0 0 8px;line-height:1.66;font-size:14.5px}
figure{margin:0 0 10px}
.ph img{width:100%;height:auto;transition:filter .45s}
.ph:hover img{filter:contrast(1.04)}
figcaption{margin-top:5px;font-family:"PT Sans",sans-serif;font-size:10.5px;line-height:1.5;color:var(--mut)}
/* ---- рубрики-плакаты (НЕ тронуты по требованию главреда) ---- */
.sect{display:flex;align-items:flex-end;gap:20px;margin:34px 0 24px;padding:0 46px}
.sect .num{font-family:"Bebas Neue",sans-serif;font-size:96px;line-height:.78;color:transparent;
-webkit-text-stroke:1.6px var(--field);opacity:.85}
.sect h2{font-family:"Bebas Neue",sans-serif;font-size:clamp(34px,5vw,60px);line-height:.9;
color:var(--field);letter-spacing:.02em}
.sect .tail{flex:1;border-bottom:3px solid var(--field);margin-bottom:10px}
.sect .date{font-family:"PT Sans",sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--mut);margin-bottom:12px}
/* ---- сетки: асимметрия, у каждой полосы своя ---- */
.g66{display:grid;grid-template-columns:1fr 1fr;gap:34px;align-items:start}
.g75{display:grid;grid-template-columns:7fr 5fr;gap:34px;align-items:start}
.g57{display:grid;grid-template-columns:5fr 7fr;gap:34px;align-items:start}
.g48{display:grid;grid-template-columns:4fr 8fr;gap:26px;align-items:start}
.r84{display:grid;grid-template-columns:8fr 4fr;gap:30px;align-items:start}
.r48{display:grid;grid-template-columns:4fr 8fr;gap:30px;align-items:start}
.r75{display:grid;grid-template-columns:7fr 5fr;gap:30px;align-items:start}
/* ---- боковой материал с цветной полосой (КПП) ---- */
.sidebar{border-left:4px solid var(--field);padding:4px 0 4px 24px;margin-top:28px;
border-top:1px solid var(--line);padding-top:20px}
/* ---- служебные блоки ---- */
.bignum{font-family:"Bebas Neue",sans-serif;font-size:40px;line-height:.9;color:var(--field);margin:4px 0 6px}
.bignum small{display:block;font-family:"PT Sans",sans-serif;font-weight:700;font-size:9.5px;
letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}
.bluebox{background:var(--field);color:var(--paper);padding:22px 24px}
.bluebox .kicker{color:var(--amber)}
.bluebox .kicker .idx{background:var(--field2);color:var(--amber)}
.bluebox .stand{color:#c8d2dc}
.bluebox .txt p{color:#e8edf2}
.bluebox figcaption{color:#aeb9c4}
.tintbox{background:var(--tint);padding:22px 24px}
.wide{margin:0 0 12px}
.wide img{width:100%;height:auto}
.ruleline{border-top:3px solid var(--field);margin:26px 0 20px}
.amberline{border-top:3px solid var(--amber);margin:10px 0 12px;width:74px}
/* ---- намеренная служебная строка внизу первой полосы ---- */
.pressline{display:flex;justify-content:space-between;align-items:baseline;gap:18px;flex-wrap:wrap;
border-top:3px solid var(--field);margin:30px 46px 0;padding-top:12px}
.pressline .be{font-size:23px;color:var(--field);letter-spacing:.05em}
.pressline .be i{font-style:normal;color:var(--amber)}
.pressline .sv{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
/* ---- подвал ---- */
.colophon{background:var(--field);color:var(--paper);margin-top:34px;padding:22px 46px 26px;
display:flex;justify-content:space-between;gap:24px;align-items:center;flex-wrap:wrap}
.colophon .credits{font-family:"PT Sans",sans-serif;font-size:11px;letter-spacing:.08em}
.colophon .made{margin-top:4px;font-family:"PT Sans",sans-serif;font-size:10px;
letter-spacing:.12em;color:#aeb9c4}
.backpill{display:inline-block;padding:9px 20px;border:1.5px solid var(--amber);border-radius:999px;
color:var(--amber);font-family:"PT Sans",sans-serif;font-weight:700;font-size:12px;letter-spacing:.08em;
text-decoration:none;transition:.25s;white-space:nowrap}
.backpill:hover{background:var(--amber);color:var(--field)}
/* ---- адаптив ---- */
@media(max-width:920px){
 .inner,.sect,.folio,.pressline{padding-left:18px;padding-right:18px;margin-left:0;margin-right:0}
 .field{padding:24px 18px 28px}
 .g66,.g75,.g57,.g48,.r84,.r48,.r75{grid-template-columns:1fr}
 .mast{flex-direction:column;align-items:flex-start}
 .mastmeta{text-align:left}
 .sect .num{font-size:64px}
 .colophon{padding:18px}
 .sheet{margin-bottom:30px}
}
"""


def fig(key, cap, alt):
    return f'<figure><div class="ph"><img src="{IMG[key]}" alt="{alt}"></div><figcaption>{cap}</figcaption></figure>'


def kick(key):
    a = A[key]
    return f'<div class="kicker"><span class="idx">{IDX[key]}</span>{a["k"]}</div>'


def txt(key):
    return '<div class="txt">' + ''.join(f'<p>{p}</p>' for p in A[key]['p']) + '</div>'


def head(key, style=''):
    a = A[key]
    st = f' style="{style}"' if style else ''
    return f'{kick(key)}<h3{st}>{a["t"]}</h3><div class="stand">{a["s"]}</div>'


def folio(no, label):
    return (f'<div class="folio"><span><b>San Fierro News</b> · выпуск № 30 · {label}</span>'
            f'<span>суббота, 3 октября 2026</span><span class="pgno">полоса {no}</span></div>')


def sect(num, name):
    return (f'<div class="sect"><span class="num">{num}</span><h2>{name}</h2>'
            f'<span class="tail"></span><span class="date">03.10.2026</span></div>')


P = []
P.append("""<!DOCTYPE html>
<html lang="ru">
<head>
<!-- © 2026 San Fierro News / Jonny Wilde. Дизайн и вёрстка защищены: CC BY-NC-ND 4.0. Копирование и переработка запрещены. -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>San Fierro News — ежедневный выпуск по штату от 03.10.2026</title>
<meta name="description" content="Ежедневный выпуск по штату San Andreas: гибель двоих полицейских на трассе под Лас-Вентурасом, торги за AngelPine Gas со ставкой $100 млн, военный КПП, вертолёт в тоннеле и яхта в парковом пруду — 12 кадров дня.">
<style>
""")
P.append(CSS)
P.append('</style>\n</head>\n<body>\n')

# ================= ПОЛОСА 1 =================
a = A['fallen']
w = a['t'].split()
c, g, k = A['crash'], A['gas'], A['kpp']
P.append('<section class="sheet">')
P.append('<div class="field">')
P.append('<div class="mast"><div class="brand"><span class="l1">San Fierro</span><span class="l2">News</span></div>'
         '<div class="mastmeta"><span><b>№ 30</b> · ежедневный выпуск</span><br>'
         '<span>Лос-Сантос — Лас-Вентурас — трассы штата</span><br>'
         '<span>12 материалов · 4 полосы · 03.10.2026</span><br>'
         '<span>Кадры: Anna Malboro · Фоторедактор: Sonya Malboro</span><br>'
         '<span>Текст/Редактор: Jonny Wilde</span></div></div>')
P.append(f'<div class="g66"><div>{kick("fallen")}'
         f'<h1><span class="md">{" ".join(w[0:2])}</span> <span class="xl">{" ".join(w[2:4])}</span> '
         f'<span class="md">{" ".join(w[4:])}</span></h1>'
         f'<div class="stand">{a["s"]}</div>{txt("fallen")}</div>'
         f'<div>{fig("fallen", a["cap"], a["alt"])}</div></div>')
P.append('</div>')
P.append('<div class="inner">')
P.append(f'<div class="r84"><article class="g66"><div>{fig("crash", c["cap"], c["alt"])}</div>'
         f'<div>{kick("crash")}<h3>{c["t"]}</h3>{txt("crash")}</div></article>'
         f'<article>{kick("gas")}<h3>{g["t"]}</h3>'
         f'<div class="bignum">$100 000 000<small>предыдущая ставка торгов</small></div>'
         f'{fig("gas", g["cap"], g["alt"])}{txt("gas")}</article></div>')
P.append(f'<article class="sidebar">{kick("kpp")}'
         f'<h3 style="font-size:clamp(26px,3vw,36px);max-width:24em">{k["t"]}</h3>'
         f'<div class="g57" style="gap:26px"><div>{fig("kpp", k["cap"], k["alt"])}</div>'
         f'<div><div class="stand">{k["s"]}</div>{txt("kpp")}</div></div></article>')
P.append('<div class="pressline"><span class="be">Выпуск № 30 · четыре полосы · <i>двенадцать материалов</i></span>'
         '<span class="sv">San Fierro News · ежедневное издание штата San Andreas · 03.10.2026</span></div>')
P.append('</div></section>\n')

# ================= ПОЛОСА 2 =================
t, q, s = A['truck'], A['square'], A['stop']
P.append('<section class="sheet">')
P.append(folio(2, 'происшествия'))
P.append(sect('01', 'Происшествия'))
P.append(f'<div class="inner"><article class="g57"><div>{kick("truck")}<h3>{t["t"]}</h3>'
         f'<div class="stand">{t["s"]}</div><div class="amberline"></div>{txt("truck")}</div>'
         f'<div>{fig("truck", t["cap"], t["alt"])}</div></article>')
P.append(f'<div class="r48" style="margin-top:30px"><article>{fig("square", q["cap"], q["alt"])}'
         f'{kick("square")}<h3>{q["t"]}</h3><div class="stand">{q["s"]}</div>{txt("square")}</article>'
         f'<article>{fig("stop", s["cap"], s["alt"])}{kick("stop")}<h3>{s["t"]}</h3>'
         f'<div class="stand">{s["s"]}</div><div class="amberline"></div>{txt("stop")}</article></div></div></section>\n')

# ================= ПОЛОСА 3 =================
h, d, cc = A['hwy'], A['dragons'], A['caligula']
P.append('<section class="sheet">')
P.append(folio(3, 'криминал · экономика'))
P.append(sect('02', 'Криминал · Экономика'))
P.append(f'<div class="inner"><article>{kick("hwy")}'
         f'<h3 style="font-size:clamp(26px,3.4vw,40px);max-width:22em">{h["t"]}</h3>'
         f'<div class="stand">{h["s"]}</div>'
         f'<figure class="wide"><div class="ph"><img src="{IMG["hwy"]}" alt="{h["alt"]}"></div>'
         f'<figcaption>{h["cap"]}</figcaption></figure>'
         f'<div class="r48"><div class="tintbox" style="padding:14px 16px">'
         f'<span class="bignum" style="font-size:30px">08</span>'
         '<small class="sv" style="font-size:9.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--mut)">материал полосы</small></div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in h['p']) + '</div></div></article>')
P.append(f'<article class="r75" style="margin-top:30px"><div>{fig("dragons", d["cap"], d["alt"])}</div>'
         f'<div class="bluebox">{kick("dragons")}<h3>{d["t"]}</h3><div class="stand">{d["s"]}</div>{txt("dragons")}</div></article>')
P.append(f'<article class="r48" style="margin-top:30px"><div>{fig("caligula", cc["cap"], cc["alt"])}</div>'
         f'<div>{kick("caligula")}<h3>{cc["t"]}</h3><div class="stand">{cc["s"]}</div>'
         f'<div class="amberline"></div>{txt("caligula")}</div></article></div></section>\n')

# ================= ПОЛОСА 4 =================
he, y = A['heli'], A['yacht']
P.append('<section class="sheet">')
P.append(folio(4, 'необычные истории'))
P.append(sect('03', 'Необычные истории'))
P.append(f'<div class="inner"><article class="r75"><div>{fig("heli", he["cap"], he["alt"])}</div>'
         f'<div>{kick("heli")}<h3 style="font-size:clamp(26px,3.2vw,38px)">{he["t"]}</h3>'
         f'<div class="stand">{he["s"]}</div><div class="amberline"></div>{txt("heli")}</div></article>')
P.append(f'<article class="tintbox r84" style="margin-top:30px"><div>{kick("yacht")}<h3>{y["t"]}</h3>'
         f'<div class="stand">{y["s"]}</div>{txt("yacht")}</div>'
         f'<div>{fig("yacht", y["cap"], y["alt"])}</div></article></div>')
P.append('<div class="colophon"><div><div class="credits">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>'
         '<div class="made">выпуск очереди подшивки · 03.10.2026 · дизайн и вёрстка — редакция San Fierro News</div></div>'
         '<a class="backpill" href="newsroom.html">← Посмотреть все выпуски редакции</a></div>')
P.append('</section>\n')

P.append('<!-- SFN · 2026 · 029 · graphite-press -->\n</body>\n</html>\n')

html = ''.join(P)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
words = sum(len((a['s'] + ' ' + ' '.join(a['p'])).split()) for a in A.values())
print(f'собрано v7: {OUT} · {len(html)//1024} КБ · полос: 4 · кадров: {len(IMG)} · слов: {words}')
