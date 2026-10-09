#!/usr/bin/env python3
"""SFN: сборка ежедневной газеты 08.10.2026, вторая редакция.
Вердикт гендиректора: v1 «Маршрут одной погони» не связан по смыслу (обрывки истории и кадров).
v2: сквозной свидетель - сама дорога; шесть глав с переходами, одна честная оговорка в подводке,
жёлтая осевая линия как визуальная нить между главами. Название: «Дорога не говорит ничего».
Кадры: work/daily0810/img/p*.b64 (12 шт). Выход: anna-malboro/daily-08-10-2026.html (URL вечный, имя не меняется).
Штамп 036 one-pursuit-route (имя дизайна живёт с первой редакции).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
IMG = os.path.join(HERE, 'img')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-08-10-2026.html')


def b64(key):
    return open(os.path.join(IMG, key + '.b64')).read().strip()


SHOTS = {
    'p01': 'Утро на мосту: дорога сначала пропускает камуфляжный грузовик - и только потом всех остальных.',
    'p02': 'Тот же чекпойнт сверху: вышка, навес, пикап и патруль под ним - дорога смотрит на себя со стороны.',
    'p03': 'Пустынная обочина: «жук» стоит, постовой у водительской двери, борт 9320 позади без маячков - дорога слушает разговор.',
    'p04': 'Деревенский съезд: перевёрнутая машина горит, борт 2904 на откосе, человек у отбойника - день впервые показывает тепло.',
    'p05': 'Открытая трасса: красный седан поперёк полос, один у багажника, второй лицом вниз на асфальте - дорога останавливает игру.',
    'p06': 'Эстакада: белый седан с горящими фарами, человек у левого борта, патруль позади с распахнутыми дверями.',
    'p07': 'Та же эстакада дальше: три патруля на мосту и четверо лежащих в разных полосах - картина, которую застаёт подкрепление.',
    'p08': 'Сверху: патруль поперёк полос у зелёного щита, люди в стыках полотна - поле, на котором игра уже сыграна.',
    'p09': 'Развязка: чёрный седан в кольце людей с оружием, зелёный у обочины, борт 224 на откосе - день собирается в точку.',
    'p10': 'Песчаная площадка: четыре патруля по кварталу, человек у разделителя - кольцо ещё не замкнуто.',
    'p11': 'Внутри кольца: SWAT и борт 7435, такси с постовым у двери, синий седан со смётым капотом - дорога принимает всех, кого принесла.',
    'p12': 'Перекрёсток у контейнерной площадки: скорая между двух пикапов SWAT, лежащий мотоцикл, самолёт в небе - день разбирается на глаголы.',
}

FIG = '''<figure class="shot" data-lb>
      <img src="data:image/jpeg;base64,{B64}" alt="{CAP}" loading="lazy">
      <figcaption>{CAP}</figcaption>
    </figure>'''


def fig(key):
    return FIG.format(B64=b64(key), CAP=SHOTS[key])


CSS = '''/* SFN-DESIGN-036: one-pursuit-route · 08.10.2026 */
:root{
  --paper:#edeff1; --panel:#f7f8f9; --ink:#10151a; --mut:#5b666e; --dim:#7d8890;
  --siren:#16406e; --tape:#e8b422; --line:rgba(16,21,26,.16);
  --disp:"Barlow Condensed",system-ui,sans-serif;
  --body:"Merriweather",Georgia,serif;
  --mono:"JetBrains Mono",ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:auto}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:16.5px;line-height:1.7}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
   repeating-linear-gradient(90deg,rgba(16,21,26,.022) 0 1px,transparent 1px 40px),
   radial-gradient(820px 420px at 12% -140px,rgba(22,64,110,.08),transparent 70%),
   radial-gradient(700px 400px at 96% 20%,rgba(232,180,34,.07),transparent 70%)}
.mono{font-family:var(--mono)}
.wrap{max-width:72rem;margin:0 auto;padding:0 1.3rem}
::selection{background:rgba(22,64,110,.22)}
.tapeline{height:7px;background:repeating-linear-gradient(-45deg,var(--tape) 0 14px,#14181d 14px 28px)}
/* мастхэд */
.mast{border-bottom:3px solid var(--ink);background:var(--panel)}
.mastin{display:flex;align-items:baseline;gap:1.1rem;flex-wrap:wrap;padding:1rem 0 .7rem}
.mastname{font-family:var(--disp);font-weight:700;font-size:1.6rem;letter-spacing:.14em;text-transform:uppercase}
.mastsub{font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.mastdate{margin-left:auto;font-family:var(--mono);font-size:.72rem;letter-spacing:.14em;color:var(--siren);
  border:1px solid rgba(22,64,110,.45);border-radius:999px;padding:.34rem .9rem;background:rgba(22,64,110,.06)}
.kchip{font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;color:var(--dim);padding:0 0 .7rem}
/* герой */
.hero{padding:2.8rem 0 2rem;border-bottom:1px solid var(--line)}
.kick{font-family:var(--mono);font-size:.68rem;letter-spacing:.26em;text-transform:uppercase;color:var(--siren);margin-bottom:1rem}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(2.3rem,6.4vw,4.4rem);line-height:1.02;text-transform:uppercase;letter-spacing:.01em;max-width:24ch}
h1 em{font-style:normal;border-bottom:.16em solid var(--tape)}
.stand{max-width:68ch;margin-top:1.15rem;color:var(--mut);font-size:1.03rem}
.stand b{color:var(--ink)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;margin-top:1.8rem}
.tile{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--siren);padding:.85rem 1rem}
.tile .big{font-family:var(--disp);font-weight:700;font-size:2.1rem;line-height:1}
.tile .lbl{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin-top:.4rem}
/* нить маршрута */
.routelbl{font-family:var(--mono);font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin:2rem 0 .5rem}
.routewrap{overflow-x:auto;padding-bottom:.4rem}
.routeline{display:flex;align-items:stretch;gap:0;min-width:640px}
.rstop{flex:1;position:relative;cursor:pointer;font:inherit;text-align:left;color:var(--ink);background:transparent;border:0;padding:1.5rem .6rem 0}
.rstop::before{content:"";position:absolute;top:.62rem;left:0;right:0;height:2px;background:repeating-linear-gradient(90deg,var(--siren) 0 8px,transparent 8px 14px)}
.rstop:first-child::before{left:50%}.rstop:last-child::before{right:50%}
.rstop .dot{position:absolute;top:.18rem;left:50%;transform:translateX(-50%);width:15px;height:15px;border-radius:50%;
  background:var(--paper);border:3px solid var(--siren);transition:.16s}
.rstop:hover .dot{background:var(--tape);border-color:var(--ink)}
.rstop .rn{font-family:var(--mono);font-size:.6rem;color:var(--dim);letter-spacing:.1em}
.rstop .rp{display:block;font-family:var(--disp);font-weight:700;font-size:1.02rem;text-transform:uppercase;letter-spacing:.04em;margin-top:.15rem}
.rstop .ru{display:block;font-family:var(--mono);font-size:.58rem;color:var(--mut);margin-top:.2rem}
/* навигация */
.snav{position:sticky;top:0;z-index:40;background:rgba(237,239,241,.94);backdrop-filter:blur(7px);border-block:1px solid var(--line)}
.snavin{display:flex;gap:.4rem;overflow-x:auto;padding:.5rem 0;scrollbar-width:none}
.snavin::-webkit-scrollbar{display:none}
.snavbtn{flex:none;cursor:pointer;font-family:var(--mono);font-size:.63rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--mut);background:transparent;border:1px solid var(--line);border-radius:999px;padding:.4rem .8rem;transition:.18s}
.snavbtn:hover{color:var(--ink);border-color:var(--siren)}
.snavbtn.cur{color:#fff;background:var(--siren);border-color:var(--siren)}
/* главы: жёлтая осевая линия соединяет главы сквозь всю страницу */
.sec{position:relative;padding:2.7rem 0 1.2rem}
.sec::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;
  background:repeating-linear-gradient(90deg,var(--tape) 0 26px,transparent 26px 46px)}
.sechead .kick{margin-bottom:.45rem}
h2{font-family:var(--disp);font-weight:700;font-size:clamp(1.6rem,3.6vw,2.5rem);text-transform:uppercase;letter-spacing:.02em;line-height:1.08}
/* лид БЕЗ буквицы: буквица снята по вердикту гендиректора 09.10.2026 («некрасиво смотрится») */
.lead{max-width:66ch;margin:1rem 0 .9rem;font-size:1.1rem;font-style:italic}
.sec p.txt{max-width:68ch;margin:.55rem 0;color:#2b3238}
.blotter{margin:1.1rem 0;background:var(--panel);border:1px solid var(--line);font-family:var(--mono);font-size:.72rem}
.blotter .bh{display:flex;justify-content:space-between;gap:1rem;padding:.5rem .8rem;background:var(--ink);color:#e8ecef;letter-spacing:.12em;text-transform:uppercase;font-size:.6rem}
.blotter .br{display:flex;gap:.9rem;padding:.42rem .8rem;border-top:1px dashed var(--line)}
.blotter .br b{color:var(--siren)}
.shot{margin:1.4rem 0}
.shot img{display:block;width:100%;height:auto;border:1px solid var(--line);background:#fff;padding:.45rem;cursor:zoom-in}
.shot figcaption{font-style:italic;color:var(--mut);font-size:.92rem;margin-top:.55rem;max-width:72ch}
.duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}
/* нитка кадров */
.thread{margin:1.2rem 0 .4rem;display:grid;gap:.5rem}
.th{display:grid;grid-template-columns:2.6rem 1fr;gap:.9rem;align-items:baseline;background:var(--panel);border:1px solid var(--line);padding:.55rem .9rem}
.th .n{font-family:var(--mono);font-size:.78rem;color:var(--siren)}
.th .s{font-size:.97rem;color:#2b3238}
.th .s b{font-family:var(--disp);text-transform:uppercase;letter-spacing:.05em}
/* позиция */
.position{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--tape);padding:1.1rem 1.2rem;margin:1.4rem 0}
.position h3{font-family:var(--disp);text-transform:uppercase;letter-spacing:.08em;font-size:1.05rem;margin-bottom:.5rem}
.position p{font-size:.95rem;color:var(--mut);max-width:72ch}
/* подвал */
footer{margin-top:3rem;border-top:3px solid var(--ink);background:var(--panel);padding:1.5rem 0 2.1rem}
.frow{display:flex;flex-wrap:wrap;gap:.6rem 1.6rem;align-items:center;font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
.pill{display:inline-flex;align-items:center;gap:.5rem;margin-top:1.15rem;font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;
  color:var(--siren);text-decoration:none;border:1px solid rgba(22,64,110,.5);border-radius:999px;padding:.62rem 1.2rem;
  background:rgba(22,64,110,.06);box-shadow:0 0 18px rgba(22,64,110,.3);transition:.2s}
.pill:hover{background:var(--siren);color:#fff;box-shadow:0 0 26px rgba(22,64,110,.5)}
/* лайтбокс */
.lb{position:fixed;inset:0;z-index:90;background:rgba(10,13,17,.94);display:none;align-items:center;justify-content:center;flex-direction:column;padding:2.4rem 1.2rem}
.lb.on{display:flex}
.lb img{max-width:min(1100px,94vw);max-height:78vh;border:1px solid rgba(247,248,249,.35);background:#fff;padding:.4rem}
.lb .lbcap{color:#e6eaee;font-style:italic;font-size:.94rem;max-width:72ch;margin-top:.9rem;text-align:center}
.lb .lbx{position:absolute;top:1rem;right:1.2rem;cursor:pointer;background:transparent;border:1px solid rgba(247,248,249,.4);color:#e6eaee;
  font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.4rem .9rem}
.lb .lbnav{display:flex;gap:.7rem;margin-top:.9rem}
.lb .lbnav button{cursor:pointer;background:transparent;border:1px solid rgba(247,248,249,.4);color:#e6eaee;font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.42rem 1rem}
@media (max-width:640px){
  .mastdate{margin-left:0}
  .th{grid-template-columns:1fr}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''

BODY = '''<div class="tapeline"></div>
<header class="mast">
  <div class="wrap">
    <div class="mastin">
      <span class="mastname">San Fierro News</span>
      <span class="mastsub">ежедневная газета · штат San Andreas</span>
      <span class="mastdate">четверг, 8 октября 2026</span>
    </div>
    <div class="kchip">Кадры: Anna Malboro · Фоторедактор: Sonya Malboro · Текст и редактор: Jonny Wilde</div>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <div class="kick">Хроника дня · один свидетель</div>
    <h1>Дорога <em>не говорит ничего</em></h1>
    <p class="stand">Двенадцать кадров одного дня на шоссе штата - от утреннего чекпойнта на мосту до кольца оцепления
    у контейнерной площадки. Мы не знаем, была ли это одна погоня или несколько вызовов одной смены: кадры молчат о причинах.
    Поэтому газета идёт за единственным свидетелем, который был на всех двенадцати кадрах, - <b>за самой дорогой</b>.
    Она соединяет точки; мы соединяем только то, что видно.</p>
    <div class="tiles">
      <div class="tile"><div class="big">12</div><div class="lbl">кадров одного дня</div></div>
      <div class="tile"><div class="big">6</div><div class="lbl">глав дороги</div></div>
      <div class="tile"><div class="big">4</div><div class="lbl">бортовых номера на бортах</div></div>
      <div class="tile"><div class="big">1</div><div class="lbl">свидетель - сама дорога</div></div>
    </div>
    <div class="routelbl">Нить дороги · шесть глав, клик ведёт к главе</div>
    <div class="routewrap"><div class="routeline">
      <button class="rstop" data-t="most"><span class="dot"></span><span class="rn">01</span><span class="rp">Мост</span><span class="ru">глава 1 · утро</span></button>
      <button class="rstop" data-t="pust"><span class="dot"></span><span class="rn">02</span><span class="rp">Пустынный съезд</span><span class="ru">глава 2</span></button>
      <button class="rstop" data-t="ogon"><span class="dot"></span><span class="rn">03</span><span class="rp">Деревенский поворот</span><span class="ru">глава 3 · огонь</span></button>
      <button class="rstop" data-t="esta"><span class="dot"></span><span class="rn">04</span><span class="rp">Эстакада</span><span class="ru">глава 4</span></button>
      <button class="rstop" data-t="uzel"><span class="dot"></span><span class="rn">05</span><span class="rp">Развязка</span><span class="ru">глава 5 · кольцо</span></button>
      <button class="rstop" data-t="final"><span class="dot"></span><span class="rn">06</span><span class="rp">Перекрёсток</span><span class="ru">глава 6 · финал</span></button>
    </div></div>
  </div>
</section>

<nav class="snav" aria-label="Разделы выпуска">
  <div class="wrap"><div class="snavin">
    <button class="snavbtn" data-t="most">1 · Мост</button>
    <button class="snavbtn" data-t="pust">2 · Пустыня</button>
    <button class="snavbtn" data-t="ogon">3 · Огонь</button>
    <button class="snavbtn" data-t="esta">4 · Эстакада</button>
    <button class="snavbtn" data-t="uzel">5 · Кольцо</button>
    <button class="snavbtn" data-t="final">6 · Финал</button>
    <button class="snavbtn" data-t="niti">Нить кадров</button>
    <button class="snavbtn" data-t="poz">Позиция редакции</button>
  </div></div>
</nav>

<section class="sec" data-sec="most">
  <div class="wrap">
    <div class="sechead"><div class="kick">Глава 1 · мост</div><h2>Утро: дорогу проверяют</h2></div>
    <p class="lead">День начинается с того, что дорога останавливается посмотреть на себя: будка, конусы, наблюдательная вышка - и камуфляжный грузовик, который проходит медленнее всех.</p>
    <p class="txt">Два патруля держат подъезды, полосатый шлагбаум поднят, под навесом - пикап POLICE и патрульный седан.
    Город за спиной чекпойнта живёт обычным утром; дорога уже живёт досмотром: каждая машина сбрасывает скорость до пешей
    и проходит между конусов, как проходят между парт.</p>
    <p class="txt">Зачем мосту чекпойнт в тихий четверг - кадр не говорит. Дорога вообще говорит мало: она только показывает,
    кого и как пропустила. Запомним это её свойство - оно пригодится к финалу.</p>
    {F_P01}
    {F_P02}
  </div>
</section>

<section class="sec" data-sec="pust">
  <div class="wrap">
    <div class="sechead"><div class="kick">Глава 2 · пустынный съезд</div><h2>Полдень: дорога сворачивает в пустыню</h2></div>
    <p class="lead">От моста дорога тянется на юг и худеет до одной полосы: здесь в полдень она останавливает оранжевый «жук» - спокойно, как останавливают без сирен.</p>
    <p class="txt">Постовой наклонён к водительской двери, борт 9320 стоит позади без маячков. В кадре ничто не кричит:
    пустыня вообще делает любой разговор тише. Но это вторая точка дня, где дорога кого-то остановила, и первая, где
    кому-то задали вопросы. Куда денется этот разговор - увидим через две главы: дороги пустыни всегда выходят к шоссе.</p>
    {F_P03}
  </div>
</section>

<section class="sec" data-sec="ogon">
  <div class="wrap">
    <div class="sechead"><div class="kick">Глава 3 · деревенский поворот</div><h2>День: дорога ломается и горит</h2></div>
    <p class="lead">Дальше дорога ныряет в деревню и на ферменном съезде ломается по-настоящему: чёрная машина на крыше горит, борт 2904 выброшен на откос, человек лежит у секции отбойника.</p>
    <p class="txt">У огня стоят люди и не подходят - так стоят, когда помощь уже позвана и руками делать нечего.
    Второй патруль держит дорогу с обеих сторон: день впервые показывает тепло, и показывает напрямую, огнём.
    Ферма за отбойником не пострадала: сараи целы, только трава вытоптана так, что погоню по ней можно читать, как след.</p>
    <p class="txt">Кадр не говорит, сам ли человек у отбойника вышел из горящей машины или его вынесли.
    Дорога не ручается ни за одну версию - и мы не ручаемся: это не наш огонь и не наши слова.</p>
    {F_P04}
  </div>
</section>

<section class="sec" data-sec="esta">
  <div class="wrap">
    <div class="sechead"><div class="kick">Глава 4 · эстакада</div><h2>Вечер: дорога поднимается и затихает</h2></div>
    <p class="lead">Эстакада - самая высокая и самая тихая точка дня: белый седан поперёк полос с горящими фарами, люди, лежащие на полотне, патрули с распахнутыми дверями.</p>
    <p class="txt">Сначала открытая трасса: красный седан поперёк полосы, один человек у багажника, второй - лицом вниз
    посреди полотна. Потом сама эстакада: человек у левого борта белого седана, патруль позади с распахнутыми дверями.
    Дальше - вид, который застаёт подкрепление: три патруля на мосту и четверо лежащих в разных полосах.</p>
    <p class="txt">Сверху эстакада похожа на поле, на котором игра уже сыграна: патруль поперёк полос у зелёного щита,
    люди в стыках полотна, длинная тень опоры - единственное, что движется в этот час. Лицом вниз лежат так, как лежат
    при задержании; кадр не отделяет задержанных от раненых - за тех и других ответит скорая в финале.</p>
    {F_P05}
    <div class="duo">{F_P06}{F_P07}</div>
    {F_P08}
  </div>
</section>

<section class="sec" data-sec="uzel">
  <div class="wrap">
    <div class="sechead"><div class="kick">Глава 5 · развязка и песчаная площадка</div><h2>Сумерки: дорога завязывается в кольцо</h2></div>
    <p class="lead">На развязке день собирается в точку: чёрный седан в кольце людей с оружием, зелёный седан на обочине с двумя постовыми, перевёрнутая машина в траве и борт 224 на откосе.</p>
    <p class="txt">Сверху видно всех сразу - и тех, кто держит кольцо, и тех, кто лежит у зелёной машины, и патрули на
    обоих съездах. Это единственный кадр дня, где операция видна целиком, как схема на планёрке: дорога свела концы
    своей нити в один узел и держит его.</p>
    <p class="txt">Дальше кольцо высыпается на песчаную площадку у окраины: четыре патруля рассредоточены по кварталу,
    человек у разделителя ждёт, пока кольцо сомкнётся. Внутри - пикапы SWAT и борт 7435, жёлтое такси с постовым у двери,
    синий седан со смётым капотом, чёрный седан и человек на песке рядом. Такси в этой компании выглядит случайным гостем;
    дорога привела всех - дорога и разберётся.</p>
    <div class="blotter">
      <div class="bh"><span>сводка редакции по бортам</span><span>где дорога их оставила</span></div>
      <div class="br"><b>224</b><span>развязка, левый откос, машина поперёк травы</span></div>
      <div class="br"><b>9320</b><span>пустынный съезд, позади оранжевого «жука»</span></div>
      <div class="br"><b>2904</b><span>деревенский поворот, на откосе у горящей машины</span></div>
      <div class="br"><b>7435</b><span>песчаная площадка, внутри кольца</span></div>
    </div>
    <div class="duo">{F_P09}{F_P10}</div>
    {F_P11}
  </div>
</section>

<section class="sec" data-sec="final">
  <div class="wrap">
    <div class="sechead"><div class="kick">Глава 6 · перекрёсток у контейнерной площадки</div><h2>Финал: дорога отдаёт людей</h2></div>
    <p class="lead">Последняя точка дня стоит уже не на шоссе, а у перекрёстка контейнерной площадки: скорая между двух пикапов SWAT, мотоцикл лежит посреди перекрёстка, в небе проходит лёгкий самолёт.</p>
    <p class="txt">Скорая - единственный адрес дня, где людей ждут. Всё, что дорога собрала за двенадцать кадров - номера,
    машины, лежащих людей, - здесь разбирается на простые глаголы: увезти, закрыть, уехать. Мотоцикл посреди перекрёстка
    останется до утра сторожить место, где нить дня оборвалась.</p>
    <p class="txt">Самолёт поднимается без остановки - единственный, кто ушёл из этого дня свободно. Дорога остаётся:
    завтра утром её снова будут проверять, останавливать, жечь и перекрывать. Она не скажет ничего. Это её работа -
    и, если подумать, наша тоже: показать её молчание кадр за кадром.</p>
    {F_P12}
  </div>
</section>

<section class="sec" data-sec="niti">
  <div class="wrap">
    <div class="sechead"><div class="kick">Приложение · нить кадров</div><h2>Двенадцать кадров по порядку камеры</h2></div>
    <p class="lead">Порядок ниже - тот, в каком камеру встретила дорога: от моста к перекрёстку. Другого порядка у редакции нет: документов со временем суток нам не дали.</p>
    <div class="thread">
      <div class="th"><span class="n">01</span><span class="s"><b>Мост</b> - чекпойнт с будкой и вышкой, камуфляжный грузовик проходит досмотр</span></div>
      <div class="th"><span class="n">02</span><span class="s"><b>Мост, сверху</b> - навес, пикап POLICE, поднятый шлагбаум</span></div>
      <div class="th"><span class="n">03</span><span class="s"><b>Пустынный съезд</b> - остановка оранжевого «жука», борт 9320 позади</span></div>
      <div class="th"><span class="n">04</span><span class="s"><b>Деревенский поворот</b> - перевёрнутая машина горит, борт 2904 на откосе</span></div>
      <div class="th"><span class="n">05</span><span class="s"><b>Открытая трасса</b> - красный седан поперёк полосы, человек лицом вниз</span></div>
      <div class="th"><span class="n">06</span><span class="s"><b>Эстакада</b> - белый седан с фарами, человек у борта, патруль позади</span></div>
      <div class="th"><span class="n">07</span><span class="s"><b>Эстакада, дальше</b> - три патруля и четверо лежащих в полосах</span></div>
      <div class="th"><span class="n">08</span><span class="s"><b>Эстакада, сверху</b> - патруль поперёк полос у зелёного щита</span></div>
      <div class="th"><span class="n">09</span><span class="s"><b>Развязка</b> - кольцо вокруг чёрного седана, борт 224, перевёрнутая машина в траве</span></div>
      <div class="th"><span class="n">10</span><span class="s"><b>Песчаная площадка</b> - четыре патруля по кварталу, кольцо не замкнуто</span></div>
      <div class="th"><span class="n">11</span><span class="s"><b>Внутри кольца</b> - SWAT, борт 7435, такси, синий седан со смётым капотом</span></div>
      <div class="th"><span class="n">12</span><span class="s"><b>Перекрёсток контейнерной площадки</b> - скорая, лежащий мотоцикл, самолёт в небе</span></div>
    </div>
  </div>
</section>

<section class="sec" data-sec="poz">
  <div class="wrap">
    <div class="position">
      <h3>Позиция редакции: дорога как свидетель</h3>
      <p>Дорога - единственный свидетель, побывавший на всех двенадцати кадрах. Она не называет причин, чинов и имён -
      поэтому и газета их не называет: бортовые номера взяты с бортов, люди остаются без имён, версии - без вердиктов.
      Виновных в этом тексте нет, потому что их не показывает ни один кадр. Если участники дня расскажут свою нить -
      мы напечатаем её рядом с этими кадрами и без правок; до тех пор двенадцать кадров лежат в том порядке,
      в каком их встретила камера.</p>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="frow"><span>Кадры: Anna Malboro</span><span>Фоторедактор: Sonya Malboro</span><span>Текст и редактор: Jonny Wilde</span></div>
    <div class="frow"><span>дизайн и вёрстка - редакция San Fierro News</span><span>8 октября 2026</span></div>
    <a class="pill" href="newsroom.html">&larr; Посмотреть все выпуски редакции</a>
  </div>
</footer>

<div class="lb" id="lb" role="dialog" aria-label="Просмотр кадра">
  <button class="lbx" id="lbx">закрыть · esc</button>
  <img id="lbimg" src="" alt="">
  <div class="lbcap" id="lbcap"></div>
  <div class="lbnav"><button id="lbprev">&larr; предыдущий</button><button id="lbnext">следующий &rarr;</button></div>
</div>
'''

JS = '''
(function(){
  var go=function(t){var el=document.querySelector('[data-sec="'+t+'"]');if(el){el.scrollIntoView({block:'start',behavior:'smooth'});}};
  document.addEventListener('click',function(e){
    var b=e.target.closest('[data-t]');if(b){go(b.getAttribute('data-t'));}
  });
  var btns=[].slice.call(document.querySelectorAll('.snavbtn'));
  var secs=[].slice.call(document.querySelectorAll('[data-sec]'));
  var spy=function(){
    var y=window.innerHeight*0.35,cur=null;
    secs.forEach(function(s){var r=s.getBoundingClientRect();if(r.top<=y){cur=s.getAttribute('data-sec');}});
    btns.forEach(function(b){b.classList.toggle('cur',b.getAttribute('data-t')===cur);});
  };
  var tick=false;
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(function(){spy();tick=false;});}},{passive:true});
  spy();
  var figs=[].slice.call(document.querySelectorAll('figure.shot'));
  var lb=document.getElementById('lb'),img=document.getElementById('lbimg'),cap=document.getElementById('lbcap');
  var i=-1;
  var show=function(n){i=(n+figs.length)%figs.length;var im=figs[i].querySelector('img');img.src=im.src;img.alt=im.alt;cap.textContent=im.alt;lb.classList.add('on');};
  figs.forEach(function(f,n){f.querySelector('img').addEventListener('click',function(){show(n);});});
  document.getElementById('lbx').addEventListener('click',function(){lb.classList.remove('on');});
  document.getElementById('lbprev').addEventListener('click',function(){show(i-1);});
  document.getElementById('lbnext').addEventListener('click',function(){show(i+1);});
  document.addEventListener('keydown',function(e){
    if(!lb.classList.contains('on'))return;
    if(e.key==='Escape'){lb.classList.remove('on');}
    if(e.key==='ArrowLeft'){show(i-1);}
    if(e.key==='ArrowRight'){show(i+1);}
  });
})();
'''

html = '''<!DOCTYPE html>
<html lang="ru">
<head>
<!-- © 2026 San Fierro News / Jonny Wilde. Дизайн и вёрстка защищены: CC BY-NC-ND 4.0. Копирование и переработка запрещены. -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>San Fierro News — Дорога не говорит ничего: двенадцать кадров одного дня на шоссе штата</title>
<meta name="description" content="Ежедневная газета San Fierro News от 8 октября 2026, вторая редакция: чекпойнт на мосту, остановка в пустыне, огонь у деревенского поворота, лежащие люди на эстакаде, кольцо на развязке и скорая у контейнерной площадки - двенадцать кадров одного дня, соединённых самим свидетелем: дорогой.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=Merriweather:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
''' + CSS + '''</style>
</head>
<body>
''' + BODY.format(F_P01=fig('p01'), F_P02=fig('p02'), F_P03=fig('p03'), F_P04=fig('p04'),
                  F_P05=fig('p05'), F_P06=fig('p06'), F_P07=fig('p07'), F_P08=fig('p08'),
                  F_P09=fig('p09'), F_P10=fig('p10'), F_P11=fig('p11'), F_P12=fig('p12')) + '''
<script>''' + JS + '''</script>
<!-- SFN · 2026 · 036 · one-pursuit-route -->
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('written', OUT, len(html.encode('utf-8')) // 1024, 'KB')
