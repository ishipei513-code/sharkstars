import os

denki_html = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>サンライズ電気工事 | 24時間緊急対応</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assist/css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  <!-- Navigation -->
  <nav class="nav" id="nav">
    <div class="nav-container">
      <div class="logo">
        <i data-lucide="zap" class="logo-icon"></i>
        <span>SUNRISE ELECTRIC</span>
      </div>
      <div class="nav-links">
        <a href="#services">Services</a>
        <a href="#works">Works</a>
        <a href="#contact" class="btn-outline">緊急連絡</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-bg">
      <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="電気工事" class="hero-img">
      <div class="hero-overlay"></div>
    </div>
    <div class="hero-content">
      <div class="badge fade-up">24/7 EMERGENCY SERVICE</div>
      <h1 class="hero-title fade-up delay-1">光を灯し、<br>未来を繋ぐ。</h1>
      <p class="hero-subtitle fade-up delay-2">確かな技術で、皆様の安全で快適な暮らしを支える電気工事のプロフェッショナル集団。</p>
      <div class="hero-actions fade-up delay-3">
        <a href="#contact" class="btn-primary">お見積り・ご相談</a>
      </div>
    </div>
  </section>

  <!-- Services / Features -->
  <section class="section" id="services">
    <div class="container">
      <div class="section-header fade-up">
        <h2 class="section-title">OUR EXPERTISE</h2>
        <p class="section-desc">妥協のないプロの仕事をお約束します。</p>
      </div>
      <div class="features-grid">
        <div class="feature-card fade-up">
          <div class="feature-icon"><i data-lucide="shield-check"></i></div>
          <h3>有資格者による施工</h3>
          <p>経験豊富な第一種電気工事士が責任を持って対応します。安全第一の確実な施工をお約束します。</p>
        </div>
        <div class="feature-card fade-up delay-1">
          <div class="feature-icon"><i data-lucide="clock"></i></div>
          <h3>24時間365日対応</h3>
          <p>突然の停電や漏電など、緊急のトラブルにも迅速に駆けつけます。深夜のトラブルもお任せください。</p>
        </div>
        <div class="feature-card fade-up delay-2">
          <div class="feature-icon"><i data-lucide="check-circle-2"></i></div>
          <h3>明朗な会計システム</h3>
          <p>作業前に必ずお見積りを提示し、ご納得いただいてから作業を開始いたします。不透明な追加費用はありません。</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Works -->
  <section class="section split-bg" id="works">
    <div class="container">
      <div class="section-header fade-up">
        <h2 class="section-title">LATEST WORKS</h2>
        <p class="section-desc">多数の施工実績が信頼の証です。</p>
      </div>
      <div class="gallery-grid">
        <div class="gallery-item fade-up">
          <img src="https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="実績1">
        </div>
        <div class="gallery-item fade-up delay-1">
          <img src="https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="実績2">
        </div>
        <div class="gallery-item fade-up delay-2">
          <img src="https://images.unsplash.com/photo-1574680096145-d05b474e2155?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="実績3">
        </div>
        <div class="gallery-item fade-up delay-3">
          <img src="https://images.unsplash.com/photo-1542361345-89e58247f2d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="実績4">
        </div>
      </div>
    </div>
  </section>

  <!-- Footer CTA -->
  <section class="section cta-section" id="contact">
    <div class="cta-box fade-up">
      <h2>電気のトラブル、今すぐ解決します。</h2>
      <p>ご相談・お見積りは無料です。</p>
      <a href="#" class="btn-primary large"><i data-lucide="phone"></i> 0120-XXX-XXX</a>
    </div>
  </section>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 SUNRISE ELECTRIC. All rights reserved.</p>
    </div>
  </footer>

  <script>
    lucide.createIcons();
    
    // Navbar scroll effect
    const nav = document.getElementById('nav');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    });

    // Reveal animations
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

