# -*- coding: utf-8 -*-
# Сборка ежедневного выпуска 02.10.2026 по Las Venturas — дизайн «CASINO NOIR»
import math, random

W = "worktmp/lv"

def rb(p):
    return open(p, encoding="utf-8").read().strip()

# ---------- fonts ----------
F_RUSSO = rb(f"{W}/font_RussoOne-Regular.b64")
F_MARCK = rb(f"{W}/font_MarckScript-Regular.b64")
F_PTSN  = rb(f"{W}/font_PT_Sans-Narrow-Web-Bold.b64")
F_BEBAS = rb(f"{W}/font_BebasNeue-Regular.b64")

# ---------- images ----------
IMG = {f"{i:02d}": rb(f"{W}/img{i:02d}.b64") for i in range(1, 9)}

# ---------- stars ----------
random.seed(42)
stars = []
for _ in range(120):
    x = random.uniform(0, 1440); y = random.uniform(0, 540)
    r = random.uniform(0.5, 1.7); o = random.uniform(0.18, 0.85)
    stars.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fff" opacity="{o:.2f}"/>')
STARS = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 560" preserveAspectRatio="xMidYMin slice">'
         + "".join(stars) + '</svg>')
import base64, urllib.parse
STARS_URI = "data:image/svg+xml," + urllib.parse.quote(STARS)
GRAIN_URI = ("data:image/svg+xml," + urllib.parse.quote(
    '<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160"><filter id="n">'
    '<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2"/><feColorMatrix type="saturate" values="0"/>'
    '</filter><rect width="160" height="160" filter="url(#n)" opacity="0.5"/></svg>'))

# ---------- twinkles ----------
tw = []
tw_pos = [(8,12),(23,6),(41,15),(58,8),(72,17),(86,10),(15,24),(64,25),(93,20),(34,4)]
for i,(x,y) in enumerate(tw_pos):
    tw.append(f'<span class="tw" style="left:{x}%;top:{y}%;animation-delay:{i*0.7:.1f}s"></span>')
TWINKLE = "".join(tw)

# ---------- marquee bulbs ----------
BULB_COLORS = ["#f6c453", "#ff2e88", "#2fe8c8", "#9b6bff"]
bulbs = "".join(
    f'<span class="bulb" style="--bc:{BULB_COLORS[i % 4]};animation-delay:{i * 0.09:.2f}s"></span>'
    for i in range(48))

# ---------- roulette tape (0..36) ----------
RED = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
def tape_cell(n):
    cls = "t-zero" if n == 0 else ("t-red" if n in RED else "t-blk")
    return f'<span class="tnum {cls}">{n}</span>'
TAPE = "".join(tape_cell(n) for n in range(37))

# ---------- roulette wheel SVG ----------
ORDER = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
seg = []
step = 360.0 / 37
for i, n in enumerate(ORDER):
    a0 = math.radians(-90 + i * step - step / 2)
    a1 = math.radians(-90 + i * step + step / 2)
    R1, R2 = 118.0, 188.0
    x0o, y0o = 200 + R2 * math.cos(a0), 200 + R2 * math.sin(a0)
    x1o, y1o = 200 + R2 * math.cos(a1), 200 + R2 * math.sin(a1)
    x0i, y0i = 200 + R1 * math.cos(a1), 200 + R1 * math.sin(a1)
    x1i, y1i = 200 + R1 * math.cos(a0), 200 + R1 * math.sin(a0)
    fill = "#14804a" if n == 0 else ("#b3123f" if n in RED else "#191120")
    seg.append(f'<path d="M{x0o:.1f},{y0o:.1f} A{R2},{R2} 0 0 1 {x1o:.1f},{y1o:.1f} '
               f'L{x0i:.1f},{y0i:.1f} A{R1},{R1} 0 0 0 {x1i:.1f},{y1i:.1f} Z" fill="{fill}" stroke="#f6c453" stroke-width="0.6" stroke-opacity="0.55"/>')
WHEEL = f'''<svg viewBox="0 0 400 400" aria-hidden="true">
<g class="wspin">
{''.join(seg)}
<circle cx="200" cy="200" r="188" fill="none" stroke="#f6c453" stroke-width="5"/>
<circle cx="200" cy="200" r="195" fill="none" stroke="#f6c453" stroke-width="1.5" stroke-opacity="0.5"/>
<g class="wball"><circle cx="200" cy="42" r="6" fill="#fff" opacity="0.95"/><circle cx="200" cy="42" r="10" fill="#fff" opacity="0.18"/></g>
</g>
<circle cx="200" cy="200" r="116" fill="url(#cone)"/>
<g stroke="#f6c453" stroke-width="3" stroke-linecap="round" opacity="0.9">
<line x1="200" y1="90" x2="200" y2="150"/><line x1="200" y1="250" x2="200" y2="310"/>
<line x1="90" y1="200" x2="150" y2="200"/><line x1="250" y1="200" x2="310" y2="200"/>
</g>
<circle cx="200" cy="200" r="42" fill="#120a18" stroke="#f6c453" stroke-width="3"/>
<text x="200" y="211" text-anchor="middle" font-family="BebasNeue,sans-serif" font-size="30" letter-spacing="2" fill="#f6c453">LV</text>
<defs><radialGradient id="cone" cx="50%" cy="42%" r="70%"><stop offset="0%" stop-color="#f6d98a"/><stop offset="55%" stop-color="#c99b3f"/><stop offset="100%" stop-color="#6e5220"/></radialGradient></defs>
</svg>'''

