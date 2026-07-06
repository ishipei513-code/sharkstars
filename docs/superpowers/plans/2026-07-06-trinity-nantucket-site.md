# TRINITY ナンタケットバスケット特化サイト 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 紹介制のナンタケットバスケット教室 TRINITY の世界観サイト（4ページ）を `client/trinity/` に新規構築する。

**Architecture:** 静的HTML/CSS/vanilla JS。ギャラリー・ホワイト（白い美術館）×シネマティック（全画面写真クロスフェード）。共通部品は `css/style.css`＋`js/main.js`、TOP専用演出は `css/top.css`＋`js/top.js`、作品集は `js/gallery.js`（自作ライトボックス）。プレビュー中は marin と同じく `https://sharkstars.jp/client/trinity/` をcanonical・`noindex` とし、本番ドメイン確定時に一括差し替え。

**Tech Stack:** HTML5 / CSS（カスタムプロパティ）/ vanilla JS（IntersectionObserver）/ Google Fonts（Shippori Mincho・Cormorant Garamond）/ JSON-LD

**Spec:** `docs/superpowers/specs/2026-07-06-trinity-nantucket-site-design.md`

---

## 静的サイトの検証方針（このリポジトリの流儀）

ユニットテストは無い。各タスクの検証は：
1. `python -m http.server 8000 -d client/trinity` を起動し `curl -s http://localhost:8000/<page>` でHTML確認（またはブラウザ目視）
2. grepによる必須タグ検査（canonical / og:image / JSON-LD など）
3. 最終タスクでリンク・画像切れの機械チェック

## 公開前差し替え定数（実装中は仮値で進める）

| 定数 | 実装中の仮値 | 確定タイミング |
| --- | --- | --- |
| 本番ドメイン | `https://sharkstars.jp/client/trinity/`（プレビューURL） | クライアントがドメイン候補から選定後、Task 11のsedで一括置換 |
| 公式LINE URL | `https://lin.ee/TRINITY-TBD` | クライアント確認⑩の回答後に置換（Task 11でgrep検出） |
| Instagram | `https://www.instagram.com/nouvelle_basket/` | 確認⑪（おそらく確定） |
| 電話 | `080-4312-3453` | 現行サイト掲載値 |

---

### Task 1: スキャフォールドと reset.css

**Files:**
- Create: `client/trinity/css/reset.css`（marinから複製）
- Create: `client/trinity/{css,js,images,images/source}/` ディレクトリ

- [ ] **Step 1: ディレクトリ作成と reset.css 複製**

```bash
mkdir -p client/trinity/css client/trinity/js client/trinity/images/source
cp client/marin/css/reset.css client/trinity/css/reset.css
```

- [ ] **Step 2: 確認**

Run: `ls client/trinity/css`
Expected: `reset.css`

- [ ] **Step 3: Commit**

```bash
git add client/trinity
git commit -m "chore(trinity): スキャフォールドとreset.cssを追加"
```

---

### Task 2: 画像回収（グーペCDN・アメブロ）と選定

⚠️ グーペ解約でCDN画像は消える。**最初に回収する**。

**Files:**
- Create: `scripts/collect_trinity_images.py`
- Create: `client/trinity/images/source/*`（回収した原本）
- Create: `client/trinity/images/{hero-1..3, work-01.., atelier-1, teacher-1}.jpg`（選定・改名後）

- [ ] **Step 1: 回収スクリプトを書く**

```python
# scripts/collect_trinity_images.py
# 現行TRINITYサイト(グーペ)とアメブロから画像URLを抽出しダウンロードする（乗り換え前の素材回収）
import re, os, urllib.request

PAGES = [
    "https://www.trinity-fukuoka.com/",
    "https://www.trinity-fukuoka.com/free/nantucket-basket",
    "https://www.trinity-fukuoka.com/free/about",
    "https://ameblo.jp/trinity345/",
]
OUT = "client/trinity/images/source"
UA = {"User-Agent": "Mozilla/5.0 (image backup before Goope cancellation)"}

os.makedirs(OUT, exist_ok=True)
seen = set()
for page in PAGES:
    try:
        html = urllib.request.urlopen(urllib.request.Request(page, headers=UA), timeout=20).read().decode("utf-8", "ignore")
    except Exception as e:
        print(f"SKIP {page}: {e}")
        continue
    urls = re.findall(r'https?://(?:img\.goope\.jp|cdn\.goope\.jp|stat\.ameba\.jp/user_images)[^\s"\'<>]+?\.(?:jpe?g|png)', html)
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        name = re.sub(r'[^A-Za-z0-9._-]', '_', u.split('/')[-1])[-60:]
        try:
            urllib.request.urlretrieve(u, os.path.join(OUT, name))
            print("OK ", u)
        except Exception as e:
            print("NG ", u, e)
print(f"done: {len(os.listdir(OUT))} files")
```

- [ ] **Step 2: 実行**

Run: `python scripts/collect_trinity_images.py`
Expected: `done: N files`（N≧10目安。0件のページがあればURLパターンをprintで確認し正規表現を調整）

- [ ] **Step 3: 選定・改名**

`client/trinity/images/source/` の画像をReadツールで1枚ずつ確認し、以下の基準で `client/trinity/images/` へコピー・改名：
- `hero-1.jpg`〜`hero-3.jpg` … バスケットが美しく写る横長向き3枚（ヒーロークロスフェード用）
- `work-01.jpg`〜（20〜30枚目標、当面はある分だけ） … 作品単体の写真
- `atelier-1.jpg` … 教室・アトリエの雰囲気
- `teacher-1.jpg` … 講師の写真（あれば）
- 認定バッジ・他レッスン（酵素/クッキー等）・ブラウザUI入りスクショは**除外**

- [ ] **Step 4: Commit（sourceも含めてバックアップとしてコミット）**

```bash
git add scripts/collect_trinity_images.py client/trinity/images
git commit -m "feat(trinity): 現行サイトから画像素材を回収・選定（グーペ解約前バックアップ）"
```

---

### Task 3: 共通CSS（style.css）— トークン・部品・ヘッダー/フッター

**Files:**
- Create: `client/trinity/css/style.css`

- [ ] **Step 1: style.css を書く**

