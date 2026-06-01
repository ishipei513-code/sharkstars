# Re-JALO 専用LP（Wix完全再現・Muku統一デザイン）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 外部Wix（usakuma15.wixsite.com/muku）のRe-JALO医療痩身LPを、構成・文言そのままに `client/muku/re-jalo/index.html` として自社内に再現し、デザインをMukuサイト（白×ワインレッド、Cormorant + Noto Serif）に統一する。

**Architecture:** 単一HTMLページ。既存 `client/muku/css/style.css` を相対パスで流用し、LP固有スタイルはページ内 `<style>` に追記。Wixから取得済みの実画像14枚を `re-jalo/images/` に配置。全CTAは新LINE `https://lin.ee/yALwLE6`。Wix原文の「院内調合」2か所は「医師監修」に変更（ユーザー指示・薬機法配慮）。

**Tech Stack:** 静的HTML5 / CSS3（既存style.css流用）/ JS（既存 `../js/main.js` のreveal・menu-toggle流用）。ビルドツールなし。ブラウザ目視確認。

---

## 前提情報（実装者向け・必読）

### このLPは静的サイトの一部
- ビルド不要。`client/muku/` 配下は手書きHTML＋共通CSS。
- 他ページ（index.html, service.html, contact.html 等）と同じ構造・同じ `style.css` を使う。
- テストフレームワークは無い。検証は「ブラウザで開いて目視」＋「壊れリンク・壊れ画像が無いことの確認」。

### 既存CSSの利用可能クラス（`client/muku/css/style.css`）
そのまま使えるクラス：
`.header .container .logo .nav .nav-cta .menu-toggle`（ヘッダー）/
`.hero .hero-bg .hero-slide .hero-overlay .hero-inner .hero-text .hero-eyebrow .hero-title .hero-sub .hero-scroll .hero-vertical`（ヒーロー）/
`.section .section-tone .section-dark .section-head .section-eyebrow .section-title .section-desc .section-number`（セクション枠）/
`.container .container-narrow`（幅）/
`.intro-grid .intro-visual .intro-visual-frame .intro-text`（画像＋テキスト2カラム）/
`.products .products-2col .product-card .product-num .product-name .product-name-en .product-desc .product-tags .product-tag`（カード）/
`.def-table`（定義テーブル）/ `.price .price-head .price-block .price-block-label .price-list .price-name .price-amount .price-note`（料金表）/
`.notice .notice-head .notice-label .notice-title .notice-items .notice-num`（注意事項）/
`.cta-banner .cta-banner-inner`（CTAバナー）/
`.line-block .line-block-eyebrow .line-block-title .line-block-desc .line-block-id .line-block-note`（LINEブロック・contact.html参照）/
`.btn .btn-primary .btn-outline .btn-line .btn-arrow`（ボタン）/
`.reveal .reveal-delay-1 .reveal-delay-2 .reveal-delay-3`（スクロール表示）/
`.footer .footer-grid .footer-brand .footer-col .footer-bottom`（フッター）/
`.page-hero .page-hero-eyebrow .page-hero-title .breadcrumb`（下層ヒーロー）

### 利用可能なCSS変数（`:root`）
カラー: `--pink-50..700`（シャンパン〜ゴールド系。--pink-500=#b08a2c がシグネチャーゴールド）/
`--wine-500: #8b6c1c` `--wine-700: #4d3c12`（ワイン＝ダークゴールド）/
`--cream-50..200` / `--ink-50..900`（本文〜濃墨）/ `--white`。
フォント: `--font-display`（Noto Serif JP）/ `--font-body`（Noto Sans JP）/ `--font-latin`（Cormorant Garamond）。
**注意:** このサイトの「ワインレッド」は実際にはゴールド/ワイン系（#8b6c1c）。仕様書の「白×ワインレッド」はこの既存パレットを指す。新しい色は足さず、必ず既存変数を使う。

### CTAリンク（全箇所統一）
`https://lin.ee/yALwLE6`（target="_blank" rel="noopener"）

### パス（re-jalo/index.html からの相対）
- CSS: `../css/reset.css` `../css/style.css`
- 共通JS: `../js/main.js`
- ロゴ: `../images/mukulogo.avif`
- LP画像: `images/<name>`

---

## Wix原文（VERBATIM・この文言を一字一句使う）

実装中はこのブロックの文言をそのままコピーする。**「院内調合」は2か所とも「医師監修」に置換**（★印）。

**ヒーロー:**
- メイン見出し: 「細胞を磨き上げる　新しい医療痩身のかたち」
- サブ: 「再生医療の研究拠点から生まれた、医師管理下の次世代GIP/GLP-1プログラム」

**クリニック紹介:**
- eyebrow: 「再生医療の最前線から。」
- 見出し: 「リジュヴェールクリニック」
- 引用: 「「細胞が持つ"再生の力"を人へ、未来へ、世界へ」」
- 本文: 「リジュヴェールクリニックは リジュヴェールクリニック川崎院（準備中）での再生医療研究を背景に持つ、次世代の医療クリニックです。」

**2拠点:**
- 川崎院: 「リジュヴェールクリニック川崎院（準備中）は 第2種・第3種 再生医療クリニック 〜新しい再生医療技術研究を兼ねた専門クリニック〜 CPC施設(細胞培養施設)・自律型自動培養装置導入を視野に入れた直営クリニックとして開設予定。 ※民間初の第1種再生医療クリニックを目指す」
- 梅田院: 「梅田院では 再生医療×美容×ウェルネスケアを融合したトータルビューティーサロンとして、「理想の美」と「本来の健康」を医学的根拠に基づく施術と高度な専門技術により包括的にサポートしています。」

**理念:**
- 見出し: 「「量」を追う時代は終わりました。これからは「質」の時代です。」
- 本文: 「過度な制限、激しい消耗。それはもう、あなたのライフスタイルには似合いません。 私たちが目指すのは、単なる体重の減少ではなく、細胞レベルでの「Rejuvenation（若返り）」。 最新の医学的知見に基づき、食欲と代謝のメカニズムを最適化する。 それは、宝石の原石を磨くように、あなた本来の美しさと健康を呼び覚ますプロセスです。」

