"""Add og:image meta tag to blog HTML files that lack one.

Inserts the tag immediately after the existing og:url line, pointing at the
shared SHARKSTARS OGP image.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
OG_IMAGE_TAG = '  <meta property="og:image" content="https://sharkstars.jp/assist/images/ogp.png">\n'

touched = []
skipped = []
for html in sorted(BLOG.glob("*.html")):
    text = html.read_text(encoding="utf-8")
    if "og:image" in text:
        skipped.append(html.name)
        continue
    m = re.search(r'^(\s*<meta property="og:url"[^>]*>\s*\n)', text, re.MULTILINE)
    if not m:
        skipped.append(f"{html.name} (no og:url anchor)")
        continue
    new_text = text[:m.end()] + OG_IMAGE_TAG + text[m.end():]
    html.write_text(new_text, encoding="utf-8")
    touched.append(html.name)

print("Added og:image to:")
for f in touched:
    print(f"  {f}")
print(f"Skipped: {len(skipped)} -> {skipped}")
print(f"TOTAL: {len(touched)} files updated")
