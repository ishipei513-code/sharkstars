# MARIN トップページ C3刷新 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** マリンケア訪問看護ステーションのトップページ（`client/marin/index.html`）を、濃紺×海×動き多めの「C3（深海）」デザインに全面刷新する（採用に強いトップ）。

**Architecture:** 静的HTML多ページ構成（ビルドツールなし）。トップだけ**専用の `css/top.css`＋`js/top.js`** で実装し、既存サブページ（service/company/contact/privacy）が使う **`css/style.css`（水色）は一切触らない**。`index.html` は `reset.css + top.css` のみを読み、`js/top.js` のみを読む。ヘッダー/フッター/JSON-LD/SEO/連絡先は既存 `index.html` のものを流用し、見た目だけC3化する。

**Tech Stack:** 素のHTML5 / CSS（CSS変数・`@keyframes`・IntersectionObserver連携クラス）/ バニラJS（カルーセル・カウントアップ・reveal・ハンバーガー・`prefers-reduced-motion`分岐）。テスト基盤は無いため**ブラウザ目視＋grepチェック**で検証する。

**Source of truth:**
- 設計書 spec：`docs/superpowers/specs/2026-06-20-marin-top-c3-redesign-design.md`
- 打合せメモ：`docs/clients/marin/トップページ-C3刷新-デザインメモ.md`
- 既存トップ（流用元の markup/連絡先/JSON-LD）：`client/marin/index.html`（水色版・本planで置換）

---

## 検証のしかた（全タスク共通）

自動テストは無い。各タスクの「Verify」は次の手順で行う：

1. リポジトリ直下でローカルサーバを起動（一度だけ）：
   `python -m http.server 8000`
2. ブラウザで `http://localhost:8000/client/marin/` を開く。
3. **DevTools Console にエラーが無い**ことを確認。
4. 各タスクの Expected（見えるもの／挙動）を目視確認。
5. モーション検証は DevTools の Rendering → "Emulate CSS prefers-reduced-motion" で `reduce` に切替えて再確認。
6. レスポンシブは DevTools のデバイスツールバーで 375px 幅を確認。

grepチェックは PowerShell では `Select-String`、bash では `grep` を使う（プロジェクトの検証用途のみ）。

---

## File Structure

| ファイル | 役割 | 操作 |
|---|---|---|
| `client/marin/index.html` | C3トップ本体（12ブロック）。header/footer/JSON-LD/SEOは流用 | **全面書き換え** |
| `client/marin/css/top.css` | C3トップ専用スタイル（トークン・base・header/footer・各セクション・`@keyframes`・`prefers-reduced-motion`） | **新規作成** |
| `client/marin/js/top.js` | カルーセル・カウントアップ・reveal・header scrolled・ハンバーガー・smooth-anchor・FAB・reduced-motion分岐 | **新規作成** |
| `client/marin/css/reset.css` | 既存リセット | 流用（変更なし） |
| `client/marin/css/style.css` | 水色＝**サブページ専用**。**触らない** | 変更禁止 |
| `client/marin/js/main.js` | 水色サブページ用。**触らない**（トップは top.js を使う） | 変更禁止 |
| `client/marin/images/*` | sea.jpg / vn.jpg / reha.jpg / feature.jpg / logo.svg / logo_white.svg / ogp.png は既存。カルーセルは vn/reha/feature を当面流用 | 流用 |

**命名方針：** 既存と同じクラス名（`.wrap` `.header` `.nav` `.menu-toggle` `.reveal`/`.is-in` `.footer` `.recruit-fab` `.btn`）は top.css でも踏襲し、JSロジックを再利用する。C3固有の見た目クラスは新規に足す。`.reveal`要素は表示時に `.is-in` が付く前提（top.jsが付与）。

**重要（行番号・DOM順）：** plan中の行番号は*元ファイル基準の目安*。**Task 3で旧`<main>`の全セクションを一括削除**した後、各セクションを **`</main>` の直前に順番に追加**して `<main>` を spec順に組み直す（タスクは番号順に実行する＝追加順がそのまま spec順になり、採用クラスター 06→07→08 が連続する）。編集箇所はセクションの**クラス名／コメント**で特定し、ドリフトする行番号には依存しないこと。

---

## Task 1: スキャフォールド（head差し替え・top.css土台・top.js土台）

**Files:**
- Modify: `client/marin/index.html`（`<head>` のCSS/JS参照と `<body>` を最小化）
- Create: `client/marin/css/top.css`
- Create: `client/marin/js/top.js`

- [ ] **Step 1: `top.css` にトークンとbaseを作成**

```css
/* マリンケア訪問看護ステーション — トップC3「深海」 Design System */
:root{
  /* C3 palette */
  --navy-0:#06182b;  /* 最深部 */
  --navy-1:#0a2540;  /* ベース濃紺 */
  --navy-2:#0a5a82;  /* 海の明るい青 */
  --sea:#3aa0c9;     /* 波・ゆらぎ */
  --pink:#ff5d8f;    /* アクセント（主軸） */
  --ink:#eaf4fb;     /* 濃紺上の本文 */
  --sub:#9fb6cc;     /* 補助テキスト */
  --card:#0c2236;    /* カード面 */
  --line:#1f3a58;    /* 罫線 */
  /* layout */
  --maxw:1120px;
  --gut:clamp(16px,4vw,40px);
  --header-h:64px;
  --radius:14px;
  /* type */
  --ff-jp:'Zen Kaku Gothic New','Zen Maru Gothic',system-ui,sans-serif;
  --ff-en:'Inter',sans-serif;
  /* accent override hook（オレンジA/B用・Task 12） */
}
html,body{overflow-x:hidden}
body{
  font-family:var(--ff-jp);
  color:var(--ink);
  background:var(--navy-1);
  line-height:1.85;
}
.wrap{max-width:var(--maxw);margin-inline:auto;padding-inline:var(--gut)}
img{max-width:100%;height:auto}
.label{font-size:11px;letter-spacing:.35em;color:var(--sea);font-family:var(--ff-en)}
.grad{color:var(--pink)}
.btn{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:13px 28px;font-weight:700;font-size:15px;text-decoration:none;transition:.18s}
.btn-primary{background:var(--pink);color:#fff;box-shadow:0 10px 28px rgba(255,93,143,.45)}
.btn-primary:hover{transform:translateY(-2px)}
.btn-ghost{border:1.5px solid var(--sea);color:var(--ink)}
.btn-ghost:hover{background:rgba(58,160,201,.14)}
/* reveal（top.jsが.is-inを付与） */
.reveal{opacity:0;transform:translateY(22px);transition:opacity .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.reveal.is-in{opacity:1;transform:none}
.reveal.d1{transition-delay:.08s}.reveal.d2{transition-delay:.20s}.reveal.d3{transition-delay:.32s}
```

- [ ] **Step 2: `top.css` の末尾に `@keyframes` と reduced-motion ガードを追加**

```css
/* ===== Motion keyframes ===== */
@keyframes seadrift{to{background-position:300px 0}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@keyframes drawline{to{width:100%}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes bob{0%,100%{transform:translate(-50%,0)}50%{transform:translate(-50%,6px)}}

/* ===== prefers-reduced-motion：動きを止め、即表示 ===== */
@media (prefers-reduced-motion: reduce){
  *,*::before,*::after{animation:none!important;transition:none!important}
  .reveal{opacity:1!important;transform:none!important}
}
```

- [ ] **Step 3: `top.js` のスケルトンを作成（IIFEで段階追加）**