**プログラム:**
- eyebrow: 「リジュヴェールクリニックがお届けする、医療痩身プログラム。」
- 見出し: 「リージャロ」
- 本文: 「「痩せる」ことだけを目的にするのではなく、身体の仕組みに向き合い、安全性を重視した体重管理を行う医療痩身プログラムです。 GLP-1／GIP受容体作動薬を用いた医師監修・当院独自の処方により、食欲や代謝に関わる身体の働きに医学的にアプローチし、無理のない体重管理を目指します。」
- お悩み見出し: 「このようなお悩みがある方へ」
- お悩み4項目: 「食事量を抑えたいが、なかなか続かない」「運動が苦手、または時間が取れない」「これまでのダイエットが長続きしなかった」「自己流ではなく、医師に相談しながら体重管理をしたい」

**サイエンス:**
- 見出し: 「世界が注目する「ダブル受容体作動」の力。」
- 本文: 「GLP-1に加え、GIPという第2のホルモンに作用する「チルゼパチド」成分を基軸に採用。従来のGLP-1単独療法を超え、血糖コントロールと脂肪燃焼を強力にサポートします。」
- 重要事項見出し: 「処方に関する重要事項」
- 重要事項本文★: 「★医師監修により濃度や配合を調整し、一般的なGLP-1製剤と比較して副作用の発現を抑えることを目指した構成としていますが、全ての副作用が無くなるわけではありません。 ※吐き気、胃のむかつき等が起こる場合があります。医師が適切に経過を観察します。」
  （★ Wix原文「院内調合により濃度や配合を調整し」→「医師監修により濃度や配合を調整し」に変更）

**ニードルフリー:**
- 見出し: 「「刺さない」という、新しい選択。」
- eyebrow: 「ニードルフリー・システム」
- 本文: 「効果は欲しいが、痛みは伴いたくない。そんな願いに応える「無針注射器」を採用しています。高圧ジェット技術により、瞬時に、そして痛みを感じにくく薬剤を浸透させます。週に1回、ご自宅でのケアを快適に続けていただけます。」
- 3ポイント: 「週1回、自宅で自己投与」「投与説明は初回にオンラインまたは院内で実施」「厳重な温度管理下のクール便でお届け」
- キャプション: 「使用方法動画」（→ 動画は無いので「使用方法」見出し＋写真3枚で代替）

**安心の3本柱:**
- 見出し: 「医師監修の安全管理体制。」
- 本文: 「Re-JALOは、サロンや非医療従事者が扱うものではありません。再生医療研究を背景に持つ医療機関として、厳格な適応判断と安全管理を行います。」
- 柱1: 「完全医師対応」「処方・経過観察は必ず医師が行います。オンライン診察にも対応。」
- 柱2: 「厳格な適応判断」「BMIや既往歴を精査し、医学的妥当性を重視した処方を行います。」
- 柱3★: 「徹底した品質管理」「★医師監修のオリジナル処方。厳重な温度管理下のクール便でお届けします。」
  （★ Wix原文「院内調合のオリジナル処方。」→「医師監修のオリジナル処方。」に変更）

**料金プラン:**
- 見出し: 「料金プラン」 / ラベル「税別表示」
- 初回セット料金:
  - 「無針注射器（Comfort-in）」 25,000円（注記「定価110,880円から特別割引」）
  - 「皮下注射薬（5.0mg×4本／1か月分）」 20,000円
- 2回目以降:
  - 「皮下注射薬（5.0mg×4本／1か月分）」 30,000円
- 注記: 「※表示価格は税別です　※初診料として別途3,000円（税込み3,300円）がかかります」

**注意事項:**
- 見出し: 「治療にあたっての大切なご案内」
- 項目: 「本治療は自由診療であり、保険適応外となります。」「効果や経過には個人差があります。」「副作用（吐き気、胃もたれ等）が生じる可能性があります。」「重大な副作用（稀）：急性膵炎、脱水、腎機能低下、胆のう疾患」「自己判断での増量、中止、または他者への譲渡は禁止です。」「患者様ごとのオーダーメイド処方という特性上、決済完了後はいかなる理由でも返金はできません。予めご了承ください。」
- 禁忌見出し: 「【禁忌】以下に該当する場合、本治療は行えません」
- 禁忌本文: 「BMI18.5未満 / 妊娠中・授乳中・妊娠希望 / 膵炎の既往 / 甲状腺髄様癌の既往または家族歴 / 重度の腎疾患・心疾患・重度高血圧 / 消化器疾患の重い方 / 主治医により制限されている場合 / 18歳未満」

**ビジョン:**
- 「人生を再起動させる医療」「輝きに満ちた、新しい自分へ。」

**最終CTA:**
- 「まずはお気軽にご相談ください。」「医師によるオンラインカウンセリングをご用意しております。」
- ボタン: 「カウンセリングを予約する」（→ 新LINE）
- 「完全予約制」「リジュヴェールクリニック梅田院」「大阪府大阪市北区曽根崎新地1-7-30」（電話 06-7777-6201 は service.html より補完）

---

## File Structure

- Create: `client/muku/re-jalo/index.html` — LP本体（単一ページ、全14セクション＋ページ内`<style>`）
- Create: `client/muku/re-jalo/images/*` — Wix取得画像14枚（リネーム後）。※ダウンロード済みの暫定名 `wix_1..14_*` をTask 1でリネーム
- Modify: `client/muku/service.html:203` — Re-JALOボタンのhrefを外部Wix→内部 `re-jalo/` に張替

---

## Task 1: 画像の整理（用途別リネーム）

**Files:**
- Modify (rename): `client/muku/re-jalo/images/wix_*.{jpg,png,webp}`

ダウンロード済みの14枚（暫定名 `wix_N_995824_<hash>.<ext>`）を、用途が分かる名前へリネームする。

- [ ] **Step 1: 現状の画像ファイルを確認**

Run:
```bash
ls -1 client/muku/re-jalo/images/
```
Expected: `wix_1_995824_...jpg` 〜 `wix_14_995824_...jpg` の14ファイルが存在。

