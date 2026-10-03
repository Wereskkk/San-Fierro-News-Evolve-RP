#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SFN: сборщик выпуска 03.10.2026 (v11, ЕДИНСТВЕННЫЙ редизайн: асимметричный бродшит).

Бриф главреда Anna Malboro от 04.10.2026 (итоговая редакция):
— ОДИН редизайн, без вариантов и переключателей;
— внешний фон сайта и оболочка листа (крем, 1120px, тень) — НЕ ТРОНУТЫ;
— весь текст и все 12 кадров сохранены; содержание статей не менялось;
— главный заголовок уменьшен до компактного сильного лок-апа (две строки, ~38px);
— НЕТ визуально оторванных элементов: каждый номер материала физически связан
  со своим лок-апом (номер + волосяная линейка + рубрика), номера-гиганты стоят
  в сетке материала, а не плавают по углам;
— НЕТ случайных пустот: пустое пространство существует только как отбивка
  между зонами, оформленная линейками, либо как узкая служебная колонка;
— НЕТ системы одинаковых колонок/карточек: у каждого материала своя
  асимметричная композиция (8/4, 5/7, 4/8, лестница, полоса во весь листа);
— сигнатуры: номерная колонка-хребет на полосах 2 и 4, чёрные плашки-подписи
  под полноширинными кадрами, толстые и волосяные линейки, контраст масштаба
  (Anton-гиганты против PT Mono 9px), лестничный сдвиг пары казино, финальный
  замок «12 + кадр» с общей линейкой.
Содержание импортируется из сборщика v4 (канон текстов) без правок, кроме
утверждённой замены номера борта 2504 (правка главреда).
Фото: width:100% + height:auto, кадры целиком, без кропа.
Выход: anna-malboro/daily-03-10-2026.html (очередь подшивки).
Запуск из корня:  python3 worktmp/build_daily_0310_state_v11.py
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

# ---- правка главреда: номер борта 2504 удалён полностью ----
REPL = [
    ('Борт 2504 и автомобиль', 'Патрульный автомобиль и машина'),
    ('Борт 2504 и легковушка', 'Патрульный автомобиль и легковушка'),
    ('Борт 2504:', 'Патрульный автомобиль:'),
    ('Патрульный борт 2504 остановил', 'Патрульный автомобиль остановил'),
]
for _a in A.values():
    for _f in ('k', 't', 's', 'cap', 'alt'):
        for _o, _n in REPL:
            _a[_f] = _a[_f].replace(_o, _n)
    _newp = []
    for _pp in _a['p']:
        for _o, _n in REPL:
            _pp = _pp.replace(_o, _n)
        _newp.append(_pp)
    _a['p'] = _newp
for _key, _a in A.items():
    for _f in ('k', 't', 's', 'cap', 'alt'):
        assert '2504' not in _a[_f], f'2504 остался в {_key}.{_f}'
    for _pp in _a['p']:
        assert '2504' not in _pp, f'2504 остался в {_key}.p'

IDX = {'fallen': '01', 'crash': '02', 'gas': '03', 'kpp': '04', 'truck': '05', 'square': '06',
       'stop': '07', 'hwy': '08', 'dragons': '09', 'caligula': '10', 'heli': '11', 'yacht': '12'}

