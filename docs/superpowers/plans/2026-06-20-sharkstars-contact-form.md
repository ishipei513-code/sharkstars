# SHARKSTARSトップ お問い合わせフォーム 実装計画

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** トップ `index.html` の `#contact` 右カード（mailto）を、Web3Forms連携の実フォーム（お名前／メール／ご相談内容）に置換する。

**Architecture:** 静的HTML。フォーム送信はクライアントJSから `https://api.web3forms.com/submit` にAJAX(POST/JSON)し、Web3Formsが `sharkstars0513@gmail.com` にメール転送。サーバーコードは持たない。CSSは既存のフォームクラス（`.form-group/.form-label/.form-input/.form-textarea/.form-submit`）を流用し、iOSズーム対策と状態表示スタイルのみ追加。JSはindex.html内のインライン`<script>`で完結（共有 `assist/js/main.js` は変更しない）。

**Tech Stack:** 素のHTML/CSS/JS（ビルドツールなし）、Web3Forms（外部フォームサービス）。検証はブラウザ（Playwright MCP）＋目視。**ユニットテストのフレームワークは無い**ため、各タスクの検証はブラウザでの挙動確認＝設計書の受け入れ基準に対応する。

**設計書:** `docs/superpowers/specs/2026-06-20-sharkstars-contact-form-design.md`

---

## ファイル構成

| ファイル | 役割 | 変更 |
|----------|------|------|
| `index.html` | `#contact` 右カードのフォームHTML／添付フォールバック行／送信ハンドラの`<script>` | Modify |
| `assist/css/style.css` | フォーム入力欄の16px化（iOS対策）＋成功/エラー/同意文/フォールバック注記のスタイル | Modify |

> **注意（行番号）:** 行番号は「編集前」基準。Task 1 でHTMLを置換すると以降の行番号がずれるので、後続タスクは**アンカー文字列**で挿入位置を特定すること。

> **検証用ローカルURL:** `file:///D:/sharkstars/index.html`（Playwright MCP `browser_navigate` で開く）

---

## Task 1: 右の「メールカード」をフォームに置換

**Files:**
- Modify: `index.html`（編集前 `3016`–`3034` 行＝`<!-- Right: Email Info -->` のカード `div` 全体）

- [ ] **Step 1: 既存の右カード（メール）をフォームに置換する**

`index.html` の以下のブロック（`<!-- Right: Email Info -->` から、その `div` を閉じる `</div>` まで＝編集前3016–3034行）を丸ごと次に置き換える。左の `<!-- Left: LINE Info -->` カードは**触らない**。

置換後:

```html
        <!-- Right: Contact Form (LINEを使わない方の受け皿) -->
        <div class="contact-form-card">
          <h3 class="contact-info-title" style="margin-bottom: 12px;">フォームでお問い合わせ 📝</h3>
          <p class="contact-info-desc" style="margin-bottom: 24px;">
            LINEをお使いでない方・PCからはこちら。<br>
            1〜2営業日以内にご返信します。
          </p>
          <form id="contact-form">
            <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY">
            <input type="hidden" name="subject" value="【SHARKSTARS】サイトからのお問い合わせ">
            <input type="checkbox" name="botcheck" style="display:none;" tabindex="-1" autocomplete="off" aria-hidden="true">

            <div class="form-group">
              <label class="form-label" for="cf-name">お名前<span class="required">*</span></label>
              <input class="form-input" type="text" id="cf-name" name="name" required autocomplete="name">
            </div>
            <div class="form-group">
              <label class="form-label" for="cf-email">メールアドレス<span class="required">*</span></label>
              <input class="form-input" type="email" id="cf-email" name="email" required autocomplete="email">
            </div>
            <div class="form-group">
              <label class="form-label" for="cf-message">ご相談内容<span class="required">*</span></label>
              <textarea class="form-textarea" id="cf-message" name="message" required></textarea>
            </div>
            <p class="form-consent">送信をもって<a href="privacy.html">プライバシーポリシー</a>に同意したものとみなします。</p>
            <button type="submit" class="form-submit">送信する</button>
            <p id="form-status" class="form-status" role="alert" hidden></p>
          </form>
        </div>
```

- [ ] **Step 2: ブラウザで描画を確認**

Playwright MCP で `file:///D:/sharkstars/index.html` を開き、`#contact` までスクロール（または `browser_snapshot`）。
Expected:
- 左にLINEカード（「LINEで気軽に無料相談 🎯」＋LINEボタン）が**従来どおり**表示される。
- 右に「フォームでお問い合わせ 📝」＋お名前／メールアドレス／ご相談内容の3項目＋「送信する」ボタンが表示される。
- `botcheck` チェックボックスは**画面に見えない**。

- [ ] **Step 3: HTML5必須バリデーションを確認**

空のまま「送信する」をクリック（Playwright `browser_click`）。
Expected: 送信されず、お名前欄にブラウザ標準の必須エラー（例「このフィールドを入力してください」）が出る。`browser_evaluate` で `document.querySelector('#cf-name').validity.valueMissing === true` を確認してもよい。