- [ ] **Step 2: 用途別にリネーム**

以下のマッピングでリネームする（Bashツールで実行）:

```bash
cd client/muku/re-jalo/images
mv wix_6_995824_*.png        hero-rejuvenation.png      # 金箔バナー（背景装飾）
mv wix_2_995824_*.webp       science-gipglp1.webp       # GIP/GLP-1 金色細胞
mv wix_10_995824_*.png       science-mechanism.png      # 痩身メカニズム人体図
mv wix_4_995824_*.webp       decor-cells.webp           # 細胞バブル装飾
mv wix_12_995824_*.webp      decor-organelle.webp       # オルガネラ装飾
mv wix_1_995824_*.jpg        device-kit.jpg             # キット内容
mv wix_3_995824_*.jpg        device-assemble.jpg        # 組立
mv wix_5_995824_*.jpg        device-inject.jpg          # 噴射
mv wix_9_995824_*.jpg        device-box.jpg             # 製品箱
mv wix_13_995824_*.png       device-starterpack.png     # スターターパック
mv wix_14_995824_*.jpg       device-logo.jpg            # Comfort-inロゴ
mv wix_7_995824_*.webp       counseling.webp            # 医師カウンセリング
mv wix_11_995824_*.jpg       vision-mirror.jpg          # 鏡の女性
mv wix_8_995824_*.png        price-original.png         # 料金表（参考・未使用）
ls -1
```
Expected: 上記14個の新ファイル名が並ぶ。

- [ ] **Step 3: コミット**

```bash
git add client/muku/re-jalo/images
git commit -m "feat(muku): add Re-JALO LP images fetched from Wix source"
```

---

## Task 2: HTMLスケルトン（head・ヘッダー・フッター・読込）

**Files:**
- Create: `client/muku/re-jalo/index.html`

まずページの骨格（DOCTYPE・head・meta・CSS読込・最小ヘッダー・フッター・JS読込）を作る。中身のセクションはTask 3以降で `<!-- SECTIONS -->` の位置に追加する。

- [ ] **Step 1: index.html を作成（骨格のみ）**

`client/muku/re-jalo/index.html` を新規作成：

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO -->
  <title>リージャロ（Re-JALO）｜医師管理下の医療痩身プログラム — Muku株式会社</title>
  <meta name="description" content="リージャロ（Re-JALO）は、再生医療の研究拠点リジュヴェールクリニックがお届けする医師管理下の医療痩身プログラム。GLP-1／GIP受容体作動薬（チルゼパチド）と無針注射器による、痛みを抑えた次世代の体重管理。">
  <meta name="keywords" content="リージャロ,Re-JALO,医療痩身,GLP-1,GIP,チルゼパチド,無針注射器,Comfort-in,リジュヴェールクリニック,Muku株式会社">
  <link rel="canonical" href="https://sharkstars.jp/client/muku/re-jalo/">

  <!-- OGP -->
  <meta property="og:title" content="リージャロ（Re-JALO）｜医師管理下の医療痩身プログラム">
  <meta property="og:description" content="再生医療の研究拠点から生まれた、医師管理下の次世代GIP/GLP-1プログラム。">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sharkstars.jp/client/muku/re-jalo/">
  <meta property="og:site_name" content="Muku株式会社">
  <meta property="og:locale" content="ja_JP">
  <meta property="og:image" content="https://sharkstars.jp/client/muku/images/ogp.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="リージャロ（Re-JALO）｜医師管理下の医療痩身プログラム">
  <meta name="twitter:description" content="再生医療の研究拠点から生まれた、医師管理下の次世代GIP/GLP-1プログラム。">
  <meta name="twitter:image" content="https://sharkstars.jp/client/muku/images/ogp.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@300;400;500;600&display=swap" rel="stylesheet">

  <!-- Styles -->
  <link rel="stylesheet" href="../css/reset.css">
  <link rel="stylesheet" href="../css/style.css">

  <!-- Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "リージャロ（Re-JALO）",
    "serviceType": "医療痩身プログラム",
    "description": "GLP-1／GIP受容体作動薬（チルゼパチド）を用いた医師管理下の医療痩身プログラム。無針注射器による在宅自己投与に対応。",
    "provider": {
      "@type": "MedicalBusiness",
      "name": "リジュヴェールクリニック梅田院",
      "address": {
        "@type": "PostalAddress",
        "addressRegion": "大阪府",
        "addressLocality": "大阪市北区",
        "streetAddress": "曽根崎新地1-7-30"
      },
      "telephone": "+81-6-7777-6201"
    },
    "areaServed": ["大阪府"],
    "url": "https://sharkstars.jp/client/muku/re-jalo/"
  }
  </script>

  <style>
  /* ==== Re-JALO LP 固有スタイル（Task 5で追記） ==== */
  </style>
</head>
<body>

<!-- ===== HEADER（最小） ===== -->
<header class="header" id="header">
  <div class="container">
    <a href="../index.html" class="logo"><img src="../images/mukulogo.avif" alt="">Muku</a>
    <a href="https://lin.ee/yALwLE6" target="_blank" rel="noopener" class="nav-cta">ご予約・ご相談</a>
  </div>
</header>

<!-- SECTIONS -->

<!-- ===== FOOTER ===== -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="../index.html" class="logo"><img src="../images/mukulogo.avif" alt="">Muku</a>
        <p>
          再生医療×次世代の技術で、<br>
          内側からの若返りと健康改善を提供する<br>
          美容医療ブランドです。
        </p>
      </div>
      <div class="footer-col">
        <h4>Sitemap</h4>
        <ul>
          <li><a href="../index.html">トップ</a></li>
          <li><a href="../service.html">取扱商品</a></li>
          <li><a href="../about.html">会社情報</a></li>
          <li><a href="../faq.html">よくある質問</a></li>
          <li><a href="../contact.html">お問い合わせ</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Information</h4>
        <ul>
          <li><a href="../privacy.html">プライバシーポリシー</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2025 Muku Inc. All rights reserved.</span>
      <span>Designed by SHARKSTARS</span>
    </div>
  </div>
