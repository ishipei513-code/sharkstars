# 株式会社Bolon Shareee コーポレートサイト Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 株式会社Bolon Shareeeのコーポレートサイト兼B.villeaサロン集客LPを `client/bolon-shareee/` に6ページ構成で構築する。

**Architecture:** 静的HTML/CSS/JS。`client/muku/` の構造を継承（reset.css + style.css + main.js + 各HTMLページ）し、デザインシステムだけ B.villea 用に差し替える。index.html は10セクションの縦長LP。残り5ページ（school / company / faq / contact / privacy）はindex確立後に共通CSSを使い回す。

**Tech Stack:** Static HTML5, CSS3 (CSS variables, grid, flex), Vanilla JS (IntersectionObserver, mobile nav toggle), Google Fonts (Zen Old Mincho / Cormorant Garamond / Zen Kaku Gothic Antique), Unsplash for placeholder imagery, JSON-LD for structured data.

**Spec reference:** `docs/superpowers/specs/2026-05-12-bolon-shareee-website-design.md`

---

## File Structure (生成・編集対象)

```
client/bolon-shareee/
├── index.html        — 縦長LP（10セクション）
├── school.html       — バストスクール詳細
├── company.html      — 会社情報詳細（3事業入口）
├── faq.html          — 全FAQ
├── contact.html      — LINE誘導 + フォーム + アクセス
├── privacy.html      — プラポリ
├── css/
│   ├── reset.css     — muku/css/reset.css をコピー（変更なし）
│   └── style.css     — 新規。デザイントークン + 全セクションスタイル
├── js/
│   └── main.js       — muku/js/main.js をコピー、軽くカスタム
└── images/
    ├── logo.svg      — Bolon Shareee テキストロゴ
    └── ogp.png       — 1200×630 OGP画像

# 既存ファイルも編集対象
sitemap.xml           — 新ページ6件を追加
index.html (ルート)    — 「制作実績」ブロックにB.villea追加
```

**変更しないファイル**: `client/muku/`, `client/abe-seitai/`, `client/libre/`, `demos/`, `blog/`, `ko/`, その他既存サイト全部。

---

## デザイン定数（全タスクで参照）

```css
/* カラーパレット — E. Editorial × Gold（ゴールド控えめ）*/
--primary: #C8276B;       /* ブーゲンビリア赤紫 */
--bg-base: #FFFFFF;        /* 純白 */
--bg-warm: #FBF6EF;        /* クリーム */
--gold: #D4A657;           /* シャンパンゴールド — 控えめ運用のみ */
--text-main: #3A1A2A;      /* ディープワイン */
--text-sub: #5A4050;       /* ローズグレー */
--border: #EDE4DC;         /* アイボリーグレー */

/* タイポ — C. Old Luxe */
--font-jp-serif: 'Zen Old Mincho', serif;
--font-en-serif: 'Cormorant Garamond', serif;
--font-jp-sans: 'Zen Kaku Gothic Antique', sans-serif;
```

**ゴールド使用ルール（厳守）**: リンクホバー下線・1px区切り線・縦書きBrandマークの英字 だけ。CTAボタンや見出しには使わない（赤紫主導）。

---

## Phase 1: Foundation（Day 1）

### Task 1: フォルダ構造とアセットの初期セットアップ

**Files:**
- Create: `client/bolon-shareee/css/reset.css` (muku からコピー)
- Create: `client/bolon-shareee/js/main.js` (muku からコピー + ヘッダーコメント変更)
- Create: `client/bolon-shareee/images/.gitkeep`

- [ ] **Step 1: フォルダを作成**

```bash
mkdir -p client/bolon-shareee/css
mkdir -p client/bolon-shareee/js
mkdir -p client/bolon-shareee/images
```

- [ ] **Step 2: reset.css を muku から複製（変更不要）**

```bash
cp client/muku/css/reset.css client/bolon-shareee/css/reset.css
```

- [ ] **Step 3: main.js を muku から複製しヘッダーコメントだけ書き換え**

`client/bolon-shareee/js/main.js` を作成。muku の `js/main.js` 全文をコピーした上で、1行目のコメントを以下に差し替え：

```js
/* 株式会社Bolon Shareee / B.villea — Interactive scripts */
```

- [ ] **Step 4: ファイル存在確認**

```bash
ls client/bolon-shareee/css/reset.css client/bolon-shareee/js/main.js
```
Expected: 両ファイルが listed される。

- [ ] **Step 5: Commit**

```bash
git add client/bolon-shareee/
git commit -m "feat(bolon-shareee): scaffold folder structure with reset.css and main.js"
```

---

### Task 2: style.css — デザイントークン + ベース

**Files:**
- Create: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: style.css ヘッダーとCSS変数を書く**

`client/bolon-shareee/css/style.css` を新規作成：

```css
/* ============================================================
   株式会社Bolon Shareee / B.villea
   Design System: E. Editorial × Gold ／ C. Old Luxe Typography
   ============================================================ */

:root {
  /* Colors */
  --primary: #C8276B;
  --primary-deep: #A11E55;
  --bg-base: #FFFFFF;
  --bg-warm: #FBF6EF;
  --gold: #D4A657;
  --text-main: #3A1A2A;
  --text-sub: #5A4050;
  --border: #EDE4DC;

  /* Typography */
  --font-jp-serif: 'Zen Old Mincho', serif;
  --font-en-serif: 'Cormorant Garamond', serif;
  --font-jp-sans: 'Zen Kaku Gothic Antique', sans-serif;

  /* Spacing scale */
  --space-xs: 8px;
  --space-sm: 16px;
  --space-md: 24px;
  --space-lg: 40px;
  --space-xl: 64px;
  --space-xxl: 100px;

  /* Layout */
  --container-max: 1200px;
  --container-pad: 32px;

  /* Easing */
  --ease: cubic-bezier(.4, 0, .2, 1);
}

/* ============================================================
   Base
   ============================================================ */

body {
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 15px;
  line-height: 1.95;
  letter-spacing: 0.06em;
  color: var(--text-main);
  background: var(--bg-base);
  overflow-x: hidden;
}

html, body { overflow-x: hidden; }

.container {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--container-pad);
}

h1, h2, h3, h4 {
  font-family: var(--font-jp-serif);
  font-weight: 500;
  line-height: 1.5;
  letter-spacing: 0.04em;
  word-break: keep-all;
  overflow-wrap: normal;
}

h1 { font-size: 64px; }
h2 { font-size: 42px; }
h3 { font-size: 24px; }

a { color: inherit; transition: color .2s var(--ease); }
a:hover { color: var(--primary); }

/* ============================================================
   Mobile base
   ============================================================ */

@media (max-width: 880px) {
  :root {
    --container-pad: 20px;
    --space-xl: 48px;
    --space-xxl: 72px;
  }
  body { font-size: 14px; }
  h1 { font-size: 40px; }
  h2 { font-size: 28px; }
  h3 { font-size: 20px; }
}
```

- [ ] **Step 2: 構文チェック（PowerShellで）**

```powershell
Get-Content client/bolon-shareee/css/style.css | Measure-Object -Line
```
Expected: 約100行程度。

- [ ] **Step 3: Commit**

```bash
git add client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add design tokens and base styles"
```

---

### Task 3: ヘッダー / ナビ コンポーネント

**Files:**
- Modify: `client/bolon-shareee/css/style.css` (追記)

- [ ] **Step 1: ヘッダーCSSを追記**

`client/bolon-shareee/css/style.css` の末尾に追記：

```css
/* ============================================================
   Header
   ============================================================ */

.header {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid transparent;
  transition: all .3s var(--ease);
}

.header.is-scrolled {
  background: rgba(255, 255, 255, 0.97);
  border-bottom-color: var(--border);
}

.header .container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-en-serif);
  font-size: 22px;
  letter-spacing: 0.05em;
  font-weight: 500;
  color: var(--text-main);
}

.logo img { height: 30px; width: auto; }

.nav { display: flex; align-items: center; gap: 36px; }
.nav-links { display: flex; gap: 28px; }
.nav-links a {
  font-size: 13px;
  letter-spacing: 0.12em;
  font-family: var(--font-jp-sans);
  font-weight: 400;
}
.nav-links a:hover { color: var(--primary); }

.nav-cta {
  padding: 10px 22px;
  background: var(--primary);
  color: #fff !important;
  border-radius: 99px;
  font-size: 12px;
  letter-spacing: 0.14em;
  font-family: var(--font-jp-sans);
  font-weight: 500;
  transition: background .2s var(--ease);
}
.nav-cta:hover { background: var(--primary-deep); color: #fff !important; }

.menu-toggle { display: none; width: 32px; height: 28px; flex-direction: column; justify-content: space-between; padding: 5px 0; }
.menu-toggle span { display: block; height: 2px; background: var(--text-main); transition: transform .3s var(--ease), opacity .2s; }

@media (max-width: 880px) {
  .header { backdrop-filter: none; -webkit-backdrop-filter: none; background: var(--bg-base); }
  .header .container { height: 60px; }
  .logo { font-size: 18px; }
  .logo img { height: 24px; }
  .menu-toggle { display: flex; }
  .nav {
    position: fixed;
    top: 60px; left: 0; right: 0;
    background: var(--bg-base);
    flex-direction: column;
    align-items: stretch;
    gap: 0;
    padding: 32px 28px;
    transform: translateY(-110%);
    transition: transform .35s var(--ease);
    height: calc(100vh - 60px);
    height: calc(100svh - 60px);
    border-top: 1px solid var(--border);
  }
  .nav.is-open { transform: translateY(0); }
  .nav-links { flex-direction: column; gap: 20px; margin-bottom: 24px; }
  .nav-links a { font-size: 18px; padding: 8px 0; border-bottom: 1px solid var(--border); }
  .nav-cta { text-align: center; padding: 14px 22px; font-size: 14px; }
  .menu-toggle.is-open span:nth-child(1) { transform: translateY(10px) rotate(45deg); }
  .menu-toggle.is-open span:nth-child(2) { opacity: 0; }
  .menu-toggle.is-open span:nth-child(3) { transform: translateY(-10px) rotate(-45deg); }
}
```

- [ ] **Step 2: Commit**

```bash
git add client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add header and mobile nav"
```

---

### Task 4: index.html スケルトン + SEO + JSON-LD

**Files:**
- Create: `client/bolon-shareee/index.html`

- [ ] **Step 1: index.html を新規作成**