```js
/* マリンケア訪問看護ステーション — トップC3 scripts */
(function(){
  'use strict';
  var REDUCED = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1) header scrolled
  var header=document.querySelector('.header');
  if(header){
    var onScroll=function(){ header.classList.toggle('is-scrolled', window.scrollY>20); };
    onScroll(); window.addEventListener('scroll',onScroll,{passive:true});
  }

  // 2) mobile menu
  var toggle=document.querySelector('.menu-toggle'), nav=document.querySelector('.nav');
  if(toggle&&nav){
    var closeNav=function(){nav.classList.remove('is-open');toggle.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');document.body.style.overflow='';};
    toggle.addEventListener('click',function(){
      var open=nav.classList.toggle('is-open');
      toggle.classList.toggle('is-open',open);
      toggle.setAttribute('aria-expanded',open?'true':'false');
      document.body.style.overflow=open?'hidden':'';
    });
    nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeNav);});
  }

  // 3) reveal on scroll（reduced時は即表示）
  var reveals=document.querySelectorAll('.reveal');
  if(REDUCED || !('IntersectionObserver' in window)){
    reveals.forEach(function(el){el.classList.add('is-in');});
  }else{
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);} });
    },{threshold:.12,rootMargin:'0px 0px -10% 0px'});
    reveals.forEach(function(el){io.observe(el);});
  }

  // 4) smooth anchor
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var id=a.getAttribute('href').slice(1); if(!id)return;
      var t=document.getElementById(id); if(!t)return;
      e.preventDefault(); t.scrollIntoView({behavior:REDUCED?'auto':'smooth',block:'start'});
    });
  });

  // 5) FAB ready
  var fab=document.getElementById('recruitFab'); if(fab)fab.classList.add('is-ready');

  // --- carousel/count-up は後続タスクでここに追加 ---
})();
```

- [ ] **Step 4: `index.html` の `<head>` を差し替え（CSS参照＋フォント）**

`client/marin/index.html` の以下2行：
```html
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/style.css">
```
を、`style.css` を外し top.css に変更：
```html
<link rel="stylesheet" href="css/reset.css">
<link rel="stylesheet" href="css/top.css">
```
同時にフォント `<link>`（line 24）を欧文Inter＋和文太ゴシックに更新：
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Zen+Kaku+Gothic+New:wght@500;700;900&family=Zen+Maru+Gothic:wght@500;700&display=swap" rel="stylesheet">
```
**変更しない**：`<meta robots noindex>`（line 6・公開前に別途削除）、title/description/keywords、canonical、OGP、Twitter、JSON-LD `@graph`（line 28-58）。

- [ ] **Step 5: `index.html` の末尾スクリプトを top.js に差し替え**

末尾（line 450）の `<script src="js/main.js"></script>` を：
```html
<script src="js/top.js" defer></script>
```

- [ ] **Step 6: Verify（土台が壊れていない）**

- `python -m http.server 8000` → `http://localhost:8000/client/marin/` を開く。
- Console エラー無し。背景が**濃紺**になっている（top.css適用の証拠）。
- grep確認（bash）：`grep -c 'css/style.css' client/marin/index.html` → **0**（サブ用CSSを読んでいない）／`grep -c 'css/top.css' client/marin/index.html` → 1。
- 既存サブページが無傷：`http://localhost:8000/client/marin/service.html` を開き、**従来の水色のまま**であることを確認（style.css/main.js 未変更）。