</footer>

<script src="../js/main.js"></script>
</body>
</html>
```

- [ ] **Step 2: ブラウザで開いて骨格確認**

Run:
```bash
start client/muku/re-jalo/index.html
```
Expected: ヘッダー（Mukuロゴ＋「ご予約・ご相談」）とフッターが表示され、Mukuサイトと同じ見た目。コンソールエラー（404）が無い。CSS/フォント/ロゴが読み込まれている。

- [ ] **Step 3: JSON-LDの構文確認**

Run:
```bash
node -e "const fs=require('fs');const h=fs.readFileSync('client/muku/re-jalo/index.html','utf8');const m=h.match(/<script type=\"application\/ld\+json\">([\s\S]*?)<\/script>/);JSON.parse(m[1]);console.log('JSON-LD OK')"
```
Expected: `JSON-LD OK`

- [ ] **Step 4: コミット**

```bash
git add client/muku/re-jalo/index.html
git commit -m "feat(muku): scaffold Re-JALO LP (head, header, footer, schema)"
```

---

## Task 3: 本文セクション 前半（ヒーロー〜プログラム）

**Files:**
- Modify: `client/muku/re-jalo/index.html`（`<!-- SECTIONS -->` を置換）

Wix構成順のセクション1〜6を追加する。文言は上記「Wix原文」ブロックからVERBATIMでコピー。

- [ ] **Step 1: `<!-- SECTIONS -->` を以下に置換**

`<!-- SECTIONS -->` の行を、次のHTMLに置き換える（後半セクションのためにend markerを残す）：

```html
<!-- ===== 01 HERO ===== -->
<section class="hero">
  <div class="hero-bg" aria-hidden="true">
    <div class="hero-slide" style="background-image: url('images/hero-rejuvenation.png');"></div>
  </div>
  <div class="hero-overlay" aria-hidden="true"></div>
  <div class="hero-vertical">Re-JALO — Medical Diet</div>
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-eyebrow">Rejuvenation for Humanity</div>
      <h1 class="hero-title">
        <span class="word"><span>細胞を磨き上げる</span></span>
        <span class="word"><span>新しい<span class="accent">医療痩身</span>のかたち</span></span>
      </h1>
      <p class="hero-sub">
        再生医療の研究拠点から生まれた、<br>
        医師管理下の次世代GIP/GLP-1プログラム
      </p>
      <div class="hero-actions">
        <a href="https://lin.ee/yALwLE6" target="_blank" rel="noopener" class="btn btn-primary">ご予約・ご相談<span class="btn-arrow">→</span></a>
      </div>
    </div>
  </div>
  <div class="hero-scroll">Scroll</div>
</section>

<!-- ===== 02 クリニック紹介 ===== -->
<section class="section section-tone">
  <div class="container container-narrow">
    <div class="section-head">
      <div class="section-eyebrow reveal">再生医療の最前線から。</div>
      <h2 class="section-title reveal reveal-delay-1">リジュヴェールクリニック</h2>
    </div>
    <div class="reveal reveal-delay-1" style="text-align:center; font-style:italic; font-family:var(--font-display); font-size:18px; color:var(--wine-500); margin-bottom:32px;">
      「細胞が持つ&ldquo;再生の力&rdquo;を人へ、未来へ、世界へ」
    </div>
    <div class="reveal" style="max-width:720px; margin:0 auto; font-size:14px; line-height:2.2; letter-spacing:0.06em; color:var(--ink-700); text-align:center;">
      <p>リジュヴェールクリニックは、リジュヴェールクリニック川崎院（準備中）での再生医療研究を背景に持つ、次世代の医療クリニックです。</p>
    </div>
  </div>
</section>

<!-- ===== 03 2拠点紹介 ===== -->
<section class="section">
  <div class="container">
    <div class="products products-2col">
      <article class="product-card reveal">
        <div class="product-num">Clinic 01</div>
        <h3 class="product-name">川崎院<span class="product-name-en" style="display:block;margin-top:6px;">Kawasaki — 準備中</span></h3>
        <p class="product-desc">
          リジュヴェールクリニック川崎院（準備中）は、第2種・第3種 再生医療クリニック 〜新しい再生医療技術研究を兼ねた専門クリニック〜。CPC施設(細胞培養施設)・自律型自動培養装置導入を視野に入れた直営クリニックとして開設予定。
        </p>
        <div class="product-tags">
          <span class="product-tag">第2種・第3種</span>
          <span class="product-tag">CPC施設</span>
          <span class="product-tag">民間初の第1種を目指す</span>
        </div>
      </article>
      <article class="product-card reveal reveal-delay-1">
        <div class="product-num">Clinic 02</div>
        <h3 class="product-name">梅田院<span class="product-name-en" style="display:block;margin-top:6px;">Umeda — 開院</span></h3>
        <p class="product-desc">
          梅田院では、再生医療×美容×ウェルネスケアを融合したトータルビューティーサロンとして、「理想の美」と「本来の健康」を医学的根拠に基づく施術と高度な専門技術により包括的にサポートしています。
        </p>
        <div class="product-tags">
          <span class="product-tag">再生医療</span>
          <span class="product-tag">美容</span>
          <span class="product-tag">ウェルネスケア</span>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ===== 04 理念 ===== -->
<section class="section section-dark">
  <div class="container container-narrow">
    <div class="section-head">
      <div class="section-eyebrow reveal">Philosophy</div>
      <h2 class="section-title reveal reveal-delay-1" style="font-size:clamp(28px,4.5vw,44px); line-height:1.4;">
        「量」を追う時代は終わりました。<br>これからは「質」の時代です。
      </h2>
    </div>
    <div class="reveal" style="text-align:center; font-size:14px; line-height:2.4; letter-spacing:0.06em; color:var(--pink-100); max-width:760px; margin:0 auto;">
      <p>
        過度な制限、激しい消耗。それはもう、あなたのライフスタイルには似合いません。<br>
        私たちが目指すのは、単なる体重の減少ではなく、細胞レベルでの「Rejuvenation（若返り）」。<br>
        最新の医学的知見に基づき、食欲と代謝のメカニズムを最適化する。<br>
        それは、宝石の原石を磨くように、あなた本来の美しさと健康を呼び覚ますプロセスです。
      </p>
    </div>
  </div>
