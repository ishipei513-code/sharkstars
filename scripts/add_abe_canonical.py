"""Add rel=canonical to abe-seitai subpages that lack one.

Uses the existing og:url value on each page as the canonical target.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "client" / "abe-seitai"
TARGETS = ["about.html", "service.html", "faq.html", "contact.html", "privacy.html"]

for name in TARGETS:
    path = SITE / name
    text = path.read_text(encoding="utf-8")
    if 'rel="canonical"' in text:
        print(f"{name}: already has canonical, skipping")
        continue
    m = re.search(r'<meta property="og:url" content="([^"]+)"\s*/?>', text)
    if not m:
        print(f"{name}: no og:url found, skipping")
        continue
    url = m.group(1)
    og_line = m.group(0)
    canonical = f'<link rel="canonical" href="{url}">'
    new_text = text.replace(og_line, f'{canonical}\n  {og_line}', 1)
    path.write_text(new_text, encoding="utf-8")
    print(f"{name}: added canonical -> {url}")