- [ ] **Step 7: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css client/marin/js/top.js
git commit -m "feat(marin-top): C3刷新の土台（top.css/top.js・head差し替え）"
```

---

## Task 2: ヘッダー（濃紺ナビ＋太いピンク下線＋ハンバーガー）

**Files:**
- Modify: `client/marin/index.html`（`<header>` は流用。`aria-current` を活かす）
- Modify: `client/marin/css/top.css`（header一式）

既存の `<header>` markup（line 63-75）はそのまま使える（logo.svg・nav・menu-toggle）。CSSだけC3化する。現在地リンク `トップ` には既に `aria-current="page"` が付いている。

- [ ] **Step 1: top.css に header スタイルを追加**

```css
.header{position:sticky;top:0;z-index:50;background:rgba(8,23,38,.72);-webkit-backdrop-filter:saturate(140%) blur(6px);backdrop-filter:saturate(140%) blur(6px);border-bottom:1px solid var(--line);transition:background .2s}
.header.is-scrolled{background:rgba(6,18,30,.92)}
/* backdrop-filter非対応/負荷回避：不透明背景にフォールバック（spec§4・モバイル罠メモ） */
@supports not ((backdrop-filter:blur(6px)) or (-webkit-backdrop-filter:blur(6px))){.header{background:rgba(6,18,30,.96)}}
.header .bar{display:flex;align-items:center;gap:18px;height:var(--header-h)}
.header .logo img{display:block;filter:brightness(0) invert(1)} /* 濃紺背景に白ロゴ */
.header .nav{margin-left:auto}
.header .nav ul{display:flex;align-items:center;gap:26px;list-style:none;margin:0;padding:0}
.header .nav a{color:var(--ink);text-decoration:none;font-size:14px;position:relative;padding:6px 0}
.header .nav a[aria-current="page"]::after{content:"";position:absolute;left:-2px;right:-2px;bottom:-6px;height:4px;background:var(--pink);border-radius:2px} /* 太いライン */
.header .nav .btn-line{background:var(--pink);color:#fff;padding:9px 18px;border-radius:999px}
.header .nav .btn-line::after{display:none}
.menu-toggle{display:none;margin-left:auto;width:42px;height:42px;background:none;border:0;flex-direction:column;justify-content:center;gap:5px;cursor:pointer}
.menu-toggle span{display:block;height:2px;background:var(--ink);transition:.2s}
@media (max-width:820px){
  .menu-toggle{display:flex}
  .header .nav{position:fixed;inset:var(--header-h) 0 auto 0;background:var(--navy-0);margin:0;max-height:0;overflow:hidden;transition:max-height .3s}
  .header .nav.is-open{max-height:80vh}
  .header .nav ul{flex-direction:column;align-items:stretch;gap:0;padding:8px var(--gut) 18px}
  .header .nav li{border-bottom:1px solid var(--line)}
  .header .nav a{display:block;padding:14px 0}
  .header .nav a[aria-current="page"]::after{left:0;right:auto;width:24px}
}
```

- [ ] **Step 2: Verify**

- デスクトップ：ナビ右寄せ、`トップ` の下に**太いピンク下線**、ロゴは白、スクロールで背景が濃くなる。
- 375px：ハンバーガーが出る → タップでメニュー開閉、`aria-expanded` が切替（DevTools Elements で確認）、開閉時に body スクロールロック。
- Console エラー無し。

- [ ] **Step 3: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): C3ヘッダー（濃紺ナビ・太い下線・ハンバーガー）"
```

---

## Task 3: ヒーロー（01）markup＋CSS（海ゆらぎ・重ね文字・見出しリビール）

**Files:**
- Modify: `client/marin/index.html`（`<section class="hero">` を置換）
- Modify: `client/marin/css/top.css`（hero一式）

カルーセルとカウントアップのJSは Task 4 で配線する。ここでは markup と静的CSS＋CSSアニメ（海・重ね文字・下線）まで。

- [ ] **Step 1: `index.html` のヒーロー（line 80-103）を以下に置換**

```html
<section class="hero" aria-label="メインビジュアル">
  <div class="hero-bg" style="background-image:url('images/sea.jpg')" aria-hidden="true"></div>
  <div class="hero-sea" aria-hidden="true"></div>
  <div class="hero-overlay" aria-hidden="true"></div>
  <div class="hero-ghost" aria-hidden="true"><b>NURSE</b></div>
  <div class="hero-ghost hero-ghost--2" aria-hidden="true"><b>+REHA</b></div>

  <div class="wrap hero-inner">
    <p class="hero-eyebrow reveal d1">RECRUIT &amp; CARE ／ 訪問看護ステーション</p>

    <div class="hero-carousel reveal d1" aria-label="マリンケアの風景">
      <div class="hero-carousel-track" id="heroTrack">
        <div class="hero-slide"><img src="images/vn.jpg" alt="ご自宅を訪問する看護師" width="1920" height="1280"></div>
        <div class="hero-slide"><img src="images/reha.jpg" alt="リハビリに寄り添うスタッフ" width="1920" height="1280"></div>
        <div class="hero-slide"><img src="images/feature.jpg" alt="ご家族とともに過ごすご利用者さま" width="1920" height="1280"></div>
        <div class="hero-slide"><img src="images/vn.jpg" alt="暮らしのそばで支える看護" width="1920" height="1280"></div>
      </div>
      <div class="hero-dots" id="heroDots" aria-hidden="true"></div>
    </div>

    <h1 class="hero-title">
      <span class="reveal d2">いのちの、</span><br>
      <span class="reveal d3">そばに<span class="key">。</span></span>
    </h1>
    <p class="hero-sub reveal d3">365日、いのちのそばで。</p>

    <div class="hero-cta reveal d3">
      <a class="btn btn-ghost" href="contact.html">ご相談はこちら</a>
      <a class="hero-entry" href="contact.html" aria-label="採用エントリー（LINEへ）">
        <svg viewBox="0 0 120 120" width="118" height="118" aria-hidden="true">
          <defs><path id="entryCirc" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs>
          <g class="hero-entry-ring"><text font-size="8.5" letter-spacing="3"><textPath href="#entryCirc">採用エントリー ・ ENTRY ・ 採用エントリー ・ ENTRY ・ </textPath></text></g>
          <circle class="hero-entry-bg" cx="60" cy="60" r="31"/>
          <text class="hero-entry-arrow" x="60" y="67" text-anchor="middle" font-size="20">→</text>
        </svg>
      </a>
    </div>
  </div>

  <div class="hero-scroll" aria-hidden="true">SCROLL ↓</div>
</section>
```

> ※ヒーロー見出しは spec §5 の通り主案「いのちの、そばに。」。別案「地域の看護を、私たちがつくる。」は実装前に確定（変更時はこの `<h1>` と `hero-sub` を差し替え）。動画素材取得後は `.hero-bg` を `<video>` ループに差し替え（reduced/低速時 sea.jpg 静止フォールバック）。

- [ ] **Step 1b: 旧 `<main>` の残りセクションを全削除（DOM順を spec順に組み直すため）**

新ヒーロー `</section>` の直後から `</main>` の直前までにある**旧セクションをすべて削除**する：`photostrip` / `philosophy` / `routes` / `biz` / `strengths` / `story` / `voices--user` / `insta` / `voices--staff` / `recruit`（cta-band） / `access`、および途中の `wave-divider` 2箇所。削除後、`<main>` の中身は**新ヒーロー1つだけ**になる。
以降の Task 5〜9 は各セクションを **`</main>` の直前に順番に追加**する（タスクを番号順に実行すれば 02→03→04→05→06→07→08→09→10→11 の spec順に並び、採用クラスター 06→07→08 が連続する）。この削除で旧 `photostrip`・旧 `story` の取り残しも同時に解消する。

- [ ] **Step 2: top.css にヒーロー静的CSS＋CSSアニメを追加**

```css
.hero{position:relative;min-height:88vh;display:flex;align-items:center;overflow:hidden;background:radial-gradient(130% 120% at 50% -15%,var(--navy-2),var(--navy-1) 58%,var(--navy-0))}
.hero-bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.28}
.hero-sea{position:absolute;inset:-20%;opacity:.16;background:repeating-linear-gradient(104deg,var(--sea) 0 2px,transparent 2px 30px);animation:seadrift 9s linear infinite}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,18,30,.25),rgba(6,18,30,.65))}
.hero-ghost{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;pointer-events:none}
.hero-ghost b{font-size:clamp(70px,16vw,170px);font-weight:900;color:transparent;-webkit-text-stroke:1.5px rgba(127,180,214,.16);font-family:var(--ff-en);animation:floatY 8s ease-in-out infinite}
.hero-ghost--2{justify-content:flex-end;align-items:flex-end}
.hero-ghost--2 b{font-size:clamp(36px,7vw,66px);-webkit-text-stroke:1px rgba(255,93,143,.20);margin:0 6vw 8vh 0;animation:floatY 6s ease-in-out infinite reverse}
.hero-inner{position:relative;z-index:3;text-align:center;padding-block:clamp(80px,12vh,140px)}
.hero-eyebrow{font-family:var(--ff-en);font-size:12px;letter-spacing:.3em;color:var(--sea)}
.hero-title{font-size:clamp(38px,9vw,84px);font-weight:900;line-height:1.3;color:#fff;margin:14px 0 6px;letter-spacing:.02em}
.hero-title .key{position:relative}
.hero-title .key::after{content:"";position:absolute;left:0;right:0;bottom:-4px;height:6px;width:0;background:var(--pink);border-radius:3px}
.hero-title .is-in .key::after,.hero-title .key.is-in::after{animation:drawline .7s ease forwards .4s}
.hero-sub{color:var(--pink);letter-spacing:.22em;font-size:clamp(12px,2.2vw,15px)}
.hero-cta{display:flex;align-items:center;justify-content:center;gap:22px;margin-top:30px;flex-wrap:wrap}
.hero-entry{display:inline-block;line-height:0}
.hero-entry-ring{transform-origin:60px 60px;animation:spin 13s linear infinite}
.hero-entry-ring text{fill:var(--ink)}
.hero-entry-bg{fill:var(--pink)}
.hero-entry-arrow{fill:#fff;font-weight:700}
.hero-entry:hover .hero-entry-ring{animation-duration:5s}
.hero-carousel{position:relative;width:min(340px,80vw);margin:22px auto 4px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.16);box-shadow:0 14px 40px rgba(0,0,0,.45);aspect-ratio:16/10}
.hero-carousel-track{display:flex;height:100%;transition:transform 1.3s cubic-bezier(.45,0,.18,1)}
.hero-slide{min-width:100%;height:100%}
.hero-slide img{width:100%;height:100%;object-fit:cover}
.hero-dots{position:absolute;bottom:8px;right:10px;display:flex;gap:5px}
.hero-dots span{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.45);transition:.35s}
.hero-dots span.on{background:var(--pink);width:15px;border-radius:3px}
.hero-scroll{position:absolute;left:50%;bottom:14px;z-index:3;transform:translateX(-50%);color:var(--sea);font-size:10px;letter-spacing:.2em;font-family:var(--ff-en);animation:bob 1.8s ease-in-out infinite}
```

> 注：`.hero-title .key::after` の起動は、その親 `.reveal` に `.is-in` が付いた時に走るよう、Task 4 で `span.reveal.d3` に `.is-in` 付与時のセレクタを保証する。上記 `.hero-title .is-in .key::after` がそれを担う。

- [ ] **Step 3: Verify**

- ヒーローが濃紺グラデ＋海ゆらぎ＋薄い重ね文字（NURSE / +REHA がふわり浮遊）。
- 見出し「いのちの、そばに。」が下から順に出て、「。」の下にピンク下線が伸びる。
- 中央に写真カルーセル（まだ自動では動かない＝Task 4で動かす。1枚目が見える）。
- 右の円形「採用エントリー」ボタンは円周文字が回転、ホバーで加速。`→` 中央。
- `SCROLL ↓` が下部で上下に揺れる。
- 375px：要素が縦に収まり、文字が画面外に溢れない。
- reduced-motion：海・浮遊・回転・下線・SCROLL揺れが**止まり**、見出しは即表示。

- [ ] **Step 4: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): C3ヒーロー（海ゆらぎ・重ね文字・見出しリビール・回るエントリー）"
```

---

## Task 4: top.js にカルーセル＋カウントアップを配線（reduced-motion対応）

**Files:**
- Modify: `client/marin/js/top.js`（Task 1 の「後続タスクでここに追加」コメント箇所）

カウントアップは Task 7 の数字セクションでも使うため、汎用に `[data-countup]` を走査する形で先に実装する。

- [ ] **Step 1: top.js の末尾コメント箇所に carousel と count-up を追加**

Task 1 の `// --- carousel/count-up は後続タスクでここに追加 ---` を以下に置換：