`client/bolon-shareee/index.html`：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO -->
  <title>B.villea｜福岡・警固のバストアップ専門サロン｜株式会社Bolon Shareee</title>
  <meta name="description" content="福岡市中央区警固のバストアップ専門サロン B.villea。2013年開業、14年で磨いた施術と代表・蒲池百都子の人柄でひとりずつに寄り添います。バストスクール・機器代理店も運営する株式会社Bolon Shareee。">
  <meta name="keywords" content="B.villea,ビーヴィレア,蒲池百都子,株式会社Bolon Shareee,福岡 バストアップサロン,警固 バストアップ,福岡市中央区 バストケア,バストスクール 福岡,バストアップ 起業">
  <link rel="canonical" href="https://sharkstars.jp/client/bolon-shareee/">

  <!-- OGP -->
  <meta property="og:title" content="B.villea｜福岡・警固のバストアップ専門サロン｜株式会社Bolon Shareee">
  <meta property="og:description" content="福岡・警固のバストアップ専門サロン。代表蒲池百都子の人柄で14年。">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sharkstars.jp/client/bolon-shareee/">
  <meta property="og:site_name" content="B.villea / 株式会社Bolon Shareee">
  <meta property="og:locale" content="ja_JP">
  <meta property="og:image" content="https://sharkstars.jp/client/bolon-shareee/images/ogp.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="B.villea｜福岡・警固のバストアップ専門サロン">
  <meta name="twitter:description" content="福岡・警固のバストアップ専門サロン。代表蒲池百都子の人柄で14年。">
  <meta name="twitter:image" content="https://sharkstars.jp/client/bolon-shareee/images/ogp.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Zen+Old+Mincho:wght@400;500;600&family=Zen+Kaku+Gothic+Antique:wght@300;400;500&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="css/reset.css">
  <link rel="stylesheet" href="css/style.css">

  <!-- Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        "@id": "https://sharkstars.jp/client/bolon-shareee/#org",
        "name": "株式会社Bolon Shareee",
        "alternateName": "Bolon Shareee",
        "url": "https://sharkstars.jp/client/bolon-shareee/",
        "logo": "https://sharkstars.jp/client/bolon-shareee/images/ogp.png",
        "description": "バストアップ専門サロンB.villea、バストスクール、バスト機器代理店を運営する福岡の女性向け美容関連企業。",
        "foundingDate": "2025-12-26",
        "founder": { "@type": "Person", "name": "蒲池 百都子" },
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "警固2-13-17 S-FORT警固タワー1801",
          "addressLocality": "福岡市中央区",
          "addressRegion": "福岡県",
          "postalCode": "810-0023",
          "addressCountry": "JP"
        },
        "telephone": "+81-90-9574-9566",
        "email": "motoko19750204@gmail.com"
      },
      {
        "@type": "HealthAndBeautyBusiness",
        "@id": "https://sharkstars.jp/client/bolon-shareee/#salon",
        "name": "B.villea（ビーヴィレア）",
        "description": "福岡・警固のバストアップ専門サロン。2013年開業、代表蒲池百都子。",
        "url": "https://sharkstars.jp/client/bolon-shareee/",
        "image": "https://sharkstars.jp/client/bolon-shareee/images/ogp.png",
        "address": { "@id": "https://sharkstars.jp/client/bolon-shareee/#org" },
        "telephone": "+81-90-9574-9566",
        "parentOrganization": { "@id": "https://sharkstars.jp/client/bolon-shareee/#org" }
      }
    ]
  }
  </script>
</head>
<body>

<!-- ===== HEADER ===== -->
<header class="header" id="header">
  <div class="container">
    <a href="index.html" class="logo">B.villea</a>
    <button class="menu-toggle" aria-label="メニューを開く" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav">
      <div class="nav-links">
        <a href="#story">代表ストーリー</a>
        <a href="#menu">メニュー</a>
        <a href="school.html">スクール</a>
        <a href="company.html">会社情報</a>
        <a href="faq.html">FAQ</a>
      </div>
      <a href="contact.html" class="nav-cta">CONTACT</a>
    </nav>
  </div>
</header>

<!-- セクションはTask 5以降で追加 -->

<script src="js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: ブラウザで開いて確認**

ブラウザで `client/bolon-shareee/index.html` を開く。ヘッダーが表示され、スクロールで `is-scrolled` クラスが付く。SP表示でハンバーガーが出る。

- [ ] **Step 3: JSON-LD バリデーション**

JSON-LD部分を https://validator.schema.org/ にペーストして、エラーがないことを確認。

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html
git commit -m "feat(bolon-shareee): add index.html skeleton with SEO + JSON-LD"
```

---

### Task 5: Hero セクション

**Files:**
- Modify: `client/bolon-shareee/index.html` (body内追加)
- Modify: `client/bolon-shareee/css/style.css` (.hero スタイル追加)

- [ ] **Step 1: Hero HTML を追加**

`index.html` の `<!-- セクションはTask 5以降で追加 -->` を以下に置換：

```html
<!-- ===== HERO ===== -->
<section class="hero">
  <div class="hero-bg" aria-hidden="true">
    <div class="hero-image" style="background-image: url('https://images.unsplash.com/photo-1597762470488-3877b1f538c6?w=1800&q=85');"></div>
    <div class="hero-overlay"></div>
  </div>

  <div class="hero-vertical" aria-hidden="true">B.villea — Bougainvillea Blooms</div>

  <div class="hero-inner">
    <p class="hero-eyebrow">Bougainvillea Blooms</p>
    <h1 class="hero-title">
      <span class="word"><span>咲き誇る</span></span>
      <span class="word"><span>あなたを、</span></span>
      <span class="word"><span><span class="accent">ここから</span>。</span></span>
    </h1>
    <p class="hero-lead">
      福岡・警固のバストアップ専門サロン。<br>
      代表・蒲池百都子の人柄と、14年の積み重ねを<br class="sp-hide">、<br class="pc-hide">ひとりずつに。
    </p>
    <a href="#line" class="hero-cta">LINEで気軽に相談する →</a>
  </div>
</section>
```

- [ ] **Step 2: Hero CSS を追加**

`style.css` 末尾に追加：

```css
/* ============================================================
   Hero
   ============================================================ */

.hero {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  align-items: center;
  overflow: hidden;
  padding: 120px 0 80px;
}

.hero-bg { position: absolute; inset: 0; z-index: 0; }
.hero-image {
  position: absolute; inset: 0;
  background-size: cover;
  background-position: center;
  filter: brightness(0.75) saturate(1.1);
}
.hero-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, rgba(251,246,239,0.85) 70%, rgba(255,255,255,0.95) 100%);
}

.hero-vertical {
  position: absolute;
  right: 32px; top: 100px;
  writing-mode: vertical-rl;
  font-family: var(--font-en-serif);
  font-size: 12px;
  letter-spacing: 0.35em;
  color: var(--gold);
  z-index: 2;
  opacity: 0.85;
}

.hero-inner {
  position: relative;
  z-index: 3;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--container-pad);
  width: 100%;
}

.hero-eyebrow {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 16px;
  letter-spacing: 0.2em;
  color: var(--primary);
  margin-bottom: 28px;
}

.hero-title {
  font-size: 76px;
  line-height: 1.45;
  letter-spacing: 0.04em;
  margin-bottom: 32px;
  color: var(--text-main);
  word-break: keep-all;
  overflow-wrap: normal;
}
.hero-title .word { display: inline-block; }
.hero-title .word > span { white-space: nowrap; }
.hero-title .accent { color: var(--primary); }

.hero-lead {
  font-family: var(--font-jp-sans);
  font-weight: 400;
  font-size: 16px;
  line-height: 2.1;
  color: var(--text-sub);
  margin-bottom: 44px;
  max-width: 620px;
}

.hero-cta {
  display: inline-block;
  padding: 18px 38px;
  background: var(--primary);
  color: #fff !important;
  border-radius: 99px;
  font-family: var(--font-jp-sans);
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 0.14em;
  transition: background .2s var(--ease), transform .2s var(--ease);
}
.hero-cta:hover { background: var(--primary-deep); transform: translateY(-2px); }

.sp-hide { display: inline; }
.pc-hide { display: none; }

@media (max-width: 880px) {
  .hero { padding: 100px 0 64px; }
  .hero-vertical { right: 18px; top: 84px; font-size: 10px; }
  .hero-eyebrow { font-size: 13px; margin-bottom: 18px; }
  .hero-title { font-size: 44px; line-height: 1.5; margin-bottom: 24px; }
  .hero-lead { font-size: 14px; line-height: 2.0; margin-bottom: 32px; }
  .hero-cta { padding: 16px 28px; font-size: 13px; }
  .sp-hide { display: none; }
  .pc-hide { display: inline; }
}
```

- [ ] **Step 3: ブラウザでPC/SP両方確認**

- ブラウザで `index.html` を開き、Heroが100vh分表示される
- DevToolsモバイル（iPhone 14）で開き、見出しが1文字ずつ縦に折り返ししないこと
- 縦書きBrandマークがゴールド色で右側に表示

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add hero section"
```

---

### Task 6: Intro / Editorial Eyebrow セクション

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加（Hero直下）**

```html
<!-- ===== INTRO ===== -->
<section class="intro">
  <div class="container">
    <p class="section-eyebrow">— Bougainvillea Blooms</p>
    <h2 class="intro-headline">
      14年、ひとつひとつのお胸に。<br>
      <span class="accent">咲かせてきたものがあります。</span>
    </h2>
    <div class="intro-meta">
      <div><span class="label">開業</span><span class="value">2013年（個人事業）</span></div>
      <div><span class="label">法人化</span><span class="value">2025年12月26日</span></div>
      <div><span class="label">所在地</span><span class="value">福岡市中央区警固</span></div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Section common — eyebrow / spacing
   ============================================================ */

.section-eyebrow {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 14px;
  letter-spacing: 0.22em;
  color: var(--primary);
  margin-bottom: 24px;
}

.intro { padding: var(--space-xxl) 0; background: var(--bg-warm); }
.intro-headline {
  font-size: 44px;
  line-height: 1.7;
  margin-bottom: 56px;
  letter-spacing: 0.05em;
  max-width: 880px;
}
.intro-headline .accent { color: var(--primary); }
.intro-meta {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  border-top: 1px solid var(--border);
  padding-top: 32px;
}
.intro-meta > div {
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.intro-meta .label {
  font-family: var(--font-en-serif);
  font-size: 11px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold);
}
.intro-meta .value {
  font-family: var(--font-jp-serif);
  font-size: 16px;
  letter-spacing: 0.06em;
}

@media (max-width: 880px) {
  .intro { padding: var(--space-xxl) 0 var(--space-xl); }
  .intro-headline { font-size: 26px; margin-bottom: 36px; line-height: 1.75; }
  .intro-meta { grid-template-columns: 1fr; gap: 18px; padding-top: 22px; }
  .intro-meta .value { font-size: 15px; }
}
```

