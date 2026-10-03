#!/usr/bin/env python3
"""SFN: сборщик выпуска 03.10.2026 (v5, вертикальная веб-газета, самостоятельный стиль).
Дизайн: SFN-DESIGN-029, слаг street-folio (бриф главреда от 03.10.2026: без перелистывания,
концепция «городская документация Сан-Фиерро», асимметрия, разные композиции полос).
Содержание (тексты, лиды, подписи, кикеры, порядок, кадры) импортируется из сборщика v4
без единой правки. Ничего не скрывается: нет overflow:hidden/line-clamp/фикс. высот.
Фото: width:100% + height:auto (кадр целиком, исходные пропорции).
Выход: anna-malboro/daily-03-10-2026.html (очередь подшивки).
Запуск из корня:  python3 worktmp/build_daily_0310_state_v5.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V4 = os.path.join(ROOT, 'worktmp', 'build_daily_0310_state_v4.py')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')

src = open(V4, encoding='utf-8').read()
src = src.replace("OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')",
                  "OUT = os.devnull")
ns = {'__name__': 'sfn_v4_data', '__file__': V4}
exec(compile(src, V4, 'exec'), ns)
IMG, A = ns['IMG'], ns['A']

CSS = """/* SFN-DESIGN-029: street-folio · 03.10.2026 */
@import url('https://fonts.googleapis.com/css2?family=Prata&family=Oswald:wght@300;400;500;600;700&family=PT+Serif:ital,wght@0,400;0,700;1,400&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%}
:root{--asphalt:#262b31;--paper:#f3f0e8;--paper2:#efece2;--ink:#171a1e;--mut:#6c675e;
--red:#a4262c;--blue:#2e4057;--sand:#e7e0cf;--line:#d5cebd}
body{background:var(--asphalt);color:var(--ink);font-family:"PT Serif",Georgia,serif;
-webkit-font-size-adjust:100%;padding:26px 14px 40px;
background-image:radial-gradient(rgba(255,255,255,.045) 1px,transparent 1px);background-size:22px 22px}
.os{font-family:"Oswald","PT Sans",Arial,sans-serif}
/* ---- полоса-лист ---- */
.sheet{max-width:1060px;margin:0 auto 22px;background:var(--paper);padding:30px 42px 34px;
box-shadow:0 12px 30px rgba(0,0,0,.4);position:relative}
.sheet:nth-child(even){background:var(--paper2)}
.folio{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.mono{border:1.5px solid var(--red);color:var(--red);font-family:"Oswald",sans-serif;font-weight:600;
font-size:11px;letter-spacing:.24em;padding:3px 9px 2px;white-space:nowrap}
.lane{flex:1 1 auto;height:3px;opacity:.4;
background:repeating-linear-gradient(90deg,var(--blue) 0 26px,transparent 26px 40px)}
.folio .no{font-family:"Oswald",sans-serif;font-size:10.5px;letter-spacing:.2em;
text-transform:uppercase;color:var(--mut);white-space:nowrap}
/* ---- рубрики полос: гигантский контурный номер ---- */
.sect{display:flex;align-items:flex-end;gap:16px;margin:2px 0 18px}
.sect .num{font-family:"Oswald",sans-serif;font-weight:700;font-size:64px;line-height:.8;
color:transparent;-webkit-text-stroke:1.4px var(--blue);letter-spacing:.02em}
.sect h2{font-family:"Oswald",sans-serif;font-weight:600;font-size:21px;letter-spacing:.3em;
text-transform:uppercase;color:var(--blue);padding-bottom:4px}
.sect .rule{flex:1;border-bottom:1px solid var(--line);margin-bottom:8px}
/* ---- типографика ---- */
.kicker{font-family:"Oswald",sans-serif;font-weight:500;font-size:11px;letter-spacing:.24em;
text-transform:uppercase;color:var(--red);margin-bottom:6px}
h1,h3{font-family:"Prata",Georgia,serif;font-weight:400;line-height:1.16;letter-spacing:0}
h1{font-size:clamp(26px,3.4vw,38px);margin-bottom:8px}
h3{font-size:clamp(16px,1.7vw,20px);margin-bottom:6px}
.stand{font-style:italic;color:var(--mut);font-size:14px;line-height:1.55;margin-bottom:9px}
.txt p{margin:0 0 8px;line-height:1.66;font-size:14.5px}
figure{margin:0 0 10px}
.ph img{width:100%;height:auto;transition:filter .45s}
.ph:hover img{filter:contrast(1.04)}
figcaption{margin-top:5px;font-family:"Oswald",sans-serif;font-weight:300;font-size:10.5px;
letter-spacing:.05em;line-height:1.5;color:var(--mut)}
/* ---- сетки ---- */
.g75{display:grid;grid-template-columns:7fr 5fr;gap:28px;align-items:start}
.g57{display:grid;grid-template-columns:5fr 7fr;gap:28px;align-items:start}
.g66{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
.g48{display:grid;grid-template-columns:4fr 8fr;gap:24px;align-items:start}
.briefs{display:grid;grid-template-columns:5fr 4fr 3fr;gap:22px;align-items:start;
border-top:2px solid var(--ink);padding-top:16px;margin-top:20px}
.cols3{columns:3;column-gap:22px;column-rule:1px solid var(--line)}
.cols3 p{margin:0 0 8px;line-height:1.66;font-size:14.5px}
/* ---- служебные блоки ---- */
.docbox{background:var(--sand);padding:14px 16px 12px}
.docbox .row{font-family:"Oswald",sans-serif;font-weight:400;font-size:10.5px;letter-spacing:.14em;
text-transform:uppercase;color:var(--blue);padding:2.5px 0;border-bottom:1px dotted var(--blue)}
.docbox .row:last-child{border-bottom:none}
.docbox .row b{color:var(--red);font-weight:600}
.bignum{font-family:"Oswald",sans-serif;font-weight:700;font-size:27px;letter-spacing:.03em;
color:var(--blue);margin:6px 0 2px}
.bignum small{display:block;font-weight:400;font-size:10px;letter-spacing:.18em;
text-transform:uppercase;color:var(--mut)}
.notice{border:1.5px dashed var(--blue);padding:14px 15px;transform:rotate(-.5deg);background:var(--paper)}
.casefile{border:1px solid var(--blue);padding:18px 20px;
background:
 linear-gradient(var(--red),var(--red)) top left/16px 3px,
 linear-gradient(var(--red),var(--red)) top left/3px 16px,
 linear-gradient(var(--red),var(--red)) top right/16px 3px,
 linear-gradient(var(--red),var(--red)) top right/3px 16px,
 linear-gradient(var(--red),var(--red)) bottom left/16px 3px,
 linear-gradient(var(--red),var(--red)) bottom left/3px 16px,
 linear-gradient(var(--red),var(--red)) bottom right/16px 3px,
 linear-gradient(var(--red),var(--red)) bottom right/3px 16px;
background-repeat:no-repeat}
/* ---- первая полоса ---- */
.mast{display:grid;grid-template-columns:8fr 4fr;gap:28px;align-items:end;margin-bottom:14px}
.brand{font-family:"Prata",Georgia,serif;font-size:clamp(30px,4.4vw,46px);line-height:1.02}
.brand i{font-style:normal;color:var(--red)}
.brand .sub{display:block;font-family:"Oswald",sans-serif;font-weight:400;font-size:11px;
letter-spacing:.3em;text-transform:uppercase;color:var(--mut);margin-top:7px}
.leadcap::first-letter{font-family:"Prata",Georgia,serif;font-size:46px;line-height:.85;
float:left;padding:3px 8px 0 0;color:var(--red)}
/* ---- подвал ---- */
.colophon{border-top:2px solid var(--ink);margin-top:24px;padding-top:12px;
display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center}
.colophon .credits{font-family:"Oswald",sans-serif;font-weight:400;font-size:11px;letter-spacing:.08em}
.colophon .made{margin-top:4px;font-family:"Oswald",sans-serif;font-weight:300;font-size:10px;
letter-spacing:.1em;color:var(--mut)}
.backpill{display:inline-block;padding:8px 18px;border:1.5px solid var(--red);border-radius:999px;
color:var(--red);font-family:"Oswald",sans-serif;font-weight:600;font-size:12px;letter-spacing:.08em;
text-decoration:none;transition:.25s;white-space:nowrap}
.backpill:hover{background:var(--red);color:var(--paper)}
/* ---- адаптив ---- */
@media(max-width:920px){
 .sheet{padding:20px 18px 24px}
 .g75,.g57,.g66,.g48,.briefs,.mast{grid-template-columns:1fr}
 .cols3{columns:1}
 .sect .num{font-size:46px}
 .colophon{grid-template-columns:1fr}
}
"""


def fig(key, cap, alt):
    return f'<figure><div class="ph"><img src="{IMG[key]}" alt="{alt}"></div><figcaption>{cap}</figcaption></figure>'


def txt(key, cls='txt'):
    a = A[key]
    return (f'<div class="kicker">{a["k"]}</div><h3>{a["t"]}</h3><div class="stand">{a["s"]}</div>'
            f'<div class="{cls}">' + ''.join(f'<p>{p}</p>' for p in a['p']) + '</div>')


def folio(no, label):
    return (f'<div class="folio"><span class="mono">SFN</span><span class="lane"></span>'
            f'<span class="no">полоса {no} · 3 октября 2026 · {label}</span></div>')


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
P.append('<section class="sheet">')
P.append(folio(1, 'главные новости'))
P.append('<div class="mast"><div class="brand">San Fierro <i>News</i>'
         '<span class="sub">независимая редакция · штат San Andreas</span></div>'
         '<div class="docbox">'
         '<div class="row"><b>№ 30</b> · ежедневный выпуск</div>'
         '<div class="row">Лос-Сантос — Лас-Вентурас — трассы штата</div>'
         '<div class="row">12 материалов · 4 полосы</div>'
         '<div class="row">суббота, 3 октября 2026</div>'
         '<div class="row">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>'
         '</div></div>')
a = A['fallen']
P.append(f'<div class="g75"><div><div class="kicker">{a["k"]}</div><h1>{a["t"]}</h1>'
         f'<div class="stand">{a["s"]}</div><div class="txt leadcap">' +
         ''.join(f'<p>{p}</p>' for p in a['p']) + '</div></div>'
         f'<div>{fig("fallen", a["cap"], a["alt"])}</div></div>')
P.append('<div class="briefs">')
c = A['crash']
P.append(f'<article class="g48"><div>{fig("crash", c["cap"], c["alt"])}</div>'
         f'<div><div class="kicker">{c["k"]}</div><h3>{c["t"]}</h3>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in c['p']) + '</div></div></article>')
g = A['gas']
P.append(f'<article class="docbox"><div class="kicker">{g["k"]}</div><h3>{g["t"]}</h3>'
         f'{fig("gas", g["cap"], g["alt"])}'
         f'<div class="bignum">$100 000 000<small>предыдущая ставка торгов</small></div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in g['p']) + '</div></article>')
k = A['kpp']
P.append(f'<article class="notice"><div class="kicker">{k["k"]}</div><h3>{k["t"]}</h3>'
         f'{fig("kpp", k["cap"], k["alt"])}'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in k['p']) + '</div></article>')
P.append('</div></section>\n')

# ================= ПОЛОСА 2 =================
P.append('<section class="sheet">')
P.append(folio(2, 'происшествия'))
P.append('<div class="sect"><span class="num">01</span><h2>Происшествия</h2><span class="rule"></span></div>')
t = A['truck']
P.append(f'<article class="g75"><div>{fig("truck", t["cap"], t["alt"])}</div>'
         f'<div><div class="kicker">{t["k"]}</div><h3>{t["t"]}</h3><div class="stand">{t["s"]}</div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in t['p']) + '</div></div></article>')
q = A['square']
P.append(f'<article class="g57" style="margin-top:22px"><div><div class="kicker">{q["k"]}</div>'
         f'<h3>{q["t"]}</h3><div class="stand">{q["s"]}</div><div class="txt">' +
         ''.join(f'<p>{p}</p>' for p in q['p']) + '</div></div>'
         f'<div>{fig("square", q["cap"], q["alt"])}</div></article>')
s = A['stop']
P.append(f'<article class="g48" style="margin-top:22px;border-top:1px solid var(--line);padding-top:18px">'
         f'<div>{fig("stop", s["cap"], s["alt"])}</div>'
         f'<div><div class="kicker">{s["k"]}</div><h3>{s["t"]}</h3><div class="stand">{s["s"]}</div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in s['p']) + '</div></div></article>')
P.append('</section>\n')

# ================= ПОЛОСА 3 =================
P.append('<section class="sheet">')
P.append(folio(3, 'криминал · экономика'))
P.append('<div class="sect"><span class="num">02</span><h2>Криминал · Экономика</h2><span class="rule"></span></div>')
h = A['hwy']
P.append(f'<article><div class="kicker">{h["k"]}</div><h3>{h["t"]}</h3><div class="stand">{h["s"]}</div>'
         f'{fig("hwy", h["cap"], h["alt"])}<div class="cols3">' +
         ''.join(f'<p>{p}</p>' for p in h['p']) + '</div></article>')
d = A['dragons']
P.append(f'<article class="g57" style="margin-top:24px"><div class="docbox">'
         f'<div class="kicker">{d["k"]}</div><h3>{d["t"]}</h3><div class="stand">{d["s"]}</div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in d['p']) + '</div></div>'
         f'<div>{fig("dragons", d["cap"], d["alt"])}</div></article>')
cc = A['caligula']
P.append(f'<article class="g66" style="margin-top:22px"><div>{fig("caligula", cc["cap"], cc["alt"])}</div>'
         f'<div><div class="kicker">{cc["k"]}</div><h3>{cc["t"]}</h3><div class="stand">{cc["s"]}</div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in cc['p']) + '</div></div></article>')
P.append('</section>\n')

# ================= ПОЛОСА 4 =================
P.append('<section class="sheet">')
P.append(folio(4, 'необычные истории'))
P.append('<div class="sect"><span class="num">03</span><h2>Необычные истории</h2><span class="rule"></span></div>')
he = A['heli']
P.append(f'<article class="g66"><div class="casefile"><div class="kicker">{he["k"]}</div>'
         f'<h3>{he["t"]}</h3><div class="stand">{he["s"]}</div><div class="txt">' +
         ''.join(f'<p>{p}</p>' for p in he['p']) + '</div></div>'
         f'<div>{fig("heli", he["cap"], he["alt"])}</div></article>')
y = A['yacht']
P.append(f'<article class="g57" style="margin-top:24px"><div>{fig("yacht", y["cap"], y["alt"])}</div>'
         f'<div><div class="kicker">{y["k"]}</div><h3>{y["t"]}</h3><div class="stand">{y["s"]}</div>'
         f'<div class="txt">' + ''.join(f'<p>{p}</p>' for p in y['p']) + '</div></div></article>')
P.append('<div class="colophon"><div><div class="credits">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>'
         '<div class="made">выпуск очереди подшивки · 03.10.2026 · дизайн и вёрстка — редакция San Fierro News</div></div>'
         '<a class="backpill" href="newsroom.html">← Посмотреть все выпуски редакции</a></div>')
P.append('</section>\n')

P.append('<!-- SFN · 2026 · 029 · street-folio -->\n</body>\n</html>\n')

html = ''.join(P)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
words = sum(len((a['s'] + ' ' + ' '.join(a['p'])).split()) for a in A.values())
print(f'собрано v5: {OUT} · {len(html)//1024} КБ · полос-листов: 4 · кадров: {len(IMG)} · слов: {words}')
