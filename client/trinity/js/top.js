// TOP専用：ヒーロー写真のクロスフェード（7.5秒周期・reduced-motion時は停止）
(function () {
  'use strict';
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var imgs = document.querySelectorAll('.hero-bg img');
  if (imgs.length < 2) return;
  var i = 0;
  setInterval(function () {
    imgs[i].classList.remove('is-active');
    i = (i + 1) % imgs.length;
    imgs[i].classList.add('is-active');
  }, 7500);
})();