- [ ] **Step 3: ブラウザ確認** — Hero下にクリーム背景のIntroが現れる。3カラムのmetaはSPで1カラムに。

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add intro / editorial eyebrow section"
```

---

### Task 7: 強み 3つ セクション（アシメトリック 1+2）

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== STRENGTHS ===== -->
<section class="strengths">
  <div class="container">
    <p class="section-eyebrow">— Our Strength</p>
    <h2 class="section-title">B.villea が選ばれる、<br>3つの理由。</h2>

    <div class="strengths-grid">
      <article class="strength-card strength-large">
        <div class="strength-num">01</div>
        <h3 class="strength-title">Motokoの人柄</h3>
        <p class="strength-body">
          「Motokoさんに会いに行きたい」<br>
          常連のお客様から、いちばん多くいただく声です。<br>
          技術だけではない、その場の温度。<br>
          14年積み重ねた信頼関係を、<br>
          おひとりずつとつくっていきます。
        </p>
      </article>
      <article class="strength-card">
        <div class="strength-num">02</div>
        <h3 class="strength-title">14年で磨いた施術</h3>
        <p class="strength-body">2013年の開業から、ひたすらバストアップひと筋。経験から生まれた手技を、丁寧にお届けします。</p>
      </article>
      <article class="strength-card">
        <div class="strength-num">03</div>
        <h3 class="strength-title">警固の隠れ家</h3>
        <p class="strength-body">福岡市中央区警固、S-FORTタワー1801。完全予約制、ひと組ずつのプライベートな時間。</p>
      </article>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Strengths — asymmetric 1+2
   ============================================================ */

.strengths { padding: var(--space-xxl) 0; }
.section-title {
  font-size: 42px;
  line-height: 1.55;
  margin-bottom: 64px;
  letter-spacing: 0.05em;
}

.strengths-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  grid-template-rows: auto auto;
  gap: 32px;
}
.strength-large { grid-row: 1 / span 2; }
.strength-card {
  padding: 48px 36px;
  background: var(--bg-warm);
  border-radius: 4px;
  position: relative;
}
.strength-large {
  background: var(--text-main);
  color: var(--bg-warm);
}
.strength-large .strength-body { color: rgba(251,246,239,0.85); }
.strength-num {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 56px;
  font-weight: 400;
  color: var(--primary);
  line-height: 1;
  margin-bottom: 24px;
  opacity: 0.85;
}
.strength-large .strength-num { color: var(--gold); }
.strength-title {
  font-size: 24px;
  margin-bottom: 18px;
  letter-spacing: 0.06em;
}
.strength-body {
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 14px;
  line-height: 2.0;
  color: var(--text-sub);
}

@media (max-width: 880px) {
  .strengths { padding: var(--space-xxl) 0 var(--space-xl); }
  .section-title { font-size: 28px; margin-bottom: 40px; }
  .strengths-grid { grid-template-columns: 1fr; grid-template-rows: auto; gap: 16px; }
  .strength-large { grid-row: auto; }
  .strength-card { padding: 36px 28px; }
  .strength-num { font-size: 44px; margin-bottom: 16px; }
  .strength-title { font-size: 20px; }
}
```

- [ ] **Step 3: 確認** — PCで1カード（左大）+ 2カード（右上下）のアシメトリック表示、SPで縦1カラム

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add strengths section (asymmetric 1+2)"
```

---

### Task 8: 代表ストーリー（about統合）セクション

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== FOUNDER STORY ===== -->
<section class="story" id="story">
  <div class="container">
    <div class="story-grid">
      <div class="story-image">
        <img src="https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=900&q=85" alt="代表 蒲池百都子" loading="lazy">
        <p class="story-image-caption">代表・蒲池百都子（がま ちもとこ）</p>
      </div>
      <div class="story-text">
        <p class="section-eyebrow">— Founder's Story</p>
        <h2 class="story-headline">
          バストの悩みに、<br>
          <span class="accent">ひとりずつ寄り添う。</span>
        </h2>
        <div class="story-body">
          <p>2013年2月、福岡で個人事業として B.villea を開業しました。</p>
          <p>「もっとお胸に自信を持ちたい」「人に言えない悩みを抱えている」<br>そんなお客様おひとりずつに、技術と時間で向き合う14年。</p>
          <p>2025年12月、株式会社 Bolon Shareee として法人化。<br>サロンに加え、バストスクール、バスト機器の代理店も運営する形になりました。</p>
          <p>規模が変わっても、変えたくないことが一つあります。<br><span class="story-emphasis">来てくださった方の温度に、ちゃんと触れること。</span></p>
        </div>
        <a href="company.html" class="story-link">会社情報を詳しく見る →</a>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Founder Story
   ============================================================ */

.story { padding: var(--space-xxl) 0; background: var(--bg-warm); }
.story-grid {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 80px;
  align-items: center;
}
.story-image { position: relative; }
.story-image img {
  width: 100%;
  height: auto;
  aspect-ratio: 4 / 5;
  object-fit: cover;
  border-radius: 4px;
}
.story-image-caption {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 12px;
  letter-spacing: 0.18em;
  color: var(--text-sub);
  margin-top: 16px;
  text-align: right;
}
.story-headline {
  font-size: 40px;
  line-height: 1.6;
  margin-bottom: 36px;
  letter-spacing: 0.05em;
}
.story-headline .accent { color: var(--primary); }
.story-body { font-family: var(--font-jp-sans); }
.story-body p {
  font-size: 15px;
  line-height: 2.1;
  color: var(--text-sub);
  margin-bottom: 22px;
}
.story-emphasis {
  color: var(--text-main);
  font-weight: 500;
  border-bottom: 1px solid var(--gold);
  padding-bottom: 2px;
}
.story-link {
  display: inline-block;
  margin-top: 16px;
  font-family: var(--font-jp-sans);
  font-size: 13px;
  letter-spacing: 0.12em;
  color: var(--text-main);
  border-bottom: 1px solid var(--text-main);
  padding-bottom: 4px;
  transition: color .2s, border-color .2s;
}
.story-link:hover { color: var(--primary); border-color: var(--primary); }

@media (max-width: 880px) {
  .story { padding: var(--space-xxl) 0 var(--space-xl); }
  .story-grid { grid-template-columns: 1fr; gap: 40px; }
  .story-headline { font-size: 28px; margin-bottom: 24px; line-height: 1.7; }
  .story-body p { font-size: 14px; line-height: 2.0; margin-bottom: 18px; }
}
```

- [ ] **Step 3: 確認** — PCで写真左、テキスト右の2カラム。SPで縦並び（写真→テキスト）

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add founder story section"
```

---

## Phase 2: index.html 下半分（Day 2）

### Task 9: メニュー & 料金（service統合）

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== MENU ===== -->
<section class="menu" id="menu">
  <div class="container">
    <p class="section-eyebrow">— Menu & Care</p>
    <h2 class="section-title">バストアップ専門の、<br>メニュー。</h2>

    <div class="menu-list">
      <article class="menu-item">
        <div class="menu-meta">
          <span class="menu-num">M01</span>
          <span class="menu-duration">90分</span>
        </div>
        <h3 class="menu-name">B.villea バストケア / 初回体験</h3>
        <p class="menu-desc">14年の手技でじっくりお胸を整える、定番のフルケア。施術前のカウンセリングからアフターまで丁寧に。</p>
        <div class="menu-price">
          <span class="price-label">初回</span>
          <span class="price-value">¥◯,◯◯◯</span>
          <span class="price-note">（税込 / 仮）</span>
        </div>
      </article>

      <article class="menu-item">
        <div class="menu-meta">
          <span class="menu-num">M02</span>
          <span class="menu-duration">60分</span>
        </div>
        <h3 class="menu-name">継続コース</h3>
        <p class="menu-desc">2回目以降の方向け、リズムを保つための定期ケア。お一人ずつの状態に合わせた施術内容。</p>
        <div class="menu-price">
          <span class="price-label">2回目以降</span>
          <span class="price-value">¥◯,◯◯◯</span>
          <span class="price-note">（税込 / 仮）</span>
        </div>
      </article>

      <article class="menu-item">
        <div class="menu-meta">
          <span class="menu-num">M03</span>
          <span class="menu-duration">120分</span>
        </div>
        <h3 class="menu-name">プレミアム / 集中ケア</h3>
        <p class="menu-desc">じっくり時間をかけて、お胸と全身を整える贅沢なコース。特別なタイミングに。</p>
        <div class="menu-price">
          <span class="price-label">プレミアム</span>
          <span class="price-value">¥◯,◯◯◯</span>
          <span class="price-note">（税込 / 仮）</span>
        </div>
      </article>
    </div>

    <!-- 施術の流れ -->
    <div class="menu-flow">
      <h3 class="flow-title">— 施術の流れ</h3>
      <ol class="flow-steps">
        <li><span class="flow-num">01</span><span class="flow-text"><strong>カウンセリング</strong>お悩み・ご希望をうかがいます。</span></li>
        <li><span class="flow-num">02</span><span class="flow-text"><strong>お着替え</strong>専用のお部屋でゆっくり。</span></li>
        <li><span class="flow-num">03</span><span class="flow-text"><strong>施術</strong>お胸まわりを丁寧に整えます。</span></li>
        <li><span class="flow-num">04</span><span class="flow-text"><strong>アフター</strong>お茶をご用意。次回のご相談も。</span></li>
      </ol>
    </div>

    <p class="menu-note">※料金は仮表示です。実際の料金はLINEまたはお問い合わせよりご確認ください。</p>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Menu & Care
   ============================================================ */

.menu { padding: var(--space-xxl) 0; }
.menu-list {
  display: flex;
  flex-direction: column;
  gap: 0;
  margin-bottom: 80px;
  border-top: 1px solid var(--border);
}
.menu-item {
  padding: 40px 0;
  border-bottom: 1px solid var(--border);
  display: grid;
  grid-template-columns: 1fr 2.5fr 1fr;
  gap: 40px;
  align-items: start;
}
.menu-meta { display: flex; flex-direction: column; gap: 8px; }
.menu-num {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 36px;
  color: var(--primary);
  letter-spacing: 0.05em;
  line-height: 1;
}
.menu-duration {
  font-family: var(--font-jp-sans);
  font-size: 12px;
  letter-spacing: 0.18em;
  color: var(--text-sub);
  border: 1px solid var(--border);
  padding: 4px 12px;
  border-radius: 99px;
  align-self: flex-start;
}
.menu-name {
  font-size: 22px;
  margin-bottom: 12px;
  letter-spacing: 0.06em;
}
.menu-desc {
  font-family: var(--font-jp-sans);
  font-size: 14px;
  line-height: 1.95;
  color: var(--text-sub);
}
.menu-price { text-align: right; font-family: var(--font-jp-sans); }
.price-label {
  display: block;
  font-size: 11px;
  letter-spacing: 0.18em;
  color: var(--gold);
  margin-bottom: 6px;
}
.price-value {
  display: block;
  font-family: var(--font-en-serif);
  font-size: 28px;
  color: var(--text-main);
  letter-spacing: 0.04em;
}
.price-note {
  display: block;
  font-size: 11px;
  color: var(--text-sub);
  margin-top: 4px;
}

.menu-flow {
  background: var(--bg-warm);
  padding: 56px 48px;
  border-radius: 4px;
}
.flow-title {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 22px;
  color: var(--primary);
  margin-bottom: 32px;
}
.flow-steps {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}
.flow-steps li { display: flex; flex-direction: column; gap: 12px; }
.flow-num {
  font-family: var(--font-en-serif);
  font-size: 22px;
  font-style: italic;
  color: var(--gold);
  border-bottom: 1px solid var(--gold);
  padding-bottom: 8px;
  width: fit-content;
  letter-spacing: 0.05em;
}
.flow-text { font-family: var(--font-jp-sans); font-size: 13px; line-height: 1.9; color: var(--text-sub); }
.flow-text strong { display: block; color: var(--text-main); margin-bottom: 4px; font-weight: 500; font-size: 14px; }

.menu-note {
  font-size: 12px;
  color: var(--text-sub);
  margin-top: 28px;
  text-align: center;
  font-family: var(--font-jp-sans);
}

@media (max-width: 880px) {
  .menu { padding: var(--space-xxl) 0 var(--space-xl); }
  .menu-item {
    grid-template-columns: 1fr;
    gap: 16px;
    padding: 32px 0;
  }
  .menu-meta { flex-direction: row; align-items: center; gap: 14px; }
  .menu-num { font-size: 28px; }
  .menu-name { font-size: 19px; }
  .menu-price { text-align: left; padding-top: 4px; }
  .price-value { font-size: 22px; }

  .menu-flow { padding: 36px 24px; }
  .flow-title { font-size: 18px; margin-bottom: 24px; }
  .flow-steps { grid-template-columns: 1fr 1fr; gap: 20px; }
}
```