```css
/* ============ TRINITY 共通スタイル ============ */
/* 世界観：白いギャラリーに写真。籐色は細線とラベルのみ。塗りボタン禁止 */
:root{
  --paper:#FDFCFA;      /* 背景 */
  --cream:#F6F3EC;      /* 生成の面（帯） */
  --ink:#1C1B19;        /* 文字 */
  --ink-soft:#55524C;   /* 従属文字 */
  --rattan:#B8A17D;     /* 籐（アクセント） */
  --rattan-deep:#8A6F4D;/* hover */
  --slate:#5B6570;      /* 灯台船の灰青（ごく従属的に） */
  --serif-jp:"Shippori Mincho","Yu Mincho","Hiragino Mincho ProN",serif;
  --serif-en:"Cormorant Garamond",Georgia,serif;
  --sans:"Yu Gothic","Hiragino Kaku Gothic ProN",sans-serif;
}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--serif-jp);font-size:15px;line-height:2.1;letter-spacing:.04em;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}
.wrap{max-width:1080px;margin:0 auto;padding:0 24px}
.en{font-family:var(--serif-en);font-style:italic;color:var(--rattan)}

/* --- セクション見出し（美術館キャプション式：籐の細線＋通し番号） --- */
.sec{padding:96px 0}
.sec-head{border-top:1px solid color-mix(in srgb,var(--rattan) 45%,transparent);padding-top:14px;margin-bottom:48px;display:flex;justify-content:space-between;align-items:baseline}
.sec-head .t{font-size:12px;letter-spacing:.42em;color:var(--ink-soft)}
.sec-head .n{font-family:var(--serif-en);font-style:italic;font-size:15px;color:var(--rattan)}
.sec-title{font-size:clamp(22px,4.6vw,30px);font-weight:500;letter-spacing:.1em;line-height:1.8;margin-bottom:28px}

/* --- ボタン：細枠のみ --- */
.btn{display:inline-block;border:1px solid var(--rattan);color:var(--rattan-deep);font-size:13px;letter-spacing:.28em;padding:14px 40px;transition:.4s;text-align:center}
.btn:hover{background:var(--rattan);color:#fff}
.pill{display:inline-flex;align-items:center;gap:8px;border:1px solid #ddd;border-radius:999px;padding:12px 28px;font-size:13px;letter-spacing:.12em;color:var(--ink-soft);transition:.4s}
.pill:hover{border-color:var(--rattan);color:var(--rattan-deep)}

/* --- 写真の額装（余白に浮かべる） --- */
.framed{box-shadow:0 32px 64px -32px rgba(28,27,25,.35)}

/* --- ヘッダー --- */
.header{position:fixed;inset:0 0 auto;z-index:100;transition:.5s;padding:22px 0}
.header .bar{display:flex;justify-content:space-between;align-items:center}
.header .logo{font-family:var(--serif-en);font-style:normal;font-size:17px;letter-spacing:.45em;color:#fff;text-decoration:none}
.header.solid,.header.sub{background:rgba(253,252,250,.94);padding:14px 0;border-bottom:1px solid #f0ece4}
.header.solid .logo,.header.sub .logo{color:var(--ink)}
.nav ul{display:flex;gap:34px;list-style:none}
.nav a{font-size:11px;letter-spacing:.3em;color:#fff;text-decoration:none}
.header.solid .nav a,.header.sub .nav a{color:var(--ink-soft)}
.nav a:hover{color:var(--rattan)}
.menu-toggle{display:none}

/* --- フッター --- */
.footer{background:var(--cream);padding:72px 0 40px;text-align:center}
.footer .logo{font-family:var(--serif-en);font-size:16px;letter-spacing:.5em;margin-bottom:6px}
.footer .tag{font-size:10px;letter-spacing:.3em;color:var(--ink-soft)}
.footer .links{display:flex;justify-content:center;gap:28px;margin:28px 0 20px;flex-wrap:wrap}
.footer .links a{font-size:12px;letter-spacing:.14em;color:var(--ink-soft);text-decoration:none}
.footer .links a:hover{color:var(--rattan-deep)}
.footer .tel{font-size:11px;color:#9a968e;letter-spacing:.08em}   /* 電話は小さく（Q11=B） */
.footer .copy{font-size:10px;color:#b5b1a8;letter-spacing:.2em;margin-top:22px}

/* --- 生成色の帯（全ページ共用） --- */
.band{background:var(--cream)}

/* --- スクロールリビール（main.js) --- */
.reveal{opacity:0;transform:translateY(22px);transition:opacity 1.1s ease,transform 1.1s ease}
.reveal.is-in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){
  .reveal{opacity:1;transform:none;transition:none}
  html{scroll-behavior:auto}
}

/* --- 下層ページ共通の小ヒーロー --- */
.page-hero{padding:150px 0 60px;text-align:center}
.page-hero .en-t{font-family:var(--serif-en);font-style:italic;font-size:15px;color:var(--rattan)}
.page-hero h1{font-size:clamp(24px,5vw,34px);font-weight:500;letter-spacing:.14em;margin-top:10px}

/* --- モバイル --- */
@media (max-width:768px){
  .sec{padding:64px 0}
  .menu-toggle{display:block;width:40px;height:40px;background:none;border:0;position:relative;z-index:120}
  .menu-toggle span{position:absolute;left:9px;width:22px;height:1px;background:currentColor;color:#fff;transition:.35s}
  .header.solid .menu-toggle span,.header.sub .menu-toggle span,.menu-open .menu-toggle span{color:var(--ink)}
  .menu-toggle span:nth-child(1){top:14px}.menu-toggle span:nth-child(2){top:20px}.menu-toggle span:nth-child(3){top:26px}
  .menu-open .menu-toggle span:nth-child(1){top:20px;transform:rotate(45deg)}
  .menu-open .menu-toggle span:nth-child(2){opacity:0}
  .menu-open .menu-toggle span:nth-child(3){top:20px;transform:rotate(-45deg)}
  .nav{position:fixed;inset:0;background:var(--paper);display:grid;place-items:center;opacity:0;pointer-events:none;transition:.45s}
  .menu-open .nav{opacity:1;pointer-events:auto}
  .nav ul{flex-direction:column;text-align:center;gap:30px}
  .nav a{color:var(--ink)!important;font-size:13px}
}
```

- [ ] **Step 2: 構文チェック（波括弧の対応）**

Run: `python -c "s=open('client/trinity/css/style.css',encoding='utf-8').read(); assert s.count('{')==s.count('}'), 'brace mismatch'; print('ok')"`
Expected: `ok`

- [ ] **Step 3: Commit**

```bash
git add client/trinity/css/style.css
git commit -m "feat(trinity): デザイントークンと共通スタイル（紙・墨・籐）"
```