</section>

<!-- ===== 05 プログラム紹介＋お悩み ===== -->
<section class="section" id="program">
  <div class="container">
    <div class="intro-grid">
      <div class="intro-text reveal">
        <div class="section-eyebrow" style="margin-bottom:14px;">リジュヴェールクリニックがお届けする、医療痩身プログラム。</div>
        <h3 style="font-family:var(--font-display); font-size:clamp(30px,5vw,48px); line-height:1.2; margin-bottom:24px;">リージャロ<span class="product-name-en" style="display:block;margin-top:8px;">Re-JALO Medical Diet</span></h3>
        <p style="font-size:14px; line-height:2; color:var(--ink-700);">
          「痩せる」ことだけを目的にするのではなく、身体の仕組みに向き合い、安全性を重視した体重管理を行う医療痩身プログラムです。
        </p>
        <p style="font-size:14px; line-height:2; color:var(--ink-700);">
          GLP-1／GIP受容体作動薬を用いた医師監修・当院独自の処方により、食欲や代謝に関わる身体の働きに医学的にアプローチし、無理のない体重管理を目指します。
        </p>
      </div>
      <div class="intro-visual reveal reveal-delay-1">
        <img src="images/counseling.webp" alt="医師によるカウンセリングの様子">
        <div class="intro-visual-frame"></div>
      </div>
    </div>

    <div class="reveal" style="margin-top:64px;">
      <h4 style="text-align:center; font-family:var(--font-display); font-size:20px; letter-spacing:0.1em; margin-bottom:32px; color:var(--ink-900);">このようなお悩みがある方へ</h4>
      <ul class="worry-list">
        <li>食事量を抑えたいが、なかなか続かない</li>
        <li>運動が苦手、または時間が取れない</li>
        <li>これまでのダイエットが長続きしなかった</li>
        <li>自己流ではなく、医師に相談しながら体重管理をしたい</li>
      </ul>
    </div>
  </div>
</section>

<!-- SECTIONS-MID -->
```

- [ ] **Step 2: ブラウザで前半を目視確認**

Run:
```bash
start client/muku/re-jalo/index.html
```
Expected: ヒーロー（背景画像＋見出し＋サブ＋CTA）→ クリニック紹介 → 2拠点カード → 理念（ダーク背景）→ プログラム＋お悩みリスト、の順で表示。`.worry-list` は未スタイルなので素のリスト表示でOK（Task 5で整える）。画像 counseling.webp / hero-rejuvenation.png が表示される（404でない）。

- [ ] **Step 3: コミット**

```bash
git add client/muku/re-jalo/index.html
git commit -m "feat(muku): Re-JALO LP sections 1-5 (hero, clinic, philosophy, program)"
```

---

## Task 4: 本文セクション 後半（サイエンス〜最終CTA）

**Files:**
- Modify: `client/muku/re-jalo/index.html`（`<!-- SECTIONS-MID -->` を置換）

セクション6〜12を追加。「院内調合→医師監修」変更（★）を必ず反映。

- [ ] **Step 1: `<!-- SECTIONS-MID -->` を以下に置換**

```html
<!-- ===== 06 サイエンス ===== -->
<section class="section section-tone">
  <div class="container">
    <div class="intro-grid" style="direction:rtl;">
      <div class="intro-text reveal" style="direction:ltr;">
        <div class="section-eyebrow" style="margin-bottom:14px;">The Science</div>
        <h3 style="font-family:var(--font-display); font-size:clamp(24px,4vw,38px); line-height:1.4; margin-bottom:24px;">世界が注目する<br>「ダブル受容体作動」の力。</h3>
        <p style="font-size:14px; line-height:2; color:var(--ink-700);">
          GLP-1に加え、GIPという第2のホルモンに作用する「チルゼパチド」成分を基軸に採用。従来のGLP-1単独療法を超え、血糖コントロールと脂肪燃焼を強力にサポートします。
        </p>
        <div style="margin-top:24px; padding:18px 22px; background:var(--pink-50); border-left:2px solid var(--pink-400);">
          <div style="font-family:var(--font-display); font-weight:500; color:var(--ink-900); margin-bottom:8px;">処方に関する重要事項</div>
          <p style="font-size:13px; line-height:1.9; color:var(--ink-700);">
            医師監修により濃度や配合を調整し、一般的なGLP-1製剤と比較して副作用の発現を抑えることを目指した構成としていますが、全ての副作用が無くなるわけではありません。<br>
            ※吐き気、胃のむかつき等が起こる場合があります。医師が適切に経過を観察します。
          </p>
        </div>
      </div>
      <div class="intro-visual reveal reveal-delay-1" style="direction:ltr;">
        <img src="images/science-gipglp1.webp" alt="GLP-1とGIPのダブル受容体作動のイメージ">
        <div class="intro-visual-frame"></div>
      </div>
    </div>
  </div>
</section>

<!-- ===== 07 ニードルフリー ===== -->
<section class="section" id="needlefree">
  <div class="container">
    <div class="section-head">
      <div class="section-eyebrow reveal">ニードルフリー・システム</div>
      <h2 class="section-title reveal reveal-delay-1">「刺さない」という、新しい選択。</h2>
      <p class="section-desc reveal reveal-delay-2">
        効果は欲しいが、痛みは伴いたくない。そんな願いに応える「無針注射器」を採用しています。高圧ジェット技術により、瞬時に、そして痛みを感じにくく薬剤を浸透させます。週に1回、ご自宅でのケアを快適に続けていただけます。
      </p>
    </div>

    <div class="nf-points reveal">
      <div class="nf-point"><span class="nf-num">01</span><p>週1回、自宅で自己投与</p></div>
      <div class="nf-point"><span class="nf-num">02</span><p>投与説明は初回にオンラインまたは院内で実施</p></div>
      <div class="nf-point"><span class="nf-num">03</span><p>厳重な温度管理下のクール便でお届け</p></div>
    </div>

    <h4 class="reveal" style="text-align:center; font-family:var(--font-display); font-size:18px; letter-spacing:0.1em; margin:56px 0 28px; color:var(--ink-900);">使用方法</h4>
    <div class="nf-gallery reveal">
      <figure><img src="images/device-kit.jpg" alt="無針注射器キットの内容"><figcaption>キット内容</figcaption></figure>
      <figure><img src="images/device-assemble.jpg" alt="無針注射器の組み立て"><figcaption>セット</figcaption></figure>
      <figure><img src="images/device-inject.jpg" alt="無針注射器による投与"><figcaption>投与（約3秒キープ）</figcaption></figure>
    </div>
    <div class="nf-products reveal">
      <img src="images/device-logo.jpg" alt="Comfort-in 無針注射器">
      <img src="images/device-box.jpg" alt="Comfort-in 製品パッケージ">
    </div>
  </div>
