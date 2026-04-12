document.addEventListener('DOMContentLoaded', () => {
  // Header scroll
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 50);
  }, { passive: true });

  // Hamburger
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

  // Fade-in on scroll
  const fadeEls = document.querySelectorAll('.fade-in');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.15 });
  fadeEls.forEach(el => obs.observe(el));
});

