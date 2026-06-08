# 株式会社Bolon Shareee コーポレートサイト 設計仕様書

- **顧客No.**: 3
- **契約番号**: SS-C-2026-003
- **クライアント**: 株式会社Bolon Shareee（代表 蒲池百都子）
- **ブランド**: B.villea（バストアップ専門サロン）
- **公開URL**: `https://sharkstars.jp/client/bolon-shareee/`
- **ローカルパス**: `client/bolon-shareee/`
- **作成日**: 2026-05-12
- **想定納期**: Day 0+3（既存SHARKSTARS標準プラン枠内）

---

## 1. 案件の位置付け

株式会社Bolon Shareeeは3つの事業を持つ親法人。今回作るのは**コーポレートサイトとサロン集客LPを兼任する単一サイト**。

| 項目 | 確定事項 |
|---|---|
| サロンLPの既存有無 | **なし**（このサイトで集客まで担う） |
| 3事業の扱い | **B.villeaサロンを最前面**、機器代理店・スクールは会社情報内で軽く触れる + `school.html` でスクール詳細ページ独立 |
| 代表の出方 | **about統合セクション**として index 内で丁寧に前面に出す。aboutページは独立させない（LP型のため） |
| 効果表現 | **体験談ベース**（Voiceセクション）+「個人の感想／効果には個人差」注記必須 |
| 会社ロゴ | サイト内サービスとして**テキストロゴ新規作成**（追加費用なし） |
| CTA | LINE誘導が最終ゴール（電話・フォームは補助） |

---

## 2. ページ構成（6ページ／LP型）

| # | ファイル | 役割 |
|---|---|---|
| 1 | `index.html` | **縦長LP**。Hero / 強み / 代表ストーリー / メニュー&料金 / Voice / FAQ抜粋 / アクセス / 会社情報サマリ / LINE誘導フッター — 全部入り。スクロール総量 約4,000–5,000px |
| 2 | `school.html` | バストスクール詳細。「バストアップ起業」「バストスクール 福岡」検索向け。卒業生→業務委託パイプライン |
| 3 | `company.html` | 会社情報詳細。3事業（B.villea／バストスクール／バスト機器代理店）の入口。B2B寄り問い合わせ窓口 |
| 4 | `faq.html` | 全FAQ。LINE相談前の不安解消用 |
| 5 | `contact.html` | LINE誘導メイン + フォーム + 電話 + 詳細アクセス |
| 6 | `privacy.html` | プライバシーポリシー |

---

## 3. トップページ（index.html）セクション構成

章番号は使わず、セクション見出しのみ。

| 順 | セクション | 内容 |
|---|---|---|
| 01 | Hero | フルブリードビジュアル（ブーゲンビリア風）+ 見出し「咲き誇るあなたを、ここから。」（仮）+ LINE CTA + 縦書きBrandマーク `B.villea — Bougainvillea` |
| 02 | Intro / Editorial Eyebrow | "Bougainvillea Blooms" eyebrow + 開業14年の重みを2行コピーで |
| 03 | 強み 3つ | ①「Motokoさんの人柄」②「14年で磨いた施術」③「警固という場所」— アシメトリック1+2構成 |
| 04 | 代表ストーリー（about統合） | "Founder's Story" — 2013年個人開業 → 2025年法人化の物語。代表写真大きめ、エディトリアル雑誌風 |
| 05 | メニュー & 料金（service統合） | "Menu & Care" — 主力メニュー2-3コース、料金、施術の流れを縦長に丁寧に |
| 06 | Voice | "Voice" — 体験者の声 2-3件抜粋。**「※個人の感想です／効果には個人差があります」注記必須** |
| 07 | FAQ抜粋 | "Questions" — 3件のみ抜粋、続きは `faq.html` へ |
| 08 | アクセス & 店舗情報 | "Studio" — 警固タワー1801の地図、最寄駅、営業時間 |
| 09 | 会社情報サマリ | "Bolon Shareee" — 法人としての3事業を1行ずつ。`school.html` / `company.html` への誘導リンク |
| 10 | LINE誘導フッター | 「まずはLINEで気軽にご相談ください」 — 公式LINE QR + ボタンで締める |

