# マリンケア訪問看護ステーション サイト Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** マリンケア訪問看護ステーション（MARIN株式会社・顧客No.5）の本体5ページの静的サイトを `client/marin/` に新規構築する。

**Architecture:** 既存クライアント案件（`client/bolon-shareee`）と同じ静的多ページ構成。`css/reset.css` + `css/style.css`（CSS変数ベースのデザインシステム）、`js/main.js`（既存流用）、各HTMLにヘッダー/フッター直書き。水色グラデ背景＋白い角丸フレーム（B案「光の波打ち際」）。本物のコピーは移行元 https://marin-care.com/ から抽出済み。

**Tech Stack:** 素のHTML5 / CSS3（カスタムプロパティ・clamp・grid）/ Vanilla JS（IntersectionObserver）/ Google Fonts（Zen Maru Gothic, Zen Kaku Gothic Antique, Inter）/ JSON-LD構造化データ。ビルドツールなし。

**設計書:** `docs/superpowers/specs/2026-05-24-marin-care-site-design.md`

**検証方針:** ユニットテストの仕組みは無い。各ページは「ローカルサーバで開いて目視＋HTML/JSON-LD妥当性チェック＋モバイル幅確認」で検証する。ローカルサーバ：`python -m http.server 8000`（`d:/sharkstars` 直下で起動し `http://localhost:8000/client/marin/` を開く）。

---

## ファイル構成

| パス | 役割 |
|------|------|
| `client/marin/index.html` | トップ（10セクション） |
| `client/marin/service.html` | 訪問看護内容（看護＋リハビリ） |
| `client/marin/company.html` | 会社概要・理念 |
| `client/marin/contact.html` | お問い合わせ（採用受け口兼） |
| `client/marin/privacy.html` | プライバシーポリシー |
| `client/marin/css/reset.css` | リセットCSS（bolon-shareeeから流用） |
| `client/marin/css/style.css` | デザインシステム＋全ページスタイル |
| `client/marin/js/main.js` | ヘッダー挙動・モバイルメニュー・スクロール演出（bolon-shareeeから流用） |
| `client/marin/images/` | ロゴ・写真・動画・OGP・海の挿絵SVG |

共通方針（全HTML）：
- `<html lang="ja">`、`<meta name="robots" content="noindex, nofollow">`（プレビュー用・公開時削除のコメント付き）
- ヘッダー/フッターは各ページに直書き（同一マークアップをコピー）
- ナビ項目：トップ / 訪問看護内容 / 会社概要 / お問い合わせ（採用は「準備中」表示で問い合わせへ）

---

## Task 0: ディレクトリ作成と素材収集

**Files:**
- Create: `client/marin/css/`, `client/marin/js/`, `client/marin/images/`

- [ ] **Step 1: ディレクトリと流用ファイルを配置**

```bash
mkdir -p client/marin/css client/marin/js client/marin/images
cp client/bolon-shareee/css/reset.css client/marin/css/reset.css
cp client/bolon-shareee/js/main.js client/marin/js/main.js
```

- [ ] **Step 2: 移行元サイトからロゴと写真を取得**

移行元 https://marin-care.com/ の以下を `client/marin/images/` にダウンロードする（クライアント所有素材の流用）。取得できないものはサンプル（ストック）で代替し、ファイル名は本番想定で置く。

```bash
# ロゴ（白/通常）
curl -L -o client/marin/images/logo.svg        https://marin-care.com/wp-content/themes/marincare-wp/images/logo.svg
curl -L -o client/marin/images/logo_white.svg  https://marin-care.com/wp-content/themes/marincare-wp/images/logo_white.svg
# 写真（海イメージ・特徴・看護/リハ）
curl -L -o client/marin/images/sea.jpg     https://marin-care.com/wp-content/uploads/2025/05/marin_image_sea.jpg
curl -L -o client/marin/images/feature.jpg https://marin-care.com/wp-content/uploads/2025/05/feature.jpg
curl -L -o client/marin/images/vn.jpg      https://marin-care.com/wp-content/themes/marincare-wp/images/vn.jpg
curl -L -o client/marin/images/reha.jpg    https://marin-care.com/wp-content/themes/marincare-wp/images/reha.jpg
```

