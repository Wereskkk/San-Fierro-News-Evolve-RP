# -*- coding: utf-8 -*-
# Пересборка карты выпуска LV 02.10: новая городская схема + пины по отметкам редакции + навигация без якорей
import re, json, io

HTML = 'daily-02-10-2026-las-venturas.html'
s = io.open(HTML, encoding='utf-8').read()
b64 = open('worktmp/lvmap2.b64').read().strip()
cir = json.load(open('worktmp/circles.json'))

K = 1600.0 / 880.0
COL = {'red': 's01', 'green': 's02', 'darkblue': 's03', 'white': 's04',
       'yellow': 's05', 'cyan': 's06', 'magenta': 's07', 'black': 's08'}
NUM = {'s01': '01', 's02': '02', 's03': '03', 's04': '04', 's05': '05', 's06': '06', 's07': '07', 's08': '08'}
LAB = {'s01': 'Офис Las Venturas News', 's02': 'Автомастерская', 's03': 'LVPD', 's04': 'Банк города',
       's05': 'Авторынок', 's06': 'Автовокзал', 's07': 'Казино Caligula', 's08': 'Армия · лагерь в пустыне'}
LEG = {'s01': 'Офис Las Venturas News — полоса «Башня родственных перьев»',
       's02': 'Автомастерская — полоса «Там, где машинам возвращают вторую жизнь»',
       's03': 'LVPD — полоса «Ход королевы»',
       's04': 'Банк города — полоса «Деньги любят тишину»',
       's05': 'Авторынок — полоса «Витрина под открытым небом»',
       's06': 'Автовокзал — полоса «Ворота города»',
       's07': 'Казино Caligula — полоса «Главная люстра города»',
       's08': 'Армия · лагерь в пустыне — полоса «Прикрытие неона»'}

coords = {}
for col, sid in COL.items():
    x, y = cir[col][0], cir[col][1]
    coords[sid] = (round(x * K, 1), round(y * K, 1))
print(coords)

pins = []
for sid in ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08']:
    x, y = coords[sid]
    pins.append(
        '<g class="pin" data-t="%s" tabindex="0" role="button" aria-label="%s: перейти к полосе номера">'
        '<circle class="halo" cx="%s" cy="%s" r="44" fill="#f6c453"/>'
        '<circle class="core" cx="%s" cy="%s" r="26"/>'
        '<text class="pnum" x="%s" y="%s">%s</text>'
        '<text class="plab" x="%s" y="%s">%s</text></g>'
        % (sid, LAB[sid], x, y, x, y, x, y + 2, NUM[sid], x, y - 46, LAB[sid]))

legend = []
for sid in ['s01', 's02', 's03', 's04', 's05', 's06', 's07', 's08']:
    legend.append('<button type="button" data-t="%s"><b>%s</b><span>%s</span></button>' % (sid, NUM[sid], LEG[sid]))

section = u'''<section class="sec" id="lvmap">
  <div class="pcard" style="--acc:#f6c453">
    <div class="corner ctl"><span class="crank">8</span><span class="csuit">&#10022;</span></div>
    <div class="corner cbr"><span class="crank">8</span><span class="csuit">&#10022;</span></div>
    <div class="sechead">
      <span class="secno">КАРТА</span>
      <div class="sechtxt"><div class="rubric">НАВИГАЦИЯ · Городская черта Las Venturas</div><h2>Восемь адресов на одной карте</h2></div>
      <span class="rule"></span>
    </div>
    <p class="standfirst">Редакция разложила городскую схему Las Venturas из своего архива и нанесла все восемь адресов номера пинами. Нажмите на пин или на строку легенды — раскроется нужная полоса; у каждого заголовка ниже есть обратная ссылка «место на карте».</p>
    <div class="mapframe">
      <img class="lvmapimg" alt="Карта Las Venturas: городская схема с восемью пинами редакционных адресов" src="data:image/jpeg;base64,%s">
      <svg class="lvmapsvg" viewBox="0 0 1600 1080" role="img" aria-label="Карта Las Venturas с восемью пинами адресов этого выпуска"><g opacity=".9"><line x1="945" y1="190" x2="945" y2="102" stroke="#f6c453" stroke-width="4.5"/><polygon points="945,76 932,102 958,102" fill="#f6c453"/><text x="945" y="228" text-anchor="middle" font-family="BebasNeue,sans-serif" font-size="32" fill="#f6c453">С</text></g>%s</svg>
    </div>
    <div class="plateline"><div class="plate">LAS VENTURAS · ГОРОДСКАЯ ЧЕРТА · 8 АДРЕСОВ НОМЕРА</div></div>
    <div class="lvlegend">%s</div>
    <p class="mapnote">Схема: городская карта Las Venturas из редакционного архива, восемь адресов обведены редактором вручную. Пины сверены по кадрам Anna Malboro и ориентирам города — Strip, аэропорт, гольф-клуб и даунтаун. Пин 08 обведён широким контуром: армейский лагерь раскинулся в пустыне за городской чертой, и редакция отметила весь район базирования.</p>
  </div>
</section>

''' % (b64, ''.join(pins), ''.join(legend))

