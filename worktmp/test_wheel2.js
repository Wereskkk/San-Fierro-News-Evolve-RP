/* Тест рулетки 02.10 LV: симуляция движка в DOM-стабе, seeded random, 140 спинов.
   Проверяет lock-фазу: шарик не вылетает из кармана, нет рывков через колесо,
   колесо докручивает карман к указателю, результат совпадает с геометрией. */
'use strict';
const fs = require('fs');
const path = process.argv[2] || 'worktmp/lv_engine_new.js';
const SEEDS = (process.argv[3] || '1').split(',').map(Number);
const SPINS = Number(process.argv[4] || 140);

let src = fs.readFileSync(path, 'utf8');
// инжект рекордера во внутренности IIFE
src = src.replace('function render(){',
  'function render(){if(globalThis.__REC){globalThis.__REC(wheelDeg,ballDeg,r,hop,phase,idx,state,t);}');
if (!src.includes('__REC')) { console.error('recorder injection failed'); process.exit(2); }

const ORDER = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26];
const STEP = 360 / 37;
const mod = (a, m) => ((a % m) + m) % m;

function makeEnv(rand) {
  const els = {};
  function mk(id) {
    const listeners = {};
    const el = {
      id, _attrs: {}, _classes: new Set(), textContent: '', className: '', disabled: false,
      setAttribute(k, v) { el._attrs[k] = v; },
      getAttribute(k) { return el._attrs[k]; },
      classList: {
        add(c) { el._classes.add(c); }, remove(c) { el._classes.delete(c); },
        contains(c) { return el._classes.has(c); }
      },
      addEventListener(ev, fn) { (listeners[ev] = listeners[ev] || []).push(fn); },
      fire(ev, e) { (listeners[ev] || []).forEach(fn => fn(e || {})); }
    };
    els[id] = el;
    return el;
  }
  ['wr','br','bh','spinBtn','wres','resNum','resWord','resNote'].forEach(mk);
  let pending = null;
  const win = {
    matchMedia: () => ({ matches: false }),
    requestAnimationFrame(cb) { pending = cb; },
    setTimeout(fn, ms) { setTimeout(fn, 0); return 0; }, // fast-forward таймеров
    clearTimeout() {}
  };
  const doc = {
    getElementById: id => els[id] || null,
    querySelectorAll: () => [],
    querySelector: () => null
  };
  return { els, win, doc, step(now) { const cb = pending; pending = null; cb(now); } };
}

function runSeed(seed) {
  // seeded LCG
  let s = seed >>> 0;
  const rand = () => { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; };
  const origRandom = Math.random;
  Math.random = rand;

  const env = makeEnv(rand);
  globalThis.window = env.win;
  globalThis.document = env.doc;

  const rec = { phase: '', samples: [] };
  globalThis.__REC = (wheelDeg, ballDeg, r, hop, phase, idx, state, t) => {
    rec.phase = phase; rec.idx = idx; rec.state = state;
    rec.last = { wheelDeg, ballDeg };
    if (phase === 'lock') rec.samples.push({ rel: ballDeg - wheelDeg, idx, ballDeg });
  };

  const vm = require('vm');
  vm.runInThisContext(src, { filename: path });

  const results = [];
  let now = 0;
  const DT = 1000 / 60;
  for (let spin = 0; spin < SPINS; spin++) {
    env.els.spinBtn.fire('click');
    rec.samples = [];
    let frames = 0;
    let lockEnd = null;
    while (frames < 1200) {
      now += DT; frames++;
      env.step(now);
      if (rec.phase === 'lock' && rec.last) { /* sampling via __REC */ }
      if (rec.state === 'done' || rec.state === 'idle2') { lockEnd = frames; break; }
    }
    if (!lockEnd) { results.push({ spin, fatal: 'timeout' }); Math.random = origRandom; return results; }
    // метрики lock-фазы
    let maxErr = 0, maxJump = 0, prevBall = null;
    for (const smp of rec.samples) {
      const rest = smp.idx * STEP;
      maxErr = Math.max(maxErr, Math.abs(smp.rel - rest));
      if (prevBall !== null) maxJump = Math.max(maxJump, Math.abs(smp.ballDeg - prevBall));
      prevBall = smp.ballDeg;
    }
    const wd = rec.last.wheelDeg, idx = rec.idx;
    const pointerErr = Math.min(mod(wd + idx * STEP, 360), 360 - mod(wd + idx * STEP, 360));
    const shown = env.els.resNum.textContent;
    const expect = String(ORDER[mod(idx, 37)]);
    results.push({ spin, maxErr, maxJump, pointerErr, shown, expect, lockFrames: rec.samples.length,
                   mismatch: shown !== expect });
  }
  Math.random = origRandom;
  return results;
}

let worstErr = 0, worstJump = 0, worstPtr = 0, fails = 0, total = 0;
for (const seed of SEEDS) {
  const res = runSeed(seed);
  for (const r of res) {
    total++;
    if (r.fatal) { console.log(`seed ${seed} spin ${r.spin}: FATAL ${r.fatal}`); fails++; continue; }
    worstErr = Math.max(worstErr, r.maxErr);
    worstJump = Math.max(worstJump, r.maxJump);
    worstPtr = Math.max(worstPtr, r.pointerErr);
    if (r.maxErr >= STEP) { fails++; if (fails < 6) console.log(`seed ${seed} spin ${r.spin}: шарик вылетел из кармана в lock: |rel-rest|=${r.maxErr.toFixed(1)}° (карман ${STEP.toFixed(2)}°)`); }
    if (r.maxJump > 6) { fails++; if (fails < 6) console.log(`seed ${seed} spin ${r.spin}: рывок шарика ${r.maxJump.toFixed(1)}°/кадр в lock`); }
    if (r.pointerErr > 0.02) { fails++; if (fails < 6) console.log(`seed ${seed} spin ${r.spin}: указатель не на кармане, err=${r.pointerErr.toFixed(3)}°`); }
    if (r.mismatch) { fails++; if (fails < 6) console.log(`seed ${seed} spin ${r.spin}: показано ${r.shown}, геометрия ${r.expect}`); }
  }
}
console.log(`\n${path}: спинов ${total}, провалов ${fails}`);
console.log(`worst |rel-rest| в lock: ${worstErr.toFixed(2)}° (лимит ${STEP.toFixed(2)}°)`);
console.log(`worst скачок ball/кадр в lock: ${worstJump.toFixed(2)}° (лимит 6°)`);
console.log(`worst ошибка указателя: ${worstPtr.toFixed(4)}°`);
process.exit(fails ? 1 : 0);
