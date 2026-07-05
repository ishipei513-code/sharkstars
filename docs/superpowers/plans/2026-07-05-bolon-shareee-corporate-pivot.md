# 株式会社Bolon Shareee コーポレート転換 実装プラン

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 既存のサロンLP型サイトを、株式会社Bolon Shareee 主役の純コーポレートサイト（A案・6ページ維持・2事業）へ転換する。

**Architecture:** 既存デザインシステム（Editorial × Gold）とCSSクラスを全面流用。新規CSSは「文字組ヒーロー(`hero-corporate`)＋ミッション帯」のみ。index.html をコーポレートTOPへ大改修し、サロンB2C要素（Before/After・Instagram）を `business.html#salon` へ移設。全6ページのロゴ・SEOを会社主役に統一（JSON-LDは変更不要）。

**Tech Stack:** 静的HTML5 / CSS3（CSS custom properties）/ バニラJS。ビルド無し。**自動テスト基盤なし** → 各タスクは grep検証＋ブラウザ目視＋HTML妥当性で確認する。

**参照スペック:** `docs/superpowers/specs/2026-07-05-bolon-shareee-corporate-pivot-design.md`

**ブランチ:** `feat/bolon-corporate-pivot`（作成済み・仕様書コミット済み fb07688）

---

## 前提・共通ルール（全タスク共通）

- **触るのは `client/bolon-shareee/` 配下のみ。** 他案件（marin/muku等）のファイルには一切触れない。
- 各ページの `<head>`（フォントlink・reset.css・style.css・JSON-LD）と `<script src="js/main.js">` は**維持**。フォントは Bodoni Moda + Cormorant Garamond + Zen Old Mincho + Zen Kaku Gothic Antique + Zen Old Mincho を読み込む既存linkをそのまま残す。
- **モバイル既踏み罠（必ず維持）:** ①ヘッダー backdrop-filter は880px以下でオフ ②フルハイトは `100vh`→`100svh` の順で二重指定 ③フォーム入力は `font-size:16px` ④見出しは `word-break:keep-all; overflow-wrap:normal` ⑤単一ブレークポイント880pxで1カラム化 ⑥`prefers-reduced-motion:reduce` 尊重 ⑦固定ヘッダー72px（モバイル60px）分の padding-top。
- **残す正当な"B.villea"（変更禁止）:** ヒーロー装飾縦書き、メッセージ署名、「B.villeaサロン」見出し、IGハンドル `@b.villea.fukuoka`、CSS/JSヘッダーコメント、`logo.svg` の aria-label、JSON-LD の `HealthAndBeautyBusiness` 名。
- **プレビュー確認方法:** 既定ブラウザで対象HTMLを直接開く。PowerShell: `Start-Process "d:\sharkstars\client\bolon-shareee\index.html"`。PC幅と、DevTablesの880px以下（例375px）でレイアウト崩れ・横スクロール無しを目視。
- **コミット単位:** 各タスク末尾で該当ファイルのみ `git add <path>` → コミット。コミットメッセージ末尾に必ず改行して `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`。

---

## ファイル構成（変更マップ）

| ファイル | 責務 | 本プランでの変更 |
| --- | --- | --- |
| `css/style.css` | デザインシステム | 末尾に `hero-corporate` / `mission` 用の新規ブロックを追記（既存規則は変更しない） |
| `index.html` | コーポレートTOP | body を9セクション構成へ大改修。head meta を会社主役に |
| `business.html` | 事業詳細（2事業） | 3→2事業。#salon にBefore/After・Instagramを受け入れ、#equipment を#schoolへ内包・削除 |
| `company.html` | 会社概要 | 事業内容3→2、カード3→2、#equipmentリンク付替、ロゴ・og:site_name |
| `contact.html` | 総合問い合わせ | ロゴ・title/desc会社主役、フォーム項目を2事業に整理 |
| `faq.html` | サロン客FAQ | ロゴ・title・OGP会社主役（本文維持） |
| `privacy.html` | 法務 | ロゴ替えのみ |

---

## Task 1: 全6ページのロゴを会社主役に統一（機械的・低リスク）

**Files:**
- Modify: `client/bolon-shareee/index.html`, `business.html`, `company.html`, `contact.html`, `faq.html`, `privacy.html`（各ヘッダー `.logo` とフッター `.footer-logo`/`.footer-corp`）

- [ ] **Step 1: 現状の全ロゴ箇所を確認（テスト＝現状把握）**

Run:
```
grep -rn "class=\"logo\"" client/bolon-shareee/*.html
grep -rn "footer-logo" client/bolon-shareee/*.html
```
Expected: 6ページ全てのヘッダー `.logo` が `>B.villea<`、フッターが `<p class="footer-logo">B.villea</p>` の直下に `<p class="footer-corp">株式会社Bolon Shareee</p>`。

- [ ] **Step 2: ヘッダーロゴを全6ページ置換**