取得失敗時は `https://images.unsplash.com/` の海・看護・高齢者ケア系画像で代替し、ファイル名は上記のまま保存する。

- [ ] **Step 3: ヒーロー/ストーリー用サンプル動画を配置**

`client/marin/images/hero.mp4`（海の光・波）と `client/marin/images/story.mp4`（任意）をサンプル動画で配置。入手できない場合は Step 4 のヒーローを「写真＋CSSアニメ背景」にフォールバックする（実装は Task 3 で分岐）。サンプルはフリー素材（例：Coverr / Pexels Videos）を使用し、5MB以下に圧縮。

- [ ] **Step 4: 確認**

```bash
ls -la client/marin/images/
```
Expected: logo.svg / logo_white.svg / sea.jpg / feature.jpg / vn.jpg / reha.jpg（＋hero.mp4 があれば）が存在。

- [ ] **Step 5: Commit**

```bash
git add client/marin
git commit -m "chore(marin): scaffold dir, reuse reset.css/main.js, collect assets"
```

---

## Task 1: デザインシステム（style.css 基盤）

**Files:**
- Create: `client/marin/css/style.css`

水色グラデ背景＋白い角丸フレームの土台、CSS変数、タイポgrad見出し、ボタン、ヘッダー/フッター、レスポンシブ基盤、reveal演出、`prefers-reduced-motion`。

- [ ] **Step 1: CSS変数とベースを書く**

```css
/* マリンケア訪問看護ステーション — Design System (B: 光の波打ち際) */
:root{
  --bg-1:#eafaff; --bg-2:#d2f0fb; --bg-3:#bfe8f5;
  --card:#ffffff;
  --ink:#0a4d6e; --deep:#0a5a82; --accent:#34b3d1; --accent-2:#7fd0e0;
  --text:#3a5663; --muted:#6f8a98;
  --radius:22px; --radius-sm:14px;
  --maxw:1080px; --gut:clamp(16px,4vw,40px);
  --shadow:0 18px 40px rgba(10,77,110,.10);
  --grad-ink:linear-gradient(120deg,#0a5a82,#34b3d1);
  --ff-jp:'Zen Maru Gothic','Zen Kaku Gothic Antique',system-ui,sans-serif;
  --ff-en:'Inter',sans-serif;
}
body{
  font-family:var(--ff-jp);
  color:var(--text);
  background:linear-gradient(180deg,var(--bg-1),var(--bg-2) 40%,var(--bg-3));
  background-attachment:fixed;
  line-height:1.85;
}
.wrap{max-width:var(--maxw);margin-inline:auto;padding-inline:var(--gut)}
/* 白い角丸フレーム（コンテンツの基本コンテナ） */
.frame{background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow);padding:clamp(24px,5vw,56px)}
section{padding-block:clamp(40px,8vw,88px)}
.grad{background:var(--grad-ink);-webkit-background-clip:text;background-clip:text;color:transparent}
.label{font-family:var(--ff-en);font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);font-weight:600}
h2.title{font-size:clamp(24px,5.5vw,38px);font-weight:700;line-height:1.35;color:var(--deep);word-break:auto-phrase}
```

- [ ] **Step 2: ボタン・ヘッダー・フッターのスタイルを書く**

```css
/* Buttons */
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 26px;border-radius:999px;font-weight:700;font-size:15px}
.btn-primary{background:var(--grad-ink);color:#fff;box-shadow:0 8px 20px rgba(52,179,209,.35)}
.btn-line{background:#06C755;color:#fff}
.btn-ghost{background:#fff;color:var(--deep);border:1.5px solid #cfe6f0}

/* Header */
.header{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.85);backdrop-filter:saturate(140%) blur(8px);transition:box-shadow .3s}
.header.is-scrolled{box-shadow:0 4px 20px rgba(10,77,110,.08)}
.header .bar{display:flex;align-items:center;justify-content:space-between;height:64px}
.header .logo img{height:34px}
.nav ul{display:flex;gap:26px;align-items:center}
.nav a{font-size:14px;font-weight:500;color:var(--deep)}
.menu-toggle{display:none}

/* Footer */
.footer{background:var(--deep);color:#cdeffa;margin-top:40px}
.footer a{color:#cdeffa}
.footer .wrap{padding-block:40px}

/* Reveal */
.reveal{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s ease}
.reveal.is-in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){
  .reveal{opacity:1;transform:none;transition:none}
  html{scroll-behavior:auto}
}
```

