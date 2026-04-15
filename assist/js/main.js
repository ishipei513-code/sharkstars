/* ============================================
   SHARKSTARS Official HP — Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  // --- Header Scroll Effect ---
  initHeaderScroll();

  // --- Hamburger Menu ---
  initHamburgerMenu();

  // --- Smooth Scroll (Nav Links) ---
  initSmoothScroll();

  // --- Gallery Filter Tabs ---
  initGalleryFilter();

  // --- FAQ Accordion ---
  initFaqAccordion();

  // --- Scroll Animations (Intersection Observer) ---
  initScrollAnimations();

  // --- Scroll To Top Button ---
  initScrollToTop();
});

/* ============================================
   Header Scroll Effect
   ============================================ */
function initHeaderScroll() {
  const header = document.querySelector('.header');
  if (!header) return;

  const onScroll = () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // Initial check
}

/* ============================================
   Hamburger Menu
   ============================================ */
function initHamburgerMenu() {
  const hamburger = document.querySelector('.hamburger');
  const nav = document.querySelector('.nav');
  const overlay = document.querySelector('.nav-overlay');
  if (!hamburger || !nav) return;

  const toggleMenu = () => {
    hamburger.classList.toggle('active');
    nav.classList.toggle('open');
    if (overlay) overlay.classList.toggle('active');
    document.body.style.overflow = nav.classList.contains('open') ? 'hidden' : '';
  };

  const closeMenu = () => {
    hamburger.classList.remove('active');
    nav.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = '';
  };

  hamburger.addEventListener('click', toggleMenu);
  if (overlay) overlay.addEventListener('click', closeMenu);

  // Close menu when a nav link is clicked
  nav.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', closeMenu);
  });
}

/* ============================================
   Smooth Scroll
   ============================================ */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const targetId = link.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (!target) return;

      e.preventDefault();
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    });
  });
}

/* ============================================
   Gallery Filter Tabs
   ============================================ */
function initGalleryFilter() {
  const tabs = document.querySelectorAll('.gallery-tab');
  const cards = document.querySelectorAll('.demo-card');
  const loadMoreBtn = document.querySelector('#gallery-load-more');
  if (!tabs.length || !cards.length) return;

  const INITIAL_SHOW = 8;

  function applyFilter(filter) {
    let visibleCount = 0;
    let totalMatch = 0;

    cards.forEach((card) => {
      const category = card.getAttribute('data-category');
      const isMatch = (filter === 'all' || category === filter);

      if (isMatch) {
        totalMatch++;
        if (visibleCount < INITIAL_SHOW) {
          card.classList.remove('hidden');
          card.style.animation = 'none';
          card.offsetHeight;
          card.style.animation = `fadeInUp 0.4s ease ${visibleCount * 0.05}s forwards`;
          visibleCount++;
        } else {
          card.classList.add('hidden');
        }
      } else {
        card.classList.add('hidden');
      }
    });

    // Show/hide load more button
    if (loadMoreBtn) {
      if (totalMatch > INITIAL_SHOW) {
        loadMoreBtn.style.display = 'inline-flex';
        loadMoreBtn.textContent = `もっと見る（残り${totalMatch - INITIAL_SHOW}件）`;
        loadMoreBtn.dataset.filter = filter;
      } else {
        loadMoreBtn.style.display = 'none';
      }
    }
  }

  // Tab click
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      applyFilter(tab.getAttribute('data-filter'));
    });
  });

  // Load more click
  if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', () => {
      const filter = loadMoreBtn.dataset.filter || 'all';
      cards.forEach((card, index) => {
        const category = card.getAttribute('data-category');
        const isMatch = (filter === 'all' || category === filter);
        if (isMatch && card.classList.contains('hidden')) {
          card.classList.remove('hidden');
          card.style.animation = 'none';
          card.offsetHeight;
          card.style.animation = `fadeInUp 0.4s ease ${index * 0.03}s forwards`;
        }
      });
      loadMoreBtn.style.display = 'none';
    });
  }

  // Initial load
  applyFilter('all');
}

/* ============================================
   FAQ Accordion
   ============================================ */
function initFaqAccordion() {
  const questions = document.querySelectorAll('.faq-question');
  if (!questions.length) return;

  questions.forEach(question => {
    question.addEventListener('click', () => {
      const item = question.closest('.faq-item');
      const isActive = item.classList.contains('active');

      // Close all other items
      document.querySelectorAll('.faq-item.active').forEach(activeItem => {
        if (activeItem !== item) {
          activeItem.classList.remove('active');
        }
      });

      // Toggle current item
      item.classList.toggle('active', !isActive);
    });
  });
}

/* ============================================
   Scroll Animations (Intersection Observer)
   ============================================ */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.fade-in');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -40px 0px'
  });

  elements.forEach(el => observer.observe(el));
}

/* ============================================
   Scroll To Top Button
   ============================================ */
function initScrollToTop() {
  const btn = document.querySelector('.scroll-top');
  if (!btn) return;

  const onScroll = () => {
    if (window.scrollY > 500) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/* ============================================
   Contact Form (Frontend Only)
   ============================================ */
const contactForm = document.querySelector('#contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Simple validation
    const name = contactForm.querySelector('#contact-name');
    const email = contactForm.querySelector('#contact-email');
    const message = contactForm.querySelector('#contact-message');

    if (!name.value.trim() || !email.value.trim() || !message.value.trim()) {
      alert('必須項目をご入力ください。');
      return;
    }

    // Show success message (frontend only)
    alert('お問い合わせありがとうございます！\n2営業日以内にご返信いたします。');
    contactForm.reset();
  });
}