# ---------- skyline ----------
TOWERS = [(60,70,120),(150,40,80),(210,90,150),(330,50,95),(420,70,130),(520,35,70),(600,110,170),
          (740,55,100),(830,80,140),(940,45,85),(1020,95,160),(1150,60,110),(1240,80,135),(1360,50,90)]
sky = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 220" preserveAspectRatio="xMidYMax slice">']
sky.append('<path d="M0,220 L0,150 L120,108 L260,158 L400,92 L560,148 L700,102 L850,158 L1000,118 L1150,162 L1300,108 L1440,148 L1440,220 Z" fill="#150c1f"/>')
for x, w, h in TOWERS:
    y = 220 - h
    sky.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#1d1029"/>')
    sky.append(f'<rect x="{x+8}" y="{y+10}" width="4" height="4" fill="#f6c453" opacity="0.5"/>')
    sky.append(f'<rect x="{x+w-14}" y="{y+22}" width="4" height="4" fill="#2fe8c8" opacity="0.4"/>')
    sky.append(f'<line x1="{x+w//2}" y1="{y}" x2="{x+w//2}" y2="{y-12}" stroke="#1d1029" stroke-width="3"/>')
    sky.append(f'<circle cx="{x+w//2}" cy="{y-14}" r="2.4" fill="#ff2e88" opacity="0.8"/>')
sky.append('</svg>')
SKYLINE = '<svg viewBox="0 0 1440 220" preserveAspectRatio="xMidYMax slice" aria-hidden="true">' + "".join(sky[1:-1]) + '</svg>'

# ---------- dice / chips divider ----------
DIVIDER = '''<div class="divider" aria-hidden="true"><svg viewBox="0 0 230 60" width="210" height="55">
<g transform="rotate(-10 45 30)"><rect x="22" y="8" width="44" height="44" rx="10" fill="#f3e9f5"/>
<circle cx="34" cy="20" r="4" fill="#171019"/><circle cx="54" cy="20" r="4" fill="#171019"/><circle cx="44" cy="30" r="4" fill="#171019"/><circle cx="34" cy="40" r="4" fill="#171019"/><circle cx="54" cy="40" r="4" fill="#171019"/></g>
<g transform="rotate(9 105 32)"><rect x="82" y="10" width="44" height="44" rx="10" fill="#f3e9f5"/>
<circle cx="94" cy="22" r="4" fill="#b3123f"/><circle cx="114" cy="42" r="4" fill="#b3123f"/></g>
<g><rect x="160" y="34" width="48" height="13" rx="6.5" fill="#b3123f" stroke="#f6c453" stroke-width="1.2"/>
<rect x="160" y="23" width="48" height="13" rx="6.5" fill="#1f1420" stroke="#f6c453" stroke-width="1.2"/>
<rect x="160" y="12" width="48" height="13" rx="6.5" fill="#14804a" stroke="#f6c453" stroke-width="1.2"/></g>
</svg></div>'''

# ---------- sign letters ----------
SIGN_LETTERS = "LAS·VENTURAS".replace("·", "")
sign = []
for i, ch in enumerate("LASVENTURAS"):
    cls = "sl fl1" if i in (2, 7) else ("sl fl2" if i == 9 else "sl")
    col = "#2fe8c8" if i % 4 == 3 else "#f6c453"
    sign.append(f'<span class="{cls}" style="--lc:{col}">{ch}</span>')
SIGN = "".join(sign)