a = s.find('<section class="sec" id="lvmap">')
b = s.find('<section class="sec" id="s01">')
assert a != -1 and b != -1 and a < b
s = s[:a] + section + s[b:]

# --- CSS: легенда и обратные ссылки становятся кнопками ---
s = s.replace('.lvlegend a{display:flex;', '.lvlegend button{display:flex;', 1)
s = s.replace('.lvlegend a:hover{', '.lvlegend button:hover{', 1)
s = s.replace('border-radius:10px;background:rgba(255,255,255,.03);text-decoration:none;color:#e7daec;',
              'border-radius:10px;background:rgba(255,255,255,.03);text-decoration:none;color:#e7daec;\n cursor:pointer;font-family:inherit;font-size:1rem;text-align:left;appearance:none;-webkit-appearance:none;', 1)
s = s.replace('.tomap{display:inline-block;', '.tomap{appearance:none;-webkit-appearance:none;cursor:pointer;display:inline-block;', 1)
# размеры пинов под новый viewBox 1600
s = s.replace('.pin .core{fill:#150c1f;stroke:#f6c453;stroke-width:5;', '.pin .core{fill:#150c1f;stroke:#f6c453;stroke-width:3.5;', 1)
s = s.replace(".pin .pnum{font-family:'BebasNeue',sans-serif;font-size:38px;", ".pin .pnum{font-family:'BebasNeue',sans-serif;font-size:27px;", 1)
s = s.replace(".pin .plab{font-family:'PTSN',sans-serif;font-weight:700;font-size:31px;", ".pin .plab{font-family:'PTSN',sans-serif;font-weight:700;font-size:22px;", 1)
s = s.replace('stroke:#0d0812;stroke-width:10;paint-order:stroke;', 'stroke:#0d0812;stroke-width:7;paint-order:stroke;', 1)
s = s.replace('@media(max-width:640px){.lvlegend{grid-template-columns:1fr}}',
              '@media(max-width:640px){.lvlegend{grid-template-columns:1fr}}\n[data-t]{-webkit-tap-highlight-color:transparent;touch-action:manipulation}\n.sec{scroll-margin-top:16px}', 1)

# --- обратные ссылки у заголовков: кнопки вместо якорей ---
s, n1 = re.subn(r'<a class="tomap" href="#lvmap">(.*?)</a>',
                lambda m: '<button type="button" class="tomap" data-t="lvmap">%s</button>' % m.group(1), s)
print('backlinks replaced:', n1)

# --- JS-навигация scrollIntoView: вставляется перед скриптом рулетки ---
nav = u'''<script>
(function(){
function goTo(id){var el=document.getElementById(id);if(!el){return;}
 if(el.scrollIntoView){el.scrollIntoView({behavior:'smooth',block:'start'});}
 else{el.scrollTop=0;}}
window.sfGoTo=goTo;
function tgt(e){return (e.target&&e.target.closest)?e.target.closest('[data-t]'):null;}
document.addEventListener('click',function(e){
 var t=tgt(e);
 if(t){e.preventDefault();goTo(t.getAttribute('data-t'));return;}
 var a=(e.target&&e.target.closest)?e.target.closest('a[href^="#"]'):null;
 if(a){e.preventDefault();var h=a.getAttribute('href');if(h&&h.length>1){goTo(h.slice(1));}}
});
document.addEventListener('keydown',function(e){
 if(e.key!=='Enter'&&e.key!==' '&&e.key!=='Spacebar'){return;}
 var t=tgt(e);
 if(t&&t.tagName!=='BUTTON'){e.preventDefault();goTo(t.getAttribute('data-t'));}
});
})();
</script>
'''
i = s.rfind('<script>')
assert i != -1
s = s[:i] + nav + s[i:]

io.open(HTML, 'w', encoding='utf-8').write(s)
print('written, len', len(s))
print('href="# left:', s.count('href="#'))
print('data-t count:', s.count('data-t='))
