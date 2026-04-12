import os

const_html = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>匠工房 | 一級建築士と創るデザインリフォーム・リノベーション</title>
  <meta name="description" content="ただ新しくするだけではない、暮らしの質を高めるデザインリフォーム。地元密着の「匠工房」なら一級建築士があなたの理想を予算内で叶えます。フルリノベから水回りの改修まで。">
  
  <!-- Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600;700;800&family=Noto+Sans+JP:wght@300;400;500&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="assist/css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  
  <!-- Header -->
  <header class="header" id="header">
    <div class="h-container">
      <div class="logo">
        <i data-lucide="home"></i>
        <span>匠工房</span>
      </div>
      <nav class="nav">
        <ul class="nav-links">
          <li><a href="#philosophy">私たちの想い</a></li>
          <li><a href="#service">リフォームメニュー</a></li>
          <li><a href="#works">施工事例</a></li>
          <li><a href="#flow">ご相談の流れ</a></li>
          <li><a href="#faq">よくある質問</a></li>
        </ul>
        <a href="#contact" class="btn btn-nav"><i data-lucide="mail"></i> 無料カタログ・ご相談</a>
      </nav>
      <button class="menu-toggle" id="menuToggle" aria-label="メニューを開く">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-bg">
      <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" alt="美しいモダンリビング">
    </div>
    <div class="hero-mask"></div>
    <div class="hero-content fade-target">
      <div class="vertical-text">
        <h1 class="hero-title">空間に、<br>新たな<span class="hero-hl">物語</span>を刻む。</h1>
        <p class="hero-subtitle">ただ綺麗にするだけではない、<br>あなたの「これからの暮らし」をデザインする本格リノベーション。</p>
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
        <h2 class="sect-heading center">今の住まいに、こんなご不満はありませんか？</h2>
        <div class="t-list">
          <div class="t-item fade-target delay-1">
            <i data-lucide="snowflake"></i>
            <p>冬になるとお風呂場や脱衣所が凍えるほど寒い。ヒートショックが心配…</p>
          </div>
          <div class="t-item fade-target delay-2">
            <i data-lucide="layout"></i>
            <p>キッチンが壁を向いていて孤立している。家族と会話しながら料理したい…</p>
          </div>
          <div class="t-item fade-target delay-3">
            <i data-lucide="building"></i>
            <p>中古マンションを買ったけれど、昔ながらの細かく区切られた間取りが使いづらい…</p>
          </div>
        </div>
        <div class="t-answer fade-target delay-1">
          <p><strong>そのお悩み、一級建築士と熟練の専属大工を抱える「匠工房」が、デザインと機能性を両立して解決します！</strong></p>
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
          <h2 class="sect-heading">家への愛着を、<br>もう一度。</h2>
          <div class="desc">
            <p>リフォームとは、単に古くなった設備を新しいものに交換することではありません。「日々の家事の負担をどう減らすか」「休日に家族が自然と集まる空間をどう作るか」という、お客様の暮らしそのものを再設計することだと私たちは考えています。</p>
            <p>匠工房には、デザイン力に優れた『一級建築士』と、ミリ単位の精度にこだわる『自社専属の熟練大工』が在籍しています。下請けへの丸投げは一切行いません。</p>
            <p>建物の見えない構造（耐震性・断熱性）からシッカリと見直し、10年後、20年後も「この家にして本当に良かった」と思える、一生涯の愛着を持てる住まいをご提案いたします。</p>
          </div>
          <div class="master-sign">
            <p>代表建築士・一級建築士</p>
            <p class="name">匠 建造</p>
          </div>
        </div>
        <div class="phil-img fade-target offset-delay">
          <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="設計図を引く建築士">
          <div class="badge">自社<br><span class="num">大工</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Service List -->
  <section class="section service bg-gray" id="service">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">S E R V I C E</span>
        <h2 class="sect-heading">リフォームメニュー・料金目安</h2>
        <p>※建物の広さや導入するメーカー設備により変動するため、プランニングとお見積り（無料）を通じて正確なご提案をいたします。</p>
      </div>

      <div class="srv-grid">
        <div class="srv-card fade-target">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1556910103-1c02745aae4d?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="水回りリフォーム">
          </div>
          <div class="srv-body">
            <h3><i data-lucide="droplets"></i> 水回りリフォーム</h3>
            <p>最新のシステムキッチンへの交換や、保温性の高いユニットバスへの改装。家事動線を劇的に改善します。</p>
            <div class="price">キッチン交換 <span>¥500,000〜</span></div>
          </div>
        </div>
        
        <div class="srv-card fade-target delay-1">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="リビング・内装">
          </div>
          <div class="srv-body">
            <h3><i data-lucide="sofa"></i> リビング・内装デザイン</h3>
            <p>間仕切り壁を撤去して広大なLDKを創出したり、無垢材のフローリングや漆喰・珪藻土などの自然素材を施工します。</p>
            <div class="price">LDK改装 <span>¥1,200,000〜</span></div>
          </div>
        </div>

        <div class="srv-card fade-target delay-2">
          <div class="srv-img">
            <img src="https://images.unsplash.com/photo-1513694203232-719a280e022f?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="フルリノベーション">
          </div>
          <div class="srv-body">
            <h3><i data-lucide="ruler"></i> フルリノベーション（まるごと）</h3>
            <p>中古物件の購入時や、親との同居時など。骨組み（スケルトン）状態から、断熱性・耐震性を引き上げる根本的な大改修。</p>
            <div class="price">マンション定額 <span>¥5,000,000〜</span></div>
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
        <h2 class="sect-heading">施工事例・お客様の声</h2>
      </div>

      <div class="works-wrap">
        <div class="work-item fade-target">
          <div class="wa-img">
            <div class="ba-tag">マンション フルリノベ</div>
            <img src="https://images.unsplash.com/photo-1484154218962-a197022b5858?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="施工事例1">
          </div>
          <div class="wa-text">
            <h3>「暗くて狭い」から「光が巡る大空間」へ。アイランドキッチンのある暮らし。</h3>
            <p>築30年の中古マンションを購入された30代ご夫婦からのご依頼。「細かく区切られた3LDK」の壁を大胆に取り払い、大空間の1LDKへとフルリノベーションしました。会話が弾むフルフラットのアイランドキッチンを採用し、週末には友人を招いてホームパーティーを楽しめる上質な空間が完成しました。</p>
          </div>
        </div>

        <div class="work-item reverse fade-target delay-1">
          <div class="wa-img">
            <div class="ba-tag">戸建て 水回り＆断熱</div>
            <img src="https://images.unsplash.com/photo-1584622781564-1d987f7333c1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="施工事例2">
          </div>
          <div class="wa-text">
            <h3>冬の寒空とおさらば。高断熱仕様の浴室と、ホテルライクな洗面台</h3>
            <p>「タイル張りのお風呂が寒すぎて限界」とお悩みだったご年配の施主様。浴室を最新のシステムバスに交換すると共に、窓をペアガラス（二重窓）に変更して徹底的な断熱対策を行いました。洗面台も造作（オーダーメイド）で設え、まるで高級ホテルのような優雅で暖かいパウダールームに生まれ変わりました。</p>
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
        <h2 class="sect-heading">ご相談から完成までの流れ</h2>
      </div>

      <div class="flow-list">
        <div class="flow-card fade-target">
          <div class="f-num">01</div>
          <h3>お問い合わせ・資料お取り寄せ</h3>
          <p>まずはお電話かWEBから資料（施工事例集）をご請求いただくか、現状のお悩みをご相談ください。しつこい後追い営業は致しません。</p>
        </div>
        <div class="flow-card fade-target delay-1">
          <div class="f-num">02</div>
          <h3>現地調査とライフスタイルのヒアリング</h3>
          <p>一級建築士がご自宅に伺い、正確な採寸をします。その際、「どんな暮らしがしたいか」「何が一番不便か」を徹底的にお聞かせください。</p>
        </div>
        <div class="flow-card fade-target delay-2">
          <div class="f-num">03</div>
          <h3>3Dパースを用いたプラン・お見積りご提示</h3>
          <p>設計図面だけでなく、完成後のイメージが直感的にわかる「3DCGパース」を作成してご提案します。ここまでは完全無料となります。</p>
        </div>
        <div class="flow-card fade-target">
          <div class="f-num">04</div>
          <h3>ご契約・着工・自社大工による施工</h3>
          <p>細部まで仕様が決まりましたらご契約となります。ご近所への挨拶回りを済ませた後、腕利きの自社大工が責任を持って工事を進めます。</p>
        </div>
        <div class="flow-card fade-target delay-1">
          <div class="f-num">05</div>
          <h3>お引き渡し・最長10年の保証システム</h3>
          <p>厳しい社内検査とお客様立会い検査を経て完成です。施工箇所については独自の保証書を発行し、施工後も定期点検のご連絡を差し上げます。</p>
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
          <summary>住みながらのリフォーム工事は可能ですか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>はい、お住まいになりながらの工事も対応可能です。水回り（キッチン、お風呂、トイレ）を何日間使えなくなるか等、生活への影響を最小限に抑える工程表をご提示し、エリアを区切りながら順次作業を進める工夫をいたします。</p></div>
        </details>
        <details class="faq-item fade-target">
          <summary>他社と「相見積もり」をしているのですが構いませんか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>はい、大歓迎です。リフォームは決して安くないお買い物ですので、複数社の提案や見積もりの詳細を比較検討されることを強く推奨しております。当社の提案内容に自信がありますので、じっくりとご検討ください。</p></div>
        </details>
        <details class="faq-item fade-target">
          <summary>中古マンションの物件探しから手伝ってもらえますか？<i data-lucide="chevron-down" class="faq-icon"></i></summary>
          <div class="faq-ans"><p>ワンストップリノベーション（物件探し＋設計施工）のサービスも提供しております。提携の不動産エージェントと共に内見に同行し、「この壁は抜ける構造か」「希望のリノベが予算内で可能か」をその場でプロの目線でアドバイスいたします。</p></div>
        </details>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section cta" id="contact">
    <div class="l-container">
      <div class="cta-inner fade-target">
        <div class="cta-head">
          <i data-lucide="home" class="cta-icon"></i>
          <h2>理想の住まいへの第一歩。</h2>
          <p>無料カタログの請求や、オンラインでのご相談も承っております。お気軽にお声がけください。</p>
        </div>
        <div class="cta-actions">
          <div class="tel-wrap">
            <span class="tel-text">一級建築士が丁寧にお話を伺います</span>
            <a href="tel:0120-000-000" class="tel-number"><i data-lucide="phone-call"></i> 0120-000-000</a>
          </div>
          <div class="btn-wrap">
            <a href="#" class="btn btn-primary"><i data-lucide="book-open"></i> 無料カタログ・事例集を請求する</a>
            <a href="#" class="btn btn-outline"><i data-lucide="mail"></i> WEBご相談フォーム</a>
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
            <i data-lucide="home"></i>
            <span>匠工房（タクミコウボウ）</span>
          </div>
          <p class="address">〒100-0000<br>東京都千代田区〇〇 1-2-3<br>・一級建築士事務所 第XXXX号<br>・建設業許可（般-X）第XXXX号<br>・住宅リフォーム瑕疵保険 登録事業者</p>
        </div>
        <div class="ft-nav">
          <ul class="ft-links">
             <li><a href="#philosophy">私たちの想い</a></li>
             <li><a href="#service">リフォームメニュー</a></li>
             <li><a href="#works">施工事例</a></li>
             <li><a href="#flow">ご相談の流れ</a></li>
             <li><a href="#faq">よくある質問</a></li>
          </ul>
        </div>
      </div>
      <div class="ft-bottom">
        <p>&copy; 2026 TAKUMI KOUBOU. All Rights Reserved.</p>
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