CSS = """/* SFN-DESIGN-029: asymmetric-broadsheet · 03.10.2026 */
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@500;600;700&family=PT+Mono&family=PT+Serif:ital,wght@0,400;0,700;1,400&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%}
:root{--paper:#f2ede3;--ink:#1a1714;--ox:#9e2b25;--mut:#6d675c;--hair:#cfc7b4;--tint:#e9e2d1;--ondark:#c9c2b4}
/* ---- внешняя среда и оболочка: байт-в-байт как до всех правок — НЕ ТРОГАТЬ ---- */
body{background:var(--paper);color:var(--ink);font-family:"PT Serif",Georgia,serif;
-webkit-font-size-adjust:100%;padding:0 0 60px}
.sheet{max-width:1120px;margin:0 auto 26px;background:var(--paper);padding:0 0 40px;
box-shadow:0 16px 40px rgba(20,24,28,.22);position:relative}
.sheet+.sheet{margin-top:34px}
/* ---- служебная типографика ---- */
.mono{font-family:"PT Mono",monospace}
.pad{padding:0 46px}
figure{margin:0}
.ph img{width:100%;height:auto;transition:filter .45s}
.ph:hover img{filter:contrast(1.04)}
figcaption{font-family:"PT Mono",monospace;font-size:9.5px;line-height:1.55;letter-spacing:.05em;
color:var(--mut);margin-top:7px}
.ph.bandcap figcaption{background:var(--ink);color:var(--paper);margin:0;padding:8px 12px;
font-weight:700;letter-spacing:.06em}
.ph.framed{border:3px solid var(--ink)}
.ph.framed.bandcap figcaption{border-top:0}
/* ---- лок-ап номера: номер ВСЕГДА связан с материалом ---- */
.lock{display:flex;align-items:stretch;gap:14px;margin-bottom:12px}
.lock .num{font-family:Anton,sans-serif;font-weight:400;font-size:56px;line-height:.86;
color:var(--ink);letter-spacing:.01em}
.lock .num.ox{color:var(--ox)}
.lock .lhair{width:1px;background:var(--ink);opacity:.55;align-self:stretch}
.lock .k{font-family:"PT Mono",monospace;font-weight:700;font-size:10px;letter-spacing:.24em;
text-transform:uppercase;color:var(--ox);align-self:center;padding-left:2px}
/* ---- заголовки и текст ---- */
h1{font-family:Oswald,sans-serif;font-weight:700;text-transform:uppercase;
font-size:clamp(25px,2.9vw,38px);line-height:1.06;letter-spacing:.005em;color:var(--ink);
margin-bottom:12px}
h1 .ln2{color:var(--ox)}
h3{font-family:Oswald,sans-serif;font-weight:600;text-transform:uppercase;
font-size:clamp(17px,1.85vw,24px);line-height:1.12;letter-spacing:.01em;color:var(--ink);
margin-bottom:8px}
.stand{font:italic 400 14px/1.58 "PT Serif",serif;color:var(--mut);
border-left:2px solid var(--ox);padding-left:12px;margin-bottom:11px}
.txt p{font:400 14.5px/1.7 "PT Serif",serif;margin:0 0 8px}
.cols2{columns:2;column-gap:26px;column-rule:1px solid var(--hair)}
.cols3{columns:3;column-gap:26px;column-rule:1px solid var(--hair)}
.cols2 p,.cols3 p{margin:0 0 8px;font:400 14.5px/1.7 "PT Serif",serif}
/* ---- линейки ---- */
.hrule{border-top:3px solid var(--ink);margin:26px 0}
.hrule.thin{border-top-width:1px;border-color:var(--hair)}
/* ---- шапка ---- */
.mtop{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;padding:14px 46px 10px;
font-family:"PT Mono",monospace;font-weight:700;font-size:9.5px;letter-spacing:.16em;
text-transform:uppercase;color:var(--mut)}
.brand{padding:14px 46px 4px;display:flex;align-items:baseline;gap:.22em;flex-wrap:wrap}
.b1,.b2{font-family:Anton,sans-serif;font-weight:400;text-transform:uppercase;line-height:.92;
letter-spacing:.004em;font-size:clamp(50px,8.2vw,104px)}
.b1{color:var(--ink)}
.b2{color:var(--ox)}
.mrule{margin:6px 46px 0;border-top:4px solid var(--ink)}
.mmeta{margin:0 46px;padding:9px 0 11px;border-bottom:1px solid var(--ink);display:flex;
flex-wrap:wrap;justify-content:space-between;gap:4px 22px;font-family:"PT Mono",monospace;
font-weight:700;font-size:9.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink)}
.mmeta b{color:var(--ox)}
/* ---- полоса 1 ---- */
#a01{display:grid;grid-template-columns:8fr 4fr;gap:0 34px;margin-top:26px;
grid-template-areas:"lock ph" "h ph" "s ph" "t ph";align-items:start}
#a01 .lock{grid-area:lock}
#a01 h1{grid-area:h}
#a01 .stand{grid-area:s}
#a01 .txt{grid-area:t}
#a01 .ph{grid-area:ph;margin-top:44px}
.bandrow{display:grid;grid-template-columns:6fr 3px 6fr;gap:0 30px;align-items:start}
.bandrow .vrule{background:var(--ink);align-self:stretch}
.stat b{display:block;font-family:Anton,sans-serif;font-weight:400;font-size:clamp(30px,3.5vw,46px);
line-height:.95;color:var(--ox);white-space:nowrap;margin:2px 0 4px}
.stat small{display:block;font-family:"PT Mono",monospace;font-weight:700;font-size:9px;
letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin-bottom:10px}
.strip{display:grid;grid-template-columns:6fr 6fr;gap:0 32px;align-items:start}
.strip .ph{margin-top:4px}
/* ---- служебная строка выпуска ---- */
.pressline{margin:30px 46px 0;background:var(--ink);color:var(--paper);padding:14px 20px;
display:flex;justify-content:space-between;align-items:baseline;gap:14px;flex-wrap:wrap}
.pl1{font-family:Oswald,sans-serif;font-weight:600;font-size:20px;text-transform:uppercase;
letter-spacing:.05em}
.pl1 i{font-style:normal;color:#e8897f}
.pl2{font-family:"PT Mono",monospace;font-weight:700;font-size:9px;letter-spacing:.2em;
text-transform:uppercase;color:var(--ondark)}
/* ---- колонтитул и секции ---- */
.folio{display:flex;justify-content:space-between;align-items:baseline;gap:14px;flex-wrap:wrap;
padding:10px 46px;border-bottom:2px solid var(--ink);font-family:"PT Mono",monospace;
font-weight:700;font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink)}
.folio b{color:var(--ox)}
.f3{background:var(--ink);color:var(--paper);padding:2px 8px}
.sect{display:flex;align-items:center;gap:18px;margin:0 0 26px}
.snum{font-family:Anton,sans-serif;font-weight:400;font-size:clamp(40px,5.2vw,64px);line-height:1;
color:var(--ox);padding:6px 0 6px 46px}
.sect h2{font-family:Oswald,sans-serif;font-weight:700;font-size:clamp(22px,3vw,38px);
text-transform:uppercase;letter-spacing:.04em;color:var(--ink)}
.stail{flex:1;border-bottom:3px solid var(--ink);margin:0 20px 0 4px}
.sdate{font-family:"PT Mono",monospace;font-weight:700;font-size:9px;letter-spacing:.2em;
text-transform:uppercase;color:var(--mut);padding-right:46px}
/* ---- номерная колонка-хребет (полосы 2 и 4) ---- */
.spine{display:grid;grid-template-columns:92px 1fr;gap:0 26px;align-items:start}
.spine .numcol{position:relative;padding-top:2px}
.spine .numcol .num{font-family:Anton,sans-serif;font-weight:400;font-size:64px;line-height:.86;
color:var(--ink);display:block}
.spine .numcol::after{content:"";position:absolute;top:70px;bottom:-26px;left:31px;width:1px;
background:var(--ink);opacity:.5}
.spine.last .numcol::after{display:none}
.spine .numcol .nlabel{display:block;margin-top:10px;font-family:"PT Mono",monospace;font-weight:700;
font-size:8.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--mut);
writing-mode:vertical-rl;position:absolute;top:76px;left:42px}
/* ---- полоса 3: лестница ---- */
.stair{margin-left:24%;border-top:3px solid var(--ink);padding-top:20px}
.pull{font-family:Oswald,sans-serif;font-weight:600;font-size:clamp(16px,1.8vw,22px);
text-transform:uppercase;color:var(--ox);border-top:3px solid var(--ink);
border-bottom:1px solid var(--ink);padding:9px 0;margin:14px 0 4px;line-height:1.1}
/* ---- финальный замок 12 ---- */
.finale{display:grid;grid-template-columns:250px 1fr;gap:0;border-top:4px solid var(--ink);
margin-top:30px;padding-top:24px;align-items:start}
.finale .fnum{padding-right:24px;border-right:3px solid var(--ink)}
.finale .fnum .num{font-family:Anton,sans-serif;font-weight:400;font-size:clamp(140px,17vw,220px);
line-height:.82;color:var(--ox);display:block}
.finale .fnum .nlabel{display:block;margin-top:14px;font-family:"PT Mono",monospace;font-weight:700;
font-size:9px;letter-spacing:.24em;text-transform:uppercase;color:var(--ink)}
.finale .fbody{padding-left:28px}
/* ---- колофон ---- */
.colophon{margin:44px 46px 0;border:1px solid var(--ink);padding:20px 24px;display:flex;
justify-content:space-between;align-items:center;gap:18px;flex-wrap:wrap;position:relative}
.colophon::before{content:"";position:absolute;top:-4px;left:-4px;width:8px;height:8px;
background:var(--ox);border-radius:50%}
.credits{font-family:"PT Mono",monospace;font-size:10.5px;letter-spacing:.06em;color:var(--ink)}
.made{margin-top:7px;font-family:"PT Mono",monospace;font-size:9px;letter-spacing:.16em;
text-transform:uppercase;color:var(--mut)}
.backpill{display:inline-block;padding:10px 20px;border:1.5px solid var(--ox);color:var(--ox);
font-family:"PT Mono",monospace;font-weight:700;font-size:10.5px;letter-spacing:.12em;
text-transform:uppercase;text-decoration:none;transition:.2s;white-space:nowrap}
.backpill:hover{background:var(--ox);color:var(--paper)}
/* ---- мобильная версия ---- */
@media(max-width:920px){
 .pad{padding:0 18px}
 .mtop,.folio{padding-left:18px;padding-right:18px}
 .brand{padding:12px 18px 4px}
 .mrule,.mmeta{margin-left:18px;margin-right:18px}
 .pressline,.colophon{margin-left:18px;margin-right:18px}
 .pressline{padding:12px 16px}
 .colophon{padding:16px}
 .snum{padding-left:18px}
 .sdate{padding-right:18px}
 #a01{grid-template-columns:1fr;grid-template-areas:"lock" "h" "s" "ph" "t";gap:0}
 #a01 .ph{margin-top:14px}
 .bandrow{grid-template-columns:1fr;gap:24px}
 .bandrow .vrule{display:none}
 .strip{grid-template-columns:1fr;gap:16px}
 .strip .ph{margin-top:0}
 .cols2,.cols3{columns:1}
 .spine{grid-template-columns:64px 1fr;gap:0 16px}
 .spine .numcol .num{font-size:44px}
 .spine .numcol::after{top:50px;left:21px}
 .spine .numcol .nlabel{display:none}
 .stair{margin-left:0}
 .finale{grid-template-columns:1fr;gap:18px}
 .finale .fnum{border-right:0;border-bottom:3px solid var(--ink);padding:0 0 14px}
 .finale .fnum .num{font-size:110px}
 .finale .fbody{padding-left:0}
}
"""


