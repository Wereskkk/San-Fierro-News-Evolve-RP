# SFN · Мониторинг, доказательная база, протокол при краже

## 1. Мониторинг (10 минут в неделю, понедельник)
1. Открыть публичные страницы конкурирующих редакций и любые «новые газеты» сервера.
2. Просмотр кода → Ctrl+F по маркерам, от грубых к тонким:
   - `SFN-DESIGN`, `SFN ·`, `San Fierro News`, `Jonny Wilde`, `Anna Malboro`, `Sonya Malboro`;
   - строка подвала `дизайн и вёрстка — редакция`;
   - имена из реестра сигнатурных классов (`snippets.md` §6): `.pcard`, `.plate`, `.jackpot`,
     `.plateline`, `.pullq`, `.chron-grid`, `.hubbtn`, `.tape`, `.mapframe`, `.wxcard`, `.hocard`;
   - характерные строки CSS: `repeating-conic-gradient(#b3123f`, `--mag:#ff2e88`, `clamp(2rem,5.2vw,3.6rem)`.
3. Совпадение по 1–2 общим словам — не доказательство. Совпадение по штампу, маркеру,
   реестровому классу ИЛИ побайтовое — доказательство. Переходим к §2.

## 2. Пакет доказательств (фиксируется ДО любых контактов и постов)
Папка `evidence/YYYY-MM-DD-<кто>/` в рабочей песочнице редакции (вне репозитория!):
1. **Их сторона:** снапшот их страницы на web.archive.org (Save Page Now) — если страница публична;
   если под логином/в игре — скриншоты (полоса целиком + шапка + подвал) и сохранённый исходник
   (`их-страница.html`) с датой получения;
2. **Хэш их файла:** `sha256sum их-страница.html` → записать в `evidence/README.md` этой папки;
3. **Наша сторона:** ссылка на наш коммит и тег с датой РАНЕЕ их снапшота; запись из `manifest.json`
   (хэш нашего файла на тот день); наш снапшот на archive.org;
4. **Таблица совпадений:** маркер → где у нас (файл, строка, дата коммита) → где у них (скрин/строка).
Формулируем сухо: даты, ссылки, хэши. Эмоции и обвинения в пакет не входят.

## 3. Протокол действий (по месту размещения копии)
**Копия на GitHub / GitLab / другом хостинге с DMCA:**
- жалоба DMCA через форму хостинга; шаблон ниже; прикладываем: LICENSE, ссылку на тег/коммит,
  таблицу совпадений, хэши. Явная копия файлов сносится обычно за дни.
**Копия в игре / на форуме Evolve RP / в Discord:**
- жалоба администрации сервера с тем же пакетом; акцент не на «лицензии», а на фактах:
  «дизайн и вёрстка нашей редакции, первенство подтверждено публичной историей от ДД.ММ.ГГГГ,
  у ответчика совпадают служебные маркеры редакции (перечень)». Администрация сервера —
  главный и самый быстрый рычаг; лицензия для неё лишь оформление.
**Публично (по желанию гендиректора, один раз):**
- короткий пост без имён и перепалок: «Оригинальные выпуски San Fierro News выходят здесь: [ссылка].
  Хронология и история правок открыты с 23.09.2026». Факты делают работу сами.

## 4. Шаблон DMCA-жалобы (GitHub)
```
To: GitHub, Inc. DMCA Agent
Subject: DMCA Takedown Notification — copyright infringement (repository: <URL копии>)

1. Identification of the copyrighted work: original editorial design, layout, markup, CSS and
   texts of the "San Fierro News" publications, © 2026 Jonny Wilde, published at
   <URL нашего репозитория/страницы>, licensed CC BY-NC-ND 4.0 (LICENSE in repository root).
2. Identification of the infringing material: <URL копии>, files: <список>.
   The material reproduces the copyrighted editorial layer verbatim / with minor alterations,
   including the editorial markers and class names listed in the attached comparison table.
3. Proof of prior publication: public commit history and release tags of the original repository,
   commit <SHA> dated <DD.MM.YYYY>, tag <имя>, preceding the infringing publication dated <дата>.
4. Contact: <имя, email, Discord-тег гендиректора>.
5. Good faith belief: I have a good faith belief that use of the material in the manner complained
   of is not authorized by the copyright owner, its agent, or the law.
6. Accuracy: I swear, under penalty of perjury, that the information in this notification is
   accurate and that I am the owner, or an agent authorized to act on behalf of the owner, of an
   exclusive right that is allegedly infringed.
Signature: Jonny Wilde, <дата>
```

## 5. Шаблон жалобы администрации Evolve RP (сухой, внутриигровой контекст)
```
Тема: Плагиат оформления издания San Fierro News
1. Факт: издание <название/автор> использует дизайн и вёрстку редакции San Fierro News.
2. Первенство: наш выпуск от ДД.ММ.ГГГГ, публичная история правок: <ссылка на тег/коммит>.
3. Совпадения: служебные маркеры редакции <список: штамп, классы, строка подвала> —
   таблица и скриншоты приложены.
4. Просьба: прекратить использование оформления редакции San Fierro News на сервере.
Приложения: пакет доказательств (скриншоты, исходники, хэши, таблица совпадений).
Подпись: Jonny Wilde, генеральный директор San Fierro News.
```

## 6. Чего НЕ делать
- Обфускация кода, запрет правого клика, «водяные знаки нулевой ширины» в тексте:
  обходится за минуты, ломает доступность и вид, выглядит неуверенно.
- Закрывать репозиторий: публичная датированная история — наше главное доказательство
  и бесплатный хостинг архива.
- Писать копирующему до сборки пакета доказательств: предупредим — зачистит маркеры.
