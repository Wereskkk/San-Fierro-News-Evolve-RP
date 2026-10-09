#!/usr/bin/env python3
"""SFN: сборка ежедневной газеты 08.10.2026 (Los Santos, суффикс -los-santos), смысл «Очередь, которая не расходится».
Фактура гендиректора: очередь стоит на вокзале в Los Santos и не может уехать,
потому что в городе безработица; автобусы и такси не работают.
Композиция-кольцо: вокзал вечером -> адреса пустой работы по штату -> стоящий транспорт
-> вокзал ночью: очередь не расходится. Название: «Очередь, которая не расходится».
Кадры: work/daily0810/img/b*.b64 (10 шт). Выход: anna-malboro/daily-07-10-2026.html (URL вечный).
Штамп 035 ten-silent-addresses (имя дизайна живёт с первой редакции).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
IMG = os.path.join(HERE, 'img')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-08-10-2026-los-santos.html')


def b64(key):
    return open(os.path.join(IMG, key + '.b64')).read().strip()


SHOTS = {
    'b09': 'Вокзал Los Santos, вечер: у дверей люди - кто с вещами, кто просто стоит. Автобусы не приходят, такси не едут: уезжать нечем.',
    'b01': 'Сады на холмах: ряды целы, под деревьями падалица - поднимать некому. Работа, которой нет, - это тоже безработица.',
    'b03': 'Сады у воды: ни стремянки, ни ящика под деревьями. Урожай доспевает сам - городу он не нужен.',
    'b04': 'Пастбище в холмах: изгородь делит пустые загоны. Ни скота, ни пастуха: село без работы вслед за городом.',
    'b02': 'Ферма у воды: комбайн со снятой жаткой, пикап с пустым кузовом у изгороди. Двор цел - работы нет.',
    'b05': 'Портовый двор: погрузчики выстроены вдоль стены, грузовые навесы пусты. Нет груза - нет и смены.',
    'b06': 'Склад изнутри: стеллажи полупустые, пол подметён. Помещение, в котором никого не ждут.',
    'b07': 'Грузовая платформа: паллеты с ярлыками у стены, вагоны с открытыми дверями. Погрузку бросили на полуслове - как всё в этом городе.',
    'b08': 'Автобусный двор: семь машин носами к стене, ни одной на маршруте. Именно поэтому очередь на вокзале не расходится.',
    'b10': 'Те же двери, ночь: очередь не стала меньше. Город не выпускает людей: работы здесь нет, а транспорта наружу - тоже.',
}

FIG = '''<figure class="shot" data-lb>
      <img src="data:image/jpeg;base64,{B64}" alt="{CAP}" loading="lazy">
      <figcaption>{CAP}</figcaption>
    </figure>'''


def fig(key):
    return FIG.format(B64=b64(key), CAP=SHOTS[key])


# силуэт человека в очереди: мотив проходит лентой через всю страницу
QSVG = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='26' height='24' "
        "viewBox='0 0 26 24'><circle cx='12' cy='5' r='3.4' fill='%23262219'/>"
        "<path d='M7 24c0-6.4 2.2-9.6 5-9.6s5 3.2 5 9.6z' fill='%23262219'/>"
        "<rect x='19' y='15' width='5' height='9' rx='1' fill='%239c4a2f'/></svg>\")")

CSS = '''/* SFN-DESIGN-035: ten-silent-addresses · 07.10.2026 */
:root{
  --paper:#ebe6db; --panel:#f5f1e8; --ink:#262219; --mut:#6f6759; --dim:#8d8474;
  --rust:#9c4a2f; --moss:#5f7052; --line:rgba(38,34,25,.16);
  --disp:"PT Sans Narrow",system-ui,sans-serif;
  --body:"PT Serif",Georgia,serif;
  --mono:"PT Mono",ui-monospace,monospace;
  --qsil:__QSVG__;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:auto}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.68}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
   repeating-linear-gradient(0deg,rgba(38,34,25,.028) 0 1px,transparent 1px 34px),
   radial-gradient(760px 420px at 88% -120px,rgba(156,74,47,.07),transparent 70%),
   radial-gradient(680px 420px at -8% 30%,rgba(95,112,82,.06),transparent 70%)}
.mono{font-family:var(--mono)}
.wrap{max-width:72rem;margin:0 auto;padding:0 1.3rem}
::selection{background:rgba(156,74,47,.25)}
/* мастхэд */
.mast{border-bottom:3px double var(--ink);background:var(--panel)}
.mastin{display:flex;align-items:baseline;gap:1.1rem;flex-wrap:wrap;padding:1.05rem 0 .8rem}
.mastname{font-family:var(--disp);font-weight:700;font-size:1.5rem;letter-spacing:.16em;text-transform:uppercase}
.mastsub{font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.mastdate{margin-left:auto;font-family:var(--mono);font-size:.72rem;letter-spacing:.14em;color:var(--rust);
  border:1px solid rgba(156,74,47,.45);border-radius:999px;padding:.34rem .9rem;background:rgba(156,74,47,.06)}
.kchip{font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;color:var(--dim);padding:0 0 .7rem}
/* герой */
.hero{padding:2.9rem 0 2.1rem;border-bottom:1px solid var(--line)}
.kick{font-family:var(--mono);font-size:.68rem;letter-spacing:.26em;text-transform:uppercase;color:var(--rust);margin-bottom:1rem}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(2.2rem,6vw,4.2rem);line-height:1.04;letter-spacing:.005em;text-transform:uppercase;max-width:24ch}
h1 em{font-style:normal;color:var(--rust)}
.stand{max-width:66ch;margin-top:1.15rem;color:var(--mut);font-size:1.05rem}
.stand b{color:var(--ink)}
.queueband{margin:1.7rem 0 .5rem;height:24px;background:var(--qsil) repeat-x left bottom/26px 24px;opacity:.85}
.queuelbl{font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;margin-top:1.6rem}
.tile{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--rust);padding:.9rem 1rem}
.tile .big{font-family:var(--disp);font-weight:700;font-size:2rem;line-height:1}
.tile .lbl{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin-top:.45rem}
/* навигация */
.snav{position:sticky;top:0;z-index:40;background:rgba(235,230,219,.94);backdrop-filter:blur(7px);border-block:1px solid var(--line)}
.snavin{display:flex;gap:.4rem;overflow-x:auto;padding:.5rem 0;scrollbar-width:none}
.snavin::-webkit-scrollbar{display:none}
.snavbtn{flex:none;cursor:pointer;font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--mut);background:transparent;border:1px solid var(--line);border-radius:999px;padding:.4rem .85rem;transition:.18s}
.snavbtn:hover{color:var(--ink);border-color:var(--rust)}
.snavbtn.cur{color:var(--paper);background:var(--rust);border-color:var(--rust)}
/* секции-статьи: лента очереди соединяет разделы */
.sec{position:relative;padding:2.6rem 0 1.2rem}
.sec::before{content:"";position:absolute;top:0;left:0;right:0;height:24px;
  background:var(--qsil) repeat-x left center/26px 24px;opacity:.5}
.sechead .kick{margin-bottom:.5rem}
h2{font-family:var(--disp);font-weight:700;font-size:clamp(1.5rem,3.4vw,2.3rem);text-transform:uppercase;letter-spacing:.02em;line-height:1.1}
/* лид БЕЗ буквицы: буквица снята по вердикту гендиректора 09.10.2026 («некрасиво смотрится») */
.lead{max-width:64ch;margin:1rem 0 .9rem;font-size:1.12rem;font-style:italic;color:var(--ink)}
.sec p.txt{max-width:66ch;margin:.55rem 0;color:#3a3428}
.pull{max-width:60ch;margin:1.3rem 0;padding:.4rem 0 .4rem 1.1rem;border-left:3px solid var(--rust);
  font-family:var(--disp);font-weight:700;font-size:1.35rem;line-height:1.3;text-transform:uppercase;letter-spacing:.02em}
.pull .who{display:block;font-family:var(--mono);font-weight:400;font-size:.64rem;letter-spacing:.16em;color:var(--mut);margin-top:.5rem;text-transform:none}
.shot{margin:1.4rem 0}
.shot img{display:block;width:100%;height:auto;border:1px solid var(--line);background:#fff;padding:.5rem;cursor:zoom-in}
.shot figcaption{font-family:var(--body);font-style:italic;color:var(--mut);font-size:.92rem;margin-top:.55rem;max-width:70ch}
.duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}
/* заметка редакции */
.method{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--moss);padding:1.1rem 1.2rem;margin:1.4rem 0}
.method h3{font-family:var(--disp);text-transform:uppercase;letter-spacing:.08em;font-size:1rem;margin-bottom:.5rem}
.method p{font-size:.95rem;color:var(--mut);max-width:70ch}
/* подвал */
footer{margin-top:3rem;border-top:3px double var(--ink);background:var(--panel);padding:1.6rem 0 2.2rem}
.frow{display:flex;flex-wrap:wrap;gap:.6rem 1.6rem;align-items:center;font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
.pill{display:inline-flex;align-items:center;gap:.5rem;margin-top:1.2rem;font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;
  color:var(--rust);text-decoration:none;border:1px solid rgba(156,74,47,.5);border-radius:999px;padding:.62rem 1.2rem;
  background:rgba(156,74,47,.06);box-shadow:0 0 18px rgba(156,74,47,.28);transition:.2s}
.pill:hover{background:var(--rust);color:var(--paper);box-shadow:0 0 26px rgba(156,74,47,.45)}
/* лайтбокс */
.lb{position:fixed;inset:0;z-index:90;background:rgba(20,17,12,.93);display:none;align-items:center;justify-content:center;flex-direction:column;padding:2.4rem 1.2rem}
.lb.on{display:flex}
.lb img{max-width:min(1100px,94vw);max-height:78vh;border:1px solid rgba(245,241,232,.35);background:#fff;padding:.4rem}
.lb .lbcap{color:#e8e2d5;font-style:italic;font-size:.94rem;max-width:70ch;margin-top:.9rem;text-align:center}
.lb .lbx{position:absolute;top:1rem;right:1.2rem;cursor:pointer;background:transparent;border:1px solid rgba(245,241,232,.4);color:#e8e2d5;
  font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.4rem .9rem}
.lb .lbnav{display:flex;gap:.7rem;margin-top:.9rem}
.lb .lbnav button{cursor:pointer;background:transparent;border:1px solid rgba(245,241,232,.4);color:#e8e2d5;font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.42rem 1rem}
@media (max-width:640px){
  .mastdate{margin-left:0}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''.replace('__QSVG__', QSVG)

BODY = '''<header class="mast">
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
    <div class="kick">Репортаж дня · Los Santos</div>
    <h1>Очередь, которая <em>не расходится</em></h1>
    <p class="stand">Вечер на вокзале Los Santos: у дверей стоят люди - с вещами и без. Им некуда уехать:
    <b>в городе безработица, автобусы и такси не работают.</b> Редакция прошла по адресам, где раньше была работа,
    посмотрела на стоящие автобусы - и вернулась к тем же дверям ночью: очередь не стала меньше.</p>
    <div class="queueband" aria-hidden="true"></div>
    <div class="queuelbl">Лента очереди · мотив выпуска: люди, которые ждут транспорта, которого нет</div>
    <div class="tiles">
      <div class="tile"><div class="big">1</div><div class="lbl">очередь · вечер и ночь у одних дверей</div></div>
      <div class="tile"><div class="big">7</div><div class="lbl">автобусов не на маршрутах</div></div>
      <div class="tile"><div class="big">7</div><div class="lbl">адресов пустой работы по штату</div></div>
      <div class="tile"><div class="big">0</div><div class="lbl">работающих маршрутов в городе</div></div>
    </div>
  </div>
</section>

<nav class="snav" aria-label="Разделы выпуска">
  <div class="wrap"><div class="snavin">
    <button class="snavbtn" data-t="vecher">Вокзал · вечер</button>
    <button class="snavbtn" data-t="adresa">Адреса пустой работы</button>
    <button class="snavbtn" data-t="gruz">Порт, склад, рельсы</button>
    <button class="snavbtn" data-t="transport">Транспорт стоит</button>
    <button class="snavbtn" data-t="noch">Вокзал · ночь</button>
    <button class="snavbtn" data-t="itog">Итог</button>
  </div></div>
</nav>

<section class="sec" data-sec="vecher">
  <div class="wrap">
    <div class="sechead"><div class="kick">Los Santos · вокзал · вечер</div><h2>Люди, которым нечем уехать</h2></div>
    <p class="lead">У дверей вокзала Los Santos к вечеру собирается очередь: кто-то с вещами, кто-то просто стоит. Автобусы не приходят, такси не едут - уезжать нечем.</p>
    <p class="txt">Это не очередь за билетами: билеты здесь ни при чём. Люди стоят у дверей, за которыми нет зала
    ожидания с расписанием, - есть только город, в котором закрылись смены. Кто-то приезжает сюда каждое утро по привычке:
    вокзал - последнее место в городе, откуда теоретически можно уехать.</p>
    <p class="txt">Теоретически. Практично - нечем: маршруты сняты, таксопарки стоят. Редакция начинает репортаж от этих
    дверей и к ним же вернётся в финале: между вечером и ночью - весь ответ на вопрос, почему очередь не расходится.</p>
    {F_B09}
  </div>
</section>

<section class="sec" data-sec="adresa">
  <div class="wrap">
    <div class="sechead"><div class="kick">Почему в городе нет работы · поля и фермы</div><h2>Адреса пустой работы</h2></div>
    <p class="lead">Безработица в Los Santos начинается не в городе: она начинается там, где раньше растили, собирали и кормили. Редакция прошла семь адресов - и на каждом застала работу, которой нет.</p>
    <p class="txt">Сады на холмах и у воды стоят с целыми изгородями и несобранным урожаем: под деревьями рыжеет падалица,
    стремянки нет ни под одним деревом. Пастбище в холмах по-прежнему поделено на загоны, но скота нет, и будка пастуха
    распахнута настежь. Ферма у воды бережёт комбайн со снятой жаткой и пикап с пустым кузовом: двор цел, порядок наведён -
    только работать некому и не для кого.</p>
    <p class="txt">Город, который не кормит своё село, остаётся без работы сам: нечего возить, нечего грузить, нечего
    продавать. От этих полей нитка тянется прямо к порту и вокзалу - дальше редакция идёт по ней.</p>
    <div class="duo">{F_B01}{F_B03}</div>
    <div class="duo">{F_B04}{F_B02}</div>
  </div>
</section>

<section class="sec" data-sec="gruz">
  <div class="wrap">
    <div class="sechead"><div class="kick">Почему в городе нет работы · порт, склад, рельсы</div><h2>Груз, который никуда не едет</h2></div>
    <p class="lead">Портовый двор, склад и грузовая платформа - три адреса, где работа остановилась на полуслове: погрузчики на смотре, стеллажи полупустые, вагоны с открытыми дверями.</p>
    <p class="txt">В портовом дворе погрузчики выстроены вдоль стены, как на смотре, а грузовые навесы пусты: ни машины
    под погрузку. Внутри склада пол подметён, ящики с ярлыками составлены аккуратно - так убираются, уходя надолго.
    На грузовой платформе паллеты стоят у стены, вагоны на путях распахнуты: погрузку прекратили, не договорив смену.</p>
    <p class="txt">Ярлыки на коробках - местные, внутриштатные: груз не собирался далеко ехать. Он просто перестал быть
    нужным. Вместе с ним перестали быть нужны смены, бригады и маршруты - всё то, из чего состоит живой город.</p>
    <div class="duo">{F_B05}{F_B06}</div>
    {F_B07}
  </div>
</section>

<section class="sec" data-sec="transport">
  <div class="wrap">
    <div class="sechead"><div class="kick">Почему очередь не расходится · транспорт</div><h2>Семь автобусов и ни одного маршрута</h2></div>
    <p class="lead">Автобусный двор за белым зданием: семь машин стоят носами к стене, ни одной на маршруте. Такси в городе не работают следом за автобусами - перевозить некого и некуда.</p>
    <p class="txt">Площадку даже не размечали под простой: машины встали как попало, будто водители вышли на минуту
    и задержались на сезон. Остановка у двора пуста дважды - без людей и без расписания. Таксопарки редакция смотрела
    отдельно: стоянки пусты так же, только таблички на диспетчерских будках ещё обещают подачу за десять минут.</p>
    <p class="txt">Вот и весь механизм очереди на вокзале: человеку некуда идти на работу, потому что работы нет,
    и нечем уехать, потому что транспорт встал вслед за работой. Очередь стоит не за надеждой - она стоит без альтернативы.</p>
    {F_B08}
  </div>
</section>

<section class="sec" data-sec="noch">
  <div class="wrap">
    <div class="sechead"><div class="kick">Los Santos · вокзал · ночь</div><h2>Те же двери: очередь не разошлась</h2></div>
    <p class="lead">Ночью редакция вернулась к вокзалу тем же маршрутом: очередь у дверей стала короче, но не разошлась. Люди стоят молча, без плакатов и криков - это не митинг, это ожидание.</p>
    <p class="txt">Здание не светит окнами: внутри никого, снаружи - те, кому утром снова сюда. За спиной очереди город
    не спорит и не гудит: он ждёт вместе с ней. Редакция не подходила с вопросами: у очереди есть право не разговаривать.</p>
    <p class="txt">Мы оставили ей два кадра - вечерний и ночной, - потому что один выглядел бы случайностью.
    Случайностью это не является: за час между снимками не изменилось ничего, что могло бы разогнать очередь.</p>
    {F_B10}
  </div>
</section>

<section class="sec" data-sec="itog">
  <div class="wrap">
    <div class="sechead"><div class="kick">Итог репортажа</div><h2>Очередь - это город, который ждёт</h2></div>
    <p class="lead">Ответ на вопрос «почему очередь не расходится» собран по всему выпуску: работы в городе нет, транспорт встал вслед за работой, вокзал остался единственной дверью наружу - и та не открывается.</p>
    <p class="txt">Завтра утром у этих дверей снова будут люди: за ночь не появится ни работы, ни маршрутов.
    Редакция продолжит снимать эту очередь каждый день, пока она не распадётся сама - или пока город не начнёт
    выходить из неё на смены. Третьего у очередей не бывает.</p>
    <div class="pull">Очередь - это не люди. Это город, который ждёт.<span class="who">последняя строка репортажа, 08.10.2026</span></div>
    <div class="method">
      <h3>Заметка редакции</h3>
      <p>Вечерний и ночной кадры сняты у одних дверей вокзала Los Santos: редакция снимала дважды, чтобы показать -
      очередь не расходится. Людей в очереди редакция не пересчитывает: очередь живая, кто-то отходит согреться,
      кто-то подходит с вещами. Безработица в городе и стоящие автобусы с такси - факты, с которых начался этот
      репортаж; семь адресов пустой работы по штату - его середина; ночь у дверей - его конец, который пока не конец.</p>
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
<title>San Fierro News — Очередь, которая не расходится: вокзал Los Santos и семь адресов пустой работы</title>
<meta name="description" content="Ежедневный репортаж San Fierro News от 8 октября 2026: очередь у вокзала Los Santos, которой нечем уехать - в городе безработица, автобусы и такси не работают; семь адресов пустой работы по штату и стоящий автобусный двор; вечер и ночь у одних дверей.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=PT+Sans+Narrow:wght@400;700&family=PT+Serif:ital,wght@0,400;0,700;1,400&family=PT+Mono&display=swap" rel="stylesheet">
<style>
''' + CSS + '''</style>
</head>
<body>
''' + BODY.format(F_B01=fig('b01'), F_B02=fig('b02'), F_B03=fig('b03'), F_B04=fig('b04'),
                  F_B05=fig('b05'), F_B06=fig('b06'), F_B07=fig('b07'), F_B08=fig('b08'),
                  F_B09=fig('b09'), F_B10=fig('b10')) + '''
<script>''' + JS + '''</script>
<!-- SFN · 2026 · 035 · ten-silent-addresses -->
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('written', OUT, len(html.encode('utf-8')) // 1024, 'KB')
