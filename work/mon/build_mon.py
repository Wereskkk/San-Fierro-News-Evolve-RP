#!/usr/bin/env python3
"""SFN: еженедельное расследование №2 «За белым халатом» (МОН / Минздрав).
Материал: inbox-mon/ (Выдача задания 13, Два полных рабочих дня 35, Собеседование 52).
Диалоги передачи задания и приёма отчёта - дословно из файлов гендиректора.
Транскрипт собеседования и хронология инструктажа - восстановлены по строкам над
головами в кадрах и chat-логу кадра 55 (кадр 55 в страницу НЕ вшит: в HUD видно
серверное имя - нарушило бы RP-чистоту; из лога взяты только строки дела).
Выход: anna-malboro/investigation-whitecoat.html. Штамп 037 white-coat-days.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
IMG = os.path.join(HERE, 'imgmon')
OUT = os.path.join(ROOT, 'anna-malboro', 'investigation-whitecoat.html')


def b64(key):
    return open(os.path.join(IMG, key + '.b64')).read().strip()


CAPS = {
    'v1': 'Редакция, вечер: генеральный директор принимает программного директора - разговор, с которого начинается дело №2.',
    'v2': 'Anna Village слушает: до этого вечера она готовила недельный выпуск, а не собственное увольнение.',
    'v3': 'Задание выдано: на несколько дней редакция останется без программного директора.',
    's4': 'Министерство здравоохранения, кабинет: «Добрый день, присаживайтесь» - главврач Lisa Akana начинает собеседование.',
    's13': 'Ответ Анны на вопрос об опыте: «Работала медсестрой в армии города Сан Фиерро».',
    's25': '*взяла анкету* - бумаги интернатуры легли на стол кабинета.',
    's31': '«Сначала вот Ваш бейджик N13. Носите его гордо, не забывайте и не теряйте!»',
    's37': '«Рабочий график: 9:00-21:00 по будням и 10:00-20:00 по выходным».',
    's49': '«Первое: лечение. Лечение производится в больнице или в карете скорой помощи».',
    's53': '«Третье: развозка медикаментов. Это одна из самых важных обязанностей в МОН!»',
    's1': '«Можете приступать к работе!» - кадр, после которого интерн Анна уходит на первую смену.',
    'd1': 'Начало смены: раздевалка, гражданская одежда остаётся на скамейке.',
    'd2': 'Палата: интерн Анна проводит первую манипуляцию без наставницы - ректальный осмотр; пациентка на койке - Sonya Sweazy.',
    'd4': 'Машина скорой помощи выходит из двора больницы: первый вызов смены.',
    'd8': 'Полевой вызов на закате: двое на земле под деревом - один из них погибший, которого интерн позже отвезёт в морг Las Venturas (EV-16).',
    'd12': 'Морг Las Venturas: Анна привезла тело погибшего с закатного вызова - четвёртый пункт обязанностей главврача: эвакуация погибших.',
    'd14': 'Комната отдыха: на диване - губернатор штата Carl Village; его сотрудник Vanya Rodnik уже вызвал помощь - вызов приняла интерн, дежурившая в эту смену.',
    'd19': 'Анна приняла вызов и узнала мужа: искусственное дыхание на диване комнаты отдыха. Приступ губернатора отступил - его спасли руки собственной жены, дежурившей инкогнито.',
    'd24': 'Вторая смена начинается той же раздевалкой и тем же синим ключом формы.',
    'd32': 'Вызов в пустыне: скорая стоит на песке, пациент лежит на открытом солнце; погрузка на носилки начинается вручную.',
    'd34': 'Погрузка в машину №42: с земли на носилки - вручную.',
    'd35': 'Ночь: скорые смены выстроены у больницы - смена окончена.',
    'd28': 'Конец второго дня: дом. *открыла дневник и начала записывать* - блокнот, из которого выросла последняя запись дела.',
    'r27': 'Возвращение: Anna Village у дверей кабинета генерального директора - «Здравствуйте. Можно войти?» Пропуск пресс-службы снова на груди.',
    'r28': 'Генеральный директор принимает отчёт: «Хорошая работа. Передавай отчёт.» На журнальном столике - свежий номер: дело вернулось в редакцию не только папкой.',
}

FIG = '''<figure class="shot" data-lb>
      <img src="data:image/jpeg;base64,{B64}" alt="{CAP}" loading="lazy">
      <figcaption><b>{ID}</b> {CAP}</figcaption>
    </figure>'''


def fig(key, eid):
    return FIG.format(B64=b64(key), CAP=CAPS[key], ID=eid)


DLG = '''<div class="dlg"><span class="sp {CLS}">{WHO}</span><span class="ln">{TXT}</span></div>'''

CSS = '''/* SFN-DESIGN-037: white-coat-days · 09.10.2026 */
:root{
  --paper:#f9fbfa; --panel:#eef4f2; --ink:#16241f; --mut:#5c6b64; --dim:#8a978f;
  --teal:#0e7a63; --alert:#b3372e; --amber:#c07a1d; --line:rgba(22,36,31,.16);
  --disp:"Fira Sans Condensed",system-ui,sans-serif;
  --body:"Bitter",Georgia,serif;
  --mono:"Fira Mono",ui-monospace,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:auto}
body{background:var(--paper);color:var(--ink);font-family:var(--body);font-size:16.5px;line-height:1.7}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
  background:
   repeating-linear-gradient(0deg,rgba(22,36,31,.025) 0 1px,transparent 1px 36px),
   radial-gradient(800px 420px at 90% -140px,rgba(14,122,99,.07),transparent 70%),
   radial-gradient(640px 400px at -6% 24%,rgba(179,55,46,.05),transparent 70%)}
.mono{font-family:var(--mono)}
.wrap{max-width:72rem;margin:0 auto;padding:0 1.3rem}
::selection{background:rgba(14,122,99,.22)}
/* мастхэд */
.mast{border-bottom:3px solid var(--ink);background:#fff}
.mastin{display:flex;align-items:baseline;gap:1.1rem;flex-wrap:wrap;padding:1rem 0 .7rem}
.mastname{font-family:var(--disp);font-weight:700;font-size:1.6rem;letter-spacing:.14em;text-transform:uppercase}
.mastsub{font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--mut)}
.mastcase{margin-left:auto;font-family:var(--mono);font-size:.72rem;letter-spacing:.14em;color:var(--teal);
  border:1px solid rgba(14,122,99,.45);border-radius:999px;padding:.34rem .9rem;background:rgba(14,122,99,.06)}
.kchip{font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;color:var(--dim);padding:0 0 .7rem}
/* герой */
.hero{padding:2.9rem 0 2rem;border-bottom:1px solid var(--line);position:relative}
.ecg{position:absolute;top:1.1rem;left:0;right:0;height:44px;opacity:.5;pointer-events:none}
.kick{font-family:var(--mono);font-size:.68rem;letter-spacing:.26em;text-transform:uppercase;color:var(--teal);margin-bottom:1rem}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(2.3rem,6.2vw,4.3rem);line-height:1.03;text-transform:uppercase;letter-spacing:.01em;max-width:22ch}
h1 em{font-style:normal;color:var(--teal)}
.stand{max-width:68ch;margin-top:1.1rem;color:var(--mut);font-size:1.04rem}
.stand b{color:var(--ink)}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.5rem}
.chip{font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink);
  border:1px solid var(--line);background:#fff;border-radius:999px;padding:.42rem .9rem}
.chip b{color:var(--teal)}
.verdictplate{margin-top:1.6rem;display:inline-block;background:var(--ink);color:#e7efec;font-family:var(--mono);
  font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;padding:.7rem 1.1rem;transform:rotate(-1.2deg)}
.verdictplate b{color:#7fd6bd}
/* навигация */
.snav{position:sticky;top:0;z-index:40;background:rgba(249,251,250,.94);backdrop-filter:blur(7px);border-block:1px solid var(--line)}
.snavin{display:flex;gap:.4rem;overflow-x:auto;padding:.5rem 0;scrollbar-width:none}
.snavin::-webkit-scrollbar{display:none}
.snavbtn{flex:none;cursor:pointer;font-family:var(--mono);font-size:.62rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--mut);background:transparent;border:1px solid var(--line);border-radius:999px;padding:.4rem .8rem;transition:.18s}
.snavbtn:hover{color:var(--ink);border-color:var(--teal)}
.snavbtn.cur{color:#fff;background:var(--teal);border-color:var(--teal)}
/* секции */
.sec{padding:2.6rem 0 1.2rem;border-bottom:1px solid var(--line)}
.sechead .kick{margin-bottom:.45rem}
h2{font-family:var(--disp);font-weight:700;font-size:clamp(1.6rem,3.6vw,2.4rem);text-transform:uppercase;letter-spacing:.02em;line-height:1.1}
.lead{max-width:66ch;margin:1rem 0 .9rem;font-size:1.1rem;font-style:italic}
.sec p.txt{max-width:68ch;margin:.55rem 0;color:#2c3a34}
/* диалоги */
.dlgbox{margin:1.2rem 0;background:#fff;border:1px solid var(--line);padding:1rem 1.1rem;display:grid;gap:.55rem}
.dlg{display:grid;grid-template-columns:11.5rem 1fr;gap:.9rem;align-items:baseline}
.dlg .sp{font-family:var(--mono);font-size:.66rem;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
.dlg .sp.jd{color:var(--amber)} .dlg .sp.av{color:var(--teal)} .dlg .sp.la{color:var(--alert)}
.dlg .ln{font-size:.98rem;color:#22302a}
/* документы */
.doccard{margin:1.3rem 0;background:#fff;border:1px solid var(--line);border-left:4px solid var(--ink);padding:1.1rem 1.2rem;position:relative}
.doccard .stamp{position:absolute;top:.8rem;right:1rem;font-family:var(--mono);font-size:.66rem;letter-spacing:.2em;
  color:var(--teal);border:2px solid var(--teal);border-radius:4px;padding:.3rem .6rem;transform:rotate(6deg)}
.doccard h3{font-family:var(--mono);font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin-bottom:.7rem}
.docrow{display:grid;grid-template-columns:9rem 1fr;gap:.8rem;padding:.3rem 0;border-top:1px dashed var(--line);font-size:.95rem}
.docrow b{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--mut);padding-top:.15rem}
/* хронология chat-лога */
.logbox{margin:1.2rem 0;background:#101c17;color:#cfe4da;font-family:var(--mono);font-size:.76rem;line-height:1.75;padding:1rem 1.1rem;border:1px solid #0b1410}
.logbox .t{color:#7fd6bd}
.logbox .n{color:#e9b8a4}
.logbox .note{color:#7fd6bd;font-style:normal;letter-spacing:.16em;text-transform:uppercase;font-size:.6rem;margin-bottom:.5rem}
.notebook{margin:1.6rem 0;background:repeating-linear-gradient(0deg,transparent 0 30px,rgba(43,58,85,.16) 30px 31px),#fffdf6;border:1px solid var(--line);border-left:4px solid #2b3a55;padding:1.4rem 1.5rem 1.2rem;transform:rotate(-.5deg);box-shadow:0 12px 28px rgba(22,36,31,.12)}
.notebook h3{font-family:var(--mono);font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:#5c6b64;margin-bottom:1rem}
.notebook p{font-family:"Marck Script",cursive;font-size:1.42rem;line-height:31px;color:#2b3a55;max-width:58ch}
.notebook .sig{font-family:"Marck Script",cursive;font-size:1.3rem;color:#5c6b64;text-align:right;margin-top:.6rem}
/* кадры */
.shot{margin:1.4rem 0}
.shot img{display:block;width:100%;height:auto;border:1px solid var(--line);background:#fff;padding:.45rem;cursor:zoom-in}
.shot figcaption{color:var(--mut);font-size:.92rem;margin-top:.55rem;max-width:72ch}
.shot figcaption b{font-family:var(--mono);font-size:.72rem;color:var(--teal);letter-spacing:.08em;margin-right:.4rem}
.duo{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.2rem}
/* доска доказательств */
.fcol{background:#fff;border:1px solid var(--line);padding:1rem 1.1rem}
.fcol h3{font-family:var(--disp);text-transform:uppercase;letter-spacing:.08em;font-size:1.02rem;margin-bottom:.6rem}
.fcol ul{list-style:none;display:grid;gap:.5rem}
.fcol li{padding-left:1.3rem;position:relative;font-size:.96rem;color:#2c3a34}
.fcol.yes{border-top:3px solid var(--teal)} .fcol.yes h3{color:var(--teal)}
.fcol.yes li::before{content:"✓";position:absolute;left:0;color:var(--teal);font-family:var(--mono)}
.fcol.no{border-top:3px solid var(--alert)} .fcol.no h3{color:var(--alert)}
.fcol.no li::before{content:"—";position:absolute;left:0;color:var(--alert);font-family:var(--mono)}
.cols2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.2rem;margin:1.2rem 0}
.evtable{margin:1.2rem 0;background:#fff;border:1px solid var(--line);font-size:.92rem;width:100%;border-collapse:collapse}
.evtable th{font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);text-align:left;padding:.55rem .8rem;border-bottom:2px solid var(--ink)}
.evtable td{padding:.5rem .8rem;border-top:1px dashed var(--line);vertical-align:top}
.evtable .id{font-family:var(--mono);color:var(--teal);white-space:nowrap}
.st{font-family:var(--mono);font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;border-radius:3px;padding:.16rem .42rem;white-space:nowrap}
.st.v{color:var(--teal);border:1px solid rgba(14,122,99,.55);background:rgba(14,122,99,.07)}
.st.a{color:var(--amber);border:1px solid rgba(192,122,29,.55);background:rgba(192,122,29,.08)}
/* вердикт */
.verdictbox{margin:1.4rem 0;background:var(--ink);color:#e7efec;padding:1.3rem 1.4rem}
.verdictbox .vb{font-family:var(--mono);font-size:.68rem;letter-spacing:.24em;text-transform:uppercase;color:#7fd6bd}
.verdictbox .vs{font-family:var(--disp);font-weight:700;font-size:clamp(1.3rem,3vw,2rem);text-transform:uppercase;letter-spacing:.03em;margin:.5rem 0 .7rem}
.verdictbox p{color:#b9cdc5;font-size:.97rem;max-width:70ch}
/* подвал */
footer{margin-top:3rem;border-top:3px solid var(--ink);background:#fff;padding:1.5rem 0 2.1rem}
.frow{display:flex;flex-wrap:wrap;gap:.6rem 1.6rem;align-items:center;font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;color:var(--mut);text-transform:uppercase}
.pill{display:inline-flex;align-items:center;gap:.5rem;margin-top:1.15rem;font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;
  color:var(--teal);text-decoration:none;border:1px solid rgba(14,122,99,.5);border-radius:999px;padding:.62rem 1.2rem;
  background:rgba(14,122,99,.06);box-shadow:0 0 18px rgba(14,122,99,.28);transition:.2s}
.pill:hover{background:var(--teal);color:#fff;box-shadow:0 0 26px rgba(14,122,99,.45)}
/* лайтбокс */
.lb{position:fixed;inset:0;z-index:90;background:rgba(8,14,12,.94);display:none;align-items:center;justify-content:center;flex-direction:column;padding:2.4rem 1.2rem}
.lb.on{display:flex}
.lb img{max-width:min(1100px,94vw);max-height:78vh;border:1px solid rgba(238,244,242,.35);background:#fff;padding:.4rem}
.lb .lbcap{color:#e2ece8;font-size:.94rem;max-width:72ch;margin-top:.9rem;text-align:center}
.lb .lbx{position:absolute;top:1rem;right:1.2rem;cursor:pointer;background:transparent;border:1px solid rgba(238,244,242,.4);color:#e2ece8;
  font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.4rem .9rem}
.lb .lbnav{display:flex;gap:.7rem;margin-top:.9rem}
.lb .lbnav button{cursor:pointer;background:transparent;border:1px solid rgba(238,244,242,.4);color:#e2ece8;font-family:var(--mono);font-size:.72rem;border-radius:999px;padding:.42rem 1rem}
@media (max-width:720px){.dlg{grid-template-columns:1fr}.docrow{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
'''

BODY = '''<header class="mast">
  <div class="wrap">
    <div class="mastin">
      <span class="mastname">San Fierro News</span>
      <span class="mastsub">еженедельное расследование · дело №2</span>
      <span class="mastcase">МОН · октябрь 2026</span>
    </div>
    <div class="kchip">Поручение: Jonny Wilde · Расследование и кадры: Anna Village · Текст и редактор: Jonny Wilde</div>
  </div>
</header>

<section class="hero">
  <svg class="ecg" viewBox="0 0 1200 44" preserveAspectRatio="none" aria-hidden="true">
    <polyline points="0,26 180,26 200,26 214,8 228,38 242,26 520,26 540,26 554,4 568,40 582,26 900,26 916,26 930,10 944,36 958,26 1200,26"
      fill="none" stroke="#0e7a63" stroke-width="2"/>
  </svg>
  <div class="wrap">
    <div class="kick">Расследование под прикрытием · Министерство здравоохранения</div>
    <h1>За белым <em>халатом</em></h1>
    <p class="stand">Что происходит внутри Министерства здравоохранения, когда пациент не видит?
    Редакция не стала отвечать на слухи слухами: программный директор Anna Village по поручению генерального
    директора временно покинула редакцию, прошла собеседование в интернатуру МОН и отработала
    <b>две полные смены</b> изнутри. Этот выпуск - её отчёт, принятый редакцией 09.10.2026.</p>
    <div class="chips">
      <span class="chip"><b>2</b> полные смены под прикрытием</span>
      <span class="chip"><b>1</b> собеседование с главврачом</span>
      <span class="chip"><b>25</b> кадров в деле</span>
      <span class="chip"><b>29</b> позиций доказательной базы</span>
      <span class="chip">вердикт: <b>partially confirmed</b></span>
    </div>
    <div class="verdictplate">Editorial verdict · <b>partially confirmed</b></div>
  </div>
</section>

<nav class="snav" aria-label="Разделы дела">
  <div class="wrap"><div class="snavin">
    <button class="snavbtn" data-t="source">Источник</button>
    <button class="snavbtn" data-t="meeting">Летучка</button>
    <button class="snavbtn" data-t="order">Распоряжение</button>
    <button class="snavbtn" data-t="sobes">Собеседование</button>
    <button class="snavbtn" data-t="brief">Инструктаж</button>
    <button class="snavbtn" data-t="smeny">Две смены</button>
    <button class="snavbtn" data-t="lines">Три вопроса</button>
    <button class="snavbtn" data-t="evidence">Доказательства</button>
    <button class="snavbtn" data-t="turn">Поворот</button>
    <button class="snavbtn" data-t="itogi">Итоги</button>
    <button class="snavbtn" data-t="otchet">Отчёт и вердикт</button>
  </div></div>
</nav>

<section class="sec" data-sec="source">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 1 · источник</div><h2>Сообщение, с которого всё началось</h2></div>
    <div class="doccard">
      <span class="stamp">unverified</span>
      <h3>Source #001 · анонимное сообщение в редакцию</h3>
      <p class="txt">«Вы видите только момент, когда медик приезжает на вызов. Но никто не знает, что происходит до и после него».</p>
    </div>
    <p class="txt">Статус сообщения - UNVERIFIED INFORMATION: полученная информация не является доказательством.
    Редакция принимает решение проверить её самостоятельно - изнутри Министерства, глазами собственного сотрудника.</p>
  </div>
</section>

<section class="sec" data-sec="meeting">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 2 · editoral meeting</div><h2>Разговор в кабинете генерального</h2></div>
    <p class="lead">RP-сцена передачи задания - дословно по записи разговора в редакции.</p>
    <div class="dlgbox">
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Присядь. Есть материал, который требует проверки.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Что произошло?') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='В редакцию поступило несколько сообщений о работе Министерства здравоохранения. Некоторые говорят о проблемах внутри организации.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Есть подтверждения?') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Нет. Пока только сообщения.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Тогда предлагаю проверить всё изнутри.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Именно поэтому я вызвал тебя.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Что от меня требуется?') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Временно покинуть редакцию, устроиться в Министерство и посмотреть на их работу изнутри.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='А если информация окажется ложной?') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Тогда именно это и будет результатом нашего расследования. Мы не ищем виновного. Мы ищем правду.') + '''
    </div>
    <div class="duo">''' + fig('v1', 'EV-01') + fig('v2', 'EV-02') + '''</div>
    ''' + fig('v3', 'EV-03') + '''
  </div>
</section>

<section class="sec" data-sec="order">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 3 · internal document</div><h2>Распоряжение о временном увольнении</h2></div>
    <div class="doccard">
      <span class="stamp">approved</span>
      <h3>Распоряжение № 024/26</h3>
      <div class="docrow"><b>Сотрудник</b><span>Anna Village</span></div>
      <div class="docrow"><b>Должность</b><span>Программный директор редакции San Fierro News</span></div>
      <div class="docrow"><b>Причина</b><span>Проведение журналистского расследования по системе «Журналист под прикрытием»</span></div>
      <div class="docrow"><b>Статус</b><span>Временно освобождена от должности с восстановлением по возвращении</span></div>
      <div class="docrow"><b>Ответственный</b><span>Jonny Wilde, генеральный директор</span></div>
    </div>
    <p class="txt">По памятке редакции расследования под прикрытием право выдавать задание, увольнять и восстанавливать
    сотрудника принадлежит только лидеру редакции; данные об уходе и возвращении фиксируются в реестре. Обе отметки в реестре стоят.</p>
  </div>
</section>

<section class="sec" data-sec="sobes">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 4 · day 01 · собеседование в интернатуру МОН</div><h2>Главврач Lisa Akana задаёт вопросы</h2></div>
    <p class="lead">Собеседование в интернатуру Министерства проводила Lisa Akana, главный врач больницы Los Santos. Редакция восстанавливает разговор дословно - по строкам, оставшимся над головами в кадрах дела.</p>
    <div class="dlgbox">
      ''' + DLG.format(CLS='av', WHO='Anna Village', TXT='Вот папка со всеми документами.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Добрый день, присаживайтесь.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Можете рассказать немного о своем образовании и опыте работы в области медицины?') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village', TXT='Работала медсестрой в армии города Сан Фиерро.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village', TXT='Мой опыт службы медсестрой в армии научил меня справляться со всеми стрессовыми ситуациями.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Отлично! У вас есть вопросы к нам?') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village', TXT='На данном этапе у меня больше нет вопросов.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village', TXT='*взяла анкету*') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Сначала вот Ваш бейджик N13. Носите его гордо, не забывайте и не теряйте!') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Можете приступать к работе!') + '''
    </div>
    <div class="duo">''' + fig('s4', 'EV-04') + fig('s13', 'EV-05') + '''</div>
    <div class="duo">''' + fig('s25', 'EV-06') + fig('s31', 'EV-07') + '''</div>
    <p class="txt">Бейджик N13 - первый предмет Министерства, который Анна получила на руки: с него начинается
    любая смена интерна и им же заканчивается любой отчёт.</p>
  </div>
</section>

<section class="sec" data-sec="brief">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 4 · инструктаж</div><h2>Что главврач велела запомнить</h2></div>
    <p class="lead">После собеседования Lisa Akana провела инструктаж: форма, телефон, коллектив и четыре пункта обязанностей. Ниже - выписка из журнала смены МОН, строка в строку, как её ведёт дежурный.</p>
    <div class="logbox">
      <div class="note">Журнал смены МОН · выписка дежурного · ночь поступления интерна</div>
      <div><span class="t">[02:54:27]</span> <span class="n">Lisa Akana [612]</span> передала форму и сделала инструктаж сотрудника МОН</div>
      <div><span class="t">[02:54:33]</span> <span class="n">Lisa Akana [612]</span>: передала фонендоскоп Anna Village [469]</div>
      <div><span class="t">[02:54:38]</span> <span class="n">Lisa Akana [612]</span>: Итак, добро пожаловать в коллектив нашей больницы.</div>
      <div><span class="t">[02:54:46]</span> <span class="n">Lisa Akana [612]</span>: Я Глав Врач Lisa Akana и сейчас расскажу Вам про основные моменты, которые стоит запомнить.</div>
      <div><span class="t">[02:54:49]</span> <span class="n">Michael Goldfather [707]</span>: Удостоверение.</div>
      <div><span class="t">[02:54:52]</span> <span class="n">Lisa Akana [612]</span>: Сначала вот Ваш бейджик N13. Носите его гордо, не забывайте и не теряйте!</div>
      <div><span class="t">[02:54:59]</span> <span class="n">Lisa Akana [612]</span>: передала бейджик</div>
    </div>
    <div class="dlgbox">
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Рабочий график: 9:00-21:00 по будням и 10:00-20:00 по выходным.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Первое: лечение. Лечение производится в больнице или в карете скорой помощи.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Второе: фонендоскоп. Носите его с собой и слушайте пациента им - до приезда кареты он Ваш главный инструмент.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Третье: развозка медикаментов. Это одна из самых важных обязанностей в МОН!') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='В кабинете главного врача Вы сможете найти статистику по состоянию складов.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Четвёртое: эвакуация трупов в морг.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Патрулировать и занимать посты можно в любом городе, главное об этом докладывать.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Докладывать нужно по специальной рации.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Это всё регламентируется уставом, который Вы всегда можете найти на сайте МОН.') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='Наш устав я Вам настоятельно рекомендую внимательно прочесть и запомнить!') + '''
      ''' + DLG.format(CLS='la', WHO='Lisa Akana · главврач', TXT='В заключение хочу добавить, что Вас могут грабить или просить о помощи байкеры.') + '''
    </div>
    <div class="duo">''' + fig('s37', 'EV-08') + fig('s49', 'EV-09') + '''</div>
    <div class="duo">''' + fig('s53', 'EV-10') + fig('s1', 'EV-11') + '''</div>
    <p class="txt">Все четыре пункта обязанностей попали в запись целиком: редакция приводит их в том порядке,
    в котором главврач называла их интерну, - лечение, фонендоскоп, развозка медикаментов, эвакуация в морг.</p>
  </div>
</section>

<section class="sec" data-sec="smeny">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этапы 5-6 · две полные рабочие смены</div><h2>Полевой дневник интерна</h2></div>
    <p class="lead">Две смены Анны уложились в одну простую формулу: работа начинается задолго до первого вызова и заканчивается далеко не с последним.</p>
    <p class="txt"><b>Смена первая.</b> Раздевалка, гражданская одежда на скамейке; палата и обход с коллегой Sonya Sweazy;
    выход скорой со двора больницы; полевой вызов на закате - двое на земле под деревом, аптечка между ними;
    возвращение в сумерках; и комната отдыха, где пациент лежит на диване, потому что в палатах мест не было.</p>
    <div class="duo">''' + fig('d1', 'EV-12') + fig('d2', 'EV-13') + '''</div>
    <div class="duo">''' + fig('d4', 'EV-14') + fig('d8', 'EV-15') + '''</div>
    <div class="duo">''' + fig('d12', 'EV-16') + fig('d14', 'EV-17') + '''</div>
    ''' + fig('d19', 'EV-18') + '''
    <p class="txt"><b>Вызов, которого не было в плане смены.</b> Комната отдыха, вторая смена: на диване - губернатор
    штата Carl Village, которому стало плохо на рабочем визите; его сотрудник Vanya Rodnik вызвал помощь и держал
    шляпу в руках, пока считал секунды. Вызов приняла интерн Анна - и узнала мужа раньше, чем дочитала карточку вызова.
    Искусственное дыхание на диване комнаты отдыха, счёт компрессий вслух, вторая медсестра на подхвате: приступ
    отступил до прихода скорой. В журнале МОН этот вызов значится строкой «пациент стабилизирован на месте»;
    в блокноте Анны он значится иначе - блокнот редакция откроет в финале.</p>
    <p class="txt"><b>Смена вторая.</b> Та же раздевалка и тот же синий ключ формы; вызов в пустыне, где скорая стоит
    на песке, а пациент лежит на открытом солнце; погрузка в машину №42 вручную - с земли на носилки; ночная парковка,
    где скорые смены выстраиваются в ряд; и наконец дом - кадр, с которого начинается этот отчёт.</p>
    <div class="duo">''' + fig('d24', 'EV-19') + fig('d32', 'EV-20') + '''</div>
    <div class="duo">''' + fig('d34', 'EV-21') + fig('d35', 'EV-22') + '''</div>
    ''' + fig('d28', 'EV-23') + '''
    <div class="notebook">
      <h3>Блокнот Анны · запись после двух смен</h3>
      <p>В этом блокноте две смены. Первая - от раздевалки до закатного вызова. Вторая - от комнаты отдыха до ночного ряда скорых.</p>
      <p>Бейджик N13 тяжелее, чем кажется: он всё время напоминает, что я здесь не совсем я.</p>
      <p>На диване комнаты отдыха лежал человек, которого я знаю лучше всех на свете. Я не имела права узнавать его - только считать компрессии.</p>
      <p>Он выжил. И я не стала ему женой на глазах всего Министерства: сначала компрессии, потом всё остальное. Наверное, это и значит - дежурить.</p>
      <p>Министерство не такое, каким его рисуют сообщения. Оно усталое. Оно держится на людях, которые считают компрессии вслух и носят бейджик гордо.</p>
      <p>Завтра я вернусь в редакцию и отдам отчёт. А эту страницу оставлю себе: пусть напоминает, зачем я туда шла.</p>
      <p class="sig">Анна Village, интерн бейджика N13</p>
    </div>
  </div>
</section>

<section class="sec" data-sec="lines">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 6 · три линии расследования</div><h2>Тяжесть, граждане, закулисье</h2></div>
    <p class="txt"><b>01. Насколько тяжела работа медика?</b> Тяжесть измеряется не отчётом, а руками. На закате - двое
    на земле под деревом и аптечка между ними, и у интерна есть минуты, а не часы. Ночью - пустыня, где скорая стоит
    на песке, а пациент лежит на открытом солнце, и носилки приходится нести вручную, потому что второй бригады рядом
    нет. Под утро - ряд скорых у больницы, который никто не называет подвигом: это просто конец смены. В блокноте Анна
    оставила строку, которой редакция верит больше всех цифр: усталость здесь - не причина уйти, а воздух профессии.</p>
    <p class="txt"><b>02. Как медики взаимодействуют с гражданами?</b> История двух смен рассказывает не о конфликте,
    а о доверии: пациенты на койках и диванах позволяют интерну прикасаться к себе - в больнице это и есть мера доверия.
    Самая острая сцена случилась не с чужими людьми: в комнате отдыха губернатору штата стало плохо на рабочем визите,
    и вызов приняла его жена в форме интерна. Она не стала женой на глазах Министерства - она начала компрессии,
    и граждане в те минуты видели не семью, а медика. Пожалуй, это и есть самый честный ответ на вопрос о взаимодействии:
    белый халат на время отменяет родство, чтобы спасти родного.</p>
    <p class="txt"><b>03. Что остаётся за кадром?</b> За кадром остаётся всё, на чём кадр держится: инструктаж, где
    главврач перечисляет четыре обязанности, как четыре опоры, - лечение, фонендоскоп, развозка медикаментов, эвакуация
    в морг; устав, который «надо прочесть и запомнить»; бейджик N13, который нельзя потерять; рация, по которой положено
    докладывать о любом посте; и предупреждение о байкерах, которые могут ограбить или попросить помощи - сразу оба.
    Пациент видит лишь момент, когда скорая подъезжает. Всё перечисленное - это то, что происходит до и после этого
    момента: ровно то, о чём писал SOURCE #001, и ровно то, чего не видит город.</p>
  </div>
</section>

<section class="sec" data-sec="evidence">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 7 · evidence board</div><h2>Доказательная база дела</h2></div>
    <table class="evtable">
      <tr><th>ID</th><th>Материал</th><th>Тип</th><th>Статус</th></tr>
      <tr><td class="id">EV-01…03</td><td>Передача задания в кабинете генерального: три кадра сцены</td><td>Фото</td><td><span class="st v">verified</span></td></tr>
      <tr><td class="id">EV-04…11</td><td>Собеседование в интернатуру МОН и инструктаж: восемь кадров, транскрипт дословно</td><td>Фото + транскрипт</td><td><span class="st v">verified</span></td></tr>
      <tr><td class="id">EV-12…23</td><td>Две полные смены: двенадцать кадров от раздевалки до ночной парковки</td><td>Фото</td><td><span class="st v">verified</span></td></tr>
      <tr><td class="id">EV-24</td><td>Журнал смены МОН, выписка дежурного 02:54:27-02:54:59: форма, фонендоскоп, бейджик N13, коллектив</td><td>Документ</td><td><span class="st v">verified</span></td></tr>
      <tr><td class="id">EV-25</td><td>Распоряжение № 024/26 о временном увольнении из редакции</td><td>Документ</td><td><span class="st v">approved</span></td></tr>
      <tr><td class="id">EV-26</td><td>Блокнот Анны: запись после второй смены, рукописью</td><td>Документ</td><td><span class="st v">verified</span></td></tr>
      <tr><td class="id">EV-27…28</td><td>Возвращение в редакцию: два кадра сцены приёма отчёта</td><td>Фото</td><td><span class="st v">verified</span></td></tr>
      <tr><td class="id">EV-29</td><td>Диалог приёма отчёта: генеральный директор и программный директор, дословно</td><td>Запись</td><td><span class="st v">verified</span></td></tr>
    </table>
    <p class="txt">Ни одна позиция не добавлена в доску заранее: всё, что стоит в таблице, лежит в папке дела
    и подшито в этот выпуск кадрами или строками записи.</p>
  </div>
</section>

<section class="sec" data-sec="turn">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 9 · поворот</div><h2>Гипотеза сменилась по дороге</h2></div>
    <p class="lead">Редакция уходила в Министерство с подозрением: «внутри есть проблемы, о которых не говорят». Две смены спустя подозрение сменилось пониманием: проблемы есть, но их природа другая.</p>
    <p class="txt">Первоначальные сообщения рисовали Министерство закрытой организацией с внутренними проблемами.
    Факты двух смен показали другое: организация открыта до регламента - устав, бейджик, рация, четыре пункта
    обязанностей, график 9:00-21:00. Проблемы, которые увидела интерн Анна, - не отношение сотрудников к людям,
    а нагрузка и невидимость их труда: пациент видит момент приезда скорой и не видит ни обхода, ни инструкции,
    ни ночи на парковке.</p>
    <p class="txt">Так расследование из разоблачительного стало документальным: мы не нашли виновных - мы нашли работу,
    которую не замечают.</p>
  </div>
</section>

<section class="sec" data-sec="itogi">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 10 · итоги</div><h2>Что показало расследование</h2></div>
    <p class="lead">Сопоставляем первоначальные сообщения с тем, что дали две смены, собеседование и журналы. Каждая строка ниже опирается на позицию доказательной базы.</p>
    <div class="cols2">
      <div class="fcol yes">
        <h3>Подтвердилось</h3>
        <ul>
          <li>Работа медика тяжела физически: ночные и пустынные вызовы, погрузка на носилки вручную, ночной ряд скорых у больницы (EV-12…23).</li>
          <li>У вызова есть невидимая для пациента часть: обход, инструктаж, устав, бейджик, рация, четыре пункта обязанностей (EV-24, EV-04…11).</li>
          <li>Вход в Министерство открыт и регламентирован: собеседование у главврача, анкета, бейджик N13, распоряжение редакции (EV-04…11, EV-25).</li>
          <li>Помощь приходит даже туда, где её не ждут: вызов к губернатору принят и отработан на месте, пациент спасён (EV-17, EV-18).</li>
        </ul>
      </div>
      <div class="fcol no">
        <h3>Не подтвердилось</h3>
        <ul>
          <li>«Министерство закрыто и живёт своими проблемами»: устав лежит на сайте МОН, график и обязанности названы интерну в первый же час (EV-24).</li>
          <li>Конфликты сотрудников с гражданами: за две смены - ни одной конфликтной сцены в кадрах (EV-12…23).</li>
          <li>«Медики - только экстренная служба»: кадры показывают обратное - обход, палаты, комната отдыха, развозка медикаментов как обязанность (EV-12…23, EV-24).</li>
          <li>Виновные в «проблемах внутри организации»: ни один кадр и ни одна строка записи не называют виновного, потому что его нет (EV-01…29).</li>
        </ul>
      </div>
    </div>
    <p class="txt"><b>Позиция редакции.</b> Министерству здравоохранения мы рекомендуем одно: рассказать гражданам о своей
    невидимой работе самим - до того, как это придётся делать газете. Редакция рекомендует продолжить наблюдение:
    две смены дают картину входа, но не картину сезона; следующий материал дела - осенние вызовы и развозка медикаментов,
    о которой главврач говорила как о самой важной обязанности.</p>
    <p class="txt"><b>Границы итогов.</b> Всё вышеперечисленное установлено кадрами и записями этого дела. То, что не попало
    в две смены интерна, в итоги не вошло: редакция не расширяет находки за пределы доказательной базы.</p>
  </div>
</section>

<section class="sec" data-sec="otchet">
  <div class="wrap">
    <div class="sechead"><div class="kick">Этап 11 · приём отчёта</div><h2>Разговор, которым дело вернулось в редакцию</h2></div>
    <p class="lead">Два кадра возвращения: папка с материалами ложится на стол генерального - и диалог приёма отчёта, дословно по записи разговора в редакции.</p>
    <div class="duo">''' + fig('r27', 'EV-27') + fig('r28', 'EV-28') + '''</div>
    <div class="dlgbox">
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Здравствуйте. Можно войти?') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Конечно, Анна. Заходи. Как прошло расследование?') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Расследование завершено. Я собрала все материалы и подготовила отчёт.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Хорошо. Мне интересно услышать твои выводы.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Я провела несколько дней внутри Министерства здравоохранения. За это время удалось изучить их рабочий процесс изнутри.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Что-нибудь подтвердилось из первоначальных сообщений?') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Не всё. Некоторые сведения оказались преувеличены. Но я обнаружила несколько моментов, которые заслуживают внимания.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Доказательства есть?') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Да. Я подготовила фотографии, записи и результаты интервью. Всё распределено по датам и отдельным эпизодам.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Отлично. А что с финальной статьёй?') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Основной текст уже готов. Осталось только проверить факты и привести материалы в порядок.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Хорошая работа. Передавай отчёт.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Вот, пожалуйста. Здесь все материалы расследования.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Принял. Теперь редакция проведёт финальную проверку. После этого решим вопрос с публикацией.') + '''
      ''' + DLG.format(CLS='av', WHO='Anna Village · программный директор', TXT='Поняла. Спасибо за доверие.') + '''
      ''' + DLG.format(CLS='jd', WHO='Jonny Wilde · генеральный директор', TXT='Это тебе спасибо. Хорошая журналистика начинается с фактов.') + '''
    </div>
    <div class="verdictbox">
      <div class="vb">Editorial verdict</div>
      <div class="vs">Partially confirmed</div>
      <p>Расследование завершено. Мы начали с вопроса, что происходит за закрытыми дверями Министерства здравоохранения,
      и ответ оказался сложнее первоначальных слухов: часть сообщений не подтвердилась, но подтвердилось главное -
      за каждым вызовом стоит работа, которую пациент не видит. Подготовка, обход, инструкция, бейджик N13, рация,
      носилки вручную и ночная парковка скорых - вот что находится за белым халатом. Редакция восстановила Анну Village
      в должности программного директора и рекомендует Министерству одно: рассказать гражданам о своей невидимой
      работе самим - пока это не сделали за них.</p>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="frow"><span>Поручение: Jonny Wilde</span><span>Расследование и кадры: Anna Village</span><span>Текст и редактор: Jonny Wilde</span></div>
    <div class="frow"><span>дизайн и вёрстка - редакция San Fierro News</span><span>дело №2 · октябрь 2026</span></div>
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
<title>San Fierro News — За белым халатом: расследование №2 внутри Министерства здравоохранения</title>
<meta name="description" content="Еженедельное расследование San Fierro News, дело №2: программный директор Anna Village под прикрытием проходит собеседование в интернатуру МОН у главврача Lisa Akana и отрабатывает две полные смены - от раздевалки и обхода до ночного вызова в пустыне. Вердикт: partially confirmed.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans+Condensed:wght@500;600;700&family=Bitter:ital,wght@0,400;0,600;1,400&family=Fira+Mono:wght@400;500&family=Marck+Script&display=swap" rel="stylesheet">
<style>
''' + CSS + '''</style>
</head>
<body>
''' + BODY + '''
<script>''' + JS + '''</script>
<!-- SFN · 2026 · 037 · white-coat-days -->
</body>
</html>
'''

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('written', OUT, len(html.encode('utf-8')) // 1024, 'KB')
