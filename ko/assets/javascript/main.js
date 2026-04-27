/* ============================================
   KOJP — Main JavaScript
   - Intersection Observer scroll animations
   - Number counter animation
   - Smooth scroll
   - Accordion control
   - Mobile menu toggle
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations();
  initCounters();
  initAccordions();
  initMobileMenu();
  initHeaderScroll();
});


/* ── Scroll Animations (Intersection Observer) ── */

function initScrollAnimations() {
  const animatedElements = document.querySelectorAll(
    '.fade-up, .fade-left, .fade-right, .scale-in, .card-grid, .stagger'
  );

  if (!animatedElements.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  animatedElements.forEach((el) => observer.observe(el));
}


/* ── Number Counter Animation ──────────────── */

function animateCount(el, target, duration = 1500) {
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  let start = 0;
  const increment = target / (duration / 16);
  const timer = setInterval(() => {
    start += increment;
    if (start >= target) {
      start = target;
      clearInterval(timer);
    }
    el.textContent = prefix + Math.floor(start).toLocaleString() + suffix;
  }, 16);
}

function initCounters() {
  const counters = document.querySelectorAll('[data-count]');
  if (!counters.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const target = parseInt(entry.target.dataset.count, 10);
          const duration = parseInt(entry.target.dataset.duration, 10) || 1500;
          animateCount(entry.target, target, duration);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );

  counters.forEach((el) => observer.observe(el));
}


/* ── Accordion ─────────────────────────────── */

function initAccordions() {
  const triggers = document.querySelectorAll('.accordion__trigger');
  if (!triggers.length) return;

  triggers.forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.accordion__item');
      const isOpen = item.classList.contains('is-open');

      // Close all siblings
      const accordion = item.closest('.accordion');
      if (accordion) {
        accordion.querySelectorAll('.accordion__item').forEach((sibling) => {
          sibling.classList.remove('is-open');
        });
      }

      // Toggle current
      if (!isOpen) {
        item.classList.add('is-open');
      }
    });
  });
}


/* ── Mobile Menu Toggle ────────────────────── */

function initMobileMenu() {
  const toggle = document.querySelector('.header__menu-toggle');
  const nav = document.querySelector('.header__nav');
  const overlay = document.querySelector('.header__overlay');

  if (!toggle || !nav) return;

  function openMenu() {
    nav.classList.add('is-open');
    toggle.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    if (overlay) overlay.classList.add('is-open');
  }

  function closeMenu() {
    nav.classList.remove('is-open');
    toggle.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    if (overlay) overlay.classList.remove('is-open');
  }

  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.contains('is-open');
    isOpen ? closeMenu() : openMenu();
  });

  if (overlay) {
    overlay.addEventListener('click', closeMenu);
  }

  // Close on nav link click (mobile)
  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('is-open')) {
      closeMenu();
    }
  });
}


/* ── Header Scroll Effect ──────────────────── */

function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  let lastScrollY = 0;
  let ticking = false;

  function updateHeader() {
    const scrollY = window.scrollY;

    // Toggle scrolled state (shadow + reduced height)
    if (scrollY > 50) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }

    // Hide header on scroll down past 200px, show on scroll up
    if (scrollY > 200) {
      if (scrollY > lastScrollY + 4) {
        header.classList.add('is-hidden');
      } else if (scrollY < lastScrollY - 4) {
        header.classList.remove('is-hidden');
      }
    } else {
      header.classList.remove('is-hidden');
    }

    lastScrollY = scrollY;
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateHeader);
      ticking = true;
    }
  }, { passive: true });
}


/* ── Respect reduced-motion in JS animations ── */

const REDUCE_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
