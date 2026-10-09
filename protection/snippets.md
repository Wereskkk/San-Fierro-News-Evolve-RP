# SFN · Сниппеты защиты: куда и что вставлять

## 1. Копирайт-комментарий (в `<head>`, первой строкой после `<head>`)
Вставляется ОДИН РАЗ в каждый `template_*.html` и в `template_newsroom.html` —
дальше попадает во все будущие выпуски автоматически через сборщик.

```html
<!-- © 2026 San Fierro News / Jonny Wilde. Дизайн и вёрстка защищены: CC BY-NC-ND 4.0. Копирование и переработка запрещены. -->
```

Массовая вставка (запустить из корня репозитория):
```bash
python3 - <<'PY'
import glob,re
LINE='<head>\n<!-- © 2026 San Fierro News / Jonny Wilde. Дизайн и вёрстка защищены: CC BY-NC-ND 4.0. Копирование и переработка запрещены. -->'
for f in glob.glob('template_*.html'):
    s=open(f,encoding='utf-8').read()
    if 'CC BY-NC-ND' in s: continue
    s=s.replace('<head>',LINE,1)
    open(f,'w',encoding='utf-8').write(s)
    print('stamped',f)
PY
```

## 2. CSS-штамп выпуска (у каждого номера свой)
Ставится в собранный выпуск первой строкой внутри `<style>`, сразу после блока `@font-face`:

```css
/* SFN-DESIGN-028: roulette-noir-lv · 02.10.2026 */
```

В сборщике (`worktmp/build_*.py`) — токен `@@STAMP@@`, значение берём из сид-таблицы ниже.
Формат: `SFN-DESIGN-<NNN>: <slug> · <DD.MM.YYYY>`, NNN — трёхзначный номер из таблицы.

## 3. Невидимый маркер в теле (перед `</body>`)
```html
<!-- SFN · 2026 · 028 · roulette-noir-lv -->
```
Читатель не видит; копировщик, тянущий страницу целиком, уносит с собой.

## 4. Видимая строка в подвал (внутриигровой тон, без юридического жаргона)
Третьей строкой в `<footer>` каждого шаблона:
```html
дизайн и вёрстка — редакция San Fierro News
```
(в `template_lv_daily.html` это строка после `выпуск подшит в архив навсегда · 02.10.2026`).
RP-чистота соблюдена: никаких «лицензия/CC/copyright» в видимом тексте.

## 5. Сид-таблица номеров штампов (hub-порядок = порядок нумерации)
| NNN | файл | slug |
|---|---|---|
| 001 | index.html | chinatown-casino |
| 002 | driving-school.html | driving-school |
| 003 | caligulas-casino.html | caligula-neon |
| 004 | all-saints-hospital.html | all-saints |
| 005 | sf-police-raid.html | sf-raid |
| 006 | sf-army-base.html | sf-army |
| 007 | sfpd-precinct.html | sfpd-precinct |
| 008 | sfpd-patrol-falk.html | patrol-falk |
| 009 | daily-24-09-2026.html | mourning-editor |
| 010 | opg-leader-interview.html | padre-interview |
| 011 | wedding-ozzy-gulnara.html | wedding-malibu |
| 012 | zone51-investigation.html | zone51 |
| 013 | daily-26-09-2026.html | daily26 |
| 014 | daily-27-09-2026.html | daily27 |
| 015 | daily-28-09-2026.html | daily28 |
| 016 | fotoreport-comedy-club.html | comedy-club |
| 017 | fotoreport-tierra-robada.html | tierra-robada |
| 018 | fotoreport-warlocks-mc.html | warlocks-mc |
| 019 | fotoreport-avtobazar-lv.html | avtobazar-lv |
| 020 | fotoreport-city-hall.html | city-hall |
| 021 | fotoreport-four-dragons.html | four-dragons |
| 022 | fotoreport-evolve-hotel.html | five-stars-hotel |
| 023 | fotoreport-abandoned-airport.html | abandoned-airport |
| 024 | daily-30-09-2026.html | daily30-sf |
| 025 | article-lisa-akana.html | lisa-akana |
| 026 | daily-30-09-2026-los-santos.html | ls-postcards |
| 027 | socio-governor-poll.html | governor-poll |
| 028 | daily-02-10-2026-las-venturas.html | roulette-noir-lv |
| 029 | daily-03-10-2026.html | day-grid-tight |
| 030 | investigation-falk.html | falk-dossier |
| 031 | article-confession-gulnara.html | hotdog-confession |
| 032 | efir-rules.html | efir-rules |
| 033 | tour-seven-places.html | state-tour-seven |
| 034 | socio-best-newsroom-poll.html | tally-station |
| 035 | daily-07-10-2026.html | ten-silent-addresses |
| 036 | daily-08-10-2026.html | one-pursuit-route |
| 037 | investigation-whitecoat.html | white-coat-days |
| 035 | (следующий выпуск) | … |

