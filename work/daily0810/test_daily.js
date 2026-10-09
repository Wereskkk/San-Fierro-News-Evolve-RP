// SFN: headless-прогон ежедневников 07.10 / 08.10 (jsdom): навигация data-t, scrollspy, лайтбокс.
const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

const ROOT = path.resolve(__dirname, '..', '..');
const FILES = [
  ['daily-08-10-2026-los-santos.html', 10, 6],
  ['anna-malboro/investigation-whitecoat.html', 25, 11],
  ['daily-10-10-2026.html', 6, 6],
  ['anna-malboro/daily-10-10-2026-unknowns.html', 6, 5],
];

let fails = 0;
const ok = (cond, msg) => { if (cond) { console.log('  ok  ', msg); } else { fails++; console.log('  FAIL', msg); } };

for (const [rel, nfig, nnav] of FILES) {
  console.log('==', rel);
  let html = fs.readFileSync(path.join(ROOT, rel), 'utf-8');
  // base64-блобы заменяем заглушкой: jsdom не нужен вес
  html = html.replace(/data:image\/jpeg;base64,[A-Za-z0-9+/=]+/g, 'data:image/jpeg;base64,AAAA');
  const dom = new JSDOM(html, { runScripts: 'outside-only', pretendToBeVisual: true });
  const { window } = dom;
  const { document } = window;
  window.Element.prototype.scrollIntoView = function () { window.__scrolled = (window.__scrolled || 0) + 1; window.__lastTarget = this.getAttribute('data-sec'); };
  // исполняем inline-скрипт
  const scripts = [...document.querySelectorAll('script')];
  for (const s of scripts) { window.eval(s.textContent); }

  ok(document.querySelectorAll('figure.shot').length === nfig, 'фигур: ' + nfig);
  ok(document.querySelectorAll('.snavbtn').length === nnav, 'кнопок навигации: ' + nnav);

  // клик по кнопке навигации -> scrollIntoView на секции
  const btn = document.querySelectorAll('.snavbtn')[1];
  const want = btn.getAttribute('data-t');
  btn.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  ok(window.__scrolled === 1 && window.__lastTarget === want, 'клик навигации скроллит секцию ' + want);

  // клик по слоту/точке маршрута (data-t вне snav)
  const slot = document.querySelector('.tslot, .rstop');
  if (slot) {
    const want2 = slot.getAttribute('data-t');
    slot.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
    ok(window.__lastTarget === want2, 'клик слота/точки скроллит секцию ' + want2);
  }

  // scrollspy: при нулевых rect'ах текущей становится последняя секция
  window.dispatchEvent(new window.Event('scroll'));
  setTimeout(() => {}, 0);
  const secs = [...document.querySelectorAll('[data-sec]')];
  const curSec = secs[secs.length - 1].getAttribute('data-sec');
  const curBtn = [...document.querySelectorAll('.snavbtn')].find(b => b.classList.contains('cur'));
  ok(!!curBtn && (curBtn.getAttribute('data-t') === curSec || secs.some(s => s.getAttribute('data-sec') === curBtn.getAttribute('data-t'))), 'scrollspy подсвечивает кнопку');

  // лайтбокс: открыть, листать, закрыть
  const img0 = document.querySelector('figure.shot img');
  img0.dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const lb = document.getElementById('lb');
  ok(lb.classList.contains('on'), 'лайтбокс открылся');
  ok(document.getElementById('lbcap').textContent === img0.getAttribute('alt'), 'подпись лайтбокса = alt кадра');
  document.getElementById('lbnext').dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const alt1 = document.querySelectorAll('figure.shot img')[1].getAttribute('alt');
  ok(document.getElementById('lbcap').textContent === alt1, 'next листает на кадр 2');
  document.getElementById('lbprev').dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  document.getElementById('lbprev').dispatchEvent(new window.MouseEvent('click', { bubbles: true }));
  const altLast = document.querySelectorAll('figure.shot img')[nfig - 1].getAttribute('alt');
  ok(document.getElementById('lbcap').textContent === altLast, 'prev с нуля заворачивает на последний кадр');
  document.dispatchEvent(new window.KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
  ok(!lb.classList.contains('on'), 'Escape закрывает лайтбокс');
}

console.log(fails === 0 ? 'HEADLESS: все ассерты зелёные' : ('HEADLESS: провалов ' + fails));
process.exit(fails === 0 ? 0 : 1);
