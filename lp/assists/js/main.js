/* SHARKSTARS 集客LP — モーション＋お問い合わせフォーム
   装飾モーションは prefers-reduced-motion を尊重。
   グレースフルデグラデーション：
   - [data-anim]系の初期非表示は html.js ＋ no-preference に限定。
   - .rise は <noscript>（JS無効時）と .js-failed（main.js読込失敗時・index.htmlのonerror）で
     表示に戻すため、JSが動かない／読めない場合も全内容が表示される。 */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- セクションのふわっと表示（.rise を .in で発火） ---- */
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: .12 });
  document.querySelectorAll('.sec,.hero').forEach(function (el) {
    if (!el.classList.contains('in')) io.observe(el);
  });

  /* ---- 価格カウントアップ（[data-count] すべて） ---- */
  function countUp(el) {
    var target = +el.dataset.count;
    var fired = false;
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting || fired) return;
        fired = true;
        co.unobserve(el);
        if (reduceMotion) { el.textContent = target.toLocaleString(); return; }
        var start = null;
        function step(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / 700, 1);
          var v = Math.floor((1 - Math.pow(1 - p, 3)) * target);
          el.textContent = v.toLocaleString();
          if (p < 1) { requestAnimationFrame(step); }
          else { el.textContent = target.toLocaleString(); el.classList.add('counted'); }
        }
        requestAnimationFrame(step);
      });
    }, { threshold: .6 });
    co.observe(el);
  }
  document.querySelectorAll('[data-count]').forEach(countUp);

  /* ---- 固定CTA：ファーストビューを過ぎたら表示＋初回パルス ---- */
  var sticky = document.querySelector('.sticky');
  var hero = document.querySelector('.article-hero, .hero');
  if (sticky && hero) {
    var pulsed = false;
    var toggleSticky = function () {
      var show = window.scrollY > hero.offsetHeight * 0.35;
      sticky.classList.toggle('is-visible', show);
      if (show && !pulsed) {
        pulsed = true;
        if (!reduceMotion) {
          var b = sticky.querySelector('.btn');
          if (b) { b.classList.add('pulse-once'); setTimeout(function () { b.classList.remove('pulse-once'); }, 1300); }
        }
      }
    };
    toggleSticky();
    window.addEventListener('scroll', toggleSticky, { passive: true });
    window.addEventListener('resize', toggleSticky);
  }

  /* ---- 見せ場アニメーション（[data-anim]） ---- */
  function typeInto(el, sel) {
    var t = el.querySelector(sel);
    var q = el.dataset.q || (t ? t.textContent : '');
    if (!t) { el.classList.add('is-anim'); return; }
    if (reduceMotion) { t.textContent = q; el.classList.add('is-anim'); return; }
    t.textContent = '';
    t.classList.add('is-typing');
    var i = 0;
    (function tick() {
      t.textContent = q.slice(0, ++i);
      if (i < q.length) { setTimeout(tick, 95); }
      else { t.classList.remove('is-typing'); setTimeout(function () { el.classList.add('is-anim'); }, 280); }
    })();
  }

  function runChat(stage) {
    var chat = stage.querySelector('.lc-chat');
    if (!chat) return;
    var rows = Array.prototype.filter.call(chat.children, function (c) {
      return c.classList.contains('lc-in') || c.classList.contains('lc-out');
    });
    if (reduceMotion) { rows.forEach(function (r) { r.classList.add('show'); }); return; }
    var delay = 250;
    rows.forEach(function (row) {
      if (row.classList.contains('lc-in')) {
        var typing = document.createElement('div');
        typing.className = 'lc-in lc-typing show';
        typing.innerHTML = '<span class="lc-av"></span><div class="lc-msg"><div class="lc-bub"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div></div>';
        (function (tp, rw, d) {
          setTimeout(function () { chat.insertBefore(tp, rw); chat.scrollTop = chat.scrollHeight; }, d);
          setTimeout(function () {
            if (tp.parentNode) tp.parentNode.removeChild(tp);
            rw.classList.add('show'); chat.scrollTop = chat.scrollHeight;
          }, d + 850);
        })(typing, row, delay);
        delay += 1500;
      } else {
        (function (rw, d) {
          setTimeout(function () { rw.classList.add('show'); chat.scrollTop = chat.scrollHeight; }, d);
        })(row, delay);
        delay += 850;
      }
    });
  }

  var animObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      animObserver.unobserve(el);
      switch (el.dataset.anim) {
        case 'search':
        case 'result': typeInto(el, '.iv-typed'); break;
        case 'chat': runChat(el); break;
        default: el.classList.add('is-anim');
      }
    });
  }, { threshold: .3, rootMargin: '0px 0px -8% 0px' });

  /* チャットは表示前にメッセージを隠す（動きを許容する場合のみ） */
  if (!reduceMotion) {
    document.querySelectorAll('[data-anim="chat"] .lc-chat').forEach(function (c) { c.classList.add('chat-armed'); });
  }
  document.querySelectorAll('[data-anim]').forEach(function (el) { animObserver.observe(el); });

  /* ---- お問い合わせフォーム（Web3Forms / AJAX＋素のPOSTフォールバック） ---- */
  var form = document.getElementById('lp-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('.lpf-submit');
      var status = form.querySelector('.lpf-status');
      status.className = 'lpf-status';
      status.textContent = '';
      if (!form.checkValidity()) { form.reportValidity(); return; }
      btn.disabled = true;
      btn.classList.add('is-loading');
      status.textContent = '送信中…';
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      })
        .then(function (res) { return res.json().then(function (j) { return { ok: res.ok, body: j }; }); })
        .then(function (r) {
          if (r.ok && r.body && r.body.success) {
            var done = document.getElementById('lpf-done');
            form.style.display = 'none';
            if (done) {
              done.removeAttribute('hidden');
              requestAnimationFrame(function () { done.classList.add('show'); });
              try { done.focus({ preventScroll: true }); } catch (_) { try { done.focus(); } catch (_e) {} }
              try { done.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' }); }
              catch (_) { done.scrollIntoView(); }
            }
          } else {
            throw new Error((r.body && r.body.message) || 'failed');
          }
        })
        .catch(function () {
          status.textContent = 'うまく送信できませんでした。お手数ですが時間をおいて再度お試しいただくか、LINEからご連絡ください。';
          status.classList.add('is-error');
          btn.disabled = false;
          btn.classList.remove('is-loading');
        });
    });
  }
})();