```js
  // 6) hero carousel（reduced時は1枚目固定）
  var track=document.getElementById('heroTrack'), dotsEl=document.getElementById('heroDots');
  if(track){
    var n=track.children.length, i=0, dots=[];
    if(dotsEl){ for(var k=0;k<n;k++){var s=document.createElement('span');if(k===0)s.className='on';dotsEl.appendChild(s);dots.push(s);} }
    if(!REDUCED && n>1){
      setInterval(function(){
        i=(i+1)%n;
        track.style.transform='translateX(-'+(i*100)+'%)';
        dots.forEach(function(d,j){d.className=(j===i)?'on':'';});
      },3000);
    }
  }

  // 7) count-up（数字セクション等。reduced時は即・最終値）
  function easeOutCubic(p){return 1-Math.pow(1-p,3);}
  function countEl(el){
    var end=parseFloat(el.getAttribute('data-countup'));
    var unit=el.getAttribute('data-unit')||'';
    if(REDUCED){ el.textContent=end+unit; return; }
    var t0=null,dur=1300;
    function step(ts){ if(!t0)t0=ts; var p=Math.min((ts-t0)/dur,1); el.textContent=Math.round(end*easeOutCubic(p))+unit; if(p<1)requestAnimationFrame(step); }
    el.textContent='0'+unit; requestAnimationFrame(step);
  }
  var counters=document.querySelectorAll('[data-countup]');
  if(counters.length){
    if(REDUCED || !('IntersectionObserver' in window)){
      counters.forEach(countEl);
    }else{
      var cio=new IntersectionObserver(function(entries){
        entries.forEach(function(e){ if(e.isIntersecting){countEl(e.target);cio.unobserve(e.target);} });
      },{threshold:.4});
      counters.forEach(function(el){cio.observe(el);});
    }
  }
```

- [ ] **Step 2: Verify**

- ヒーローのカルーセルが約3秒ごとに横スライドし、ピンクのドットが現在地を示す。
- Console エラー無し。
- reduced-motion：カルーセルは1枚目で停止（自動送りなし）。
- （数字は Task 7 で見た目確認。ここでは Console エラーが無ければOK。）

- [ ] **Step 3: Commit**

```bash
git add client/marin/js/top.js
git commit -m "feat(marin-top): カルーセル自動送り＋汎用カウントアップ（reduced-motion対応）"
```

---

## Task 5: ブロック02 理念 ＋ 03 3つの入口

**Files:**
- Modify: `client/marin/index.html`（02理念・03入口を `</main>` 直前に追加。旧mainはTask3で削除済み）
- Modify: `client/marin/css/top.css`

既存の理念テキストはそのまま流用（コピーは確定済み）。3つの入口は spec §6 のリンク先（①service ②採用クラスター#numbers ③company）に確定する。

- [ ] **Step 1: 理念（02）を `</main>` 直前に追加**

以下を `</main>` の直前に追加：
```html
<section class="philosophy" aria-labelledby="philosophy-title">
  <div class="wrap">
    <p class="label reveal">理念 / PHILOSOPHY</p>
    <h2 class="phi-title reveal d1" id="philosophy-title">あなたの物語を大切に。<br><span class="phi-key">その〝人〟らしく生きるを看る。</span></h2>
    <p class="phi-body reveal d2">人生という物語の主人公であるあなたが大切にしてきた生き方を尊重し、最期まで共に寄り添います。『自分らしく生きたい』と願うあなたやご家族に、訪問看護の限界を一歩越えた希望ある選択肢をご提供いたします。</p>
  </div>
</section>
```

- [ ] **Step 2: 3つの入口（03）を `</main>` 直前に追加**

02 の直後（＝`</main>` の直前）に以下を追加：
```html
<section class="routes" aria-label="ご覧の方別のご案内">
  <div class="wrap route-grid">
    <a class="route-card reveal d1" href="service.html">
      <span class="route-ic" aria-hidden="true">♡</span>
      <h3>利用者・ご家族の方へ</h3>
      <p>訪問看護でできること、ご利用までの流れをご案内します。</p>
      <span class="route-go">くわしく見る →</span>
    </a>
    <a class="route-card route-card--job reveal d2" href="#numbers">
      <span class="route-ic" aria-hidden="true">＋</span>
      <h3>採用をお考えの方へ</h3>
      <p>一緒に地域の看護をつくる仲間を募集中。働く環境を見る。</p>
      <span class="route-go">採用情報へ ↓</span>
    </a>
    <a class="route-card reveal d3" href="company.html">
      <span class="route-ic" aria-hidden="true">✦</span>
      <h3>連携先の医療・介護の方へ</h3>
      <p>多職種で地域を支える連携先を歓迎いたします。</p>
      <span class="route-go">会社概要を見る →</span>
    </a>
  </div>
</section>
```
> ②のリンク先 `#numbers` は Task 7 の採用数字セクションの `id`。**ダミーリンクにしないこと**（実在アンカーへ）。

- [ ] **Step 3: top.css に 02/03 のスタイルを追加**

```css
/* 02 philosophy */
.philosophy{padding:clamp(70px,10vw,120px) 0;text-align:center}
.phi-title{font-size:clamp(22px,4.4vw,38px);font-weight:900;color:#fff;line-height:1.7;margin:10px 0 22px}
.phi-key{position:relative;display:inline-block}
.phi-key::after{content:"";position:absolute;left:0;right:0;bottom:-4px;height:4px;background:linear-gradient(90deg,var(--sea),var(--pink));border-radius:2px}
.phi-body{max-width:720px;margin-inline:auto;color:var(--sub)}
/* 03 routes */
.route-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding-bottom:clamp(40px,6vw,80px)}
.route-card{display:block;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:26px 22px;text-decoration:none;color:var(--ink);transition:.18s}
.route-card:hover{transform:translateY(-4px);border-color:var(--sea)}
.route-card--job{border-left:4px solid var(--pink);background:linear-gradient(90deg,rgba(255,93,143,.10),var(--card) 42%)}
.route-ic{font-size:26px;color:var(--pink)}
.route-card h3{font-size:16px;color:#fff;margin:10px 0 6px}
.route-card p{font-size:13px;color:var(--sub);line-height:1.7}
.route-go{display:inline-block;margin-top:12px;font-size:13px;color:var(--sea)}
@media (max-width:760px){.route-grid{grid-template-columns:1fr}}
```

