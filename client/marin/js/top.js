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

  // --- carousel/count-up は後続タスクでここに追加 ---
})();
