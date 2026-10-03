#!/usr/bin/env python3
"""SFN: сборщик выпуска 03.10.2026 (v8, арт-дирекция композиций, оболочка v6).
Дизайн: SFN-DESIGN-029, слаг artdesk (бриф главреда от 04.10.2026:
внешняя среда и оболочка — КАК ДО v7 (кремовый фон сайта, листы 1120px с тенью без границ);
секционные заголовки не тронуты; переделаны ТОЛЬКО статьи и их взаимодействие:
у каждого материала собственная композиция по его редакционному весу; КПП — газетная
колонка с колонными линейками вместо карточки; пустота используется намеренно).
Содержание импортируется из сборщика v7 без правок. Фото: width:100% + height:auto.
Выход: anna-malboro/daily-03-10-2026.html (очередь подшивки).
Запуск из корня:  python3 worktmp/build_daily_0310_state_v8.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V7 = os.path.join(ROOT, 'worktmp', 'build_daily_0310_state_v7.py')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')

src = open(V7, encoding='utf-8').read()
src = src.replace("OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')",
                  "OUT = os.devnull")
ns = {'__name__': 'sfn_v7_data', '__file__': V7}
exec(compile(src, V7, 'exec'), ns)
IMG, A = ns['IMG'], ns['A']

IDX = {'fallen': '01', 'crash': '02', 'gas': '03', 'kpp': '04', 'truck': '05', 'square': '06',
       'stop': '07', 'hwy': '08', 'dragons': '09', 'caligula': '10', 'heli': '11', 'yacht': '12'}

CSS = """/* SFN-DESIGN-029: artdesk · 03.10.2026 */
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=PT+Sans:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%}
:root{--field:#16324f;--field2:#1d3f61;--paper:#f2ede3;--tint:#e7e1d2;--ink:#14181c;
--mut:#6b665c;--amber:#d97b29;--line:#cfc7b4}
/* ---- внешняя среда: КАК ДО v7, не тронута ---- */
body{background:var(--paper);color:var(--ink);font-family:"PT Serif",Georgia,serif;
-webkit-font-size-adjust:100%;padding:0 0 60px}
.be{font-family:"Bebas Neue","Oswald",Arial,sans-serif;font-weight:400;letter-spacing:.015em}
.sv{font-family:"PT Sans",Arial,sans-serif}
.sheet{max-width:1120px;margin:0 auto 26px;background:var(--paper);padding:0 0 40px;
box-shadow:0 16px 40px rgba(20,24,28,.22);position:relative}
.sheet+.sheet{margin-top:34px}
.inner{padding:0 46px}
.folio{display:flex;justify-content:space-between;gap:14px;align-items:baseline;
padding:10px 46px;border-bottom:1px solid var(--line);
font-family:"PT Sans",sans-serif;font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--mut)}
.folio b{color:var(--field);font-weight:700}
.folio .pgno{font-family:"Bebas Neue",sans-serif;font-size:16px;letter-spacing:.08em;color:var(--amber)}
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
/* ---- типографика материалов ---- */
.kicker{font-family:"PT Sans",sans-serif;font-weight:700;font-size:10.5px;letter-spacing:.26em;
text-transform:uppercase;color:var(--amber);margin-bottom:8px}
.kicker .idx{color:var(--field);background:var(--tint);padding:1px 6px;margin-right:8px;
font-family:"Bebas Neue",sans-serif;font-size:13px;letter-spacing:.1em}
.field .kicker .idx{background:var(--field2);color:var(--amber)}
h1,h3{font-family:"Bebas Neue",sans-serif;font-weight:400;line-height:.94;letter-spacing:.01em}
h1{font-size:clamp(34px,4.6vw,56px);margin-bottom:12px}
h1 .md{display:block;font-size:.66em}
h1 .xl{display:block;font-size:1em;color:var(--amber)}
h3{font-size:clamp(21px,2.4vw,30px);line-height:1;margin-bottom:8px}
.stand{font-style:italic;color:var(--mut);font-size:14px;line-height:1.55;margin-bottom:10px}
.txt p{margin:0 0 8px;line-height:1.66;font-size:14.5px}
figure{margin:0 0 10px}
.ph img{width:100%;height:auto;transition:filter .45s}
.ph:hover img{filter:contrast(1.04)}
figcaption{margin-top:5px;font-family:"PT Sans",sans-serif;font-size:10.5px;line-height:1.5;color:var(--mut)}
/* ---- секции: НЕ тронуты ---- */
.sect{display:flex;align-items:flex-end;gap:20px;margin:34px 0 24px;padding:0 46px}
.sect .num{font-family:"Bebas Neue",sans-serif;font-size:96px;line-height:.78;color:transparent;
-webkit-text-stroke:1.6px var(--field);opacity:.85}
.sect h2{font-family:"Bebas Neue",sans-serif;font-size:clamp(34px,5vw,60px);line-height:.9;
color:var(--field);letter-spacing:.02em}
.sect .tail{flex:1;border-bottom:3px solid var(--field);margin-bottom:10px}
.sect .date{font-family:"PT Sans",sans-serif;font-size:10px;letter-spacing:.2em;
text-transform:uppercase;color:var(--mut);margin-bottom:12px}
/* ---- композиционные классы v8 (у каждого материала свои) ---- */
.lockup{border-top:3px solid var(--paper);border-bottom:1px solid rgba(242,237,227,.4);
padding:20px 0 6px;display:grid;grid-template-columns:6fr 6fr;gap:34px;align-items:start}
.band{display:grid;grid-template-columns:7fr 5fr;gap:32px;align-items:start;
border-top:1px solid var(--line);margin-top:24px;padding-top:20px}
.strip{display:grid;grid-template-columns:4fr 6fr;gap:22px;align-items:start}
.colsband{display:grid;grid-template-columns:3fr 4fr 5fr;gap:0;align-items:start;
border-top:3px solid var(--field);margin-top:26px;padding-top:18px}
.colsband>div{padding:0 24px;border-left:1px solid var(--line)}
.colsband>div:first-child{padding-left:0;border-left:none}
.g84{display:grid;grid-template-columns:8fr 4fr;gap:32px;align-items:start}
.g39{display:grid;grid-template-columns:3fr 9fr;gap:30px;align-items:start}
.briefline{display:grid;grid-template-columns:2fr 10fr;gap:22px;align-items:start;
border-top:1px solid var(--line);margin-top:24px;padding-top:16px}
.vert{border-left:3px solid var(--amber);padding-left:16px}
.g75t{display:grid;grid-template-columns:7fr 5fr;gap:30px;align-items:start}
.cols2{columns:2;column-gap:24px;column-rule:1px solid var(--line)}
.cols2 p,.cols3 p{margin:0 0 8px;line-height:1.66;font-size:14.5px}
.cols3{columns:3;column-gap:22px;column-rule:1px solid var(--line)}
.duo{display:grid;grid-template-columns:5fr 7fr;gap:0;align-items:start;margin-top:28px}
.duo>article{padding:0 28px;border-left:1px solid var(--line)}
.duo>article:first-child{padding-left:0;border-left:none}
.wide{margin:0 0 12px}
.wide img{width:100%;height:auto}
.amberline{border-top:3px solid var(--amber);margin:10px 0 12px;width:74px}
.bignum{font-family:"Bebas Neue",sans-serif;font-size:40px;line-height:.9;color:var(--field);margin:4px 0 6px}
.bignum small{display:block;font-family:"PT Sans",sans-serif;font-weight:700;font-size:9.5px;
letter-spacing:.2em;text-transform:uppercase;color:var(--mut)}
.pause{display:flex;flex-direction:column;justify-content:flex-start;gap:6px}
.ghost{font-family:"Bebas Neue",sans-serif;font-size:150px;line-height:.8;color:transparent;
-webkit-text-stroke:1.5px var(--field);opacity:.5}
.pause .sv{font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.marg{display:grid;grid-template-columns:7fr 5fr;gap:34px;align-items:start;margin-top:30px}
.pressline{display:flex;justify-content:space-between;align-items:baseline;gap:18px;flex-wrap:wrap;
border-top:3px solid var(--field);margin:30px 46px 0;padding-top:12px}
.pressline .be{font-size:23px;color:var(--field);letter-spacing:.05em}
.pressline .be i{font-style:normal;color:var(--amber)}
.pressline .sv{font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.colophon{background:var(--field);color:var(--paper);margin-top:34px;padding:22px 46px 26px;
display:flex;justify-content:space-between;gap:24px;align-items:center;flex-wrap:wrap}
.colophon .credits{font-family:"PT Sans",sans-serif;font-size:11px;letter-spacing:.08em}
.colophon .made{margin-top:4px;font-family:"PT Sans",sans-serif;font-size:10px;
letter-spacing:.12em;color:#aeb9c4}
.backpill{display:inline-block;padding:9px 20px;border:1.5px solid var(--amber);border-radius:999px;
color:var(--amber);font-family:"PT Sans",sans-serif;font-weight:700;font-size:12px;letter-spacing:.08em;
text-decoration:none;transition:.25s;white-space:nowrap}
.backpill:hover{background:var(--amber);color:var(--field)}
@media(max-width:920px){
 .inner,.sect,.folio,.pressline{padding-left:18px;padding-right:18px;margin-left:0;margin-right:0}
 .field{padding:24px 18px 28px}
 .lockup,.band,.strip,.colsband,.g84,.g39,.briefline,.g75t,.duo,.marg{grid-template-columns:1fr}
 .colsband>div{border-left:none;padding:0 0 18px}
 .duo>article{border-left:none;padding:0 0 18px}
 .cols2,.cols3{columns:1}
 .mast{flex-direction:column;align-items:flex-start}
 .mastmeta{text-align:left}
 .sect .num{font-size:64px}
 .ghost{font-size:90px}
 .colophon{padding:18px}
}
"""


def fig(key, cap, alt):
    return f'<figure><div class="ph"><img src="{IMG[key]}" alt="{alt}"></div><figcaption>{cap}</figcaption></figure>'


def kick(key):
    return f'<div class="kicker"><span class="idx">{IDX[key]}</span>{A[key]["k"]}</div>'


def txt(key, cls='txt'):
    return f'<div class="{cls}">' + ''.join(f'<p>{p}</p>' for p in A[key]['p']) + '</div>'


def hd(key, style=''):
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

# ================= ПОЛОСА 1: лок-ап + лента + типографический блок + колонка КПП =================
a, c, g, k = A['fallen'], A['crash'], A['gas'], A['kpp']
w = a['t'].split()
P.append('<section class="sheet">')
P.append('<div class="field">')
P.append('<div class="mast"><div class="brand"><span class="l1">San Fierro</span><span class="l2">News</span></div>'
         '<div class="mastmeta"><span><b>№ 30</b> · ежедневный выпуск</span><br>'
         '<span>Лос-Сантос — Лас-Вентурас — трассы штата</span><br>'
         '<span>12 материалов · 4 полосы · 03.10.2026</span><br>'
         '<span>Кадры: Anna Malboro · Фоторедактор: Sonya Malboro</span><br>'
         '<span>Текст/Редактор: Jonny Wilde</span></div></div>')
P.append(f'<div class="lockup"><div>{kick("fallen")}'
         f'<h1><span class="md">{" ".join(w[0:2])}</span> <span class="xl">{" ".join(w[2:4])}</span> '
         f'<span class="md">{" ".join(w[4:])}</span></h1>'
         f'<div class="stand">{a["s"]}</div>{txt("fallen")}</div>'
         f'<div>{fig("fallen", a["cap"], a["alt"])}</div></div>')
P.append('</div>')
P.append('<div class="inner">')
P.append(f'<div class="band"><article class="strip"><div>{fig("crash", c["cap"], c["alt"])}</div>'
         f'<div>{kick("crash")}<h3>{c["t"]}</h3>{txt("crash")}</div></article>'
         f'<article>{kick("gas")}<h3>{g["t"]}</h3>'
         f'<div class="bignum">$100 000 000<small>предыдущая ставка торгов</small></div>'
         f'{txt("gas")}{fig("gas", g["cap"], g["alt"])}</article></div>')
P.append(f'<div class="colsband"><div>{fig("kpp", k["cap"], k["alt"])}</div>'
         f'<div>{kick("kpp")}<h3 style="font-size:clamp(24px,2.6vw,32px)">{k["t"]}</h3></div>'
         f'<div><div class="stand">{k["s"]}</div>{txt("kpp")}</div></div>')
P.append('<div class="pressline"><span class="be">Выпуск № 30 · четыре полосы · <i>двенадцать материалов</i></span>'
         '<span class="sv">San Fierro News · ежедневное издание штата San Andreas · 03.10.2026</span></div>')
P.append('</div></section>\n')

# ================= ПОЛОСА 2: фотографическая =================
t, q, s = A['truck'], A['square'], A['stop']
P.append('<section class="sheet">')
P.append(folio(2, 'происшествия'))
P.append(sect('01', 'Происшествия'))
P.append(f'<div class="inner"><article class="g84"><div>{fig("truck", t["cap"], t["alt"])}</div>'
         f'<div>{kick("truck")}<h3>{t["t"]}</h3><div class="stand">{t["s"]}</div><div class="amberline"></div>{txt("truck")}</div></article>')
P.append(f'<article class="g39" style="margin-top:28px"><div class="vert">{kick("square")}<h3>{q["t"]}</h3>'
         f'<div class="stand">{q["s"]}</div>{txt("square")}</div>'
         f'<div>{fig("square", q["cap"], q["alt"])}</div></article>')
P.append(f'<article class="briefline"><div>{fig("stop", s["cap"], s["alt"])}</div>'
         f'<div>{kick("stop")}<h3>{s["t"]}</h3><div class="stand">{s["s"]}</div>{txt("stop")}</div></article>'
         '</div></section>\n')

# ================= ПОЛОСА 3: типографическая =================
h, d, cc = A['hwy'], A['dragons'], A['caligula']
P.append('<section class="sheet">')
P.append(folio(3, 'криминал · экономика'))
P.append(sect('02', 'Криминал · Экономика'))
P.append(f'<div class="inner"><article>{kick("hwy")}'
         f'<h3 style="font-size:clamp(28px,3.6vw,44px);max-width:20em">{h["t"]}</h3>'
         f'<div class="stand">{h["s"]}</div>'
         f'<div class="g75t"><div class="cols2">' + ''.join(f'<p>{p}</p>' for p in h['p']) + '</div>'
         f'<div>{fig("hwy", h["cap"], h["alt"])}</div></div></article>')
P.append(f'<div class="duo"><article>{fig("dragons", d["cap"], d["alt"])}{kick("dragons")}<h3>{d["t"]}</h3>'
         f'<div class="stand">{d["s"]}</div>{txt("dragons")}</article>'
         f'<article>{kick("caligula")}<h3>{cc["t"]}</h3><div class="stand">{cc["s"]}</div>{txt("caligula")}'
         f'{fig("caligula", cc["cap"], cc["alt"])}</article></div></div></section>\n')

# ================= ПОЛОСА 4: плотная =================
he, y = A['heli'], A['yacht']
P.append('<section class="sheet">')
P.append(folio(4, 'необычные истории'))
P.append(sect('03', 'Необычные истории'))
P.append(f'<div class="inner"><article>{kick("heli")}'
         f'<h3 style="font-size:clamp(26px,3.2vw,40px);max-width:24em">{he["t"]}</h3>'
         f'<div class="stand">{he["s"]}</div>'
         f'<figure class="wide"><div class="ph"><img src="{IMG["heli"]}" alt="{he["alt"]}"></div>'
         f'<figcaption>{he["cap"]}</figcaption></figure>'
         f'<div class="cols3">' + ''.join(f'<p>{p}</p>' for p in he['p']) + '</div></article>')
P.append(f'<div class="marg"><div class="pause"><span class="ghost">12</span>'
         f'<span class="sv">материал полосы · Лос-Сантос</span></div>'
         f'<article>{fig("yacht", y["cap"], y["alt"])}{kick("yacht")}<h3>{y["t"]}</h3>'
         f'<div class="stand">{y["s"]}</div>{txt("yacht")}</article></div></div>')
P.append('<div class="colophon"><div><div class="credits">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>'
         '<div class="made">выпуск очереди подшивки · 03.10.2026 · дизайн и вёрстка — редакция San Fierro News</div></div>'
         '<a class="backpill" href="newsroom.html">← Посмотреть все выпуски редакции</a></div>')
P.append('</section>\n')

P.append('<!-- SFN · 2026 · 029 · artdesk -->\n</body>\n</html>\n')

html = ''.join(P)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
words = sum(len((a['s'] + ' ' + ' '.join(a['p'])).split()) for a in A.values())
print(f'собрано v8: {OUT} · {len(html)//1024} КБ · полос: 4 · кадров: {len(IMG)} · слов: {words}')