# ---------- sections ----------
SECS = [
 dict(n="01", rank="A", suit="&#9824;", suitname="Пиковый туз", acc="#7de8ff",
      title="Башня родственных перьев", plate="Офис Las Venturas News", img="01",
      alt="Офис редакции Las Venturas News",
      text="Колода сегодняшнего номера открывается тузом — и он принадлежит коллегам. Башня Las Venturas News стоит в самом сердце города: те же дедлайны, те же горячие телефоны, тот же кофе у пресс-машины — только неон за окном другого цвета. Каждое утро отсюда местная газета уезжает в киоски, а каждый вечер её редакторы так же яростно спорят о заголовках, как наши. San Fierro News протягивает руку через весь штат: пусть тиражи растут, наборщик не клинит, а первая полоса всегда находит место для хорошей новости.",
      chips=[("STRIP", "Редакция — в самом сердце неонового квартала"), ("24/7", "Лента новостей не спит — как и город")],
      link=None),
 dict(n="02", rank="K", suit="&#9829;", suitname="Червонный король", acc="#ff4d7d",
      title="Там, где машинам возвращают вторую жизнь", plate="Автомастерская города Las Venturas", img="02",
      alt="Автомастерская города Las Venturas",
      text="Король червей достался тем, у кого под ногтями масло. Городская автомастерская — адрес, где машинам возвращают вторую жизнь: от подлатанного колеса до капитальной переборки мотора. Из-под подъёмников летят искры, в глубине цеха негромко играет радио, а мастер обходит крыло с планшетом, как врач — палату. В городе, который построен на лошадиных силах, это место важнее любого казино: здесь удачу меряют не фишками, а моментом затяжки.",
      chips=[("ИСКРА", "Из-под подъёмника — ярче любого неона"), ("МОТОР", "Вторая жизнь для сердца машины")],
      link=None),
 dict(n="03", rank="Q", suit="&#9830;", suitname="Бубновая дама", acc="#ff4d7d",
      title="Ход королевы", plate="LVPD", img="03",
      alt="Полицейский департамент LVPD",
      text="Дама бубен следит за тем, чтобы улицы оставались улицами, а не декорацией к вестерну. LVPD — департамент, где развод начинается до рассвета, а смена заканчивается далеко за полночь. Во дворе ровным строем стоят патрульные машины, рация сыплет адресами, а за стеклянной дверью дежурной части висит доска с ориентировками на тех, кто путает чужое с ничейным. Дама не повышает голос — она просто делает ход. И в Las Venturas этот ход всегда точный.",
      chips=[("СМЕНА", "Развод до рассвета — отбой за полночь"), ("ПОРЯДОК", "Ход королевы всегда точный")],
      link=None),
 dict(n="04", rank="J", suit="&#9827;", suitname="Трефовый валет", acc="#7de8ff",
      title="Деньги любят тишину", plate="Банк города Las Venturas", img="04",
      alt="Банк города Las Venturas",
      text="Валет треф хранит чужие секреты лучше, чем кто-либо в городе. Городской банк — адрес, где все одинаково вежливы и одинаково немногословны. Мрамор, латунь, негромкие стойки — а за ними хранилище, которое видело больше денег, чем все казино Strip вместе взятые. Правило «деньги любят тишину» здесь написано до того, как ты вошёл в дверь. Валет умеет держать удар — и умеет держать слово: городские счета спят спокойнее любых гостей отеля.",
      chips=[("СЕЙФ", "За тихими стойками — самый молчаливый зал города"), ("ЛАТУНЬ", "Мрамор и латунь — дресс-код банка")],
      link=None),
 dict(n="05", rank="10", suit="&#9824;", suitname="Пиковая десятка", acc="#7de8ff",
      title="Витрина под открытым небом", plate="Авторынок в городе Las Venturas", img="05",
      alt="Авторынок в городе Las Venturas",
      text="Десятка пик — самая большая витрина под открытым небом в штате. Ряды машин под навесами, капоты распахнуты, как крылья, а менеджер шагает между рядами с уверенностью крупье за собственным столом. Здесь находят всё: от честной рабочей лошадки до машины с характером и историей. Этот адрес редакция уже разбирала подробно — в фоторепортаже «Главный автобазар штата»; сегодня он просто занимает законное место в колоде.",
      chips=[("СДЕЛКА", "Менеджер ходит между рядами, как крупье"), ("РЯД", "Машины под навесами — до самого горизонта")],
      link=("fotoreport-avtobazar-lv.html", "Фоторепортаж: Главный автобазар штата")),
 dict(n="06", rank="9", suit="&#9829;", suitname="Червонная девятка", acc="#ff4d7d",
      title="Ворота города", plate="Автовокзал города Las Venturas", img="06",
      alt="Автовокзал города Las Venturas",
      text="Девятка червей — ворота города. Автовокзал встречает тех, кто приехал без собственного коня: касса, табло расписания и автобусы, один за другим уходящие в сторону Los Santos и San Fierro. Сюда приезжают за удачей — и отсюда же уезжают, оставив её в городе. Перрон не судит и не задаёт вопросов: он просто везёт. И в этом он честнее любого казино — билет в один конец стоит ровно столько, сколько на нём напечатано.",
      chips=[("БИЛЕТ", "Один билет — три города штата"), ("РЕЙС", "На восток, на запад, на юг — с одной платформы")],
      link=None),
 dict(n="07", rank="8", suit="&#9830;", suitname="Бубновая восьмёрка", acc="#ff4d7d",
      title="Главная люстра города", plate="Казино Caligula города Las Venturas", img="07",
      alt="Казино Caligula города Las Venturas",
      text="Восьмёрка бубен — и главная люстра города. Caligula в представлении не нуждается: мраморный двор, золото портика, а за дверями — зелёные столы, рулетка и та особенная тишина, которая бывает только вокруг большой ставки. Редакция уже проводила здесь вечер — в спецвыпуске «Империя удачи». Сегодняшняя карта лишь напоминает: дом всегда в плюсе, но красивую игру здесь помнят дольше, чем крупные проигрыши.",
      chips=[("СТАВКА", "Особенная тишина — только вокруг большой ставки"), ("ЗОЛОТО", "Портик Caligula — главная люстра города")],
      link=("caligulas-casino.html", "Спецвыпуск: Империя удачи — один вечер в Caligula's")),
 dict(n="08", rank="7", suit="&#9827;", suitname="Трефовая семёрка", acc="#7de8ff",
      title="Прикрытие неона", acc2="",
      plate="Армия Las Venturas", img="08",
      alt="Армейская база Las Venturas",
      text="Семёрка треф закрывает колоду — и делает это строевым шагом. Армейская база на восточной окраине — адрес, которого нет ни на одной туристической карте: КПП, шлагбаум, ровные ряды техники под навесами и плац, где утро начинается с команды, а не с рулетки. Пока на Strip горит неон и звенят фишки, здесь стоят на посту — чтобы праздник города не прерывался. Последняя карта номера всегда прикрывает игру: без неё колода не колода.",
      chips=[("ПОСТ", "КПП и шлагбаум — адрес не с туристической карты"), ("КАРАУЛ", "Чтобы праздник города не прерывался")],
      link=None),
]