- [ ] **Step 3: モバイル対応（メニュー・iOS罠回避）を書く**

```css
/* iOS入力ズーム防止：フォーム要素は16px以上 */
input,textarea,select{font-size:16px}

@media (max-width:860px){
  .menu-toggle{display:flex;flex-direction:column;gap:5px;width:44px;height:44px;align-items:center;justify-content:center}
  .menu-toggle span{width:24px;height:2px;background:var(--deep);transition:.3s}
  .nav{position:fixed;inset:64px 0 auto 0;background:#fff;transform:translateY(-120%);transition:transform .35s;box-shadow:0 12px 30px rgba(10,77,110,.12)}
  .nav.is-open{transform:translateY(0)}
  .nav ul{flex-direction:column;gap:0;padding:8px 0}
  .nav li{width:100%}
  .nav a{display:block;padding:16px var(--gut)}
}
```

- [ ] **Step 4: 検証**

`d:/sharkstars` で `python -m http.server 8000` を起動。Task 2/3 で実体ができるまではこのStepは「CSS構文エラーが無い」ことの確認に留める（ブラウザのコンソールにCSSパースエラーが出ない）。

- [ ] **Step 5: Commit**

```bash
git add client/marin/css/style.css
git commit -m "feat(marin): design system base (water-blue bg, white frame, header/footer)"
```

---

## Task 2: 共通ヘッダー/フッターのマークアップ（基準テンプレート）

**Files:**
- Reference markup（各ページにコピーして使う。本Taskでは確定版を定義するだけ）

- [ ] **Step 1: ヘッダーマークアップを確定**

全ページの `<body>` 先頭にこのマークアップを入れる（`aria-current` を現在ページに付ける）。

```html
<header class="header">
  <div class="wrap bar">
    <a class="logo" href="index.html" aria-label="マリンケア訪問看護ステーション">
      <img src="images/logo.svg" alt="マリンケア訪問看護ステーション" width="160" height="34">
    </a>
    <button class="menu-toggle" aria-label="メニュー" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav">
      <ul>
        <li><a href="index.html">トップ</a></li>
        <li><a href="service.html">訪問看護内容</a></li>
        <li><a href="company.html">会社概要</a></li>
        <li><a href="contact.html">お問い合わせ</a></li>
        <li><a class="btn btn-line" href="contact.html">LINEで相談</a></li>
      </ul>
    </nav>
  </div>
</header>
```

- [ ] **Step 2: フッターマークアップを確定**

```html
<footer class="footer">
  <div class="wrap">
    <p style="font-weight:700;font-size:18px;color:#fff">マリンケア訪問看護ステーション</p>
    <p>〒814-0134 福岡県福岡市城南区板倉1-5-35</p>
    <p>TEL <a href="tel:0924001821">092-400-1821</a> ／ FAX 092-400-1831</p>
    <p>Email <a href="mailto:marin.20220801@gmail.com">marin.20220801@gmail.com</a></p>
    <nav style="margin-top:16px;display:flex;gap:18px;flex-wrap:wrap">
      <a href="index.html">トップ</a><a href="service.html">訪問看護内容</a>
      <a href="company.html">会社概要</a><a href="contact.html">お問い合わせ</a>
      <a href="privacy.html">プライバシーポリシー</a>
    </nav>
    <p style="margin-top:20px;font-size:12px;color:#7fb6cf">© MARIN株式会社</p>
  </div>
</footer>
<script src="js/main.js"></script>
```

- [ ] **Step 3: SEO `<head>` の共通テンプレートを確定**