Примечание форензики: номер 029 первоначально собран со слагом `state-broadsheet`;
после редизайна по брифу главреда (03.10.2026, пересборщик `worktmp/build_daily_0310_state_v2.py`)
слаг стал `classic-broadsheet`; после второго редизайна того же дня (пересборщик
`worktmp/build_daily_0310_state_v3.py` — интерактивная газета из 7 полос с перелистыванием)
действующий слаг — `interactive-pages`; после третьего редизайна того же дня (пересборщик
`worktmp/build_daily_0310_state_v4.py` — компактная газета из 4 полос, тексты −70…74% при сохранении
информации и подписей) действующий слаг — `compact-edition`; после четвёртого редизайна того же дня (пересборщик
`worktmp/build_daily_0310_state_v5.py` — вертикальная веб-газета без перелистывания, концепция
«городская документация Сан-Фиерро») действующий слаг — `street-folio`; после пятого редизайна того же дня (пересборщик
`worktmp/build_daily_0310_state_v6.py` — плакатная редакционная эстетика: цветовые поля, крупная
типографика Bebas Neue, номера материалов как графика) действующий слаг — `harbor-poster`; после композиционной правки 04.10.2026 (пересборщик
`worktmp/build_daily_0310_state_v7.py` — графитовый фон сайта, листы с границей и тенью, КПП как
боковой материал с цветной полосой, асимметричные сетки полос) действующий слаг — `graphite-press`; после арт-директорской правки 04.10.2026 (пересборщик
`worktmp/build_daily_0310_state_v8.py` — оболочка возвращена к v6, у каждого материала собственная
композиция, КПП как газетная колонка с колонными линейками) действующий слаг — `artdesk`; после конкурсной композиционной правки 04.10.2026 (пересборщик
`worktmp/build_daily_0310_state_v9.py` — full-bleed фото, якоря-номера у своих материалов, диптих-контраст,
плакатный вынос дословной фразы, ступенчатые лок-апы) действующий слаг — `prize-desk`.
Прежние имена жили до 03.10.2026.

Примечание по делу №1 (04.10.2026, ветка `investigation-falk-draft`): черновой тираж `investigation-falk.html` был собран со штампом `SFN-DESIGN-029: falk-two-lives`, но номер 029 уже занят `daily-03-10-2026.html` — коллизия закрыта при переработке дела по методике расследования: действующий штамп `SFN-DESIGN-030: falk-dossier`, маркер `<!-- SFN · 2026 · 030 · falk-dossier -->`. Имя `falk-two-lives` жило до 04.10.2026.

Еженедельники нумеруемся отдельно: `SFN-WEEKLY-001` и т.д. (у них свой характер и свой шаблон).

