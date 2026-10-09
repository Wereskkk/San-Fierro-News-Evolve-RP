#!/usr/bin/env python3
"""SFN: ежедневная газета 10.10.2026 «Сводка, которую не дали пресс-службы».
Материал: inbox/ (6 кадров, партия 10.10: пять происшествий в трёх городах).
Дизайн 038 dispatch-desk: ночная диспетчерская доска, прогресс-чтения, борд инцидентов,
факт-панели, сводная таблица дня, лайтбокс со счётчиком. Выход: anna-malboro/daily-10-10-2026.html.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
IMG = os.path.join(HERE, 'img')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-10-10-2026.html')


def b64(key):
    return open(os.path.join(IMG, key + '.b64')).read().strip()


CAPS = {
    'f1': 'Los Santos, ночь у Ammu-Nation: ограбление закончилось перестрелкой - вертолёт сел прямо на полотно, патруль и белый спорткар закрыли вход, у тротуара люди с оружием. Есть пострадавшие.',
    'f2': 'Los Santos у автовокзала: фура сломалась, прицеп отцепился и лёг поперёк полосы. Помощи на месте нет - ни тягача, ни бригады: только объезд по зелёной стрелке.',
    'f3': 'Дорога у пляжа Santa Maria: борт 405 после встречи с фурой на встречной полосе; оба полицейских погибли до приезда скорой. LSPD комментарии давать отказались.',
    'f4': 'Las Venturas, Авторынок: перестрелка в разгаре - человек с винтовкой из-за чёрного седана, борт 9320 подходит с шоссе, люди расходятся по площадке веером.',
    'f5': 'Авторынок после: машины раскиданы по песку, пострадавшие лежат у жёлтого седана и у борта с распахнутыми дверями. Пострадавших много; LVPD комментарии не даёт.',
    'f6': 'San Fierro, мост: финал погони в четыре экипажа - борта 7436 и 7426 заперли полотно, офицеры с винтовками, подозреваемый на коленях посреди полос. Ущерб - десятки миллионов долларов.',
}

FIG = '''<figure class="shot" data-lb>
      <img src="data:image/jpeg;base64,{B64}" alt="{CAP}" loading="lazy">
      <figcaption><b>{ID}</b> {CAP}</figcaption>
    </figure>'''


def fig(key, eid):
    return FIG.format(B64=b64(key), CAP=CAPS[key], ID=eid)


FACTS = '''<div class="facts">
      <div class="frow"><b>Город</b><span>{CITY}</span></div>
      <div class="frow"><b>Службы</b><span>{SRV}</span></div>
      <div class="frow"><b>Статус</b><span>{ST}</span></div>
      <div class="frow"><b>Пресс-служба</b><span>{PR}</span></div>
    </div>'''

CSS = '''/* SFN-DESIGN-038: dispatch-desk · 10.10.2026 */
:root{
  --bg:#101318; --panel:#171c24; --panel2:#12161d; --ink:#e8ecf2; --mut:#98a2ae; --dim:#6b7683;
  --red:#d33f36; --amber:#e8b422; --blue:#4f8cff; --grey:#7d8ca3; --line:rgba(232,236,242,.14);
  --disp:"Rubik",system-ui,sans-serif;
  --body:"Source Serif 4",Georgia,serif;
  --mono:"Courier Prime",ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:auto}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16.5px;line-height:1.7}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
   repeating-linear-gradient(0deg,rgba(232,236,242,.022) 0 1px,transparent 1px 40px),
   radial-gradient(820px 420px at 88% -140px,rgba(211,63,54,.09),transparent 70%),
   radial-gradient(700px 420px at -8% 30%,rgba(79,140,255,.06),transparent 70%)}
.mono{font-family:var(--mono)}
.wrap{max-width:72rem;margin:0 auto;padding:0 1.3rem}
::selection{background:rgba(211,63,54,.35)}
/* прогресс чтения */
.pbar{position:fixed;top:0;left:0;height:3px;width:0;background:linear-gradient(90deg,var(--red),var(--amber));z-index:60}
/* срочная строка */
.alertline{background:var(--red);color:#fff;font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;
  padding:.42rem 1rem;display:flex;gap:1.4rem;flex-wrap:wrap;justify-content:center}
/* мастхэд */
.mast{border-bottom:1px solid var(--line);background:var(--panel2)}
.mastin{display:flex;align-items:baseline;gap:1.1rem;flex-wrap:wrap;padding:1rem 0 .7rem}
.mastname{font-family:var(--disp);font-weight:800;font-size:1.55rem;letter-spacing:.12em;text-transform:uppercase}
.mastsub{font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.mastdate{margin-left:auto;font-family:var(--mono);font-size:.72rem;letter-spacing:.14em;color:var(--amber);
  border:1px solid rgba(232,180,34,.45);border-radius:999px;padding:.34rem .9rem;background:rgba(232,180,34,.07)}
.kchip{font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;color:var(--dim);padding:0 0 .7rem}
/* герой */
.hero{padding:2.8rem 0 2rem;border-bottom:1px solid var(--line)}
.kick{font-family:var(--mono);font-size:.68rem;letter-spacing:.26em;text-transform:uppercase;color:var(--red);margin-bottom:1rem}
h1{font-family:var(--disp);font-weight:800;font-size:clamp(2.2rem,6vw,4.1rem);line-height:1.05;letter-spacing:-.005em;max-width:24ch}
h1 em{font-style:normal;color:var(--amber)}
.stand{max-width:68ch;margin-top:1.1rem;color:var(--mut);font-size:1.04rem}
.stand b{color:var(--ink)}
/* диспетчерский борд */
.boardlbl{font-family:var(--mono);font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin:1.9rem 0 .6rem}
.board{display:grid;gap:.5rem}
.brow{display:grid;grid-template-columns:3.4rem 4.6rem 1fr auto;gap:1rem;align-items:center;text-align:left;cursor:pointer;
  font:inherit;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--dim);padding:.7rem .95rem;transition:.16s}
.brow:hover{transform:translateX(3px);border-color:var(--line);background:var(--panel2)}
.brow .bnum{font-family:var(--disp);font-weight:800;font-size:1.5rem;color:var(--dim);line-height:1}
.brow .bcity{font-family:var(--mono);font-size:.72rem;letter-spacing:.16em;color:var(--mut)}
.brow .bname{font-family:var(--disp);font-weight:600;font-size:1.02rem;letter-spacing:.02em;text-transform:uppercase}
.bstat{font-family:var(--mono);font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;border-radius:3px;padding:.24rem .55rem;white-space:nowrap}
.bstat.dead{color:#ffd9d6;background:rgba(211,63,54,.16);border:1px solid rgba(211,63,54,.6)}
.bstat.hurt{color:#ffe9b8;background:rgba(232,180,34,.14);border:1px solid rgba(232,180,34,.55)}
.bstat.block{color:#dbe3ec;background:rgba(125,140,163,.16);border:1px solid rgba(125,140,163,.55)}
.bstat.dmg{color:#d6e4ff;background:rgba(79,140,255,.14);border:1px solid rgba(79,140,255,.55)}
.brow.dead{border-left-color:var(--red)} .brow.hurt{border-left-color:var(--amber)}
.brow.block{border-left-color:var(--grey)} .brow.dmg{border-left-color:var(--blue)}
/* навигация */
.snav{position:sticky;top:0;z-index:50;background:rgba(16,19,24,.93);backdrop-filter:blur(8px);border-block:1px solid var(--line)}
.snavin{display:flex;gap:.4rem;overflow-x:auto;padding:.5rem 0;scrollbar-width:none}
.snavin::-webkit-scrollbar{display:none}
.snavbtn{flex:none;cursor:pointer;font-family:var(--mono);font-size:.63rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--mut);background:transparent;border:1px solid var(--line);border-radius:999px;padding:.42rem .85rem;transition:.18s}
.snavbtn:hover{color:var(--ink);border-color:var(--amber)}
.snavbtn.cur{color:#101318;background:var(--amber);border-color:var(--amber)}
/* секции инцидентов */
.sec{padding:2.7rem 0 1.2rem;border-bottom:1px solid var(--line)}
.sechead{display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap;justify-content:center}
.sechead .bignum{font-family:var(--disp);font-weight:800;font-size:3rem;line-height:1;color:transparent;-webkit-text-stroke:1.4px var(--dim)}
.sechead .kick{margin:0}
h2{font-family:var(--disp);font-weight:700;font-size:clamp(1.5rem,3.4vw,2.3rem);text-transform:uppercase;letter-spacing:.01em;line-height:1.12;margin-top:.4rem;text-align:center}
.lead{margin:1rem auto .9rem;font-size:1.1rem;font-style:italic;color:var(--ink);text-align:center}
.sec p.txt{max-width:82ch;margin:.55rem 0;color:#c3cad3}
.colwrap{max-width:76ch;margin:0 auto}
.facts{margin:1.5rem 0 0;background:var(--panel);border:1px solid var(--line);display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr))}
.facts .frow{display:grid;gap:.35rem;padding:.75rem .95rem;border-left:1px dashed var(--line);font-size:.95rem;color:#c3cad3}
.facts .frow:first-child{border-left:0}
.facts b{font-family:var(--mono);font-weight:400;font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:var(--mut)}
.backline{margin:1.1rem 0 0;text-align:center}
.backline button{cursor:pointer;background:none;border:0;font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}
.backline button:hover{color:var(--amber)}
/* кадры */
.shot{margin:1.4rem 0}
.shot img{display:block;width:100%;height:auto;border:1px solid var(--line);background:#000;padding:.4rem;cursor:zoom-in}
.shot figcaption{color:var(--mut);font-size:.92rem;margin-top:.55rem;max-width:74ch}
.shot figcaption b{font-family:var(--mono);font-size:.72rem;color:var(--amber);letter-spacing:.08em;margin-right:.4rem}
.duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}
/* итоги */
.sumtable{margin:1.2rem 0;background:var(--panel);border:1px solid var(--line);width:100%;border-collapse:collapse;font-size:.93rem}
.sumtable th{font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);text-align:left;padding:.55rem .85rem;border-bottom:1px solid var(--line)}
.sumtable td{padding:.55rem .85rem;border-top:1px dashed var(--line);color:#c3cad3;vertical-align:top}
.sumtable .id{font-family:var(--mono);color:var(--amber);white-space:nowrap}
/* подвал */
footer{margin-top:3rem;border-top:1px solid var(--line);background:var(--panel2);padding:1.5rem 0 2.1rem}
.frow2{display:flex;flex-wrap:wrap;gap:.6rem 1.6rem;align-items:center;font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
.pill{display:inline-flex;align-items:center;gap:.5rem;margin-top:1.15rem;font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;
  color:var(--amber);text-decoration:none;border:1px solid rgba(232,180,34,.5);border-radius:999px;padding:.62rem 1.2rem;
  background:rgba(232,180,34,.07);box-shadow:0 0 18px rgba(232,180,34,.25);transition:.2s}
.pill:hover{background:var(--amber);color:#101318;box-shadow:0 0 26px rgba(232,180,34,.45)}
/* лайтбокс */
.lb{position:fixed;inset:0;z-index:90;background:rgba(6,8,11,.95);display:none;align-items:center;justify-content:center;flex-direction:column;padding:2.4rem 1.2rem}
.lb.on{display:flex}
.lb img{max-width:min(1100px,94vw);max-height:76vh;border:1px solid rgba(232,236,242,.3)}
.lb .lbcap{color:#dfe5ec;font-size:.94rem;max-width:74ch;margin-top:.9rem;text-align:center}
.lb .lbcnt{font-family:var(--mono);font-size:.64rem;letter-spacing:.2em;color:var(--amber);margin-top:.6rem}
.lb .lbx{position:absolute;top:1rem;right:1.2rem;cursor:pointer;background:transparent;border:1px solid rgba(232,236,242,.4);color:#e8ecf2;
  font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.4rem .9rem}
.lb .lbnav{display:flex;gap:.7rem;margin-top:.8rem}
.lb .lbnav button{cursor:pointer;background:transparent;border:1px solid rgba(232,236,242,.4);color:#e8ecf2;font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.42rem 1rem}
@media (max-width:720px){
  .brow{grid-template-columns:2.6rem 1fr;grid-auto-rows:auto;row-gap:.3rem}
  .brow .bcity{grid-column:2}
  .bstat{grid-column:2;justify-self:start}
  .mastdate{margin-left:0}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''

BODY = '''<div class="pbar" id="pbar" aria-hidden="true"></div>
<div class="alertline"><span>срочно · 10 октября 2026</span><span>5 происшествий · 3 города</span><span>2 пресс-службы молчат</span></div>
<header class="mast">
  <div class="wrap">
    <div class="mastin">
      <span class="mastname">San Fierro News</span>
      <span class="mastsub">ежедневная газета · штат San Andreas</span>
      <span class="mastdate">суббота, 10 октября 2026</span>
    </div>
    <div class="kchip">Кадры: Anna Village · Фоторедактор: Sonya Malboro · Текст и редактор: Jonny Wilde</div>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <div class="kick">Сводка дня · дежурная доска</div>
    <h1>Сводка, которую <em>не дали</em> пресс-службы</h1>
    <p class="stand">Пять происшествий за один день в трёх городах: ограбление с перестрелкой в Los Santos, фура у автовокзала,
    встречный удар патруля и фуры у пляжа Santa Maria, перестрелка на Авторынке Las Venturas и финал погони на мосту San Fierro.
    <b>LSPD и LVPD комментарии давать отказались.</b> Редакция собрала сводку сама - по кадрам с места и по тому, что службы
    всё-таки сказали молчанием.</p>
    <div class="boardlbl">Диспетчерская доска · клик по строке ведёт к происшествию</div>
    <div class="board">
      <button class="brow hurt" data-t="i01"><span class="bnum">01</span><span class="bcity">LS · ночь</span><span class="bname">Ограбление Ammu-Nation, перестрелка</span><span class="bstat hurt">пострадавшие</span></button>
      <button class="brow block" data-t="i02"><span class="bnum">02</span><span class="bcity">LS · день</span><span class="bname">Фура и прицеп у автовокзала</span><span class="bstat block">помехи · помощи нет</span></button>
      <button class="brow dead" data-t="i03"><span class="bnum">03</span><span class="bcity">LS · Santa Maria</span><span class="bname">Патруль и фура: встречная полоса</span><span class="bstat dead">двое погибших</span></button>
      <button class="brow hurt" data-t="i04"><span class="bnum">04</span><span class="bcity">LV · Авторынок</span><span class="bname">Перестрелка на площадке</span><span class="bstat hurt">много пострадавших</span></button>
      <button class="brow dmg" data-t="i05"><span class="bnum">05</span><span class="bcity">SF · мост</span><span class="bname">Погоня в четыре экипажа</span><span class="bstat dmg">ущерб: десятки млн $</span></button>
    </div>
  </div>
</section>

<nav class="snav" aria-label="Разделы выпуска">
  <div class="wrap"><div class="snavin">
    <button class="snavbtn" data-t="i01">01 · Ammu-Nation</button>
    <button class="snavbtn" data-t="i02">02 · Автовокзал</button>
    <button class="snavbtn" data-t="i03">03 · Santa Maria</button>
    <button class="snavbtn" data-t="i04">04 · Авторынок</button>
    <button class="snavbtn" data-t="i05">05 · Мост SF</button>
    <button class="snavbtn" data-t="itogi">Итоги дня</button>
  </div></div>
</nav>

<section class="sec" data-sec="i01">
  <div class="wrap">
    <div class="sechead"><span class="bignum">01</span><div class="kick">Los Santos · ночь · ограбление</div></div>
    <div class="colwrap">
    <h2>Перестрелка у витрин Ammu-Nation</h2>
    <p class="lead">Ограбление магазина аммуниции закончилось перестрелкой прямо у входа: вертолёт сел на полотно улицы, патруль и белый спорткар закрыли витрины, у тротуара - люди с оружием.</p>
    <p class="txt">Ночной Los Santos увидел сцену, которую обычно показывают в сводках одним словом «перестрелка». Слово
    складывается из деталей: ротор вертолёта над разметкой, открытый багажник патруля, две фигуры у спорткара - одна
    с поднятым стволом, вторая в шаге от двери магазина. Пострадавшие есть: их имена редакция не называет, пока их
    не назовёт больница.</p>
    <p class="txt">Ограбление магазина аммуниции - всегда проверка города на скорость: между витриной и выстрелом
    проходят секунды. В эту ночь город успел лишь частично: перестрелка закончилась, прежде чем у тротуара появились
    первые свидетели, готовые говорить.</p>
    ''' + FACTS.format(CITY='Los Santos, торговая улица у Ammu-Nation', SRV='полиция, авиазвено, скорая', ST='перестрелка, есть пострадавшие', PR='не выступала') + '''
    <div class="backline"><button data-t="itogi">&uarr; к сводке дня</button></div>
    </div>
    ''' + fig('f1', 'EV-01') + '''
  </div>
</section>

<section class="sec" data-sec="i02">
  <div class="wrap">
    <div class="sechead"><span class="bignum">02</span><div class="kick">Los Santos · день · помехи на дороге</div></div>
    <div class="colwrap">
    <h2>Фура, которую никто не пришёл чинить</h2>
    <p class="lead">У автовокзала сломалась фура: тягач откатился вперёд, прицеп отцепился и лёг поперёк полосы. Помехи на дороге - и помощи нет: ни тягача эвакуации, ни бригады, ни даже водителя в кадре.</p>
    <p class="txt">Это происшествие без пострадавших и без выстрелов - и потому оно самое говорливое: о городе судят
    не только по тому, как он стреляет, но и по тому, как быстро он убирает с дороги сорок футов железа. Ответ:
    никак. Прицеп стоит, светофор зелёный, объезд по тротуарной дуге.</p>
    <p class="txt">Редакция оставила этот кадр в сводке намеренно: день, в который молчат пресс-службы, состоит
    не только из сирен. Иногда он состоит из прицепа, который некому прицепить.</p>
    ''' + FACTS.format(CITY='Los Santos, улица у автовокзала', SRV='не прибыли: помощи нет', ST='помехи на дороге, прицеп поперёк полосы', PR='не запрашивалась') + '''
    <div class="backline"><button data-t="itogi">&uarr; к сводке дня</button></div>
    </div>
    ''' + fig('f2', 'EV-02') + '''
  </div>
</section>

<section class="sec" data-sec="i03">
  <div class="wrap">
    <div class="sechead"><span class="bignum">03</span><div class="kick">Los Santos · пляж Santa Maria · гибель двоих</div></div>
    <div class="colwrap">
    <h2>Встречная полоса: борт 405 не доехал до скорой</h2>
    <p class="lead">Патрульная машина выехала на встречную полосу недалеко от пляжа Santa Maria и столкнулась с фурой. Оба полицейских погибли до приезда скорой. LSPD комментарии давать отказались.</p>
    <p class="txt">Кадр снят сверху и потому не щадит: борт 405 развёрнут поперёк своей полосы, фура встала юзом у
    отбойника, двое на асфальте - по одному с каждой стороны удара. Такси проезжает мимо по встречной: в этот час
    дорога уже живёт своей жизнью, а двое - нет.</p>
    <p class="txt">LSPD отказалась объяснить, почему патруль оказался на встречной, - и этот отказ занесён в сводку
    отдельной строкой. Вместо службы говорит кадр: удар был встречным, оба полицейских остались лежать на асфальте
    рядом с машиной, и скорая приехала слишком поздно, чтобы их спасти. Две гибели в одном кадре - цена одного
    неверного выезда на встречную полосу.</p>
    ''' + FACTS.format(CITY='Los Santos, дорога у пляжа Santa Maria', SRV='патруль (борт 405), фура, скорая опоздала', ST='оба полицейских погибли', PR='LSPD: отказ от комментариев') + '''
    <div class="backline"><button data-t="itogi">&uarr; к сводке дня</button></div>
    </div>
    ''' + fig('f3', 'EV-03') + '''
  </div>
</section>

<section class="sec" data-sec="i04">
  <div class="wrap">
    <div class="sechead"><span class="bignum">04</span><div class="kick">Las Venturas · Авторынок · перестрелка</div></div>
    <div class="colwrap">
    <h2>Песок Авторынка принял всех</h2>
    <p class="lead">Перестрелка у Авторынка: человек с винтовкой держит сектор из-за чёрного седана, борт 9320 заходит с шоссе, люди расходятся по площадке веером - каждый ищет своё укрытие.</p>
    <p class="txt">Первый кадр снят в разгар: стволы подняты, бегущий ещё в шаге от песка, жёлтый седан стоит с открытой
    дверью. Второй - после: машины раскиданы по площадке, как фишки после партии, пострадавшие лежат у жёлтого седана
    и у борта с распахнутыми дверями. Много пострадавших - формула, за которой стоят люди, а не цифра.</p>
    <p class="txt">LVPD комментарии не даёт. Редакция отмечает: вторая за день пресс-служба, которая выбирает молчание,
    и вторая площадка, где молчание приходится заполнять кадрами.</p>
    ''' + FACTS.format(CITY='Las Venturas, Авторынок', SRV='полиция (борт 9320 и другие), скорые', ST='перестрелка, много пострадавших', PR='LVPD: отказ от комментариев') + '''
    <div class="backline"><button data-t="itogi">&uarr; к сводке дня</button></div>
    </div>
    <div class="duo">''' + fig('f4', 'EV-04') + fig('f5', 'EV-05') + '''</div>
  </div>
</section>

<section class="sec" data-sec="i05">
  <div class="wrap">
    <div class="sechead"><span class="bignum">05</span><div class="kick">San Fierro · мост · финал погони</div></div>
    <div class="colwrap">
    <h2>Четыре экипажа и одни колени на полотне</h2>
    <p class="lead">Погоня за преступником в четыре экипажа закончилась на мосту San Fierro: борта 7436 и 7426 заперли полотно, офицеры с винтовками взяли сектор, подозреваемый встал на колени посреди полос.</p>
    <p class="txt">Мост - хорошая сцена для финала: деваться некуда, впереди рельсы, по бокам вода. Четыре экипажа
    поставили точку там, где город ставит запятую: серый седан подозреваемого зажат между патрулями, двери распахнуты,
    а человек на коленях выглядит меньше всей техники, что вокруг него.</p>
    <p class="txt">Сумма нанесённого ущерба составила десятки миллионов долларов: погоня прошла через полгорода, и
    счёт ей выставит не суд, а сметы. Редакция приводит сумму со слов источников, близких к делу: официальной
    калькуляции в сводке нет - и это тоже строка о молчании служб.</p>
    ''' + FACTS.format(CITY='San Fierro, мост', SRV='четыре экипажа (борта 7436, 7426 и ещё два)', ST='подозреваемый задержан на мосту', PR='официальной калькуляции нет') + '''
    <div class="backline"><button data-t="itogi">&uarr; к сводке дня</button></div>
    </div>
    ''' + fig('f6', 'EV-06') + '''
  </div>
</section>

<section class="sec" data-sec="itogi">
  <div class="wrap">
    <div class="sechead"><div class="kick">Итоги дня · сводная таблица</div></div>
    <h2>День, за который говорили только кадры</h2>
    <table class="sumtable">
      <tr><th>№</th><th>Происшествие</th><th>Город</th><th>Цена</th><th>Пресс-служба</th></tr>
      <tr><td class="id">01</td><td>Ограбление Ammu-Nation, перестрелка</td><td>Los Santos</td><td>пострадавшие</td><td>молчит</td></tr>
      <tr><td class="id">02</td><td>Фура и прицеп у автовокзала</td><td>Los Santos</td><td>помехи, помощи нет</td><td>не запрашивалась</td></tr>
      <tr><td class="id">03</td><td>Патруль и фура, встречная полоса</td><td>Los Santos</td><td>двое погибших полицейских</td><td>LSPD молчит</td></tr>
      <tr><td class="id">04</td><td>Перестрелка на Авторынке</td><td>Las Venturas</td><td>много пострадавших</td><td>LVPD молчит</td></tr>
      <tr><td class="id">05</td><td>Погоня в четыре экипажа</td><td>San Fierro</td><td>ущерб: десятки млн $</td><td>калькуляции нет</td></tr>
    </table>
    <p class="txt">Две пресс-службы за один день выбрали молчание - это тоже информация: о том, кому неудобны вопросы.
    Редакция продолжит задавать их письменно и печатать отказы рядом со сводками: молчание службы - часть картины дня,
    а не повод её свернуть. Города, между тем, отвечают сами: вертолётом на полотне, прицепом поперёк полосы,
    коленями подозреваемого на мосту.</p>
    <p class="txt">Завтра утром доска обнулится: новые строки, новые борты, новые отказы. Эта сводка остаётся
    в архиве как доказательство того, что 10 октября 2026 года штат говорил с нами кадрами - потому что службы
    говорить не стали.</p>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="frow2"><span>Кадры: Anna Village</span><span>Фоторедактор: Sonya Malboro</span><span>Текст и редактор: Jonny Wilde</span></div>
    <div class="frow2"><span>дизайн и вёрстка - редакция San Fierro News</span><span>10 октября 2026</span></div>
    <a class="pill" href="newsroom.html">&larr; Посмотреть все выпуски редакции</a>
  </div>
</footer>

<div class="lb" id="lb" role="dialog" aria-label="Просмотр кадра">
  <button class="lbx" id="lbx">закрыть · esc</button>
  <img id="lbimg" src="" alt="">
  <div class="lbcap" id="lbcap"></div>
  <div class="lbcnt" id="lbcnt"></div>
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
  var pbar=document.getElementById('pbar');
  var spy=function(){
    var y=window.innerHeight*0.35,cur=null;
    secs.forEach(function(s){var r=s.getBoundingClientRect();if(r.top<=y){cur=s.getAttribute('data-sec');}});
    btns.forEach(function(b){b.classList.toggle('cur',b.getAttribute('data-t')===cur);});
    var h=document.documentElement;
    var max=h.scrollHeight-h.clientHeight;
    pbar.style.width=(max>0?(h.scrollTop/max)*100:0)+'%';
  };
  var tick=false;
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(function(){spy();tick=false;});}},{passive:true});
  window.addEventListener('resize',function(){spy();});
  spy();
  var figs=[].slice.call(document.querySelectorAll('figure.shot'));
  var lb=document.getElementById('lb'),img=document.getElementById('lbimg'),cap=document.getElementById('lbcap'),cnt=document.getElementById('lbcnt');
  var i=-1;
  var show=function(n){i=(n+figs.length)%figs.length;var im=figs[i].querySelector('img');img.src=im.src;img.alt=im.alt;cap.textContent=im.alt;cnt.textContent='кадр '+(i+1)+' из '+figs.length;lb.classList.add('on');};
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
<title>San Fierro News — Сводка, которую не дали пресс-службы: пять происшествий 10 октября в трёх городах</title>
<meta name="description" content="Ежедневная газета San Fierro News от 10 октября 2026: ограбление Ammu-Nation с перестрелкой, фура у автовокзала без помощи, гибель двоих полицейских во встречном ударе у пляжа Santa Maria, перестрелка на Авторынке Las Venturas и финал погони в четыре экипажа на мосту San Fierro. LSPD и LVPD комментарии давать отказались.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;600;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
<style>
''' + CSS + '''</style>
</head>
<body>
''' + BODY + '''
<script>''' + JS + '''</script>
<!-- SFN · 2026 · 038 · dispatch-desk -->
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('written', OUT, len(html.encode('utf-8')) // 1024, 'KB')