各ページの `<title>`/`description`/`canonical`/OGP を以下のひな型で作る（`<PAGE>` を置換）。

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow"><!-- プレビュー用：本番公開時に削除 -->
<title><!-- 各ページ固有 --></title>
<meta name="description" content="<!-- 各ページ固有 -->">
<meta name="keywords" content="訪問看護,訪問看護ステーション,福岡市城南区,24時間対応,リハビリ 訪問,マリンケア,MARIN株式会社">
<link rel="canonical" href="https://sharkstars.jp/client/marin/<PAGE>">
<meta property="og:type" content="website">
<meta property="og:site_name" content="マリンケア訪問看護ステーション">
<meta property="og:locale" content="ja_JP">
<meta property="og:url" content="https://sharkstars.jp/client/marin/<PAGE>">
<meta property="og:title" content="<!-- 各ページ固有 -->">
<meta property="og:description" content="<!-- 各ページ固有 -->">
<meta property="og:image" content="https://sharkstars.jp/client/marin/images/ogp.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://sharkstars.jp/client/marin/images/ogp.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Zen+Kaku+Gothic+Antique:wght@400;500;700&family=Zen+Maru+Gothic:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/style.css">
```

（このTaskはコミット不要。Task 3以降で実体化する。）

---

## Task 3: index.html（トップ）

**Files:**
- Create: `client/marin/index.html`
- Modify: `client/marin/css/style.css`（トップ固有セクションのスタイル追記）

- [ ] **Step 1: ページ骨格＋head＋ヘッダー/フッターを作る**

Task 2 の head テンプレを使用。固有値：
- `<title>`：`マリンケア訪問看護ステーション｜福岡市城南区の訪問看護・リハビリ`
- description：`福岡市城南区の訪問看護ステーション マリンケア。24時間365日対応、看護師とリハビリ職が連携し、小児から高齢者まで「その人らしい生き方」を支えます。`
- canonical/og:url：`https://sharkstars.jp/client/marin/`
JSON-LD は Task 8 で追加。

- [ ] **Step 2: セクション01–05のマークアップを作る**

実コピー（移行元から抽出）を使用：
- **01 ヒーロー**：動画背景 `<video autoplay muted loop playsinline poster="images/sea.jpg"><source src="images/hero.mp4" type="video/mp4"></video>`。見出し「いのちのそばに。」サブ「あなたの物語を大切に。その〝人〟らしく生きるを看る。」CTA：`お問い合わせ`(btn-primary)＋`LINEで相談`(btn-line)。動画が無い場合は `<video>` を省き `.hero{background-image:url(images/sea.jpg)}` にする。
- **02 写真ストリップ**：`sea.jpg / vn.jpg / reha.jpg` を3枚横並び（grid）。
- **03 理念**：白フレーム内に理念テキスト「人生という物語の主人公であるあなたが…希望ある選択肢をご提供いたします。」＋「人生の先輩方への恩返し、次の世代への恩送り。マリンケアの揺るぎない想いです。」
- **04 3つの導線カード**：`利用者・ご家族へ`→`service.html`／`採用情報`→`contact.html`（バッジ「準備中」）／`連携先の皆さまへ`→`company.html`。各 `.reveal`。
- **05 強み3つ**：`24時間365日対応` / `看護師＋リハビリ職の連携` / `小児から高齢者まで対応` をアイコン（インラインSVG）＋3カラム。

- [ ] **Step 3: セクション06–10＋海の挿絵を作る**

- **06 ストーリー動画**：`<video controls poster=...>` または `sea.jpg` 静止画＋コピー。
- **07 写真ギャラリー**：`feature.jpg / vn.jpg / reha.jpg / sea.jpg` をタイルgrid。
- **08 声**：コメントカード3枚（※仮テキスト。`<!-- TODO: 公開前に実コメントへ差替え -->` を明記）。例「住み慣れた家で過ごせて本当に安心しています。」（ご家族）等。
- **09 採用CTA**：濃紺グラデ帯。「一緒に働きませんか？」「正看護師（パート・アルバイト）／未経験歓迎／同行訪問・無料見学体験あり」CTA→`contact.html`、注記「採用専用ページは準備中です」。
- **10 事業所情報＋問い合わせ**：住所・TEL・FAX・対応エリア（福岡市城南区）＋Googleマップ `<iframe>`（住所クエリ）＋`contact.html` への導線。
- 海の挿絵：泡・魚・波の軽量インラインSVGを背景アクセントとして数か所に（`aria-hidden="true"`、控えめ）。

- [ ] **Step 4: トップ固有スタイルを style.css に追記**

ヒーロー（動画フルブリード・オーバーレイ・グラデ見出し）、写真ストリップgrid、3導線カード、強み3カラム、ギャラリーtile、声カード、採用CTA帯。モバイルで1カラムに落とす。

- [ ] **Step 5: 検証**

