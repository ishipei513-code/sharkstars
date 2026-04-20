"""Fix malformed Unsplash URLs where two URLs got concatenated.

Pattern:
  src="https://images.unsplash.com/photo-AAA?ixlibhttps://images.unsplash.com/photo-BBB?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"

Keep the second (complete) URL; drop the first malformed half.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMOS = ROOT / "demos"

PAT = re.compile(
    r"https://images\.unsplash\.com/photo-[A-Za-z0-9_-]+\?ixlib"
    r"(https://images\.unsplash\.com/)"
)

total_fixed = 0
files_touched = []
for html in DEMOS.rglob("index.html"):
    text = html.read_text(encoding="utf-8")
    new_text, n = PAT.subn(r"\1", text)
    if n:
        html.write_text(new_text, encoding="utf-8")
        total_fixed += n
        files_touched.append((html.relative_to(ROOT), n))

for f, n in files_touched:
    print(f"{f}: {n}")
print(f"TOTAL: {total_fixed} fixes across {len(files_touched)} files")
