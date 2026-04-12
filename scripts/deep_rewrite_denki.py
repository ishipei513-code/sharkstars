import os

denki_html = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>サンライズ電気 | 24時間365日、電気トラブル即日解決</title>
  <meta name="description" content="ブレーカーが落ちる、コンセントを増やしたい、漏電が心配…。地元密着の電気工事専門・サンライズ電気へ。第一種電気工事士が在籍し、安心施工と明朗会計をお約束します。">
  
  <!-- Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Teko:wght@500;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="assist/css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  
  <!-- Header -->
  <header class="header" id="header">
    <div class="h-container">
      <div class="logo">
        <i data-lucide="zap"></i>
        <span>サンライズ電気</span>
      </div>
      <nav class="nav">
        <ul class="nav-links">
          <li><a href="#philosophy">私たちの想い</a></li>
          <li><a href="#service">料金・メニュー</a></li>
          <li><a href="#works">施工実績</a></li>
          <li><a href="#flow">ご依頼の流れ</a></li>
          <li><a href="#faq">よくある質問</a></li>
        </ul>
        <a href="#contact" class="btn btn-nav"><i data-lucide="phone"></i> 0120-000-000</a>
      </nav>
      <button class="menu-toggle" id="menuToggle" aria-label="メニューを開く">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-bg">
      <img src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="電気工事の職人">
    </div>
    <div class="hero-mask"></div>
    <div class="hero-content fade-target">
      <div class="vertical-text">
        <h1 class="hero-title">暗闇の不安を、<br>一秒でも早く<br><span class="hero-hl">「明かり」に変える。</span></h1>
        <p class="hero-subtitle">漏電、停電、見えない電気のトラブル。<br>国家資格を持つプロが、あなたの暮らしの「あたりまえ」を迅速に取り戻します。</p>
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
        <h2 class="sect-heading center">電気のことで、こんなお悩みはありませんか？</h2>
        <div class="t-list">
          <div class="t-item fade-target delay-1">
            <i data-lucide="alert-triangle"></i>
            <p>電子レンジとドライヤーを同時に使うと、すぐにブレーカーが落ちて困っている…</p>
          </div>
          <div class="t-item fade-target delay-2">
            <i data-lucide="plug"></i>
            <p>テレワーク部屋のコンセントが足りない。タコ足配線で火事にならないか心配…</p>
          </div>
          <div class="t-item fade-target delay-3">
            <i data-lucide="flame"></i>
            <p>コンセント周辺から焦げ臭いにおいがする。漏電しているかもしれない…</p>
          </div>
        </div>
        <div class="t-answer fade-target delay-1">
          <p><strong>そのお悩み、第一種電気工事士が在籍する「サンライズ電気」が最短即日でスピード解決いたします！</strong></p>
        </div>
      </div>
    </div>
  </section>

  <!-- Philosophy -->
  <section class="section philosophy" id="philosophy">
    <div class="l-container">
      <div class="phil-wrap">
        <div class="phil-text fade-target">
          <span class="en-label">P H I L O S O P H Y</span>
          <h2 class="sect-heading">見えない配線にこそ、<br>プロの美学が宿る。</h2>
          <div class="desc">
            <p>電気は目に見えません。だからこそ、壁の中や天井裏など「お客様の目に見えない部分」の施工に一切の妥協を許さないのが本物の電気工事です。</p>
            <p>サンライズ電気では、在籍スタッフ全員が国家資格である『第一種電気工事士』または『第二種電気工事士』を取得。単に電気を通すだけでなく、漏電火災のリスクを根絶する完璧な絶縁処理と、後から見ても誰にでも分かる美しい配線処理にこだわっています。</p>
            <p>「コンセントの調子が悪い」といった些細なご相談でも、すぐに駆けつけます。地域の皆様の生活インフラを守る裏方として、私たちをお役立てください。</p>
          </div>
          <div class="master-sign">
            <p>代表親方・第一種電気工事士</p>
            <p class="name">東 太陽</p>
          </div>
        </div>
        <div class="phil-img fade-target offset-delay">
          <img src="https://images.unsplash.com/photo-1542361345-89e58247f2d5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="作業中の電気工事士">
          <div class="badge">緊急<br><span class="num">対応</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Service List -->
  <section class="section service bg-gray" id="service">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">S E R V I C E</span>
        <h2 class="sect-heading">業務内容・目安料金</h2>
        <p>※建物の構造や配線の状況により変動するため、施工前には必ず<strong>無料のお見積り</strong>を提出し、ご納得いただいてから作業を開始いたします。</p>
      </div>

      <div class="srv-grid">
        <div class="srv-card fade-target">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1621905252472-881bbb63b36e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="スイッチ・コンセント工事">
          </div>
          <div class="srv-body">
            <h3><i data-lucide="plug"></i> コンセント・スイッチ増設</h3>
            <p>タコ足配線の解消や、エアコン用の専用回路増設、古くなったスイッチの交換（最新のワイドスイッチなど）を行います。</p>
            <div class="price">コンセント増設 <span>¥8,800〜</span></div>
          </div>
        </div>
        
        <div class="srv-card fade-target delay-1">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1498679093836-e8d197609a36?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="照明器具・LED">
          </div>
          <div class="srv-body">
            <h3><i data-lucide="lightbulb"></i> 照明器具工事・LED化</h3>
            <p>電気代を大幅に削減する家全体のLED化や、シーリングライトの取付、ダクトレールの新設など、光の演出をお手伝いします。</p>
            <div class="price">照明取付工事 <span>¥5,500〜</span></div>
          </div>
        </div>

        <div class="srv-card fade-target delay-2">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1558449028-b53a39d100fc?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="漏電調査・ブレーカー">
          </div>
          <div class="srv-body">
            <h3><i data-lucide="shield-alert"></i> 漏電調査・分電盤交換</h3>
            <p>ブレーカーが頻繁に落ちる原因を専用テスターで突き止めます。老朽化した分電盤（ブレーカーボックス）の安全な交換も対応。</p>
            <div class="price">漏電専用調査 <span>¥11,000〜</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Works -->
  <section class="section works" id="works">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">W O R K S</span>
        <h2 class="sect-heading">施工実績</h2>
      </div>

      <div class="works-wrap">
        <div class="work-item fade-target">
          <div class="wa-img">
            <div class="ba-tag">分電盤のフル交換</div>
            <img src="https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="施工事例1">
          </div>
          <div class="wa-text">
            <h3>築40年の戸建て、頻繁に落ちるブレーカーを最新設備へ一新</h3>
            <p>電子レンジを使うとすぐに停電してしまうというお悩み。漏電調査の結果、配線の老朽化と電力容量不足が原因でした。単相3線式への切り替え（アンペア増設）と最新の分電盤への交換工事を行い、安心して電化製品を使える環境を整えました。</p>
          </div>
        </div>

        <div class="work-item reverse fade-target delay-1">
          <div class="wa-img">
            <div class="ba-tag">店舗の照明デザイン工事</div>
            <img src="https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="施工事例2">
          </div>
          <div class="wa-text">
            <h3>カフェ新規オープンに伴う、ダクトレール＆ペンダントライト施工</h3>
            <p>スケルトン物件からの店舗工事のご依頼。図面を元に配線設計を行い、温かみのある空間を演出するためのライティングレールを設置。各テーブルの位置に合わせた美しい照明計画を実現し、オーナー様にも「想像以上の空間になった」と喜ばれました。</p>
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
        <h2 class="sect-heading">ご依頼の流れ</h2>
      </div>

      <div class="flow-list">
        <div class="flow-card fade-target">
          <div class="f-num">01</div>
          <h3>お問い合わせ（24時間受付）</h3>
          <p>トラブルの場合は焦らずお電話ください。「コンセントが焦げ臭い」「真っ暗になった」など、状況をお伝えいただけますと幸いです。</p>
        </div>
        <div class="flow-card fade-target delay-1">
          <div class="f-num">02</div>
          <h3>現地調査と原因究明（ヒアリング）</h3>
          <p>プロの電気工事士が専用の計測器を持参し、トラブルの原因を究明します。増設工事の場合は、配線ルートを調査します。</p>
        </div>
        <div class="flow-card fade-target delay-2">
          <div class="f-num">03</div>
          <h3>お見積りのご提示</h3>
          <p>部材費と作業費を含めた明確なお見積書をご提示します。ここまではエリア内であれば完全無料。勝手に作業を始めて請求することはありません。</p>
        </div>
        <div class="flow-card fade-target">
          <div class="f-num">04</div>
          <h3>安全第一の確実な施工</h3>
          <p>ご納得いただきましたら施工を開始します。漏電や火災のリスクがないよう、国の基準を厳守した安全な配線作業を行います。</p>
        </div>
        <div class="flow-card fade-target delay-1">
          <div class="f-num">05</div>
          <h3>動作確認と保証書の発行</h3>
          <p>一緒に動作を確認して完了です。万が一の場合に備え、施工不良によるトラブルには長期の無償保証制度をご用意しております。</p>
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
          <summary>夜中や早朝でもすぐに来てもらえますか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>はい、「地域密着の電気の救急車」として24時間体制で待機しております。深夜割増料金は発生しますが、トラブル時は時間帯問わずお電話ください。</p></div>
        </details>
        <details class="faq-item fade-target">
          <summary>少しの作業（電球の交換など）でも頼んで良いでしょうか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>もちろんです。「天井が高くて電球が替えられない」「スイッチのカバーが取れただけ」といった些細なお困りごとも大歓迎です。</p></div>
        </details>
        <details class="faq-item fade-target">
          <summary>賃貸マンションでも自分から作業依頼できますか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>軽微な修理であれば可能ですが、分電盤の交換やコンセントの増設のような壁に穴を空ける「据付工事」を伴う場合は、事前に管理会社様または大家様の許可を頂くようお願いしております。管理会社様への説明事項が必要な場合は、私たちから説明等サポートすることも可能です。</p></div>
        </details>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section cta" id="contact">
    <div class="l-container">
      <div class="cta-inner fade-target">
        <div class="cta-head">
          <i data-lucide="zap" class="cta-icon"></i>
          <h2>電気のトラブル、今すぐ解決します。</h2>
          <p>お見積り・現地調査は無料です。危険なトラブルに発展する前に、プロにご相談ください。</p>
        </div>
        <div class="cta-actions">
          <div class="tel-wrap">
            <span class="tel-text">24時間365日 スピード駆けつけ対応</span>
            <a href="tel:0120-000-000" class="tel-number"><i data-lucide="phone-call"></i> 0120-000-000</a>
          </div>
          <div class="btn-wrap">
            <a href="#" class="btn btn-primary"><i data-lucide="mail"></i> メールでのお問い合わせ</a>
            <a href="#" class="btn btn-line"><i data-lucide="message-circle"></i> LINEで写真を送って見積り</a>
          </div>
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
            <i data-lucide="zap"></i>
            <span>サンライズ電気</span>
          </div>
          <p class="address">〒100-0000<br>東京都千代田区〇〇 1-2-3<br>・第一種電気工事士 在籍<br>・登録電気工事業者 届出済<br>・安心の賠償責任保険加入店</p>
        </div>
        <div class="ft-nav">
          <ul class="ft-links">
             <li><a href="#philosophy">私たちの想い</a></li>
             <li><a href="#service">料金・メニュー</a></li>
             <li><a href="#works">施工実績</a></li>
             <li><a href="#flow">ご依頼の流れ</a></li>
             <li><a href="#faq">よくある質問</a></li>
          </ul>
        </div>
      </div>
      <div class="ft-bottom">
        <p>&copy; 2026 SUNRISE ELECTRIC. All Rights Reserved.</p>
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