`python -m http.server 8000` → `http://localhost:8000/client/marin/` を開く。確認：
- 10セクションが上から順に表示／水色背景＋白フレーム
- スクロールでreveal発火、ヘッダーが `is-scrolled` に
- 360px幅（DevToolsモバイル）でレイアウト崩れ無し・横スクロール無し
- 動画が再生 or poster表示

- [ ] **Step 6: Commit**

```bash
git add client/marin/index.html client/marin/css/style.css
git commit -m "feat(marin): build top page (10 sections, video hero, real copy)"
```

---

## Task 4: service.html（訪問看護内容）

**Files:**
- Create: `client/marin/service.html`
- Modify: `client/marin/css/style.css`

- [ ] **Step 1: head＋ヘッダー/フッター**

- title：`訪問看護内容｜マリンケア訪問看護ステーション（福岡市城南区）`
- description：`マリンケアの訪問看護・リハビリの内容。医療行為、健康観察、服薬管理、小児看護、ターミナルケア、運動機能回復や福祉用具調整まで。福岡市城南区対応。`
- canonical：`https://sharkstars.jp/client/marin/service.html`、ナビ `service.html` に `aria-current="page"`

- [ ] **Step 2: 本文セクションを作る（実コピー）**

- イントロ（利用者・家族向けやさしいトーン）
- **訪問看護**カード一覧：医師の指示による医療行為／健康状態の観察・バイタルチェック／服薬管理・栄養指導／排便コントロール／小児看護／点滴・注射指示対応／疼痛緩和／ターミナルケア（末期の悪性腫瘍）
- **リハビリ**カード一覧：運動機能の回復・維持／ADL（日常動作）／廃用症候群の予防／難病の進行予防／呼吸器リハビリ／心臓リハビリ／高次脳機能障害／環境（福祉用具）調整
- 利用の流れ（お問い合わせ→ご相談・面談→契約→訪問開始）を4ステップで
- ページ末CTA：`お問い合わせ`／`LINEで相談`

- [ ] **Step 3: スタイル追記（必要なら）＋検証**

サービスカードgrid・流れステップ。`http://localhost:8000/client/marin/service.html` を開き、看護8項目・リハ6項目以上が表示、モバイルで1カラム、横スクロール無しを確認。

- [ ] **Step 4: Commit**

```bash
git add client/marin/service.html client/marin/css/style.css
git commit -m "feat(marin): service page (nursing + rehab content)"
```

---

## Task 5: company.html（会社概要）

**Files:**
- Create: `client/marin/company.html`
- Modify: `client/marin/css/style.css`

- [ ] **Step 1: head＋ヘッダー/フッター**

- title：`会社概要｜マリンケア訪問看護ステーション・MARIN株式会社`
- description：`MARIN株式会社が運営するマリンケア訪問看護ステーション。代表 西隆之介。福岡市城南区を中心に24時間365日、看護とリハビリの連携で地域を支えます。`
- canonical：`https://sharkstars.jp/client/marin/company.html`

- [ ] **Step 2: 本文（実コピー）**

- 理念ブロック（恩返し・恩送りメッセージ含む）
- **会社情報テーブル**：会社名＝MARIN株式会社／屋号＝マリンケア訪問看護ステーション／代表取締役＝西 隆之介／所在地＝〒814-0134 福岡県福岡市城南区板倉1-5-35／TEL 092-400-1821／FAX 092-400-1831／Email marin.20220801@gmail.com／対応エリア＝福岡市城南区（中心）／営業＝24時間365日 緊急対応
  - `<!-- 公開前確認：住所は契約書=板倉。移行元サイト=飯倉。西社長にLINEで正式表記を確認のこと -->`
- 体制（看護師＋リハ職の連携／多職種連携）— 連携先向け安心材料
- アクセス（Googleマップ iframe）

- [ ] **Step 3: スタイル＋検証**

定義リスト/テーブルのスタイル。`company.html` を開き情報テーブル・理念・地図表示、モバイル確認。

- [ ] **Step 4: Commit**

```bash
git add client/marin/company.html client/marin/css/style.css
git commit -m "feat(marin): company page (philosophy, company info, access)"
```

---

## Task 6: contact.html（お問い合わせ）

**Files:**
- Create: `client/marin/contact.html`
- Modify: `client/marin/css/style.css`

