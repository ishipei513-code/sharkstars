import os

const_html = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>匠工房 | デザインリフォーム・建築</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital@0;1&family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assist/css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  <nav class="nav" id="nav">
    <div class="nav-container">
      <div class="logo">匠工房</div>
      <div class="nav-links">
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#works">Works</a>
        <a href="#contact" class="btn-primary-sm">ご相談</a>
      </div>
    </div>
  </nav>

  <section class="hero">
    <div class="container hero-inner">
      <div class="hero-content">
        <h1 class="hero-title fade-up">空間に、<br><span class="italic-serif">Craft</span> の息吹を。</h1>
        <p class="hero-desc fade-up delay-1">長年培った確かな技術と、現代のライフスタイルに寄り添うデザインで、あなたの理想の空間を形にします。</p>
        <div class="fade-up delay-2">
          <a href="#works" class="cta-link">施工事例を見る <i data-lucide="arrow-right"></i></a>
        </div>
      </div>
      <div class="hero-img-wrapper fade-up delay-1">
        <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80" alt="建築" class="hero-img">
      </div>
    </div>
  </section>

  <section class="section bg-white" id="services">
    <div class="container">
      <div class="section-badge fade-up">OUR EXPERTISE</div>
      <h2 class="section-title fade-up delay-1">技術とデザインの融合</h2>
      <div class="services-grid">
        <div class="service-card fade-up">
          <div class="service-icon"><i data-lucide="home"></i></div>
          <h3>フルリノベーション</h3>
          <p>スケルトン状態からの全面改装。間取り変更からインテリアデザインまでトータルでプロデュースします。</p>
        </div>
        <div class="service-card fade-up delay-1">
          <div class="service-icon"><i data-lucide="paint-roller"></i></div>
          <h3>部分リフォーム</h3>
          <p>キッチン、バスルームなどの水回りや、リビングの部分的な改修。少しの変化で暮らしの質を上げます。</p>
        </div>
        <div class="service-card fade-up delay-2">
          <div class="service-icon"><i data-lucide="pen-tool"></i></div>
          <h3>オーダー家具</h3>
          <p>空間にぴったりと収まる造作家具。職人の手仕事による温もりある仕上がりをお約束します。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="works">
    <div class="container">
      <div class="section-badge fade-up">PORTFOLIO</div>
      <h2 class="section-title fade-up delay-1">施工事例</h2>
      <div class="works-grid">
        <div class="work-item fade-up">
          <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Work 1">
          <div class="work-info">
            <h4>Modern House</h4><p>戸建て全面改装</p>
          </div>
        </div>
        <div class="work-item fade-up delay-1">
          <img src="https://images.unsplash.com/photo-1484154218962-a197022b5858?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Work 2">
          <div class="work-info">
            <h4>Nordic Kitchen</h4><p>キッチンリフォーム</p>
          </div>
        </div>
        <div class="work-item fade-up delay-2">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Work 3">
          <div class="work-info">
            <h4>Cozy Living</h4><p>リビング・ダイニング改修</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer-flex">
      <div class="footer-logo">匠工房</div>
      <p class="footer-copy">&copy; TAKUMI KOUBOU. All Rights Reserved.</p>
    </div>
  </footer>

  <script>
    lucide.createIcons();
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
  </script>
</body>
</html>
"""

const_css = """
:root {
  --bg-color: #fafafa;
  --text-main: #111827;
  --text-muted: #6b7280;
  --accent: #b45309; /* Warm amber/brown */
  --surface: #ffffff;
  --font-base: 'Noto Sans JP', sans-serif;
  --font-serif: 'Playfair Display', serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-base);
  background-color: var(--bg-color);
  color: var(--text-main);
  line-height: 1.8;
  overflow-x: hidden;
  font-weight: 300;
}

.container { width: 100%; max-width: 1280px; margin: 0 auto; padding: 0 5%; }
.section { padding: 140px 0; }
.bg-white { background-color: var(--surface); }

/* Nav */
.nav {
  position: fixed; top: 0; left: 0; width: 100%; z-index: 100;
  padding: 32px 0; transition: all 0.4s ease;
}
.nav.scrolled {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px); padding: 20px 0;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}
.nav-container {
  display: flex; justify-content: space-between; align-items: center;
  max-width: 1280px; margin: 0 auto; padding: 0 5%;
}
.logo { font-size: 1.4rem; font-weight: 700; letter-spacing: 0.1em; color: var(--text-main); }
.nav-links { display: flex; align-items: center; gap: 40px; }
.nav-links a { color: var(--text-main); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: opacity 0.3s; }
.nav-links a:hover { opacity: 0.6; }
.btn-primary-sm {
  background: var(--text-main); color: #fff !important; padding: 10px 24px; border-radius: 100px;
}
.btn-primary-sm:hover { opacity: 0.9 !important; background: var(--accent); }