- [ ] **Step 3: 確認** — PCで3カラム、SPで縦並び。施術の流れがPC4カラム、SP2カラム

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add menu and treatment flow section"
```

---

### Task 10: Voice（お客様の声）セクション

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== VOICE ===== -->
<section class="voice">
  <div class="container">
    <p class="section-eyebrow">— Voice</p>
    <h2 class="section-title">お客様の、<br>声から。</h2>

    <div class="voice-list">
      <article class="voice-item">
        <p class="voice-quote">「Motokoさんに会うと元気になる」</p>
        <p class="voice-body">3年通っています。技術はもちろんですが、いちばんは話を聴いてくれること。終わったあとはお胸も心も軽くなって帰ります。</p>
        <p class="voice-author">— S様 / 40代 / 福岡市</p>
      </article>

      <article class="voice-item">
        <p class="voice-quote">「自分のお胸が、好きになった」</p>
        <p class="voice-body">ずっとコンプレックスでした。1年通って、いまは鏡の前で自分を見るのが嫌じゃなくなりました。それがいちばんの変化です。</p>
        <p class="voice-author">— K様 / 30代 / 福岡市</p>
      </article>

      <article class="voice-item">
        <p class="voice-quote">「サロンに行く時間そのものが好き」</p>
        <p class="voice-body">完全予約制で、人と会わずに通えるのがありがたい。自分のためだけの90分です。</p>
        <p class="voice-author">— M様 / 50代 / 北九州市</p>
      </article>
    </div>

    <p class="voice-disclaimer">※個人の感想であり、効果には個人差があります。</p>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Voice
   ============================================================ */

.voice { padding: var(--space-xxl) 0; background: var(--text-main); color: var(--bg-warm); }
.voice .section-eyebrow { color: var(--gold); }
.voice .section-title { color: var(--bg-base); }

.voice-list {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 28px;
  margin-top: 48px;
}
.voice-item {
  padding: 36px 28px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 4px;
}
.voice-quote {
  font-family: var(--font-jp-serif);
  font-size: 18px;
  line-height: 1.7;
  color: var(--bg-base);
  margin-bottom: 18px;
  letter-spacing: 0.05em;
  position: relative;
  padding-left: 16px;
}
.voice-quote::before {
  content: '"';
  position: absolute;
  left: -4px; top: -8px;
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 36px;
  color: var(--primary);
  line-height: 1;
}
.voice-body {
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 13px;
  line-height: 2.0;
  color: rgba(251,246,239,0.75);
  margin-bottom: 18px;
}
.voice-author {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 12px;
  letter-spacing: 0.1em;
  color: var(--gold);
}

.voice-disclaimer {
  margin-top: 32px;
  text-align: center;
  font-size: 11px;
  letter-spacing: 0.08em;
  color: rgba(251,246,239,0.5);
  font-family: var(--font-jp-sans);
}

@media (max-width: 880px) {
  .voice { padding: var(--space-xxl) 0 var(--space-xl); }
  .voice-list { grid-template-columns: 1fr; gap: 18px; margin-top: 32px; }
  .voice-item { padding: 28px 22px; }
  .voice-quote { font-size: 16px; }
}
```

- [ ] **Step 3: 確認** — 黒背景に3カードのVoice、disclaimer注記表示

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add voice section with disclaimer"
```

---

### Task 11: FAQ抜粋セクション

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== FAQ EXCERPT ===== -->
<section class="faq-excerpt">
  <div class="container">
    <div class="faq-grid">
      <div class="faq-head">
        <p class="section-eyebrow">— Questions</p>
        <h2 class="section-title">よくいただく、<br>ご質問。</h2>
        <a href="faq.html" class="faq-link">FAQをすべて見る →</a>
      </div>

      <div class="faq-items">
        <details class="faq-item">
          <summary class="faq-q">お胸の変化は、本当にありますか？</summary>
          <div class="faq-a">個人差はありますが、続けていただくことで多くのお客様に変化を感じていただいています。詳しくはカウンセリング時にご相談ください。<br><small>※個人の感想であり、効果には個人差があります。</small></div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">初めてでも大丈夫ですか？</summary>
          <div class="faq-a">もちろんです。初めての方には、カウンセリングからお流れをご説明し、安心して受けていただけるようにしています。</div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">男性スタッフはいますか？</summary>
          <div class="faq-a">スタッフはすべて女性です（代表 蒲池 + 業務委託の女性スタッフ）。安心してお越しください。</div>
        </details>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   FAQ Excerpt
   ============================================================ */

.faq-excerpt { padding: var(--space-xxl) 0; background: var(--bg-warm); }
.faq-grid {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 80px;
  align-items: start;
}
.faq-head { position: sticky; top: 100px; }
.faq-link {
  display: inline-block;
  margin-top: 16px;
  font-family: var(--font-jp-sans);
  font-size: 13px;
  letter-spacing: 0.12em;
  color: var(--text-main);
  border-bottom: 1px solid var(--text-main);
  padding-bottom: 4px;
}
.faq-link:hover { color: var(--primary); border-color: var(--primary); }

.faq-items { display: flex; flex-direction: column; gap: 0; }
.faq-item {
  border-top: 1px solid var(--border);
  padding: 24px 0;
}
.faq-item:last-child { border-bottom: 1px solid var(--border); }
.faq-q {
  font-family: var(--font-jp-serif);
  font-size: 17px;
  line-height: 1.7;
  cursor: pointer;
  list-style: none;
  position: relative;
  padding-right: 40px;
  letter-spacing: 0.05em;
}
.faq-q::-webkit-details-marker { display: none; }
.faq-q::after {
  content: '+';
  position: absolute;
  right: 8px; top: 0;
  font-family: var(--font-en-serif);
  font-size: 26px;
  color: var(--primary);
  transition: transform .25s var(--ease);
}
.faq-item[open] .faq-q::after { content: '−'; }
.faq-a {
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 14px;
  line-height: 2.0;
  color: var(--text-sub);
  padding: 16px 0 8px;
  letter-spacing: 0.06em;
}
.faq-a small { display: block; margin-top: 12px; color: var(--gold); font-size: 11px; letter-spacing: 0.1em; }

@media (max-width: 880px) {
  .faq-excerpt { padding: var(--space-xxl) 0 var(--space-xl); }
  .faq-grid { grid-template-columns: 1fr; gap: 36px; }
  .faq-head { position: static; }
  .faq-q { font-size: 15px; padding-right: 32px; }
}
```

- [ ] **Step 3: 確認** — クリックでアコーディオン開閉、PC 2カラム / SP 縦並び

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add FAQ excerpt section"
```

---

### Task 12: アクセス & 店舗情報セクション

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== STUDIO / ACCESS ===== -->
<section class="studio">
  <div class="container">
    <p class="section-eyebrow">— Studio</p>
    <h2 class="section-title">お越しいただく、<br>場所のこと。</h2>

    <div class="studio-grid">
      <div class="studio-map">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3322.0!2d130.392!3d33.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zSi1GT1JU5pyo5LiB44K_44Ov44O8!5e0!3m2!1sja!2sjp!4v1700000000000"
          width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy"
          referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <dl class="studio-info">
        <div><dt>所在地</dt><dd>〒810-0023<br>福岡市中央区警固2-13-17<br>S-FORT警固タワー 1801</dd></div>
        <div><dt>最寄駅</dt><dd>福岡市営地下鉄 赤坂駅 徒歩◯分<br>西鉄バス 警固町停 徒歩◯分</dd></div>
        <div><dt>営業時間</dt><dd>10:00 – 19:00（最終受付 17:30 / 仮）</dd></div>
        <div><dt>定休日</dt><dd>不定休（LINEにてご確認ください）</dd></div>
        <div><dt>予約方法</dt><dd>完全予約制 / LINE優先</dd></div>
      </dl>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Studio / Access
   ============================================================ */

.studio { padding: var(--space-xxl) 0; }
.studio-grid {
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  gap: 48px;
  margin-top: 48px;
  align-items: stretch;
}
.studio-map {
  border-radius: 4px;
  overflow: hidden;
  min-height: 420px;
  background: var(--bg-warm);
}
.studio-map iframe { min-height: 420px; display: block; }
.studio-info {
  display: flex;
  flex-direction: column;
  font-family: var(--font-jp-sans);
}
.studio-info > div {
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 20px;
  padding: 20px 0;
  border-bottom: 1px solid var(--border);
  align-items: start;
}
.studio-info > div:first-child { padding-top: 0; }
.studio-info > div:last-child { border-bottom: 0; }
.studio-info dt {
  font-family: var(--font-en-serif);
  font-size: 11px;
  letter-spacing: 0.18em;
  color: var(--gold);
  text-transform: uppercase;
  padding-top: 4px;
}
.studio-info dd {
  font-size: 14px;
  line-height: 1.9;
  color: var(--text-main);
  letter-spacing: 0.05em;
}

@media (max-width: 880px) {
  .studio { padding: var(--space-xxl) 0 var(--space-xl); }
  .studio-grid { grid-template-columns: 1fr; gap: 28px; margin-top: 32px; }
  .studio-map, .studio-map iframe { min-height: 300px; }
  .studio-info > div { grid-template-columns: 90px 1fr; gap: 14px; padding: 16px 0; }
  .studio-info dt { font-size: 10px; }
  .studio-info dd { font-size: 13px; }
}
```

