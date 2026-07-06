// TRINITY 共通スクリプト：スクロールリビール／ヘッダー状態／モバイルナビ
(function () {
  'use strict';

  // スクロールリビール
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -12% 0px' });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  // TOPのみ：ヒーローを過ぎたらヘッダーを白背景に（下層は .sub 固定）
  var header = document.querySelector('.header');
  if (header && !header.classList.contains('sub')) {
    var onScroll = function () {
      header.classList.toggle('solid', window.scrollY > window.innerHeight * 0.7);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // モバイルナビ
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        document.body.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
})();