/* Hero */
.hero { min-height: 100vh; display: flex; align-items: center; padding-top: 80px; }
.hero-inner { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; }
.hero-title { font-size: clamp(2.5rem, 5vw, 4.5rem); font-weight: 300; line-height: 1.2; margin-bottom: 32px; letter-spacing: -0.02em; }
.italic-serif { font-family: var(--font-serif); font-style: italic; font-weight: 400; color: var(--accent); }
.hero-desc { font-size: 1.1rem; color: var(--text-muted); margin-bottom: 48px; max-width: 480px; }
.cta-link {
  display: inline-flex; align-items: center; gap: 12px; font-weight: 500; color: var(--text-main); text-decoration: none;
  font-size: 1.1rem; border-bottom: 1px solid var(--text-main); padding-bottom: 4px; transition: color 0.3s, border-color 0.3s;
}
.cta-link:hover { color: var(--accent); border-color: var(--accent); }
.hero-img-wrapper { aspect-ratio: 4/5; border-radius: 200px 200px 0 0; overflow: hidden; box-shadow: 0 30px 60px rgba(0,0,0,0.1); }
.hero-img { width: 100%; height: 100%; object-fit: cover; }

/* Sections */
.section-badge { font-family: var(--font-serif); font-size: 0.8rem; letter-spacing: 0.2em; color: var(--accent); margin-bottom: 16px; text-transform: uppercase; }
.section-title { font-size: 2.5rem; font-weight: 300; margin-bottom: 64px; }

/* Services */
.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
.service-card { padding: 48px; border-radius: 24px; background: var(--bg-color); transition: transform 0.4s; }
.service-card:hover { transform: translateY(-8px); background: #f3f4f6; }
.service-icon { width: 48px; height: 48px; color: var(--accent); margin-bottom: 24px; }
.service-icon svg { width: 100%; height: 100%; stroke-width: 1.5; }
.service-card h3 { font-size: 1.3rem; font-weight: 500; margin-bottom: 16px; }
.service-card p { font-size: 0.95rem; color: var(--text-muted); }

/* Works */
.works-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
.work-item { group; cursor: pointer; }
.work-item img {
  width: 100%; aspect-ratio: 4/5; object-fit: cover; border-radius: 16px;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}
.work-item:hover img { transform: scale(1.03); box-shadow: 0 20px 40px rgba(0,0,0,0.1); }
.work-info { margin-top: 24px; text-align: center; }
.work-info h4 { font-size: 1.1rem; font-weight: 500; margin-bottom: 4px; }
.work-info p { font-size: 0.85rem; color: var(--text-muted); }

/* Footer */
.footer { padding: 64px 0; border-top: 1px solid rgba(0,0,0,0.05); background: var(--surface); }
.footer-flex { display: flex; justify-content: space-between; align-items: center; }
.footer-logo { font-size: 1.2rem; font-weight: 700; }
.footer-copy { font-size: 0.8rem; color: var(--text-muted); }

/* Utilities */
.fade-up { opacity: 0; transform: translateY(40px); transition: opacity 1s ease, transform 1s cubic-bezier(0.16, 1, 0.3, 1); }
.fade-up.in-view { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.15s; }
.delay-2 { transition-delay: 0.3s; }

@media (max-width: 768px) {
  .hero-inner { grid-template-columns: 1fr; gap: 40px; }
  .hero { padding-top: 120px; }
  .hero-img-wrapper { aspect-ratio: 1/1; border-radius: 50%; }
  .services-grid, .works-grid { grid-template-columns: 1fr; }
  .nav-links { display: none; }
  .footer-flex { flex-direction: column; gap: 24px; text-align: center; }
}
"""

with open(r'd:\sharkstars\demos\construction-01\index.html', 'w', encoding='utf-8') as f:
    f.write(const_html.strip())

with open(r'd:\sharkstars\demos\construction-01\assist\css\style.css', 'w', encoding='utf-8') as f:
    f.write(const_css.strip())

print("Construction-01 rewritten to 500% premium quality.")
