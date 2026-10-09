#!/usr/bin/env python3
"""SFN: ежедневная газета от 10.10.2026, второй выпуск даты: «Четыре загадки одной ночи».
Материал: inbox/ (6 кадров партии 10.10-b: доки, прицеп, полицейский, казино).
Стиль по заданию гендиректора - загадочный: туман, досье, штампы «нет ответа», вопросы вместо вердиктов.
Выход: anna-malboro/daily-10-10-2026-unknowns.html. Штамп 039 four-unknowns.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
IMG = os.path.join(HERE, 'img')
OUT = os.path.join(ROOT, 'anna-malboro', 'daily-10-10-2026-unknowns.html')


def b64(key):
    return open(os.path.join(IMG, key + '.b64')).read().strip()


CAPS = {
    'k1': 'Доки Los Santos сверху: военные ангары, вышки, кран - и ни одного человека. База стоит брошенной: ворота не заперты, посты пусты.',
    'k2': 'Внутри складов базы: люди в масках с винтовками у фургонов, ящики вскрыты. Пока военных нет в доках, банды разграбляют боезапасы.',
    'k3': 'Грунтовая дорога за городом, у самой воды: белый прицеп кинут без тягача. Контрабанда или последствия аварии - кадр не отвечает.',
    'k4': 'Ночное шоссе: патруль на обочине, белый спорткар с распахнутой дверью, тело на асфальте между ними. Приступник в маске убил полицейского при исполнении.',
    'k5': 'Caligula в ту же ночь: парковка забита, гирлянды на пальмах, фонтан светится. Казино работает в штатном режиме - бокалы полны, игра кипит.',
    'k6': 'The Four Dragons: красные пагоды над пустой площадью, две машины у бордюра, в окнах темно. Закрыто на техобслуживание - без объявления и сроков.',
}

FIG = '''<figure class="shot" data-lb>
      <img src="data:image/jpeg;base64,{B64}" alt="{CAP}" loading="lazy">
      <figcaption><b>{ID}</b> {CAP}</figcaption>
    </figure>'''


def fig(key, eid):
    return FIG.format(B64=b64(key), CAP=CAPS[key], ID=eid)


QS = '''<div class="quests">
      <div class="qlbl">Вопросы редакции · ответы не получены</div>
      <ul>{ITEMS}</ul>
    </div>'''


def quests(items):
    return QS.format(ITEMS=''.join('<li>' + i + '</li>' for i in items))


CSS = '''/* SFN-DESIGN-039: four-unknowns · 10.10.2026 */
:root{
  --bg:#0b0e14; --panel:#121722; --panel2:#0e131c; --ink:#dfe6ee; --mut:#8b96a5; --dim:#5d6875;
  --vio:#8f7bf0; --stamp:#c0453e; --line:rgba(223,230,238,.14);
  --disp:"Cormorant Garamond",Georgia,serif;
  --body:"Lora",Georgia,serif;
  --type:"Special Elite",ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:auto}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16.5px;line-height:1.72}
/* туман */
body::before{content:"";position:fixed;inset:-20%;z-index:-1;pointer-events:none;opacity:.55;
  background:
   radial-gradient(46% 34% at 22% 30%,rgba(143,123,240,.10),transparent 70%),
   radial-gradient(40% 30% at 78% 62%,rgba(120,150,190,.08),transparent 70%),
   radial-gradient(52% 40% at 50% 88%,rgba(192,69,62,.05),transparent 70%);
  animation:fog 46s linear infinite alternate}
@keyframes fog{from{transform:translate3d(-2%,-1%,0) scale(1)}to{transform:translate3d(2%,1.5%,0) scale(1.06)}}
.mono,.type{font-family:var(--type)}
.wrap{max-width:70rem;margin:0 auto;padding:0 1.3rem}
::selection{background:rgba(143,123,240,.35)}
/* мастхэд */
.mast{border-bottom:1px solid var(--line);background:rgba(14,19,28,.8);backdrop-filter:blur(6px)}
.mastin{display:flex;align-items:baseline;gap:1.1rem;flex-wrap:wrap;padding:1rem 0 .7rem}
.mastname{font-family:var(--disp);font-weight:700;font-size:1.7rem;letter-spacing:.12em;text-transform:uppercase}
.mastsub{font-family:var(--type);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.mastdate{margin-left:auto;font-family:var(--type);font-size:.7rem;letter-spacing:.14em;color:var(--vio);
  border:1px solid rgba(143,123,240,.45);border-radius:999px;padding:.34rem .9rem;background:rgba(143,123,240,.07)}
.kchip{font-family:var(--type);font-size:.62rem;letter-spacing:.14em;color:var(--dim);padding:0 0 .7rem}
/* герой */
.hero{padding:3.2rem 0 2.2rem;border-bottom:1px solid var(--line);position:relative;overflow:hidden}
.hero .qmark{position:absolute;right:-2rem;top:-4rem;font-family:var(--disp);font-weight:700;font-size:26rem;line-height:1;
  color:transparent;-webkit-text-stroke:1px rgba(143,123,240,.16);pointer-events:none;user-select:none}
.kick{font-family:var(--type);font-size:.66rem;letter-spacing:.26em;text-transform:uppercase;color:var(--vio);margin-bottom:1rem}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(2.4rem,6.4vw,4.4rem);line-height:1.04;max-width:22ch}
h1 em{font-style:italic;color:var(--vio)}
.stand{max-width:64ch;margin-top:1.15rem;color:var(--mut);font-size:1.04rem}
.stand b{color:var(--ink)}
/* оглавление досье */
.fileslbl{font-family:var(--type);font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin:2rem 0 .7rem}
.files{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.7rem}
.file{position:relative;text-align:left;cursor:pointer;font:inherit;color:var(--ink);background:var(--panel);
  border:1px solid var(--line);padding:.9rem 1rem 1.1rem;transition:.16s}
.file:hover{transform:translateY(-3px);border-color:rgba(143,123,240,.5);box-shadow:0 10px 26px rgba(0,0,0,.4)}
.file .fn{font-family:var(--type);font-size:.62rem;letter-spacing:.16em;color:var(--dim);text-transform:uppercase}
.file .ft{display:block;font-family:var(--disp);font-weight:700;font-size:1.25rem;line-height:1.15;margin:.35rem 0 .5rem}
.file .fs{font-family:var(--type);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;color:var(--stamp);
  border:1.6px solid rgba(192,69,62,.65);border-radius:3px;padding:.2rem .45rem;display:inline-block;transform:rotate(-2.5deg)}
/* навигация */
.snav{position:sticky;top:0;z-index:40;background:rgba(11,14,20,.92);backdrop-filter:blur(8px);border-block:1px solid var(--line)}
.snavin{display:flex;gap:.4rem;overflow-x:auto;padding:.5rem 0;scrollbar-width:none}
.snavin::-webkit-scrollbar{display:none}
.snavbtn{flex:none;cursor:pointer;font-family:var(--type);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--mut);background:transparent;border:1px solid var(--line);border-radius:999px;padding:.42rem .85rem;transition:.18s}
.snavbtn:hover{color:var(--ink);border-color:var(--vio)}
.snavbtn.cur{color:#0b0e14;background:var(--vio);border-color:var(--vio)}
/* досье-секции */
.sec{padding:2.9rem 0 1.3rem;border-bottom:1px solid var(--line);position:relative}
.sec::before{content:"?";position:absolute;right:2rem;top:2.2rem;font-family:var(--disp);font-weight:700;font-size:9rem;line-height:1;
  color:transparent;-webkit-text-stroke:1px rgba(143,123,240,.14);pointer-events:none}
.casehead{display:flex;align-items:baseline;gap:1rem;flex-wrap:wrap;margin-bottom:.4rem}
.casehead .cn{font-family:var(--type);font-size:.72rem;letter-spacing:.2em;color:var(--vio);text-transform:uppercase}
.casehead .cstamp{font-family:var(--type);font-size:.58rem;letter-spacing:.16em;text-transform:uppercase;color:var(--stamp);
  border:1.6px solid rgba(192,69,62,.65);border-radius:3px;padding:.2rem .5rem;transform:rotate(-2deg)}
h2{font-family:var(--disp);font-weight:700;font-size:clamp(1.7rem,3.8vw,2.6rem);line-height:1.1;max-width:30ch}
.lead{max-width:64ch;margin:1rem 0 .9rem;font-size:1.08rem;font-style:italic;color:var(--ink)}
.sec p.txt{max-width:66ch;margin:.55rem 0;color:#b9c2cd}
.known{margin:1.2rem 0;background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--vio);padding:.95rem 1.1rem}
.known h3{font-family:var(--type);font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--vio);margin-bottom:.5rem}
.known p{font-size:.96rem;color:#b9c2cd;max-width:64ch}
.quests{margin:1.1rem 0 1.3rem;background:var(--panel2);border:1px dashed rgba(192,69,62,.45);padding:.95rem 1.1rem}
.quests .qlbl{font-family:var(--type);font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--stamp);margin-bottom:.55rem}
.quests ul{list-style:none;display:grid;gap:.45rem}
.quests li{padding-left:1.5rem;position:relative;font-size:.97rem;color:#c4ccd6;font-style:italic}
.quests li::before{content:"?";position:absolute;left:.15rem;top:0;font-family:var(--disp);font-weight:700;font-size:1.15rem;color:var(--stamp)}
/* кадры */
.shot{margin:1.4rem 0}
.shot img{display:block;width:100%;height:auto;border:1px solid var(--line);background:#000;padding:.4rem;cursor:zoom-in;filter:saturate(.92) contrast(1.03)}
.shot figcaption{color:var(--mut);font-size:.92rem;margin-top:.55rem;max-width:72ch}
.shot figcaption b{font-family:var(--type);font-size:.7rem;color:var(--vio);letter-spacing:.08em;margin-right:.4rem}
.duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}
/* эпилог */
.epilog{margin:1.4rem 0;background:var(--panel);border:1px solid var(--line);padding:1.2rem 1.3rem}
.epilog h3{font-family:var(--disp);font-weight:700;font-size:1.35rem;margin-bottom:.6rem}
.epilog p{color:#b9c2cd;font-size:.98rem;max-width:68ch}
.epilog .sig{font-family:var(--type);font-size:.66rem;letter-spacing:.16em;color:var(--dim);margin-top:.8rem;text-transform:uppercase}
/* подвал */
footer{margin-top:3rem;border-top:1px solid var(--line);background:rgba(14,19,28,.85);padding:1.5rem 0 2.1rem}
.frow{display:flex;flex-wrap:wrap;gap:.6rem 1.6rem;align-items:center;font-family:var(--type);font-size:.64rem;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
.pill{display:inline-flex;align-items:center;gap:.5rem;margin-top:1.15rem;font-family:var(--type);font-size:.7rem;letter-spacing:.1em;
  color:var(--vio);text-decoration:none;border:1px solid rgba(143,123,240,.5);border-radius:999px;padding:.62rem 1.2rem;
  background:rgba(143,123,240,.07);box-shadow:0 0 18px rgba(143,123,240,.28);transition:.2s}
.pill:hover{background:var(--vio);color:#0b0e14;box-shadow:0 0 26px rgba(143,123,240,.45)}
/* лайтбокс */
.lb{position:fixed;inset:0;z-index:90;background:rgba(4,6,10,.95);display:none;align-items:center;justify-content:center;flex-direction:column;padding:2.4rem 1.2rem}
.lb.on{display:flex}
.lb img{max-width:min(1100px,94vw);max-height:78vh;border:1px solid rgba(223,230,238,.3)}
.lb .lbcap{color:#dfe6ee;font-size:.94rem;max-width:72ch;margin-top:.9rem;text-align:center}
.lb .lbcnt{font-family:var(--type);font-size:.62rem;letter-spacing:.2em;color:var(--vio);margin-top:.6rem}
.lb .lbx{position:absolute;top:1rem;right:1.2rem;cursor:pointer;background:transparent;border:1px solid rgba(223,230,238,.4);color:#dfe6ee;
  font-family:var(--type);font-size:.7rem;border-radius:999px;padding:.4rem .9rem}
.lb .lbnav{display:flex;gap:.7rem;margin-top:.8rem}
.lb .lbnav button{cursor:pointer;background:transparent;border:1px solid rgba(223,230,238,.4);color:#dfe6ee;font-family:var(--type);font-size:.7rem;border-radius:999px;padding:.42rem 1rem}
@media (max-width:640px){.mastdate{margin-left:0}.hero .qmark{display:none}.sec::before{display:none}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
'''

BODY = '''<header class="mast">
  <div class="wrap">
    <div class="mastin">
      <span class="mastname">San Fierro News</span>
      <span class="mastsub">ежедневная газета · выпуск вопросов</span>
      <span class="mastdate">суббота, 10 октября 2026</span>
    </div>
    <div class="kchip">Кадры: Anna Village · Фоторедактор: Sonya Malboro · Текст и редактор: Jonny Wilde</div>
  </div>
</header>

<section class="hero">
  <span class="qmark" aria-hidden="true">?</span>
  <div class="wrap">
    <div class="kick">Спецвыпуск дня · досье без вердиктов</div>
    <h1>Четыре загадки <em>одной ночи</em></h1>
    <p class="stand">Этот выпуск собран не из ответов, а из вопросов. Брошенная военная база в доках, кинутый прицеп
    у воды, убитый полицейский и маска за рулём спорткара, два казино с разной судьбой в одну ночь -
    <b>редакция показывает то, что видно, и честно пишет то, чего не знает.</b> Ниже - четыре досье: в каждом кадры,
    установленные факты и вопросы, на которые никто не ответил.</p>
    <div class="fileslbl">Оглавление досье · клик открывает дело</div>
    <div class="files">
      <button class="file" data-t="delo1"><span class="fn">Дело 01 · доки LS</span><span class="ft">База, которую оставили</span><span class="fs">нет ответа</span></button>
      <button class="file" data-t="delo2"><span class="fn">Дело 02 · окраина LS</span><span class="ft">Прицеп у воды</span><span class="fs">неизвестно</span></button>
      <button class="file" data-t="delo3"><span class="fn">Дело 03 · ночное шоссе</span><span class="ft">Маска и спорткар</span><span class="fs">нет ответа</span></button>
      <button class="file" data-t="delo4"><span class="fn">Дело 04 · Las Venturas</span><span class="ft">Два казино, одна ночь</span><span class="fs">неизвестно</span></button>
    </div>
  </div>
</section>

<nav class="snav" aria-label="Разделы выпуска">
  <div class="wrap"><div class="snavin">
    <button class="snavbtn" data-t="delo1">Дело 01 · База</button>
    <button class="snavbtn" data-t="delo2">Дело 02 · Прицеп</button>
    <button class="snavbtn" data-t="delo3">Дело 03 · Маска</button>
    <button class="snavbtn" data-t="delo4">Дело 04 · Казино</button>
    <button class="snavbtn" data-t="epilog">Вместо эпилога</button>
  </div></div>
</nav>

<section class="sec" data-sec="delo1">
  <div class="wrap">
    <div class="casehead"><span class="cn">Дело 01 · доки Los Santos</span><span class="cstamp">нет ответа</span></div>
    <h2>База, которую оставили</h2>
    <p class="lead">Военная база в доках стоит брошенной: ангары открыты ветру, вышки пусты, кран застыл над водой. И пока военных нет - банды разграбляют боезапасы.</p>
    ''' + fig('k1', 'EV-01') + '''
    <div class="known">
      <h3>Что установлено</h3>
      <p>База в доках пуста: ни постов у ворот, ни людей в ангарах, ни движения на внутренней дороге. Внутри складов -
      люди в масках с винтовками у фургонов и вскрытые ящики: разграбление идёт прямо в кадре, спокойно, как работа.</p>
    </div>
    ''' + fig('k2', 'EV-02') + '''
    ''' + quests([
      'Куда ушли военные с базы в доках - и ушли ли они сами?',
      'Кто отдал приказ оставить ангары и вышки без постов?',
      'Сколько ночей банды вывозят боезапасы - и почему первая ночь без охраны совпала с первой ночью без свидетелей?',
      'Кому предназначено оружие из вскрытых ящиков?',
    ]) + '''
  </div>
</section>

<section class="sec" data-sec="delo2">
  <div class="wrap">
    <div class="casehead"><span class="cn">Дело 02 · окраина Los Santos</span><span class="cstamp">неизвестно</span></div>
    <h2>Прицеп у воды</h2>
    <p class="lead">На грунтовой дороге за городом, у самой воды, стоит белый прицеп без тягача. Ни людей, ни следов аварии, ни объяснений.</p>
    <p class="txt">Прицеп входит в этот выпуск так же, как он вошёл в городскую повесть дня - один и без сопроводительных
    бумаг. Белый фургонный кузов стоит на грунтовке, которая не ведёт ни к складу, ни к причалу: она обрывается у воды,
    и дальше её продолжает только темнота. Тягача нет, дверей никто не охраняет, огоньков аварийки не горит - груз
    оставлен так, будто место выбрали заранее и знали, что возвращаться не придётся.</p>
    <p class="txt">Кинутый прицеп - всегда чьё-то решение, принятое в спехе. Либо водитель боялся доехать до точки,
    либо боялся остаться с грузом на глазах у города, либо точки больше не существует. Редакция не выбирает из этих
    версий ни одной: все три одинаково возможны и одинаково не доказаны. Контрабанда, которую не смогли довезти,
    и последствия аварии, о которой не заявили, - две версии, которые город уже шепчет по углам; обе остались шёпотом.</p>
    <p class="txt">Показательна и тишина служб: за прицепом за сутки не приехал никто - ни эвакуатор, ни дознание,
    ни хозяин. У брошенного груза в этом городе обычно есть очередь из претендентов; здесь очередь не выстроилась,
    и это, пожалуй, самая громкая деталь кадра. Молчание документов - тоже документ: редакция подшивает его в дело
    пустой строкой.</p>
    ''' + fig('k3', 'EV-03') + '''
    <div class="known">
      <h3>Что установлено</h3>
      <p>Прицеп отцеплен и оставлен на обочине грунтовой дороги, ведущей к воде; тягача рядом нет, дверей никто не
      охраняет. Город светит окнами на том берегу - и никто не пришёл за прицепом ни за ночь, ни днём.</p>
    </div>
    ''' + quests([
      'Контрабанда, которую не смогли довезти, или груз после аварии, о которой не заявили?',
      'Что было внутри: товар, который ищут, или товар, от которого избавились?',
      'Почему прицеп бросили именно у воды - здесь кончается дорога или начинается чья-то территория?',
    ]) + '''
  </div>
</section>

<section class="sec" data-sec="delo3">
  <div class="wrap">
    <div class="casehead"><span class="cn">Дело 03 · ночное шоссе</span><span class="cstamp">нет ответа</span></div>
    <h2>Маска и спорткар</h2>
    <p class="lead">Приступник в маске и на спорткаре убил полицейского при исполнении. На асфальте остались патруль, белый спорткар с распахнутой дверью и тело между ними.</p>
    <p class="txt">Ночное шоссе не оставляет свидетелей, но оставляет следы расстановки: патруль стоит на обочине ровно
    так, как ставят машину для остановки беглеца, а белый спорткар лёг поперёк полосы с распахнутой дверью - так,
    как ложится машина, из которой вышли на ходу и насовсем. Тело полицейского - между ними, на открытом асфальте:
    значит, разговор состоялся лицом к лицу, а не через стекло.</p>
    <p class="txt">Полицейский при исполнении погибает обычно одним способом: на вызове, к которому он готовился
    по уставу. Эта ночь предложила способ другой - маска, спорткар и выстрел в упор на пустой дороге выглядят не
    как случайная встреча, а как назначенное свидание. Кто и кому его назначил, редакция не знает и не берётся
    утверждать: заказное убийство и личные счёты - две версии, между которыми в кадре нет ни одной зацепки.</p>
    <p class="txt">Отдельная строка дела - поведение города после выстрела. Спорткар остался на месте: либо маска
    ушла пешком в темноту обочин, либо её ждали в третьей машине, которую ночь не показала камерам. Службы в эту
    смерть не говорили совсем - о молчании пресс-служб в тот день редакция собрала отдельную сводку
    («Сводка, которую не дали пресс-службы», выпуск от 10.10.2026); здесь оно звучит особенно глухо: молчать о гибели
    своего - значит оставить сослуживцев читать кадры вместо рапорта.</p>
    ''' + fig('k4', 'EV-04') + '''
    <div class="known">
      <h3>Что установлено</h3>
      <p>Патруль остановлен на обочине ночного шоссе; белый спорткар стоит поперёк полосы с открытой дверью, тело
      полицейского - на асфальте между машинами. Убийца в маске ушёл: ни одной фигуры, кроме стоящей у спорткара,
      кадр не удержал.</p>
    </div>
    ''' + quests([
      'Заказное убийство или личные счёты - что привело маску именно к этому патрулю?',
      'Почему спорткар бросили на месте: не завёлся, не рассчитал или не боялся?',
      'Кто стоял у открытой двери, когда патруль ещё подавал признаки жизни?',
      'Сколько таких масок сейчас спит в городе, пока служба молчит?',
    ]) + '''
  </div>
</section>

<section class="sec" data-sec="delo4">
  <div class="wrap">
    <div class="casehead"><span class="cn">Дело 04 · Las Venturas</span><span class="cstamp">неизвестно</span></div>
    <h2>Два казино, одна ночь</h2>
    <p class="lead">В одну и ту же ночь Caligula работает в штатном режиме - парковка забита, бокалы полны, игра кипит, - а The Four Dragons закрыто на техобслуживание без объявления и сроков.</p>
    <div class="duo">''' + fig('k5', 'EV-05') + fig('k6', 'EV-06') + '''</div>
    <div class="known">
      <h3>Что установлено</h3>
      <p>У Caligula - полная парковка, свет в окнах и гирлянды на пальмах: зал живёт. У Four Dragons - пустая площадь,
      две машины у бордюра и темнота в витринах: вывеска горит, дверей нет. Оба казино стоят на одной улице города,
      который не умеет спать.</p>
    </div>
    ''' + quests([
      'Что за «техобслуживание», о котором не предупредили ни гостей, ни город?',
      'Куда ушли сотрудники и игроки Four Dragons за одну ночь - в зал Caligula или дальше?',
      'Есть ли связь между закрытыми дверями одного казино и полной парковкой другого?',
    ]) + '''
  </div>
</section>

<section class="sec" data-sec="epilog">
  <div class="wrap">
    <div class="casehead"><span class="cn">Вместо эпилога</span></div>
    <h2>Газета, которая умеет говорить «не знаю»</h2>
    <div class="epilog">
      <h3>Четыре досье, ноль вердиктов</h3>
      <p>Редакция не станет дорисовывать то, чего не видела: у четырёх загадок этой ночи нет ответов, и честнее
      поставить штамп «нет ответа», чем выдумать виновного. Кадры остаются в архиве, вопросы остаются открытыми,
      а места под ответы в каждом досье приготовлены. Когда службы, базы или казино заговорят - их слова встанут
      рядом с этими строками без правок и без скидок.</p>
      <p>Город молчит не всегда: иногда он просто ждёт, пока вопрос зададут вслух. Этот выпуск - четыре вопроса,
      заданных вслух.</p>
      <div class="sig">редакция San Fierro News · 10 октября 2026 · досье остаются открытыми</div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="frow"><span>Кадры: Anna Village</span><span>Фоторедактор: Sonya Malboro</span><span>Текст и редактор: Jonny Wilde</span></div>
    <div class="frow"><span>дизайн и вёрстка - редакция San Fierro News</span><span>10 октября 2026 · выпуск вопросов</span></div>
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
  var spy=function(){
    var y=window.innerHeight*0.35,cur=null;
    secs.forEach(function(s){var r=s.getBoundingClientRect();if(r.top<=y){cur=s.getAttribute('data-sec');}});
    btns.forEach(function(b){b.classList.toggle('cur',b.getAttribute('data-t')===cur);});
  };
  var tick=false;
  window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(function(){spy();tick=false;});}},{passive:true});
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
<title>San Fierro News — Четыре загадки одной ночи: выпуск вопросов от 10 октября 2026</title>
<meta name="description" content="Ежедневная газета San Fierro News от 10 октября 2026, выпуск вопросов: брошенная военная база в доках Los Santos и разграбляемые боезапасы, кинутый прицеп у воды, убитый полицейский и маска за рулём спорткара, два казино с разной судьбой в одну ночь. Четыре досье, ноль вердиктов.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=Lora:ital,wght@0,400;0,600;1,400&family=Special+Elite&display=swap" rel="stylesheet">
<style>
''' + CSS + '''</style>
</head>
<body>
''' + BODY + '''
<script>''' + JS + '''</script>
<!-- SFN · 2026 · 039 · four-unknowns -->
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('written', OUT, len(html.encode('utf-8')) // 1024, 'KB')