- [ ] **Step 3: 確認** — 地図がiframeで表示、店舗情報リスト

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add studio access section"
```

---

### Task 13: 会社情報サマリ（3事業）セクション

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加**

```html
<!-- ===== COMPANY SUMMARY ===== -->
<section class="company-summary">
  <div class="container">
    <p class="section-eyebrow">— Bolon Shareee</p>
    <h2 class="section-title">3つの事業で、<br>女性を支える。</h2>

    <div class="business-list">
      <article class="business-item">
        <div class="business-num">事業 01</div>
        <h3 class="business-title">B.villea サロン</h3>
        <p class="business-desc">福岡・警固のバストアップ専門サロン。本サイトでご紹介している事業の中心です。</p>
        <a href="#menu" class="business-link">メニューを見る →</a>
      </article>

      <article class="business-item">
        <div class="business-num">事業 02</div>
        <h3 class="business-title">バストスクール</h3>
        <p class="business-desc">14年で培った技術と経営の知見を、サロン開業を目指す方へ。卒業生は当社の業務委託パートナーとしてもご活躍いただけます。</p>
        <a href="school.html" class="business-link">スクール詳細 →</a>
      </article>

      <article class="business-item">
        <div class="business-num">事業 03</div>
        <h3 class="business-title">バスト機器 代理店・販売</h3>
        <p class="business-desc">サロンで使用している専門機器を、信頼できるサロン様へ。お取り扱いについてはお問い合わせください。</p>
        <a href="company.html" class="business-link">会社情報 →</a>
      </article>
    </div>
  </div>
</section>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   Company Summary
   ============================================================ */

.company-summary { padding: var(--space-xxl) 0; background: var(--bg-warm); }
.business-list {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 48px;
}
.business-item {
  padding: 40px 32px;
  background: var(--bg-base);
  border-radius: 4px;
  border: 1px solid var(--border);
  display: flex;
  flex-direction: column;
}
.business-num {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 13px;
  letter-spacing: 0.18em;
  color: var(--gold);
  margin-bottom: 20px;
}
.business-title {
  font-size: 22px;
  margin-bottom: 14px;
  letter-spacing: 0.05em;
}
.business-desc {
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 13px;
  line-height: 2.0;
  color: var(--text-sub);
  margin-bottom: 28px;
  flex-grow: 1;
}
.business-link {
  font-family: var(--font-jp-sans);
  font-size: 12px;
  letter-spacing: 0.14em;
  color: var(--text-main);
  border-bottom: 1px solid var(--text-main);
  padding-bottom: 4px;
  width: fit-content;
}
.business-link:hover { color: var(--primary); border-color: var(--primary); }

@media (max-width: 880px) {
  .company-summary { padding: var(--space-xxl) 0 var(--space-xl); }
  .business-list { grid-template-columns: 1fr; gap: 14px; margin-top: 32px; }
  .business-item { padding: 32px 24px; }
  .business-title { font-size: 19px; }
}
```

- [ ] **Step 3: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add company summary section (3 businesses)"
```

---

### Task 14: LINE誘導フッターブロック + フッター本体

**Files:**
- Modify: `client/bolon-shareee/index.html`
- Modify: `client/bolon-shareee/css/style.css`

- [ ] **Step 1: HTML追加（index.htmlのbody末尾、`<script>`の前）**

```html
<!-- ===== LINE CTA ===== -->
<section class="line-cta" id="line">
  <div class="container">
    <p class="section-eyebrow" style="color: var(--gold);">— Get in Touch</p>
    <h2 class="line-headline">
      まずはLINEで、<br>
      <span class="accent">気軽にご相談ください。</span>
    </h2>
    <p class="line-lead">
      お悩み、お見積もり、初めての方のご不安。<br>
      おひとりずつ、Motokoが直接お返事しています。
    </p>
    <div class="line-actions">
      <a href="https://lin.ee/" class="line-btn line-btn-primary" target="_blank" rel="noopener">
        <span class="line-icon" aria-hidden="true">L</span>
        LINEで相談する
      </a>
      <a href="contact.html" class="line-btn line-btn-secondary">フォームから問い合わせる</a>
    </div>
    <p class="line-note">電話でも承ります： <a href="tel:+819095749566">090-9574-9566</a></p>
  </div>
</section>

<!-- ===== FOOTER ===== -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <p class="footer-logo">B.villea</p>
        <p class="footer-corp">株式会社Bolon Shareee</p>
        <p class="footer-addr">〒810-0023<br>福岡市中央区警固2-13-17<br>S-FORT警固タワー 1801</p>
      </div>
      <nav class="footer-nav">
        <h4>Site</h4>
        <a href="index.html">トップ</a>
        <a href="school.html">スクール</a>
        <a href="company.html">会社情報</a>
        <a href="faq.html">FAQ</a>
        <a href="contact.html">お問い合わせ</a>
        <a href="privacy.html">プライバシーポリシー</a>
      </nav>
      <div class="footer-meta">
        <h4>Contact</h4>
        <p>TEL <a href="tel:+819095749566">090-9574-9566</a></p>
        <p>Mail <a href="mailto:motoko19750204@gmail.com">motoko19750204@gmail.com</a></p>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="copyright">© 2026 株式会社Bolon Shareee. All Rights Reserved.</p>
      <p class="produced-by">Produced by <a href="https://sharkstars.jp/" target="_blank" rel="noopener">SHARKSTARS</a></p>
    </div>
  </div>
</footer>
```

- [ ] **Step 2: CSS追加**

```css
/* ============================================================
   LINE CTA
   ============================================================ */

.line-cta {
  padding: var(--space-xxl) 0;
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-deep) 100%);
  color: #fff;
  text-align: center;
}
.line-cta .section-eyebrow { color: var(--gold); }
.line-headline {
  font-size: 42px;
  line-height: 1.6;
  margin-bottom: 24px;
  color: #fff;
  letter-spacing: 0.04em;
}
.line-headline .accent { color: #fff; opacity: 0.85; }
.line-lead {
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 15px;
  line-height: 2.1;
  margin-bottom: 40px;
  color: rgba(255,255,255,0.9);
}
.line-actions { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.line-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 18px 36px;
  border-radius: 99px;
  font-family: var(--font-jp-sans);
  font-weight: 500;
  font-size: 14px;
  letter-spacing: 0.14em;
  transition: transform .2s var(--ease);
}
.line-btn:hover { transform: translateY(-2px); }
.line-btn-primary {
  background: #06C755;
  color: #fff !important;
}
.line-btn-secondary {
  background: rgba(255,255,255,0.12);
  color: #fff !important;
  border: 1px solid rgba(255,255,255,0.3);
}
.line-icon {
  display: inline-grid;
  place-items: center;
  width: 22px; height: 22px;
  background: #fff;
  color: #06C755;
  border-radius: 4px;
  font-weight: 700;
  font-size: 14px;
}
.line-note {
  margin-top: 32px;
  font-size: 13px;
  color: rgba(255,255,255,0.85);
  font-family: var(--font-jp-sans);
}
.line-note a { color: #fff; border-bottom: 1px solid rgba(255,255,255,0.5); }

/* ============================================================
   Footer
   ============================================================ */

.footer {
  background: var(--text-main);
  color: var(--bg-warm);
  padding: 72px 0 24px;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr;
  gap: 48px;
  padding-bottom: 48px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
.footer-logo {
  font-family: var(--font-en-serif);
  font-size: 28px;
  letter-spacing: 0.05em;
  margin-bottom: 12px;
}
.footer-corp {
  font-family: var(--font-jp-serif);
  font-size: 14px;
  margin-bottom: 16px;
  color: #fff;
  letter-spacing: 0.06em;
}
.footer-addr {
  font-family: var(--font-jp-sans);
  font-size: 12px;
  line-height: 1.9;
  color: rgba(251,246,239,0.7);
}
.footer-nav h4, .footer-meta h4 {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 12px;
  letter-spacing: 0.22em;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 20px;
}
.footer-nav a, .footer-meta a, .footer-meta p {
  display: block;
  font-family: var(--font-jp-sans);
  font-size: 13px;
  line-height: 1;
  padding: 8px 0;
  color: rgba(251,246,239,0.85);
  letter-spacing: 0.06em;
}
.footer-nav a:hover, .footer-meta a:hover { color: var(--gold); }
.footer-meta p { padding: 8px 0 4px; }

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 28px;
  flex-wrap: wrap;
  gap: 8px;
}
.copyright, .produced-by {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 11px;
  letter-spacing: 0.12em;
  color: rgba(251,246,239,0.5);
}
.produced-by a { color: rgba(251,246,239,0.7); border-bottom: 1px solid rgba(251,246,239,0.2); }

@media (max-width: 880px) {
  .line-cta { padding: var(--space-xxl) 0 var(--space-xl); }
  .line-headline { font-size: 26px; }
  .line-lead { font-size: 14px; margin-bottom: 28px; }
  .line-btn { padding: 16px 24px; font-size: 13px; width: 100%; justify-content: center; }
  .line-actions { flex-direction: column; }

  .footer { padding: 56px 0 24px; }
  .footer-grid { grid-template-columns: 1fr; gap: 36px; padding-bottom: 36px; }
  .footer-bottom { flex-direction: column; align-items: flex-start; }
}
```

- [ ] **Step 3: 確認** — index.htmlを通しでブラウザ確認。Hero〜Footerまで通して違和感ないこと。SPでも全セクションが破綻なく表示

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/index.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add LINE CTA and footer (index.html complete)"
```

---

## Phase 3: 残りのページ（Day 2 終盤〜Day 3）

### Task 15: school.html — バストスクール詳細

**Files:**
- Create: `client/bolon-shareee/school.html`

- [ ] **Step 1: school.html を作成**

index.htmlを参考に、`<head>`部分は SEO/OGP/JSON-LD を school 向けに調整：

```html
<title>バストスクール｜B.villea｜株式会社Bolon Shareee</title>
<meta name="description" content="14年のサロン経営ノウハウを伝えるバストアップ起業スクール。福岡発、卒業後は当社業務委託パートナーとしての道も。代表蒲池百都子が直接指導します。">
<meta name="keywords" content="バストスクール 福岡,バストアップ 起業,バストケア 技術 習得,女性起業,B.villea スクール">
<link rel="canonical" href="https://sharkstars.jp/client/bolon-shareee/school.html">
<!-- OGP は index と同じ画像を使い、og:url と og:title をschoolに -->
```

bodyのヘッダー / フッターはindex.htmlからコピー。中身は：

```html
<main class="page-main">
  <!-- ページヘッダー -->
  <section class="page-hero">
    <div class="container">
      <p class="section-eyebrow">— Bust School</p>
      <h1 class="page-title">バストスクール</h1>
      <p class="page-lead">14年のサロン経験を、次の世代へ。<br>福岡発、バストアップ起業のためのスクール。</p>
    </div>
  </section>

  <!-- 想定対象 -->
  <section class="school-target">
    <div class="container">
      <p class="section-eyebrow">— Who</p>
      <h2 class="section-title">こんな方へ。</h2>
      <ul class="check-list">
        <li>サロンを開業したい女性</li>
        <li>美容業界で独立したい方</li>
        <li>育休からの復職で「自分の場所」を持ちたい方</li>
        <li>既存サロンに新メニューを加えたい方</li>
      </ul>
    </div>
  </section>

  <!-- カリキュラム -->
  <section class="school-curriculum">
    <div class="container">
      <p class="section-eyebrow">— Curriculum</p>
      <h2 class="section-title">学べること。</h2>
      <div class="curriculum-list">
        <article><h3>01 / 解剖学とお胸の基礎</h3><p>お胸の構造、ケアの基本理論。</p></article>
        <article><h3>02 / 手技</h3><p>14年で磨いた施術手技を、実技で。</p></article>
        <article><h3>03 / カウンセリング</h3><p>お客様の悩みに寄り添うコミュニケーション。</p></article>
        <article><h3>04 / 経営・集客</h3><p>個人事業から法人化までの実践。</p></article>
      </div>
      <p class="curriculum-note">※カリキュラム詳細・期間・受講料は仮表示です。LINEまたはお問い合わせよりご案内します。</p>
    </div>
  </section>

  <!-- 卒業後のサポート -->
  <section class="school-support">
    <div class="container">
      <div class="support-block">
        <p class="section-eyebrow">— After</p>
        <h2 class="section-title">卒業後も、<br>つながり続けます。</h2>
        <p>当社の業務委託パートナーとして、サロン業務にご参画いただく道もあります。<br>独立開業のフォローアップも継続。</p>
        <a href="contact.html" class="hero-cta">お問い合わせ・資料請求 →</a>
      </div>
    </div>
  </section>