---

### Task 4: 共通JS（main.js）— リビール・ヘッダー状態・モバイルナビ

**Files:**
- Create: `client/trinity/js/main.js`

- [ ] **Step 1: main.js を書く**

```js
// TRINITY 共通スクリプト：スクロールリビール／ヘッダー状態／モバイルナビ
(function () {
  'use strict';

  // スクロールリビール
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -12% 0px' });
  document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });

  // TOPのみ：ヒーローを過ぎたらヘッダーを白背景に（下層は .sub 固定）
  var header = document.querySelector('.header');
  if (header && !header.classList.contains('sub')) {
    var onScroll = function () {
      header.classList.toggle('solid', window.scrollY > window.innerHeight * 0.7);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // モバイルナビ
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        document.body.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
})();
```

- [ ] **Step 2: 構文チェック**

Run: `node --check client/trinity/js/main.js`
Expected: エラーなし（nodeが無い環境なら `python -c "print('skip')"` とし、Task 11のブラウザ確認で担保）

- [ ] **Step 3: Commit**

```bash
git add client/trinity/js/main.js
git commit -m "feat(trinity): 共通JS（リビール・ヘッダー・モバイルナビ）"
```

---

### Task 5: index.html 骨格 — HEAD（SEO/JSON-LD）・ヘッダー・フッター

**Files:**
- Create: `client/trinity/index.html`（骨格。セクション中身はTask 7）

- [ ] **Step 1: index.html を書く**

```html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow"><!-- プレビュー用：本番公開時に削除 -->
<title>TRINITY｜ナンタケットバスケット教室（福岡・大濠公園）</title>
<meta name="description" content="福岡・大濠公園のナンタケットバスケット教室 TRINITY。19世紀ナンタケット島から受け継がれる籠編みを、少人数の静かなアトリエで。一生を共にする籠を、ひと編みずつ。">
<link rel="canonical" href="https://sharkstars.jp/client/trinity/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nantucket Basket Atelier TRINITY">
<meta property="og:locale" content="ja_JP">
<meta property="og:url" content="https://sharkstars.jp/client/trinity/">
<meta property="og:title" content="TRINITY｜ナンタケットバスケット教室（福岡・大濠公園）">
<meta property="og:description" content="一生を、共にする籠。福岡・大濠公園のナンタケットバスケット教室。">
<meta property="og:image" content="https://sharkstars.jp/client/trinity/images/ogp.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/top.css">
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@graph":[
    {
      "@type":"LocalBusiness",
      "@id":"https://sharkstars.jp/client/trinity/#atelier",
      "name":"Nantucket Basket Atelier TRINITY",
      "alternateName":"ナンタケットバスケット教室 TRINITY",
      "description":"福岡・大濠公園のナンタケットバスケット教室。ザ・ヌーベル・ナンタケットバスケット・アカデミー・オブ・ジャパン認定教室。紹介制。",
      "url":"https://sharkstars.jp/client/trinity/",
      "image":"https://sharkstars.jp/client/trinity/images/ogp.jpg",
      "telephone":"+81-80-4312-3453",
      "foundingDate":"2014-04",
      "founder":{"@type":"Person","name":"城島佐代子"},
      "address":{"@type":"PostalAddress","addressLocality":"福岡市中央区","addressRegion":"福岡県","addressCountry":"JP"},
      "sameAs":["https://www.instagram.com/nouvelle_basket/","https://ameblo.jp/trinity345/"]
    },
    {
      "@type":"WebSite",
      "@id":"https://sharkstars.jp/client/trinity/#website",
      "url":"https://sharkstars.jp/client/trinity/",
      "name":"Nantucket Basket Atelier TRINITY",
      "publisher":{"@id":"https://sharkstars.jp/client/trinity/#atelier"}
    }
  ]
}
</script>
</head>
<body id="top">

<header class="header">
  <div class="wrap bar">
    <a class="logo" href="index.html" aria-label="TRINITY">TRINITY</a>
    <button class="menu-toggle" aria-label="メニュー" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav"><ul>
      <li><a href="index.html" aria-current="page">トップ</a></li>
      <li><a href="works.html">作品集</a></li>
      <li><a href="lesson.html">レッスン</a></li>
      <li><a href="index.html#atelier">アトリエ</a></li>
      <li><a href="index.html#contact">ご連絡</a></li>
    </ul></nav>
  </div>
</header>

<main>
<!-- ===== HERO（Task 6） ===== -->
<!-- ===== CONCEPT / WORKS / STORY / LESSON / ATELIER / CONTACT（Task 7） ===== -->
</main>

<footer class="footer">
  <div class="wrap">
    <p class="logo">TRINITY</p>
    <p class="tag">NANTUCKET BASKET ATELIER — FUKUOKA</p>
    <div class="links">
      <a href="https://ameblo.jp/trinity345/" target="_blank" rel="noopener">今月のレッスン（ブログ）</a>
      <a href="https://www.instagram.com/nouvelle_basket/" target="_blank" rel="noopener">Instagram</a>
      <a href="works.html">作品集</a>
      <a href="lesson.html">レッスン</a>
      <a href="privacy.html">プライバシーポリシー</a>
    </div>
    <p class="tel">お電話：<a href="tel:08043123453" style="color:inherit;text-decoration:none">080-4312-3453</a></p>
    <p class="copy">&copy; TRINITY All Rights Reserved.</p>
  </div>
</footer>

<script src="js/main.js" defer></script>
<script src="js/top.js" defer></script>
</body>
</html>
```

- [ ] **Step 2: 検証**

Run: `python -m http.server 8000 -d client/trinity &` → `curl -s http://localhost:8000/index.html | grep -c "ld+json"`
Expected: `1`

- [ ] **Step 3: Commit**

```bash
git add client/trinity/index.html
git commit -m "feat(trinity): TOP骨格（HEAD/JSON-LD/ヘッダー/フッター）"
```

---

### Task 6: HERO — シネマティッククロスフェード（top.css + top.js）

**Files:**
- Create: `client/trinity/css/top.css`
- Create: `client/trinity/js/top.js`
- Modify: `client/trinity/index.html`（`<main>` 冒頭にHERO挿入）

- [ ] **Step 1: index.html の `<!-- ===== HERO（Task 6） ===== -->` を置換**