def fig(key, band=False, framed=False):
    a = A[key]
    cls = 'ph' + (' bandcap' if band else '') + (' framed' if framed else '')
    return (f'<figure class="{cls}"><img src="{IMG[key]}" alt="{a["alt"]}">'
            f'<figcaption>{a["cap"]}</figcaption></figure>')


def lock(key, ox=False, nonum=False):
    a = A[key]
    num = '' if nonum else f'<span class="num{" ox" if ox else ""}">{IDX[key]}</span>'
    return (f'<div class="lock">{num}'
            f'<span class="lhair" aria-hidden="true"></span>'
            f'<span class="k">{a["k"]}</span></div>')


def txt(key, cls='txt'):
    return f'<div class="{cls}">' + ''.join(f'<p>{p}</p>' for p in A[key]['p']) + '</div>'


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
a, c, g, k = A['fallen'], A['crash'], A['gas'], A['kpp']
w = a['t'].split()
P.append('<section class="sheet" id="p1">')
P.append('<div class="mtop"><span>Независимая редакция · штат San Andreas</span>'
         '<span>суббота, 3 октября 2026</span></div>')
P.append('<div class="brand"><span class="b1">San Fierro</span><span class="b2">News</span></div>')
P.append('<div class="mrule" aria-hidden="true"></div>')
P.append('<div class="mmeta"><span><b>№ 30</b> · ежедневный выпуск</span>'
         '<span>Лос-Сантос — Лас-Вентурас — трассы штата</span>'
         '<span>12 материалов · 4 полосы · 03.10.2026</span>'
         '<span>Кадры: Anna Malboro · Фоторедактор: Sonya Malboro</span>'
         '<span>Текст/Редактор: Jonny Wilde</span></div>')