</section>

<!-- ===== 08 安心の3本柱 ===== -->
<section class="section section-tone">
  <div class="container">
    <div class="section-head">
      <div class="section-eyebrow reveal">Safety &amp; Trust</div>
      <h2 class="section-title reveal reveal-delay-1">医師監修の安全管理体制。</h2>
      <p class="section-desc reveal reveal-delay-2">
        Re-JALOは、サロンや非医療従事者が扱うものではありません。再生医療研究を背景に持つ医療機関として、厳格な適応判断と安全管理を行います。
      </p>
    </div>
    <div class="products">
      <article class="product-card reveal">
        <div class="product-num">01</div>
        <h3 class="product-name">完全医師対応</h3>
        <p class="product-desc">処方・経過観察は必ず医師が行います。オンライン診察にも対応。</p>
      </article>
      <article class="product-card reveal reveal-delay-1">
        <div class="product-num">02</div>
        <h3 class="product-name">厳格な適応判断</h3>
        <p class="product-desc">BMIや既往歴を精査し、医学的妥当性を重視した処方を行います。</p>
      </article>
      <article class="product-card reveal reveal-delay-2">
        <div class="product-num">03</div>
        <h3 class="product-name">徹底した品質管理</h3>
        <p class="product-desc">医師監修のオリジナル処方。厳重な温度管理下のクール便でお届けします。</p>
      </article>
    </div>
  </div>
</section>

<!-- ===== 09 料金プラン ===== -->
<section class="section" id="price">
  <div class="container container-narrow">
    <div class="section-head">
      <div class="section-eyebrow reveal">Price</div>
      <h2 class="section-title reveal reveal-delay-1">料金プラン</h2>
    </div>
    <div class="price reveal">
      <div class="price-block">
        <div class="price-block-label">初回セット料金 <small>（税別表示）</small></div>
        <ul class="price-list">
          <li>
            <span class="price-name">無針注射器（Comfort-in）</span>
            <span class="price-amount">25,000円</span>
            <span class="price-note">定価110,880円から特別割引</span>
          </li>
          <li>
            <span class="price-name">皮下注射薬 5.0mg×4本（1か月分）</span>
            <span class="price-amount">20,000円</span>
          </li>
        </ul>
      </div>
      <div class="price-block">
        <div class="price-block-label">2回目以降</div>
        <ul class="price-list">
          <li>
            <span class="price-name">皮下注射薬 5.0mg×4本（1か月分）</span>
            <span class="price-amount">30,000円</span>
          </li>
        </ul>
      </div>
      <p style="margin-top:24px; font-size:12px; color:var(--ink-500); line-height:1.9; text-align:center;">
        ※表示価格は税別です　※初診料として別途3,000円（税込み3,300円）がかかります
      </p>
    </div>
  </div>
</section>

<!-- ===== 10 注意事項・禁忌 ===== -->
<section class="section section-tone">
  <div class="container container-narrow">
    <aside class="notice reveal">
      <div class="notice-head">
        <span class="notice-label">Notice / 治療にあたって</span>
        <h4 class="notice-title">治療にあたっての大切なご案内</h4>
      </div>
      <ul class="notice-items">
        <li><span class="notice-num">01</span><span>本治療は自由診療であり、保険適応外となります。</span></li>
        <li><span class="notice-num">02</span><span>効果や経過には個人差があります。</span></li>
        <li><span class="notice-num">03</span><span>副作用（吐き気、胃もたれ等）が生じる可能性があります。</span></li>
        <li><span class="notice-num">04</span><span>重大な副作用（稀）：急性膵炎、脱水、腎機能低下、胆のう疾患</span></li>
        <li><span class="notice-num">05</span><span>自己判断での増量、中止、または他者への譲渡は禁止です。</span></li>
        <li><span class="notice-num">06</span><span>患者様ごとのオーダーメイド処方という特性上、決済完了後はいかなる理由でも返金はできません。予めご了承ください。</span></li>
      </ul>
      <div class="contra">
        <div class="contra-head">【禁忌】以下に該当する場合、本治療は行えません</div>
        <p>BMI18.5未満 / 妊娠中・授乳中・妊娠希望 / 膵炎の既往 / 甲状腺髄様癌の既往または家族歴 / 重度の腎疾患・心疾患・重度高血圧 / 消化器疾患の重い方 / 主治医により制限されている場合 / 18歳未満</p>
      </div>
    </aside>
  </div>
</section>

<!-- ===== 11 ビジョン ===== -->
<section class="vision">
  <div class="vision-bg" aria-hidden="true" style="background-image:url('images/vision-mirror.jpg');"></div>
  <div class="vision-overlay" aria-hidden="true"></div>
  <div class="vision-inner reveal">
    <div class="section-eyebrow" style="color:var(--pink-200);">人生を再起動させる医療</div>
    <h2>輝きに満ちた、<br>新しい自分へ。</h2>
  </div>
</section>

