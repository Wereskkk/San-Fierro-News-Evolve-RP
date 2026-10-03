#!/usr/bin/env python3
"""SFN: пересборщик выпуска 03.10.2026 (v2, классическая газетная композиция).
Дизайн: classic-broadsheet (SFN-DESIGN-029, редизайн по брифу главреда от 03.10.2026).
Содержание (тексты, лиды, подписи, кикеры, анонсы) импортируется ИЗ СБОРЩИКА v1
без единой правки — меняется только визуальная подача.
Выход: anna-malboro/daily-03-10-2026.html (очередь подшивки).
Запуск из корня репозитория:  python3 worktmp/build_daily_0310_state_v2.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1 = os.path.join(ROOT, 'worktmp', 'build_daily_0310_state.py')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')

# ---- импорт данных выпуска из v1 (без запуска его записи: OUT уходит в devnull) ----
src = open(V1, encoding='utf-8').read()
src = src.replace("OUT = os.path.join(ROOT, 'anna-malboro', 'daily-03-10-2026.html')",
                  "OUT = os.devnull")
ns = {'__name__': 'sfn_v1_data', '__file__': V1}
exec(compile(src, V1, 'exec'), ns)
IMG, LEAD, SEC, SECTIONS, READIN = ns['IMG'], ns['LEAD'], ns['SEC'], ns['SECTIONS'], ns['READIN']

CSS = """/* SFN-DESIGN-029: classic-broadsheet · 03.10.2026 */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,700&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=PT+Sans:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%;animation:fade .6s ease both}
@keyframes fade{from{opacity:0}to{opacity:1}}
:root{--paper:#f6f3ec;--ink:#1a1a18;--mut:#6e6a63;--line:#d8d2c6;--red:#9e1b1b;--box:#efeade}
body{background:var(--paper);color:var(--ink);font-family:"PT Serif",Georgia,serif;-webkit-font-size-adjust:100%}
.sans{font-family:"PT Sans","PT Serif",Arial,sans-serif}
.wrap{max-width:68rem;margin:0 auto;padding:0 1.25rem}
a{color:var(--red);text-decoration:none;transition:color .2s}
/* ---- шапка: компактная, 10-15% первого экрана ---- */
.mast{padding-top:1rem}
.masttop{display:flex;justify-content:space-between;gap:1rem;align-items:baseline;
font-family:"PT Sans",sans-serif;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.mastname{font-family:"Playfair Display",Georgia,serif;font-weight:900;text-align:center;
font-size:clamp(1.9rem,4.2vw,2.9rem);letter-spacing:.01em;line-height:1.1;padding:.55rem 0 .4rem}
.mastname i{font-style:normal;color:var(--red)}
.mastmeta{display:flex;flex-wrap:wrap;justify-content:center;gap:.25rem 1.1rem;
font-family:"PT Sans",sans-serif;font-size:.76rem;letter-spacing:.06em;color:var(--ink);
border-top:1px solid var(--ink);border-bottom:4px double var(--ink);padding:.5rem 0 .55rem}
.mastmeta b{color:var(--red);font-weight:700}
.mastcred{margin-top:.45rem;text-align:center;font-family:"PT Sans",sans-serif;font-size:.7rem;color:var(--mut);letter-spacing:.05em}
/* ---- рубрики-кикеры, заголовки ---- */
.kicker{font-family:"PT Sans",sans-serif;font-size:.68rem;font-weight:700;letter-spacing:.2em;
text-transform:uppercase;color:var(--red);margin-bottom:.45rem}
h1,h3{font-family:"Playfair Display",Georgia,serif;font-weight:800;line-height:1.14;letter-spacing:-.004em}
h1{font-size:clamp(1.7rem,3.4vw,2.55rem);margin-bottom:.6rem}
h3{font-size:clamp(1.15rem,2vw,1.45rem);margin-bottom:.4rem}
.stand{font-style:italic;color:var(--mut);font-size:1rem;line-height:1.6;margin-bottom:.9rem}
/* ---- фото и подписи: без рамок, как в печати ---- */
figure{margin:0 0 1.1rem}
.ph{overflow:hidden;background:#ddd}
.ph img{width:100%;height:auto;object-fit:cover;object-position:top right}
.ph-big img{aspect-ratio:16/9}
.ph-wide img{aspect-ratio:21/9}
.ph-strip img{aspect-ratio:21/6}
.ph-side img{aspect-ratio:4/3}
figcaption{margin-top:.4rem;font-family:"PT Sans",sans-serif;font-size:.76rem;line-height:1.5;color:var(--mut)}
/* ---- текстовые колонки ---- */
.cols2{columns:2;column-gap:2.1rem;column-rule:1px solid var(--line)}
.cols2 p,.cols1 p{margin:0 0 .85rem;line-height:1.72;font-size:.99rem}
.cols1 p{font-size:.95rem}
h4.sub{font-family:"PT Sans",sans-serif;font-weight:700;font-size:.86rem;letter-spacing:.1em;
text-transform:uppercase;color:var(--ink);margin:1.1rem 0 .5rem}
/* ---- ключевая деталь / вынос ---- */
.fact{border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);background:var(--box);
padding:.75rem 1rem;margin:1.15rem 0}
.fact .lbl{font-family:"PT Sans",sans-serif;font-weight:700;font-size:.64rem;letter-spacing:.2em;
text-transform:uppercase;color:var(--red);display:block;margin-bottom:.3rem}
.fact .q{font-style:italic;font-size:1.02rem;line-height:1.55}
/* ---- композиции полос ---- */
.frow{display:grid;grid-template-columns:7.6fr 4.4fr;gap:2.3rem;margin-top:1.6rem;
padding-bottom:1.6rem;border-bottom:1px solid var(--line)}
.rail .art{margin-bottom:1.5rem;padding-bottom:1.3rem;border-bottom:1px solid var(--line)}
.rail .art:last-of-type{border-bottom:none;padding-bottom:0}
.readin{border-top:4px double var(--ink);border-bottom:1px solid var(--line);padding:.7rem 0 .8rem;margin-top:.4rem}
.readin h5{font-family:"PT Sans",sans-serif;font-weight:700;font-size:.72rem;letter-spacing:.18em;
text-transform:uppercase;margin-bottom:.45rem}
.readin li{list-style:none;font-family:"PT Sans",sans-serif;font-size:.78rem;line-height:1.55;
padding:.3rem 0;border-top:1px dotted var(--line);color:var(--ink)}
.readin li b{color:var(--red)}
.sechead{display:flex;align-items:baseline;gap:.6rem;margin:2.6rem 0 1.3rem;
border-top:1px solid var(--ink);padding-top:.5rem}
.sechead .sq{width:8px;height:8px;background:var(--red);flex:0 0 8px;transform:translateY(-1px)}
.sechead h2{font-family:"PT Sans",sans-serif;font-weight:700;font-size:.92rem;letter-spacing:.18em;text-transform:uppercase}
.sechead .pg{margin-left:auto;font-family:"PT Sans",sans-serif;font-size:.7rem;color:var(--mut);letter-spacing:.08em}
.art{margin:0 0 2.1rem}
.g-side{display:grid;grid-template-columns:5fr 7fr;gap:1.8rem;align-items:start}
.g-side-rev{display:grid;grid-template-columns:7fr 5fr;gap:1.8rem;align-items:start}
.g-pair{display:grid;grid-template-columns:1fr 1fr;gap:2.2rem}
.g-pair>.art+.art{border-left:1px solid var(--line);padding-left:2.2rem}
/* ---- подвал ---- */
.foot{border-top:4px double var(--ink);margin-top:3rem;padding:1.1rem 0 3rem}
.foot .credits{font-family:"PT Sans",sans-serif;font-size:.76rem;letter-spacing:.05em}
.foot .made{margin-top:.35rem;font-family:"PT Sans",sans-serif;font-size:.7rem;color:var(--mut)}
.backpill{display:block;width:max-content;margin:1.6rem auto 0;padding:.7rem 1.5rem;
border:1px solid var(--red);border-radius:999px;color:var(--red);
font-family:"PT Sans",sans-serif;font-weight:700;font-size:.88rem;
box-shadow:0 0 14px rgba(158,27,27,.22);transition:.25s}
.backpill:hover{background:var(--red);color:var(--paper);box-shadow:0 0 20px rgba(158,27,27,.35)}
/* ---- лёгкое появление при прокрутке (только при живом JS) ---- */
.js .rv{opacity:0;transform:translateY(10px);transition:opacity .55s ease,transform .55s ease}
.js .rv.in{opacity:1;transform:none}
/* ---- адаптив ---- */
@media(max-width:920px){
 .frow{grid-template-columns:1fr}
 .cols2{columns:1}
 .g-side,.g-side-rev,.g-pair{grid-template-columns:1fr}
 .g-pair>.art+.art{border-left:none;padding-left:0}
 .ph-strip img{aspect-ratio:16/7}
 .mastmeta{justify-content:flex-start}
}
"""


def fig(a, size):
    return (f'<figure><div class="ph ph-{size}"><img src="{IMG[a["key"]]}" alt="{a["alt"]}"></div>'
            f'<figcaption>{a["cap"]}</figcaption></figure>')


def body_blocks(a, cols='cols2', pull=None, pull_after=0, sub=None, sub_before=2):
    """Тело статьи: колонки + вынос (pull) сразу после абзаца pull_after
    и подзаголовок (sub) перед абзацем sub_before. Тексты — без правок."""
    out, buf = [], []

    def flush():
        if buf:
            out.append(f'<div class="{cols}">' + ''.join(f'<p>{p}</p>' for p in buf) + '</div>')
            buf.clear()

    for i, p in enumerate(a['paras']):
        if sub and i == sub_before:
            flush()
            out.append(f'<h4 class="sub">{sub}</h4>')
        buf.append(p)
        if pull and i == pull_after:
            flush()
            out.append(f'<div class="fact"><span class="lbl">Ключевая деталь</span>'
                       f'<span class="q">«{pull}»</span></div>')
    flush()
    return ''.join(out)


P = []
P.append("""<!DOCTYPE html>
<html lang="ru">
<head>
<!-- © 2026 San Fierro News / Jonny Wilde. Дизайн и вёрстка защищены: CC BY-NC-ND 4.0. Копирование и переработка запрещены. -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>San Fierro News — ежедневный выпуск по штату от 03.10.2026</title>
<meta name="description" content="Ежедневный выпуск по штату San Andreas: гибель двоих полицейских на трассе под Лас-Вентурасом, торги за AngelPine Gas со ставкой $100 млн, военные на КПП, вертолёт в тоннеле и яхта в парковом пруду — 12 кадров дня.">
<style>
""")
P.append(CSS)
P.append("""</style>
</head>
<body>
<header class="wrap mast">
<div class="masttop"><span>Независимая редакция · штат San Andreas</span><span>суббота, 3 октября 2026</span></div>
<div class="mastname">San Fierro <i>News</i></div>
<div class="mastmeta"><span><b>№ 30</b></span><span>ежедневный выпуск</span><span>Лос-Сантос — Лас-Вентурас — трассы штата</span><span>12 материалов</span><span>5 полос</span></div>
<div class="mastcred">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>
</header>
<main class="wrap">
""")

# ---------- ПЕРВАЯ ПОЛОСА: главный материал + боковая колонка ----------
P.append('<section class="frow rv"><div class="leadart">')
P.append(f'<div class="kicker">{LEAD["kicker"]}</div><h1>{LEAD["title"]}</h1>'
         f'<div class="stand">{LEAD["stand"]}</div>')
P.append(fig(LEAD, 'big'))
P.append(body_blocks(LEAD, 'cols2',
                     pull='По данным редакции, оба погибших — сотрудники полиции. Их имена и подразделения на момент выхода номера не назывались.',
                     pull_after=1,
                     sub='Вопросов больше, чем ответов', sub_before=2))
P.append('</div><aside class="rail">')
for a in SEC:
    P.append(f'<article class="art rv"><div class="kicker">{a["kicker"]}</div><h3>{a["title"]}</h3>'
             f'<div class="stand">{a["stand"]}</div>'
             f'{fig(a, "side")}<div class="cols1">' + ''.join(f'<p>{p}</p>' for p in a['paras']) + '</div></article>')
P.append('<div class="readin"><h5>Читайте в номере</h5><ul>')
P.append(''.join(f'<li><b>{w}</b> — {t}</li>' for w, t in READIN))
P.append('</ul></div></aside></section>')

# ---------- ПОЛОСА 2: происшествия ----------
s = SECTIONS[0]
P.append(f'<section class="rv"><div class="sechead"><span class="sq"></span><h2>{s["name"]}</h2><span class="pg">{s["no"]}</span></div>')
sq_, stop_ = s['arts']
P.append(f'<article class="art g-side rv"><div>{fig(sq_, "side")}</div><div>'
         f'<div class="kicker">{sq_["kicker"]}</div><h3>{sq_["title"]}</h3>'
         f'<div class="stand">{sq_["stand"]}</div><div class="cols1">' +
         ''.join(f'<p>{p}</p>' for p in sq_['paras']) + '</div></div></article>')
P.append(f'<article class="art rv">{fig(stop_, "strip")}'
         f'<div class="kicker">{stop_["kicker"]}</div><h3>{stop_["title"]}</h3>'
         f'<div class="stand">{stop_["stand"]}</div><div class="cols2">' +
         ''.join(f'<p>{p}</p>' for p in stop_['paras']) + '</div></article></section>')

# ---------- ПОЛОСА 3: криминал и силовые структуры ----------
s = SECTIONS[1]
P.append(f'<section class="rv"><div class="sechead"><span class="sq"></span><h2>{s["name"]}</h2><span class="pg">{s["no"]}</span></div>')
hwy_, kpp_ = s['arts']
P.append(f'<article class="art rv"><div class="kicker">{hwy_["kicker"]}</div><h3>{hwy_["title"]}</h3>'
         f'<div class="stand">{hwy_["stand"]}</div>{fig(hwy_, "wide")}')
P.append(body_blocks(hwy_, 'cols2',
                     pull='Тормозной след за чёрной машиной длинный и прямой, а сама она встала под углом к оси дороги.',
                     sub='Версии без подтверждений'))
P.append('</article>')
P.append(f'<article class="art g-side-rev rv"><div><div class="kicker">{kpp_["kicker"]}</div>'
         f'<h3>{kpp_["title"]}</h3><div class="stand">{kpp_["stand"]}</div><div class="cols1">' +
         ''.join(f'<p>{p}</p>' for p in kpp_['paras']) + '</div></div><div>' + fig(kpp_, 'side') + '</div></article></section>')

# ---------- ПОЛОСА 4: экономика и городская жизнь ----------
s = SECTIONS[2]
P.append(f'<section class="rv"><div class="sechead"><span class="sq"></span><h2>{s["name"]}</h2><span class="pg">{s["no"]}</span></div>')
gas_, dragons_, caligula_ = s['arts']
P.append(f'<article class="art rv"><div class="kicker">{gas_["kicker"]}</div><h3>{gas_["title"]}</h3>'
         f'<div class="stand">{gas_["stand"]}</div>{fig(gas_, "wide")}')
P.append(body_blocks(gas_, 'cols2',
                     pull='Цифра на тёмном табло выглядит ошибкой набора: сто миллионов долларов — предыдущая ставка.',
                     sub='Борьба за актив'))
P.append('</article><div class="g-pair">')
for a in (dragons_, caligula_):
    P.append(f'<article class="art rv">{fig(a, "side")}<div class="kicker">{a["kicker"]}</div>'
             f'<h3>{a["title"]}</h3><div class="stand">{a["stand"]}</div><div class="cols1">' +
             ''.join(f'<p>{p}</p>' for p in a['paras']) + '</div></article>')
P.append('</div></section>')

# ---------- ПОЛОСА 5: необычные истории ----------
s = SECTIONS[3]
P.append(f'<section class="rv"><div class="sechead"><span class="sq"></span><h2>{s["name"]}</h2><span class="pg">{s["no"]}</span></div>')
heli_, yacht_ = s['arts']
P.append(f'<article class="art rv"><div class="kicker">{heli_["kicker"]}</div><h3>{heli_["title"]}</h3>'
         f'<div class="stand">{heli_["stand"]}</div>{fig(heli_, "big")}')
P.append(body_blocks(heli_, 'cols2',
                     pull='И посреди полосы, на собственных полозьях, стоит светло-серый вертолёт — аккуратно, будто его припарковали по разметке.',
                     sub='Как он оказался внутри'))
P.append('</article>')
P.append(f'<article class="art g-side rv"><div>{fig(yacht_, "side")}</div><div>'
         f'<div class="kicker">{yacht_["kicker"]}</div><h3>{yacht_["title"]}</h3>'
         f'<div class="stand">{yacht_["stand"]}</div><div class="cols1">' +
         ''.join(f'<p>{p}</p>' for p in yacht_['paras']) + '</div></div></article></section>')

P.append("""<footer class="foot">
<div class="credits">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст/Редактор: Jonny Wilde</div>
<div class="made">выпуск очереди подшивки · 03.10.2026<br>дизайн и вёрстка — редакция San Fierro News</div>
<a class="backpill" href="newsroom.html">← Посмотреть все выпуски редакции</a>
</footer>
</main>
<script>
(function(){var d=document.documentElement;d.classList.add('js');
var els=[].slice.call(document.querySelectorAll('.rv'));
if(!('IntersectionObserver'in window)){els.forEach(function(e){e.classList.add('in')});return;}
var io=new IntersectionObserver(function(en){en.forEach(function(x){
if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.08});
els.forEach(function(e){io.observe(e)})})();
</script>
<!-- SFN · 2026 · 029 · classic-broadsheet -->
</body>
</html>
""")

html = ''.join(P)
with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print(f'собрано v2: {OUT} · {len(html)//1024} КБ · кадров: {len(IMG)}')