```html
<section class="hero" aria-label="TRINITY ナンタケットバスケット">
  <div class="hero-bg">
    <img src="images/hero-1.jpg" alt="ナンタケットバスケットの作品" class="is-active">
    <img src="images/hero-2.jpg" alt="バスケットを編む手元" >
    <img src="images/hero-3.jpg" alt="アトリエに並ぶナンタケットバスケット">
  </div>
  <div class="hero-inner">
    <p class="hero-en">Nantucket Basket Atelier</p>
    <h1 class="hero-title">一生を、<br class="sp">共にする籠。</h1>
    <p class="hero-sub">TRINITY — FUKUOKA</p>
  </div>
  <span class="hero-scroll">SCROLL</span>
</section>
```

- [ ] **Step 2: top.css を書く**

```css
/* ============ TOP専用：シネマティックヒーロー＋TOPセクション ============ */
.hero{position:relative;height:100vh;height:100svh;min-height:560px;overflow:hidden;display:grid;place-items:center}
.hero-bg{position:absolute;inset:0}
.hero-bg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity 2.4s ease}
.hero-bg img.is-active{opacity:1;animation:kenburns 9s ease-out forwards}
@keyframes kenburns{from{transform:scale(1.06)}to{transform:scale(1)}}
.hero-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(28,27,25,.34),rgba(28,27,25,.12) 45%,rgba(28,27,25,.38))}
.hero-inner{position:relative;z-index:2;text-align:center;color:#fff;padding:0 24px}
.hero-en{font-family:var(--serif-en);font-style:italic;font-size:clamp(14px,2.4vw,19px);letter-spacing:.14em;opacity:0;animation:heroIn 1.6s ease .6s forwards}
.hero-title{font-size:clamp(30px,6.4vw,54px);font-weight:500;letter-spacing:.16em;line-height:1.8;margin:18px 0 22px;opacity:0;animation:heroIn 1.8s ease 1.1s forwards}
.hero-sub{font-size:11px;letter-spacing:.5em;opacity:0;animation:heroIn 1.6s ease 1.8s forwards}
@keyframes heroIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
.hero-scroll{position:absolute;bottom:28px;left:50%;transform:translateX(-50%);color:#fff;font-size:9px;letter-spacing:.4em;z-index:2}
.hero-scroll::after{content:"";display:block;width:1px;height:44px;background:#fff;margin:10px auto 0;animation:scrollLine 2.2s ease infinite}
@keyframes scrollLine{0%{transform:scaleY(0);transform-origin:top}45%{transform:scaleY(1);transform-origin:top}55%{transform:scaleY(1);transform-origin:bottom}100%{transform:scaleY(0);transform-origin:bottom}}
.sp{display:none}
@media (max-width:768px){.sp{display:block}}
@media (prefers-reduced-motion:reduce){
  .hero-bg img{transition:none;animation:none!important}
  .hero-bg img.is-active{opacity:1;transform:none}
  .hero-en,.hero-title,.hero-sub{animation:none;opacity:1}
  .hero-scroll::after{animation:none}
}
```

- [ ] **Step 3: top.js を書く**

```js
// TOP専用：ヒーロー写真のクロスフェード（7.5秒周期・reduced-motion時は停止）
(function () {
  'use strict';
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var imgs = document.querySelectorAll('.hero-bg img');
  if (imgs.length < 2) return;
  var i = 0;
  setInterval(function () {
    imgs[i].classList.remove('is-active');
    i = (i + 1) % imgs.length;
    imgs[i].classList.add('is-active');
  }, 7500);
})();
```

- [ ] **Step 4: 検証（ブラウザ目視）**

Run: `python -m http.server 8000 -d client/trinity` → ブラウザで `http://localhost:8000/`
Expected: 全画面写真が7.5秒でクロスフェード、文字が順に立ち上がる、SCROLLの線が動く

- [ ] **Step 5: Commit**

```bash
git add client/trinity/css/top.css client/trinity/js/top.js client/trinity/index.html
git commit -m "feat(trinity): シネマティックヒーロー（クロスフェード＋Ken Burns）"
```

---

### Task 7: TOPセクション実装（CONCEPT〜CONTACT・実コピー流し込み）

**Files:**
- Modify: `client/trinity/index.html`（セクションプレースホルダコメントを置換）
- Modify: `client/trinity/css/top.css`（セクション用スタイル追記）

- [ ] **Step 1: `<!-- ===== CONCEPT / ... ===== -->` コメントを以下で置換**

