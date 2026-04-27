# KOJP — 韓国企業の日本市場進出支援サイト

> SEO + AEO + GEO + MEO 統合サービスのコーポレートサイト

## 技術スタック

- **HTML5** + **CSS3** + **Vanilla JavaScript**（フレームワーク不使用）
- **フォント**: Pretendard (CDN)
- **アイコン**: Lucide Icons (CDN)
- **デプロイ先**: Cloudflare Pages

## デザインDNA

5サイト融合戦略:
1. **Toss** — パステル、友好的タイポ
2. **Tamburins** — エディトリアル、マガジン的
3. **Aesop** — 余白、抑制、品格
4. **Plus X** — 建築的構成、強活字
5. **Linear** — 微細ホバー、滑らかアニメ

## ページ構成

| パス | 状態 | 内容 |
|---|---|---|
| `/` | ✅ 実装済 | トップページ（10セクション） |
| `/pricing/` | ✅ 実装済 | 料金プラン（3プラン比較） |
| `/free-diagnosis/` | ✅ 実装済 | 無料診断申込（フォーム+バリデーション） |
| `/contact/` | ✅ 実装済 | お問い合わせ（フォーム+連絡手段） |
| `/legal/privacy/` | ✅ 実装済 | プライバシーポリシー |
| `/services/` | 🔲 テンプレート | サービス一覧 |
| `/services/seo/` | 🔲 テンプレート | SEO詳細 |
| `/services/aeo/` | 🔲 テンプレート | AEO詳細 |
| `/services/geo/` | 🔲 テンプレート | GEO詳細 |
| `/services/meo/` | 🔲 テンプレート | MEO詳細 |
| `/about/` | 🔲 テンプレート | 会社概要 |
| `/case-studies/` | 🔲 テンプレート | 導入事例 |
| `/blog/` | 🔲 テンプレート | ブログ |
| `/ko/` | 🔲 テンプレート | 韓国語版 |

## SEO/AIO 対応

- ✅ hreflang (ja-JP, ko-KR, x-default)
- ✅ canonical
- ✅ Open Graph / Twitter Card
- ✅ JSON-LD (Organization, WebSite, FAQPage, BreadcrumbList, Service)
- ✅ sitemap.xml
- ✅ robots.txt
- ✅ llms.txt (AI検索最適化)

## ローカル開発

```bash
cd website
npx serve .
```

ブラウザで `http://localhost:3000` を開く。

## デプロイ手順（Cloudflare Pages）

### 1. リポジトリ連携

1. Cloudflare Dashboard → Pages → 「Create a project」
2. GitHub / GitLab リポジトリを連携
3. ビルド設定:
   - **Framework preset**: None
   - **Build command**: （空欄）
   - **Build output directory**: `website`
   - **Root directory**: `./`

### 2. カスタムドメイン

1. Pages プロジェクト → Custom domains
2. `sharkstars.jp` を追加
3. DNS設定で CNAME レコードを追加
4. パス `/kojp/` でサブディレクトリ配信

### 3. 環境変数（不要）

静的サイトのため環境変数は不要。

### 4. デプロイ後の確認

```
✅ https://sharkstars.jp/kojp/ が正常表示
✅ https://sharkstars.jp/kojp/sitemap.xml がアクセス可能
✅ https://sharkstars.jp/kojp/robots.txt がアクセス可能
✅ https://sharkstars.jp/kojp/llms.txt がアクセス可能
✅ _headers のセキュリティヘッダーが適用
✅ 404ページが表示される
```

## ファイル構成

```
website/
├── index.html              # トップページ
├── 404.html                # 404エラーページ
├── sitemap.xml
├── robots.txt
├── llms.txt
├── _headers                # Cloudflare セキュリティヘッダー
├── _redirects              # Cloudflare リダイレクト
├── assets/
│   ├── css/
│   │   ├── main.css        # メインスタイルシート
│   │   ├── reset.css
│   │   ├── variables.css   # デザイントークン
│   │   ├── components.css  # 共通コンポーネント
│   │   ├── animations.css
│   │   ├── layout.css      # ヘッダー/フッター/レイアウト
│   │   └── pages/          # ページ固有CSS
│   ├── javascript/
│   │   ├── main.js         # メインJS（アニメーション等）
│   │   ├── components.js   # ヘッダー/フッター動的挿入
│   │   └── form-validation.js
│   └── img/
├── pricing/index.html
├── free-diagnosis/index.html
├── contact/index.html
├── legal/privacy/index.html
└── ...
```