各ページのヘッダーロゴ行:
```html
<a href="index.html" class="logo">B.villea</a>
```
を次へ:
```html
<a href="index.html" class="logo">Bolon Shareee</a>
```

- [ ] **Step 3: フッターロゴの順序を全6ページ入れ替え**

各ページの:
```html
<p class="footer-logo">B.villea</p>
<p class="footer-corp">株式会社Bolon Shareee</p>
```
を次へ:
```html
<p class="footer-logo">Bolon Shareee</p>
<p class="footer-corp">株式会社Bolon Shareee（バストアップ専門サロン B.villea）</p>
```

- [ ] **Step 4: 検証（会社主役に統一されたか）**

Run:
```
grep -rn "class=\"logo\">B.villea" client/bolon-shareee/*.html
grep -rn "footer-logo\">B.villea" client/bolon-shareee/*.html
```
Expected: **どちらもヒット0件**。
```
grep -rcn "class=\"logo\">Bolon Shareee" client/bolon-shareee/*.html
```
Expected: 6ページで各1件。

- [ ] **Step 5: コミット**

```
git add client/bolon-shareee/index.html client/bolon-shareee/business.html client/bolon-shareee/company.html client/bolon-shareee/contact.html client/bolon-shareee/faq.html client/bolon-shareee/privacy.html
git commit -m "refactor(bolon): ヘッダー/フッターロゴを会社(Bolon Shareee)主役に統一"
```

---

## Task 2: SEOメタを会社主役に統一（index / faq / contact ＋ og:site_name 5ページ）

**Files:**
- Modify: `client/bolon-shareee/index.html`（title L9, og:title L15, twitter:title L25, og:site_name L19）
- Modify: `client/bolon-shareee/faq.html`（title, og:title, twitter:title, og:site_name, meta description, keywords）
- Modify: `client/bolon-shareee/contact.html`（title, meta description, og:title, twitter:title, og:site_name）
- Modify: `client/bolon-shareee/business.html`, `company.html`（og:site_name のみ）

> business/company/privacy の `<title>` は既に会社主役のため変更しない。privacy はOGP無しのため対象外。

- [ ] **Step 1: 現状把握**

Run:
```
grep -rn "og:site_name" client/bolon-shareee/*.html
grep -rn "<title>" client/bolon-shareee/*.html
```
Expected: og:site_name は5ページ（index/business/company/contact/faq）で `content="B.villea / 株式会社Bolon Shareee"`。title は index/faq/contact が B.villea 先頭。

- [ ] **Step 2: og:site_name を5ページ一括で会社主役へ**

各該当行:
```html
<meta property="og:site_name" content="B.villea / 株式会社Bolon Shareee">
```
を:
```html
<meta property="og:site_name" content="株式会社Bolon Shareee / B.villea">
```

- [ ] **Step 3: index.html の title / og:title / twitter:title / description / og:description を会社主役へ**

> title は SERP/OGP で切れないよう ~30全角に収める（会社名＋2事業が見える長さ）。description は会社主役かつ**2事業**（機器販売はスクール内包）に更新し、旧文の「機器代理店＝3事業目」表現を排除する。

title:
```html
<title>株式会社Bolon Shareee｜福岡・警固のバストアップサロン＆スクール</title>
```
og:title:
```html
<meta property="og:title" content="株式会社Bolon Shareee｜福岡・警固のバストアップサロン＆スクール">
```
twitter:title:
```html
<meta name="twitter:title" content="株式会社Bolon Shareee｜福岡・警固のバストアップ・スクール事業">
```
meta description:
```html
<meta name="description" content="株式会社Bolon Shareee は福岡・警固を拠点に、バストアップ専門サロン「B.villea」と、その技術を伝えるスクール事業（施術機器の販売を含む）を運営しています。エステ歴23年・代表 蒲池百都子。">
```
og:description:
```html
<meta property="og:description" content="株式会社Bolon Shareee｜福岡・警固でバストアップサロン「B.villea」とスクール事業を運営。エステ歴23年・代表 蒲池百都子。">
```

- [ ] **Step 4: faq.html の title / og:title / twitter:title / description / keywords を会社主役へ**

```html
<title>よくあるご質問｜株式会社Bolon Shareee（B.villea）</title>
```
```html
<meta property="og:title" content="よくあるご質問｜株式会社Bolon Shareee（B.villea）">
<meta name="twitter:title" content="よくあるご質問｜株式会社Bolon Shareee">
```
meta description は先頭を会社主役に（例）:
```html
<meta name="description" content="株式会社Bolon Shareee が運営するバストアップ専門サロン B.villea へのよくあるご質問。初めての方・ご予約・施術内容・通い方・アクセスについてお答えします。">
```
keywords は先頭を会社主役に並べ替え（`株式会社Bolon Shareee,B.villea,...` の順）。

- [ ] **Step 5: contact.html の title / description / og:title / twitter:title を会社主役へ**