```html
<!-- CONCEPT -->
<section class="sec concept">
  <div class="wrap">
    <p class="concept-lead reveal">
      ナンタケットバスケットは、19世紀アメリカ・ナンタケット島で<br class="pc">
      灯台船の船員たちが編み始めた籠。<br>
      百年を超えて受け継がれる、"使える工芸品"です。<br><br>
      TRINITYは、福岡・大濠公園のアトリエで、<br class="pc">
      ひと編みずつ籠と向き合う、静かな時間をお届けします。
    </p>
  </div>
</section>

<!-- WORKS抜粋 -->
<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">WORKS — 作品</span><span class="n">01</span></div>
    <div class="works-preview">
      <figure class="reveal"><img src="images/work-01.jpg" alt="ナンタケットバスケットの作品" class="framed" loading="lazy"></figure>
      <figure class="reveal"><img src="images/work-02.jpg" alt="ナンタケットバスケットの作品" class="framed" loading="lazy"></figure>
      <figure class="reveal"><img src="images/work-03.jpg" alt="ナンタケットバスケットの作品" class="framed" loading="lazy"></figure>
    </div>
    <p class="works-note reveal">作品は、教室に通う方々の手から生まれたものです。</p>
    <p class="center reveal"><a class="btn" href="works.html">作品集を見る</a></p>
  </div>
</section>

<!-- STORY -->
<section class="sec story">
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">STORY — 講師</span><span class="n">02</span></div>
    <div class="story-grid">
      <figure class="reveal"><img src="images/teacher-1.jpg" alt="講師 城島佐代子" class="framed" loading="lazy"></figure>
      <div class="story-text reveal">
        <p class="en story-en">Sayoko Kijima</p>
        <h2 class="sec-title">城島佐代子</h2>
        <p>大学で児童教育を学んだのち、ABCクッキングスタジオで7年間、福岡・熊本の主要スタジオで統括責任者を務める。2014年、福岡・大濠公園のほとりにTRINITYを開く。</p>
        <p>ひと編みごとに形が生まれていくナンタケットバスケットの奥深さに魅せられ、ザ・ヌーベル・ナンタケットバスケット・アカデミー・オブ・ジャパン認定教室として、その技術と物語を福岡から伝えている。<!-- 出会いのエピソードはクライアント取材後に差し替え（確認②） --></p>
      </div>
    </div>
  </div>
</section>

<!-- LESSON概要 -->
<section class="sec lesson-intro">
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">LESSON — レッスン</span><span class="n">03</span></div>
    <div class="lesson-grid">
      <div class="reveal">
        <h2 class="sec-title">初めてのひと籠が、<br>一生ものになる。</h2>
        <p>少人数制のレッスンは、1回2時間から2時間半。初めての方の最初の作品「4インチラウンド」は、2〜3回のレッスンで完成します。形、サイズ、木の種類、装飾——ひとつずつ選ぶところから、籠づくりは始まります。</p>
        <p class="center-sp" style="margin-top:34px"><a class="btn" href="lesson.html">レッスンについて</a></p>
      </div>
      <figure class="reveal"><img src="images/work-04.jpg" alt="レッスンで編みかけのナンタケットバスケット" class="framed" loading="lazy"></figure>
    </div>
  </div>
</section>

<!-- ATELIER -->
<section class="sec atelier" id="atelier">
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">ATELIER — アトリエ</span><span class="n">04</span></div>
    <div class="atelier-grid">
      <figure class="reveal"><img src="images/atelier-1.jpg" alt="TRINITYのアトリエ" loading="lazy"></figure>
      <div class="reveal">
        <h2 class="sec-title">大濠公園のほとりで。</h2>
        <p>アトリエは、地下鉄大濠公園駅からすぐ。天神からは7分ほどです。</p>
        <p class="note">※ 詳しい場所は、ご予約の際にご案内いたします。<!-- 住所公開範囲はクライアント確認⑤ --></p>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section class="sec contact" id="contact">
  <div class="wrap center">
    <div class="sec-head reveal"><span class="t">CONTACT — ご連絡</span><span class="n">05</span></div>
    <p class="reveal">ご紹介の方・レッスンのご相談は、<br class="sp">LINEまたはInstagramのDMからどうぞ。</p>
    <div class="contact-btns reveal">
      <a class="pill" href="https://lin.ee/TRINITY-TBD" target="_blank" rel="noopener">LINEでご連絡</a>
      <a class="pill" href="https://www.instagram.com/nouvelle_basket/" target="_blank" rel="noopener">Instagram DM</a>
    </div>
    <p class="contact-note reveal">今月のレッスン日程は<a href="https://ameblo.jp/trinity345/" target="_blank" rel="noopener">ブログ</a>でご案内しています。</p>
  </div>
</section>
```

- [ ] **Step 2: top.css 末尾にセクションスタイルを追記**

```css
/* ---- TOPセクション ---- */
.center{text-align:center}
.pc{display:block}
@media (max-width:768px){.pc{display:none}}
.concept{padding-top:110px}
.concept-lead{text-align:center;font-size:clamp(15px,2.4vw,18px);line-height:2.6;letter-spacing:.08em}
.works-preview{display:grid;grid-template-columns:1.3fr 1fr 1.1fr;gap:28px;align-items:start}
.works-preview figure:nth-child(2){margin-top:52px}
.works-preview figure:nth-child(3){margin-top:24px}
.works-note{text-align:center;font-size:12px;color:var(--ink-soft);letter-spacing:.14em;margin:30px 0 34px}
.story{background:var(--cream)}   /* TOPのSTORY帯（lesson等ではstyle.cssの.bandを使う） */
.story-grid{display:grid;grid-template-columns:1fr 1.6fr;gap:56px;align-items:center}
.story-en{font-size:15px;margin-bottom:4px}
.lesson-grid,.atelier-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:56px;align-items:center}
.atelier-grid{grid-template-columns:1fr 1fr}
.note{font-size:12px;color:var(--ink-soft)}
.contact{background:var(--cream)}
.contact-btns{display:flex;justify-content:center;gap:18px;margin:34px 0 26px;flex-wrap:wrap}
.contact-note{font-size:12px;color:var(--ink-soft)}
.contact-note a{color:var(--rattan-deep)}
@media (max-width:768px){
  .works-preview{grid-template-columns:1fr 1fr}
  .works-preview figure:first-child{grid-column:1/-1}
  .story-grid,.lesson-grid,.atelier-grid{grid-template-columns:1fr;gap:30px}
  .center-sp{text-align:center}
}
```

- [ ] **Step 3: 画像参照の実在確認**

Run: `python - <<'EOF'
import re,os
html=open('client/trinity/index.html',encoding='utf-8').read()
missing=[s for s in re.findall(r'(?:src|href)="(images/[^"]+)"',html) if not os.path.exists('client/trinity/'+s)]
print('missing:',missing or 'none')
EOF`
Expected: `missing: none`（不足があればTask 2の選定画像から充当。work-04.jpg等が無ければ実在する作品写真の番号に差し替える）

- [ ] **Step 4: ブラウザ目視**

`http://localhost:8000/` — 全セクションが順にフェードアップ、STORYとCONTACTは生成色の帯、モバイル幅で1カラム化。

- [ ] **Step 5: Commit**

```bash
git add client/trinity/index.html client/trinity/css/top.css
git commit -m "feat(trinity): TOP全セクション（CONCEPT/WORKS/STORY/LESSON/ATELIER/CONTACT）"
```

---

### Task 8: works.html — 作品集ギャラリー＋ライトボックス

**Files:**
- Create: `client/trinity/works.html`
- Create: `client/trinity/js/gallery.js`
- Modify: `client/trinity/css/style.css`（ギャラリー＋ライトボックス様式を末尾に追記）

- [ ] **Step 1: works.html を書く**

HEADはTask 5のindex.htmlと同じ構成で以下だけ変更（`css/top.css`と`js/top.js`は**読み込まない**。JSON-LDは`WebSite`ブロック省略・`LocalBusiness`のみ）：
- title: `作品集｜TRINITY ナンタケットバスケット教室（福岡）`
- description: `TRINITYの教室から生まれたナンタケットバスケットの作品集。かたち・木・装飾、ひとつとして同じもののない籠たち。`
- canonical / og:url: `https://sharkstars.jp/client/trinity/works.html`
- ヘッダーは `<header class="header sub">`（常時白背景）、ナビの`aria-current`は作品集へ

本文：