P.append('<div class="pad">')
P.append('<article id="a01">')
P.append(lock('fallen', ox=True))
P.append(f'<h1><span class="ln1">{" ".join(w[:4])}</span> <span class="ln2">{" ".join(w[4:])}</span></h1>')
P.append(f'<div class="stand">{a["s"]}</div>')
P.append(txt('fallen'))
P.append(fig('fallen', band=True, framed=True))
P.append('</article>')
P.append('<div class="hrule" aria-hidden="true"></div>')
P.append('<div class="bandrow">')
P.append(f'<article id="a02">{lock("crash")}<h3>{c["t"]}</h3>'
         f'<div class="stand">{c["s"]}</div>{fig("crash", framed=True)}{txt("crash")}</article>')
P.append('<span class="vrule" aria-hidden="true"></span>')
P.append(f'<article id="a03">{lock("gas")}'
         f'<h3>{g["t"]}</h3>'
         f'<div class="stat"><b>$100 000 000</b><small>предыдущая ставка торгов</small></div>'
         f'<div class="stand">{g["s"]}</div>{txt("gas")}{fig("gas", band=True, framed=True)}</article>')
P.append('</div>')
P.append('<div class="hrule" aria-hidden="true"></div>')
P.append(f'<article id="a04" class="strip">{fig("kpp", framed=True)}'
         f'<div>{lock("kpp")}<h3>{k["t"]}</h3><div class="stand">{k["s"]}</div>'
         f'{txt("kpp", "cols2")}</div></article>')
