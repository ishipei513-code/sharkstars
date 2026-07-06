// 作品集：軽量ライトボックス（クリック拡大・Esc/背景クリックで閉じる）
(function () {
  'use strict';
  var box = document.createElement('div');
  box.className = 'lb';
  box.innerHTML = '<img alt=""><button class="lb-close" aria-label="閉じる">&times;</button>';
  document.body.appendChild(box);
  var big = box.querySelector('img');

  document.querySelectorAll('.gallery img').forEach(function (img) {
    img.parentElement.addEventListener('click', function () {
      big.src = img.src;
      big.alt = img.alt;
      box.classList.add('is-open');
    });
  });
  function close() { box.classList.remove('is-open'); }
  box.addEventListener('click', function (e) { if (e.target !== big) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
})();
