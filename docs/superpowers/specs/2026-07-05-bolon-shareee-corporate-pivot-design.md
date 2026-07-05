# 株式会社Bolon Shareee コーポレートサイト転換 設計仕様書

- **作成日**: 2026-07-05
- **顧客No.**: 3 / **契約番号**: SS-C-2026-003
- **対象**: `client/bolon-shareee/`（プレビュー中・本番未公開）
- **前提スペック**: `docs/superpowers/specs/2026-05-12-bolon-shareee-website-design.md`（当初=「B.villeaサロン最前面」方針。本書はこれを上書きする転換仕様）

---

## 1. 背景と目的

現行サイトは「サロンB.villea」を主役にした実質サロンLPで、運営会社 株式会社Bolon Shareee は脇役の扱い。
クライアント要望により、**主役を「会社（株式会社Bolon Shareee）」へ寄せた純コーポレートサイト**へ転換する。

### 確定した方向性（ユーザー確認済み）
1. **会社主役**：株式会社Bolon Shareee を前面。B.villea はブランド／事業の一つに位置づける。
2. **純コーポレート**：全事業を平等に見せ、会社の信頼・プレゼンスを作る。強い単一販促CTAは置かず、総合お問い合わせに集約。上品なトーン。
3. **事業は2つ**：①サロン事業（B.villea）／②スクール事業（**機器販売はスクールに内包**）。※旧「3事業（サロン／スクール／機器代理店）」から変更。
4. **アプローチ = A案**：既存6ページ骨格・CSS・ロゴ資産を活かし、トップの中身を会社起点に再構成。新規ページは作らない（月額3,980円・6ページ標準内）。
5. **ヒーロー = 文字組**：会社写真が無い制約を逆手に、クリーム×ゴールドの文字組ヒーロー（写真非依存）。
6. **サロンB2C要素**：お客様の声のみトップに信頼材料として残し、Before/After・Instagram は事業ページ（`business.html#salon`）へ移設。
7. **主CTA**：総合お問い合わせ（`contact.html`）を主、公式LINEを副。

---

## 2. 制約：使える会社写真がほぼ無い（重要）

監査の結果、コーポレートの「顔」を作る画像資産が不足している。

| 資産 | 用途可否 |
| --- | --- |
| `logo.svg`（Bolon Shareee ワードマーク） | ○ 会社ロゴとして使用（唯一の会社アイデンティティ資産） |
| `ogp.png`（クリーム地の文字組シェア画像） | △ ヒーローの文字組テンプレとして参考。背景素材そのものではない |
| `download.jpg`（サロン内観） | △ ランジェリー写り込みで「サロン感」が強い。会社ヒーローには不適 → サロン枠用 |
| `C057417807.jpg`（代表 蒲池百都子 顔写真） | △ 164×219と低解像。代表メッセージの小枠のみ可、ヒーロー不可 |
| `C037959832.jpg`（Before/After 胴体） | × 会社の顔に不適・低解像 |
| `insta-*.jpg` / スクショPNG群 | × ブラウザUI入りスクショ。清潔な写真ではない |

**不足（クライアント提供が必要）**：中立な会社/オフィス/チーム写真、スクール（講習）写真、機器写真、高解像の代表ポートレート、本物のBefore/After。
→ **設計方針**：写真に依存しない文字組・エディトリアル構成で「今ある資産だけで公開できる」状態を作る。写真提供は任意の後追い差し替えとする（公開ブロッカーにしない）。

---

## 3. サイト構成（6ページ維持）

| ファイル | 変更 |
| --- | --- |
| `index.html` | ★大改修：サロンLP → コーポレートTOP |
| `business.html` | 3事業 → 2事業に再編（機器販売をスクールへ内包）。サロンB2C要素（Before/After・Instagram）を#salonへ集約 |
| `company.html` | 事業内容を3→2に更新。ロゴ・SEO会社寄せ |
| `faq.html` | サロン客向けFAQのまま維持。ロゴ・title会社寄せのみ |
| `contact.html` | ロゴ・title/desc会社寄せ。フォーム項目を2事業に微調整 |
| `privacy.html` | 現状維持（ロゴ替えのみ。既に会社寄せ） |

グローバルナビは現状維持：`トップ / 事業内容 / 会社概要 / よくある質問 + CONTACT`。

---

## 4. コーポレートTOP（index.html）セクション仕様

順に以下で構成する。既存CSSクラスを流用（新規は文字組ヒーローの1バリアントのみ）。

