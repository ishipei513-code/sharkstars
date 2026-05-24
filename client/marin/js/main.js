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

// 6) Recruit FAB — dismiss + in-view hide (top page only)
(function () {
  const fab = document.getElementById('recruitFab');
  if (!fab) return;

  const SESSION_KEY = 'marinRecruitFabClosed';

  // If already dismissed this session, hide immediately (no animation flash)
  if (sessionStorage.getItem(SESSION_KEY)) {
    fab.classList.add('is-hidden');
    return;
  }

  // FAB is shown — make it visible (both normal and reduced-motion paths)
  fab.classList.add('is-ready');

  // Close button — dismiss for the session
  const closeBtn = fab.querySelector('.recruit-fab-close');
  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      fab.classList.add('is-hidden');
      sessionStorage.setItem(SESSION_KEY, '1');
    });
  }

  // Top-page only: hide FAB while #recruit section is in view
  const recruitSection = document.getElementById('recruit');
  if (recruitSection && 'IntersectionObserver' in window) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          // Only toggle visibility if user has not dismissed
          if (sessionStorage.getItem(SESSION_KEY)) return;
          if (e.isIntersecting) {
            fab.classList.add('is-hidden');
          } else {
            fab.classList.remove('is-hidden');
          }
        });
      },
      { threshold: 0.15 }
    );
    sectionObserver.observe(recruitSection);
  }
})();