</main>
```

CSS追加（style.css末尾）：

```css
/* ============================================================
   Page common (school / company / faq / contact / privacy)
   ============================================================ */

.page-main { padding-top: 72px; }
@media (max-width: 880px) { .page-main { padding-top: 60px; } }

.page-hero {
  padding: var(--space-xxl) 0 var(--space-xl);
  background: var(--bg-warm);
}
.page-title {
  font-family: var(--font-jp-serif);
  font-size: 56px;
  letter-spacing: 0.05em;
  margin: 16px 0 24px;
  font-weight: 500;
}
.page-lead {
  font-family: var(--font-jp-sans);
  font-size: 16px;
  line-height: 2.0;
  color: var(--text-sub);
  max-width: 720px;
}

@media (max-width: 880px) {
  .page-title { font-size: 34px; }
  .page-lead { font-size: 14px; }
}

/* school */
.school-target, .school-curriculum, .school-support { padding: var(--space-xxl) 0; }
.school-target { background: var(--bg-base); }
.school-curriculum { background: var(--bg-warm); }
.school-support { background: var(--text-main); color: var(--bg-warm); }
.school-support .section-eyebrow { color: var(--gold); }
.school-support .section-title { color: #fff; }
.school-support p { color: rgba(251,246,239,0.85); font-family: var(--font-jp-sans); font-size: 15px; line-height: 2.0; margin: 16px 0 28px; }
.support-block { max-width: 700px; }

.check-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-top: 36px;
}
.check-list li {
  font-family: var(--font-jp-sans);
  font-size: 15px;
  padding: 16px 24px;
  background: var(--bg-warm);
  border-radius: 4px;
  position: relative;
  padding-left: 48px;
}
.check-list li::before {
  content: '✓';
  position: absolute;
  left: 20px; top: 50%;
  transform: translateY(-50%);
  color: var(--primary);
  font-weight: 700;
}

.curriculum-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-top: 36px;
}
.curriculum-list article {
  background: var(--bg-base);
  padding: 32px 28px;
  border-radius: 4px;
}
.curriculum-list h3 {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 18px;
  letter-spacing: 0.06em;
  color: var(--primary);
  margin-bottom: 12px;
}
.curriculum-list article > p {
  font-family: var(--font-jp-sans);
  font-size: 13px;
  line-height: 1.95;
  color: var(--text-sub);
}
.curriculum-note {
  text-align: center;
  font-size: 12px;
  color: var(--text-sub);
  margin-top: 28px;
  font-family: var(--font-jp-sans);
}

@media (max-width: 880px) {
  .check-list, .curriculum-list { grid-template-columns: 1fr; gap: 12px; }
}
```

- [ ] **Step 2: ブラウザ確認** — school.html がヘッダー / 4セクション / フッター揃って表示

- [ ] **Step 3: Commit**

```bash
git add client/bolon-shareee/school.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add school.html (bust school detail page)"
```

---

### Task 16: company.html — 会社情報詳細

**Files:**
- Create: `client/bolon-shareee/company.html`

- [ ] **Step 1: company.html を作成**

`<head>`：
```html
<title>会社情報｜株式会社Bolon Shareee</title>
<meta name="description" content="株式会社Bolon Shareeeの会社情報。バストアップ専門サロンB.villea、バストスクール、バスト機器代理店の3事業を運営。代表 蒲池百都子、福岡市中央区警固。">
<link rel="canonical" href="https://sharkstars.jp/client/bolon-shareee/company.html">
```

中身：
```html
<main class="page-main">
  <section class="page-hero">
    <div class="container">
      <p class="section-eyebrow">— Company</p>
      <h1 class="page-title">会社情報</h1>
      <p class="page-lead">株式会社Bolon Shareee は、<br>3つの事業を通じて女性の美と自信を支える企業です。</p>
    </div>
  </section>

  <!-- 会社概要テーブル -->
  <section class="company-table-sec">
    <div class="container">
      <p class="section-eyebrow">— Overview</p>
      <h2 class="section-title">会社概要</h2>
      <dl class="company-table">
        <div><dt>商号</dt><dd>株式会社 Bolon Shareee（ボロン シャリィ）</dd></div>
        <div><dt>代表取締役</dt><dd>蒲池 百都子（がま ちもとこ）</dd></div>
        <div><dt>設立</dt><dd>2025年12月26日<br><small>※前身の個人事業は2013年2月4日開業</small></dd></div>
        <div><dt>所在地</dt><dd>〒810-0023<br>福岡市中央区警固2-13-17 S-FORT警固タワー 1801</dd></div>
        <div><dt>連絡先</dt><dd>TEL: 090-9574-9566<br>Mail: motoko19750204@gmail.com</dd></div>
        <div><dt>従業員</dt><dd>業務委託パートナー制</dd></div>
        <div><dt>事業内容</dt><dd>
          ① バストアップ専門サロン B.villea の運営<br>
          ② バストスクール（育成事業）の運営<br>
          ③ バストアップ機器の代理店・販売
        </dd></div>
      </dl>
    </div>
  </section>

  <!-- 事業詳細（index と内容共通） -->
  <section class="company-summary">
    <div class="container">
      <p class="section-eyebrow">— Businesses</p>
      <h2 class="section-title">3つの事業について。</h2>
      <!-- index.html の business-list と同じ内容を再掲 -->
    </div>
  </section>

  <!-- B2B 問い合わせ誘導 -->
  <section class="company-cta">
    <div class="container">
      <h2 class="section-title">代理店・スクール・<br>業務委託のご相談。</h2>
      <p>B to B のご相談、機器販売や提携、業務委託パートナーの応募などはお問い合わせフォームよりご連絡ください。</p>
      <a href="contact.html" class="hero-cta">お問い合わせフォームへ →</a>
    </div>
  </section>
</main>
```

CSS追加：
```css
.company-table-sec { padding: var(--space-xxl) 0; }
.company-table {
  margin-top: 36px;
  border-top: 1px solid var(--border);
}
.company-table > div {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 32px;
  padding: 24px 0;
  border-bottom: 1px solid var(--border);
  align-items: start;
}
.company-table dt {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 13px;
  letter-spacing: 0.14em;
  color: var(--primary);
}
.company-table dd {
  font-family: var(--font-jp-sans);
  font-size: 15px;
  line-height: 2.0;
  color: var(--text-main);
}
.company-table dd small { display: block; font-size: 12px; color: var(--text-sub); margin-top: 4px; }

.company-cta { padding: var(--space-xxl) 0; background: var(--text-main); color: var(--bg-warm); text-align: center; }
.company-cta .section-title { color: #fff; margin-bottom: 24px; }
.company-cta p { font-family: var(--font-jp-sans); font-size: 15px; line-height: 2.0; color: rgba(251,246,239,0.85); margin-bottom: 32px; max-width: 640px; margin-left: auto; margin-right: auto; }

@media (max-width: 880px) {
  .company-table > div { grid-template-columns: 1fr; gap: 6px; padding: 20px 0; }
  .company-table dt { font-size: 12px; }
  .company-table dd { font-size: 14px; }
}
```

- [ ] **Step 2: ブラウザ確認** — company.html を開いて、会社概要テーブル + 事業詳細 + B2B CTA が見える

- [ ] **Step 3: Commit**

```bash
git add client/bolon-shareee/company.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add company.html (corporate info page)"
```

---

### Task 17: faq.html — 全FAQ

**Files:**
- Create: `client/bolon-shareee/faq.html`

- [ ] **Step 1: faq.html を作成**

`<head>` に FAQPage JSON-LD を追加：
```html
<title>よくあるご質問｜B.villea</title>
<meta name="description" content="B.villea / 株式会社Bolon Shareee へよくいただくご質問。施術内容、料金、初回の流れ、男性スタッフの有無など。">
<link rel="canonical" href="https://sharkstars.jp/client/bolon-shareee/faq.html">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "お胸の変化は本当にありますか？", "acceptedAnswer": { "@type": "Answer", "text": "個人差はありますが、続けていただくことで多くのお客様に変化を感じていただいています。" } },
    { "@type": "Question", "name": "初めてでも大丈夫ですか？", "acceptedAnswer": { "@type": "Answer", "text": "もちろんです。初めての方にはカウンセリングからお流れをご説明します。" } },
    { "@type": "Question", "name": "男性スタッフはいますか？", "acceptedAnswer": { "@type": "Answer", "text": "スタッフは全員女性です。" } },
    { "@type": "Question", "name": "完全予約制ですか？", "acceptedAnswer": { "@type": "Answer", "text": "はい、完全予約制です。LINEより優先的にご予約を承っています。" } },
    { "@type": "Question", "name": "支払い方法は？", "acceptedAnswer": { "@type": "Answer", "text": "現金・各種電子決済に対応しております（詳細はカウンセリング時にご案内）。" } },
    { "@type": "Question", "name": "通う頻度はどれくらいが目安ですか？", "acceptedAnswer": { "@type": "Answer", "text": "個人差・お悩みにより異なります。カウンセリング時にお一人ずつご提案します。" } }
  ]
}
</script>
```

中身：
```html
<main class="page-main">
  <section class="page-hero">
    <div class="container">
      <p class="section-eyebrow">— Questions</p>
      <h1 class="page-title">よくあるご質問</h1>
      <p class="page-lead">皆さまから多くいただくご質問をまとめました。<br>ここにないご質問は、LINEまたはお問い合わせフォームよりお気軽にどうぞ。</p>
    </div>
  </section>

  <section class="faq-full">
    <div class="container">
      <div class="faq-items">
        <!-- 6項目を details/summary で並べる -->
        <details class="faq-item">
          <summary class="faq-q">お胸の変化は、本当にありますか？</summary>
          <div class="faq-a">個人差はありますが、続けていただくことで多くのお客様に変化を感じていただいています。詳しくはカウンセリング時にご相談ください。<br><small>※個人の感想であり、効果には個人差があります。</small></div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">初めてでも大丈夫ですか？</summary>
          <div class="faq-a">もちろんです。初めての方には、カウンセリングからお流れをご説明し、安心して受けていただけるようにしています。</div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">男性スタッフはいますか？</summary>
          <div class="faq-a">スタッフは全員女性です（代表 蒲池 + 業務委託の女性スタッフ）。</div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">完全予約制ですか？</summary>
          <div class="faq-a">はい、完全予約制です。お客様ひと組ずつのプライベートな空間で施術を受けていただきます。LINEより優先的にご予約を承っています。</div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">支払い方法は？</summary>
          <div class="faq-a">現金・各種電子決済に対応しております（詳細はカウンセリング時にご案内します）。</div>
        </details>
        <details class="faq-item">
          <summary class="faq-q">通う頻度はどれくらいが目安ですか？</summary>
          <div class="faq-a">個人差・お悩みにより異なります。一般的には◯週間に一度のペースで通っていただく方が多いですが、初回カウンセリング時にお一人ずつご提案します。</div>
        </details>
      </div>
    </div>
  </section>

  <!-- LINE CTA再掲 -->
  <section class="line-cta">
    <div class="container">
      <h2 class="line-headline">他のご質問は<br><span class="accent">LINEでお気軽に。</span></h2>
      <div class="line-actions">
        <a href="https://lin.ee/" class="line-btn line-btn-primary" target="_blank" rel="noopener"><span class="line-icon">L</span>LINEで相談する</a>
      </div>
    </div>
  </section>
