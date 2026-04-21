# 開発の絶対ルール：表は狂気、裏は優等生 (Two-Face)

- **デザイン**: 既存のWebレイアウトは全面禁止。指定したコンセプトの「メタファーUI」を極限まで洗練させること。
- **SEO至上主義**: 見た目がどれだけ狂っていても、裏のHTMLはAstroでセマンティック（h1, p等）に書き、構造化データを含めること。
- **技術スタック**: Astro, Three.js, GSAP, @studio-freight/lenis
- **自律的行動**: コマンド実行（npm install等）は自律的に行い、不足している設定は自分で補うこと。

## Concept: THE WALL
- メタファー: 画面は美術館の打ち放しコンクリート壁面。作品は細い糸で吊られている。
- カラー: `#BDB9B4` concrete / `#0A0A0A` ink / `#E8E4DC` paper — 3色固定
- タイポ: Cormorant / Didot 極細 × Noto Serif JP 200 / IBM Plex Mono 300
- 余白: 画面の85%以上が「何もない壁」であること。等間隔配置は禁止。
- 質感: SVG fractalNoise + GLSL shader で生成。写真素材のテクスチャは使用禁止。
