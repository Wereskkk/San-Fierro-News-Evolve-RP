
(function(){
'use strict';
function $(id){return document.getElementById(id);}
var wr=$('wr'),br=$('br'),bh=$('bh'),btn=$('spinBtn'),wres=$('wres');
var resNum=$('resNum'),resWord=$('resWord'),resNote=$('resNote');
if(!wr||!br||!bh||!btn){return;}
var ORDER=[0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26];
var RED={1:1,3:1,5:1,7:1,9:1,12:1,14:1,16:1,18:1,19:1,21:1,23:1,25:1,27:1,30:1,32:1,34:1,36:1};
var STEP=360/37,RT=196.5,RP=160;
var wheelDeg=0,ballDeg=-25,r=RT,hop=0,hopV=0,r0=RT;
var state='idle',phase='',t=0,last=0;
var idx=0,relDeg=0,relV=0,relStart=0,rollT=0,rollDur=1.8,rollDelta=0,bkt=0,crossed=0,bvDrop=60;
var lock=null,bounces=[];
var lastFret=0,lastDia=0,lastHopT=-9;
var reduced=false;
try{reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;}catch(e){}
var HW=20,HZ=0.14,SK=26,SZ=0.32;
var NOTES=[
'Дом в плюсе — но красивую игру в этом городе помнят дольше, чем крупные проигрыши.',
'Число записано в журнал смены. Пит-босс кивнул и перетасовал фишки.',
'Крупье убрал фишки со стола. Город моргнул неоном — ставки приняты.',
'Шарик сказал своё слово — спорить с ним за зелёным сукном не принято.',
'Редакция занесла число в блокнот: вдруг совпадёт с завтрашним тиражом.',
'Удача выбрала число сама. Мы просто успели записать.'
];
function mod(a,m){return ((a%m)+m)%m;}
function lerp(a,b,p){return a+(b-a)*p;}
function smooth(p){p=Math.min(1,Math.max(0,p));return p*p*(3-2*p);}
function kick(v){hopV+=v*(reduced?0.55:1);}
function spring(dt){
  var acc=-HW*HW*hop-2*HZ*HW*hopV;
  hopV+=acc*dt;hop+=hopV*dt;
  if(hop<-2.5){hop=-2.5;if(hopV<0){hopV*=-0.35;}}
  if(hop>17){hop=17;if(hopV>0){hopV=0;}}
}
function render(){
  wr.setAttribute('transform','rotate('+wheelDeg.toFixed(2)+' 220 220)');
  br.setAttribute('transform','rotate('+ballDeg.toFixed(2)+' 220 220)');
  bh.setAttribute('transform','translate(0 '+(-(r+hop)).toFixed(2)+')');
}
function showResult(){
  var n=ORDER[idx];
  resNum.textContent=String(n);
  resNum.className='resnum '+(n===0?'rz':(RED[n]?'rr':'rb'));
  resWord.textContent=(n===0?'ЗЕРО':(RED[n]?'КРАСНОЕ':'ЧЁРНОЕ'));
  resNote.textContent=NOTES[Math.floor(Math.random()*NOTES.length)];
  wres.classList.add('on');
  btn.disabled=false;
  btn.textContent='КРУТИТЬ ЕЩЁ РАЗ';
  var old=document.querySelectorAll('.tnum.hit'),i;
  for(i=0;i<old.length;i++){old[i].classList.remove('hit');}
  var tc=document.querySelector('.tnum[data-n="'+n+'"]');
  if(tc){tc.classList.add('hit');}
}
function onDone(){
  showResult();
  window.setTimeout(function(){if(state==='done'){state='idle2';}},1600);
}
/* шарик упал с обода на цифры: скользит относительно колеса и скачет через разделители */
function startRoll(){
  phase='roll';rollT=0;crossed=0;
  relStart=ballDeg-wheelDeg;relDeg=relStart;
  var hopN,frac;
  if(reduced){
    hopN=2+Math.floor(Math.random()*3);
    frac=0.2+Math.random()*0.6;
    rollDur=0.8+Math.random()*0.3;
  }else{
    hopN=2+Math.floor(Math.random()*35);
    frac=0.15+Math.random()*0.7;
    rollDur=Math.min(2.7,0.75+(hopN+frac)*0.055)+Math.random()*0.25;
  }
  rollDelta=-(STEP*(hopN+frac));
  bkt=Math.floor((relDeg-STEP/2)/STEP);
  lastHopT=-9;
  resNote.textContent='Шарик на цифрах: скачет через разделители…';
}
/* карман поймал шарик: пружинное успокоение + колесо докручивает до указателя */
function startLock(wvNow){
  phase='lock';
  var kRaw=Math.round(relDeg/STEP);
  idx=mod(kRaw,37);
  relDeg=idx*STEP+(relDeg-kRaw*STEP);
  relV=(Math.random()-0.5)*8;
  SZ=reduced?0.6:0.32;
  var d0=mod(-idx*STEP-wheelDeg,360);
  var T2=reduced?1.1:1.8;
  var d2=wvNow*T2/2;
  var delta=(d0>d2+60)?d0:d0+360;
  var d1=delta-d2;
  if(d1<0){d1=0;d2=delta;T2=2*delta/wvNow;}
  lock={t0:t,w0:wheelDeg,v1:wvNow,d1:d1,d2:d2,T2:T2,t1:d1/wvNow,tEnd:d1/wvNow+T2};
  bounces=[{at:0.03,v:170,done:false},{at:0.4,v:110,done:false},{at:0.85,v:60,done:false}];
  kick(150);
  resNote.textContent='Карман поймал шарик: колесо докручивает к указателю…';
}
function finish(){
  relDeg=idx*STEP;relV=0;
  ballDeg=wheelDeg+relDeg;
  state='done';phase='';r=RP;
  onDone();
}
function spinStart(){
  if(state==='spin'){return;}
  state='spin';phase='accel';t=0;r0=r;lock=null;hop=0;hopV=0;relV=0;
  btn.disabled=true;btn.textContent='ШАРИК В ИГРЕ…';
  wres.classList.remove('on');
  resNum.textContent='…';resNum.className='resnum r0';
  resWord.textContent='КРУТИТСЯ';
  resNote.textContent='Разгон, борт, спираль — шарик ищет своё число.';
  lastFret=Math.floor((ballDeg-wheelDeg)/STEP);
  lastDia=Math.floor((ballDeg-22.5)/45);
  lastHopT=-9;
  bvDrop=45+Math.random()*40;
}
btn.addEventListener('click',spinStart);
function frame(now){
  if(!last){last=now;}
  var dt=(now-last)/1000;last=now;
  if(dt>0.05){dt=0.05;}
  if(dt<0){dt=0;}
  var wv=0,bv=0;
  if(state==='idle'){
    if(!reduced){wv=20;bv=-46;}
    r=RT;
  }else if(state==='idle2'){
    wv=reduced?0:9;
    wheelDeg+=wv*dt;
    ballDeg=wheelDeg+idx*STEP;
    r=RP;spring(dt);render();
    window.requestAnimationFrame(frame);return;
  }else if(state==='done'){
    r=RP;
  }else if(state==='spin'){
    t+=dt;
    /* фаза: скачки по цифрам — scripted slide, гаснущий к своему карману */
    if(phase==='roll'){
      rollT+=dt;
      var pr=Math.min(1,rollT/rollDur);
      var ee=reduced?(1-(1-pr)*(1-pr)):(1-(1-pr)*(1-pr)*(1-pr));
      relDeg=relStart+rollDelta*ee;
      var sp=Math.abs(rollDelta)*(reduced?(2*(1-pr)):(3*(1-pr)*(1-pr)))/rollDur;
      var b2=Math.floor((relDeg-STEP/2)/STEP);
      if(b2!==bkt){
        bkt=b2;crossed++;
        if(rollT-lastHopT>0.05){lastHopT=rollT;kick(30+Math.min(160,sp*1.2));}
      }
      wv=lerp(200,180,pr);
      wheelDeg+=wv*dt;
      ballDeg=wheelDeg+relDeg;
      r=RP;
      spring(dt);render();
      if(pr>=1){startLock(wv);}
      window.requestAnimationFrame(frame);return;
    }
    /* фаза: пойман карманом, колесо докручивает к указателю */
    if(phase==='lock'){
      var td=t-lock.t0;
      if(td<lock.t1){wheelDeg=lock.w0+lock.v1*td;}
      else if(td<lock.tEnd){var pl=(td-lock.t1)/lock.T2;wheelDeg=lock.w0+lock.d1+lock.d2*(1-(1-pl)*(1-pl));}
      else{wheelDeg=lock.w0+lock.d1+lock.d2;finish();}
      var acc=-SK*SK*(relDeg-idx*STEP)-2*SK*SZ*relV;
      relV+=acc*dt;relDeg+=relV*dt;
      for(var bi=0;bi<bounces.length;bi++){var bb= bounces[bi];if(!bb.done&&td>=bb.at){bb.done=true;kick(bb.v);}}
      ballDeg=wheelDeg+relDeg;
      r=RP;
      spring(dt);render();
      window.requestAnimationFrame(frame);return;
    }
    /* фазы разгона, обода и спирали */
    var A1=reduced?0.25:0.5;
    var B1=A1+(reduced?0.9:1.6);
    var C1=B1+(reduced?0.8:1.5);
    if(t<A1){
      var p=t/A1;
      wv=lerp(20,210,smooth(p));
      bv=lerp(-46,-640,smooth(p));
      r=lerp(r0,RT,smooth(p));
    }else if(t<B1){
      wv=210;
      bv=-640+12*Math.sin(t*7);
      r=RT;
      var dseg=Math.floor((ballDeg-22.5)/45);
      if(dseg!==lastDia){
        lastDia=dseg;
        if(Math.random()<0.6){kick(140+Math.random()*90);}
      }
    }else{
      var q=Math.min(1,(t-B1)/(C1-B1));
      wv=lerp(210,200,q);
      bv=lerp(-640,bvDrop,smooth(q));
      var q2=(t-(B1+0.35))/(C1-B1-0.35);
      r=lerp(RT,RP,smooth(q2));
      if(r<RT-12){
        var rel=ballDeg-wheelDeg;
        var fs=Math.floor(rel/STEP);
        if(fs!==lastFret){
          lastFret=fs;
          if(t-lastHopT>0.045){
            lastHopT=t;
            kick(24+110*Math.min(1,Math.abs(bv-wv)/700));
          }
        }
      }
      if(t>=C1){startRoll();}
    }
  }
  spring(dt);
  wheelDeg+=wv*dt;
  ballDeg+=bv*dt;
  render();
  window.requestAnimationFrame(frame);
}
render();
window.requestAnimationFrame(frame);
})();