def chip_html(tok, lab):
    return (f'<div class="chip"><span class="tok"><span class="tokw">{tok}</span></span><span class="clab">{lab}</span></div>')

sec_html = []
for i, s in enumerate(SECS):
    link_html = ""
    if s["link"]:
        href, label = s["link"]
        link_html = f'<a class="srclink" href="{href}">{label} →</a>'
    sec_html.append(f'''<section class="sec" id="s{s['n']}">
  <div class="pcard" style="--acc:{s['acc']}">
    <div class="corner ctl"><span class="crank">{s['rank']}</span><span class="csuit">{s['suit']}</span></div>
    <div class="corner cbr"><span class="crank">{s['rank']}</span><span class="csuit">{s['suit']}</span></div>
    <div class="sechead">
      <div class="secnum">{s['n']}</div>
      <div class="sechtxt">
        <h2>{s['title']}</h2>
        <div class="secsuit">{s['suitname']} · {s['rank']}{s['suit']}</div>
      </div>
    </div>
    <div class="shot"><img src="data:image/jpeg;base64,{IMG[s['img']]}" alt="{s['alt']}" loading="lazy"></div>
    <div class="plateline"><div class="plate">{s['plate']}</div></div>
    <p class="sectext">{s['text']}</p>
    <div class="chips">{chip_html(*s['chips'][0])}{chip_html(*s['chips'][1])}</div>
    {link_html}
  </div>
</section>''')
    if i < len(SECS) - 1:
        sec_html.append(DIVIDER)
SECTIONS = "\n".join(sec_html)