---

## 4. デザインシステム

### 4.1 カラーパレット（E. Editorial × Gold ／ ゴールド控えめ）

| 用途 | 色 | HEX |
|---|---|---|
| Primary（ブランド・CTA・アクセント） | ブーゲンビリア赤紫 | `#C8276B` |
| Background base | 純白 | `#FFFFFF` |
| Background warm | クリーム | `#FBF6EF` |
| Gold accent（**控えめ**・ホバー下線・1px引き線・縦書き英字のみ） | シャンパンゴールド | `#D4A657` |
| Text main | ディープワイン | `#3A1A2A` |
| Text sub | ローズグレー | `#5A4050` |
| Border / divider | アイボリーグレー | `#EDE4DC` |

**ゴールド使用ルール（厳守）**
- 使う: リンクホバー下線、区切り線、縦書きBrandマークの英字
- 使わない: CTAボタン、見出し、大きな装飾、アイコン

### 4.2 タイポグラフィ（C. Old Luxe）

| 用途 | フォント | ウェイト |
|---|---|---|
| 和文見出し | **Zen Old Mincho** | 500 / 600 |
| 欧文見出し・eyebrow | **Cormorant Garamond** | 500 / italic 500 |
| 和文本文 | **Zen Kaku Gothic Antique** | 300（メイン）/ 400（強調） |

**サイズ目安（PC / SP）**
- H1: `64px / 40px`
- H2: `42px / 28px`
- 本文: `15px / 14px`
- 行間: 1.85〜2.0 / レター 0.06em

**全文 Google Fonts、商用無料。**

### 4.3 レイアウト原則

- **アシメトリック構成**: 1+2グリッド、ずれレイアウト、縦書き要素
- **セクション縦間隔**: PC `120-160px` / SP `72-96px`
- **マーキー帯**: `BOLON SHAREEE — BOUGAINVILLEA BLOOMS —` の英字ループを1〜2箇所
- **カードは均等3個並び禁止**（mukuの「ださい」回避ルール継承）
- **章番号なし**（ヒアリングで明示却下）

### 4.4 モバイル対応（CSS落とし穴回避）

mukuで踏んだ罠を全て回避：
1. ヘッダー `backdrop-filter` はSPで切る（fixed要素のcontaining block問題）
2. デスクトップ用 `display: flex` をSPで `flex-direction: column` に上書き
3. 大型日本語見出しは `word-break: keep-all; overflow-wrap: normal;` + `<span class="word">` で1単語ずつ包む
4. フォーム要素 `font-size: 16px` 以上でiOS自動ズーム防止
5. `100vh` と `100svh` 併記
6. `html, body { overflow-x: hidden }` 必須
7. inline style での `grid-template-columns` 禁止（specificity負け回避）

---

## 5. SEO戦略

### 5.1 キーワード階層

| 階層 | 主軸キーワード |
|---|---|
| コア（B2C・サロン） | `福岡 バストアップサロン` / `警固 バストアップ` / `福岡市中央区 バストケア` |
| 指名 | `B.villea` / `ビーヴィレア` / `蒲池百都子 サロン` |
| 法人 | `株式会社Bolon Shareee` / `Bolon Shareee` |
| スクール（school.html） | `バストスクール 福岡` / `バストアップ 起業` / `バスト 技術 習得` |
| 機器代理店（company.html） | `バスト機器 代理店` / `バストアップ機器 販売` |

### 5.2 メタ情報（index.html）

```
<title>B.villea｜福岡・警固のバストアップ専門サロン｜株式会社Bolon Shareee</title>
<meta name="description" content="福岡市中央区警固のバストアップ専門サロン B.villea。2013年開業、14年で磨いた施術と代表・蒲池百都子の人柄でひとりずつに寄り添います。バストスクール・機器代理店も運営する株式会社Bolon Shareee。">
```

### 5.3 構造化データ（JSON-LD）

- `Organization` — Bolon Shareee（全ページ）
- `LocalBusiness` (`HealthAndBeautyBusiness`) — B.villea（住所・営業時間・電話、indexのみ）
- `FAQPage` — faq.html
- `Person` — 蒲池百都子（index代表ストーリー / company）

