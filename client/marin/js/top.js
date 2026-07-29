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
    var setFab=function(open){var fab=document.getElementById('recruitFab');if(fab)fab.classList.toggle('is-nav-open',open);};
    var closeNav=function(){nav.classList.remove('is-open');toggle.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');document.body.style.overflow='';setFab(false);};
    toggle.addEventListener('click',function(){
      var open=nav.classList.toggle('is-open');
      toggle.classList.toggle('is-open',open);
      toggle.setAttribute('aria-expanded',open?'true':'false');
      document.body.style.overflow=open?'hidden':'';
      setFab(open);
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
      },4500);
    }
  }

  // 7) count-up（数字セクション等。reduced時は即・最終値）
  function easeOutCubic(p){return 1-Math.pow(1-p,3);}
  function countEl(el){
    var end=parseFloat(el.getAttribute('data-countup'));
    var unit=el.getAttribute('data-unit')||'';
    if(REDUCED){ el.textContent=end+unit; return; }
    var t0=null,dur=1950;
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

  // 8.5) hero video（実写の波。再生できたらSVG波を隠す。reduced時は静止ポスター）
  var hv=document.getElementById('heroVideo'), heroEl=document.querySelector('.hero');
  if(hv){
    if(REDUCED){ hv.removeAttribute('autoplay'); try{hv.pause();}catch(e){} }
    else{
      var markVideo=function(){ if(heroEl)heroEl.classList.add('has-video'); };
      hv.addEventListener('playing',markVideo);
      hv.addEventListener('loadeddata',function(){ if(hv.readyState>=2 && !hv.error){markVideo();} });
    }
  }

  // 8) 3D tilt on cards（マウスでカードが傾く。reduced/タッチ時は無効）
  if(!REDUCED && window.matchMedia && window.matchMedia('(hover:hover)').matches){
    var tiltSel='.route-card,.strength-item,.biz-col,.num-card,.staff-card,.voice-card,.pb-item';
    document.querySelectorAll(tiltSel).forEach(function(card){
      card.addEventListener('mousemove',function(e){
        var r=card.getBoundingClientRect();
        var px=(e.clientX-r.left)/r.width-0.5;
        var py=(e.clientY-r.top)/r.height-0.5;
        card.style.transform='perspective(720px) rotateX('+(-py*7).toFixed(2)+'deg) rotateY('+(px*9).toFixed(2)+'deg) translateY(-5px)';
      });
      card.addEventListener('mouseleave',function(){ card.style.transform=''; });
    });
  }

  // 9) Instagram 最新投稿の自動取得（公開JSONフィード）
  //    有効化：#instaMosaic に data-ig-feed="<公開フィードURL>" を付ける、または window.IG_FEED_URL を設定。
  //    例）Behold.so（無料）で @marin_care_nurse のフィードを作成 → 発行されるJSON URLを指定するだけ。
  //    未設定 or 取得失敗時は、設置済みのサンプルタイルをそのまま表示（壊れない）。
  (function(){
    var mosaic=document.getElementById('instaMosaic'); if(!mosaic) return;
    var feed=window.IG_FEED_URL||mosaic.getAttribute('data-ig-feed'); if(!feed||!window.fetch) return;
    var tiles=mosaic.querySelectorAll('.insta-tile'); if(!tiles.length) return;
    var pick=function(p){
      return p.mediaUrl||p.media_url||p.thumbnailUrl||p.thumbnail_url||
        (p.sizes&&((p.sizes.medium&&p.sizes.medium.mediaUrl)||(p.sizes.full&&p.sizes.full.mediaUrl)||(p.sizes.small&&p.sizes.small.mediaUrl)))||
        (p.images&&p.images.standard_resolution&&p.images.standard_resolution.url)||'';
    };
    fetch(feed,{mode:'cors'}).then(function(r){return r.json();}).then(function(data){
      var posts=Array.isArray(data)?data:(data.feed||data.posts||data.media||data.data||[]);
      if(!posts||!posts.length) return;
      tiles.forEach(function(tile,i){
        var p=posts[i]; if(!p) return;
        var img=tile.querySelector('img'), src=pick(p), link=p.permalink||p.link||p.url;
        if(img&&src){ img.removeAttribute('srcset'); img.setAttribute('src',src); }
        if(link){ tile.setAttribute('href',link); }
        if(p.caption){ tile.setAttribute('aria-label',String(p.caption).slice(0,80)); }
      });
    }).catch(function(){ /* サンプル表示のまま */ });
  })();

  // 10) 3Dカバーフロー・カルーセル（中央前面＋左右が奥へ／矢印・View・サイド画像クリック・ドット・自動送り）
  (function(){
    var track=document.getElementById('cfTrack'); if(!track) return;
    var slides=Array.prototype.slice.call(track.querySelectorAll('.cf-slide'));
    var n=slides.length; if(!n) return;
    var dotsEl=document.getElementById('cfDots'), dots=[], cur=0, timer=null;
    function render(){
      slides.forEach(function(s,k){
        s.classList.remove('is-center','is-prev','is-next');
        var d=(k-cur+n)%n;
        if(d===0)s.classList.add('is-center');
        else if(d===1)s.classList.add('is-next');
        else if(d===n-1)s.classList.add('is-prev');
      });
      dots.forEach(function(dt,k){ dt.className=(k===cur)?'on':''; });
    }
    function go(i){ cur=(i%n+n)%n; render(); }
    function next(){ go(cur+1); } function prev(){ go(cur-1); }
    if(dotsEl){ slides.forEach(function(_,k){ var s=document.createElement('span'); s.addEventListener('click',function(){go(k);}); dotsEl.appendChild(s); dots.push(s); }); }
    render();
    var bn=document.getElementById('cfNext'), bp=document.getElementById('cfPrev');
    if(bn)bn.addEventListener('click',next);
    if(bp)bp.addEventListener('click',prev);
    slides.forEach(function(s){ s.addEventListener('click',function(){ if(s.classList.contains('is-next'))next(); else if(s.classList.contains('is-prev'))prev(); }); });
    if(!REDUCED && n>1){
      var stop=function(){ if(timer){clearInterval(timer);timer=null;} };
      var start=function(){ stop(); timer=setInterval(next,6300); };
      start();
      var stage=document.getElementById('cfStage');
      if(stage){ stage.addEventListener('mouseenter',stop); stage.addEventListener('mouseleave',start); }
    }
  })();
})();