# ---------- page ----------
CSS = '''
*{margin:0;padding:0;box-sizing:border-box}
:root{
 --bg1:#0d0812; --bg2:#170d20;
 --mag:#ff2e88; --gold:#f6c453; --turq:#2fe8c8; --viol:#9b6bff;
 --ink:#f0e6f3; --mut:#b39dbd;
 --panel:rgba(255,255,255,.028);
 --line:rgba(246,196,83,.22);
}
html{scroll-behavior:smooth}
body{
 font-family:'PTSN',sans-serif; color:var(--ink);
 background:linear-gradient(180deg,#0d0812 0%,#170d20 45%,#120a1a 75%,#0d0812 100%);
 background-attachment:fixed; min-height:100vh; overflow-x:hidden;
}
body::before{content:"";position:fixed;inset:0 0 auto 0;height:70vh;z-index:0;pointer-events:none;
 background:url("@@STARS@@"),url("@@STARS@@");background-size:1440px 560px,900px 400px;
 background-position:top left,top right;background-repeat:no-repeat;opacity:.55}
body::after{content:"";position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.05;
 background:url("@@GRAIN@@");mix-blend-mode:overlay}
.wrap{position:relative;z-index:2;max-width:88rem;margin:0 auto;padding:0 22px 60px}
.mono{font-family:'BebasNeue',sans-serif;letter-spacing:2px}

/* ---- маркиза ---- */
.marquee{position:relative;z-index:3;display:flex;justify-content:space-between;gap:6px;
 padding:9px 18px;background:linear-gradient(180deg,#1a0f26,#0d0812);
 border-bottom:1px solid rgba(246,196,83,.35);box-shadow:0 6px 24px rgba(0,0,0,.5)}
.bulb{width:9px;height:9px;border-radius:50%;background:var(--bc);flex:0 0 auto;
 box-shadow:0 0 8px var(--bc),0 0 18px var(--bc);animation:blink 1.9s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.15}}

/* ---- hero ---- */
header{position:relative;overflow:hidden;padding:34px 0 8px}
.skyline{position:absolute;left:0;right:0;bottom:-6px;height:230px;z-index:0;opacity:.85;pointer-events:none}
.skyline svg{width:100%;height:100%}
.haze{position:absolute;left:50%;bottom:-40px;transform:translateX(-50%);width:min(1100px,96%);height:260px;z-index:0;
 background:radial-gradient(ellipse at center bottom,rgba(255,46,136,.16),rgba(155,107,255,.08) 45%,transparent 70%);
 pointer-events:none;filter:blur(4px)}
.tw{position:absolute;width:4px;height:4px;border-radius:50%;background:#fff;z-index:1;pointer-events:none;
 box-shadow:0 0 6px 2px rgba(255,255,255,.6);animation:twk 3.4s infinite}
@keyframes twk{0%,100%{opacity:.15;transform:scale(.7)}50%{opacity:.9;transform:scale(1.25)}}
.hero{position:relative;z-index:2;display:grid;grid-template-columns:auto 1fr auto;gap:38px;align-items:center;
 padding:26px 0 30px}
@media(max-width:960px){.hero{grid-template-columns:1fr;justify-items:center;text-align:center;gap:26px}}

/* вертикальная вывеска */
.sign{display:flex;flex-direction:column;align-items:center;gap:2px}
.signbase{width:58px;padding:16px 6px 14px;border:2px solid rgba(246,196,83,.55);border-radius:10px;
 background:linear-gradient(180deg,rgba(26,15,38,.92),rgba(13,8,18,.92));
 box-shadow:0 0 26px rgba(255,46,136,.28),inset 0 0 18px rgba(0,0,0,.6)}
.sl{display:block;font-family:'RussoOne',sans-serif;font-size:1.32rem;line-height:1.5;text-align:center;
 color:var(--lc);text-shadow:0 0 6px var(--lc),0 0 16px rgba(255,46,136,.75),0 0 34px rgba(255,46,136,.4)}
.fl1{animation:flick1 5.5s infinite}
.fl2{animation:flick2 7.2s infinite}
@keyframes flick1{0%,89%,91%,93%,100%{opacity:1}90%{opacity:.22}92%{opacity:.45}}
@keyframes flick2{0%,64%,66%,70%,72%,100%{opacity:1}65%{opacity:.3}71%{opacity:.5}}
.signpole{width:8px;height:44px;background:linear-gradient(90deg,#2a1b38,#4a3160,#2a1b38);margin:0 auto}
.signstar{font-family:'BebasNeue',sans-serif;color:var(--gold);font-size:1.1rem;text-align:center;
 text-shadow:0 0 10px rgba(246,196,83,.9);margin-bottom:4px}
@media(max-width:960px){.sign{flex-direction:row}.signbase{display:flex;flex-direction:row;padding:8px 14px;gap:4px}
 .sl{font-size:1.05rem}.signpole{width:44px;height:8px}.sign{flex-direction:column}}

.heromain{min-width:0}
.kicker{font-family:'BebasNeue',sans-serif;letter-spacing:3px;color:var(--turq);font-size:.95rem;
 text-shadow:0 0 10px rgba(47,232,200,.6);margin-bottom:10px}
h1{font-family:'RussoOne',sans-serif;font-weight:400;font-size:clamp(2rem,5.2vw,3.6rem);line-height:1.14;
 color:#fff5fa;text-shadow:0 0 8px rgba(255,46,136,.9),0 0 26px rgba(255,46,136,.55),0 0 60px rgba(155,107,255,.4)}
h1 .thin{color:var(--gold);text-shadow:0 0 8px rgba(246,196,83,.9),0 0 26px rgba(246,196,83,.5)}
.sub{margin-top:12px;color:var(--mut);font-size:1.06rem;line-height:1.65;max-width:62ch}
@media(max-width:960px){.sub{margin-left:auto;margin-right:auto}}
.jackpot{margin-top:22px;width:max-content;max-width:100%;padding:14px 26px 12px;border-radius:12px;
 border:2px solid var(--gold);background:linear-gradient(180deg,#160c20,#0d0812);position:relative;
 box-shadow:0 0 22px rgba(246,196,83,.28),inset 0 0 22px rgba(0,0,0,.65)}
@media(max-width:960px){.jackpot{margin-left:auto;margin-right:auto}}
/* SFN fix 03.10.2026: мобильная шапка без горизонтального оверфлоу (jackpot по max-content растягивал heromain) */
.marquee{overflow:hidden}
@media(max-width:960px){.heromain{min-width:0}.jackpot{width:auto;max-width:100%}.signbase{gap:6px}}

.jackpot::after{content:"";position:absolute;inset:0;border-radius:10px;pointer-events:none;
 background:repeating-linear-gradient(0deg,rgba(255,255,255,.05) 0 1px,transparent 1px 4px)}
.jplab{font-family:'BebasNeue',sans-serif;letter-spacing:4px;font-size:.8rem;color:var(--mag);
 text-shadow:0 0 8px rgba(255,46,136,.8)}
.jpdate{font-family:'BebasNeue',sans-serif;font-size:clamp(2.2rem,4.6vw,3.2rem);line-height:1.05;color:#ffe9b0;
 letter-spacing:4px;text-shadow:0 0 8px rgba(246,196,83,.9),0 0 26px rgba(246,196,83,.5),0 0 52px rgba(255,46,136,.3)}
.jpsub{font-family:'BebasNeue',sans-serif;letter-spacing:3px;font-size:.86rem;color:var(--turq);
 text-shadow:0 0 8px rgba(47,232,200,.6)}
.wheel{width:clamp(220px,26vw,320px);flex:0 0 auto}
.wheel svg{width:100%;height:auto;display:block;filter:drop-shadow(0 0 24px rgba(255,46,136,.35))}
.wspin{animation:spin 30s linear infinite;transform-origin:200px 200px}
.wball{animation:spinrev 12s linear infinite;transform-origin:200px 200px}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes spinrev{to{transform:rotate(-360deg)}}

/* ---- лид ---- */
.lead{position:relative;z-index:2;margin:26px auto 8px;max-width:76ch;text-align:center;
 font-size:1.14rem;line-height:1.85;color:#e9dcef}
.lead .ms{font-family:'MarckScript',cursive;font-size:1.5rem;color:var(--gold);
 text-shadow:0 0 12px rgba(246,196,83,.55)}

/* ---- секции-карты ---- */
.sec{position:relative;z-index:2;margin:0 auto;max-width:64rem}
.pcard{position:relative;padding:34px clamp(20px,4vw,46px) 40px;border-radius:20px;
 border:1px solid var(--line);background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.012));
 box-shadow:0 18px 44px rgba(0,0,0,.45);transition:transform .35s ease,box-shadow .35s ease,border-color .35s ease}
.pcard:hover{transform:rotate(-.45deg) translateY(-4px);border-color:color-mix(in srgb,var(--acc) 55%,transparent);
 box-shadow:0 26px 54px rgba(0,0,0,.55),0 0 42px color-mix(in srgb,var(--acc) 16%,transparent)}
.corner{position:absolute;display:flex;flex-direction:column;align-items:center;line-height:1;
 font-family:'BebasNeue',sans-serif;color:var(--gold);text-shadow:0 0 10px rgba(246,196,83,.5)}
.ctl{top:12px;left:16px}
.cbr{bottom:12px;right:16px;transform:rotate(180deg)}
.crank{font-size:1.5rem}
.csuit{font-size:1.05rem;color:var(--acc);text-shadow:0 0 10px color-mix(in srgb,var(--acc) 60%,transparent)}
.sechead{display:flex;align-items:center;gap:18px;margin-bottom:22px}
.secnum{font-family:'BebasNeue',sans-serif;font-size:2.6rem;line-height:1;color:transparent;
 -webkit-text-stroke:1.6px var(--gold);text-shadow:0 0 18px rgba(155,107,255,.55)}
h2{font-family:'RussoOne',sans-serif;font-weight:400;font-size:clamp(1.35rem,2.8vw,1.9rem);line-height:1.2;
 color:#fff;text-shadow:0 0 8px color-mix(in srgb,var(--acc) 80%,transparent),0 0 26px color-mix(in srgb,var(--acc) 45%,transparent)}
.secsuit{margin-top:5px;font-family:'BebasNeue',sans-serif;letter-spacing:2.5px;font-size:.9rem;color:var(--mut)}
.shot{border-radius:14px;overflow:hidden;border:1px solid rgba(246,196,83,.4);
 box-shadow:0 20px 44px rgba(0,0,0,.6),0 10px 34px color-mix(in srgb,var(--acc) 26%,transparent)}
.shot img{display:block;width:100%;height:auto}
.plateline{display:flex;justify-content:center;margin-top:-16px;position:relative;z-index:2}
.plate{width:max-content;max-width:92%;padding:7px 26px;border-radius:8px;text-align:center;
 font-family:'BebasNeue',sans-serif;letter-spacing:2.5px;font-size:.98rem;color:#241604;
 background:linear-gradient(180deg,#f6d98a,#d9a94a);border:1px solid #8a6a25;
 box-shadow:0 6px 18px rgba(0,0,0,.55),0 0 16px rgba(246,196,83,.28),inset 0 1px 0 rgba(255,255,255,.55)}
.sectext{margin:22px auto 0;max-width:70ch;font-size:1.06rem;line-height:1.8;color:#e7daec}
.chips{display:flex;flex-wrap:wrap;gap:22px;margin-top:24px;justify-content:center}
.chip{display:flex;align-items:center;gap:12px;transition:transform .3s ease}
.chip:hover{transform:translateY(-4px) rotate(-1.2deg)}
.tok{width:64px;height:64px;border-radius:50%;flex:0 0 auto;display:flex;align-items:center;justify-content:center;
 background:repeating-conic-gradient(#b3123f 0 10deg,#171019 10deg 20deg);padding:7px;
 box-shadow:0 6px 16px rgba(0,0,0,.5)}
.clab{max-width:26ch;font-size:.95rem;line-height:1.5;color:var(--mut)}
/* внутренний круг фишки */
.tokw{width:100%;height:100%;border-radius:50%;background:radial-gradient(circle at 38% 32%,#241730,#120a18);
 border:1px solid rgba(246,196,83,.5);display:flex;align-items:center;justify-content:center;
 font-family:'BebasNeue',sans-serif;font-size:.78rem;letter-spacing:1px;color:var(--gold);
 text-shadow:0 0 8px rgba(246,196,83,.6);padding:4px}
.srclink{display:block;width:max-content;max-width:100%;margin:26px auto 0;padding:11px 26px;border-radius:999px;
 font-family:'BebasNeue',sans-serif;letter-spacing:2px;font-size:.95rem;text-decoration:none;color:#ffe9b0;
 border:1px solid rgba(246,196,83,.65);background:rgba(246,196,83,.07);
 box-shadow:0 0 14px rgba(246,196,83,.22);transition:all .28s ease}
.srclink:hover{box-shadow:0 0 24px rgba(246,196,83,.5);background:rgba(246,196,83,.14);transform:translateY(-2px)}

/* ---- разделители ---- */
.divider{display:flex;align-items:center;gap:16px;max-width:64rem;margin:38px auto;opacity:.9}
.divider::before,.divider::after{content:"";height:1px;flex:1;
 background:linear-gradient(90deg,transparent,rgba(246,196,83,.4),transparent)}
.divider svg{flex:0 0 auto;filter:drop-shadow(0 4px 10px rgba(0,0,0,.5))}

/* ---- финал ---- */
.finale{position:relative;z-index:2;max-width:60rem;margin:56px auto 0;padding:38px clamp(22px,4vw,48px);
 border-radius:20px;border:1px solid rgba(246,196,83,.45);
 background:linear-gradient(180deg,rgba(255,46,136,.05),rgba(13,8,18,.55));
 box-shadow:0 0 40px rgba(255,46,136,.14),0 22px 50px rgba(0,0,0,.5)}
.finttl{font-family:'MarckScript',cursive;font-size:clamp(1.9rem,4vw,2.7rem);text-align:center;color:var(--gold);
 text-shadow:0 0 14px rgba(246,196,83,.6),0 0 40px rgba(255,46,136,.35)}
.fintext{margin:20px auto 0;max-width:68ch;text-align:center;font-size:1.08rem;line-height:1.85;color:#eadff0}
.logbook{margin:30px auto 0;max-width:34rem;border:1px dashed rgba(246,196,83,.45);border-radius:12px;
 padding:18px 24px;background:rgba(13,8,18,.55)}
.logttl{font-family:'BebasNeue',sans-serif;letter-spacing:3px;font-size:.85rem;color:var(--turq);
 text-shadow:0 0 8px rgba(47,232,200,.55);margin-bottom:10px}
.logrow{display:flex;justify-content:space-between;gap:14px;padding:5px 0;border-bottom:1px dotted rgba(246,196,83,.18);
 font-family:'BebasNeue',sans-serif;letter-spacing:1.5px;font-size:.98rem}
.logrow:last-child{border-bottom:none}
.logrow b{color:var(--mut);font-weight:400}
.logrow span{color:#ffe9b0}

/* ---- кнопка хаба ---- */
.hubline{text-align:center;margin:52px 0 6px;position:relative;z-index:2}
.hubbtn{display:inline-block;padding:15px 34px;border-radius:999px;text-decoration:none;
 font-family:'BebasNeue',sans-serif;letter-spacing:2.5px;font-size:1.05rem;color:#ffd9ea;
 border:1px solid var(--mag);background:rgba(255,46,136,.08);
 box-shadow:0 0 18px rgba(255,46,136,.45),inset 0 0 12px rgba(255,46,136,.14);transition:all .3s ease}
.hubbtn:hover{box-shadow:0 0 34px rgba(255,46,136,.75),inset 0 0 18px rgba(255,46,136,.25);transform:translateY(-2px);
 background:rgba(255,46,136,.16)}

/* ---- рулеточная лента ---- */
.tape{position:relative;z-index:2;display:flex;overflow-x:auto;margin-top:44px;border-top:2px solid rgba(246,196,83,.5);
 border-bottom:2px solid rgba(246,196,83,.5);background:#0b0610;scrollbar-width:thin}
.tnum{flex:0 0 auto;min-width:44px;padding:9px 6px;text-align:center;font-family:'BebasNeue',sans-serif;
 font-size:.95rem;letter-spacing:1px;border-right:1px solid rgba(246,196,83,.22);color:#ffe9b0}
.t-red{background:#8f1236}
.t-blk{background:#161019}
.t-zero{background:#14804a}

footer{position:relative;z-index:2;text-align:center;color:var(--mut);font-size:.92rem;line-height:1.7;
 padding:30px 16px 44px;font-family:'PTSN',sans-serif}
footer b{color:var(--gold)}
@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}
@media(max-width:640px){
 .corner{display:none}
 .pcard{padding:28px 18px 34px}
 .chips{gap:16px}
}
'''


