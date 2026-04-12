import os

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cooking Studio 旬彩 | 少人数制フランス家庭料理教室</title>
  <meta name="description" content="旬の食材を使った一生モノの料理メソッドを学ぶ。初心者から通える最大4名の少人数制・完全予約制キッチンスタジオ「Cooking Studio 旬彩（しゅんさい）」。">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600;800&family=Zen+Kaku+Gothic+New:wght@300;400;500;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="assist/css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  
  <!-- Header -->
  <header class="header" id="header">
    <div class="h-container">
      <div class="logo">
        <span class="logo-jp">Cooking Studio 旬彩</span>
        <span class="logo-sub">COOKING STUDIO SHUNSAI</span>
      </div>
      <nav class="nav">
        <ul class="nav-links">
          <li><a href="#concept">私たちの想い</a></li>
          <li><a href="#menu">レッスンメニュー</a></li>
          <li><a href="#flow">体験の流れ</a></li>
          <li><a href="#faq">よくあるご質問</a></li>
        </ul>
        <a href="#contact" class="btn btn-nav">体験レッスンを予約する</a>
      </nav>
      <button class="menu-toggle" id="menuToggle" aria-label="メニューを開く">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-bg">
      <img src="assist/images/hero.png" alt="美しいキッチンカウンター">
    </div>
    <div class="hero-mask"></div>
    <div class="hero-content fade-target">
      <div class="hero-text-box">
        <p class="hero-sub fade-target delay-1">基礎からきちんと学べる、少人数制料理教室</p>
        <h1 class="hero-title fade-target delay-2">今日のご飯が、<br>もっと楽しみになる。</h1>
        <p class="hero-desc fade-target delay-3">旬の食材に触れ、丁寧に作って、美味しく味わう。<br>一生モノの「料理の基本」を、心地よいキッチンスタジオで。</p>
      </div>
    </div>
  </section>

  <!-- Trouble Section -->
  <section class="section trouble bg-white" id="trouble">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">WORRIES</span>
        <h2 class="sect-heading">料理について、こんなお悩みはありませんか？</h2>
      </div>
      
      <div class="trouble-grid">
        <div class="trouble-item fade-target delay-1">
          <div class="t-icon"><i data-lucide="smartphone"></i></div>
          <h3>レシピを見ないと作れない</h3>
          <p>クックパッドなどのレシピサイトを見ながらでないと、分量や手順が分からず、全く料理が作れない。</p>
        </div>
        <div class="trouble-item fade-target delay-2">
          <div class="t-icon"><i data-lucide="utensils"></i></div>
          <h3>いつも味がブレてしまう</h3>
          <p>同じ料理を作っているはずなのに、日によって味が濃かったり薄かったりして美味しく仕上がらない。</p>
        </div>
        <div class="trouble-item fade-target delay-3">
          <div class="t-icon"><i data-lucide="shopping-bag"></i></div>
          <h3>お惣菜ばかりで罪悪感</h3>
          <p>仕事帰りにスーパーのお惣菜やコンビニ弁当ばかり買ってしまい、体調もエンゲル係数も心配…。</p>
        </div>
      </div>
      
      <div class="trouble-answer fade-target">
        <p><strong>「Cooking Studio 旬彩」は、レシピの暗記ではなく<br>一生使える「料理の理論と基本」を身につける料理教室です。</strong></p>
      </div>
    </div>
  </section>

  <!-- Philosophy Section -->
  <section class="section philosophy" id="concept">
    <div class="l-container">
      <div class="phil-wrap">
        <div class="phil-img fade-target offset-delay">
          <img src="assist/images/concept.png" alt="笑顔で教える講師">
        </div>
        <div class="phil-text fade-target">
          <span class="en-label">CONCEPT</span>
          <h2 class="sect-heading">「見るだけ」で終わらない、<br>確かな料理の実力を。</h2>
          <div class="desc">
            <p>大人数の料理教室にありがちな、「先生が作るのを見ていただけで、結局自分では何も身に付かなかった」という経験はありませんか？</p>
            <p>当スタジオは、すべてのレッスンが<strong>【最大4名までの超少人数制】</strong>です。一人ひとりの包丁の持ち方から、火加減の微細な調整、味付けのタイミングまで、講師が隣で徹底的にサポートします。</p>
            <p>レシピの手順をなぞるのではなく、「なぜここで弱火にするのか」「なぜこの調味料を先に入れるのか」という<strong>『理屈』</strong>を丁寧に解説。だからこそ、家に帰ってからも一人で確実に美味しい料理を再現できるようになるのです。</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Menu Section -->
  <section class="section menu bg-leaf" id="menu">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">LESSON MENU</span>
        <h2 class="sect-heading">レッスンメニュー</h2>
        <p>受講者様のレベルや目的に合わせた3つの特化コースをご用意しました。</p>
      </div>

      <div class="menu-list">
        <!-- Course 1 -->
        <div class="menu-card fade-target">
          <div class="mc-img">
            <img src="assist/images/basic.png" alt="肉じゃがなどの基礎料理">
            <div class="mc-badge">人気 No.1</div>
          </div>
          <div class="mc-body">
            <h3>家庭料理・基礎クラス</h3>
            <p>包丁の正しい持ち方や、一番出汁の取り方といった「基本のキ」から学べるコース。「肉じゃが」「だし巻き卵」「ハンバーグ」など、絶対に失敗したくない愛され家庭料理をマスターします。</p>
            <ul class="mc-points">
              <li><i data-lucide="check-circle-2"></i> 料理経験ゼロの初心者の方に最適</li>
              <li><i data-lucide="check-circle-2"></i> 基礎中の基礎から一生モノのスキルへ</li>
            </ul>
            <div class="mc-price"><span>¥6,600</span> / 1回（材料費込）</div>
          </div>
        </div>

        <!-- Course 2 -->
        <div class="menu-card fade-target delay-1">
          <div class="mc-img">
            <img src="assist/images/course.png" alt="おもてなし用コース料理">
          </div>
          <div class="mc-body">
            <h3>おもてなし・彩りクラス</h3>
            <p>ホームパーティーや記念日など、特別な日に作ってあげたい「ちょっと豪華で華やかな」料理を学ぶクラス。フレンチやイタリアンの要素を取り入れた見栄えするコース仕立ての献立を作ります。</p>
            <ul class="mc-points">
              <li><i data-lucide="check-circle-2"></i> 盛り付けの美しいテクニックも習得</li>
              <li><i data-lucide="check-circle-2"></i> ペアリング用のワインもご用意（試食時）</li>
            </ul>
            <div class="mc-price"><span>¥8,800</span> / 1回（材料費込）</div>
          </div>
        </div>

        <!-- Course 3 -->
        <div class="menu-card fade-target delay-2">
          <div class="mc-img">
            <img src="assist/images/fish.png" alt="魚のさばき方">
          </div>
          <div class="mc-body">
            <h3>魚介さばき方・特訓クラス</h3>
            <p>「スーパーで丸ごとの魚を見ても、どうしていいか分からない」という方向けの専門特化クラス。アジの三枚おろしなど、基本から魚を綺麗にさばく技術を徹底的にご指導いたします。</p>
            <ul class="mc-points">
              <li><i data-lucide="check-circle-2"></i> アジ、イカ、鯛など旬の魚介を使用</li>
              <li><i data-lucide="check-circle-2"></i> 刺身、煮付け、アラ汁まで余す所なく調理</li>
            </ul>
            <div class="mc-price"><span>¥9,900</span> / 1回（材料費込）</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Flow Section -->
  <section class="section flow" id="flow">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">TRIAL FLOW</span>
        <h2 class="sect-heading">体験レッスンの流れ</h2>
      </div>

      <div class="flow-steps">
        <div class="step-card fade-target">
          <div class="s-num">01</div>
          <div class="s-text">
            <h3>手ぶらでご来店</h3>
            <p>Webからご予約の上、開始5分前にお越しください。エプロン、お手拭き、レシピバインダーはこちらで全てご用意しておりますので、お仕事帰りでも手ぶらでそのまま参加可能です。</p>
          </div>
        </div>
        <div class="step-card fade-target delay-1">
          <div class="s-num">02</div>
          <div class="s-text">
            <h3>レシピの理論説明（15分）</h3>
            <p>まずは座学で「なぜその材料を使うのか」「どうしてその温度で焼くのか」という調理の裏にある『仕組みと理論』を分かりやすく解説します。</p>
          </div>
        </div>
        <div class="step-card fade-target delay-2">
          <div class="s-num">03</div>
          <div class="s-text">
            <h3>調理実習（90分）</h3>
            <p>講師のお手本を見た後、最大4名の少人数グループで調理開始です。講師が常に横について、包丁の角度やフライパンの振り方など細かなポイントを直接指導します。</p>
          </div>
        </div>
        <div class="step-card fade-target delay-3">
          <div class="s-num">04</div>
          <div class="s-text">
            <h3>試食・ご質問（30分）</h3>
            <p>完成した料理を、温かみのあるダイニングテーブルでいただきます。食べながら、分からなかったところを質問したり、次回の予約を取ることも可能です。無理な勧誘は一切ありません。</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section class="section faq bg-light" id="faq">
    <div class="l-container">
      <div class="sect-header center fade-target">
        <span class="en-label">Q &amp; A</span>
        <h2 class="sect-heading">よくあるご質問</h2>
      </div>
      
      <div class="faq-list">
        <div class="faq-item fade-target">
          <div class="faq-q">
            <span class="q-icon">Q</span>
            包丁の持ち方も分からない全くの初心者ですが、大丈夫ですか？
          </div>
          <div class="faq-a">
            <span class="a-icon">A</span>
            <p>もちろん大丈夫です！基礎クラスの受講生のうち、約8割が「自己流でしかやったことがない」「全く料理をしてこなかった」という方々です。少人数制なので、他の方のペースを気にすることなく、基本のキから丁寧にお教えします。</p>
          </div>
        </div>
        <div class="faq-item fade-target">
          <div class="faq-q">
            <span class="q-icon">Q</span>
            男性でも受講することは可能ですか？
          </div>
          <div class="faq-a">
            <span class="a-icon">A</span>
            <p>はい、大歓迎です。近年は「自分で美味しいおつまみを作りたい」「魚をさばけるようになりたい」という男性の受講生様も非常に増えております。和気あいあいとしたアットホームな雰囲気ですのでご安心ください。</p>
          </div>
        </div>
        <div class="faq-item fade-target">
          <div class="faq-q">
            <span class="q-icon">Q</span>
            材料費などは別途かかりますか？
          </div>
          <div class="faq-a">
            <span class="a-icon">A</span>
            <p>いいえ、表示されているレッスン料金には「材料費」「エプロン・タオルのレンタル代」「レシピ代」がすべて含まれております。当日追加でお支払いいただくものはございません。</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <section class="cta" id="contact">
    <div class="cta-inner fade-target">
      <h2 class="cta-title">まずは体験レッスンへ<br>お越しください！</h2>
      <p class="cta-desc">初回限定、ワンコイン（500円）で基礎クラスの体験レッスンを受講可能です。<br>皆様のご参加を心よりお待ちしております。</p>
      
      <div class="cta-buttons">
        <a href="#" class="btn btn-primary"><i data-lucide="calendar"></i> 24時間WEB予約</a>
        <a href="#" class="btn btn-line"><i data-lucide="message-circle"></i> LINEで質問・予約する</a>
      </div>
      <p class="cta-note">※お電話（03-XXXX-XXXX）でのご予約も承っております。</p>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="l-container">
      <div class="footer-grid">
        <div class="footer-info">
          <div class="logo">
            <span class="logo-jp">Cooking Studio 旬彩</span>
          </div>
          <p class="address">〒150-0001<br>東京都渋谷区神宮前 X-X-X 1階<br>JR原宿駅 徒歩5分</p>
          <p class="hours">営業時間：10:00 - 21:00（月曜定休）</p>
        </div>
        <div class="footer-links">
          <a href="#concept">私たちの想い</a>
          <a href="#menu">レッスンメニュー</a>
          <a href="#flow">体験の流れ</a>
          <a href="#faq">よくあるご質問</a>
        </div>
      </div>
      <div class="footer-copy">
        &copy; 2026 Cooking Studio Shunsai. All Rights Reserved.
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
  </script>