```html
<title>お問い合わせ｜株式会社Bolon Shareee</title>
```
```html
<meta name="description" content="株式会社Bolon Shareee（バストアップ専門サロン B.villea）へのお問い合わせ。サロンのご予約・スクール・機器のご相談まで、LINE・お電話・フォームで承ります。福岡市中央区警固より。">
```
```html
<meta property="og:title" content="お問い合わせ｜株式会社Bolon Shareee">
<meta name="twitter:title" content="お問い合わせ｜株式会社Bolon Shareee">
```

- [ ] **Step 6: 検証**

Run:
```
grep -rn "og:site_name" client/bolon-shareee/*.html
grep -rn "content=\"B.villea" client/bolon-shareee/*.html
```
Expected: og:site_name は全て `株式会社Bolon Shareee / B.villea`。`content="B.villea` 先頭のメタは0件（装飾縦書き等の本文は対象外）。JSON-LD の `"name": "株式会社Bolon Shareee"` と salon の `"name": "B.villea（ビーヴィレア）"` は**変更していない**ことを確認。

- [ ] **Step 7: コミット**

```
git add client/bolon-shareee/index.html client/bolon-shareee/faq.html client/bolon-shareee/contact.html client/bolon-shareee/business.html client/bolon-shareee/company.html
git commit -m "seo(bolon): title/OGP/site_nameを会社主役に統一(JSON-LDは会社名維持)"
```

---

## Task 3: 文字組ヒーロー＋ミッション帯のCSSを追加

**Files:**
- Modify: `client/bolon-shareee/css/style.css`（**末尾に追記のみ**。既存規則は編集しない）

- [ ] **Step 1: style.css 末尾に新規ブロックを追記**

```css
/* ============================================================
   Corporate Hero (typographic, no photo) + Mission band
   2026-07-05 コーポレート転換で追加
   ============================================================ */
.hero-corporate {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: calc(72px + var(--space-xl)) var(--container-pad) var(--space-xl);
  background: radial-gradient(120% 80% at 50% 0%, #ffffff 0%, var(--bg-warm) 58%, #f3e7d6 100%);
  overflow: hidden;
}
.hero-corporate::before {
  content: "";
  position: absolute;
  inset: 24px;
  border: 1px solid rgba(212, 166, 87, 0.35);
  pointer-events: none;
}
.hero-corp-inner {
  position: relative;
  max-width: 760px;
}
.hero-corp-eyebrow {
  font-family: var(--font-en-serif);
  font-style: italic;
  font-size: 15px;
  letter-spacing: 0.18em;
  color: var(--gold);
  margin-bottom: var(--space-md);
}
.hero-corp-title {
  font-family: var(--font-jp-serif);
  font-weight: 500;
  font-size: clamp(30px, 5vw, 52px);
  line-height: 1.4;
  letter-spacing: 0.06em;
  color: var(--text-main);
  word-break: keep-all;
  overflow-wrap: normal;
}
.hero-corp-rule {
  display: block;
  width: 48px;
  height: 1px;
  background: var(--gold);
  margin: var(--space-lg) auto;
}
.hero-corp-copy {
  font-family: var(--font-jp-serif);
  font-weight: 500;
  font-size: clamp(20px, 3.4vw, 30px);
  line-height: 1.85;
  letter-spacing: 0.08em;
  color: var(--primary);
  word-break: keep-all;
  overflow-wrap: normal;
}
.hero-corp-sub {
  margin-top: var(--space-md);
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 14px;
  letter-spacing: 0.08em;
  color: var(--text-sub);
}

/* Mission band */
.mission-body {
  max-width: 720px;
  margin: 0 auto;
  text-align: center;
  font-family: var(--font-jp-sans);
  font-weight: 300;
  font-size: 15px;
  line-height: 1.95;
  letter-spacing: 0.06em;
  color: var(--text-sub);
}

/* Contact CTA — ブランド・マゼンタの主ボタン（LINE緑と明確に区別） */
.line-btn.btn-contact { background: var(--primary); color: #fff; }
.line-btn.btn-contact:hover { background: var(--primary-deep); }

@media (max-width: 880px) {
  .hero-corporate {
    padding: calc(60px + var(--space-lg)) var(--container-pad) var(--space-lg);
  }
  .hero-corporate::before { inset: 14px; }
  .mission-body { font-size: 14px; }
}
```

- [ ] **Step 2: 既存 `.hero-scroll` が `.hero-corporate` 内でも機能するか確認**

`.hero-scroll` は既存で絶対配置（`.hero` 内前提）。`.hero-corporate` は `position:relative` なのでアンカーは効く。もし bottom 位置が合わなければ、次を追記:
```css
.hero-corporate .hero-scroll { position: absolute; bottom: 28px; left: 50%; transform: translateX(-50%); }
```
（既存 `.hero-scroll` に同等指定があれば不要。ブラウザ目視で判断。）

- [ ] **Step 3: 検証**

