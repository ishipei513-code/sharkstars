/* マリンケア訪問看護ステーション — トップC3 scripts */
(function(){
  'use strict';
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1) header scrolled ＋ ヒーロー表示中はフローティングCTAを隠す
  //    （波帯の右下リンクと重なるため。メニュー開閉の is-nav-open とは別クラスで管理する）
  var header=document.querySelector('.header');
  var heroEl=document.querySelector('.hero');
  var fabEl=document.getElementById('recruitFab');
  var onScroll=function(){
    if(header) header.classList.toggle('is-scrolled', window.scrollY>20);
    if(fabEl&&heroEl) fabEl.classList.toggle('is-over-hero', window.scrollY < heroEl.offsetHeight*0.6);
  };
  onScroll(); window.addEventListener('scroll',onScroll,{passive:true});
  window.addEventListener('resize',onScroll,{passive:true});

  // 2) 全画面メニュー（開閉・Esc・背景クリック・フォーカストラップ・スクロールロック）
  var toggle=document.getElementById('menuToggle'), gmenu=document.getElementById('globalMenu');
  if(toggle&&gmenu){
    var lastFocus=null, lockedY=0;
    var focusables=function(){
      return Array.prototype.slice.call(gmenu.querySelectorAll('a[href],button:not([disabled])'));
    };
    var isOpen=function(){ return gmenu.classList.contains('is-open'); };
    var openMenu=function(){
      lastFocus=document.activeElement;
      lockedY=window.scrollY||window.pageYOffset||0;
      gmenu.classList.add('is-open'); gmenu.removeAttribute('inert');
      toggle.classList.add('is-open');
      toggle.setAttribute('aria-expanded','true');
      toggle.setAttribute('aria-label','メニューを閉じる');
      document.body.classList.add('menu-open');
      // iOS でも背景が動かないよう body を固定（閉じたら元の位置へ戻す）
      document.body.style.position='fixed';
      document.body.style.top=(-lockedY)+'px';
      document.body.style.left='0'; document.body.style.right='0'; document.body.style.width='100%';
      var f=focusables(); if(f.length) f[0].focus();
      var fab=document.getElementById('recruitFab'); if(fab) fab.classList.add('is-nav-open');
    };
    var closeMenu=function(restoreFocus){
      gmenu.classList.remove('is-open'); gmenu.setAttribute('inert','');
      toggle.classList.remove('is-open');
      toggle.setAttribute('aria-expanded','false');
      toggle.setAttribute('aria-label','メニューを開く');
      document.body.classList.remove('menu-open');
      document.body.style.position=''; document.body.style.top='';
      document.body.style.left=''; document.body.style.right=''; document.body.style.width='';
      window.scrollTo(0,lockedY);
      var fab=document.getElementById('recruitFab'); if(fab) fab.classList.remove('is-nav-open');
      if(restoreFocus!==false){
        var back=(lastFocus&&lastFocus.focus&&lastFocus!==document.body)?lastFocus:toggle;
        back.focus();
      }
    };
    toggle.addEventListener('click',function(){ isOpen()?closeMenu():openMenu(); });
    gmenu.addEventListener('click',function(e){
      // リンク・ボタン以外のどこを押しても閉じる（ul/li/nav の余白も拾う）
      if(!e.target.closest||!e.target.closest('a,button')) closeMenu();
    });
    gmenu.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click',function(){ closeMenu(false); });
    });
    document.addEventListener('keydown',function(e){
      if(!isOpen()) return;
      if(e.key==='Escape'||e.key==='Esc'){ e.preventDefault(); closeMenu(); return; }
      if(e.key!=='Tab') return;
      var f=focusables(); if(!f.length) return;
      f.push(toggle); // ハンバーガー（＝閉じるボタン）もトラップに含める
      var first=f[0], last=f[f.length-1];
      if(e.shiftKey && document.activeElement===first){ e.preventDefault(); last.focus(); }
      else if(!e.shiftKey && document.activeElement===last){ e.preventDefault(); first.focus(); }
    });
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
      e.preventDefault();
      // ヘッダーが fixed なので、その高さぶん手前で止める（潜り防止）
      var off=(header?header.offsetHeight:0)+12;
      var y=t.getBoundingClientRect().top+window.scrollY-off;
      window.scrollTo({top:y,behavior:REDUCED?'auto':'smooth'});
    });
  });

  // 5) FAB ready
  var fab=document.getElementById('recruitFab'); if(fab)fab.classList.add('is-ready');

  // 6) ヒーロー：全面写真のクロスフェード（reduced時は1枚目で固定）
  //    ゆっくりしたズームはCSS側で全スライドに常時かけている（切替時の縮みを避けるため）
  var heroMedia=document.getElementById('heroMedia');
  if(heroMedia){
    var shots=Array.prototype.slice.call(heroMedia.querySelectorAll('.hero-shot'));
    if(!REDUCED && shots.length>1){
      var hi=0, zi=1;
      setInterval(function(){
        var prev=hi;
        hi=(hi+1)%shots.length;
        // 次の1枚を手前に重ねてフェードインさせる（両方を半透明にすると下地が透けて濁る）
        shots[hi].style.zIndex=(++zi);
        shots[hi].classList.add('is-on');
        setTimeout(function(){ shots[prev].classList.remove('is-on'); },1300);
      },6000);
    }
  }

  // 6.5) カーブコピーが波に乗って右から流れ込む
  //      参照サイトは1文字ずつSVGグリフをモーションパス配置しているが、
  //      textPath の startOffset を動かせば曲線に沿った回転はブラウザが処理する。
  (function(){
    var skipOpening = document.documentElement.classList.contains('no-opening');
    try{ sessionStorage.setItem('marinOpened','1'); }catch(e){}

    var tps = document.querySelectorAll('.hero-arc textPath[data-from]');
    if(!tps.length || REDUCED) return;   // reduced時は最終位置のまま動かさない

    var parse = function(v){ return { n: parseFloat(v), pct: /%\s*$/.test(v) }; };
    var easeOutCubic = function(p){ return 1-Math.pow(1-p,3); };

    Array.prototype.forEach.call(tps, function(tp){
      var to = parse(tp.getAttribute('startOffset'));
      var from = parse(tp.getAttribute('data-from'));
      var dur = parseFloat(tp.getAttribute('data-dur')||'1500');
      // 幕を出さない回（2回目以降）は待たずに動かす
      var delay = skipOpening ? 140 : parseFloat(tp.getAttribute('data-delay')||'0');
      var unit = to.pct ? '%' : '';

      tp.setAttribute('startOffset', from.n + unit);
      var t0 = null;
      var step = function(ts){
        if(t0===null) t0=ts;
        var e = ts - t0 - delay;
        if(e < 0){ requestAnimationFrame(step); return; }
        var p = Math.min(e/dur, 1);
        tp.setAttribute('startOffset', (from.n + (to.n-from.n)*easeOutCubic(p)) + unit);
        if(p < 1) requestAnimationFrame(step);
        else tp.setAttribute('startOffset', to.n + unit);
      };
      requestAnimationFrame(step);
    });
  })();

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