<!-- ===== 12 最終CTA ===== -->
<section class="section">
  <div class="container container-narrow">
    <article class="line-block reveal">
      <div class="line-block-eyebrow">— Reservation</div>
      <h2 class="line-block-title">まずはお気軽に<br><span style="font-style:italic; color:var(--wine-500);">ご相談ください</span></h2>
      <p class="line-block-desc">
        医師によるオンラインカウンセリングをご用意しております。
      </p>
      <a href="https://lin.ee/yALwLE6" target="_blank" rel="noopener" class="btn btn-primary btn-line">
        カウンセリングを予約する<span class="btn-arrow">→</span>
      </a>
      <div class="line-block-id">完全予約制</div>
      <p class="line-block-note">
        リジュヴェールクリニック梅田院<br>
        大阪府大阪市北区曽根崎新地1-7-30 ／ Tel: 06-7777-6201
      </p>
    </article>
  </div>
</section>
```

- [ ] **Step 2: ブラウザで後半を目視確認**

Run:
```bash
start client/muku/re-jalo/index.html
```
Expected: サイエンス（右画像＋重要事項ボックスに「医師監修により濃度や配合を調整し」）→ ニードルフリー（3ポイント＋使用方法写真3枚＋製品2枚）→ 安心3本柱（柱3に「医師監修のオリジナル処方」）→ 料金表 → 注意事項＋禁忌 → ビジョン（鏡画像背景）→ 最終CTA（LINE）。画像が全て表示。`.nf-points .nf-gallery .nf-products .worry-list .contra .vision` はまだ未スタイル（Task 5で整える）。

- [ ] **Step 3: 「院内調合」が残っていないことを確認**

Run:
```bash
grep -c "院内調合" client/muku/re-jalo/index.html
```
Expected: `0`

- [ ] **Step 4: 文言の取りこぼし確認（主要キーワード）**

Run:
```bash
grep -c -e "チルゼパチド" -e "Rejuvenation" -e "禁忌" -e "曽根崎新地" -e "完全予約制" client/muku/re-jalo/index.html
```
Expected: 各行 `1` 以上（5行出力、すべて1以上）。

- [ ] **Step 5: コミット**

```bash
git add client/muku/re-jalo/index.html
git commit -m "feat(muku): Re-JALO LP sections 6-12 (science, needle-free, safety, price, notice, vision, CTA); 院内調合→医師監修"
```

---

## Task 5: LP固有スタイル（`<style>`ブロック）

**Files:**
- Modify: `client/muku/re-jalo/index.html`（head内の `<style>` を埋める）

Task 3-4で使った未スタイルクラス（`.worry-list .nf-points .nf-point .nf-num .nf-gallery .nf-products .contra .contra-head .vision .vision-bg .vision-overlay .vision-inner`）を、Muku既存トーンに合わせてスタイリングする。

- [ ] **Step 1: `<style>` ブロックを以下で置換**

head内の `/* ==== Re-JALO LP 固有スタイル（Task 5で追記） ==== */` を含む `<style>...</style>` を次に置換：

```html
  <style>
  /* ==== Re-JALO LP 固有スタイル ==== */

  /* お悩みリスト */
  .worry-list {
    list-style: none;
    max-width: 640px;
    margin: 0 auto;
    display: grid;
    gap: 14px;
  }
  .worry-list li {
    position: relative;
    padding: 18px 24px 18px 52px;
    background: var(--cream-50);
    border: 1px solid var(--ink-100);
    border-radius: 8px;
    font-size: 14px;
    line-height: 1.7;
    color: var(--ink-800);
  }
  .worry-list li::before {
    content: "✓";
    position: absolute;
    left: 22px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--pink-500);
    font-weight: 700;
  }

  /* ニードルフリー 3ポイント */
  .nf-points {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 8px;
  }
  .nf-point {
    text-align: center;
    padding: 32px 20px;
    background: var(--cream-50);
    border: 1px solid var(--ink-100);
    border-radius: 12px;
  }
  .nf-num {
    display: block;
    font-family: var(--font-latin);
    font-size: 28px;
    color: var(--pink-500);
    margin-bottom: 12px;
  }
  .nf-point p { font-size: 13px; line-height: 1.8; color: var(--ink-700); }

  /* 使用方法ギャラリー */
  .nf-gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }
  .nf-gallery figure { margin: 0; }
  .nf-gallery img {
    width: 100%;
    aspect-ratio: 4 / 3;
    object-fit: cover;
    border-radius: 10px;
    display: block;
  }
  .nf-gallery figcaption {
    margin-top: 10px;
    text-align: center;
    font-size: 12px;
    letter-spacing: 0.08em;
    color: var(--ink-500);
  }
  .nf-products {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 24px;
  }
  .nf-products img {
    width: 100%;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    border-radius: 10px;
    display: block;
  }

  /* 禁忌ボックス */
  .contra {
    margin-top: 28px;
    padding: 24px;
    background: var(--ink-900);
    border-radius: 10px;
  }
  .contra-head {
    font-family: var(--font-display);
    font-size: 15px;
    color: var(--pink-200);
    margin-bottom: 12px;
    letter-spacing: 0.04em;
  }
  .contra p {
    font-size: 13px;
    line-height: 2;
    color: var(--cream-100);
    letter-spacing: 0.03em;
  }

  /* ビジョン（フルブリード） */
  .vision {
    position: relative;
    min-height: 70vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    text-align: center;
  }
  .vision-bg {
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: center;
  }
  .vision-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(21,17,11,0.45), rgba(21,17,11,0.65));
  }
  .vision-inner { position: relative; z-index: 1; padding: 40px 24px; }
  .vision-inner h2 {
    font-family: var(--font-display);
    font-size: clamp(32px, 6vw, 56px);
    line-height: 1.3;
    color: var(--white);
    margin-top: 16px;
  }

  /* レスポンシブ */
  @media (max-width: 768px) {
    .nf-points { grid-template-columns: 1fr; }
    .nf-gallery { grid-template-columns: 1fr; }
    .nf-products { grid-template-columns: 1fr; }
  }
  </style>