```html
<main>
<section class="page-hero">
  <p class="en-t">Works</p>
  <h1>作品集</h1>
</section>
<section class="sec" style="padding-top:20px">
  <div class="wrap">
    <p class="works-lead reveal">教室に通う方々と講師の手から生まれた籠たち。<br>同じ形でも、木と装飾の選び方でひとつずつ表情が変わります。</p>
    <div class="gallery">
      <!-- images/work-*.jpg を番号順に全点並べる。altは「ナンタケットバスケットの作品」＋分かる範囲で特徴 -->
      <figure><img src="images/work-01.jpg" alt="ナンタケットバスケットの作品" loading="lazy"></figure>
      <figure><img src="images/work-02.jpg" alt="ナンタケットバスケットの作品" loading="lazy"></figure>
      <!-- …以下、実在するwork画像を全点 -->
    </div>
  </div>
</section>
</main>
```

フッターはindex.htmlと同一。`<script src="js/main.js" defer></script><script src="js/gallery.js" defer></script>`。

- [ ] **Step 2: style.css 末尾にギャラリー様式を追記**

```css
/* --- 作品集ギャラリー（works.html） --- */
.works-lead{text-align:center;margin-bottom:56px;color:var(--ink-soft)}
.gallery{columns:3;gap:26px}
.gallery figure{break-inside:avoid;margin-bottom:26px;cursor:zoom-in}
.gallery img{width:100%;box-shadow:0 24px 48px -28px rgba(28,27,25,.3);transition:.5s}
.gallery figure:hover img{transform:translateY(-4px)}
@media (max-width:768px){.gallery{columns:2;gap:14px}.gallery figure{margin-bottom:14px}}
/* --- ライトボックス --- */
.lb{position:fixed;inset:0;z-index:200;background:rgba(28,27,25,.92);display:grid;place-items:center;opacity:0;pointer-events:none;transition:.35s}
.lb.is-open{opacity:1;pointer-events:auto}
.lb img{max-width:92vw;max-height:86vh;width:auto;height:auto;box-shadow:0 40px 80px rgba(0,0,0,.5)}
.lb-close{position:absolute;top:18px;right:22px;color:#fff;font-size:26px;background:none;border:0;cursor:pointer;line-height:1}
```

- [ ] **Step 3: gallery.js を書く**

```js
// 作品集：軽量ライトボックス（クリック拡大・Esc/背景クリックで閉じる）
(function () {
  'use strict';
  var box = document.createElement('div');
  box.className = 'lb';
  box.innerHTML = '<img alt=""><button class="lb-close" aria-label="閉じる">&times;</button>';
  document.body.appendChild(box);
  var big = box.querySelector('img');

  document.querySelectorAll('.gallery img').forEach(function (img) {
    img.parentElement.addEventListener('click', function () {
      big.src = img.src;
      big.alt = img.alt;
      box.classList.add('is-open');
    });
  });
  function close() { box.classList.remove('is-open'); }
  box.addEventListener('click', function (e) { if (e.target !== big) close(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
})();
```

- [ ] **Step 4: 検証**

`http://localhost:8000/works.html` — マソンリー3列（SP2列）、クリックで拡大、Escで閉じる。
Run: 画像実在チェック（Task 7 Step 3のスクリプトのファイル名を `works.html` に変えて実行）
Expected: `missing: none`

- [ ] **Step 5: Commit**

```bash
git add client/trinity/works.html client/trinity/js/gallery.js client/trinity/css/style.css
git commit -m "feat(trinity): 作品集ギャラリー（マソンリー＋ライトボックス）"
```

---

### Task 9: lesson.html — 歴史・レッスン・料金・FAQ（FAQPage JSON-LD）

**Files:**
- Create: `client/trinity/lesson.html`
- Modify: `client/trinity/css/style.css`（レッスンページ様式を末尾に追記）

- [ ] **Step 1: lesson.html を書く**

HEAD構成はworks.htmlと同様に変更（top.css/top.js無し・`header sub`）：
- title: `レッスン｜TRINITY ナンタケットバスケット教室（福岡）`
- description: `福岡・大濠公園のナンタケットバスケット教室TRINITYのレッスン案内。少人数制・1回2〜2.5時間。初めての方の4インチラウンドは2〜3回で完成します。`
- canonical / og:url: `https://sharkstars.jp/client/trinity/lesson.html`
- JSON-LDは `LocalBusiness`（Task 5と同内容）＋以下の `FAQPage` を追加：

```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"道具を持っていなくても始められますか？","acceptedAnswer":{"@type":"Answer","text":"はい。編むための道具は教室にご用意していますので、手ぶらでお越しいただけます。材料費は作品ごとに別途かかります。"}},
    {"@type":"Question","name":"手先が器用でなくても大丈夫ですか？","acceptedAnswer":{"@type":"Answer","text":"少人数制で、講師がひと編みずつ丁寧にお伝えします。初めての方の最初の作品（4インチラウンド）も、2〜3回のレッスンで完成します。"}},
    {"@type":"Question","name":"ひとつの籠が完成するまで、どのくらいかかりますか？","acceptedAnswer":{"@type":"Answer","text":"レッスンは1回2時間〜2時間半。最初の4インチラウンドは2〜3回で完成します。その後は作品の大きさや装飾によって変わります。"}},
    {"@type":"Question","name":"紹介がなくても通えますか？","acceptedAnswer":{"@type":"Answer","text":"当教室はご紹介の方を中心にご案内しています。まずはLINEまたはInstagramのDMからご相談ください。"}},
    {"@type":"Question","name":"予約はどうすればいいですか？","acceptedAnswer":{"@type":"Answer","text":"今月のレッスン日程はブログでご案内しています。ご予約・ご相談はLINEまたはInstagramのDMからお願いします。"}}
  ]
}
</script>
```

本文（実コピー。FAQはJSON-LDと同文をHTMLにも）：