P.append('</div>')
P.append('<footer class="pressline"><span class="pl1">Выпуск № 30 · четыре полосы · '
         '<i>двенадцать материалов</i></span>'
         '<span class="pl2">San Fierro News · ежедневное издание штата San Andreas · 03.10.2026</span>'
         '</footer>')
P.append('</section>\n')

# ================= ПОЛОСА 2 (номерная колонка-хребет) =================
t, q, s = A['truck'], A['square'], A['stop']
P.append('<section class="sheet" id="p2">')
P.append('<div class="folio"><span class="f1"><b>San Fierro News</b> · выпуск № 30 · происшествия</span>'
         '<span class="f2">суббота, 3 октября 2026</span><span class="f3">полоса 2</span></div>')
P.append('<header class="sect"><span class="snum">01</span><h2>Происшествия</h2>'
         '<span class="stail" aria-hidden="true"></span><span class="sdate">03.10.2026</span></header>')
P.append('<div class="pad">')
P.append(f'<article id="a05" class="spine"><div class="numcol"><span class="num">05</span>'
         f'<span class="nlabel">материал полосы</span></div>'
         f'<div>{lock("truck", nonum=True)}<h3 style="font-size:clamp(21px,2.5vw,32px)">{t["t"]}</h3>'
         f'<div class="stand">{t["s"]}</div>{fig("truck", band=True, framed=True)}'
         f'{txt("truck", "cols3")}</div></article>')
P.append('<div class="hrule thin" aria-hidden="true"></div>')
P.append(f'<article id="a06" class="spine"><div class="numcol"><span class="num">06</span></div>'
         f'<div style="display:grid;grid-template-columns:5fr 7fr;gap:0 28px;align-items:start">'
         f'<div>{lock("square", nonum=True)}<h3>{q["t"]}</h3><div class="stand">{q["s"]}</div>{txt("square")}</div>'
         f'{fig("square", framed=True)}</div></article>')
P.append('<div class="hrule thin" aria-hidden="true"></div>')
P.append(f'<article id="a07" class="spine last"><div class="numcol"><span class="num">07</span></div>'
         f'<div style="display:grid;grid-template-columns:4fr 8fr;gap:0 28px;align-items:start">'
         f'{fig("stop", framed=True)}'
         f'<div>{lock("stop", nonum=True)}<h3>{s["t"]}</h3><div class="stand">{s["s"]}</div>{txt("stop")}</div>'
         f'</div></article>')
P.append('</div></section>\n')

# ================= ПОЛОСА 3 (типографическая, лестница) =================
h, d, cc = A['hwy'], A['dragons'], A['caligula']
P.append('<section class="sheet" id="p3">')
P.append('<div class="folio"><span class="f1"><b>San Fierro News</b> · выпуск № 30 · криминал · экономика</span>'
         '<span class="f2">суббота, 3 октября 2026</span><span class="f3">полоса 3</span></div>')
P.append('<header class="sect"><span class="snum">02</span><h2>Криминал · Экономика</h2>'
         '<span class="stail" aria-hidden="true"></span><span class="sdate">03.10.2026</span></header>')
P.append('<div class="pad">')
P.append(f'<article id="a08">{lock("hwy")}'
         f'<h3 style="font-size:clamp(20px,2.6vw,34px);max-width:40ch">{h["t"]}</h3>'
         f'<div style="display:grid;grid-template-columns:5fr 7fr;gap:0 30px;align-items:start">'
         f'<div><div class="stand">{h["s"]}</div>{txt("hwy")}'
         f'<div class="pull">На полотне — отделившаяся деталь кузова</div></div>'
         f'<div style="margin-top:34px">{fig("hwy", band=True, framed=True)}</div></div></article>')