Run: `grep -n "hero-corporate" client/bolon-shareee/css/style.css`
Expected: 追記ブロックがヒット。既存の `.hero {` 規則は無傷（`grep -c "^.hero {" ...` が従来通り）。CSS構文エラーが無いこと（波括弧の対応）を目視。

- [ ] **Step 4: コミット**

```
git add client/bolon-shareee/css/style.css
git commit -m "style(bolon): 文字組ヒーロー(hero-corporate)とミッション帯CSSを追加"
```

---

## Task 4: index.html を コーポレートTOP（9セクション）へ大改修

**Files:**
- Modify: `client/bolon-shareee/index.html`（`<body>` 内。`<head>` は Task2 で更新済。header/footer のロゴは Task1 で更新済）

> `<head>`・`<header>`・`<footer>`・末尾 `<script>` は保持。**HERO〜CONTACT の中身を差し替える。** JSON-LD（Organization＋HealthAndBeautyBusiness）は保持。

- [ ] **Step 1: 旧ヒーロー（`<section class="hero">…</section>`）を文字組ヒーローに置換**

```html
<!-- ===== HERO (Corporate, typographic) ===== -->
<section class="hero-corporate">
  <div class="hero-corp-inner reveal">
    <p class="hero-corp-eyebrow">Bolon Shareee Inc.</p>
    <h1 class="hero-corp-title">株式会社Bolon&nbsp;Shareee</h1>
    <span class="hero-corp-rule" aria-hidden="true"></span>
    <p class="hero-corp-copy">女性の美と自信を、<br>事業で支える。</p>
    <p class="hero-corp-sub">福岡・警固｜バストアップ専門サロン &amp; スクール事業</p>
  </div>
  <a href="#mission" class="hero-scroll" aria-label="下へスクロール">
    <span class="hero-scroll-label">Scroll</span>
    <span class="hero-scroll-line" aria-hidden="true"></span>
  </a>
</section>
```

- [ ] **Step 2: 旧 MESSAGE を「ミッション帯」に差し替え（id=mission）**

旧 `<section class="message" id="message">…</section>` を次へ:
```html
<!-- ===== MISSION ===== -->
<section class="company-summary" id="mission">
  <div class="container reveal">
    <p class="section-eyebrow">— Mission</p>
    <h2 class="section-title">確かな技術を、<br>誠実に届ける。</h2>
    <p class="mission-body">
      株式会社Bolon Shareee は、福岡・警固を拠点に、<br>
      バストアップ専門サロン「B.villea」の運営と、その技術を次の世代へ伝えるスクール事業を営む会社です。<br>
      ひとりずつに寄り添う姿勢で、女性が自分らしく前を向ける場をつくります。
    </p>
  </div>
</section>
```

> コピー方針: ヒーローのタグライン「女性の美と自信を、事業で支える。」とは**別の言い回し**にする（同一文の反復＝AI感を避けるため）。ミッション帯は「会社が何をやっているか（2事業）」を語り、代表メッセージ（後述）は「創業者の個人的な動機（エステ歴23年）」を語る、と役割を分ける。

- [ ] **Step 3: 事業セクションを 3→2 カードへ差し替え（平等）**

旧 `<section class="company-summary" id="business">` 内の `.business-list`（3 article）を2 articleへ:
```html
<div class="business-list">
  <article class="business-item reveal">
    <div class="business-num">01</div>
    <h3 class="business-title">サロン事業 ／ B.villea</h3>
    <figure class="business-ph"><span>ここに写真が入ります</span></figure>
    <p class="business-desc">福岡・警固のバストアップ専門サロン。完全予約・完全個室で、おひとりずつに寄り添います。</p>
    <a href="business.html#salon" class="business-link">サロン事業を見る →</a>
  </article>
  <article class="business-item reveal">
    <div class="business-num">02</div>
    <h3 class="business-title">スクール事業</h3>
    <figure class="business-ph"><span>ここに写真が入ります</span></figure>
    <p class="business-desc">エステ歴23年の技術と経営の知見を、開業を目指す方へ。卒業後の業務委託や、施術機器の販売・導入サポートまで一貫して支えます。</p>
    <a href="business.html#school" class="business-link">スクール事業を見る →</a>
  </article>
</div>
```
見出し `<h2 class="section-title">` は「2つの事業で<br>女性を支える」に更新。CTA `business-cta` は「事業内容を詳しく見る →」のまま維持。

> `.business-link` は既存クラス（audit確認済）。無ければ `business-cta` を各カード下に流用。

- [ ] **Step 4: 代表メッセージを会社トーンで追加（旧 message の代表要素を昇格・再配置）**