</main>
```

CSS追加：
```css
.faq-full { padding: var(--space-xxl) 0; }
.faq-full .faq-items { max-width: 880px; margin: 0 auto; }
```

- [ ] **Step 2: JSON-LD バリデーション** — schema.org validator で FAQPage が正しく検出されることを確認

- [ ] **Step 3: Commit**

```bash
git add client/bolon-shareee/faq.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add faq.html with FAQPage JSON-LD"
```

---

### Task 18: contact.html — LINE誘導 + フォーム

**Files:**
- Create: `client/bolon-shareee/contact.html`

- [ ] **Step 1: contact.html を作成**

`<head>` に：
```html
<title>お問い合わせ｜B.villea｜株式会社Bolon Shareee</title>
<meta name="description" content="B.villea / 株式会社Bolon Shareee へのお問い合わせ。LINE優先、お電話・フォームも対応。福岡市中央区警固からお返事します。">
<link rel="canonical" href="https://sharkstars.jp/client/bolon-shareee/contact.html">
```

中身：
```html
<main class="page-main">
  <section class="page-hero">
    <div class="container">
      <p class="section-eyebrow">— Contact</p>
      <h1 class="page-title">お問い合わせ</h1>
      <p class="page-lead">LINEでのご連絡を優先してお返事しています。<br>お電話・フォームでもお気軽にどうぞ。</p>
    </div>
  </section>

  <section class="contact-routes">
    <div class="container">
      <div class="route-grid">
        <a href="https://lin.ee/" class="route-card route-line" target="_blank" rel="noopener">
          <div class="route-icon">L</div>
          <h3>LINE で相談</h3>
          <p>友だち追加から、Motokoが直接お返事します。</p>
          <span class="route-arrow">→</span>
        </a>
        <a href="tel:+819095749566" class="route-card">
          <div class="route-icon icon-tel">℡</div>
          <h3>電話する</h3>
          <p>090-9574-9566<br><small>※施術中は折り返しになる場合あり</small></p>
          <span class="route-arrow">→</span>
        </a>
        <div class="route-card route-form-anchor">
          <div class="route-icon icon-form">✎</div>
          <h3>フォーム</h3>
          <p>下記フォームより、お気軽に。</p>
        </div>
      </div>
    </div>
  </section>

  <section class="contact-form-sec">
    <div class="container">
      <p class="section-eyebrow">— Form</p>
      <h2 class="section-title">お問い合わせフォーム</h2>
      <form class="contact-form" action="#" method="post" novalidate>
        <label>お名前 <span class="req">必須</span><input type="text" name="name" required></label>
        <label>メールアドレス <span class="req">必須</span><input type="email" name="email" required></label>
        <label>電話番号<input type="tel" name="tel"></label>
        <label>ご相談内容<select name="topic"><option>サロン体験について</option><option>料金について</option><option>バストスクールについて</option><option>機器販売について</option><option>業務委託について</option><option>その他</option></select></label>
        <label>メッセージ <span class="req">必須</span><textarea name="message" rows="6" required></textarea></label>
        <p class="form-note">送信前に<a href="privacy.html">プライバシーポリシー</a>をご確認ください。</p>
        <button type="submit" class="hero-cta">送信する →</button>
      </form>
    </div>
  </section>
</main>
```

CSS追加：
```css
.contact-routes { padding: var(--space-xl) 0; }
.route-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
}
.route-card {
  display: block;
  padding: 36px 28px;
  background: var(--bg-warm);
  border-radius: 4px;
  position: relative;
  transition: transform .2s var(--ease), box-shadow .2s var(--ease);
  color: var(--text-main);
}
.route-card:hover { transform: translateY(-3px); box-shadow: 0 10px 36px rgba(0,0,0,.06); color: var(--text-main); }
.route-icon {
  display: inline-grid;
  place-items: center;
  width: 44px; height: 44px;
  background: var(--primary);
  color: #fff;
  border-radius: 50%;
  font-family: var(--font-en-serif);
  font-weight: 700;
  font-size: 22px;
  margin-bottom: 20px;
}
.route-line .route-icon { background: #06C755; }
.icon-form, .icon-tel { font-size: 20px; }
.route-card h3 { font-size: 18px; margin-bottom: 8px; letter-spacing: 0.05em; }
.route-card p { font-family: var(--font-jp-sans); font-size: 13px; line-height: 1.85; color: var(--text-sub); }
.route-card small { font-size: 11px; }
.route-arrow {
  position: absolute;
  right: 24px; bottom: 24px;
  font-family: var(--font-en-serif);
  font-size: 24px;
  color: var(--primary);
}

.contact-form-sec { padding: var(--space-xxl) 0; }
.contact-form { max-width: 640px; margin: 36px auto 0; display: flex; flex-direction: column; gap: 20px; }
.contact-form label {
  display: block;
  font-family: var(--font-jp-sans);
  font-size: 13px;
  letter-spacing: 0.1em;
  color: var(--text-main);
}
.contact-form .req {
  display: inline-block;
  margin-left: 8px;
  padding: 2px 8px;
  background: var(--primary);
  color: #fff;
  font-size: 10px;
  border-radius: 99px;
  letter-spacing: 0.08em;
}
.contact-form input, .contact-form select, .contact-form textarea {
  display: block;
  width: 100%;
  margin-top: 8px;
  padding: 14px 16px;
  font-family: var(--font-jp-sans);
  font-size: 16px; /* iOSズーム防止 */
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--bg-base);
  transition: border-color .2s;
}
.contact-form input:focus, .contact-form select:focus, .contact-form textarea:focus {
  outline: none;
  border-color: var(--primary);
}
.form-note { font-size: 12px; color: var(--text-sub); font-family: var(--font-jp-sans); }
.form-note a { border-bottom: 1px solid var(--text-sub); }

@media (max-width: 880px) {
  .route-grid { grid-template-columns: 1fr; gap: 12px; }
}
```

- [ ] **Step 2: ブラウザ確認** — 3ルート（LINE/電話/フォーム）+ フォームが表示。SP対応OK

- [ ] **Step 3: Commit**

```bash
git add client/bolon-shareee/contact.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add contact.html with LINE/phone/form routes"
```

---

### Task 19: privacy.html — プライバシーポリシー

**Files:**
- Create: `client/bolon-shareee/privacy.html`

- [ ] **Step 1: privacy.html を作成（mukuのprivacy.htmlを参照しつつ会社名差し替え）**

`<head>`：
```html
<title>プライバシーポリシー｜株式会社Bolon Shareee</title>
<meta name="description" content="株式会社Bolon Shareee（B.villea）のプライバシーポリシー。個人情報の取扱いについて。">
<link rel="canonical" href="https://sharkstars.jp/client/bolon-shareee/privacy.html">
<meta name="robots" content="noindex,nofollow">
```

中身（標準的なプライバシーポリシー雛形）：
```html
<main class="page-main">
  <section class="page-hero">
    <div class="container">
      <p class="section-eyebrow">— Privacy Policy</p>
      <h1 class="page-title">プライバシーポリシー</h1>
      <p class="page-lead">株式会社Bolon Shareee（B.villea）は、お客様の個人情報を以下のとおり取り扱います。</p>
    </div>
  </section>

  <section class="privacy-body">
    <div class="container">
      <article class="legal-article">
        <h2>1. 個人情報の定義</h2>
        <p>本ポリシーにおける「個人情報」とは、お客様個人を識別できる氏名・住所・電話番号・メールアドレス等を指します。</p>

        <h2>2. 利用目的</h2>
        <ul>
          <li>お問い合わせへの対応</li>
          <li>サービス・施術のご提供</li>
          <li>商品・サービスのご案内</li>
        </ul>

        <h2>3. 第三者提供</h2>
        <p>法令に基づく場合を除き、お客様の同意なく第三者へ個人情報を提供することはありません。</p>

        <h2>4. 開示・訂正・削除</h2>
        <p>お客様ご本人からの請求に基づき、適切に対応します。お問い合わせフォームよりご連絡ください。</p>

        <h2>5. お問い合わせ</h2>
        <p>株式会社Bolon Shareee<br>〒810-0023 福岡市中央区警固2-13-17 S-FORT警固タワー 1801<br>TEL: 090-9574-9566 / Mail: motoko19750204@gmail.com</p>

        <h2>6. 改定</h2>
        <p>本ポリシーは予告なく改定する場合があります。改定後は本ページに掲示します。</p>

        <p class="privacy-date">制定: 2025年12月26日</p>
      </article>
    </div>
  </section>
</main>
```

CSS追加：
```css
.privacy-body { padding: var(--space-xxl) 0; }
.legal-article { max-width: 760px; margin: 0 auto; font-family: var(--font-jp-sans); }
.legal-article h2 {
  font-family: var(--font-jp-serif);
  font-size: 22px;
  letter-spacing: 0.06em;
  margin: 36px 0 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}