| # | セクション | 内容 | 再利用クラス |
| --- | --- | --- | --- |
| 1 | ヘッダー | ロゴ `B.villea` → `Bolon Shareee` | `header` `logo` `nav` |
| 2 | ヒーロー（文字組） | クリーム×ゴールドのCSS背景。eyebrow「Bolon Shareee Inc.」／H1「株式会社Bolon Shareee」／コピー「女性の美と自信を、事業で支える。」／金の罫線。**写真なし**。スクロール誘導は流用 | 新規 `hero-corporate`（`hero`系の写真なしバリアント） |
| 3 | 理念/ミッション | 会社の考えを短文で。company.htmlのリード「〜女性の美と自信を支える企業です」を昇格・肉付け | `intro`（または `message` 系） |
| 4 | 事業（2カード） | 01 サロン事業（B.villea）／02 スクール事業（機器販売含む）を**平等**に。各カードから `business.html#salon` / `#school` へ | `company-summary` `business-list` `business-item` `business-num` |
| 5 | 代表メッセージ | 蒲池百都子ポートレート（小枠OK）＋会社ビジョン寄りに再トーン（サロン軟文体→会社）。署名「株式会社Bolon Shareee 代表取締役 蒲池百都子」 | `message` または `story-grid` |
| 6 | お客様の声 | 会社の信頼材料として簡潔に残す（3件）。**Before/Afterは載せない**。「個人差」注記維持 | `voice`（ダーク帯） |
| 7 | 会社概要（抜粋） | 商号／代表／設立／所在地／事業内容（2事業）。詳細は `company.html` へ誘導 | `company-table` または `studio-info`（`studio-grid-solo`） |
| 8 | お問い合わせ | **主CTA＝総合お問い合わせ（contact.html）**、公式LINEは副ボタン | `line-cta` / `contact-cta-sec` `line-actions` `line-btn` |
| 9 | フッター | ロゴ順を会社→サロンへ（`footer-logo`=Bolon Shareee、`footer-corp`=B.villea表記） | `footer` |

**TOPから撤去 → `business.html#salon` へ移設**：Before/Afterギャラリー、Instagram3枚、サロン営業時間、ホットペッパー予約リンク。

---

## 5. business.html 再編（3→2事業）

- ページリード：「株式会社Bolon Shareee は**2つの事業**で女性の美と自信を支えています。」
- **Business 01 サロン事業（B.villea, #salon）**：既存のサロン詳細（こんなお悩みに／大切にしていること／施術の流れ／メニューと料金）を維持し、**index.htmlから移設したBefore/After・Instagram**をここへ集約。末尾にホットペッパー予約CTA。＝サロンB2Cハブ。
- **Business 02 スクール事業（#school）**：既存スクール詳細（こんな方へ／学べること／卒業後=業務委託パートナー）に、**旧Business 03「機器代理店・販売」を内包サブブロックとして統合**（卒業生・提携サロンへの機器販売／代理店）。CTA：スクール資料請求／機器導入相談。
- 旧 `#equipment` セクションは削除（内容はスクール内へ）。company.html等からの `#equipment` リンクは `#school` に付け替え。

---

## 6. 他ページの変更

- **company.html**：基本情報の「事業内容」行を 3→2（①サロン ②スクール〈機器販売含む〉）。「3つの事業について」カード → 2カード。B2B相談ブロックは維持。ロゴ・og:site_name会社寄せ。
- **faq.html**：サロン客FAQのまま維持。ヘッダー/フッターロゴ替え、title・og/twitterを会社主役に。
- **contact.html**：ロゴ替え、title/description会社主役に。フォームの「ご相談内容」selectを2事業前提に整理（サロン体験・料金／スクール・機器／業務委託／その他）。Formspree action プレースホルダ（`REPLACE_WITH_FORMSPREE_ID`）は別課題として保持。
- **privacy.html**：ヘッダー/フッターロゴ替えのみ（本文は既に会社寄せ）。

---

## 7. ブランド／SEO 統一（会社主役）

全6ページ横断で以下を統一（監査で全箇所特定済み）。