事業セクションの後に、既存 `message` クラスで代表メッセージを配置:
```html
<!-- ===== REPRESENTATIVE MESSAGE ===== -->
<section class="message" id="rep-message">
  <div class="container">
    <p class="section-eyebrow reveal">— Message</p>
    <h2 class="message-headline reveal reveal--d1">
      ひとりの変化から、<br><span class="accent">事業へ。</span>
    </h2>
    <p class="message-body reveal reveal--d2">
      この道ひとすじ、エステ歴23年。技術を磨くほどに実感したのは、<br>
      変化のきっかけは「安心して委ねられる関係」から生まれるということでした。<br>
      B.villea で培った手技と姿勢を、スクールを通じて次の担い手へ。<br>
      女性が自分らしく輝ける場を、これからも事業として広げていきます。
    </p>
    <figure class="message-portrait reveal reveal--d3">
      <img src="images/C057417807.jpg" alt="代表取締役 蒲池百都子" loading="lazy" width="164" height="219">
    </figure>
    <p class="message-sign reveal reveal--d4">株式会社Bolon Shareee ／ 代表取締役 蒲池 百都子</p>
  </div>
</section>
```

- [ ] **Step 5: Before/After・Instagram セクションは この Task では残す（移設は Task5 で原子的に実施）**

`<section class="gallery" id="gallery">…</section>` と `<section class="insta" id="insta">…</section>` は **この Task では削除しない**。Task5 で「live な index.html からコピー → business.html へ貼付 → index から削除 → 両ファイルを同一コミット」を原子的に行う。subagent実行でも移設元が確実に存在するよう、index.html にマークアップを残したまま次へ進む。（配置は代表メッセージの後・声セクションの前のまま。）

- [ ] **Step 6: お客様の声（voice）は維持（信頼材料）**

`<section class="voice" id="voice">…</section>` はそのまま残す。文言変更不要。「個人差」注記維持。

- [ ] **Step 7: 会社情報ブロックを「会社概要抜粋」に差し替え**

旧 `<section class="access" id="access">`（営業時間・定休日・完全予約制・HotPepper予約を含むサロン運営情報）を、会社概要抜粋へ:
```html
<!-- ===== COMPANY SUMMARY ===== -->
<section class="company-summary" id="company">
  <div class="container">
    <p class="section-eyebrow reveal">— Company</p>
    <h2 class="section-title reveal reveal--d1">会社概要</h2>
    <div class="studio-grid studio-grid-solo reveal reveal--d1">
      <dl class="studio-info">
        <div><dt>商号</dt><dd>株式会社Bolon Shareee</dd></div>
        <div><dt>代表者</dt><dd>代表取締役 蒲池 百都子</dd></div>
        <div><dt>設立</dt><dd>2025年12月26日<br><small>（前身の個人事業は2013年2月開業）</small></dd></div>
        <div><dt>所在地</dt><dd>〒810-0023<br>福岡市中央区警固2-13-17<br>S-FORT警固タワー 1801</dd></div>
        <div><dt>事業内容</dt><dd>バストアップ専門サロンの運営（B.villea）<br>バストアップ起業スクールの運営（施術機器の販売・代理店を含む）</dd></div>
      </dl>
    </div>
    <a href="company.html" class="business-cta reveal">会社概要を詳しく見る →</a>
  </div>
</section>
```

- [ ] **Step 8: お問い合わせCTAを「問合を主・LINEを副」に差し替え**

旧 `<section class="contact-cta-sec" id="contact-cta">` の見出しを「お気軽にご相談ください」にする。リード段落を置く場合は**既存の `access-cta-lead` クラス**（`.contact-cta-sec` 用にボタン前 margin-bottom 32px/モバイル24px を持つ）で「サロンのご予約から、スクール・機器のご相談まで。まずは総合お問い合わせ窓口へ。」を配置する（`.mission-body` は縦マージン0でボタンが詰まるため**使わない**）。`.line-actions` を次へ:
```html
<div class="line-actions reveal reveal--d1">
  <a href="contact.html" class="line-btn btn-contact">お問い合わせはこちら</a>
  <a href="https://lin.ee/" class="line-btn line-btn-primary" target="_blank" rel="noopener">公式LINEはこちら</a>
</div>
```

> 配色の意図（緑ボタン問題の回避）: お問い合わせ＝**ブランド・マゼンタ**（`btn-contact`＝Task3で追加した `background:var(--primary)`）で最優先。公式LINE＝**LINE緑**（既存 `line-btn-primary` の #06C755）で副。**緑ボタンを「お問い合わせ」に使わない。** 優先度は「色（マゼンタ＞緑）」と「並び順（問合を先頭）」で表現する。既存 `.line-cta` バンド内の緑配色は変更しない。

- [ ] **Step 9: JSON-LD 確認（変更しない）**

`<head>` の JSON-LD で `Organization`（`"name":"株式会社Bolon Shareee"`）と `HealthAndBeautyBusiness`（`"name":"B.villea（ビーヴィレア）"`）が**そのまま**残っていることを確認。変更不要。

- [ ] **Step 10: 検証**

