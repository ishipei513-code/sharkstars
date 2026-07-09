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

// Instagram埋め込みの高さ調整：ウィジェット実測に基づく計算式で中身ぴったりに合わせる（余白防止）
// 実測値（headless Edge）：ヘッダー157px（狭幅で名前が折返すと181px）／グリッド2行・1マス=(幅-14)/3（最小159.5px）
(function () {
  'use strict';
  var iframe = document.querySelector('.insta-embed iframe');
  if (!iframe) return;
  function fit() {
    var w = iframe.clientWidth;
    if (!w) return;
    var cell = Math.max((w - 14) / 3, 159.5);
    var header = w < 470 ? 181 : 157;
    iframe.style.height = Math.ceil(header + 2 * cell + 2) + 'px';
  }
  fit();
  window.addEventListener('resize', fit);
  window.addEventListener('load', fit);
  // Instagramが実高を通知してきた場合はそちらを優先（現状は送られてこないが将来対応）
  window.addEventListener('message', function (e) {
    if (e.origin !== 'https://www.instagram.com') return;
    var data = e.data;
    try {
      if (typeof data === 'string') data = JSON.parse(data);
    } catch (err) { return; }
    if (data && data.type === 'MEASURE' && data.details && data.details.height) {
      iframe.style.height = data.details.height + 'px';
    }
  });
})();
