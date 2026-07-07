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

// Instagram埋め込みの高さ自動調整：Instagram側が送るMEASUREメッセージを受け、中身の実高に合わせる（余白防止）
(function () {
  'use strict';
  var iframe = document.querySelector('.insta-embed iframe');
  if (!iframe) return;
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
