/* マリンケア訪問看護ステーション — トップC3 scripts */
(function(){
  'use strict';
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1) header scrolled
  var header=document.querySelector('.header');
  if(header){
    var onScroll=function(){ header.classList.toggle('is-scrolled', window.scrollY>20); };
    onScroll(); window.addEventListener('scroll',onScroll,{passive:true});
  }

  // 2) mobile menu
  var toggle=document.querySelector('.menu-toggle'), nav=document.querySelector('.nav');
  if(toggle&&nav){
    var closeNav=function(){nav.classList.remove('is-open');toggle.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');document.body.style.overflow='';};
    toggle.addEventListener('click',function(){
      var open=nav.classList.toggle('is-open');
      toggle.classList.toggle('is-open',open);
      toggle.setAttribute('aria-expanded',open?'true':'false');
      document.body.style.overflow=open?'hidden':'';
    });
    nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeNav);});
  }

  // 3) reveal on scroll（reduced時は即表示）
  var reveals=document.querySelectorAll('.reveal');
  if(REDUCED || !('IntersectionObserver' in window)){
    reveals.forEach(function(el){el.classList.add('is-in');});
  }else{
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);} });
    },{threshold:.12,rootMargin:'0px 0px -10% 0px'});
    reveals.forEach(function(el){io.observe(el);});
  }

  // 4) smooth anchor
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var id=a.getAttribute('href').slice(1); if(!id)return;
      var t=document.getElementById(id); if(!t)return;
      e.preventDefault(); t.scrollIntoView({behavior:REDUCED?'auto':'smooth',block:'start'});
    });
  });

  // 5) FAB ready
  var fab=document.getElementById('recruitFab'); if(fab)fab.classList.add('is-ready');

  // 6) hero carousel（reduced時は1枚目固定）
  var track=document.getElementById('heroTrack'), dotsEl=document.getElementById('heroDots');
  if(track){
    var n=track.children.length, i=0, dots=[];
    if(dotsEl){ for(var k=0;k<n;k++){var s=document.createElement('span');if(k===0)s.className='on';dotsEl.appendChild(s);dots.push(s);} }
    if(!REDUCED && n>1){
      setInterval(function(){
        i=(i+1)%n;
        track.style.transform='translateX(-'+(i*100)+'%)';
        dots.forEach(function(d,j){d.className=(j===i)?'on':'';});
      },3000);
    }
  }

  // 7) count-up（数字セクション等。reduced時は即・最終値）
  function easeOutCubic(p){return 1-Math.pow(1-p,3);}
  function countEl(el){
    var end=parseFloat(el.getAttribute('data-countup'));
    var unit=el.getAttribute('data-unit')||'';
    if(REDUCED){ el.textContent=end+unit; return; }
    var t0=null,dur=1300;
    function step(ts){ if(!t0)t0=ts; var p=Math.min((ts-t0)/dur,1); el.textContent=Math.round(end*easeOutCubic(p))+unit; if(p<1)requestAnimationFrame(step); }
    el.textContent='0'+unit; requestAnimationFrame(step);
  }
  var counters=document.querySelectorAll('[data-countup]');
  if(counters.length){
    if(REDUCED || !('IntersectionObserver' in window)){
      counters.forEach(countEl);
    }else{
      var cio=new IntersectionObserver(function(entries){
        entries.forEach(function(e){ if(e.isIntersecting){countEl(e.target);cio.unobserve(e.target);} });
      },{threshold:.4});
      counters.forEach(function(el){cio.observe(el);});
    }
  }
})();
