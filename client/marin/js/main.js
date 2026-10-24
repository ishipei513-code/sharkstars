/* マリンケア訪問看護ステーション — Interactive scripts */

// 1) Header: add .is-scrolled when page is scrolled
(function () {
  const header = document.querySelector('.header');
  if (!header) return;
  const onScroll = () => {
    if (window.scrollY > 20) header.classList.add('is-scrolled');
    else header.classList.remove('is-scrolled');
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
})();

// 2) 全画面メニュー（開閉・Esc・背景クリック・フォーカストラップ・スクロールロック）
(function () {
  const toggle = document.getElementById('menuToggle');
  const gmenu = document.getElementById('globalMenu');
  if (!toggle || !gmenu) return;

  let lastFocus = null;
  let lockedY = 0;
  const focusables = () =>
    Array.from(gmenu.querySelectorAll('a[href],button:not([disabled])'));
  const isOpen = () => gmenu.classList.contains('is-open');

  const openMenu = () => {
    lastFocus = document.activeElement;
    lockedY = window.scrollY || 0;
    gmenu.classList.add('is-open');
    gmenu.removeAttribute('inert');
    toggle.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'メニューを閉じる');
    document.body.classList.add('menu-open');
    // iOS でも背景が動かないよう body を固定（閉じたら元の位置へ戻す）
    document.body.style.position = 'fixed';
    document.body.style.top = `${-lockedY}px`;
    document.body.style.left = '0';
    document.body.style.right = '0';
    document.body.style.width = '100%';
    const f = focusables();
    if (f.length) f[0].focus();
    const fab = document.getElementById('recruitFab');
    if (fab) fab.classList.add('is-nav-open');
  };

  const closeMenu = (restoreFocus = true) => {
    gmenu.classList.remove('is-open');
    gmenu.setAttribute('inert', '');
    toggle.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'メニューを開く');
    document.body.classList.remove('menu-open');
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.left = '';
    document.body.style.right = '';
    document.body.style.width = '';
    window.scrollTo(0, lockedY);
    const fab = document.getElementById('recruitFab');
    if (fab) fab.classList.remove('is-nav-open');
    if (restoreFocus) {
      const back = lastFocus && lastFocus.focus && lastFocus !== document.body ? lastFocus : toggle;
      back.focus();
    }
  };

  toggle.addEventListener('click', () => (isOpen() ? closeMenu() : openMenu()));

  gmenu.addEventListener('click', (e) => {
    // リンク・ボタン以外のどこを押しても閉じる（ul/li/nav の余白も拾う）
    if (!e.target.closest || !e.target.closest('a,button')) closeMenu();
  });

  gmenu.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => closeMenu(false))
  );

  document.addEventListener('keydown', (e) => {
    if (!isOpen()) return;
    if (e.key === 'Escape') {
      e.preventDefault();
      closeMenu();
      return;
    }
    if (e.key !== 'Tab') return;
    const f = focusables();
    if (!f.length) return;
    f.push(toggle); // ハンバーガー（＝閉じるボタン）もトラップに含める
    const first = f[0];
    const last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });
})();

// 3) Reveal on scroll (Intersection Observer)
(function () {
  const els = document.querySelectorAll('.reveal');
  if (!els.length || !('IntersectionObserver' in window)) {
    els.forEach((el) => el.classList.add('is-in'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -10% 0px' }
  );
  els.forEach((el) => io.observe(el));
})();

// 4) FAQ accordion
(function () {
  document.querySelectorAll('.faq-item').forEach((item) => {
    const q = item.querySelector('.faq-q');
    if (!q) return;
    q.addEventListener('click', () => {
      item.classList.toggle('is-open');
      q.setAttribute(
        'aria-expanded',
        item.classList.contains('is-open') ? 'true' : 'false'
      );
    });
  });
})();

// 5) Smooth-anchor for in-page links
(function () {
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href').slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      // ヘッダーが fixed なので、その高さぶん手前で止める（潜り防止）
      const hd = document.querySelector('.header');
      const off = (hd ? hd.offsetHeight : 0) + 12;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - off, behavior: 'smooth' });
    });
  });
})();

// 6) Recruit FAB — always visible (常時表示)
(function () {
  const fab = document.getElementById('recruitFab');
  if (!fab) return;
  // 常に表示する：スクロールでの自動非表示・閉じる機能は撤去。
  // モバイルメニュー開閉中の一時非表示のみ、セクション2の is-nav-open で制御。
  fab.classList.add('is-ready');
})();