- [ ] **Step 1: head＋ヘッダー/フッター**

- title：`お問い合わせ｜マリンケア訪問看護ステーション（福岡市城南区）`
- description：`マリンケア訪問看護ステーションへのお問い合わせ・採用のご相談。お電話・LINE・メールで承ります。福岡市城南区。`
- canonical：`https://sharkstars.jp/client/marin/contact.html`

- [ ] **Step 2: 本文**

- 連絡手段カード3つ：TEL `tel:0924001821`（大きくタップしやすく）／LINE（`btn-line`、LINE URLは仮 `#` ＋ `<!-- TODO: 公式LINE URL -->`）／メール `mailto:marin.20220801@gmail.com`
- 問い合わせ種別の案内文に「**採用に関するお問い合わせも承ります**（採用専用ページは準備中）」を明記
- 受付時間・対応エリア・Googleマップ
- （サーバ送信フォームは作らない＝YAGNI）

- [ ] **Step 3: スタイル＋検証**

連絡カード。`tel:`/`mailto:` リンクが正しく機能（hrefを確認）。モバイルでタップ領域44px以上。

- [ ] **Step 4: Commit**

```bash
git add client/marin/contact.html client/marin/css/style.css
git commit -m "feat(marin): contact page (tel/LINE/mail, recruit intake)"
```

---

## Task 7: privacy.html（プライバシーポリシー）

**Files:**
- Create: `client/marin/privacy.html`

- [ ] **Step 1: head＋ヘッダー/フッター**

- title：`プライバシーポリシー｜マリンケア訪問看護ステーション`
- description：`マリンケア訪問看護ステーションの個人情報保護方針。`
- canonical：`https://sharkstars.jp/client/marin/privacy.html`

- [ ] **Step 2: 本文（医療・個人情報配慮）**

白フレーム内に条項：1) 事業者情報（MARIN株式会社）2) 取得する個人情報 3) 利用目的（訪問看護サービス提供・医療連携）4) **医療情報・要配慮個人情報の取り扱い**（個人情報保護法に基づき適正に管理）5) 第三者提供（主治医・連携医療機関等への必要な範囲での提供と同意）6) 安全管理措置 7) 開示・訂正・利用停止の請求 8) お問い合わせ窓口（TEL/Email）。`muku`/`bolon-shareee` の privacy.html を文体の参考にする。

- [ ] **Step 3: 検証＋Commit**

`privacy.html` 表示確認。
```bash
git add client/marin/privacy.html
git commit -m "feat(marin): privacy policy (healthcare/PII considerations)"
```

---

## Task 8: SEO仕上げ・JSON-LD・OGP・sitemap

**Files:**
- Modify: 全5ページ（JSON-LD追加）
- Create: `client/marin/images/ogp.png`
- Modify: `sitemap.xml`

- [ ] **Step 1: トップに `@graph` JSON-LD を追加**

`index.html` の `<head>` に追加：

```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"MedicalBusiness",
      "@id":"https://sharkstars.jp/client/marin/#org",
      "name":"マリンケア訪問看護ステーション",
      "url":"https://sharkstars.jp/client/marin/",
      "logo":"https://sharkstars.jp/client/marin/images/logo.svg",
      "image":"https://sharkstars.jp/client/marin/images/ogp.png",
      "telephone":"+81-92-400-1821",
      "faxNumber":"092-400-1831",
      "email":"marin.20220801@gmail.com",
      "priceRange":"保険適用",
      "medicalSpecialty":["Nursing","Physiotherapy","HomeHealth"],
      "openingHours":"Mo-Su 00:00-23:59",
      "address":{"@type":"PostalAddress","streetAddress":"板倉1-5-35","addressLocality":"福岡市城南区","addressRegion":"福岡県","postalCode":"814-0134","addressCountry":"JP"},
      "areaServed":{"@type":"AdministrativeArea","name":"福岡市城南区"},
      "parentOrganization":{"@type":"Organization","name":"MARIN株式会社","founder":{"@type":"Person","name":"西 隆之介"}}
    },
    {
      "@type":"WebSite",
      "@id":"https://sharkstars.jp/client/marin/#website",
      "url":"https://sharkstars.jp/client/marin/",
      "name":"マリンケア訪問看護ステーション",
      "publisher":{"@id":"https://sharkstars.jp/client/marin/#org"}
    }
  ]
}
</script>
```