## 6. Реестр сигнатурных имён (форензика переживает рефакторы)
Считаем отпечатками редакции (если встречаются чужой странице — это копипаста, а не «похожий стиль»):
`.marquee/.bulb`, `.signbase/.sl/.signpole`, `.jackpot/.jplab/.jpdate`, `.pcard/.corner/.crank/.csuit`,
`.standfirst`, `.plateline/.plate/.mapplate`, `.pullq`, `.chips/.tok/.tokw`, `.chron-grid/.chron-item`,
`.logbook/.logrow`, `.hubbtn`, `.tape/.tnum/.t-red/.t-blk/.t-zero`, `.mapframe/.pin/.pinprev/.pvplate`,
`.lvlegend`, `.tomap/.tomapline`, `.wxcard/.hocard/.wxbin/.hobin/.ho-min/.wx-min`, `.hostars/.hoday`,
`.sidestrip`, `.fin ttl/.fintext` (класс `.finttl`), `.factrow/.fact`, `.divider`, `.secno/.rubric/.rule`.
Дело №1 `investigation-falk.html` (04.10.2026, штампы 029 `falk-two-lives` → 030 `falk-dossier`): `.splitwrap/.split/.pane/.splithandle/.handle/.splitrange`, `.mosaic/.mshot`, `.evgrid/.ev/.evbtn/.evimg/.evnum/.evcap/.evsrc`, `.route/.rnode/.rbtn/.rshot/.rlbl/.rtxt/.rmark`, `.factgrid/.fcol/.knum`, `.tgbtns/.tgbtn/.tgpanel/.tgnote`, `.qwall/.qnum/.qtxt`, `.finalshot/.fimg/.fcap/.watch/.openend`, `.tlgrid/.tlside/.tlline/.tlfill/.tlpct/.stage/.stnum/.stthumbs/.th`, `.refcard/.rlabel`, `.mailwrap/.mail/.mailbar/.mailhead/.mrow/.mailsubj/.mailbody/.mailsign/.attach/.atch/.stampmark/.threadbtn/.msg2/.sidecard/.sclbl/.sidenote`, `.triggrid/.trig/.tn/.tpill/.trigshot`, `.steps/.step/.sn/.sstat/.spill/.swhen/.stdbox/.stlbl/.stdlist`, `.spheregrid/.scard/.sch/.snum/.smeta/.idbadge/.btop/.bname/.brole/.bcode/.bnum/.rules/.rlbl`, `.fldhead/.fldrow/.flddate/.fldplace/.fldwhat/.fldres/.fldnote/.nb/.nl`, `.reghead/.regrow/.regnum/.regthumb/.regobj/.regtxt/.regline/.rpill/.regsum/.rsum/.rn/.rl`, `.ivtabs/.ivtab/.ivpanel/.ivmeta/.ivq/.ivpull`, `.exitgrid/.exdoc/.dlbl/.dtext/.dsign/.dlg/.dwhen/.dlgline/.exstamp/.sttxt`, `.fstep`.
Юмористическая колонка `article-confession-gulnara.html` (04.10.2026, штамп 031 `hotdog-confession`): `.gate/.gbox/.gage/.gbtn/.gbtn.no/.gfine`, `.pol/.pols/.pcap/.pimg`, `.leadshot/.ls/.cap`, `.letter/.llbl/.lstamp`, `.hand`, `.hdwrap/.hdsvg/.rate/.rrow/.rnum/.rname/.rbar/.bar/.rv`, `.ednote/.en`, `.disclaim/.agepill/.dlbl`, `.strip/.st`, `.pull/.who`, `.cols`, `.secpad/.dark/.pinksec`, `.mast/.mastlogo/.mastmeta`, `.hero/.heroin/.kick/.heroline/.standfirst/.chips/.chip/.herobtns/.btn`, `.topnav/.topnavin/.navbtn`, Хаб-редизайн 04.10.2026 (`newsroom.html`, штамп остаётся `SFN-DESIGN-HUB`, слаг `newsroom-face`): `.tkin/.tk`, `.livebox/.lb-top/.onair/.clock`, `.wxgrid/.wxcity/.wxmain/.wxtemp/.wxcond/.wxicons/.wxrow/.wxhours/.wxh/.wxdays/.wxd/.wxstamp`, `.ic/.sun/.rays/.cl/.drop/.bolt/.fog/.flake`, `.hzwrap/.hzring/.hzsigns/.hzbtn/.hzstars/.hzcard/.hznums/.hznum`, `.teamgrid/.teamtext/.vacs/.vac/.vtags/.vtag/.steps3/.st3`, `.ruletabs/.rtab/.rpanel/.rgroup/.exline/.replfilter/.repl/.arw`, `.qzbox/.qztop/.qzprog/.qzscore/.qzq/.qzopts/.qzopt/.qzfb/.qznext/.qzres/.qzmiss`; страница `efir-rules.html` (032): `.studio/.stin/.onair/.vu/.freq/.needle`, `.list`, `.cards3/.tcard`, `.grid3/.box.ok/.warn/.no`, `.dials/.dial`, `.steps4/.st4`, Тур недели `tour-seven-places.html` (05.10.2026, штамп 033 `state-tour-seven`): плашки героя `.chips/.chip` и колонка подвала «Как устроен тур» жили до 07.10.2026 - сняты по команде гендиректора «всё что я отправил, удалить» (классы `.chips/.chip` продолжают жить в колонке 031), строка «Мир рассказа…» из выходных данных тура снята тогда же (в деле №1 и колонке живёт своя редакция строки - не тронута): `.mapbox/.leg/.pin/.halo/#car/.maplegend/.mapbtns`, `.drivebar/.drivetxt/.drivesub`, `.carrot`, `.stopnav/.btn.back`, `.stop/.stophead/.snum/.scity/.slead/.big/.bimg/.thumbs/.th`, `.voice/.vbtn/.vwave/.vtxt`, `.flat/.flatbox/.fw`, `.routesec/.rrow/.rn/.rt/.rc/.rb/.mini` (кнопки `.rb/.mini` в списке маршрута сняты 05.10.2026 по правке гендиректора «только Поехали/Назад» - классы в CSS живут), `.view/.on`. `.script/.scriptgrid`, `.topics/.tlist`. `.lb/.lbctl/.lbx/.lbnav/.lbnum/.lbcnt`, `.clothesline/.rope`, `.angels/.cupid/.c1-.c8/.w` (ангелочки `.angel/.a1-.a4` жили до 04.10.2026 - заменены купидонами по правке гендиректора) (имена живут с 04.10.2026; стопки `.pols` жили до 04.10.2026 - заменены верёвками с прищепками по правке гендиректора «полароиды в один столбик»). SVG-иллюстрация хот-дога `.hdsvg` заменена архивным кадром по правке гендиректора 04.10.2026 — имя жило до этой правки, класс в CSS оставлен.
Спецвыпуск-социсследование `socio-best-newsroom-poll.html` (07.10.2026, штамп 034 `tally-station`, очередь `anna-malboro/`): `.tallybar/.tbin/.tblive`, `.snav/.snavin/.snavbtn`, `.kicker/.herolead/.hl`, `.statgrid/.stattile`, `.stsec/.sthead/.stnum/.hrule`, `.phead/.prow/.plabel/.pval/.mrow/.mlabel/.mval/.mlist`, `.figure/.figcap/.tblnote`, `.lane/.lanelbl/.lanetrack/.lanefill/.votecell/.lanenum`, `.tbl/.tname/.dot/.sumrow`, `.dgrid/.donutbox/.donut/.dcenter/.dcnum/.dclbl/.dleg/.dlrow/.dlsw/.dlname/.dlnum`, `.ribbon/.rbseg/.rblegs/.rbleg`, `.ancard/.anleft/.anpct/.ansub`, `.flipnote/.fnbtn/.fnpanel`, `.ptgrid/.ptcard/.pttop/.ptpct/.ptsub/.ptq/.ptwho`, `.btabs/.btab/.bcount/.ballots/.ballot/.bperf/.bhead/.bnum/.gchip/.bstamp/.bname/.bopts/.opt/.box/.bquote`, `.verdict/.vnum/.vtext`, `.ednote/.ent`, `.mline`, `.recgrid/.reccard/.rto`, `.signrow/.signlbl/.signname/.signscript`, `.colophon/.backpill/.copyline`, `.num[data-to]/.reveal/.noanim`; состояния `.on/.hot/.cur/.open/.chosen/.hide` и варианты `.mini/.mid/.hatch` (имена живут с 07.10.2026; `.lead/.panel/.mono` совпадают по именам с прежними выпусками, но живут в CSS своего файла независимо).
Ежедневная газета `daily-07-10-2026.html` (07.10.2026, штамп 035 `ten-silent-addresses`, очередь `anna-malboro/`): `.mast/.mastin/.mastname/.mastsub/.mastdate/.kchip`, `.hero/.kick/.stand/.tiles/.tile`, `.snav/.snavin/.snavbtn`, `.sec/.sechead/.lead/.txt/.pull/.who`, `.shot/.duo`, `.method`, `.frow/.pill`, `.lb/.lbx/.lbnav/.lbcap`, лента очереди `.queueband/.queuelbl` и мотив силуэтов на разделителях глав `.sec::before` (имена живут с 09.10.2026, вторая редакция смысла «Очередь, которая не расходится»); табель-доска `.racklbl/.rack/.tslot/.tnum/.tplace/.tstamp` и хроника `.dayline/.dl/.t/.s` жили до 09.10.2026 - сняты при переписывании смысла по фактуре гендиректора (вокзал Los Santos, безработица, стоящие автобусы и такси); `.mast/.snav/.shot/.pull/.who/.lb` совпадают по именам с прежними выпусками, но живут в CSS своего файла независимо.
Ежедневная газета `daily-08-10-2026.html` (08.10.2026, штамп 036 `one-pursuit-route`, очередь `anna-malboro/`): `.tapeline`, `.routelbl/.routewrap/.routeline/.rstop/.dot/.rn/.rp/.ru`, `.blotter/.bh/.br`, `.thread/.th/.n/.s`, `.position`, а также семейство мастхэда и секций из 035 в своей редакции (имена жили с 08.10.2026 до 10.10.2026: по решению гендиректора выпуск «Дорога не говорит ничего» СНЯТ с публикации и удалён из очереди 10.10.2026, страница в корень не попадала - вечный URL не занимался; штамп 036 `one-pursuit-route` зарезервирован и новым выпускам не выдаётся).
Расследование №2 `investigation-whitecoat.html` (09.10.2026, штамп 037 `white-coat-days`, очередь `anna-malboro/`): `.ecg`, `.chips/.chip`, `.verdictplate`, `.dlgbox/.dlg/.sp/.ln` и спикеры `.jd/.av/.la`, `.doccard/.stamp/.docrow`, `.logbox/.t/.n/.note`, `.evtable/.id/.st` и статусы `.v/.a`, `.verdictbox/.vb/.vs`, а также домовые семейства `.mast/.snav/.sec/.sechead/.kick/.lead/.shot/.duo/.frow/.pill/.lb` в своей редакции CSS (имена живут с 09.10.2026).
Пополнять реестр при каждом новом фирменном элементе; при рефакторе — не удалять записи,
а помечать датой «имя жило до …».

## 7. Ретро-штамповка опубликованных страниц (ТОЛЬКО по команде «ретро-штампуй»)
Комментарий + маркер не меняют вид, но меняют байты 28 файлов; URLs остаются вечными.
Делается одним коммитом скриптом (добавляет блоки §1 и §3 по номеру из таблицы), после чего
сразу коммит + тег + манифест.
