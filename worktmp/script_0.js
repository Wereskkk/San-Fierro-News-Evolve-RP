
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