下層4ページには `MedicalBusiness`（`@id` 参照）＋ `WebPage` の軽量JSON-LDを入れる。`streetAddress` は公開前の住所確認結果に合わせる（板倉/飯倉）。

- [ ] **Step 2: OGP画像を作成**

`client/marin/images/ogp.png`（1200×630）。水色グラデ背景＋ロゴ＋「いのちのそばに。／マリンケア訪問看護ステーション」。`bolon-shareee/images/ogp.png` の作り方を踏襲（HTML→スクショ、または既存手順）。

- [ ] **Step 3: sitemap.xml に追加**

`d:/sharkstars/sitemap.xml` に `https://sharkstars.jp/client/marin/` 配下5URLを追加（`bolon-shareee` のエントリ形式に合わせる）。

- [ ] **Step 4: 検証**

- 各ページのJSON-LDを https://validator.schema.org/ 相当で妥当性確認（または `node -e` でJSON.parse通過を確認）。
- 全ページ canonical / og:url がページ実体と一致。

```bash
node -e "const fs=require('fs');['index','service','company','contact','privacy'].forEach(p=>{const h=fs.readFileSync('client/marin/'+p+'.html','utf8');const m=[...h.matchAll(/<script type=\"application\/ld\+json\">([\s\S]*?)<\/script>/g)];m.forEach(x=>JSON.parse(x[1]));console.log(p,'JSON-LD OK',m.length)})"
```
Expected: 各ページ `JSON-LD OK` と件数が表示、例外なし。

- [ ] **Step 5: Commit**

```bash
git add client/marin sitemap.xml
git commit -m "feat(marin): JSON-LD (MedicalBusiness), OGP image, sitemap entries"
```

---

## Task 9: 最終QA（レスポンシブ・アクセシビリティ・整合）

**Files:**
- Modify: 必要に応じて全ページ／style.css

- [ ] **Step 1: レスポンシブQA**

DevToolsで 360 / 390 / 768 / 1024 / 1280px を確認。チェック：横スクロール無し／日本語大型見出しの不自然な折返し無し（`word-break:auto-phrase`）／タップ領域44px以上／画像が枠に収まる。

- [ ] **Step 2: アクセシビリティ/挙動QA**

全画像に `alt`／ヘッダーナビが現在ページに `aria-current`／`menu-toggle` の `aria-expanded` がトグル／`prefers-reduced-motion` で演出停止／キーボードでナビ操作可。

- [ ] **Step 3: リンク整合チェック**

全ページのヘッダー/フッターリンクが5ページ間で正しく相互リンク。採用導線が全て `contact.html`（または準備中表示）に向く。`tel:`/`mailto:` 正常。

```bash
node -e "const fs=require('fs');['index','service','company','contact','privacy'].forEach(p=>{const h=fs.readFileSync('client/marin/'+p+'.html','utf8');['index.html','service.html','company.html','contact.html','privacy.html'].forEach(l=>{if(!h.includes(l))console.log('WARN',p,'missing link',l)})});console.log('link check done')"
```
Expected: `link check done`（WARNが出たら該当リンクを補う）

- [ ] **Step 4: 設計書の公開前チェックリストを README/コミットに反映**

`client/marin/` の状態が設計書「8. 公開前チェック」の未完了項目（noindex削除・本番素材差替え・声の差替え・**住所確認**）と一致していることを確認し、未了項目はコード内コメント `<!-- TODO -->` で残す。

- [ ] **Step 5: 最終Commit**

```bash
git add client/marin client/marin/css/style.css
git commit -m "fix(marin): final responsive/a11y/link QA pass"
```

---

## 完了の定義（Definition of Done）

- `client/marin/` に5ページ＋css/js/imagesが揃い、ローカルサーバで全ページ表示できる
- 水色背景＋白フレームのB案デザイン、動画ヒーロー、グラデ見出しが反映
- 実コピー（移行元抽出）が各ページに入っている
- 全ページ noindex（プレビュー）／SEO・OGP・JSON-LD完備／sitemap追加
- モバイルで崩れ・横スクロール無し
- 公開前TODO（住所確認・noindex削除・本番素材差替え・声差替え・LINE URL）がコメントで明示されている