- [ ] **Step 4: コミット**

```bash
git add index.html
git commit -m "feat(contact): トップ#contactの右カードをお問い合わせフォームに置換"
```

---

## Task 2: フォーム用CSS（iOSズーム対策＋状態表示）を追加

**Files:**
- Modify: `assist/css/style.css`（`.form-submit:hover { ... }` の直後＝編集前 `1894` 行の `}` の後、`/* LEGAL / PAGE CONTENT */` コメントの前に挿入）

- [ ] **Step 1: 既存フォームスタイルの直後に追記**

アンカー：`.form-submit:hover { background-color: var(--gray-700); }` を閉じる `}`（編集前1894行）と、`/* ====...  LEGAL / PAGE CONTENT` コメント（編集前1896行）の**間**に、次を挿入する。

```css

/* ============================================
   CONTACT FORM (index #contact)
   ============================================ */
/* iOS Safari は font-size<16px の入力欄フォーカスで自動ズームするため、
   このフォームの入力欄だけ 16px に引き上げる（既存 .form-input=0.85rem を上書き） */
#contact-form .form-input,
#contact-form .form-textarea {
  font-size: 16px;
}

.form-consent {
  font-size: 0.72rem;
  color: var(--gray-500);
  line-height: 1.5;
  margin-bottom: 16px;
}
.form-consent a { color: var(--gray-700); text-decoration: underline; }

.form-status {
  margin-top: 16px;
  padding: 12px 14px;
  font-size: 0.8rem;
  line-height: 1.6;
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  color: #b91c1c;
}
.form-status a { color: #b91c1c; text-decoration: underline; }

.form-success {
  text-align: center;
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.7;
  color: var(--gray-900);
  padding: 24px 0;
}

.contact-fallback-note {
  text-align: center;
  font-size: 0.78rem;
  color: var(--gray-500);
  margin-top: 28px;
  line-height: 1.6;
}
.contact-fallback-note a { color: var(--gray-700); text-decoration: underline; }
```

- [ ] **Step 2: スタイル適用とiOS対策を確認**

Playwright MCP でページを再読込し `#contact` を確認。
Expected:
- 入力欄が16px相当で表示され、同意文（`.form-consent`）がグレーの小さめ文字でリンク付き表示。
- `browser_evaluate` で `getComputedStyle(document.querySelector('#cf-name')).fontSize === '16px'` を確認（iOSズーム回避の担保）。

- [ ] **Step 3: コミット**

```bash
git add assist/css/style.css
git commit -m "style(contact): フォーム入力を16px化(iOSズーム回避)＋成功/エラー/同意/注記スタイル追加"
```

---

## Task 3: 添付フォールバックの一文を追加

**Files:**
- Modify: `index.html`（`.contact-wrapper` を閉じる `</div>` の直後、`.container` を閉じる `</div>` の直前）

- [ ] **Step 1: wrapper の下にフォールバック注記を挿入**

アンカー：`#contact` 内で `.contact-wrapper` を閉じる `</div>`（左LINEカードと右フォームカードを包む div の閉じタグ。Task 1 置換後はフォームカードの `</div>` の次の行）と、その外側 `.container` の `</div>` の**間**に、次の1ブロックを挿入する。

```html
      <p class="contact-fallback-note">
        ファイルを添付したい方・LINEをお使いでない方は
        <a href="mailto:sharkstars0513@gmail.com">sharkstars0513@gmail.com</a> へ直接どうぞ。
      </p>
```

挿入後のおおまかな構造（確認用）:

```html
  <section class="section contact" id="contact">
    <div class="container">
      ...
      <div class="contact-wrapper fade-in">
        <div class="contact-form-card"> … LINE … </div>
        <div class="contact-form-card"> … フォーム … </div>
      </div>
      <p class="contact-fallback-note"> … 追加した1行 … </p>
    </div>
  </section>
```

- [ ] **Step 2: 表示を確認**

Playwright MCP で再読込。
Expected: 2カラムの下中央に「ファイルを添付したい方・LINEをお使いでない方は sharkstars0513@gmail.com へ直接どうぞ。」がグレー小文字で表示され、メールリンクが機能する。

- [ ] **Step 3: コミット**

```bash
git add index.html
git commit -m "feat(contact): 添付・LINE非利用者向けのメールフォールバック行を追加"
```

---

## Task 4: 送信ハンドラ（Web3Forms AJAX）を追加

**Files:**
- Modify: `index.html`（`<script src="assist/js/main.js"></script>`＝編集前 `3118` 行の**直前**に新しい `<script>` を挿入）

- [ ] **Step 1: インライン送信ハンドラを挿入**

アンカー：`<script src="assist/js/main.js"></script>` の**直前の行**に、次を挿入する。

