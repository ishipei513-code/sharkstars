# SHARKSTARSトップページ お問い合わせフォーム 設計書

- **対象**：SHARKSTARS自社サイト トップページ `index.html` の `#contact` セクション
- **公開URL**：`https://sharkstars.jp/`（リポジトリ直下 `index.html`）
- **作成日**：2026-06-20
- **関連**：[[design_preferences]]（シンプル／AI感を嫌う／モバイル優先）、[[mobile_css_pitfalls]]（iOSフォームzoom）、[[deployment_structure]]（sharkstars.jp はリポジトリ直）

---

## 1. 目的・読者層

トップの問い合わせ手段に、**LINE以外の「受け皿」**として実フォームを1つ足す。

- 主対象：**PCから見ている人／LINEに抵抗がある層／B2B（連携先）**。LINEをタップしない見込み客の取りこぼしを防ぐ。
- **LINEは引き続き主役**。フォームは脇役＝低摩擦・最小項目。
- 返信は**メール**で行う前提（フォームの入力メールアドレス宛）。

---

## 2. スコープ

### 今回作る
- `index.html` の `#contact` 右カード（現在はメール`mailto`カード）を、**実フォームに置換**。
- Web3Forms連携の送信処理（AJAX）＋送信中/成功/失敗のUI。
- フォーム要素のCSS（既存カードスタイル `.contact-form-card` に準拠して最小追加）。

### 今回作らない（YAGNI）
- 添付ファイルのアップロード（→ メール導線で代替）
- 自動返信メール（オートレスポンダ）※必要になれば後日Web3Forms側で追加可能
- reCAPTCHA等の表示型ボット対策（ハニーポットで代替）
- 他ページ（service.html等）やクライアントサイトへの横展開（今回はトップのみ）
- フォーム内容のDB保存・管理画面（メール転送のみ）

---

## 3. 送信方式：外部フォームサービス（Web3Forms）

静的サイト（Apache配信）のため、送信後処理は外部サービスに委譲する。自前PHPメーラーは保守・スパム・到達性（共有サーバの`mail()`はGmailで不達/迷惑メール化しやすい）を抱えるため不採用。Googleフォーム埋め込みはデザインがブランドに馴染まず不採用。

### 連携仕様（公式 docs.web3forms.com で確認済み・2026-06-20）
- **エンドポイント**：`POST https://api.web3forms.com/submit`
- **必須隠しフィールド**：`access_key`（無料登録で取得。`web3forms.com/#start` で `sharkstars0513@gmail.com` を登録 → キーがメールで届く）。**キーはHTMLに直書き＝公開前提**の設計。
- **宛先**：登録アカウントのメール（= `sharkstars0513@gmail.com`）に自動転送。フォーム側に宛先指定は不要。
- **Reply-To**：フォームの `email` フィールドが自動でReply-Toになる → 受信メールにそのまま返信すれば顧客に届く。
- **件名**：隠しフィールド `subject` で指定 → `【SHARKSTARS】サイトからのお問い合わせ`。
- **送信形式**：FormData → プレーンオブジェクト → JSON文字列。ヘッダは `Content-Type: application/json` と `Accept: application/json`。
- **レスポンス**：HTTP 200 かつ JSON `{ success: true, message }` で成功、それ以外を失敗として扱う。

### 送信処理コードスケッチ
```js
const form = document.getElementById('contact-form');
const status = document.getElementById('form-status');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const btn = form.querySelector('button[type=submit]');
  btn.disabled = true; btn.textContent = '送信中…';
  const json = JSON.stringify(Object.fromEntries(new FormData(form)));
  try {
    const res = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: json
    });
    const data = await res.json();
    if (res.status === 200 && data.success) {
      form.innerHTML = '<p class="form-success" role="status">✓ 送信ありがとうございました。<br>1〜2営業日以内にご返信します。</p>';
    } else { throw new Error(data.message || '送信に失敗しました'); }
  } catch (err) {
    status.hidden = false;
    status.textContent = '送信に失敗しました。お手数ですがLINEまたは sharkstars0513@gmail.com までご連絡ください。';
    btn.disabled = false; btn.textContent = '送信する';
  }
});
```

---

## 4. 入力項目・バリデーション