const_css = """
:root {
  --bg: #ffffff;
  --bg-gray: #f8fafc;
  --text: #334155;
  --text-muted: #64748b;
  --primary: #92400e; /* Luxury Amber / Bronze */
  --primary-hover: #b45309;
  font-family: 'Noto Sans JP', sans-serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { background: var(--bg); color: var(--text); line-height: 2; overflow-x: hidden; font-weight: 300; }

/* Containers */
.h-container { max-width: 1300px; margin: 0 auto; padding: 0 4%; display: flex; justify-content: space-between; align-items: center; height: 90px; transition: 0.4s; }
.l-container { max-width: 1100px; margin: 0 auto; padding: 0 5%; }
.section { padding: 140px 0; }
.bg-gray { background: var(--bg-gray); }
img { max-width: 100%; height: auto; display: block; }
.center { text-align: center; }

/* Typography */
h1, h2, h3, .logo { font-family: 'Shippori Mincho', serif; }
.en-label { font-family: 'Noto Sans JP', sans-serif; font-size: 0.85rem; letter-spacing: 0.3em; color: var(--primary); display: block; margin-bottom: 24px; font-weight: 500; }
.sect-heading { font-size: clamp(2.2rem, 4.5vw, 3.2rem); font-weight: 700; line-height: 1.4; margin-bottom: 64px; color: #1e293b; }

/* Header & Nav */
.header { position: fixed; width: 100%; top: 0; z-index: 1000; transition: all 0.4s; border-bottom: 1px solid rgba(0,0,0,0.05); background: transparent; }
.header.scrolled { background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); }
.header.scrolled .h-container { height: 75px; }
.logo { font-size: 1.6rem; font-weight: 700; display: flex; align-items: center; gap: 8px; color: #1e293b; letter-spacing: 0.1em; }
.nav { display: flex; align-items: center; gap: 40px; }
.nav-links { display: flex; list-style: none; gap: 32px; }
.nav-links a { text-decoration: none; color: var(--text); font-weight: 500; font-size: 0.95rem; transition: color 0.3s; }
.nav-links a:hover { color: var(--primary); }
.btn-nav { display: inline-flex; align-items: center; gap: 8px; background: var(--primary); color: #fff; padding: 12px 28px; border-radius: 4px; text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: background 0.3s; }
.btn-nav:hover { background: var(--primary-hover); }
.menu-toggle { display: none; background: none; border: none; cursor: pointer; width: 30px; height: 20px; position: relative; z-index: 1001; }
.menu-toggle span { display: block; width: 100%; height: 2px; background: var(--text); position: absolute; transition: 0.3s; }
.menu-toggle span:nth-child(1) { top: 0; }
.menu-toggle span:nth-child(2) { top: 9px; }
.menu-toggle span:nth-child(3) { bottom: 0; }

/* Hero */
.hero { height: 100vh; position: relative; display: flex; align-items: center; }
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; opacity: 0.9; }
.hero-mask { position: absolute; inset: 0; z-index: 1; background: linear-gradient(90deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.6) 50%, rgba(255,255,255,0) 100%); }
.hero-content { position: relative; z-index: 2; width: 100%; padding: 0 5%; max-width: 1400px; margin: 0 auto; display: flex; justify-content: flex-start; }
.vertical-text { writing-mode: vertical-rl; text-orientation: mixed; margin-left: 5%; }
.hero-title { font-size: clamp(3rem, 7vw, 6rem); line-height: 1.4; font-weight: 600; color: #1e293b; letter-spacing: 0.15em; }
.hero-hl { color: var(--primary); }
.hero-subtitle { font-size: clamp(1rem, 2vw, 1.15rem); color: var(--text); margin-left: 40px; margin-top: 40px; letter-spacing: 0.15em; line-height: 2.2; font-family: 'Shippori Mincho', serif; }
.scroll-down { position: absolute; bottom: 40px; left: 5%; display: flex; flex-direction: column; align-items: center; gap: 8px; color: var(--text); font-size: 0.85rem; letter-spacing: 0.2em; font-weight: 500; }
.scroll-down .line { width: 1px; height: 60px; background: rgba(0,0,0,0.1); position: relative; overflow: hidden; }
.scroll-down .line::before { content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 100%; background: var(--primary); animation: scrollDown 2s ease-in-out infinite; }
@keyframes scrollDown { 0% { top: -100%; } 100% { top: 100%; } }

/* Trouble */
.trouble-box { background: #fff; padding: 80px 60px; border-radius: 4px; box-shadow: 0 30px 60px rgba(0,0,0,0.05); border: 1px solid rgba(0,0,0,0.03); }
.t-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-bottom: 50px; justify-content: center; }
.t-item { text-align: center; }
.t-item i { width: 56px; height: 56px; color: var(--primary); margin-bottom: 24px; stroke-width: 1.5; }
.t-item p { font-size: 0.95rem; color: var(--text); text-align: justify; }
.t-answer { text-align: center; font-size: 1.3rem; padding: 30px; background: var(--bg-gray); color: var(--primary); border-radius: 4px; border-top: 4px solid var(--primary); font-family: 'Shippori Mincho', serif; font-weight: 600; }

/* Philosophy */
.phil-wrap { display: flex; gap: 100px; align-items: center; }
.phil-text { flex: 1.2; }
.phil-text .desc p { margin-bottom: 24px; color: var(--text); font-size: 1.05rem; text-align: justify; }
.master-sign { margin-top: 50px; border-left: 2px solid var(--primary); padding-left: 24px; }
.master-sign p { color: var(--text-muted); font-size: 0.9rem; margin-bottom: 4px; }
.master-sign .name { font-size: 1.8rem; font-weight: 600; color: #1e293b; font-family: 'Shippori Mincho', serif; }
.phil-img { flex: 1; position: relative; }
.phil-img img { box-shadow: -20px 20px 0 var(--bg-gray); }
.phil-img .badge { position: absolute; bottom: -40px; right: -20px; background: var(--primary); color: #fff; width: 130px; height: 130px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; font-weight: 500; font-family: 'Shippori Mincho', serif; line-height: 1.3; box-shadow: 0 10px 30px rgba(146,64,14,0.3); }
.phil-img .badge .num { font-size: 2.2rem; font-weight: 700; letter-spacing: 0; }

/* Service */
.srv-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 80px; }
.srv-card { background: #fff; box-shadow: 0 10px 40px rgba(0,0,0,0.03); transition: transform 0.4s, box-shadow 0.4s; display: flex; flex-direction: column; }
.srv-card:hover { transform: translateY(-8px); box-shadow: 0 20px 50px rgba(0,0,0,0.08); }
.srv-img img { height: 260px; width: 100%; object-fit: cover; }
.srv-body { padding: 40px 30px; flex: 1; display: flex; flex-direction: column; }
.srv-body h3 { font-size: 1.4rem; margin-bottom: 20px; display: flex; align-items: center; gap: 12px; color: #1e293b; }
.srv-body h3 i { color: var(--primary); width: 24px; height: 24px; stroke-width: 1.5; }
.srv-body p { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 30px; flex: 1; }
.srv-card .price { font-size: 1rem; color: var(--text); font-weight: 500; display: flex; justify-content: space-between; align-items: baseline; border-top: 1px solid rgba(0,0,0,0.05); padding-top: 20px; }
.srv-card .price span { font-size: 1.6rem; font-family: 'Shippori Mincho', serif; color: var(--primary); font-weight: 700; }

/* Works */
.works-wrap { display: flex; flex-direction: column; gap: 120px; margin-top: 80px; }
.work-item { display: flex; gap: 80px; align-items: center; }
.work-item.reverse { flex-direction: row-reverse; }
.wa-img { flex: 1.2; position: relative; }
.wa-img::before { content:''; position:absolute; inset: -20px 20px 20px -20px; background: var(--bg-gray); z-index: -1; }
.work-item.reverse .wa-img::before { inset: -20px -20px 20px 20px; }
.ba-tag { position: absolute; top: -15px; left: 30px; background: #fff; color: var(--text); padding: 12px 30px; font-weight: 500; font-size: 0.9rem; box-shadow: 0 10px 30px rgba(0,0,0,0.1); z-index: 2; letter-spacing: 0.1em; }
.wa-img img { box-shadow: 0 20px 50px rgba(0,0,0,0.1); width: 100%; height: auto; aspect-ratio: 4/3; object-fit: cover; }
.wa-text { flex: 1; }
.wa-text h3 { font-size: 1.8rem; line-height: 1.6; margin-bottom: 30px; color: #1e293b; }
.wa-text p { color: var(--text-muted); font-size: 1.05rem; text-align: justify; }

/* Flow */
.flow-list { margin-top: 80px; display: grid; gap: 30px; counter-reset: flow-counter; }
.flow-card { background: #fff; padding: 40px 50px; display: flex; gap: 60px; align-items: flex-start; border-bottom: 1px solid rgba(0,0,0,0.05); position: relative; }
.f-num { font-family: 'Shippori Mincho', serif; font-size: 3rem; color: var(--primary); font-weight: 700; line-height: 1; min-width: 60px; opacity: 0.8; }
.flow-card h3 { font-size: 1.35rem; margin-bottom: 12px; color: #1e293b; }
.flow-card p { color: var(--text-muted); font-size: 1rem; }
.flow-content { flex: 1; }

/* FAQ */
.faq-accordion { margin-top: 80px; max-width: 900px; margin-left: auto; margin-right: auto; }
.faq-item { background: #fff; margin-bottom: 20px; border: 1px solid rgba(0,0,0,0.05); box-shadow: 0 4px 15px rgba(0,0,0,0.02); }
.faq-item summary { padding: 30px 40px; font-weight: 600; font-size: 1.15rem; cursor: pointer; list-style: none; display: flex; justify-content: space-between; align-items: center; outline: none; color: #1e293b; }
.faq-item summary::-webkit-details-marker { display: none; }
.faq-icon { transition: transform 0.3s; color: var(--text-muted); }
.faq-ans { padding: 0 40px 30px; color: var(--text-muted); font-size: 1rem; line-height: 1.9; }

/* CTA */
.cta { padding: 160px 0; background: var(--bg-gray); }
.cta-inner { background: #fff; padding: 100px 60px; text-align: center; border: 1px solid rgba(0,0,0,0.03); box-shadow: 0 30px 80px rgba(0,0,0,0.04); }
.cta-icon { width: 56px; height: 56px; color: var(--primary); margin-bottom: 30px; stroke-width: 1; }
.cta-head h2 { font-size: 2.8rem; margin-bottom: 20px; color: #1e293b; }
.cta-head p { color: var(--text-muted); font-size: 1.1rem; margin-bottom: 60px; }
.cta-actions { display: flex; flex-direction: column; gap: 40px; align-items: center; }
.tel-wrap { display: flex; flex-direction: column; gap: 12px; }
.tel-text { font-size: 0.95rem; color: var(--text); font-weight: 500; letter-spacing: 0.1em; }
.tel-number { font-size: 3.5rem; font-family: 'Shippori Mincho', serif; font-weight: 600; color: var(--primary); text-decoration: none; display: flex; align-items: center; gap: 16px; line-height: 1; }
.btn-wrap { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 12px; padding: 18px 40px; font-weight: 500; text-decoration: none; transition: all 0.3s; font-size: 1.05rem; }
.btn-primary { background: var(--primary); color: #fff; }
.btn-primary:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 30px rgba(146,64,14,0.2); }
.btn-outline { background: #fff; color: var(--text); border: 1px solid rgba(0,0,0,0.1); }
.btn-outline:hover { background: var(--bg-gray); }

/* Footer */
.footer { border-top: 1px solid rgba(0,0,0,0.05); padding: 100px 0 40px; background: #fff; }
.ft-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; margin-bottom: 80px; }
.ft-brand .logo { margin-bottom: 30px; }
.ft-brand .address { color: var(--text-muted); line-height: 2.2; font-size: 0.95rem; }
.ft-links { list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }
.ft-links a { color: var(--text-muted); text-decoration: none; transition: color 0.3s; font-size: 0.95rem; }
.ft-links a:hover { color: var(--primary); }
.ft-bottom { border-top: 1px solid rgba(0,0,0,0.05); padding-top: 40px; text-align: center; color: var(--text-muted); font-size: 0.85rem; letter-spacing: 0.1em; }

/* Animations */
.fade-target { opacity: 0; transform: translateY(40px); transition: opacity 1s ease, transform 1s cubic-bezier(0.16,1,0.3,1); }
.fade-target.is-visible { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.15s; }
.delay-2 { transition-delay: 0.3s; }
.delay-3 { transition-delay: 0.45s; }
.offset-delay { transition-delay: 0.2s; }

/* Mobile */
@media (max-width: 900px) {
  .vertical-text { margin-left: 0; margin-bottom: 40px; }
  .t-list, .srv-grid { grid-template-columns: 1fr; }
  .phil-wrap, .work-item, .wa-img { flex-direction: column !important; gap: 40px; }
  .flow-card { flex-direction: column; align-items: flex-start; gap: 20px; }
  .ft-grid { grid-template-columns: 1fr; gap: 40px; }
  .nav-links, .btn-nav { display: none; }
  .menu-toggle { display: block; }
}
"""

with open(r'd:\sharkstars\demos\construction-01\index.html', 'w', encoding='utf-8') as f:
    f.write(const_html.strip())

with open(r'd:\sharkstars\demos\construction-01\assist\css\style.css', 'w', encoding='utf-8') as f:
    f.write(const_css.strip())

print("construction-01 HTML and CSS rewritten successfully.")