```html
<main>
<section class="page-hero">
  <p class="en-t">Lesson</p>
  <h1>レッスン</h1>
</section>

<section class="sec" style="padding-top:30px">
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">HISTORY — ナンタケットバスケットとは</span><span class="n">01</span></div>
    <div class="hist-grid">
      <div class="reveal">
        <p>ナンタケット島は、アメリカ・マサチューセッツ州沖の大西洋に浮かぶ小さな島。19世紀、捕鯨の中心地だったこの島で、樽職人たちが灯台船（ライトシップ）に乗り込み、長い洋上の時間のなかで籠を編み始めました。それが「ライトシップバスケット」——ナンタケットバスケットの始まりです。</p>
        <p>木の底板に籐を編み込む堅牢なつくりは、百年を超えて使い継がれ、いまも世代を越えて受け継がれる"使える工芸品"として愛されています。</p>
      </div>
      <figure class="reveal"><img src="images/work-05.jpg" alt="伝統的なつくりのナンタケットバスケット" class="framed" loading="lazy"></figure>
    </div>
    <div class="nouvelle reveal">
      <h2 class="sec-title" style="font-size:clamp(18px,3vw,22px)">ヌーベルナンタケットバスケット</h2>
      <p>TRINITYでお教えするのは、伝統を踏まえながら「いまの暮らしに合う籠」として生まれたヌーベルナンタケットバスケット。やわらかな縁（ソフトリム）が特徴で、日常の装いからフォーマルな場面まで寄り添います。</p>
    </div>
  </div>
</section>

<section class="sec band"><!-- 生成の帯（style.cssの.band） -->
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">COURSE — レッスン内容</span><span class="n">02</span></div>
    <div class="course-list">
      <div class="course reveal">
        <h3>初めての方</h3>
        <p>最初の作品は、直径約10cmの「4インチラウンド」。かたちを選び、木を選び、2〜3回のレッスンで完成します。</p>
      </div>
      <div class="course reveal">
        <h3>続ける方</h3>
        <p>バッグ、トレイ、蓋つきの籠——。形・サイズ・木の種類・装飾を選び、自分だけの一点を編み上げます。</p>
      </div>
      <div class="course reveal">
        <h3>資格をめざす方</h3>
        <p>ザ・ヌーベル・ナンタケットバスケット・アカデミー・オブ・ジャパンの課程についてはお問い合わせください。<!-- 課程詳細はクライアント確認④ --></p>
      </div>
    </div>
    <div class="price reveal">
      <h3 class="price-t">料金のご案内</h3>
      <table class="price-table">
        <tr><th>入会金</th><td>10,800円（アカデミー登録料を含む）</td></tr>
        <tr><th>レッスン料</th><td>5,000円／回（1回 2時間〜2時間半）</td></tr>
        <tr><th>材料費</th><td>10,000円〜（作品・お選びになる素材により変わります）</td></tr>
        <tr><th>スターターキット</th><td>10,800円（ご自宅での練習用・ご希望の方のみ）</td></tr>
      </table>
      <p class="note">※ 表示は現行の料金です。最新の料金はご予約時にご確認ください。<!-- 確認③ --></p>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal"><span class="t">FAQ — よくあるご質問</span><span class="n">03</span></div>
    <dl class="faq">
      <dt>道具を持っていなくても始められますか？</dt>
      <dd>はい。編むための道具は教室にご用意していますので、手ぶらでお越しいただけます。材料費は作品ごとに別途かかります。</dd>
      <dt>手先が器用でなくても大丈夫ですか？</dt>
      <dd>少人数制で、講師がひと編みずつ丁寧にお伝えします。初めての方の最初の作品（4インチラウンド）も、2〜3回のレッスンで完成します。</dd>
      <dt>ひとつの籠が完成するまで、どのくらいかかりますか？</dt>
      <dd>レッスンは1回2時間〜2時間半。最初の4インチラウンドは2〜3回で完成します。その後は作品の大きさや装飾によって変わります。</dd>
      <dt>紹介がなくても通えますか？</dt>
      <dd>当教室はご紹介の方を中心にご案内しています。まずはLINEまたはInstagramのDMからご相談ください。</dd>
      <dt>予約はどうすればいいですか？</dt>
      <dd>今月のレッスン日程は<a href="https://ameblo.jp/trinity345/" target="_blank" rel="noopener">ブログ</a>でご案内しています。ご予約・ご相談はLINEまたはInstagramのDMからお願いします。</dd>
    </dl>
  </div>
</section>

<section class="sec band" style="padding:72px 0">
  <div class="wrap center">
    <p class="reveal">今月のレッスン日程は<a href="https://ameblo.jp/trinity345/" target="_blank" rel="noopener" style="color:var(--rattan-deep)">ブログ</a>でご案内しています。</p>
    <div class="contact-btns reveal" style="display:flex;justify-content:center;gap:18px;margin-top:30px;flex-wrap:wrap">
      <a class="pill" href="https://lin.ee/TRINITY-TBD" target="_blank" rel="noopener">LINEでご予約・ご相談</a>
      <a class="pill" href="https://www.instagram.com/nouvelle_basket/" target="_blank" rel="noopener">Instagram DM</a>
    </div>
  </div>
</section>
</main>
```

- [ ] **Step 2: style.css 末尾にレッスンページ様式を追記**

```css
/* --- レッスンページ（lesson.html） --- */
.hist-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:48px;align-items:center}
.nouvelle{margin-top:64px;padding:40px;background:var(--paper);border:1px solid color-mix(in srgb,var(--rattan) 35%,transparent)}
.course-list{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;margin-bottom:64px}
.course{background:var(--paper);padding:34px 28px}
.course h3{font-size:16px;letter-spacing:.14em;margin-bottom:14px;color:var(--rattan-deep)}
.price-t{text-align:center;font-size:17px;letter-spacing:.2em;margin-bottom:26px}
.price-table{width:100%;max-width:640px;margin:0 auto;border-collapse:collapse}
.price-table th,.price-table td{border-bottom:1px solid #e8e2d6;padding:16px 12px;font-weight:400;text-align:left;font-size:14px}
.price-table th{width:34%;color:var(--ink-soft);letter-spacing:.1em}
.faq dt{font-size:15px;letter-spacing:.08em;padding:22px 0 6px;color:var(--rattan-deep)}
.faq dt::before{content:"Q. ";font-family:var(--serif-en);font-style:italic}
.faq dd{border-bottom:1px solid #f0ece4;padding-bottom:22px;color:var(--ink-soft);font-size:14px}
@media (max-width:768px){.hist-grid{grid-template-columns:1fr;gap:28px}.course-list{grid-template-columns:1fr;gap:14px}.nouvelle{padding:26px 20px}}
```

- [ ] **Step 3: 検証**

Run: `curl -s http://localhost:8000/lesson.html | grep -c "FAQPage"`
Expected: `1`
FAQの `dl` に5問が入っていること・料金表4行を目視確認。

- [ ] **Step 4: Commit**