- [ ] **Step 4: Verify**

- 02：理念見出しの下にグラデ下線、スクロールでフェードイン。
- 03：3カードが横並び（375pxで縦積み）。中央「採用」カードはピンクの左ボーダー＆淡いピンク背景。
- 「採用をお考えの方へ」クリック → ページ内を採用数字へスムーススクロール（Task 7後に最終確認。今は `#numbers` が無いので動かなくてOK＝Console警告も出ない実装）。
- ①→service.html ③→company.html に実際に遷移する。

- [ ] **Step 5: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): 02理念・03三つの入口（採用は#numbersへアンカー）"
```

---

## Task 6: ブロック04 事業内容（看護＋リハ）＋ 05 選ばれる理由・体制

**Files:**
- Modify: `client/marin/index.html`（04事業内容・05選ばれる理由を `</main>` 直前に順に追加。旧mainはTask3で削除済み）
- Modify: `client/marin/css/top.css`

既存の看護/リハ項目・強み3項目のテキストは流用。

- [ ] **Step 1: 04 事業内容 を `</main>` 直前に追加**（既存の項目テキストを流用）

```html
<section class="biz" aria-labelledby="biz-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">WHAT WE DO</p><h2 id="biz-title">事業内容・<span class="grad">できること</span></h2></div>
    <div class="biz-grid">
      <div class="biz-col reveal d1 from-left">
        <h3><span aria-hidden="true">🩺</span> 訪問看護</h3>
        <ul><li>健康観察・バイタルチェック</li><li>服薬管理・栄養管理</li><li>点滴・注射・医師の指示による医療行為</li><li>小児看護</li><li>疼痛緩和・ターミナルケア</li></ul>
      </div>
      <div class="biz-col reveal d2 from-right">
        <h3><span aria-hidden="true">🌿</span> リハビリ</h3>
        <ul><li>運動機能の回復・維持</li><li>ADL向上・廃用症候群の予防</li><li>呼吸器・心臓リハビリ</li><li>難病の進行予防</li><li>福祉用具の調整</li></ul>
      </div>
    </div>
    <p class="biz-meta reveal">対象＝赤ちゃん〜高齢の方まで／対応エリア＝福岡市全域</p>
    <div class="biz-cta reveal"><a class="btn btn-primary" href="service.html">サービスを詳しく見る →</a></div>
  </div>
</section>
```

- [ ] **Step 2: 05 選ばれる理由 を `</main>` 直前に追加**（強み3項目テキスト流用。04の直後）

```html
<section class="strengths" aria-labelledby="strengths-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">OUR STRENGTHS</p><h2 id="strengths-title">マリンケアが<span class="grad">選ばれる理由</span></h2></div>
    <div class="strength-grid">
      <div class="strength-item reveal d1"><div class="strength-no">01</div><h3>24時間365日対応</h3><p>緊急時もご連絡いただけます。夜間・休日も、暮らしのそばで備えています。</p></div>
      <div class="strength-item reveal d2"><div class="strength-no">02</div><h3>看護＋リハの多職種連携</h3><p>一人ひとりに最適なケアを多職種で。医療と暮らしのあいだをつなぎます。</p></div>
      <div class="strength-item reveal d3"><div class="strength-no">03</div><h3>小児〜難病・終末期対応</h3><p>幅広いステージのご利用者さまに寄り添います。</p></div>
    </div>
  </div>
