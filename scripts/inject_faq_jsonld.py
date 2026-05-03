"""
Add FAQPage JSON-LD to demos that have visible FAQ sections.

Extracts <details>...<summary>Q</summary>...<p>A</p>...</details> from index.html
and emits a FAQPage schema block right after the existing JSON-LD script.

Skips demos that already have FAQPage in any JSON-LD.
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMOS = ROOT / "demos"

FAQ_DEMOS = {
    "cafe-01", "carshop-01", "cleaning-01", "construction-01", "cooking-01",
    "denki-01", "esthe-01", "garden-01", "gym-01", "juku-01", "lawfirm-01",
    "nail-01", "painter-01", "petsalon-01", "piano-01", "reform-01", "salon-01",
    "tantei-01", "yoga-01",
    "restaurant-01", "lawyer-01", "detective-01",
}


def strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = html_lib.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def extract_faqs(html: str) -> list[tuple[str, str]]:
    """Extract Q/A pairs from common FAQ markup patterns."""
    pairs: list[tuple[str, str]] = []

    # Pattern 1: <details>...<summary>Q</summary>BODY</details>
    for body in re.findall(r"<details[^>]*>(.*?)</details>", html, re.S | re.I):
        sm = re.search(r"<summary[^>]*>(.*?)</summary>", body, re.S | re.I)
        if not sm:
            continue
        q = strip_tags(sm.group(1))
        a = strip_tags(body[sm.end():])
        if q and a:
            pairs.append((q, a))
    if pairs:
        return pairs

    # Pattern 2: zip faq-q / faq-a found sequentially in document order.
    q_re = re.compile(r'<(button|div|h\d)[^>]*class="[^"]*\bfaq-q\b[^"]*"[^>]*>(.*?)</\1>',
                       re.S | re.I)
    a_re = re.compile(r'<div[^>]*class="[^"]*\bfaq-a\b[^"]*"[^>]*>(.*?)(?=<div[^>]*class="[^"]*\bfaq-(?:q|item)\b|<button[^>]*class="[^"]*\bfaq-q\b|</section)',
                       re.S | re.I)
    qs = [strip_tags(m.group(2)) for m in q_re.finditer(html)]
    answers_raw = [m.group(1) for m in a_re.finditer(html)]
    answers = [strip_tags(re.sub(r'<div[^>]*class="[^"]*\bfaq-a-inner\b[^"]*"[^>]*>', '', a)) for a in answers_raw]
    if qs and len(qs) == len(answers):
        for q, a in zip(qs, answers):
            if q and a:
                pairs.append((q, a))
    if pairs:
        return pairs

    # Pattern 3: <div class="q-item"><h4>Q...</h4><p>A...</p></div>
    for body in re.findall(r'<div\s+class="[^"]*\bq-item\b[^"]*"[^>]*>(.*?)</div>',
                            html, re.S | re.I):
        qm = re.search(r"<h\d[^>]*>(.*?)</h\d>", body, re.S | re.I)
        am = re.search(r"<p[^>]*>(.*?)</p>", body, re.S | re.I)
        if qm and am:
            q = strip_tags(qm.group(1))
            a = strip_tags(am.group(1))
            # Trim leading "Q." / "A." prefix
            q = re.sub(r"^Q\.?\s*", "", q)
            a = re.sub(r"^A\.?\s*", "", a)
            if q and a:
                pairs.append((q, a))
    return pairs


def has_faqpage(html: str) -> bool:
    return '"FAQPage"' in html or "'FAQPage'" in html


def inject(slug: str, dry_run: bool = False) -> str:
    if slug not in FAQ_DEMOS:
        return f"SKIP {slug}: not in FAQ list"
    path = DEMOS / slug / "index.html"
    if not path.exists():
        return f"SKIP {slug}: no index.html"

    html = path.read_text(encoding="utf-8")
    if has_faqpage(html):
        return f"SKIP {slug}: already has FAQPage"

    faqs = extract_faqs(html)
    if not faqs:
        return f"SKIP {slug}: no <details> faq pairs found"

    block = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }
    block_str = (
        "\n  <script type=\"application/ld+json\">\n"
        + json.dumps(block, ensure_ascii=False, indent=2)
        + "\n  </script>\n"
    )

    # Insert after the existing closing </script> of the first JSON-LD block.
    pattern = re.compile(r"(<script\s+type=\"application/ld\+json\">.*?</script>)", re.S | re.I)
    new_html, n = pattern.subn(lambda m: m.group(1) + block_str, html, count=1)
    if n != 1:
        return f"SKIP {slug}: no existing JSON-LD block to anchor on"

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")
    return f"OK   {slug}: added FAQPage with {len(faqs)} questions"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    for slug in sorted(FAQ_DEMOS):
        print(inject(slug, dry_run=args.dry_run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