Run:
```
grep -n "hero-corporate\|id=\"mission\"\|id=\"rep-message\"\|id=\"company\"" client/bolon-shareee/index.html
```
Expected: 各1件。
```
grep -n "id=\"gallery\"\|id=\"insta\"" client/bolon-shareee/index.html
```
Expected: **この時点ではまだ各1件残存が正常**（gallery/insta の移設・削除は Task5 で実施）。
ブラウザで index.html を開き、PC/375px の両方で: ①文字組ヒーローがクリーム地で表示・横スクロール無し ②ヒーロー→ミッション→2事業→代表→(gallery/insta残)→声→会社概要→CTA の順で表示 ③代表写真が表示 ④声セクション健在 ⑤お問い合わせボタンがマゼンタ・LINEが緑で問合が先頭 ⑥崩れ無し。

- [ ] **Step 11: コミット**

```
git add client/bolon-shareee/index.html
git commit -m "feat(bolon): TOPをコーポレート化(文字組ヒーロー/ミッション/2事業/代表/会社概要/CTA)"
```

---

## Task 5: business.html を2事業へ再編（#salonにBA・IG受入、#equipmentを#schoolへ内包）

**Files:**
- Modify: `client/bolon-shareee/business.html`

- [ ] **Step 1: ページリードを 3→2 事業へ**

```html
<p class="page-lead">株式会社Bolon Shareee は<br>2つの事業で女性の美と自信を支えています。</p>
```

- [ ] **Step 1b: business.html の HEADメタを2事業へ（「3事業／バスト機器代理店」を排除）**

`<head>` に残る「3事業／バスト機器代理店」表現を2事業（サロン＋スクール〈機器販売含む〉）に更新する。対象は `<meta name="description">`・`<meta property="og:description">`（L16付近）・`<meta name="twitter:description">`（L26付近）。例:
```html
<meta name="description" content="株式会社Bolon Shareeeの事業内容。バストアップ専門サロンB.villeaと、その技術を伝えるスクール事業（施術機器の販売を含む）の2事業。福岡発、代表蒲池百都子。">
<meta property="og:description" content="バストアップ専門サロンB.villeaと、スクール事業（施術機器の販売を含む）の2事業。福岡発、代表蒲池百都子。">
<meta name="twitter:description" content="バストアップ専門サロン・スクール（機器販売を含む）の2事業。福岡発、代表蒲池百都子。">
```
検証: `grep -n "機器代理店\|3事業" client/bolon-shareee/business.html` が0件。JSON-LD `name`/`@type` は不変。

- [ ] **Step 2: #salon の末尾に、live な index.html からコピーした Before/After・Instagram を挿入**

**先に `client/bolon-shareee/index.html` を開き**、`<section class="gallery" id="gallery">` の `.ba-list`（3 figure）と `<section class="insta" id="insta">` の `.insta-grid`（3 a.insta-card）の**現物マークアップを取得**する。`<section class="biz-detail" id="salon">` 内、HotPepper予約CTA（`<a ... class="hero-cta">ホットペッパービューティーで予約する →</a>`）の**直前**に、取得した2ブロックを `school-block` でラップして挿入:
```html
<div class="school-block">
  <p class="section-eyebrow">— Before / After</p>
  <h3 class="biz-subhead">バストアップのビフォーアフター</h3>
  <div class="ba-list">
    <!-- index.html の gallery セクションの .ba-list 内 3 figure をそのままコピー -->
  </div>
  <p class="gallery-note">※掲載写真はご本人の同意を得て掲載しています。個人の感想であり、効果には個人差があります。施術効果を保証するものではありません。</p>
</div>

<div class="school-block">
  <p class="section-eyebrow">— Instagram</p>
  <h3 class="biz-subhead">日々の発信を Instagram で</h3>
  <div class="insta-grid">
    <!-- index.html の insta セクションの .insta-grid 内 3 a.insta-card をそのままコピー -->
  </div>
</div>
```
> `.ba-list` / `.insta-grid` 等のクラスは既存CSSで定義済（audit確認済）。実体は「index からコピー → 後続 Step で index から削除」で**移動**する（最終的に複製は残さない）。

- [ ] **Step 3: #school に「機器販売」を内包サブブロックとして統合**

`<section class="biz-detail biz-detail-alt" id="school">` 内、「卒業後もつながり続けます」ブロックの後（`資料請求` CTA付近）に、旧 Business 03 の内容を統合:
```html
<div class="school-block">
  <p class="section-eyebrow">— Equipment</p>
  <h3 class="biz-subhead">施術機器の販売・代理店</h3>
  <p class="biz-detail-body">
    サロンで実際に使用している専門機器を、卒業生や信頼できるサロン様へ。<br>
    導入のご相談・お取り扱いはお問い合わせフォームよりご連絡ください。
  </p>
  <a href="contact.html" class="hero-cta">機器導入を相談する →</a>
</div>
```

- [ ] **Step 4: 旧 Business 03（`<section class="biz-detail" id="equipment">…</section>`）を丸ごと削除**

`#equipment` セクションを削除（内容はStep3で#schoolへ内包済）。