</section>
```
（旧 `wave-divider` は Task 3 の一括削除で既に除去済み。追加不要。）

- [ ] **Step 3: top.css に 04/05 ＋ sec-head 共通＋ from-left/right を追加**

```css
.sec-head{text-align:center;margin-bottom:34px}
.sec-head h2{font-size:clamp(24px,4.6vw,40px);font-weight:900;color:#fff;margin-top:6px}
.biz{padding:clamp(60px,9vw,110px) 0}
.biz-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.biz-col{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px 26px}
.biz-col h3{font-size:20px;color:#fff;margin-bottom:14px}
.biz-col ul{list-style:none;margin:0;padding:0}
.biz-col li{padding:8px 0 8px 22px;position:relative;color:var(--sub);border-bottom:1px dashed var(--line)}
.biz-col li::before{content:"›";position:absolute;left:4px;color:var(--pink)}
.biz-meta{text-align:center;color:var(--sub);margin:22px 0;font-size:14px}
.biz-cta{text-align:center}
.strengths{padding:clamp(60px,9vw,110px) 0}
.strength-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.strength-item{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:26px 22px;text-align:center}
.strength-no{font-family:var(--ff-en);font-size:30px;font-weight:800;color:var(--pink)}
.strength-item h3{color:#fff;font-size:17px;margin:8px 0}
.strength-item p{color:var(--sub);font-size:13px;line-height:1.8}
/* スクロールで左右からスライドイン */
.from-left{transform:translateX(-40px)}.from-right{transform:translateX(40px)}
.from-left.is-in,.from-right.is-in{transform:none}
@media (max-width:760px){.biz-grid{grid-template-columns:1fr}.strength-grid{grid-template-columns:1fr}}
```

- [ ] **Step 4: Verify**

- 04：2カラム（看護/リハ）が左右からスライドイン（375pxで縦積み）。
- 05：強み3枚に大きな番号、フェードイン。
- 旧wave-divider（水色の波）が消えている。
- reduced-motion：スライドが即表示。

- [ ] **Step 5: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): 04事業内容・05選ばれる理由（左右スライドイン）"
```

---

## Task 7: ブロック06 採用の数字（4つ・カウントアップ）

**Files:**
- Modify: `client/marin/index.html`（採用ゾーンの起点。06数字を `</main>` 直前に追加＝05の直後）
- Modify: `client/marin/css/top.css`

数字は spec §7 の4つ：男女比率（割合バー）・月平均残業（◯h）・年間休日（◯日）・平均年齢（◯歳）。**全て仮値**で `data-countup` を埋め、`<!-- 仮 -->` を明示。`id="numbers"` を付け Task 5 の②アンカー先にする。

- [ ] **Step 1: numbers セクション markup を `</main>` 直前に追加**（05の直後）

```html
<!-- ===== 06【採用】働く環境の数字（4つ・全て仮値→西社長から実数差し替え） ===== -->
<section id="numbers" class="numbers" aria-labelledby="numbers-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">DATA</p><h2 id="numbers-title">働く環境を、<span class="grad">数字で。</span></h2></div>
    <div class="num-grid">
      <div class="num-card reveal d1"><span class="num-tag">仮</span>
        <div class="num-ratio"><span class="num-ratio-f" style="width:20%"></span></div>
        <div class="num-big"><span data-countup="2" data-unit="">0</span>：<span data-countup="8" data-unit="">0</span></div>
        <p class="num-lab">男女比率（男：女）</p>
      </div>
      <div class="num-card reveal d2"><span class="num-tag">仮</span>
        <div class="num-big"><span data-countup="4" data-unit="">0</span><i>h</i></div>
        <p class="num-lab">月平均残業</p>
      </div>
      <div class="num-card reveal d3"><span class="num-tag">仮</span>
        <div class="num-big"><span data-countup="120" data-unit="">0</span><i>日</i></div>
        <p class="num-lab">年間休日</p>
      </div>
      <div class="num-card reveal d3"><span class="num-tag">仮</span>
        <div class="num-big"><span data-countup="38" data-unit="">0</span><i>歳</i></div>
        <p class="num-lab">平均年齢</p>
      </div>
    </div>
    <p class="num-note">※数値はすべて仮です。公開前に実数へ差し替えます。</p>
  </div>
</section>
```

- [ ] **Step 2: top.css に numbers スタイルを追加**

```css
.numbers{padding:clamp(64px,9vw,120px) 0;background:radial-gradient(120% 140% at 50% -10%,#0e3756,var(--navy-1) 60%,var(--navy-0))}
.num-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.num-card{position:relative;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:24px 18px;text-align:center}
.num-tag{position:absolute;top:8px;right:10px;font-size:9px;color:#5f7d97;letter-spacing:.1em}
.num-big{font-size:clamp(34px,5vw,46px);font-weight:900;color:#fff;line-height:1}
.num-big i{font-style:normal;font-size:18px;color:var(--pink);margin-left:2px}
.num-lab{margin-top:10px;font-size:12px;color:var(--sub);letter-spacing:.05em}
.num-ratio{height:6px;border-radius:3px;background:#15314e;overflow:hidden;margin-bottom:14px}
.num-ratio-f{display:block;height:100%;background:linear-gradient(90deg,var(--sea),var(--pink))}
.num-note{text-align:center;color:#5f7d97;font-size:11px;margin-top:16px}
@media (max-width:760px){.num-grid{grid-template-columns:1fr 1fr}}
```

- [ ] **Step 3: Verify**

- スクロールでカードが現れた瞬間に4つの数字が0からカウントアップ（男女比率は「2：8」、残業4h、年間休日120日、平均年齢38歳）。
- 各カードに「仮」タグ、下に注記。
- Task 5 の「採用をお考えの方へ」をクリック → このセクションへスムーススクロールする（`#numbers` が存在するので機能する）。
- reduced-motion：数字は即・最終値。
- 375px：2×2グリッド。

- [ ] **Step 4: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): 06採用の数字4つ（カウントアップ・#numbersアンカー）"
```

---

## Task 8: ブロック07 スタッフの声・一日 ＋ 08 採用CTA（→LINE / Indeed）

**Files:**
- Modify: `client/marin/index.html`（07スタッフの声・08採用CTAを `</main>` 直前に順に追加＝06の直後。これで採用クラスター06→07→08が連続する）
- Modify: `client/marin/css/top.css`

採用クラスターの締め。CTAは spec §8：エントリー→**公式LINE**（当面プレースホルダーURL）＋ **Indeed求人リンク**（プレースホルダー）。
> ※spec ブロック07は「スタッフの声・**一日の流れ**」。本タスクでは**スタッフの声（2枚）を実装**し、**「一日の流れ」タイムラインは次パスに延期**（実コンテンツ取得後）。spec との差分として明記。

- [ ] **Step 1: 07 スタッフの声 を `</main>` 直前に追加**（06の直後・既存仮コメント流用）

```html
<section class="staff" aria-labelledby="staff-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">VOICE / STAFF</p><h2 id="staff-title">はたらく人の声</h2></div>
    <!-- TODO: 実コメント未取得。公開前に差し替え -->
    <div class="staff-grid">
      <figure class="staff-card reveal d1"><img src="images/vn.jpg" alt="看護師スタッフ" loading="lazy" width="1920" height="1280"><figcaption><blockquote>チームがあたたかく、困ったときはすぐ相談できます。看護とリハが連携しているので一人で抱え込まずに働けます。</blockquote><span>看護師</span></figcaption></figure>
      <figure class="staff-card reveal d2"><img src="images/reha.jpg" alt="リハビリスタッフ" loading="lazy" width="1920" height="1280"><figcaption><blockquote>ライフスタイルに合わせて働けて、家庭と両立できています。利用者さまの「ありがとう」が毎日のやりがいです。</blockquote><span>リハビリスタッフ</span></figcaption></figure>
    </div>
  </div>
</section>
```

- [ ] **Step 2: 08 採用CTA を `</main>` 直前に追加**（07の直後）

```html
<section id="recruit" class="recruit" aria-labelledby="recruit-title">
  <div class="recruit-sea" aria-hidden="true"></div>
  <div class="wrap recruit-inner reveal">
    <p class="label">RECRUIT</p>
    <h2 class="recruit-title" id="recruit-title">一緒に、地域の看護を<br>つくりませんか。</h2>
    <p class="recruit-body">正看護師さん（パート・アルバイト）を募集中。未経験歓迎、同行訪問・無料の見学体験あり。</p>
    <div class="recruit-cta">
      <!-- TODO: 公式LINEの友だち追加URLに差し替え（現状プレースホルダー） -->
      <a class="btn btn-primary" href="https://line.me/" target="_blank" rel="noopener noreferrer">LINEで応募・相談する</a>
      <!-- TODO: Indeed求人ページURLに差し替え -->
      <a class="btn btn-ghost" href="https://jp.indeed.com/" target="_blank" rel="noopener noreferrer">Indeedで求人を見る</a>
    </div>
  </div>
</section>
```

- [ ] **Step 3: top.css に 07/08 スタイルを追加**

```css
.staff{padding:clamp(60px,9vw,110px) 0}
.staff-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.staff-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;margin:0}
.staff-card img{width:100%;height:200px;object-fit:cover}
.staff-card figcaption{padding:20px}
.staff-card blockquote{margin:0 0 10px;color:var(--ink);font-size:14px;line-height:1.9}
.staff-card span{color:var(--pink);font-size:12px;font-weight:700}
.recruit{position:relative;overflow:hidden;padding:clamp(70px,11vw,140px) 0;text-align:center;background:radial-gradient(120% 130% at 50% 0%,var(--navy-2),var(--navy-0))}
.recruit-sea{position:absolute;inset:-20%;opacity:.16;background:repeating-linear-gradient(104deg,var(--sea) 0 2px,transparent 2px 30px);animation:seadrift 9s linear infinite}
.recruit-inner{position:relative;z-index:2}
.recruit-title{font-size:clamp(26px,5.2vw,46px);font-weight:900;color:#fff;line-height:1.5;margin:10px 0 14px}
.recruit-body{color:var(--sub);max-width:560px;margin:0 auto 26px}
.recruit-cta{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
@media (max-width:760px){.staff-grid{grid-template-columns:1fr}}
```

- [ ] **Step 4: Verify**

- 07：スタッフ2枚（写真＋コメント）。375pxで縦積み。
- 08：濃紺グラデ＋海ゆらぎ背景、見出し、CTA2本（LINE＝ピンク塗り／Indeed＝ゴースト）。両方 `target=_blank rel=noopener`。
- LINE/Indeed のリンクは**プレースホルダーURL**だが実在ドメイン（リンク切れにしない）。
- reduced-motion：背景の海が止まる。

- [ ] **Step 5: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): 07スタッフの声・08採用CTA（LINE/Indeed導線）"
```

---

## Task 9: ブロック09 利用者の声 ＋ 10 Instagram ＋ 11 アクセス（＋旧storyの除去）

**Files:**
- Modify: `client/marin/index.html`（09利用者の声・10Instagram・11アクセスを `</main>` 直前に順に追加＝08の直後。旧 story 等は Task 3 で削除済み）
- Modify: `client/marin/css/top.css`

- [ ] **Step 1: （旧 story 等は Task 3 で削除済み）09/10/11 を順に `</main>` 直前へ追加していく**

- [ ] **Step 2: 09 利用者の声 を `</main>` 直前に追加**（08の直後・既存仮コメント流用）

```html
<section class="voices" aria-labelledby="voice-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">VOICE / FAMILY</p><h2 id="voice-title">利用者・ご家族の声</h2></div>
    <!-- TODO: 実コメント未取得。公開前に差し替え -->
    <div class="voice-grid">
      <figure class="voice-card reveal d1"><span class="voice-mark" aria-hidden="true">“</span><blockquote>夜間も相談できる体制があり、安心して任せられました。住み慣れた家で家族と過ごせたことに感謝しています。</blockquote><figcaption>ご家族</figcaption></figure>
      <figure class="voice-card reveal d2"><span class="voice-mark" aria-hidden="true">“</span><blockquote>いつもやさしく声をかけてくださって、訪問の時間が楽しみになりました。一人ひとりに寄り添ってくれるのが伝わります。</blockquote><figcaption>ご利用者さま</figcaption></figure>
    </div>
  </div>
</section>
```

- [ ] **Step 3: 10 Instagram を `</main>` 直前に追加**（09の直後・プレースホルダーグリッド＋ウィジェット差し替え前提）

```html
<section class="insta" aria-labelledby="insta-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">INSTAGRAM</p><h2 id="insta-title">日々の<span class="grad">あたたかい風景</span></h2></div>
    <!-- TODO: 自動更新ウィジェット（SnapWidget/LightWidget/Behold等）の埋め込みに差し替え。下のグリッドは設置後に削除 -->
    <div class="insta-grid reveal" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span></div>
    <div class="insta-cta reveal"><!-- TODO: 正式IG URLに差し替え --><a class="btn btn-ghost" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">＠marin で最新を見る →</a></div>
  </div>
</section>
```

- [ ] **Step 4: 11 アクセス を `</main>` 直前に追加**（10の直後・既存の連絡先・地図・住所コメントを流用）

```html
<section class="access" aria-labelledby="access-title">
  <div class="wrap">
    <div class="sec-head reveal"><p class="label">ACCESS</p><h2 id="access-title">事業所情報・アクセス</h2></div>
    <div class="access-grid reveal">
      <div class="access-info">
        <!-- 公開前確認：住所は契約書=板倉。移行元=飯倉。西社長にLINEで正式表記を確認 -->
        <dl class="info-list">
          <div><dt>名称</dt><dd>マリンケア訪問看護ステーション</dd></div>
          <div><dt>住所</dt><dd>〒814-0134 福岡県福岡市城南区板倉1-5-35</dd></div>
          <div><dt>TEL</dt><dd><a href="tel:0924001821">092-400-1821</a></dd></div>
          <div><dt>FAX</dt><dd>092-400-1831</dd></div>
          <div><dt>LINE</dt><dd><a href="contact.html">LINEで相談する</a></dd></div>
          <div><dt>対応エリア</dt><dd>福岡市全域（拠点＝城南区）</dd></div>
          <div><dt>営業</dt><dd>24時間365日 緊急対応</dd></div>
        </dl>
        <a class="btn btn-primary" href="contact.html">お問い合わせはこちら</a>
      </div>
      <div class="access-map">
        <iframe src="https://maps.google.com/maps?q=福岡県福岡市城南区板倉1-5-35&output=embed" title="マリンケア訪問看護ステーションの地図" loading="lazy" referrerpolicy="no-referrer-when-downgrade" width="100%" height="100%" style="border:0"></iframe>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 5: top.css に 09/10/11 スタイルを追加**

```css
.voices{padding:clamp(60px,9vw,110px) 0}
.voice-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.voice-card{position:relative;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px 24px;margin:0}
.voice-mark{position:absolute;top:8px;left:14px;font-size:40px;color:rgba(255,93,143,.4);font-family:Georgia,serif}
.voice-card blockquote{margin:10px 0 8px;color:var(--ink);line-height:1.9}
.voice-card figcaption{color:var(--sub);font-size:13px}
.insta{padding:clamp(60px,9vw,110px) 0}
.insta-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}
.insta-grid span{aspect-ratio:1;background:linear-gradient(160deg,#13405f,#0c2a40);border-radius:8px}
.insta-cta{text-align:center;margin-top:22px}
.access{padding:clamp(60px,9vw,110px) 0}
.access-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.access-info,.access-map{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:26px;overflow:hidden}
.access-map{padding:0;min-height:320px}
.access-map iframe{display:block;height:100%;min-height:320px}
.info-list div{display:flex;gap:14px;padding:9px 0;border-bottom:1px dashed var(--line)}
.info-list dt{flex:none;width:80px;color:var(--sea);font-size:13px}
.info-list dd{color:var(--ink);font-size:14px}
.info-list a{color:var(--ink)}
.access-info .btn{margin-top:18px}
@media (max-width:760px){.voice-grid,.insta-grid{grid-template-columns:1fr 1fr}.access-grid{grid-template-columns:1fr}}
```

- [ ] **Step 6: Verify**

- 旧storyブロックが無い（重複なし）。
- 09 利用者の声2枚、10 Instagramプレースホルダー6枚（濃紺タイル）、11 アクセス（情報＋地図）。
- 地図が表示され、住所アンカーが正しい。
- 375px：それぞれ崩れず縦に収まる。

- [ ] **Step 7: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): 09利用者の声・10Instagram・11アクセス＋旧story除去"
```

---

## Task 10: フッター＋追従FAB の C3化、全体通し確認

**Files:**
- Modify: `client/marin/index.html`（footer(line 428) と recruit-fab(line 441) は流用。FABのリンク先を `#numbers` か `#recruit` に）
- Modify: `client/marin/css/top.css`

既存 footer / recruit-fab の markup は流用可。FABの `href="#recruit"` は採用CTA(08)へ飛ぶので維持。色だけC3化。

- [ ] **Step 1: top.css に footer ＋ FAB スタイルを追加**

```css
.footer{background:var(--navy-0);border-top:1px solid var(--line);padding:48px 0 60px;text-align:center;color:var(--sub)}
.footer img{height:38px;width:auto;margin-bottom:14px;filter:brightness(0) invert(1);opacity:.9}
.footer p{font-size:13px;line-height:1.9}
.footer a{color:var(--ink)}
.footer nav{margin-top:16px;display:flex;gap:18px;flex-wrap:wrap;justify-content:center}
.footer nav a{font-size:13px;color:var(--sub)}
.recruit-fab{position:fixed;right:14px;bottom:16px;z-index:60;opacity:0;transform:translateY(10px);transition:.3s}
.recruit-fab.is-ready{opacity:1;transform:none}
.recruit-fab.is-nav-open{opacity:0;pointer-events:none}
.recruit-fab-btn{display:flex;flex-direction:column;align-items:center;gap:2px;background:var(--pink);color:#fff;text-decoration:none;border-radius:14px;padding:10px 12px;box-shadow:0 10px 26px rgba(255,93,143,.5);font-size:11px;font-weight:700;line-height:1.3}
```
> 既存 footer の `logo_white.svg` はそのまま使える（FAB markupも流用）。footer内の `style=""` インライン（line 430,434,437）は残ってよい。

- [ ] **Step 2: FAB の遷移先を確認**（既存 `href="#recruit"` のままでよい。`#recruit` は Task 8 の採用CTA id）。`smooth-anchor` で採用CTAへスクロールする。

- [ ] **Step 3: Verify（全体通し）**

- 上から下まで通しスクロール：01〜12が spec の順で並ぶ（01ヒーロー→02理念→03入口→04事業→05強み→06数字→07スタッフ→08採用CTA→09利用者声→10IG→11アクセス→12フッター）。
- 追従FAB「求職者はコチラ」が右下に常時表示、タップで採用CTAへ。モバイルメニュー開時は隠れる。
- Console エラー無し。

- [ ] **Step 4: Commit**

```bash
git add client/marin/index.html client/marin/css/top.css
git commit -m "feat(marin-top): フッター・追従FABのC3化＋全体通し"
```

---

## Task 11: 仕上げチェック（モバイル／reduced-motion／リンク／SEO／サブページ無傷）

**Files:**
- Modify: 必要に応じて `client/marin/index.html` / `client/marin/css/top.css`（不具合修正のみ）

- [ ] **Step 1: リンク健全性（ダミー禁止）**

bash で確認：
```bash
grep -nE 'href="#' client/marin/index.html
```
Expected：`#numbers`（03②）と `#recruit`（FAB）のみ。両アンカー id が本文に存在することを目視確認（`id="numbers"` `id="recruit"`）。`href="#"` 単体や存在しないアンカーが**無い**こと。

- [ ] **Step 1b: セクション順＝spec順を検証（採用クラスター連続性）**

`<main>` 内の `<section>` を上から読み、順序が **hero → 02理念(philosophy) → 03入口(routes) → 04事業(biz) → 05強み(strengths) → 06数字(numbers) → 07スタッフ(staff) → 08採用CTA(recruit) → 09利用者声(voices) → 10IG(insta) → 11アクセス(access)** であることを確認。とくに **06(numbers)→07(staff)→08(recruit) が連続**していること。旧 `photostrip`・旧 `story` が**残っていない**こと（`grep -c 'class="photostrip"' client/marin/index.html` → 0、`grep -c 'class="story"' client/marin/index.html` → 0）。

- [ ] **Step 2: SEO/構造化データ無傷**

```bash
grep -c 'application/ld+json' client/marin/index.html   # → 1
grep -c 'noindex' client/marin/index.html               # → 1（プレビュー維持）
grep -c 'canonical' client/marin/index.html             # → 1
```
title/description/keywords/OGP/Twitter が Task 1 以降変わっていないこと（headを目視）。

- [ ] **Step 3: サブページが無傷**

```bash
git status --porcelain client/marin/css/style.css client/marin/js/main.js
```
Expected：**出力なし**（両ファイル未変更）。ブラウザで service.html / company.html / contact.html / privacy.html を開き、**従来の水色のまま**であることを確認。

- [ ] **Step 4: reduced-motion 全面確認**

DevTools で `prefers-reduced-motion: reduce` をエミュレート → 海ゆらぎ・重ね文字浮遊・回転ボタン・カルーセル自動送り・SCROLL揺れ・reveal が**全て静止/即表示**、数字は最終値。レイアウト崩れなし。

- [ ] **Step 5: モバイル 375px / 414px 確認**

ヒーロー文字が溢れない、各グリッドが縦/2列に落ちる、横スクロールが出ない（`overflow-x:hidden` 効いている）、FABが内容に被って操作を妨げない。

- [ ] **Step 6: 不具合があれば修正してコミット**

```bash
git add -A client/marin/
git commit -m "fix(marin-top): 仕上げ（リンク/SEO/reduced-motion/モバイル）"
```
（修正不要ならコミット省略）

---

## Task 12: オレンジ・アクセント版ヒーロー（A/B比較用）

**Files:**
- Modify: `client/marin/css/top.css`（末尾にテーマ上書きを追加）
- Create: なし（クラス切替で実現）

spec §2 の通り、ピンク主軸に対し**オレンジ版をA/Bできるように**する。`<html>` か `<body>` に `class="accent-orange"` を付けると全アクセントがオレンジになる、という最小の仕組みにする（本番はピンクのまま。比較時だけクラスを付ける）。

- [ ] **Step 1: top.css 末尾にオレンジ上書きを追加**

```css
/* ===== オレンジ・アクセントA/B（body.accent-orange で全アクセント差し替え） ===== */
body.accent-orange{--pink:#ff8a3d}
body.accent-orange .btn-primary{box-shadow:0 10px 28px rgba(255,138,61,.45)}
body.accent-orange .recruit-fab-btn{box-shadow:0 10px 26px rgba(255,138,61,.5)}
```
> `--pink` 変数を全箇所で参照しているため、これだけでヒーロー下線・回るボタン・採用カード・数字・CTA・FABのアクセントが一括でオレンジになる。

- [ ] **Step 2: Verify（比較）**

- DevTools の Console で `document.body.classList.add('accent-orange')` を実行 → ピンクだった箇所が**すべてオレンジ**に変わることを確認（ヒーロー下線・エントリーボタン・03採用カード・06数字単位・08CTA・FAB）。
- `document.body.classList.remove('accent-orange')` で元に戻る。
- **本番の `index.html` には付与しない**（ピンクが主軸）。比較結果を石橋／西社長と確認し、採用色を最終決定。

- [ ] **Step 3: Commit**

```bash
git add client/marin/css/top.css
git commit -m "feat(marin-top): オレンジ・アクセントA/B切替（body.accent-orange）"
```

---

## Self-Review（このplanの自己点検）

- **Spec coverage**：①C3ビジュアル(Task1,3)②モーション一式(Task1,3,4,6,8＋reduced対応)③ヒーロー（海/カルーセル/重ね文字/回るボタン/2CTA, Task3,4）④12ブロック構成(Task2-10)⑤数字4つ(Task7)⑥採用=LINE/Indeed(Task8)⑦トップのみ・別CSS/JSで既存非破壊(Task1,11)⑧採用ページ無し→#numbersアンカー(Task5,7)⑨SEO/JSON-LD踏襲(Task1,11)⑩素材プレースホルダー(Task3,7,9)⑪オレンジA/B(Task12) — spec各項に対応タスクあり。
- **DOM順＝spec順（最重要）**：Task 3 で旧 `<main>` の全セクション（旧 photostrip/story 含む）を一括削除し、Task 5〜9 で各セクションを `</main>` 直前に**番号順に追加**するため、最終DOMは hero,02,03,04,05,06,07,08,09,10,11 となり、**採用クラスター 06→07→08 が連続**する（ユーザー確認事項）。Task 11 で order を検証。
- **取り残しなし**：旧 photostrip・旧 story は Task 3 の一括削除で除去（top.css に対応スタイルも作らない）。
- **Placeholder scan**：仮値・TODOは「素材/実数の差し替え」を意図した実コンテンツ（実在URL・実在画像・具体値）であり、コード上の未実装プレースホルダーではない。`href="#"` 単体やダミーリンクは禁止と明記(Task5,11)。spec ブロック07「一日の流れ」は次パス延期と明記(Task8)。
- **Type/命名整合**：`#numbers`(Task7定義←Task5参照)、`#recruit`(Task8定義←Task10 FAB参照)、`[data-countup]`/`data-unit`(Task4実装←Task7使用)、`.reveal/.is-in`(Task1←全タスク)、`.hero-entry-bg`(Task3 markup←CSS)、`--pink`変数(全タスク←Task12で一括上書き) が一致。SVG presentation属性に `var()` を使わない（CSSで `fill`）。

## Execution Handoff

各タスクは独立コミット可能で、Task順に積み上げると常に表示可能なトップが保たれる。
**実行方式は Inline 実行（superpowers:executing-plans）を推奨**：本planは1つの `index.html` ＋ `top.css` ＋ `top.js` を12タスクで**逐次的に育てる**構造で、各タスクが直前のファイル状態（特に `</main>` 直前への追加順）に依存する。タスクごとに新規サブエージェントを立てる subagent-driven は、ファイル状態の共有が無く相性が悪い。Inline でチェックポイントを挟みつつ進めるのが安全。