denki_css = """
:root {
  --bg-color: #030712;
  --surface: #111827;
  --surface-light: #1f2937;
  --text-main: #f9fafb;
  --text-muted: #9ca3af;
  --accent-1: #0ea5e9;
  --accent-2: #10b981;
  --font-sans: 'Inter', 'Noto Sans JP', sans-serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--font-sans);
  background-color: var(--bg-color);
  color: var(--text-main);
  line-height: 1.6;
  overflow-x: hidden;
}

.container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 5%; }
.section { padding: 120px 0; }

/* Navigation */
.nav {
  position: fixed; top: 0; left: 0; width: 100%; z-index: 100;
  transition: all 0.4s ease; padding: 24px 0;
}
.nav.scrolled {
  background: rgba(3, 7, 18, 0.8);
  backdrop-filter: blur(12px);
  padding: 16px 0;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.nav-container {
  display: flex; justify-content: space-between; align-items: center;
  max-width: 1200px; margin: 0 auto; padding: 0 5%;
}
.logo {
  display: flex; align-items: center; gap: 8px; font-weight: 800; font-size: 1.2rem;
  letter-spacing: 0.05em; background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.logo-icon { color: var(--accent-1); }
.nav-links { display: flex; align-items: center; gap: 32px; }
.nav-links a {
  color: var(--text-main); text-decoration: none; font-size: 0.9rem;
  font-weight: 600; transition: color 0.3s;
}
.nav-links a:hover { color: var(--accent-1); }
.btn-outline {
  border: 1px solid rgba(255,255,255,0.2); border-radius: 100px;
  padding: 8px 20px; transition: all 0.3s !important;
}
.btn-outline:hover { background: #fff; color: #000 !important; }

/* Buttons */
.btn-primary {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
  color: #fff; text-decoration: none; font-weight: 700; border-radius: 100px;
  padding: 16px 36px; font-size: 1.1rem; transition: transform 0.3s, box-shadow 0.3s;
  box-shadow: 0 10px 20px rgba(14, 165, 233, 0.2);
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 15px 30px rgba(14, 165, 233, 0.3);
}
.btn-primary.large { font-size: 1.3rem; padding: 20px 48px; }

/* Hero */
.hero { height: 100vh; position: relative; display: flex; align-items: center; }
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-img { width: 100%; height: 100%; object-fit: cover; opacity: 0.6; }
.hero-overlay {
  position: absolute; inset: 0;
  background: radial-gradient(circle at center, rgba(3,7,18,0.2) 0%, rgba(3,7,18,0.8) 100%), linear-gradient(180deg, rgba(3,7,18,0.4) 0%, rgba(3,7,18,1) 100%);
}
.hero-content { position: relative; z-index: 1; max-width: 1200px; margin: 0 auto; padding: 0 5%; width: 100%; }
.badge {
  display: inline-block; padding: 6px 16px; border-radius: 100px; background: rgba(255,255,255,0.1);
  backdrop-filter: blur(4px); font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em;
  margin-bottom: 24px; border: 1px solid rgba(255,255,255,0.1);
}
.hero-title { font-size: clamp(3rem, 8vw, 5.5rem); font-weight: 900; line-height: 1.1; margin-bottom: 24px; letter-spacing: -0.02em; }
.hero-subtitle { font-size: clamp(1rem, 2vw, 1.25rem); color: var(--text-muted); max-width: 600px; margin-bottom: 40px; }

/* Sections */
.section-header { text-align: center; margin-bottom: 64px; }
.section-title { font-size: 2.5rem; font-weight: 900; margin-bottom: 16px; letter-spacing: -0.02em; }
.section-desc { font-size: 1.1rem; color: var(--text-muted); }

/* Features */
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; }
.feature-card {
  background: var(--surface); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px;
  padding: 40px; transition: transform 0.4s, background 0.4s;
}
.feature-card:hover {
  transform: translateY(-8px); background: var(--surface-light);
  border-color: rgba(14,165,233,0.3);
}
.feature-icon {
  width: 56px; height: 56px; border-radius: 16px; display: flex; align-items: center; justify-content: center;
  background: rgba(14,165,233,0.1); color: var(--accent-1); margin-bottom: 24px;
}
.feature-icon svg { width: 28px; height: 28px; }
.feature-card h3 { font-size: 1.4rem; margin-bottom: 16px; font-weight: 800; }
.feature-card p { color: var(--text-muted); line-height: 1.7; font-size: 0.95rem; }

/* Works */
.split-bg { background: linear-gradient(to bottom, var(--bg-color) 50%, var(--surface) 50%); }
.gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; }
.gallery-item {
  border-radius: 24px; overflow: hidden; aspect-ratio: 4/3; position: relative;
  box-shadow: 0 20px 40px rgba(0,0,0,0.4);
}
.gallery-item img {
  width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}
.gallery-item:hover img { transform: scale(1.05); }

/* CTA */
.cta-section { background: var(--surface); }
.cta-box {
  background: linear-gradient(135deg, var(--surface-light), var(--surface));
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 32px; padding: 80px 40px; text-align: center; max-width: 800px; margin: 0 auto;
}
.cta-box h2 { font-size: 2.5rem; margin-bottom: 16px; }
.cta-box p { color: var(--text-muted); font-size: 1.1rem; margin-bottom: 40px; }

/* Footer */
.footer { border-top: 1px solid rgba(255,255,255,0.05); padding: 40px 0; text-align: center; color: var(--text-muted); font-size: 0.9rem; }

/* Animations */
.fade-up { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.16, 1, 0.3, 1); }
.fade-up.in-view { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.1s; }
.delay-2 { transition-delay: 0.2s; }
.delay-3 { transition-delay: 0.3s; }

@media (max-width: 768px) {
  .gallery-grid { grid-template-columns: 1fr; }
  .nav-links { display: none; } /* Simplified for demo */
}
"""

with open(r'd:\sharkstars\demos\denki-01\index.html', 'w', encoding='utf-8') as f:
    f.write(denki_html.strip())

with open(r'd:\sharkstars\demos\denki-01\assist\css\style.css', 'w', encoding='utf-8') as f:
    f.write(denki_css.strip())

print("Denki-01 rewritten to 500% premium quality.")
