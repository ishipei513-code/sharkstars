import re

html_path = r'd:\sharkstars\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_hero_pattern = r'<section class="hero" id="hero">.*?</section>'
new_hero = """<section class="hero" id="hero">
    <!-- Background Image -->
    <div class="hero-bg">
      <img src="assist/images/main_hero_bg.png" alt="SHARKSTARS Web Design" loading="eager">
      <div class="hero-overlay"></div>
    </div>

    <div class="container">
      <div class="hero-content text-center text-white">
        <!-- Badge -->
        <div class="hero-badge hero-badge-dark fade-in">
          ＼ 専門知識は一切不要 ／
        </div>

        <!-- Main Copy -->
        <h1 class="hero-title fade-in delay-1">
          初期費用0円。<br>
          あなたのお店に、<br>
          プロ品質のWebサイトを。
        </h1>

        <p class="hero-subtitle fade-in delay-2">
          ずっと月額5,000円（税込5,500円）のみ。サーバー代も、面倒な保守管理もすべてお任せください。<br>
          50種類以上のデザインから選ぶだけで、1週間前後であなたのビジネスがWeb上に誕生します。
        </p>

        <!-- CTA Buttons -->
        <div class="hero-buttons justify-center fade-in delay-3">
          <a href="#gallery" class="btn-primary" id="hero-cta-gallery">
            デザイン一覧を見る
          </a>
          <a href="#contact" class="btn-secondary btn-outline-white" id="hero-cta-contact">
            お問い合わせ
          </a>
        </div>
      </div>
    </div>
  </section>"""

text = re.sub(old_hero_pattern, new_hero, text, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

css_path = r'd:\sharkstars\assist\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# I will append the NEW css to the END of the file to override existing styles safely
new_css = """
/* --- OVERRIDE HERO FOR FULL BACKGROUND COOL LAYOUT --- */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex !important;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding-top: var(--header-height);
  background-color: #111 !important;
}
.hero-bg {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 0;
}
.hero-bg img {
  width: 100%;
  height: 100% !important;
  object-fit: cover !important;
  opacity: 1 !important;
  transform: scale(1.05); /* Slight scale for breathing effect or just robust cover */
}
.hero-overlay {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: linear-gradient(135deg, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 100%);
  z-index: 1;
}
.hero .container {
  position: relative;
  z-index: 2;
  width: 100%;
  display: flex !important;
  justify-content: center !important;
}
.hero-content {
  width: 100% !important;
  max-width: 800px !important;
  padding-right: 0 !important;
}
.hero-content.text-center {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.hero-content.text-white .hero-title {
  color: #fff !important;
  text-shadow: 0 4px 20px rgba(0,0,0,0.5);
  font-size: clamp(2.5rem, 6vw, 4.5rem) !important;
  line-height: 1.3 !important;
}
.hero-content.text-white .hero-subtitle {
  color: #ddd !important;
  text-shadow: 0 2px 10px rgba(0,0,0,0.3);
  font-size: 1.1rem !important;
}
.hero-badge-dark {
  background: rgba(255,255,255,0.1) !important;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.3) !important;
  color: #fff !important;
  margin: 0 auto 32px auto !important;
  width: fit-content;
}
.hero-buttons.justify-center {
  justify-content: center !important;
  margin-top: 40px !important;
}
.btn-outline-white {
  background: rgba(255,255,255,0.1) !important;
  backdrop-filter: blur(5px);
  color: #fff !important;
  border: 1px solid rgba(255,255,255,0.3) !important;
}
.btn-outline-white:hover {
  background: rgba(255,255,255,0.2) !important;
  border-color: #fff !important;
  color: #fff !important;
}

@media (max-width: 768px) {
  .hero {
    min-height: 80vh !important;
    padding-top: calc(var(--header-height) + 40px) !important;
  }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css)

print("Hero section updated to full-width background.")