denki_css = """
:root {
  --bg: #030712;
  --bg-gray: #111827;
  --text: #f9fafb;
  --text-muted: #9ca3af;
  --primary: #fbbf24; /* Electric Yellow Accent */
  --primary-hover: #f59e0b;
  --line-color: #f1ebd5; /* Line Green equivalent for dark mode? No let's use a nice green */
  --btn-line: #06c755;
  font-family: 'Noto Sans JP', sans-serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--text); line-height: 1.8; overflow-x: hidden; }

/* Containers */
.h-container { max-width: 1200px; margin: 0 auto; padding: 0 4%; display: flex; justify-content: space-between; align-items: center; height: 80px; }
.l-container { max-width: 1100px; margin: 0 auto; padding: 0 5%; }
.section { padding: 120px 0; }
.bg-gray { background: var(--bg-gray); }
img { max-width: 100%; height: auto; display: block; }
.center { text-align: center; }

/* Typography */
.en-label { font-family: 'Teko', sans-serif; font-size: 1.8rem; letter-spacing: 0.2em; color: var(--primary); display: block; margin-bottom: 8px; }
.sect-heading { font-size: clamp(2rem, 4vw, 2.8rem); font-weight: 700; line-height: 1.4; margin-bottom: 64px; }

/* Header & Nav */
.header { position: fixed; width: 100%; top: 0; z-index: 1000; transition: all 0.4s; }
.header.scrolled { background: rgba(3,7,18,0.9); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
.logo { font-size: 1.5rem; font-weight: 700; display: flex; align-items: center; gap: 8px; color: #fff; }
.logo i { color: var(--primary); }
.nav { display: flex; align-items: center; gap: 32px; }
.nav-links { display: flex; list-style: none; gap: 24px; }
.nav-links a { text-decoration: none; color: #fff; font-weight: 500; font-size: 0.95rem; transition: color 0.3s; }
.nav-links a:hover { color: var(--primary); }
.btn-nav { display: inline-flex; align-items: center; gap: 8px; background: var(--primary); color: #000; padding: 10px 24px; border-radius: 50px; text-decoration: none; font-weight: 700; transition: background 0.3s; }
.btn-nav:hover { background: var(--primary-hover); }
.menu-toggle { display: none; background: none; border: none; cursor: pointer; width: 30px; height: 20px; position: relative; z-index: 1001; }
.menu-toggle span { display: block; width: 100%; height: 2px; background: #fff; position: absolute; transition: 0.3s; }
.menu-toggle span:nth-child(1) { top: 0; }
.menu-toggle span:nth-child(2) { top: 9px; }
.menu-toggle span:nth-child(3) { bottom: 0; }

/* Hero */
.hero { height: 100vh; position: relative; display: flex; align-items: center; }
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; opacity: 0.5; filter: grayscale(80%) sepia(20%) hue-rotate(180deg); }
.hero-mask { position: absolute; inset: 0; z-index: 1; background: linear-gradient(120deg, rgba(3,7,18,0.9) 0%, rgba(3,7,18,0.4) 100%); }
.hero-content { position: relative; z-index: 2; width: 100%; padding: 0 5%; max-width: 1400px; margin: 0 auto; display: flex; justify-content: flex-end; }
.vertical-text { writing-mode: vertical-rl; text-orientation: mixed; margin-right: 5%; }
.hero-title { font-size: clamp(3rem, 7vw, 6rem); line-height: 1.3; font-weight: 700; color: #fff; letter-spacing: 0.1em; text-shadow: 0 10px 30px rgba(0,0,0,0.8); }
.hero-hl { color: var(--primary); }
.hero-subtitle { font-size: clamp(1rem, 2vw, 1.25rem); color: rgba(255,255,255,0.8); margin-right: 40px; margin-top: 40px; letter-spacing: 0.1em; line-height: 2.2; text-shadow: 0 5px 15px rgba(0,0,0,0.5); }
.scroll-down { position: absolute; bottom: 40px; left: 5%; display: flex; flex-direction: column; align-items: center; gap: 8px; color: #fff; font-family: 'Teko', sans-serif; font-size: 1.2rem; letter-spacing: 0.1em; }
.scroll-down .line { width: 1px; height: 60px; background: rgba(255,255,255,0.3); position: relative; overflow: hidden; }
.scroll-down .line::before { content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 100%; background: #fff; animation: scrollDown 2s ease-in-out infinite; }
@keyframes scrollDown { 0% { top: -100%; } 100% { top: 100%; } }

/* Trouble */
.trouble-box { background: var(--bg-gray); padding: 80px 60px; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.05); }
.t-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-bottom: 40px; justify-content: center; }
.t-item { text-align: center; background: rgba(255,255,255,0.03); padding: 30px 20px; border-radius: 12px; }
.t-item i { width: 48px; height: 48px; color: var(--primary); margin-bottom: 20px; }
.t-item p { font-size: 1rem; color: var(--text-muted); }
.t-answer { text-align: center; font-size: 1.4rem; padding: 20px; background: rgba(251,191,36,0.1); color: var(--primary); border-radius: 10px; border: 1px solid rgba(251,191,36,0.2); }

/* Philosophy */
.phil-wrap { display: flex; gap: 80px; align-items: center; }
.phil-text { flex: 1; }
.phil-text .desc p { margin-bottom: 24px; color: var(--text-muted); font-size: 1.1rem; }
.master-sign { margin-top: 40px; border-left: 4px solid var(--primary); padding-left: 20px; }
.master-sign p { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 4px; }
.master-sign .name { font-size: 1.5rem; font-weight: 700; color: #fff; }
.phil-img { flex: 1; position: relative; }
.phil-img img { border-radius: 24px; box-shadow: 0 30px 60px rgba(0,0,0,0.5); border: 2px solid rgba(255,255,255,0.1); }
.phil-img .badge { position: absolute; bottom: -30px; left: -30px; background: var(--primary); color: #000; width: 140px; height: 140px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: 700; line-height: 1.2; box-shadow: 0 10px 20px rgba(0,0,0,0.3); border: 4px solid var(--bg); }
.phil-img .badge .num { font-size: 2.5rem; font-family: 'Teko', sans-serif; letter-spacing: 0; }

/* Service */
.srv-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 60px; }
.srv-card { background: var(--bg); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.2); transition: transform 0.3s; border: 1px solid rgba(255,255,255,0.03); }
.srv-card:hover { transform: translateY(-10px); border-color: rgba(251,191,36,0.3); }
.srv-img img { height: 220px; width: 100%; object-fit: cover; }
.srv-body { padding: 30px; }
.srv-body h3 { font-size: 1.3rem; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; }
.srv-body h3 i { color: var(--primary); width: 20px; height: 20px; }
.srv-body p { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 24px; height: 85px; }
.srv-card .price { font-size: 1.1rem; color: #fff; font-weight: 500; display: flex; justify-content: space-between; align-items: baseline; background: rgba(255,255,255,0.05); padding: 12px 16px; border-radius: 8px; }
.srv-card .price span { font-size: 1.5rem; font-family: 'Teko', sans-serif; color: var(--primary); }

/* Works */
.works-wrap { display: flex; flex-direction: column; gap: 80px; margin-top: 60px; }
.work-item { display: flex; gap: 60px; align-items: center; }
.work-item.reverse { flex-direction: row-reverse; }
.wa-img { flex: 1; position: relative; border-radius: 20px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
.wa-img::after { content: ''; position: absolute; inset: 0; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.1); pointer-events: none; border-radius: 20px; }
.ba-tag { position: absolute; top: 20px; left: -10px; background: var(--primary); color: #000; padding: 8px 24px; font-weight: 700; box-shadow: 0 10px 20px rgba(0,0,0,0.3); z-index: 2; border-radius: 0 100px 100px 0; }
.wa-img img { transition: transform 0.5s; }
.work-item:hover .wa-img img { transform: scale(1.05); }
.wa-text { flex: 1; }
.wa-text h3 { font-size: 1.5rem; line-height: 1.5; margin-bottom: 20px; border-left: 4px solid var(--primary); padding-left: 16px; }
.wa-text p { color: var(--text-muted); font-size: 1.05rem; }

/* Flow */
.flow-list { margin-top: 60px; display: grid; gap: 24px; }
.flow-card { background: var(--bg); padding: 30px 40px; border-radius: 16px; display: flex; gap: 40px; align-items: center; border: 1px solid rgba(255,255,255,0.03); position: relative; overflow: hidden; }
.flow-card::before { content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 4px; background: var(--primary); }
.f-num { font-family: 'Teko', sans-serif; font-size: 4rem; color: rgba(255,255,255,0.05); font-weight: 700; line-height: 1; position: absolute; right: 20px; bottom: -10px; }
.flow-card h3 { font-size: 1.3rem; margin-bottom: 8px; width: 30%; flex-shrink: 0; }
.flow-card p { color: var(--text-muted); font-size: 1rem; flex: 1; }

/* FAQ */
.faq-accordion { margin-top: 60px; max-width: 800px; margin-left: auto; margin-right: auto; }
.faq-item { background: var(--bg-gray); margin-bottom: 16px; border-radius: 12px; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); }
.faq-item summary { padding: 24px 30px; font-weight: 700; font-size: 1.1rem; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; outline: none; }
.faq-item summary::-webkit-details-marker { display: none; }
.faq-icon { transition: transform 0.3s; color: var(--primary); }
.faq-ans { padding: 0 30px 30px; color: var(--text-muted); border-top: 1px dashed rgba(255,255,255,0.1); margin-top: -10px; padding-top: 24px; }

/* CTA */
.cta { padding: 160px 0; background: linear-gradient(to bottom, var(--bg) 0%, var(--bg-gray) 100%); }
.cta-inner { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 30px; padding: 80px 60px; text-align: center; position: relative; overflow: hidden; }
.cta-inner::before { content: ''; position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(251,191,36,0.1) 0%, transparent 60%); pointer-events: none; }
.cta-icon { width: 64px; height: 64px; color: var(--primary); margin-bottom: 24px; }
.cta-head h2 { font-size: 2.5rem; margin-bottom: 16px; font-weight: 700; }
.cta-head p { color: var(--text-muted); font-size: 1.1rem; margin-bottom: 48px; }
.cta-actions { display: flex; flex-direction: column; gap: 32px; align-items: center; }
.tel-wrap { display: flex; flex-direction: column; gap: 8px; }
.tel-text { font-size: 0.9rem; color: var(--primary); font-weight: 700; letter-spacing: 0.1em; }
.tel-number { font-size: 3rem; font-family: 'Teko', sans-serif; font-weight: 700; color: #fff; text-decoration: none; display: flex; align-items: center; gap: 12px; line-height: 1; }
.btn-wrap { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 16px 32px; border-radius: 100px; font-weight: 700; text-decoration: none; transition: transform 0.3s, opacity 0.3s; }
.btn:hover { transform: translateY(-3px); opacity: 0.9; }
.btn-primary { background: #fff; color: #000; box-shadow: 0 10px 20px rgba(255,255,255,0.2); }
.btn-line { background: var(--btn-line); color: #fff; box-shadow: 0 10px 20px rgba(6,199,85,0.3); }

/* Footer */
.footer { border-top: 1px solid rgba(255,255,255,0.05); padding: 80px 0 40px; background: var(--bg-gray); }
.ft-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; margin-bottom: 60px; }
.ft-brand .logo { margin-bottom: 20px; }
.ft-brand .address { color: var(--text-muted); line-height: 2; font-size: 0.95rem; }
.ft-links { list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.ft-links a { color: var(--text-muted); text-decoration: none; transition: color 0.3s; }
.ft-links a:hover { color: var(--primary); }
.ft-bottom { border-top: 1px solid rgba(255,255,255,0.05); padding-top: 30px; text-align: center; color: var(--text-muted); font-size: 0.85rem; font-family: 'Teko', sans-serif; letter-spacing: 0.05em; }

/* Animations */
.fade-target { opacity: 0; transform: translateY(40px); transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.16,1,0.3,1); }
.fade-target.is-visible { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.15s; }
.delay-2 { transition-delay: 0.3s; }
.delay-3 { transition-delay: 0.45s; }
.offset-delay { transition-delay: 0.2s; }

/* Mobile */
@media (max-width: 900px) {
  .vertical-text { margin-right: 0; margin-bottom: 40px; }
  .t-list, .srv-grid { grid-template-columns: 1fr; }
  .phil-wrap, .work-item, .wa-img { flex-direction: column !important; }
  .flow-card { flex-direction: column; align-items: flex-start; gap: 16px; }
  .flow-card h3 { width: 100%; }
  .ft-grid { grid-template-columns: 1fr; }
  .nav-links, .btn-nav { display: none; }
  .menu-toggle { display: block; }
}
"""

with open(r'd:\sharkstars\demos\denki-01\index.html', 'w', encoding='utf-8') as f:
    f.write(denki_html.strip())

with open(r'd:\sharkstars\demos\denki-01\assist\css\style.css', 'w', encoding='utf-8') as f:
    f.write(denki_css.strip())

print("denki-01 HTML and CSS rewritten successfully.")
