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

// 2) Mobile menu toggle
(function () {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
    const fab = document.getElementById('recruitFab');
    if (fab) fab.classList.toggle('is-nav-open', open);
  });
  nav.querySelectorAll('a').forEach((a) =>
    a.addEventListener('click', () => {
      nav.classList.remove('is-open');
      toggle.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      const fab = document.getElementById('recruitFab');
      if (fab) fab.classList.remove('is-nav-open');
    })
  );
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
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
