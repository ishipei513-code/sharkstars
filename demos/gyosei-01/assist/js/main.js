document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.querySelector('.hamburger');
  const navList = document.querySelector('.nav-list');
  if (hamburger) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      navList.classList.toggle('open');
    });
    navList.querySelectorAll('.nav-link').forEach(l => l.addEventListener('click', () => {
      hamburger.classList.remove('active');
      navList.classList.remove('open');
    }));
  }

  // FAQ accordion
  document.querySelectorAll('.faq-question').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq-item');
      document.querySelectorAll('.faq-item.active').forEach(a => { if (a !== item) a.classList.remove('active'); });
      item.classList.toggle('active');
    });
  });

  // Fade-in
  const fadeEls = document.querySelectorAll('.fade-in');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.15 });
  fadeEls.forEach(el => obs.observe(el));
});