### 5.4 OGP

- 1200×630px ブーゲンビリア風キービジュアル（新規制作）
- `og:image`, `twitter:summary_large_image` 両対応

### 5.5 その他SEO

- 全ページ `canonical` 設定
- `sitemap.xml` への追加
- ルートの `index.html`（SHARKSTARS制作実績）への追加
- `robots.txt` 確認（クロール許可）

---

## 6. ファイル構成

```
client/bolon-shareee/
├── index.html
├── school.html
├── company.html
├── faq.html
├── contact.html
├── privacy.html
├── css/
│   ├── reset.css       — muku再利用
│   └── style.css       — 新規（B.villea専用デザインシステム）
├── js/
│   └── main.js         — ハンバーガー / スクロール演出
└── images/
    ├── logo.svg        — Bolon Shareee テキストロゴ（新規）
    ├── salon-logo.png  — B.villea サロンロゴ（契約後支給）
    ├── motoko.jpg      — 代表写真（契約後支給／Unsplash仮置き）
    ├── hero.jpg        — ヒーロー画像（Unsplash仮置き→契約後差替）
    └── ogp.png         — 1200×630 OGP（新規制作）
```

---

## 7. スコープ

### 7.1 スコープ内
- 上記6ページのHTML/CSS/JS フルコーディング
- Bolon Shareee テキストロゴ（SVG/PNG）
- OGP画像（1200×630）
- 全ページの SEO（title/meta/canonical/OGP/Twitter Card/JSON-LD）
- レスポンシブ（PC/タブレット/SP）
- `sitemap.xml` / トップサイト制作実績への追加

### 7.2 スコープ外（別建てまたは後続）
- 独自ドメイン取得・DNS設定（標準サブドメインで公開）
- 写真撮影
- 動画・ムービー制作
- B.villea サロン集客LP独立版（本サイトで兼任）
- ロゴガイドライン（テキストロゴのみのため不要）
- お客様の声の収集代行（クライアントが用意）

### 7.3 料金プラン
- 月額3,980円 × 標準6ページ（SS-C-2026-003 範囲内）
- 初期費用・初月無料・ドメイン費別途

---

## 8. 進行スケジュール

| Day | 内容 |
|---|---|
| Day 0 | spec承認 → 実装プラン作成（writing-plans） |
| Day 1 | css/style.css 設計 + index.html 上半分（Hero / 強み / 代表ストーリー） |
| Day 2 | index.html 下半分（メニュー / Voice / FAQ抜粋 / アクセス / 会社情報 / LINE） + school / company |
| Day 3 | faq / contact / privacy + レスポンシブ調整 + SEO + 法人ロゴ作成 + OGP画像 |
| Day 3+ | クライアント確認 → 微修正 → 公開 |

mukuと同じ「最短3日完成」枠。素材未到着のところは Unsplash + プレースホルダーで先行制作、契約後素材で差し替え。

---

## 9. 連絡・確認事項

### 9.1 契約後にクライアントから受領必須
- B.villea サロンロゴ画像
- 代表（蒲池百都子）の顔写真・お仕事中の写真（aboutストーリー用、複数枚）
- サロン店内写真（雰囲気カット、施術風景）
- お客様の声 2-3件（テキスト + 可能なら写真）
- 営業時間・定休日の正確な情報
- メニューコース名・料金・所要時間
- バストスクールの内容・期間・料金（school.html用）

### 9.2 仮置きで先行制作するもの
- Hero画像 → Unsplashのブーゲンビリア・抽象的なお花画像
- 代表写真 → 一旦シルエットor抽象画像
- Voice → ダミーテキスト「※実際のお客様の声が入ります」明示
- メニュー詳細 → 「主力コース（仮）」表示

### 9.3 リスク管理
- **薬機法・景表法**: バストアップに関する「効果」断定表現は使わない。「個人の感想です」注記をVoice・FAQに必須配置
- **個人情報**: お客様の声を匿名性高く扱う（イニシャル + 年代）
- **競合表現**: 他サロンとの比較・優位表現は避ける

---

## 10. 次のステップ

このspec承認後、`superpowers:writing-plans` skillで実装プランを作成し、Day 1から実装着手する。
