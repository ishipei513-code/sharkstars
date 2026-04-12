import os

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Belle | 表参道の完全個室プライベートサロン</title>
  <meta name="description" content="表参道駅から徒歩3分。完全個室・マンツーマン施術のラグジュアリーサロン「Belle」。ダメージレスな髪質改善から、あなただけの似合わせカットまで。非日常的な極上の時間をお過ごしください。">
  
  <!-- Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Shippori+Mincho:wght@400;500;600;800&family=Noto+Sans+JP:wght@300;400;500&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="assist/css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  
  <!-- Header -->
  <header class="header" id="header">
    <div class="h-container">
      <div class="logo">
        <span class="logo-en">Belle</span>
      </div>
      <nav class="nav">
        <ul class="nav-links">
          <li><a href="#concept">Concept</a></li>
          <li><a href="#menu">Menu</a></li>
          <li><a href="#style">Style Gallery</a></li>
          <li><a href="#flow">Flow</a></li>
          <li><a href="#faq">FAQ</a></li>
        </ul>
        <a href="#contact" class="btn btn-nav">ご予約はこちら</a>
      </nav>
      <button class="menu-toggle" id="menuToggle" aria-label="メニューを開く">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-bg">
      <img src="https://images.unsplash.com/photo-1521590832167-7bfc620cb6b2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="エレガントなサロンスタイル">
    </div>
    <div class="hero-mask"></div>
    <div class="hero-content fade-target">
      <div class="vertical-text">
        <p class="hero-en">Private Salon in Omotesando</p>
        <h1 class="hero-title">「私らしい」<br>美しさを引き出す、<br><span class="hero-hl">特別な空間。</span></h1>
        <p class="hero-subtitle">日常の喧騒から離れた完全個室で、<br>髪から始まるあなただけのストーリーを。</p>
      </div>
      <div class="scroll-down">
        <span>SCROLL</span>
        <div class="line"></div>
      </div>
    </div>
  </section>

  <!-- Trouble Section -->
  <section class="section trouble" id="trouble">
    <div class="l-container">
      <div class="trouble-box fade-target">
        <h2 class="sect-heading center">美容室選びで、こんなお悩みはありませんか？</h2>
        <div class="t-list">
          <div class="t-item fade-target delay-1">
            <div class="t-icon">01</div>
            <p><strong>周りの目が気になる</strong><br>大型店特有のガヤガヤした雰囲気や、隣のお客さんの目が気になってリラックスできない…</p>
          </div>
          <div class="t-item fade-target delay-2">
            <div class="t-icon">02</div>
            <p><strong>髪のパサつき・広がり</strong><br>毎日のコテやカラーの繰り返しで、髪が傷んでツヤがない。年齢によるうねりも気になる…</p>
          </div>
          <div class="t-item fade-target delay-3">
            <div class="t-icon">03</div>
            <p><strong>要望が伝わらない</strong><br>いつも「似合うスタイル」が分からずお任せにしてしまうが、仕上がりに満足できない…</p>
          </div>
        </div>
        <div class="t-answer fade-target delay-1">
          <p><strong>Belleは、そんな大人女性の悩みに徹底的に寄り添う「完全個室・マンツーマン」のラグジュアリーサロンです。</strong></p>
        </div>
      </div>
    </div>
  </section>

  <!-- Philosophy -->
  <section class="section philosophy" id="concept">
    <div class="l-container">
      <div class="phil-wrap">
        <div class="phil-text fade-target">
          <span class="en-label">C O N C E P T</span>
          <h2 class="sect-heading">髪を通じて、<br>心まで満ちる時間を。</h2>
          <div class="desc">
            <p>私たちは、ただ髪を切ったり染めたりするだけの場所ではありません。「美容室での時間が、最高のリフレッシュになるように」という想いから、完全プライベートの設計にこだわりました。</p>
            <p>最初のカウンセリングから、シャンプー、カット、仕上げに至るまで、アシスタント任せにせず一人のトップスタイリストが専属で担当いたします。途中で人が入れ替わる煩わしさはありません。</p>
            <p>使用する薬剤は、オーガニックの国際認証を受けた最高級品のみ。一人ひとりの骨格・髪質を見極めた「洗練された似合わせ」と、思わず触れたくなるような「極上の艶髪」をお約束します。</p>
          </div>
        </div>
        <div class="phil-img fade-target offset-delay">
          <img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="丁寧なカウンセリング風景">
          <div class="badge">完全<br><span class="num">個室</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Service List -->
  <section class="section service bg-gray" id="menu">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">M E N U</span>
        <h2 class="sect-heading">メニュー・料金</h2>
        <p>※以下は代表的なメニューの一部です。全メニュースパシャンプー・ブロー込みの明朗会計です。</p>
      </div>

      <div class="srv-grid">
        <div class="srv-card fade-target">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1522337660859-02fbefca4702?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="似合わせカット">
          </div>
          <div class="srv-body">
            <h3><span class="en">Cut</span> 骨格矯正・似合わせカット</h3>
            <p>頭の形や顔の輪郭を計算し、360度どこから見ても美しいシルエットを創り出します。ご自宅での再現性の高さも特徴です。</p>
            <div class="price"><span>¥7,700</span> (税込)</div>
          </div>
        </div>
        
        <div class="srv-card fade-target delay-1">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="プレミアムカラー">
          </div>
          <div class="srv-body">
            <h3><span class="en">Color</span> プレミアム透明感カラー</h3>
            <p>ダメージを最小限に抑えるケアカラー。赤みを消した透明感のあるアッシュや、上品で艶やかなグレージュが得意です。</p>
            <div class="price"><span>¥11,000</span> (税込)</div>
          </div>
        </div>

        <div class="srv-card fade-target delay-2">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1515377905703-c4788e51af15?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="髪質改善トリートメント">
          </div>
          <div class="srv-body">
            <h3><span class="en">Treatment</span> 髪質改善トリートメント</h3>
            <p>うねりやパサつきの根本原因にアプローチ。髪の内部に栄養を閉じ込め、シルクのような滑らかな艶髪へと導きます。</p>
            <div class="price"><span>¥9,900</span> (税込)</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Works -->
  <section class="section works" id="style">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">S T Y L E   G A L L E R Y</span>
        <h2 class="sect-heading">スタイルギャラリー</h2>
      </div>

      <div class="works-wrap">
        <div class="work-item fade-target">
          <div class="wa-img">
            <div class="ba-tag">大人ショートボブ</div>
            <img src="https://images.unsplash.com/photo-1519699047748-de8e457a634e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="スタイル事例1">
          </div>
          <div class="wa-text">
            <h3>首元を美しく魅せる、大人のための洗練ショートボブ</h3>
            <p>「ロングからばっさり切りたいけれど似合うか不安」というお客様。お顔の輪郭に合わせてサイドの長さをミリ単位で調整し、小顔効果抜群のショートボブをご提案しました。朝のスタイリングもオイルを馴染ませるだけで決まる、忙しい大人女性に大人気のスタイルです。</p>
          </div>
        </div>

        <div class="work-item reverse fade-target delay-1">
          <div class="wa-img">
            <div class="ba-tag">オリーブグレージュ</div>
            <img src="https://images.unsplash.com/photo-1620601633519-21a42b0c3639?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="スタイル事例2">
          </div>
          <div class="wa-text">
            <h3>光に透けるような透明感。赤みを抑えたオリーブグレージュ</h3>
            <p>髪の赤みやオレンジ味がすぐに出てしまうというお悩みに対し、寒色系のオリーブをブレンドした特製カラーを施術。ブリーチなしでも、光に当たると透けるような柔らかさと透明感を実現しました。併せて実施した髪質改善トリートメントにより、思わず触れたくなる艶が蘇りました。</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Flow -->
  <section class="section flow bg-gray" id="flow">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">F L O W</span>
        <h2 class="sect-heading">ご来店からの流れ</h2>
      </div>

      <div class="flow-list">
        <div class="flow-card fade-target">
          <div class="f-num">01</div>
          <div class="f-content">
            <h3>丁寧なカウンセリング（約15分）</h3>
            <p>ウェルカムドリンクをお出しし、髪のお悩みや理想のスタイルをしっかりお伺いします。過去の失敗談や、言葉にしづらいニュアンスも丁寧に汲み取ります。</p>
          </div>
        </div>
        <div class="flow-card fade-target delay-1">
          <div class="f-num">02</div>
          <div class="f-content">
            <h3>極上のシャンプー＆極上スパ</h3>
            <p>フルフラットの最高級シャンプーベッドを使用。頭皮の汚れを落としつつ、絶妙な力加減のヘッドマッサージで日頃の疲れを癒やします。</p>
          </div>
        </div>
        <div class="flow-card fade-target delay-2">
          <div class="f-num">03</div>
          <div class="f-content">
            <h3>マンツーマン施術</h3>
            <p>担当スタイリストが責任を持ってすべて施術します。途中で待たされたり、担当者が変わって不安になることは決してございません。</p>
          </div>
        </div>
        <div class="flow-card fade-target">
          <div class="f-num">04</div>
          <div class="f-content">
            <h3>仕上げ・スタイリングレクチャー</h3>
            <p>乾かし方のコツからアイロンの巻き方、おすすめのスタイリング剤まで。ご自宅で明日から「サロン帰り」を再現できる方法を丁寧にお伝えします。</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section faq" id="faq">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">Q &amp; A</span>
        <h2 class="sect-heading">よくあるご質問</h2>
      </div>
      <div class="faq-accordion">
        <details class="faq-item fade-target" open>
          <summary>完全個室とのことですが、別途料金（個室料）はかかりますか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>いいえ、全席が完全個室仕様となっておりますため、別途個室料金を頂くことは一切ございません。メニュー表記通りのご料金で、特別なプライベート空間をお楽しみいただけます。</p></div>
        </details>
        <details class="faq-item fade-target">
          <summary>初めて行く美容室は緊張するのですが、お任せでも大丈夫ですか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>大歓迎です！最初のヒアリングで、お客様の骨格、髪質、普段のお洋服のテイストなどを総合的に判断し、「最も魅力的に見えるスタイル」をこちらからいくつかご提案させていただきます。「なんとなくこんな雰囲気にしたい」といったアバウトなご要望から形にいたします。</p></div>
        </details>
        <details class="faq-item fade-target">
          <summary>お支払いにクレジットカードや電子マネーは使えますか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>はい、各種クレジットカード（VISA, MasterCard, JCB, AMEX, Diners）、およびPayPay、iD、QUICPay等の電子マネーをご利用いただけます。</p></div>
        </details>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section cta" id="contact">
    <div class="l-container">
      <div class="cta-inner fade-target">
        <div class="cta-head">
          <span class="en">Reservation</span>
          <h2>ご予約について</h2>
          <p>当店は完全予約制となっております。<br>極上のリラックス空間をご用意してお待ちしております。</p>
        </div>
        <div class="cta-actions">
          <div class="btn-wrap">
            <a href="#" class="btn btn-primary"><i data-lucide="calendar"></i> 24時間WEB予約（HotPepper）</a>
            <a href="#" class="btn btn-outline"><i data-lucide="smartphone"></i> LINEにてご相談・予約</a>
          </div>
          <p class="tel-notice">※施術中はお電話に出られない場合がございます。WEBまたはLINEからのご予約がスムーズです。<br>お電話（03-XXXX-XXXX）</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="l-container">
      <div class="ft-grid">
        <div class="ft-brand">
          <div class="logo">
            <span class="logo-en">Belle</span>
          </div>
          <p class="address">〒107-0062<br>東京都港区南青山 X-X-X Belleビル 2F<br>表参道駅 B2出口より徒歩3分<br>営業時間: 10:00 - 20:00（火曜定休）</p>
        </div>
        <div class="ft-nav">
          <ul class="ft-links">
             <li><a href="#concept">Concept</a></li>
             <li><a href="#menu">Menu</a></li>
             <li><a href="#style">Style Gallery</a></li>
             <li><a href="#flow">Flow</a></li>
             <li><a href="#faq">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="ft-bottom">
        <p>&copy; 2026 Belle Hair Salon. All Rights Reserved.</p>
      </div>
    </div>
  </footer>

  <script>
    lucide.createIcons();
    
    // Header Scroll
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) header.classList.add('scrolled');
      else header.classList.remove('scrolled');
    });

    // Mobile Menu
    const menuToggle = document.getElementById('menuToggle');
    const nav = document.querySelector('.nav');
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      nav.classList.toggle('active');
    });

    // Intersection Observer
    const obs = new IntersectionObserver((entries, observer) => {
      entries.forEach(e => {
        if(e.isIntersecting) {
          e.target.classList.add('is-visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.fade-target').forEach(el => obs.observe(el));

    // Accordion
    document.querySelectorAll('details').forEach(detail => {
      detail.addEventListener('toggle', () => {
        const icon = detail.querySelector('.faq-icon');
        icon.style.transform = detail.open ? 'rotate(180deg)' : 'rotate(0deg)';
      });
    });
  </script>
</body>
</html>
"""

css_content = """
:root {
  --bg: #faf9f6; /* Elegant Greige */
  --bg-gray: #f2efe9;
  --text: #4a4541; /* Soft dark brown/gray */
  --text-muted: #8b8379;
  --primary: #c5a880; /* Champagne Gold */
  --primary-hover: #b0916a;
  
  --font-base: 'Noto Sans JP', sans-serif;
  --font-serif: 'Shippori Mincho', serif;
  --font-en: 'Cormorant Garamond', serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--text); line-height: 2; overflow-x: hidden; font-weight: 300; font-family: var(--font-base); }

/* Containers */
.h-container { max-width: 1300px; margin: 0 auto; padding: 0 4%; display: flex; justify-content: space-between; align-items: center; height: 90px; transition: 0.4s; }
.l-container { max-width: 1000px; margin: 0 auto; padding: 0 5%; }
.section { padding: 140px 0; }
.bg-gray { background: var(--bg-gray); }
img { max-width: 100%; height: auto; display: block; }
.center { text-align: center; }

/* Typography */
h1, h2, h3 { font-family: var(--font-serif); font-weight: 500; color: #352f2b; }
.en { font-family: var(--font-en); font-style: italic; }
.en-label { font-family: var(--font-en); font-size: 1.2rem; letter-spacing: 0.3em; color: var(--primary); display: block; margin-bottom: 24px; text-transform: uppercase; }
.sect-heading { font-size: clamp(2.2rem, 4vw, 3rem); line-height: 1.4; margin-bottom: 64px; }

/* Header & Nav */
.header { position: fixed; width: 100%; top: 0; z-index: 1000; transition: all 0.5s cubic-bezier(0.16,1,0.3,1); border-bottom: 1px solid rgba(0,0,0,0.03); background: transparent; }
.header.scrolled { background: rgba(250,249,246,0.95); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
.header.scrolled .h-container { height: 75px; }
.logo-en { font-family: var(--font-en); font-size: 2.2rem; font-style: italic; font-weight: 600; color: #352f2b; letter-spacing: 0.05em; }
.nav { display: flex; align-items: center; gap: 40px; }
.nav-links { display: flex; list-style: none; gap: 32px; }
.nav-links a { text-decoration: none; color: var(--text); font-family: var(--font-en); font-size: 1.1rem; letter-spacing: 0.05em; transition: color 0.3s; }
.nav-links a:hover { color: var(--primary); }
.btn-nav { display: inline-flex; align-items: center; gap: 8px; background: var(--primary); color: #fff; padding: 10px 30px; border-radius: 100px; text-decoration: none; font-size: 0.95rem; transition: background 0.3s; font-family: var(--font-serif); }
.btn-nav:hover { background: var(--primary-hover); }
.menu-toggle { display: none; background: none; border: none; cursor: pointer; width: 30px; height: 20px; position: relative; z-index: 1001; }
.menu-toggle span { display: block; width: 100%; height: 1px; background: var(--text); position: absolute; transition: 0.3s; }
.menu-toggle span:nth-child(1) { top: 0; }
.menu-toggle span:nth-child(2) { top: 9px; }
.menu-toggle span:nth-child(3) { bottom: 0; }

/* Hero */
.hero { height: 100vh; position: relative; display: flex; align-items: center; }
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; opacity: 0.8; filter: contrast(95%); }
.hero-mask { position: absolute; inset: 0; z-index: 1; background: linear-gradient(100deg, rgba(250,249,246,0.95) 0%, rgba(250,249,246,0.5) 55%, rgba(250,249,246,0) 100%); }
.hero-content { position: relative; z-index: 2; width: 100%; padding: 0 5%; max-width: 1400px; margin: 0 auto; display: flex; justify-content: flex-start; }
.vertical-text { writing-mode: vertical-rl; text-orientation: mixed; margin-left: 10%; margin-top: 50px; }
.hero-title { font-size: clamp(3rem, 7vw, 4.5rem); line-height: 1.5; font-weight: 500; font-family: var(--font-serif); color: #352f2b; letter-spacing: 0.15em; }
.hero-hl { color: var(--primary); }
.hero-en { font-family: var(--font-en); font-size: 1.2rem; letter-spacing: 0.4em; color: var(--primary); margin-right: 40px; text-transform: uppercase; font-style: italic; }
.hero-subtitle { font-size: clamp(0.95rem, 2vw, 1.1rem); color: var(--text); margin-right: 40px; margin-top: 50px; letter-spacing: 0.2em; line-height: 2.2; font-family: var(--font-serif); }
.scroll-down { position: absolute; bottom: 40px; left: 5%; display: flex; flex-direction: column; align-items: center; gap: 12px; color: var(--primary); font-size: 0.8rem; letter-spacing: 0.2em; font-family: var(--font-en); text-transform: uppercase; }
.scroll-down .line { width: 1px; height: 60px; background: rgba(197,168,128,0.2); position: relative; overflow: hidden; }
.scroll-down .line::before { content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 100%; background: var(--primary); animation: scrollDown 2s ease-in-out infinite; }
@keyframes scrollDown { 0% { top: -100%; } 100% { top: 100%; } }

/* Trouble */
.trouble-box { background: #fff; padding: 100px 80px; box-shadow: 0 20px 60px rgba(0,0,0,0.03); position: relative; }
.trouble-box::before { content: ''; position: absolute; inset: 10px; border: 1px solid rgba(197,168,128,0.3); pointer-events: none; }
.t-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 50px; margin-bottom: 60px; justify-content: center; }
.t-item { text-align: center; }
.t-icon { font-family: var(--font-en); font-size: 3rem; color: var(--primary); font-style: italic; line-height: 1; margin-bottom: 20px; opacity: 0.6; }
.t-item p { font-size: 0.95rem; color: var(--text); text-align: justify; }
.t-item strong { display: block; font-family: var(--font-serif); font-size: 1.1rem; color: #352f2b; margin-bottom: 12px; font-weight: 600; }
.t-answer { text-align: center; font-size: 1.25rem; font-family: var(--font-serif); padding-top: 40px; border-top: 1px solid rgba(197,168,128,0.2); color: var(--primary); font-weight: 600; line-height: 1.8; }

/* Philosophy */
.phil-wrap { display: flex; gap: 80px; align-items: center; }
.phil-text { flex: 1.1; }
.phil-text .desc p { margin-bottom: 24px; color: var(--text); font-size: 1rem; text-align: justify; }
.phil-img { flex: 1; position: relative; }
.phil-img img { box-shadow: 20px -20px 0 var(--bg-gray); }
.phil-img .badge { position: absolute; bottom: -30px; left: -30px; background: var(--primary); color: #fff; width: 120px; height: 120px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: 500; font-family: var(--font-serif); line-height: 1.3; box-shadow: 0 10px 30px rgba(197,168,128,0.3); border: 2px solid #fff; }
.phil-img .badge .num { font-family: var(--font-serif); font-size: 1.8rem; letter-spacing: 0; }

/* Service */
.srv-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 80px; }
.srv-card { background: #fff; transition: transform 0.5s; display: flex; flex-direction: column; }
.srv-card:hover { transform: translateY(-10px); box-shadow: 0 20px 50px rgba(0,0,0,0.05); }
.srv-img img { height: 280px; width: 100%; object-fit: cover; }
.srv-body { padding: 40px 30px; flex: 1; display: flex; flex-direction: column; text-align: center; }
.srv-body h3 { font-size: 1.15rem; margin-bottom: 20px; color: #352f2b; }
.srv-body h3 .en { display: block; color: var(--primary); font-size: 1.5rem; margin-bottom: 8px; }
.srv-body p { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 30px; flex: 1; text-align: justify; }
.srv-card .price { font-size: 0.9rem; color: var(--text-muted); border-top: 1px solid rgba(0,0,0,0.03); padding-top: 20px; }
.srv-card .price span { font-size: 1.5rem; font-family: var(--font-en); color: #352f2b; font-weight: 600; margin-right: 4px; }

/* Works */
.works-wrap { display: flex; flex-direction: column; gap: 100px; margin-top: 80px; }
.work-item { display: flex; gap: 80px; align-items: center; }
.work-item.reverse { flex-direction: row-reverse; }
.wa-img { flex: 1; position: relative; }
.wa-img::before { content:''; position:absolute; inset: 20px -20px -20px 20px; border: 1px solid var(--primary); z-index: -1; }
.work-item.reverse .wa-img::before { inset: 20px 20px -20px -20px; }
.ba-tag { position: absolute; top: -15px; left: -15px; background: var(--bg); color: var(--primary); padding: 8px 24px; font-family: var(--font-serif); font-size: 0.9rem; border: 1px solid var(--primary); z-index: 2; }
.work-item.reverse .ba-tag { left: auto; right: -15px; }
.wa-img img { width: 100%; height: auto; aspect-ratio: 3/4; object-fit: cover; }
.wa-text { flex: 1; }
.wa-text h3 { font-size: 1.6rem; line-height: 1.6; margin-bottom: 30px; color: #352f2b; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 20px; }
.wa-text p { color: var(--text-muted); font-size: 1rem; text-align: justify; }

/* Flow */
.flow-list { margin-top: 80px; display: grid; gap: 40px; }
.flow-card { background: #fff; padding: 40px 50px; display: flex; gap: 50px; align-items: center; border: 1px solid rgba(0,0,0,0.03); position: relative; }
.f-num { font-family: var(--font-en); font-size: 4rem; color: var(--primary); font-style: italic; line-height: 1; min-width: 80px; opacity: 0.4; }
.flow-content h3 { font-size: 1.25rem; margin-bottom: 12px; color: #352f2b; }
.flow-content p { color: var(--text-muted); font-size: 0.95rem; }

/* FAQ */
.faq-accordion { margin-top: 80px; max-width: 800px; margin-left: auto; margin-right: auto; border-top: 1px solid rgba(197,168,128,0.3); }
.faq-item { border-bottom: 1px solid rgba(197,168,128,0.3); }
.faq-item summary { padding: 30px 20px; font-family: var(--font-serif); font-size: 1.15rem; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; outline: none; color: #352f2b; }
.faq-item summary::-webkit-details-marker { display: none; }
.faq-icon { transition: transform 0.3s; color: var(--primary); stroke-width: 1.5; }
.faq-ans { padding: 0 20px 30px; color: var(--text-muted); font-size: 0.95rem; line-height: 1.9; }

/* CTA */
.cta { padding: 140px 0; background: #fff; position: relative; }
.cta::before { content: ''; position: absolute; inset: 20px; border: 1px solid rgba(197,168,128,0.2); pointer-events: none; }
.cta-inner { text-align: center; max-width: 700px; margin: 0 auto; position: relative; z-index: 2; }
.cta-head .en { display: block; font-family: var(--font-en); font-size: 1.5rem; letter-spacing: 0.2em; color: var(--primary); margin-bottom: 24px; text-transform: uppercase; }
.cta-head h2 { font-size: 2.2rem; margin-bottom: 20px; color: #352f2b; }
.cta-head p { color: var(--text-muted); font-size: 1rem; margin-bottom: 60px; font-family: var(--font-serif); }
.cta-actions { display: flex; flex-direction: column; gap: 30px; align-items: center; }
.btn-wrap { display: flex; gap: 24px; justify-content: center; flex-wrap: wrap; width: 100%; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 12px; padding: 20px 40px; font-family: var(--font-serif); text-decoration: none; transition: all 0.4s ease; font-size: 1rem; width: 100%; max-width: 320px; border-radius: 100px; }
.btn-primary { background: #352f2b; color: #fff; }
.btn-primary:hover { background: var(--primary); transform: translateY(-3px); box-shadow: 0 15px 30px rgba(197,168,128,0.3); }
.btn-outline { background: #fff; color: #352f2b; border: 1px solid #352f2b; }
.btn-outline:hover { background: #352f2b; color: #fff; }
.tel-notice { font-size: 0.85rem; color: var(--text-muted); margin-top: 20px; }

/* Footer */
.footer { padding: 100px 0 40px; background: #352f2b; color: rgba(255,255,255,0.8); }
.ft-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; margin-bottom: 80px; }
.ft-brand .logo-en { color: #fff; display: block; margin-bottom: 30px; }
.ft-brand .address { font-size: 0.9rem; line-height: 2.2; }
.ft-links { list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
.ft-links a { color: rgba(255,255,255,0.6); text-decoration: none; transition: color 0.3s; font-family: var(--font-en); font-size: 1.1rem; letter-spacing: 0.05em; }
.ft-links a:hover { color: var(--primary); }
.ft-bottom { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 40px; text-align: center; color: rgba(255,255,255,0.4); font-size: 0.8rem; font-family: var(--font-en); letter-spacing: 0.1em; }

/* Animations */
.fade-target { opacity: 0; transform: translateY(30px); transition: opacity 1s ease, transform 1s cubic-bezier(0.16,1,0.3,1); }
.fade-target.is-visible { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.15s; }
.delay-2 { transition-delay: 0.3s; }
.delay-3 { transition-delay: 0.45s; }
.offset-delay { transition-delay: 0.2s; }

/* Mobile */
@media (max-width: 900px) {
  .vertical-text { margin-left: 0; margin-bottom: 40px; margin-top: 20px; }
  .trouble-box { padding: 60px 40px; }
  .t-list, .srv-grid { grid-template-columns: 1fr; gap: 40px; }
  .phil-wrap, .work-item, .wa-img { flex-direction: column !important; gap: 40px; }
  .flow-card { flex-direction: column; align-items: flex-start; gap: 20px; }
  .ft-grid { grid-template-columns: 1fr; gap: 50px; }
  .nav-links, .btn-nav { display: none; }
  .menu-toggle { display: block; }
}
"""

with open(r'd:\sharkstars\demos\salon-01\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content.strip())

with open(r'd:\sharkstars\demos\salon-01\assist\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css_content.strip())

print("salon-01 HTML and CSS rewritten successfully.")