PAGE = '''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>San Fierro News — Ежедневный выпуск 02.10.2026: Las Venturas, колода из восьми карт</title>
<meta name="description" content="Ежедневный выпуск San Fierro News от 02.10.2026: ночная поездка по Las Venturas — офис Las Venturas News, автомастерская, LVPD, банк, авторынок, автовокзал, казино Caligula и армия на окраине. Восемь адресов — восемь игральных карт.">
<style>
@font-face{font-family:'RussoOne';src:url(data:font/ttf;base64,@@F_RUSSO@@) format('truetype')}
@font-face{font-family:'MarckScript';src:url(data:font/ttf;base64,@@F_MARCK@@) format('truetype')}
@font-face{font-family:'PTSN';src:url(data:font/ttf;base64,@@F_PTSN@@) format('truetype')}
@font-face{font-family:'BebasNeue';src:url(data:font/ttf;base64,@@F_BEBAS@@) format('truetype')}
@@CSS@@
</style>
</head>
<body>

<div class="marquee" aria-hidden="true">@@BULBS@@</div>

<header>
  <div class="skyline" aria-hidden="true">@@SKYLINE@@</div>
  <div class="haze" aria-hidden="true"></div>
  @@TWINKLE@@
  <div class="wrap">
    <div class="hero">
      <div class="sign">
        <div class="signstar">★</div>
        <div class="signbase">@@SIGN@@</div>
        <div class="signpole"></div>
      </div>
      <div class="heromain">
        <div class="kicker">SAN FIERRO NEWS · ЕЖЕДНЕВНЫЙ ВЫПУСК · ПЯТНИЦА</div>
        <h1>Las Venturas: <span class="thin">колода из восьми карт</span></h1>
        <p class="sub">Ночная поездка редакции на восток штата: восемь адресов города, который не умеет складывать карты — от башни коллег-газетчиков до армейского КПП на окраине. Каждая карта — место, каждая подпись — латунная табличка, каждая фишка — факт.</p>
        <div class="jackpot">
          <div class="jplab">JACKPOT · НОМЕР ДНЯ</div>
          <div class="jpdate">02.10.2026</div>
          <div class="jpsub">ПЯТНИЦА · ВОСТОЧНЫЙ БЕРЕГ ПУСТЫНИ · 24/7</div>
        </div>
      </div>
      <div class="wheel" aria-hidden="true">@@WHEEL@@</div>
    </div>
  </div>
</header>

<div class="wrap">

  <p class="lead"><span class="ms">Колесо крутится, ставка сделана.</span><br>
  После San Fierro и Los Santos редакционный пресс-трак выехал на восточную трассу — через пустыню, к зареву, которое видно за тридцать миль до границы города. Las Venturas не спит: здесь раздают карты, крутят колесо, меняют смены в полицейском участке и встречают автобусы один за другим. Этот номер — колода из восьми карт: восемь адресов, на которых держится день — и ночь — этого города. Тасуйте осторожно.</p>

@@SECTIONS@@

  <section class="finale">
    <div class="finttl">Ставка сделана. Больше ничего не меняется.</div>
    <p class="fintext">Las Venturas сдал нам восемь карт честно — ни одного блефа. Этот город можно обвинять в чём угодно, кроме нечестности к гостям: он обещает огни — и даёт огни, обещает удачу — и даёт шанс, обещает, что ты вернёшься, — и ты возвращаешься. Колода собрана, номер уходит в печать. У пресс-трака ещё полный бак, а на карте San Andreas остались белые углы — значит, до встречи скоро.</p>
    <div class="logbook">
      <div class="logttl">ЖУРНАЛ СМЕНЫ · ПИТ-БОСС</div>
      <div class="logrow"><b>Кадры</b><span>Anna Malboro</span></div>
      <div class="logrow"><b>Фоторедактор</b><span>Sonya Malboro</span></div>
      <div class="logrow"><b>Текст / Редактор</b><span>Jonny Wilde</span></div>
      <div class="logrow"><b>Выпуск</b><span>02.10.2026 · Las Venturas</span></div>
    </div>
  </section>

  <div class="hubline"><a class="hubbtn" href="newsroom.html">← Посмотреть все выпуски редакции</a></div>

</div>

<div class="tape" aria-hidden="true">@@TAPE@@</div>

<footer>© 2026 <b>San Fierro News</b> · Evolve Role Play · Las Venturas, колода из восьми карт<br>выпуск подшит в архив навсегда · 02.10.2026</footer>

</body>
</html>
'''

page = (PAGE
    .replace("@@F_RUSSO@@", F_RUSSO)
    .replace("@@F_MARCK@@", F_MARCK)
    .replace("@@F_PTSN@@", F_PTSN)
    .replace("@@F_BEBAS@@", F_BEBAS)
    .replace("@@CSS@@", CSS)
    .replace("@@BULBS@@", bulbs)
    .replace("@@SKYLINE@@", SKYLINE)
    .replace("@@TWINKLE@@", TWINKLE)
    .replace("@@SIGN@@", SIGN)
    .replace("@@WHEEL@@", WHEEL)
    .replace("@@SECTIONS@@", SECTIONS)
    .replace("@@TAPE@@", TAPE)
    .replace("@@STARS@@", STARS_URI)
    .replace("@@GRAIN@@", GRAIN_URI))

open("daily-02-10-2026-las-venturas.html", "w", encoding="utf-8").write(page)
print("OK, size:", len(page) // 1024, "KB")
print("data:image count:", page.count("data:image/jpeg;base64,"))
for bad in ["Saint-Louis", "чат", "_"]:
    if bad in page.replace("data:",""):
        print("WARN token:", bad)