</body>
</html>
"""

css_content = """
:root {
  --bg-white: #fdfcf9;
  --bg-light: #f5f3ed;
  --bg-leaf: #e9ece4;
  --text-main: #4a453f;
  --text-light: #7a736a;
  --primary: #75866d; /* Sage green */
  --primary-hover: #5d6d56;
  --accent: #d4a373; /* Warm wooden accent */
  
  --font-base: 'Zen Kaku Gothic New', sans-serif;
  --font-serif: 'Shippori Mincho', serif;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { background: var(--bg-white); color: var(--text-main); font-family: var(--font-base); line-height: 1.8; overflow-x: hidden; }

img { max-width: 100%; height: auto; display: block; }
a { text-decoration: none; color: inherit; }
.center { text-align: center; }

/* Containers */
.h-container { max-width: 1200px; margin: 0 auto; padding: 0 4%; display: flex; justify-content: space-between; align-items: center; height: 90px; transition: 0.3s; }
.l-container { max-width: 1000px; margin: 0 auto; padding: 0 5%; }
.section { padding: 120px 0; }
.bg-light { background: var(--bg-light); }
.bg-leaf { background: var(--bg-leaf); }

/* Typography */
h1, h2, h3 { font-family: var(--font-serif); font-weight: 500; color: #3d3834; }
.en-label { display: block; font-size: 0.9rem; font-family: var(--font-base); font-weight: 700; letter-spacing: 0.15em; color: var(--primary); margin-bottom: 20px; text-transform: uppercase; }
.sect-heading { font-size: clamp(2rem, 4vw, 2.8rem); line-height: 1.4; margin-bottom: 60px; }

/* Header */
.header { position: fixed; width: 100%; top: 0; z-index: 1000; transition: 0.3s; background: transparent; border-bottom: 1px solid rgba(255,255,255,0.1); }
.header.scrolled { background: rgba(253,252,249,0.95); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.05); border-bottom: none; }
.header.scrolled .logo-jp { color: var(--text-main); }
.header.scrolled .nav-links a { color: var(--text-main); }
.logo { display: flex; flex-direction: column; }
.logo-jp { font-family: var(--font-serif); font-size: 1.8rem; font-weight: 600; color: var(--bg-white); transition: color 0.3s; }
.logo-sub { font-size: 0.7rem; letter-spacing: 0.1em; color: var(--primary); }
.nav { display: flex; align-items: center; gap: 40px; }
.nav-links { display: flex; list-style: none; gap: 30px; }
.nav-links a { color: var(--bg-white); font-weight: 500; transition: color 0.3s; }
.nav-links a:hover { color: var(--primary); }
.btn-nav { display: inline-flex; align-items: center; background: var(--primary); color: #fff; padding: 10px 24px; border-radius: 50px; font-weight: 500; font-size: 0.95rem; transition: 0.3s; }
.btn-nav:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 4px 12px rgba(117,134,109,0.3); }

/* Mobile Menu */
.menu-toggle { display: none; background: none; border: none; width: 30px; height: 20px; cursor: pointer; position: relative; z-index: 1001; }
.menu-toggle span { display: block; position: absolute; width: 100%; height: 2px; background: var(--primary); transition: 0.3s; }
.header.scrolled .menu-toggle span { background: var(--text-main); }
.menu-toggle span:nth-child(1) { top: 0; }
.menu-toggle span:nth-child(2) { top: 9px; }
.menu-toggle span:nth-child(3) { bottom: 0; }

/* Hero */
.hero { height: 100vh; position: relative; display: flex; align-items: center; justify-content: flex-start; }
.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-bg img { width: 100%; height: 100%; object-fit: cover; }
.hero-mask { position: absolute; inset: 0; z-index: 1; background: linear-gradient(90deg, rgba(30,30,30,0.6) 0%, rgba(30,30,30,0) 100%); }
.hero-content { position: relative; z-index: 2; width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 5%; }
.hero-text-box { color: #fff; }
.hero-sub { display: inline-block; background: var(--primary); color: #fff; padding: 6px 16px; font-size: 0.9rem; font-weight: 500; letter-spacing: 0.05em; border-radius: 4px; margin-bottom: 24px; }
.hero-title { font-size: clamp(2.5rem, 6vw, 4.5rem); line-height: 1.4; color: #fff; text-shadow: 0 4px 20px rgba(0,0,0,0.2); margin-bottom: 24px; }
.hero-desc { font-size: clamp(1rem, 2vw, 1.2rem); font-weight: 500; text-shadow: 0 2px 10px rgba(0,0,0,0.3); }

/* Trouble */
.trouble-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-bottom: 60px; }
.trouble-item { text-align: center; padding: 40px 30px; background: var(--bg-light); border-radius: 8px; border-top: 4px solid var(--primary); }
.t-icon { color: var(--accent); margin-bottom: 20px; }
.t-icon svg { width: 40px; height: 40px; }
.trouble-item h3 { font-size: 1.2rem; margin-bottom: 16px; font-weight: 600; font-family: var(--font-base); color: var(--text-main); }
.trouble-item p { font-size: 0.95rem; color: var(--text-light); text-align: justify; }
.trouble-answer { text-align: center; font-size: 1.3rem; font-family: var(--font-serif); padding-top: 40px; border-top: 1px dashed rgba(0,0,0,0.1); color: var(--primary); line-height: 1.8; }

/* Philosophy */
.phil-wrap { display: flex; gap: 80px; align-items: center; }
.phil-img { flex: 1; border-radius: 200px 200px 0 0; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.05); }
.phil-img img { width: 100%; height: 100%; object-fit: cover; aspect-ratio: 4/5; }
.phil-text { flex: 1.1; }
.phil-text .desc p { margin-bottom: 20px; color: var(--text-light); text-align: justify; }

/* Menu */
.menu-list { display: flex; flex-direction: column; gap: 40px; }
.menu-card { display: flex; background: var(--bg-white); border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.03); transition: transform 0.4s; border: 1px solid rgba(0,0,0,0.02); }
.menu-card:hover { transform: translateY(-5px); box-shadow: 0 15px 40px rgba(0,0,0,0.06); }
.mc-img { flex: 0 0 400px; position: relative; }
.mc-img img { width: 100%; height: 100%; object-fit: cover; }
.mc-badge { position: absolute; top: 20px; left: 20px; background: var(--accent); color: #fff; padding: 6px 16px; font-family: var(--font-base); font-weight: 700; border-radius: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
.mc-body { padding: 40px 50px; flex: 1; display: flex; flex-direction: column; }
.mc-body h3 { font-size: 1.6rem; color: var(--primary); margin-bottom: 20px; border-bottom: 1px solid rgba(117,134,109,0.2); padding-bottom: 10px; }
.mc-body p { color: var(--text-main); margin-bottom: 24px; text-align: justify; }
.mc-points { list-style: none; margin-bottom: 30px; }
.mc-points li { display: flex; align-items: center; gap: 8px; color: var(--text-main); font-weight: 500; margin-bottom: 8px; }
.mc-points li i { color: var(--primary); width: 18px; height: 18px; }
.mc-price { margin-top: auto; font-size: 1rem; color: var(--text-light); text-align: right; }
.mc-price span { font-size: 1.8rem; font-weight: 700; color: #3d3834; font-family: var(--font-base); margin-right: 4px; }

/* Flow */
.flow-steps { position: relative; padding-left: 20px; border-left: 2px dashed rgba(117,134,109,0.3); margin-top: 60px; max-width: 800px; margin-left: auto; margin-right: auto; }
.step-card { position: relative; margin-bottom: 50px; padding-left: 40px; }
.step-card:last-child { margin-bottom: 0; }
.s-num { position: absolute; left: -40px; top: 0; width: 40px; height: 40px; background: var(--primary); color: #fff; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-weight: 700; font-family: var(--font-base); font-size: 1.1rem; box-shadow: 0 0 0 6px var(--bg-white); }
.s-text h3 { font-size: 1.3rem; margin-bottom: 12px; font-family: var(--font-base); font-weight: 700; color: var(--primary); }
.s-text p { color: var(--text-light); text-align: justify; }

/* FAQ */
.faq-list { max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px; }
.faq-item { background: var(--bg-white); border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); overflow: hidden; }
.faq-q { padding: 24px 30px; display: flex; align-items: flex-start; gap: 16px; font-weight: 700; font-family: var(--font-base); font-size: 1.1rem; color: var(--primary); }
.q-icon { display: block; flex: 0 0 32px; height: 32px; background: var(--primary); color: #fff; border-radius: 50%; text-align: center; line-height: 32px; font-size: 1rem; }
.faq-a { padding: 0 30px 24px 78px; display: flex; align-items: flex-start; gap: 16px; color: var(--text-main); }
.a-icon { display: block; flex: 0 0 32px; height: 32px; background: var(--accent); color: #fff; border-radius: 50%; text-align: center; line-height: 32px; font-size: 1rem; margin-left: -48px;}

/* CTA */
.cta { padding: 120px 5%; background: var(--primary); background-image: radial-gradient(circle at top right, rgba(255,255,255,0.1), transparent 40%); color: #fff; text-align: center; }
.cta-title { font-size: clamp(2rem, 4vw, 2.5rem); color: #fff; margin-bottom: 24px; }
.cta-desc { font-size: 1.1rem; margin-bottom: 40px; font-weight: 300; }
.cta-buttons { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-bottom: 20px; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 18px 40px; border-radius: 50px; font-weight: 700; font-size: 1.1rem; transition: 0.3s; min-width: 280px; }
.btn-primary { background: #fff; color: var(--primary); }
.btn-primary:hover { background: var(--bg-light); transform: translateY(-3px); }
.btn-line { background: #06c755; color: #fff; }
.btn-line:hover { background: #05a546; transform: translateY(-3px); }
.cta-note { font-size: 0.85rem; opacity: 0.8; }

/* Footer */
.footer { background: #FAFDF7; padding: 80px 0 30px; border-top: 1px solid rgba(117,134,109,0.2); color: var(--text-main); }
.footer-grid { display: flex; justify-content: space-between; margin-bottom: 60px; max-width: 1000px; margin-left: auto; margin-right: auto; }
.footer-info .logo-jp { font-size: 1.5rem; color: var(--primary); display: block; margin-bottom: 20px; }
.footer-info p { font-size: 0.9rem; line-height: 1.8; color: var(--text-light); }
.footer-links { display: flex; flex-direction: column; gap: 15px; }
.footer-links a { color: var(--primary); font-weight: 500; font-size: 0.95rem; }
.footer-links a:hover { text-decoration: underline; }
.footer-copy { text-align: center; border-top: 1px solid rgba(117,134,109,0.2); padding-top: 30px; font-size: 0.8rem; letter-spacing: 0.05em; color: var(--text-light); }

/* Animation Utils */
.fade-target { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease, transform 0.8s cubic-bezier(0.16,1,0.3,1); }
.fade-target.is-visible { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.15s; }
.delay-2 { transition-delay: 0.3s; }
.delay-3 { transition-delay: 0.45s; }
.offset-delay { transition-delay: 0.2s; }

/* Responsive */
@media (max-width: 900px) {
  .trouble-grid { grid-template-columns: 1fr; gap: 20px; }
  .phil-wrap { flex-direction: column; gap: 40px; }
  .phil-img { border-radius: 40px; }
  .menu-card { flex-direction: column; }
  .mc-img { flex: auto; height: 250px; }
  .footer-grid { flex-direction: column; gap: 40px; text-align: center; }
  .footer-links { text-align: center; }
  .nav-links, .btn-nav { display: none; }
  .menu-toggle { display: block; }
  .header.scrolled .logo-jp { color: var(--primary); }
}
"""

with open(r'd:\sharkstars\demos\cooking-01\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content.strip())

with open(r'd:\sharkstars\demos\cooking-01\assist\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css_content.strip())

print("cooking-01 HTML and CSS rewritten successfully.")