- [ ] **Step 5: `— Business 0X` エイブロウ番号を2事業に整合**

#salon の `— Business 01`、#school の `— Business 02` は維持でOK。#equipment 由来の `— Business 03` は削除済。

- [ ] **Step 6: コピー完了を確認のうえ、index.html から #gallery / #insta を削除（移設の完了）**

Step2 で business.html に Before/After・Instagram を貼付できたことを確認したら、Task4で残しておいた index.html の `<section class="gallery" id="gallery">…</section>` と `<section class="insta" id="insta">…</section>` を**丸ごと削除**する。これで「コピー→削除」の移設が完了する（両ファイルを次の同一コミットに含める）。

- [ ] **Step 7: 検証**

Run:
```
grep -n "id=\"equipment\"\|Business 03\|3つの事業" client/bolon-shareee/business.html
```
Expected: **0件**。
```
grep -n "id=\"salon\"\|id=\"school\"\|ba-list\|insta-grid" client/bolon-shareee/business.html
```
Expected: salon/school 各1、ba-list/insta-grid 各1（移設済）。
```
grep -n "id=\"gallery\"\|id=\"insta\"" client/bolon-shareee/index.html
```
Expected: **0件**（index から撤去済）。
ブラウザで business.html を開き、#salon にBefore/After・IGが表示、#school に機器サブブロックがある、2事業のみ、崩れ無しを確認。index.html にBefore/After・IGが**無い**ことも再確認。

- [ ] **Step 8: コミット（business.html と index.html を同一コミットで）**

```
git add client/bolon-shareee/business.html client/bolon-shareee/index.html
git commit -m "feat(bolon): 事業を2本に再編(機器販売をスクール内包/BA・IGを#salonへ原子的に移設)"
```

---

## Task 6: company.html を2事業に更新

**Files:**
- Modify: `client/bolon-shareee/company.html`

- [ ] **Step 1: 基本情報テーブルの「事業内容」行を 3→2 へ**

`事業内容` の dd を:
```html
<dd>
  ① バストアップ専門サロンの運営（B.villea）<br>
  ② バストアップ起業スクールの運営（施術機器の販売・代理店を含む）
</dd>
```

- [ ] **Step 1b: company.html の HEADメタを2事業へ（「3事業／バスト機器代理店」を排除）**

`<head>` の `<meta name="description">`（L10付近）・`<meta property="og:description">`（L16付近）に残る「バスト機器代理店の3事業」を2事業に更新。例:
```html
<meta name="description" content="株式会社Bolon Shareeeの会社概要。バストアップ専門サロンB.villeaと、その技術を伝えるスクール事業（施術機器の販売を含む）の2事業を運営。福岡発、代表蒲池百都子。">
<meta property="og:description" content="バストアップ専門サロンB.villeaと、スクール事業（施術機器の販売を含む）の2事業を運営。福岡発、代表蒲池百都子。">
```
検証: `grep -n "機器代理店\|3事業" client/bolon-shareee/company.html` が0件（本文・head両方）。JSON-LD `name`/`@type` は不変。

- [ ] **Step 2: 「3つの事業について」→「2つの事業について」カードを 3→2 へ**

見出しを「2つの事業について」に。3枚のカードを2枚（サロン→`index.html`/`business.html#salon`、スクール→`business.html#school`）に。旧「機器代理店」カード（`business.html#equipment` や `contact.html` へのリンク）は削除し、スクールカードの説明に「施術機器の販売・代理店を含む」を追記。

- [ ] **Step 3: `#equipment` への内部リンクを `#school` へ付替**

Run: `grep -n "#equipment" client/bolon-shareee/company.html`
ヒットした `business.html#equipment` を `business.html#school` に置換。

- [ ] **Step 4: 検証**

Run:
```
grep -rn "#equipment\|3つの事業\|バスト機器 代理店" client/bolon-shareee/company.html
```
Expected: **0件**。ブラウザで company.html を開き、事業内容が2事業、カード2枚、リンク切れ無しを確認。

- [ ] **Step 5: コミット**

```
git add client/bolon-shareee/company.html
git commit -m "feat(bolon): 会社概要を2事業構成に更新(機器販売はスクール内包)"
```

---

## Task 7: contact.html のフォーム項目を2事業に整理

**Files:**
- Modify: `client/bolon-shareee/contact.html`

- [ ] **Step 1: 「ご相談内容」select を2事業前提に整理**

現状の option（サロン体験・料金・スクール・機器販売・業務委託・その他）を、2事業の枠組みで並べ替え・グルーピング（例）:
```html
<option value="salon-trial">サロン体験・ご予約について</option>
<option value="salon-price">サロン料金について</option>
<option value="school">スクール（開業・受講）について</option>
<option value="equipment">施術機器の販売・導入について</option>
<option value="partner">業務委託・提携について</option>
<option value="other">その他</option>
```
（値・文言は既存に合わせて微調整可。機器はスクール事業の一部だが、問い合わせ導線としては独立項目を残すと利便性が高い。）

