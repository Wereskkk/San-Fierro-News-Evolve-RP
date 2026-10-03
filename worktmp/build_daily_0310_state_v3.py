#!/usr/bin/env python3
"""SFN: сборщик выпуска 03.10.2026 (v3, интерактивная газета с перелистыванием).
Дизайн: SFN-DESIGN-029, слаг interactive-pages (редизайн v3 по брифу главреда:
выпуск = 7 газетных листов с перелистыванием, а не одна вертикальная страница).
Содержание импортируется из сборщика v1 без правок.
Выход: anna-malboro/daily-03-10-2026.html (очередь подшивки).
Запуск из корня:  python3 worktmp/build_daily_0310_state_v3.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1 = os.path.join(ROOT, 'worktmp', 'build_daily_0310_state.py')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')

src = open(V1, encoding='utf-8').read()
src = src.replace("OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')",
                  "OUT = os.devnull")
ns = {'__name__': 'sfn_v1_data', '__file__': V1}
exec(compile(src, V1, 'exec'), ns)
IMG, LEAD, SEC, SECTIONS, READIN = ns['IMG'], ns['LEAD'], ns['SEC'], ns['SECTIONS'], ns['READIN']
TRUCK, CRASH = SEC
SQ, STOP = SECTIONS[0]['arts']
HWY, KPP = SECTIONS[1]['arts']
GAS, DRAG, CAL = SECTIONS[2]['arts']
HELI, YACHT = SECTIONS[3]['arts']

CSS = """/* SFN-DESIGN-029: interactive-pages · 03.10.2026 */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=PT+Sans:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%}
:root{--paper:#f7f4ed;--paper2:#f4f0e6;--ink:#1b1a17;--mut:#6e6a62;--line:#d9d3c6;--red:#9e1b1b;--box:#efeade}
body{background:#e8e4da;color:var(--ink);font-family:"PT Serif",Georgia,serif;
-webkit-font-size-adjust:100%;min-height:100vh;display:flex;flex-direction:column;align-items:center;
padding:14px 12px 10px;background-image:radial-gradient(#ddd8cb 1px,transparent 1px);background-size:26px 26px}
.sans{font-family:"PT Sans",Arial,sans-serif}
/* ---- сцена и лист ---- */
.stage{flex:1 1 auto;display:flex;align-items:center;justify-content:center;width:100%;min-height:0}
.sheet-wrap{position:relative}
.book{position:absolute;top:0;left:0;width:720px;height:1000px;transform-origin:top left;perspective:2200px}
.page{position:absolute;inset:0;background:var(--paper);padding:26px 28px;overflow:hidden;
box-shadow:0 14px 34px rgba(40,36,28,.22),0 2px 6px rgba(40,36,28,.14);
border:1px solid #cfc8b8;opacity:0;visibility:hidden;transform:rotateY(0deg);
transform-origin:left center;transition:transform .56s cubic-bezier(.35,.1,.25,1),opacity .5s,visibility 0s .56s}
.page:nth-child(even){background:var(--paper2)}
.page::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:0;
background:linear-gradient(100deg,rgba(60,50,30,.28),rgba(60,50,30,0) 42%);transition:opacity .56s}
.page.cur{opacity:1;visibility:visible;z-index:2;transform:none;
transition:transform .56s cubic-bezier(.35,.1,.25,1),opacity .45s,visibility 0s}
.page.out-l{visibility:visible;z-index:3;transform:rotateY(-68deg);opacity:.15}
.page.out-l::after{opacity:1}
.page.out-r{visibility:visible;z-index:3;transform-origin:right center;transform:rotateY(68deg);opacity:.15}
.page.out-r::after{opacity:1;background:linear-gradient(-100deg,rgba(60,50,30,.28),rgba(60,50,30,0) 42%)}
.page.in-r{visibility:visible;z-index:2;transform-origin:right center;transform:rotateY(46deg);opacity:.5;transition:none}
.page.in-l{visibility:visible;z-index:2;transform:rotateY(-46deg);opacity:.5;transition:none}
/* ---- типографика листа ---- */
.kicker{font-family:"PT Sans",sans-serif;font-size:10px;font-weight:700;letter-spacing:.19em;
text-transform:uppercase;color:var(--red);margin-bottom:4px}
h1,h3{font-family:"Playfair Display",Georgia,serif;font-weight:800;line-height:1.13;letter-spacing:-.004em}
h1{font-size:30px;margin-bottom:6px}
h3{font-size:18.5px;margin-bottom:4px}
.stand{font-style:italic;color:var(--mut);font-size:12.5px;line-height:1.5;margin-bottom:8px}
figure{margin:0 0 9px}
.ph{overflow:hidden;background:#ddd}
.ph img{width:100%;height:100%;object-fit:cover;object-position:top right;transition:transform .5s ease}
.ph:hover img{transform:scale(1.02)}
figcaption{margin-top:4px;font-family:"PT Sans",sans-serif;font-size:10.5px;line-height:1.45;color:var(--mut)}
.cols2{columns:2;column-gap:16px;column-rule:1px solid var(--line)}
.cols3{columns:3;column-gap:14px;column-rule:1px solid var(--line)}
.cols1 p,.cols2 p,.cols3 p{margin:0 0 7px;line-height:1.55;font-size:13.5px}
h4.sub{font-family:"PT Sans",sans-serif;font-weight:700;font-size:11px;letter-spacing:.1em;
text-transform:uppercase;margin:8px 0 5px}
.fact{border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);background:var(--box);
padding:7px 10px;margin:8px 0}
.fact .lbl{font-family:"PT Sans",sans-serif;font-weight:700;font-size:9px;letter-spacing:.2em;
text-transform:uppercase;color:var(--red);display:block;margin-bottom:2px}
.fact .q{font-style:italic;font-size:12.5px;line-height:1.5}
.jump{font-family:"PT Sans",sans-serif;font-size:10.5px;font-weight:700;color:var(--red);
letter-spacing:.06em;margin-top:5px}
/* ---- шапка и рубрики листа ---- */
.masttop{display:flex;justify-content:space-between;font-family:"PT Sans",sans-serif;font-size:9.5px;
letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.mastname{font-family:"Playfair Display",Georgia,serif;font-weight:900;text-align:center;font-size:33px;
line-height:1.08;padding:5px 0 4px}
.mastname i{font-style:normal;color:var(--red)}
.mastmeta{display:flex;flex-wrap:wrap;justify-content:center;gap:2px 12px;font-family:"PT Sans",sans-serif;
font-size:10px;letter-spacing:.05em;border-top:1px solid var(--ink);border-bottom:4px double var(--ink);
padding:4px 0}
.mastmeta b{color:var(--red)}
.mastcred{margin-top:4px;text-align:center;font-family:"PT Sans",sans-serif;font-size:9.5px;color:var(--mut)}
.sechead{display:flex;align-items:baseline;gap:6px;border-top:1px solid var(--ink);
border-bottom:1px solid var(--line);padding:4px 0 5px;margin-bottom:12px}
.sechead .sq{width:7px;height:7px;background:var(--red);flex:0 0 7px;transform:translateY(-1px)}
.sechead h2{font-family:"PT Sans",sans-serif;font-weight:700;font-size:12px;letter-spacing:.17em;text-transform:uppercase}
.sechead .pg{margin-left:auto;font-family:"PT Sans",sans-serif;font-size:9.5px;color:var(--mut)}
/* ---- композиции блоков ---- */
.g-side{display:grid;grid-template-columns:38fr 62fr;gap:16px;align-items:start;margin-bottom:14px}
.g-side-rev{display:grid;grid-template-columns:62fr 38fr;gap:16px;align-items:start;margin-bottom:14px}
.briefs{display:grid;grid-template-columns:1fr 1fr;gap:18px;border-top:1px solid var(--line);padding-top:10px}
.readin{border-top:4px double var(--ink);border-bottom:1px solid var(--line);padding:6px 0 7px;margin-top:12px}
.readin h5{font-family:"PT Sans",sans-serif;font-weight:700;font-size:10px;letter-spacing:.18em;
text-transform:uppercase;margin-bottom:4px}
.readin li{list-style:none;font-family:"PT Sans",sans-serif;font-size:10.5px;line-height:1.5;
padding:3px 0;border-top:1px dotted var(--line)}
.readin li b{color:var(--red)}
.colophon{margin-top:14px;border-top:4px double var(--ink);padding-top:8px}
.colophon .credits{font-family:"PT Sans",sans-serif;font-size:10.5px}
.colophon .made{margin-top:3px;font-family:"PT Sans",sans-serif;font-size:9.5px;color:var(--mut)}
.backpill{display:block;width:max-content;margin:10px auto 0;padding:7px 16px;border:1px solid var(--red);
border-radius:999px;color:var(--red);font-family:"PT Sans",sans-serif;font-weight:700;font-size:11px;
text-decoration:none;box-shadow:0 0 12px rgba(158,27,27,.2);transition:.25s}
.backpill:hover{background:var(--red);color:var(--paper)}
/* ---- навигация перелистывания ---- */
.navbar{display:flex;align-items:center;gap:14px;padding:10px 0 2px;
font-family:"PT Sans",sans-serif;font-size:11px;letter-spacing:.1em;color:var(--mut)}
.navbar button{background:none;border:1px solid var(--line);color:var(--ink);width:34px;height:30px;
border-radius:4px;cursor:pointer;font-size:15px;line-height:1;transition:.2s}
.navbar button:hover{border-color:var(--red);color:var(--red);transform:translateX(1px)}
.navbar button:first-child:hover{transform:translateX(-1px)}
.dots{display:flex;gap:5px}
.dots span{width:7px;height:7px;border-radius:50%;background:#c9c2b2;transition:.25s}
.dots span.on{background:var(--red);transform:scale(1.25)}
.pageno{text-transform:uppercase}
/* ---- адаптив: на мобильном лист можно прокручивать внутри ---- */
@media(max-width:820px){
 body{padding:8px 6px}
 .stage{display:block}
 .sheet-wrap{width:100%!important;height:auto!important}
 .book{position:relative;width:100%!important;height:auto!important;transform:none!important;perspective:none}
 .page{position:relative;display:none;opacity:1;visibility:visible;transform:none!important;
 max-height:80vh;overflow-y:auto;box-shadow:0 6px 18px rgba(40,36,28,.18)}
 .page.cur{display:block}
 .page::after{display:none}
 .cols2,.cols3{columns:1}
 .g-side,.g-side-rev,.briefs{grid-template-columns:1fr}
}
@media(max-height:760px) and (min-width:821px){
 .page{overflow-y:auto}
}
"""

JS = """
(function(){
var pages=[].slice.call(document.querySelectorAll('.page'));
var dots=[].slice.call(document.querySelectorAll('.dots span'));
var label=document.getElementById('pageno');
var cur=0,busy=false;
function paint(){dots.forEach(function(d,i){d.classList.toggle('on',i===cur)});
label.textContent='Страница '+(cur+1)+' из '+pages.length;}
function go(n,dir){
 if(busy||n===cur||n<0||n>=pages.length)return;busy=true;
 var out=pages[cur],inn=pages[n];
 inn.classList.add(dir>0?'in-r':'in-l');
 void inn.offsetWidth;
 out.classList.add(dir>0?'out-l':'out-r');
 inn.classList.remove('in-r','in-l');inn.classList.add('cur');
 setTimeout(function(){out.classList.remove('cur','out-l','out-r');cur=n;paint();busy=false;},580);
}
window.sfnGo=function(d){go(cur+d,d)};
document.addEventListener('keydown',function(e){
 if(e.key==='ArrowRight'||e.key==='PageDown'){go(cur+1,1);e.preventDefault();}
 if(e.key==='ArrowLeft'||e.key==='PageUp'){go(cur-1,-1);e.preventDefault();}
 if(e.key==='Home'){go(0,-1);} if(e.key==='End'){go(pages.length-1,1);}});
var tx=null;
document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;},{passive:true});
document.addEventListener('touchend',function(e){if(tx===null)return;
 var dx=e.changedTouches[0].clientX-tx;tx=null;
 if(Math.abs(dx)>56){go(cur+(dx<0?1:-1),dx<0?1:-1);}},{passive:true});
paint();
})();
"""


def fig(a, h, w='100%'):
    return (f'<figure><div class="ph" style="height:{h}px"><img src="{IMG[a["key"]]}" alt="{a["alt"]}"></div>'
            f'<figcaption>{a["cap"]}</figcaption></figure>')


def paras(ps, cols='cols2'):
    return f'<div class="{cols}">' + ''.join(f'<p>{p}</p>' for p in ps) + '</div>'


def side(a, photo_h, rev=False, fact=None, sub=None, ps=None):
    txt = (f'<div class="kicker">{a["kicker"]}</div><h3>{a["title"]}</h3>'
           f'<div class="stand">{a["stand"]}</div>')
    if fact:
        txt += f'<div class="fact"><span class="lbl">Ключевая деталь</span><span class="q">«{fact}»</span></div>'
    if sub:
        txt += f'<h4 class="sub">{sub}</h4>'
    txt += paras(ps or a['paras'], 'cols1')
    ph = fig(a, photo_h)
    cls = 'g-side-rev' if rev else 'g-side'
    return f'<article class="{cls}">{("<div>"+ph+"</div><div>"+txt+"</div>") if not rev else ("<div>"+txt+"</div><div>"+ph+"</div>")}</article>'


P = []
P.append("""<!DOCTYPE html>
<html lang="ru">
<head>
<!-- © 2026 San Fierro News / Jonny Wilde. Дизайн и вёрстка защищены: CC BY-NC-ND 4.0. Копирование и переработка запрещены. -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>San Fierro News — ежедневный выпуск по штату от 03.10.2026</title>
<meta name="description" content="Ежедневный выпуск по штату San Andreas в семи полосах с перелистыванием: гибель двоих полицейских на трассе под Лас-Вентурасом, торги за AngelPine Gas со ставкой $100 млн, военные на КПП, вертолёт в тоннеле и яхта в парковом пруду — 12 кадров дня.">
<style>
""")
P.append(CSS)
P.append('</style>\n</head>\n<body>\n<div class="stage"><div class="sheet-wrap" id="sheet"><div class="book">\n')

# ================= ПОЛОСА 1 =================
P.append('<section class="page page-1 cur">')
P.append('<div class="masttop"><span>Независимая редакция · штат San Andreas</span><span>суббота, 3 октября 2026</span></div>')
P.append('<div class="mastname">San Fierro <i>News</i></div>')
P.append('<div class="mastmeta"><span><b>№ 30</b></span><span>ежедневный выпуск</span><span>Лос-Сантос — Лас-Вентурас — трассы штата</span><span>12 материалов</span><span>7 полос</span></div>')
P.append(f'<div class="mastcred">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>'
         f'<div style="height:12px"></div>'
         f'<div class="kicker">{LEAD["kicker"]}</div><h1>{LEAD["title"]}</h1><div class="stand">{LEAD["stand"]}</div>')
P.append(fig(LEAD, 285))
P.append(paras(LEAD['paras'][:2], 'cols2'))
P.append('<div class="jump">Продолжение на стр. 2</div>')
P.append('<div class="briefs">')
for a in (TRUCK, CRASH):
    P.append(f'<article><div class="kicker">{a["kicker"]}</div><h3>{a["title"]}</h3>'
             f'<div class="stand">{a["stand"]}</div><div class="jump">Продолжение на стр. 2</div></article>')
P.append('</div></section>\n')

# ================= ПОЛОСА 2 =================
P.append('<section class="page page-2">')
P.append('<div class="sechead"><span class="sq"></span><h2>Происшествия</h2><span class="pg">полоса 2</span></div>')
P.append('<div class="jump" style="margin:0 0 6px">Продолжение. Начало на стр. 1</div>')
P.append(f'<div class="fact"><span class="lbl">Ключевая деталь</span><span class="q">«По данным редакции, оба погибших — сотрудники полиции. Их имена и подразделения на момент выхода номера не назывались.»</span></div>')
P.append(f'<h4 class="sub">Вопросов больше, чем ответов</h4>')
P.append(paras(LEAD['paras'][2:], 'cols3'))
P.append(side(TRUCK, 190))
P.append(side(CRASH, 190))
P.append('</section>\n')

# ================= ПОЛОСА 3 =================
P.append('<section class="page page-3">')
P.append('<div class="sechead"><span class="sq"></span><h2>Происшествия · продолжение</h2><span class="pg">полоса 3</span></div>')
P.append(side(SQ, 200, rev=True))
P.append(f'<article>{fig(STOP, 150)}<div class="kicker">{STOP["kicker"]}</div><h3>{STOP["title"]}</h3>'
         f'<div class="stand">{STOP["stand"]}</div>{paras(STOP["paras"], "cols2")}</article>')
P.append('</section>\n')

# ================= ПОЛОСА 4 =================
P.append('<section class="page page-4">')
P.append('<div class="sechead"><span class="sq"></span><h2>Криминал и силовые структуры</h2><span class="pg">полоса 4</span></div>')
P.append(side(HWY, 195, fact='Тормозной след за чёрной машиной длинный и прямой, а сама она встала под углом к оси дороги.',
              sub='Версии без подтверждений'))
P.append(side(KPP, 195, rev=True))
P.append('</section>\n')

# ================= ПОЛОСА 5 =================
P.append('<section class="page page-5">')
P.append('<div class="sechead"><span class="sq"></span><h2>Экономика</h2><span class="pg">полоса 5</span></div>')
P.append(side(GAS, 195, fact='Цифра на тёмном табло выглядит ошибкой набора: сто миллионов долларов — предыдущая ставка.',
              sub='Борьба за актив'))
P.append(side(DRAG, 195, rev=True))
P.append('</section>\n')

# ================= ПОЛОСА 6 =================
P.append('<section class="page page-6">')
P.append('<div class="sechead"><span class="sq"></span><h2>Экономика · Необычные истории</h2><span class="pg">полоса 6</span></div>')
P.append(side(CAL, 195))
P.append(side(HELI, 195, rev=True,
              fact='И посреди полосы, на собственных полозьях, стоит светло-серый вертолёт — аккуратно, будто его припарковали по разметке.',
              sub='Как он оказался внутри'))
P.append('</section>\n')

# ================= ПОЛОСА 7 =================
P.append('<section class="page page-7">')
P.append('<div class="sechead"><span class="sq"></span><h2>Необычные истории</h2><span class="pg">полоса 7</span></div>')
P.append(side(YACHT, 200))
P.append('<div class="readin"><h5>Читайте в номере</h5><ul>')
P.append(''.join(f'<li><b>{w}</b> — {t}</li>' for w, t in READIN))
P.append('</ul></div>')
P.append('<div class="colophon"><div class="credits">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>'
         '<div class="made">выпуск очереди подшивки · 03.10.2026 · дизайн и вёрстка — редакция San Fierro News</div>'
         '<a class="backpill" href="newsroom.html">← Посмотреть все выпуски редакции</a></div>')
P.append('</section>\n')

P.append('</div></div></div>\n')
P.append('<nav class="navbar"><button onclick="sfnGo(-1)" aria-label="Предыдущая страница">‹</button>'
         '<div class="dots">' + '<span></span>' * 7 + '</div>'
         '<span class="pageno" id="pageno">Страница 1 из 7</span>'
         '<button onclick="sfnGo(1)" aria-label="Следующая страница">›</button></nav>\n')
P.append(f'<script>{JS}</script>\n')
P.append('<script>(function(){var s=document.getElementById("sheet"),b=document.querySelector(".book");'
         'function fit(){var ah=window.innerHeight-92,aw=window.innerWidth-24;'
         'var k=Math.min(ah/1000,aw/720,1);k=Math.max(k,.5);'
         'if(window.innerWidth<=820){s.style.width="100%";s.style.height="auto";b.style.transform="none";return;}'
         's.style.width=(720*k)+"px";s.style.height=(1000*k)+"px";b.style.transform="scale("+k+")";}'
         'fit();window.addEventListener("resize",fit);})();</script>\n')
P.append('<!-- SFN · 2026 · 029 · interactive-pages -->\n</body>\n</html>\n')

html = ''.join(P)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print(f'собрано v3: {OUT} · {len(html)//1024} КБ · полос: 7 · кадров: {len(IMG)}')