| 項目 | name | 必須 | 型・備考 |
|------|------|------|----------|
| お名前 | `name` | ✅ | `type=text` |
| メールアドレス | `email` | ✅ | `type=email`（HTML5検証＋Reply-Toにも使用） |
| ご相談内容 | `message` | ✅ | `textarea`（3〜4行） |

- 空送信は HTML5 `required` で防止。`email` は `type=email` でフォーマット検証。
- **入力欄の `font-size` は16px以上**（iOS Safariの自動ズーム＝[[mobile_css_pitfalls]] を回避）。
- 各入力に `<label>` を紐付け（`for`/`id`）。スクリーンリーダ対応。
- 隠しフィールド：`access_key`（キー）、`subject`（件名）、`botcheck`（ハニーポット）。

---

## 5. 配置・マークアップ

- `#contact` の `.contact-wrapper` は2カラム維持。**左＝LINEカード（現状のまま・主役）／右＝メールカードをフォームに置換**。
- 右カード見出し：**「フォームでお問い合わせ 📝」**＋小見出し「LINEをお使いでない方・PCからはこちら。1〜2営業日でご返信します。」（＝「LINEの受け皿」という狙いを明示）。
- `.contact-wrapper` の下に小さなテキストリンクを1行：**「ファイルを添付したい方・LINE未利用の方は `sharkstars0513@gmail.com` へ」**（旧メールカードが担っていた“添付対応”役を温存）。
- フォーム外観は既存 `.contact-form-card` の角丸・余白・配色・フォントに合わせ、**新規の装飾を足さない**（AI感・既製感を出さない）。入力欄は既存のCSS変数（配色）に準拠。

---

## 6. UX（状態遷移）

- **送信前**：通常表示。送信ボタン「送信する」。
- **送信中**：ボタンを `disabled`、ラベル「送信中…」。二重送信防止。
- **成功**：カード内容を成功メッセージ（`✓ 送信ありがとうございました。1〜2営業日以内にご返信します。`）に差し替え。`role="status"` でアナウンス。
- **失敗**：`#form-status`（`aria-live`）にエラー文＋**LINE/メールのフォールバック導線**を表示。ボタンを元に戻し再送信可能に。

---

## 7. スパム・プライバシー

- **ハニーポット**：`<input type="checkbox" name="botcheck" style="display:none">`（Web3Forms標準）。人間には不可視、ボットがチェックすると弾かれる。＋Web3Forms側スパムフィルタ。
- **reCAPTCHAは入れない**：摩擦増・見た目を汚す・AI感が出るため。
- **プライバシー配慮**：送信ボタン付近に一文「送信をもって[プライバシーポリシー](privacy.html)に同意したものとみなします」。氏名・メールを扱うため明示。

---

## 8. 石橋さんのセットアップ作業（1つだけ）

1. `https://web3forms.com/#start` で **`sharkstars0513@gmail.com`** を登録し、無料の**アクセスキー**を受け取る。
2. キーを共有 → HTMLの `access_key` 隠しフィールドに差し込む（または先にプレースホルダ `YOUR_ACCESS_KEY` で実装し、後で置換）。

※無料プランで利用（月間上限は公称250件程度＝問い合わせ用途には十分。正確な上限は登録時に確認）。

---

## 9. 受け入れ基準（テスト観点）

- [ ] 必須項目が空だと送信できない（HTML5検証）。不正メール形式も弾かれる。
- [ ] 正常送信で `sharkstars0513@gmail.com` に件名「【SHARKSTARS】サイトからのお問い合わせ」で届き、Reply-Toが入力メールになっている。
- [ ] 送信成功でページ遷移せず成功メッセージに切り替わる。送信中はボタンが押せない。
- [ ] 通信失敗時にエラー文＋LINE/メール導線が出て、再送信できる。
- [ ] スマホ（iOS Safari）で入力欄タップ時に画面が自動ズームしない（font-size 16px以上）。
- [ ] 左のLINEカード・nav/sticky CTA・他セクションのデザインが崩れない。
- [ ] ハニーポット `botcheck` は画面に見えない。

---

## 10. 非対象（再掲）

添付アップロード／自動返信／reCAPTCHA／DB保存・管理画面／他ページ横展開。必要になった時点で別タスクとして検討する。