```html
  <!-- Contact form submit (Web3Forms) -->
  <script>
    (function () {
      var form = document.getElementById('contact-form');
      if (!form) return;
      var status = document.getElementById('form-status');
      form.addEventListener('submit', async function (e) {
        e.preventDefault();
        var btn = form.querySelector('.form-submit');
        var original = btn.textContent;
        btn.disabled = true;
        btn.textContent = '送信中…';
        if (status) { status.hidden = true; status.textContent = ''; }
        try {
          var payload = JSON.stringify(Object.fromEntries(new FormData(form)));
          var res = await fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: payload
          });
          var data = await res.json();
          if (res.status === 200 && data.success) {
            form.innerHTML = '<p class="form-success" role="status">✓ 送信ありがとうございました。<br>1〜2営業日以内にご返信します。</p>';
          } else {
            throw new Error((data && data.message) || '送信に失敗しました');
          }
        } catch (err) {
          if (status) {
            status.hidden = false;
            status.innerHTML = '送信に失敗しました。お手数ですが LINE または <a href="mailto:sharkstars0513@gmail.com">sharkstars0513@gmail.com</a> までご連絡ください。';
          }
          btn.disabled = false;
          btn.textContent = original;
        }
      });
    })();
  </script>
```

- [ ] **Step 2: エラーパスをブラウザで確認**

`access_key` はプレースホルダ `YOUR_ACCESS_KEY` のままなので、Web3Forms は失敗を返す＝**エラーパスを実地検証できる**。
Playwright MCP で `#contact` を開き、お名前=「テスト」、メール=「test@example.com」、ご相談内容=「テスト送信」を入力 → 「送信する」をクリック。
Expected:
- 送信中はボタンが `disabled`＋「送信中…」。
- 数秒後、`#form-status` に「送信に失敗しました。…LINE または sharkstars0513@gmail.com まで…」が表示される。
- ボタンが「送信する」に戻り、再クリック可能。

> **成功パスの検証**は本物のアクセスキーが必要（Task 6 のセットアップ後）。ここではエラーパスとUI遷移（送信中→失敗→復帰）の確認まで。

- [ ] **Step 3: コミット**

```bash
git add index.html
git commit -m "feat(contact): Web3FormsへのAJAX送信ハンドラ(送信中/成功/失敗UI)を追加"
```

---

## Task 5: 受け入れ基準のQAパス（PC／モバイル）

**Files:**
- Modify: 必要に応じて `index.html` / `assist/css/style.css`（不具合があれば修正）

- [ ] **Step 1: 設計書の受け入れ基準を一通り確認**

Playwright MCP で `file:///D:/sharkstars/index.html` を開き、次を確認：
- [ ] 必須未入力で送信不可（HTML5）。不正メール形式も弾かれる（`browser_evaluate` で `#cf-email` に「abc」を入れ `validity.typeMismatch === true`）。
- [ ] 送信成功で**ページ遷移しない**設計になっている（ハンドラが `e.preventDefault()`）。
- [ ] エラー時にフォールバック導線が出て再送信できる（Task 4 で確認済みなら再掲不要）。
- [ ] 左LINEカード・nav の「お問い合わせ」アンカー・末尾の sticky CTA・他セクションが**崩れていない**。

- [ ] **Step 2: モバイル表示を確認**

`browser_resize` で幅375pxにし `#contact` を確認。
Expected:
- 2カラムが縦積みになり、LINEカード→フォームカードの順。入力欄が潰れない。
- `getComputedStyle(document.querySelector('#cf-name')).fontSize === '16px'`（iOSズーム回避の最終担保）。

- [ ] **Step 3: 問題があれば修正してコミット／無ければ完了を記録**

```bash
# 修正した場合のみ
git add -A
git commit -m "fix(contact): QAパスでの表示・挙動の微修正"
```

---

## Task 6: 本番有効化（石橋さんの作業 → キー差し込み）

> これはコード実装後の運用ステップ。Task 1–5 はプレースホルダキーのまま完了できる。

- [ ] **Step 1:** 石橋さんが `https://web3forms.com/#start` で `sharkstars0513@gmail.com` を登録し、無料アクセスキーを取得。
- [ ] **Step 2:** `index.html` の `value="YOUR_ACCESS_KEY"` を実キーに差し替え。

```bash
git add index.html
git commit -m "chore(contact): Web3Formsアクセスキーを設定し本番有効化"
```

- [ ] **Step 3:** 実キーで本物の送信テスト → `sharkstars0513@gmail.com` に件名「【SHARKSTARS】サイトからのお問い合わせ」で届き、Reply-Toが入力メールになっていること、成功メッセージに切り替わることを確認。

---

## 完了の定義

- `#contact` 右カードが3項目フォームになり、左LINEカードは主役のまま維持。
- 送信が Web3Forms 経由で `sharkstars0513@gmail.com` に届く（キー設定後）。
- 送信中／成功／失敗のUIが機能し、失敗時はLINE/メールへ誘導。
- iOSで入力欄フォーカス時に自動ズームしない（16px）。
- PC/モバイルともレイアウト崩れなし。