- [ ] **Step 2: 検証**

Run: `grep -n "<option" client/bolon-shareee/contact.html`
Expected: 6項目、サロン/スクール/機器/業務委託/その他が揃う。ブラウザでフォーム表示・selectが機能することを確認。フォーム入力の `font-size:16px`（iOSズーム防止）が維持されていることをCSSで確認。

- [ ] **Step 3: コミット**

```
git add client/bolon-shareee/contact.html
git commit -m "feat(bolon): 問い合わせフォームの相談内容を2事業構成に整理"
```

---

## Task 8: 全体整合の最終検証（会社主役・移設・モバイル罠）

**Files:** なし（検証のみ。修正が出たら該当ファイルを直しコミット）

- [ ] **Step 1: ブランド統一の最終grep**

Run:
```
grep -rn "class=\"logo\">B.villea\|footer-logo\">B.villea" client/bolon-shareee/*.html
grep -rn "og:site_name" client/bolon-shareee/*.html
grep -rn "content=\"B.villea" client/bolon-shareee/*.html
```
Expected: 1つ目0件、2つ目は全て会社主役、3つ目0件。

- [ ] **Step 2: 移設の最終確認**

Run:
```
grep -rn "id=\"gallery\"\|id=\"insta\"" client/bolon-shareee/index.html
grep -rn "ba-list\|insta-grid" client/bolon-shareee/business.html
grep -rn "id=\"equipment\"\|3つの事業" client/bolon-shareee/*.html
```
Expected: index に gallery/insta 無し、business に ba-list/insta-grid 有り、equipment/「3つの事業」全ページ0件。

- [ ] **Step 3: JSON-LD健全性**

Run: `grep -rn "\"@type\"\|\"name\": \"株式会社Bolon Shareee\"\|B.villea（ビーヴィレア）" client/bolon-shareee/*.html`
Expected: Organization名は会社名、salonサブ実体名は `B.villea（ビーヴィレア）` で保持。壊れていないこと（各JSON-LDブロックの波括弧対応）を目視。

- [ ] **Step 4: モバイル罠の維持確認**

Run:
```
grep -n "100svh\|backdrop-filter: none\|font-size: 16px\|keep-all\|prefers-reduced-motion" client/bolon-shareee/css/style.css
```
Expected: 既存の該当規則が全て健在（追記で壊していない）。新規 `.hero-corporate` に `100svh` と `keep-all` があること。

- [ ] **Step 5: 全6ページ ブラウザ目視（PC + 375px）**

index / business / company / faq / contact / privacy を順に開き、①ヘッダー/フッターが会社主役 ②横スクロール無し ③880px以下で1カラム化 ④リンク切れ無し（特に `business.html#salon` `#school`、`company.html`）を確認。

- [ ] **Step 6: 差分レビュー用に superpowers:requesting-code-review を実行（任意・推奨）**

実装完了後、`git diff main...feat/bolon-corporate-pivot -- client/bolon-shareee/` を対象にコードレビューを依頼。

- [ ] **Step 7: 修正が出たらコミット**

```
git add client/bolon-shareee/...
git commit -m "fix(bolon): 最終検証で見つかった不整合を修正"
```

---

## Self-Review（スペック網羅チェック）

- 仕様書§3 サイト構成6ページ → Task1〜7 で全ページ着手。✓
- §4 TOP 9セクション → Task4 の Step1〜8 で全セクション実装。✓（ヒーロー/ミッション/2事業/代表/声/会社概要/CTA）
- §5 business 2事業・BA/IG移設・機器内包 → Task5。✓
- §6 company/faq/contact/privacy → company=Task6、contact=Task7、faq=Task1+2、privacy=Task1。✓
- §7 ブランド/SEO統一・JSON-LD不変 → Task1・2・8。✓
- §8 デザインシステム流用・新規CSS最小・モバイル罠 → Task3＋各Taskの検証・Task8 Step4。✓
- §9 コンプラ（個人差注記維持）→ Task4 Step6（声）・Task5 Step2（BA注記移設）。✓
- §12 完了条件6項目 → Task8 の各Stepで検証。✓

**プレースホルダ走査:** 「TBD/後で」等は無し。Task5 のコメント `<!-- index の … をそのまま移設 -->` は「既存マークアップを移動する」明示指示であり、移動元は index に実在するため実装可能（プレースホルダではない）。

**型/名称整合:** 使用クラスは全て audit で存在確認済（`hero-scroll` `section-eyebrow` `section-title` `company-summary` `business-list/item/num/link` `message*` `studio-grid(-solo)` `studio-info` `line-actions` `line-btn(-primary/secondary)` `ba-list` `insta-grid` `school-block` `biz-detail` `hero-cta` `business-cta`）。新規は `hero-corporate` 系＋`mission-body` のみ（Task3で定義）。id参照（`#mission` `#salon` `#school` `#company`）は生成側と一致。