```bash
git add client/trinity/lesson.html client/trinity/css/style.css
git commit -m "feat(trinity): レッスンページ（歴史・コース・料金・FAQ/FAQPage）"
```

---

### Task 10: privacy.html

**Files:**
- Create: `client/trinity/privacy.html`

- [ ] **Step 1: privacy.html を書く**

HEADはworks.htmlと同構成（title: `プライバシーポリシー｜TRINITY`、canonical: `.../privacy.html`、JSON-LD不要、`noindex`はプレビュー中共通）。`header sub`。本文：

```html
<main>
<section class="page-hero">
  <p class="en-t">Privacy Policy</p>
  <h1>プライバシーポリシー</h1>
</section>
<section class="sec" style="padding-top:20px">
  <div class="wrap" style="max-width:760px">
    <p>TRINITY（以下「当教室」）は、お客様の個人情報を以下の方針で取り扱います。</p>
    <h2 class="pp-h">1. 取得する情報</h2>
    <p>LINE・InstagramのDM・お電話でのご連絡の際にお伺いする、お名前・ご連絡先・ご予約内容等。</p>
    <h2 class="pp-h">2. 利用目的</h2>
    <p>レッスンのご予約・ご連絡、材料の手配、教室からのご案内のために利用し、それ以外の目的には使用しません。</p>
    <h2 class="pp-h">3. 第三者提供</h2>
    <p>法令に基づく場合を除き、ご本人の同意なく第三者に提供しません。</p>
    <h2 class="pp-h">4. 外部サービス</h2>
    <p>当サイトはGoogle Fontsを利用しています。また、LINE・Instagram・Amebaブログへのリンクを含み、リンク先でのお取り扱いは各サービスのポリシーに従います。</p>
    <h2 class="pp-h">5. お問い合わせ</h2>
    <p>本ポリシーに関するお問い合わせは、LINEまたはInstagramのDMよりお願いいたします。</p>
    <p class="note" style="margin-top:40px">制定日：2026年◯月◯日<!-- 公開日に合わせる --></p>
  </div>
</section>
</main>
```

style.css 末尾に追記：

```css
/* --- プライバシーポリシー --- */
.pp-h{font-size:15px;letter-spacing:.14em;color:var(--rattan-deep);margin:36px 0 8px}
```

- [ ] **Step 2: 検証**

`http://localhost:8000/privacy.html` 目視。

- [ ] **Step 3: Commit**

```bash
git add client/trinity/privacy.html client/trinity/css/style.css
git commit -m "feat(trinity): プライバシーポリシー"
```

---

### Task 11: OGP画像・sitemap・robots・最終検証

**Files:**
- Create: `client/trinity/images/ogp.jpg`
- Create: `client/trinity/sitemap.xml`
- Create: `client/trinity/robots.txt`

- [ ] **Step 1: OGP画像を生成（代表作品写真から1200×630中央クロップ）**

```python
# 一時スクリプト（scratchpadで実行可）
from PIL import Image
im = Image.open('client/trinity/images/hero-1.jpg')
w, h = im.size
target = 1200 / 630
cw = min(w, int(h * target)); ch = int(cw / target)
im.crop(((w-cw)//2, (h-ch)//2, (w+cw)//2, (h+ch)//2)).resize((1200, 630)).save('client/trinity/images/ogp.jpg', quality=88)
print('ok')
```

Pillow未導入なら `pip install pillow`。元画像が低解像で1200pxに満たない場合は拡大せず原寸維持で保存し、高解像写真の提供後に作り直す。

- [ ] **Step 2: sitemap.xml / robots.txt を書く**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://sharkstars.jp/client/trinity/</loc></url>
  <url><loc>https://sharkstars.jp/client/trinity/works.html</loc></url>
  <url><loc>https://sharkstars.jp/client/trinity/lesson.html</loc></url>
  <url><loc>https://sharkstars.jp/client/trinity/privacy.html</loc></url>
</urlset>
```

```
User-agent: *
Allow: /
Sitemap: https://sharkstars.jp/client/trinity/sitemap.xml
```

- [ ] **Step 3: 機械チェック一式**

```bash
# 必須タグ：全4ページに canonical / og:image / viewport があるか
for f in index works lesson privacy; do
  echo "== $f"; for k in 'rel="canonical"' 'og:image' 'name="viewport"'; do
    grep -c "$k" client/trinity/$f.html; done; done
# 仮値の残存確認（意図した2種以外に仮値がないか）
grep -rn "TRINITY-TBD\|sharkstars.jp/client/trinity" client/trinity --include="*.html" | wc -l
```

Expected: 各ページ `1/1/1`（privacyはog:image無しでも可＝その場合期待値を調整）。仮値は「LINE URL」「プレビューURL」の2種のみ。

- [ ] **Step 4: リンク・画像切れ最終チェック**

```python
# 一時スクリプト：全ページの相対 src/href の実在確認
import re, os, glob
for f in glob.glob('client/trinity/*.html'):
    html = open(f, encoding='utf-8').read()
    for m in re.findall(r'(?:src|href)="([^"#][^":]*?)"', html):
        if not m.startswith(('http', 'tel:', 'mailto:')) and not os.path.exists(os.path.join('client/trinity', m)):
            print('MISSING', f, m)
print('done')
```

Expected: `done` のみ（MISSINGなし）

- [ ] **Step 5: 全ページブラウザ目視（モバイル幅含む）**

`python -m http.server 8000 -d client/trinity` で4ページを確認：
- ヒーローのクロスフェード／リビール動作／ハンバーガーメニュー開閉
- DevToolsで幅375pxにし、横スクロールが出ないこと・見出しの改行が破綻しないこと
- `prefers-reduced-motion` をエミュレートし演出が止まること

- [ ] **Step 6: Commit**

```bash
git add client/trinity
git commit -m "feat(trinity): OGP画像・sitemap・robots・最終検証"
```

---

## 公開時に行うこと（このプランのスコープ外・備忘）

1. クライアント確認13項目（スペック§10）の回答を反映（LINE URL・住所・料金・取材文・資格課程）
2. ドメイン確定 → 全HTML/sitemap/robotsの `https://sharkstars.jp/client/trinity/` を新ドメインへ一括置換、`noindex` メタ削除
3. `D:\本番環境更新用\trinity` へコピーしデプロイ（deployment_structure標準）
4. 高解像写真提供後：hero/work/ogp差し替え、`srcset`整備
5. グーペ解約はクライアント確認⑬のタイミングで（画像回収済みを確認してから）