.legal-article p { font-size: 14px; line-height: 2.0; color: var(--text-sub); margin-bottom: 16px; }
.legal-article ul { padding-left: 28px; margin-bottom: 16px; }
.legal-article ul li { font-size: 14px; line-height: 2.0; color: var(--text-sub); list-style: disc; }
.privacy-date { margin-top: 48px; text-align: right; color: var(--text-sub); font-style: italic; }
```

- [ ] **Step 2: Commit**

```bash
git add client/bolon-shareee/privacy.html client/bolon-shareee/css/style.css
git commit -m "feat(bolon-shareee): add privacy.html"
```

---

## Phase 4: アセット & 仕上げ（Day 3）

### Task 20: Bolon Shareee テキストロゴ（SVG）作成

**Files:**
- Create: `client/bolon-shareee/images/logo.svg`
- Modify: `client/bolon-shareee/index.html` ヘッダー `.logo` 部分（任意でロゴ画像差し替え）

- [ ] **Step 1: ロゴSVGを作成**

`client/bolon-shareee/images/logo.svg`：

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 60" role="img" aria-label="Bolon Shareee">
  <style>
    .logo-text { font-family: 'Cormorant Garamond', 'Garamond', serif; font-weight: 500; letter-spacing: 0.06em; }
    .b-mark { font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 500; }
  </style>
  <text x="0" y="42" class="logo-text" font-size="36" fill="#3A1A2A">Bolon</text>
  <text x="118" y="42" class="logo-text" font-size="36" fill="#C8276B" font-style="italic">Shareee</text>
  <line x1="0" y1="52" x2="290" y2="52" stroke="#D4A657" stroke-width="0.5"/>
</svg>
```

- [ ] **Step 2: ファビコン用にPNG縮小版も作成（オプション、SVGがあれば省略可）**

- [ ] **Step 3: company.html / footer などで使用したい場合は <img src="images/logo.svg"> で挿入可能**

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/images/logo.svg
git commit -m "feat(bolon-shareee): add Bolon Shareee text logo (SVG)"
```

---

### Task 21: OGP画像作成（1200×630）

**Files:**
- Create: `client/bolon-shareee/images/ogp.png`

**手順:** HTML→ブラウザでスクショ→トリミング→PNG出力。または既存のHTMLテンプレを使う。

- [ ] **Step 1: 一時HTMLをローカル作成（git管理外）**

`scratch-ogp.html`（プロジェクトルート、後で削除）：

```html
<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,500&family=Zen+Old+Mincho:wght@500;600&display=swap" rel="stylesheet">
<style>
  body { margin:0; }
  .ogp { width:1200px; height:630px; background:linear-gradient(135deg,#FBF6EF 0%,#fff 60%,#FBF6EF 100%); padding:80px; box-sizing:border-box; position:relative; overflow:hidden; }
  .ogp::before { content:''; position:absolute; right:-100px; top:-100px; width:600px; height:600px; background:radial-gradient(circle,#C8276B22 0%,transparent 70%); }
  .eyebrow { font-family:'Cormorant Garamond',serif; font-style:italic; font-size:24px; letter-spacing:0.2em; color:#C8276B; margin:0 0 32px; }
  .title { font-family:'Zen Old Mincho',serif; font-size:84px; line-height:1.5; color:#3A1A2A; letter-spacing:0.04em; margin:0 0 48px; font-weight:600; }
  .title em { color:#C8276B; font-style:normal; }
  .meta { font-family:'Zen Old Mincho',serif; font-size:22px; color:#5A4050; }
  .brand { position:absolute; bottom:60px; right:80px; font-family:'Cormorant Garamond',serif; font-style:italic; font-size:28px; color:#D4A657; letter-spacing:0.18em; }
</style></head>
<body>
<div class="ogp">
  <p class="eyebrow">— Bougainvillea Blooms</p>
  <h1 class="title">咲き誇るあなたを、<br><em>ここから。</em></h1>
  <p class="meta">B.villea ／ 福岡・警固のバストアップ専門サロン</p>
  <p class="brand">Bolon Shareee</p>
</div>
</body></html>
```

- [ ] **Step 2: ブラウザで `scratch-ogp.html` を開き、DevTools で viewport 1200×630 に固定、フルスクリーンショット撮影**

- [ ] **Step 3: 撮ったスクリーンショットを `client/bolon-shareee/images/ogp.png` として保存。`scratch-ogp.html` は削除**

```bash
# 確認
ls client/bolon-shareee/images/ogp.png
# サイズチェック（1200×630であること）
```

- [ ] **Step 4: Commit**

```bash
git add client/bolon-shareee/images/ogp.png
git commit -m "feat(bolon-shareee): add OGP image (1200x630)"
```

---

### Task 22: モバイル・全ページ動作確認 + 修正

**Files:**
- 全ページ（修正があれば）

- [ ] **Step 1: 全ページをローカルブラウザで開く**

PowerShell:
```powershell
Start-Process "client/bolon-shareee/index.html"
Start-Process "client/bolon-shareee/school.html"
Start-Process "client/bolon-shareee/company.html"
Start-Process "client/bolon-shareee/faq.html"
Start-Process "client/bolon-shareee/contact.html"
Start-Process "client/bolon-shareee/privacy.html"
```

- [ ] **Step 2: 各ページで DevTools モバイルビュー（iPhone 14 Pro / 390x844）で確認**

チェック項目：
- [ ] ヘッダーのハンバーガーが動く（タップでナビ展開、リンク押下で閉じる）
- [ ] Hero タイトルが1文字ずつ縦折り返しになっていない（`word-break: keep-all` 効いている）
- [ ] 全セクション横スクロールが発生していない（`overflow-x: hidden` 効いている）
- [ ] フォーム要素にフォーカスしてもズームしない（`font-size: 16px` 効いている）
- [ ] アコーディオン（FAQ）の開閉が動く
- [ ] スクロール時にヘッダーに `is-scrolled` クラスが付く

- [ ] **Step 3: 修正があればコミット**

```bash
# 必要なら
git commit -m "fix(bolon-shareee): mobile responsive adjustments"
```

---

### Task 23: SEO 全ページ最終確認 + sitemap.xml 追加

**Files:**
- Modify: `sitemap.xml`（ルート）
- Check: 全 .html ページ

- [ ] **Step 1: 各ページのSEOチェックリスト確認**

各ページで以下が揃っていることを確認：
- `<title>` がページごとに固有
- `<meta name="description">` がページごとに固有・120-160字
- `<link rel="canonical">` 正しいURL
- OGP（og:title, og:description, og:url, og:image, og:type）
- Twitter Card（twitter:card="summary_large_image", twitter:title, twitter:description, twitter:image）
- JSON-LD（index: Organization+LocalBusiness、faq: FAQPage、その他: Organization）
- `<html lang="ja">`

- [ ] **Step 2: sitemap.xml に追加**

```bash
# 現状を確認
cat sitemap.xml | head -30
```

`sitemap.xml` の `</urlset>` 直前に追加：
```xml
  <url><loc>https://sharkstars.jp/client/bolon-shareee/</loc><lastmod>2026-05-12</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>
  <url><loc>https://sharkstars.jp/client/bolon-shareee/school.html</loc><lastmod>2026-05-12</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>
  <url><loc>https://sharkstars.jp/client/bolon-shareee/company.html</loc><lastmod>2026-05-12</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>
  <url><loc>https://sharkstars.jp/client/bolon-shareee/faq.html</loc><lastmod>2026-05-12</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>
  <url><loc>https://sharkstars.jp/client/bolon-shareee/contact.html</loc><lastmod>2026-05-12</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>
```

(privacy.html は noindex なので追加しない)

- [ ] **Step 3: schema.org validator で index.html / faq.html の JSON-LD を最終チェック**

- [ ] **Step 4: Commit**

```bash
git add sitemap.xml
git commit -m "feat(bolon-shareee): add to sitemap.xml"
```

---

### Task 24: SHARKSTARS トップサイトの「制作実績」へ追加

**Files:**
- Modify: `index.html`（ルート）

- [ ] **Step 1: ルート `index.html` の制作実績ブロックを探す**

```bash
# どこにあるか確認
```

Grep ツールで `client/muku` を検索し、同じパターンで B.villea のカードを追加できる場所を特定。

- [ ] **Step 2: muku のカードと同じ構造で bolon-shareee のカードを追加**

例（既存パターンに従う）：
```html
<a href="client/bolon-shareee/" class="work-card">
  <div class="work-thumb" style="background-image: url('client/bolon-shareee/images/ogp.png');"></div>
  <div class="work-meta">
    <span class="work-cat">バストアップサロン・コーポレート</span>
    <h3 class="work-title">B.villea / 株式会社Bolon Shareee</h3>
    <p class="work-desc">福岡・警固のバストアップ専門サロン × 法人コーポレート。エディトリアル × ブーゲンビリア赤紫。</p>
  </div>
</a>
```

※ 具体的なHTML構造はルートのindex.htmlの既存実績エリアに合わせる。

- [ ] **Step 3: ブラウザでルート `index.html` を開き、制作実績にB.villeaが表示されることを確認**

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat(home): add B.villea / Bolon Shareee to portfolio works"
```

---

### Task 25: 最終総合確認 + 公開準備

**Files:**
- 全体

- [ ] **Step 1: 全ページの最終リンクチェック**

PowerShellでローカルプレビュー：
```powershell
# ルートから index.html → 各ページへのリンクが全部生きてるか
# 各ページから他ページ・LINEリンク・電話リンクへの遷移
```

各ページ間のナビゲーション・フッターリンク・LINE誘導・電話リンクが全て正しく動くこと。

- [ ] **Step 2: 全ファイル一覧確認**

```bash
ls -R client/bolon-shareee/
```

期待: 6 HTMLファイル + css/reset.css + css/style.css + js/main.js + images/logo.svg + images/ogp.png

- [ ] **Step 3: コンソールエラーチェック**

DevTools コンソールでエラー・警告がないことを確認（Google Fonts の読み込み・iframe・画像の404など）。

- [ ] **Step 4: 最終コミット & プッシュ準備**

```bash
git status
git log --oneline -25  # 全タスクのコミット履歴を確認
```

公開準備完了。クライアント（蒲池さん）にプレビューURL（GitHub Pagesまたはローカル）を共有して確認依頼。

---

## Self-Review Notes

- **Spec coverage**: 仕様書 §1-§10 すべて対応するタスクあり。素材未到着の写真等はTask 5/8でUnsplash仮置き、契約後差し替え運用（仕様書 §9.2 準拠）。
- **Type/path consistency**: CSS変数（`--primary` `--bg-warm` 等）、フォント変数、セクションクラス名（`.section-eyebrow` `.section-title` `.hero-cta` 等）を全タスク横断で統一。HTML側のID（`#story` `#menu` `#line`）もアンカーリンクと一致。
- **Mobile pitfalls**: memory記録のmuku落とし穴8項目（backdrop-filter / flex-direction / word-break / iOS zoom / 100svh / overflow-x / inline grid / 提携素材確認）すべて対策コードまたはルールに反映済み。
- **薬機法配慮**: Voice/FAQ抜粋・FAQ全頁すべて「※個人の感想」「効果には個人差」注記を明示記載。

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-05-12-bolon-shareee-website.md`. Two execution options:

**1. Subagent-Driven (recommended)** — タスクごとに別サブエージェントを立てて、完了ごとに本ターンでレビュー。タスク間で文脈を独立させられるので、CSSの肥大化や混乱を避けやすい。

**2. Inline Execution** — このセッション内で全タスクを順に実行。中断ポイントを設けつつバッチ進行。会話の流れが切れない代わりに、本セッションのコンテキストが大きくなる。

どちらで進めますか？