P.append('<div class="hrule" aria-hidden="true"></div>')
P.append(f'<article id="a09" style="display:grid;grid-template-columns:6fr 6fr;gap:0 30px;'
         f'align-items:start">{fig("dragons", framed=True)}'
         f'<div>{lock("dragons")}<h3>{d["t"]}</h3><div class="stand">{d["s"]}</div>{txt("dragons")}</div>'
         f'</article>')
P.append(f'<article id="a10" class="stair">{lock("caligula")}<h3 style="max-width:34ch">{cc["t"]}</h3>'
         f'<div style="display:grid;grid-template-columns:5fr 7fr;gap:0 30px;align-items:start">'
         f'<div><div class="stand">{cc["s"]}</div>{txt("caligula")}</div>'
         f'<div style="margin-top:6px">{fig("caligula", framed=True)}</div></div></article>')
P.append('</div></section>\n')

# ================= ПОЛОСА 4 (хребет + финальный замок) =================
he, y = A['heli'], A['yacht']
P.append('<section class="sheet" id="p4">')
P.append('<div class="folio"><span class="f1"><b>San Fierro News</b> · выпуск № 30 · необычные истории</span>'
         '<span class="f2">суббота, 3 октября 2026</span><span class="f3">полоса 4</span></div>')
P.append('<header class="sect"><span class="snum">03</span><h2>Необычные истории</h2>'
         '<span class="stail" aria-hidden="true"></span><span class="sdate">03.10.2026</span></header>')
P.append('<div class="pad">')
P.append(f'<article id="a11" class="spine last"><div class="numcol"><span class="num">11</span>'
         f'<span class="nlabel">трасса штата</span></div>'
         f'<div>{lock("heli", nonum=True)}<h3 style="font-size:clamp(20px,2.4vw,30px)">{he["t"]}</h3>'
         f'<div class="stand">{he["s"]}</div>{fig("heli", band=True, framed=True)}'
         f'{txt("heli", "cols3")}</div></article>')
P.append(f'<article id="a12" class="finale"><div class="fnum"><span class="num">12</span>'
         f'<span class="nlabel">материал полосы · Лос-Сантос</span></div>'
         f'<div class="fbody">{lock("yacht", ox=True, nonum=True)}<h3>{y["t"]}</h3>'
         f'<div class="stand">{y["s"]}</div>{fig("yacht", framed=True)}{txt("yacht", "cols2")}</div>'
         f'</article>')
P.append('</div>')
P.append('<footer class="colophon"><div>'
         '<div class="credits">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · '
         'Текст/Редактор: Jonny Wilde</div>'
         '<div class="made">выпуск очереди подшивки · 03.10.2026 · '
         'дизайн и вёрстка — редакция San Fierro News</div></div>'
         '<a class="backpill" href="newsroom.html">← Посмотреть все выпуски редакции</a></footer>')
P.append('</section>\n')

P.append('<!-- SFN · 2026 · 029 · asymmetric-broadsheet -->\n</body>\n</html>\n')

html = ''.join(P)

# ---- самопроверка ----
assert '2504' not in html, 'в выпуске остался номер 2504'
assert html.count('data:image/jpeg;base64,') == 12, 'кадров не 12'
for n in range(1, 13):
    assert f'id="a{n:02d}"' in html, f'нет материала a{n:02d}'
assert 'SFN-DESIGN-029: asymmetric-broadsheet' in html
assert '<!-- SFN · 2026 · 029 · asymmetric-broadsheet -->' in html
assert '<title>' in html[:4000] and 'viewport' in html[:4000] and 'name="description"' in html[:4000]
assert 'дизайн и вёрстка — редакция San Fierro News' in html
assert 'href="newsroom.html"' in html
assert 'lock(' not in html and 'class="lock"' in html

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
words = sum(len((a_['s'] + ' ' + ' '.join(a_['p'])).split()) for a_ in A.values())
print(f'собрано v11 (asymmetric-broadsheet): {OUT}')
print(f'  размер: {len(html)//1024} КБ · полос: 4 · кадров: {len(IMG)} · слов в материалах: {words}')
print('  2504: удалён везде · переключателей нет · один дизайн')