- **ヘッダーロゴ**（`.logo`）：`B.villea` → `Bolon Shareee`（全6ページ）。
- **フッターロゴ**（`.footer-logo` / `.footer-corp`）：順を会社主役に入れ替え（全6ページ）。
- **ヒーローH1**（index）：`B.villea` → 会社主役（文字組ヒーロー化に伴い置換）。
- **`<title>`**：index / faq / contact を会社主役に（business / company / privacy は既に会社主役）。
- **`og:site_name`**：`B.villea / 株式会社Bolon Shareee` → `株式会社Bolon Shareee / B.villea`（OGPを持つ5ページ）。
- **`og:title` / `twitter:title` / `meta description`**：index / faq / contact を会社主役に合わせて更新。
- **JSON-LDは変更不要**：Organization名は既に会社名。サロンの `HealthAndBeautyBusiness` 名 `B.villea（ビーヴィレア）` は正しいので**保持**。
- **残す正当な"B.villea"（変更しない）**：ヒーロー装飾縦書き、メッセージ署名、「B.villeaサロン」見出し、IGハンドル `@b.villea.fukuoka`、CSS/JSヘッダーコメント、logo.svg aria-label。
- **sitemap.xml**：6URLはプレビュー中でコメントアウト済み。本番公開時に解除（本書スコープ外・公開手続き側）。

---

## 8. デザインシステム（既存流用・新規最小）

- **世界観**：Editorial × Gold（クリーム地／ブーゲンビリア・マゼンタ主役／ゴールド差し色／深いプラム文字）。AI感を嫌う文字組主体。
- **配色トークン**：`--primary #C8276B` / `--primary-deep #A11E55` / `--bg-base #FFFFFF` / `--bg-warm #FBF6EF` / `--gold #D4A657` / `--text-main #3A1A2A` / `--text-sub #5A4050` / `--border #EDE4DC`。LINE緑 `#06C755`。
- **フォント**：見出し=Zen Old Mincho（JP明朝）／アクセント=Cormorant Garamond（EN斜体）／本文=Zen Kaku Gothic Antique（JP sans 300）。表示ワードマークにBodoni Moda。※新規/改修ページの `<head>` に全フォントのリンクを維持すること（CSSは@importしない）。
- **新規CSS**：`hero-corporate`（写真スライドショー無し・クリーム/ゴールドCSS背景の文字組ヒーロー）。既存 `hero` 系の余白・タイポ・scroll誘導・reveal・vh→svh を踏襲したバリアントとして最小追加。

### 8.1 モバイル既踏み罠（必ず踏襲）
- ヘッダー `backdrop-filter` は880px以下で**オフ**（不透明背景に）。
- フルハイト要素は `100vh` の後に `100svh`（URLバー対策）。
- フォーム入力は `font-size:16px` 維持（iOS自動ズーム防止）。
- 見出しは `word-break: keep-all; overflow-wrap: normal`（日本語の不自然な折返し防止）。
- 単一ブレークポイント880pxで各グリッドを1カラム化。
- `prefers-reduced-motion: reduce` を新規アニメでも尊重。
- 固定ヘッダー72px（モバイル60px）分の `padding-top` オフセット。

---

## 9. コンプライアンス

- 会社寄せにより body-focused な表現が減り、薬機法/景表法リスクは**低下**。
- お客様の声・Before/After枠の「個人の感想／効果には個人差があります」注記は維持。
- IGプロフィールの断定表現（「巨乳」「◯カップUP」等）はサイトに転載しない（既存方針踏襲）。

---

## 10. クライアント提供待ち（公開ブロッカーではない・後追い差し替え）

- 高解像の代表ポートレート（代表メッセージ用）
- 任意：中立な会社/オフィス/チーム写真（将来の写真ヒーロー化用）
- スクール（講習風景）写真 ／ 機器写真（事業ページのプレースホルダ差し替え）
- 本物のBefore/After（サロン枠のプレースホルダ差し替え）
- Formspree ID（`contact.html` の action 差し替え）／公式LINE URL（`lin.ee` 実URL）

---

## 11. 非対象（Non-goals）

- 新規ページの追加（salon.html 等。A案のため作らない）。
- CSSの全面刷新・配色/フォント変更（既存デザインシステムを維持）。
- 本番公開手続き（独自ドメイン・sitemap解除・noindex解除・Formspree/LINE実接続）。別タスク。
- ロゴの新規デザイン制作（既存 logo.svg を使用）。

---

## 12. 完了条件（受け入れ基準）

1. index.html がコーポレートTOP（第4章の9セクション）として表示され、写真なしで破綻しない。
2. 全6ページのヘッダー/フッターロゴが会社主役に統一。
3. business.html が2事業構成になり、Before/After・Instagram が #salon に存在、TOPには無い。
4. index/faq/contact の title・OGP・twitter・og:site_name が会社主役に統一。JSON-LDは会社名維持・サロンサブ実体は保持。
5. 主CTAが総合お問い合わせ（contact.html）でLINEが副。
6. モバイル既踏み罠（第8.1章）が全て維持され、880px以下で1カラム化・レイアウト破綻なし。