```

- [ ] **Step 2: ブラウザでPC幅の見た目確認**

Run:
```bash
start client/muku/re-jalo/index.html
```
Expected: お悩みリストにチェックマーク、3ポイントが3カラム、使用方法が3枚横並び、製品2枚、禁忌が濃色ボックス、ビジョンが背景画像＋オーバーレイ＋白文字でフルブリード表示。Mukuサイトと統一感がある。

- [ ] **Step 3: モバイル幅の確認（DevTools）**

ブラウザのDevToolsで幅375pxに切替（またはウィンドウを狭める）。
Expected: 3カラム系（nf-points/nf-gallery/nf-products）が1カラムに縦積み。横スクロールが発生しない。見出しが折り返しで崩れない。

- [ ] **Step 4: コミット**

```bash
git add client/muku/re-jalo/index.html
git commit -m "feat(muku): Re-JALO LP component styles (worry list, needle-free, contra, vision)"
```

---

## Task 6: service.html のリンク張替

**Files:**
- Modify: `client/muku/service.html:203`

外部Wixリンクを内部Re-JALO LPに張り替える。

- [ ] **Step 1: 現在のリンクを確認**

Run:
```bash
grep -n "usakuma15.wixsite.com" client/muku/service.html
```
Expected: 1件ヒット（203行目付近、`<a href="https://usakuma15.wixsite.com/muku" target="_blank" rel="noopener noreferrer" class="btn btn-primary">`）。

- [ ] **Step 2: Editで張替**

`client/muku/service.html` の該当 `<a>` を置換：

old:
```html
      <a href="https://usakuma15.wixsite.com/muku" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
        Re-JALO 公式LPへ<span class="btn-arrow">↗</span>
      </a>
```
new:
```html
      <a href="re-jalo/" class="btn btn-primary">
        Re-JALO 詳細・ご予約はこちら<span class="btn-arrow">→</span>
      </a>
```

- [ ] **Step 3: 張替確認**

Run:
```bash
grep -n "usakuma15.wixsite.com" client/muku/service.html; grep -n 'href="re-jalo/"' client/muku/service.html
```
Expected: 1行目（wixsite）は出力なし。2行目（re-jalo/）は1件ヒット。

- [ ] **Step 4: リンク導線をブラウザ確認**

Run:
```bash
start client/muku/service.html
```
Expected: Re-JALOセクションのボタンが「Re-JALO 詳細・ご予約はこちら」になり、クリックで `re-jalo/index.html` が開く（Wixに飛ばない）。

- [ ] **Step 5: コミット**

```bash
git add client/muku/service.html
git commit -m "feat(muku): point service.html Re-JALO link to internal LP (was external Wix)"
```

---

## Task 7: 最終検証（壊れリンク・壊れ画像・全体通し）

**Files:**
- なし（検証のみ）

- [ ] **Step 1: 参照画像がすべて実在することを確認**

Run:
```bash
cd client/muku/re-jalo
for f in $(grep -oE "images/[A-Za-z0-9._-]+" index.html | sort -u); do [ -f "$f" ] && echo "OK  $f" || echo "MISSING  $f"; done
```
Expected: すべて `OK`。`MISSING` が無い。

- [ ] **Step 2: 相対パス（CSS/JS/ロゴ）の実在確認**

Run:
```bash
cd client/muku/re-jalo
for f in ../css/reset.css ../css/style.css ../js/main.js ../images/mukulogo.avif; do [ -f "$f" ] && echo "OK  $f" || echo "MISSING  $f"; done
```
Expected: すべて `OK`。

- [ ] **Step 3: 全セクション存在の確認**

Run:
```bash
grep -c -e "細胞を磨き上げる" -e "リジュヴェールクリニック" -e "量」を追う時代" -e "リージャロ" -e "ダブル受容体作動" -e "刺さない" -e "安全管理体制" -e "料金プラン" -e "治療にあたっての大切" -e "人生を再起動" -e "ご相談ください" client/muku/re-jalo/index.html
```
Expected: 11行すべて `1` 以上（全14セクションの主要見出しが存在）。

- [ ] **Step 4: ブラウザで全体を上から下まで通し確認**

Run:
```bash
start client/muku/re-jalo/index.html
```
Expected:
- 全セクションがWix順（ヒーロー→クリニック→2拠点→理念→プログラム→サイエンス→ニードルフリー→3本柱→料金→注意事項→ビジョン→CTA）で表示
- 全画像が表示（壊れアイコン無し）
- 全CTA（ヘッダー・ヒーロー・最終CTA）がLINE `lin.ee/yALwLE6` を指す
- reveal アニメーションが動作（スクロールで要素がフェードイン）
- ハンバーガーメニューは最小ヘッダーには無い（ナビが無いので不要）。コンソールエラーが出ないこと。

- [ ] **Step 5: CTAリンクの最終grep確認**

Run:
```bash
grep -c "lin.ee/yALwLE6" client/muku/re-jalo/index.html
```
Expected: `3`（ヘッダー・ヒーロー・最終CTA）。

- [ ] **Step 6: 完了コミット（もし未コミットの変更があれば）**

```bash
git add -A client/muku/
git commit -m "chore(muku): Re-JALO LP final verification" --allow-empty
```

---

## Self-Review（プラン作成者による確認・記録）

- **Spec coverage:** 仕様書の全14セクション → Task 3（1-5）/ Task 4（6-12）でカバー。画像14枚 → Task 1。リンク張替 → Task 6。デザイン統一 → 既存style.css流用＋Task 5。CTA統一 → 全タスクで `lin.ee/yALwLE6`。院内調合→医師監修 → Task 4のStep内★＋Step 3で検証。✓
- **Placeholder scan:** メタタイトルは確定値を記載（「仮」表現はプランからは排除済み）。各コード片は完全なHTML/CSSを記載。TODO無し。✓
- **Type/クラス整合:** Task 3-4で使うクラス（worry-list, nf-points, nf-point, nf-num, nf-gallery, nf-products, contra, contra-head, vision, vision-bg, vision-overlay, vision-inner）はすべてTask 5でスタイル定義。既存クラス名はstyle.css実在を確認済み。✓
- **薬機法:** 効果断定を避け、Wix原文の注意事項・禁忌を完全再現。「院内調合」は表現リスク回避のため「医師監修」へ（ユーザー指示）。✓
