# 開発の絶対ルール：表は狂気、裏は優等生 (Two-Face)

- **デザイン**: 既存のWebレイアウトは全面禁止。指定したコンセプトの「メタファーUI」を極限まで洗練させること。
- **SEO至上主義**: 見た目がどれだけ狂っていても、裏のHTMLはAstroでセマンティック（h1, p等）に書き、構造化データを含めること。
- **技術スタック**: Astro, Three.js, GSAP, lenis
- **自律的行動**: コマンド実行（npm install等）は自律的に行い、不足している設定は自分で補うこと。

## Concept: NOCTURNE — Contemporary Ink Art Gallery
- メタファー: 画面は深夜の展示水槽（TANK）。内部に墨絵が一点浮かび、下の水盆に新たな一滴が拡散（INK POND）。
- カラー: `#050C10` 廊下の闇 / `#1A5460` 水の青緑 / `#C4B890` 真鍮プレートの象牙 — 3色固定
- タイポ: Cormorant 極細（英） / Noto Serif JP 200（和） / IBM Plex Mono（刻印）
- 余白: 画面85%以上は「水と闇」。作品・プレートは散在、等間隔配置禁止。
- 質感: GLSL水屈折 + コースティクス + 気泡 + 墨の Navier-Stokes 風拡散。写真素材のテクスチャは使用禁止。
- HP必須: Hero / Concept / Exhibition / Artists / Program / News / Visit / Contact / Footer
