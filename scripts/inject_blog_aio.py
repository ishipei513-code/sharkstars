#!/usr/bin/env python3
"""Inject AIO metadata + structured data into blog/*.html.

For each blog article:
  1. Insert <link rel="canonical"> (if missing)
  2. Insert Twitter Card meta tags (if missing)
  3. Replace Article/BlogPosting author Organization -> Person (石橋昇平)
  4. Append BreadcrumbList JSON-LD (if missing)

For blog/index.html additionally:
  - Add Blog + ItemList JSON-LD listing every article

Idempotent: skips work that's already been applied.
Run from repo root:  python scripts/inject_blog_aio.py
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOG = ROOT / "blog"
BASE_URL = "https://sharkstars.jp"

TITLE_FALLBACK = "ブログ記事"

PERSON_AUTHOR = {
    "@type": "Person",
    "@id": f"{BASE_URL}/company.html#founder",
    "name": "石橋昇平",
    "url": f"{BASE_URL}/company.html",
    "jobTitle": "代表・Webディレクター",
    "knowsAbout": ["ホームページ制作", "SEO対策", "MEO対策", "Webマーケティング"],
}


def extract_title(html: str, fname: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if m:
        t = m.group(1).strip()
        # strip " | SHARKSTARS..." suffix
        t = re.split(r"\s*[|｜]\s*SHARKSTARS", t)[0].strip()
        return t or fname
    return fname


def inject_canonical_and_twitter(html: str, url: str, title: str, fname: str) -> tuple[str, bool]:
    changed = False
    inject = []
    if 'rel="canonical"' not in html and "rel='canonical'" not in html:
        inject.append(f'  <link rel="canonical" href="{url}">')
        changed = True
    if 'name="twitter:card"' not in html and "name='twitter:card'" not in html:
        desc_m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', html)
        desc = desc_m.group(1) if desc_m else "SHARKSTARSのブログ記事"
        og_img = (
            re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html).group(1)
            if re.search(r'<meta[^>]+property="og:image"', html)
            else f"{BASE_URL}/assist/images/ogp.png"
        )
        tc = [
            f'  <meta name="twitter:card" content="summary_large_image">',
            f'  <meta name="twitter:title" content="{title}">',
            f'  <meta name="twitter:description" content="{desc}">',
            f'  <meta name="twitter:image" content="{og_img}">',
            f'  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">',
        ]
        inject.extend(tc)
        changed = True
    if not changed:
        return html, False
    # Insert right before </head>
    return html.replace("</head>", "\n".join(inject) + "\n</head>", 1), True


def replace_author_with_person(html: str) -> tuple[str, bool]:
    """Replace the Article author block (Organization) with Person.

    Finds the Article/BlogPosting JSON-LD and swaps "author": {...Organization...}
    for a Person block. Keeps publisher intact.
    """
    if '"@id": "https://sharkstars.jp/company.html#founder"' in html:
        return html, False  # already patched

    # Match: "author": { "@type": "Organization", ... } up to balanced closing brace
    pattern = re.compile(
        r'"author":\s*\{\s*"@type":\s*"Organization",(?:[^{}]|\{[^{}]*\})*?\}',
        re.DOTALL,
    )
    new_author = '"author": ' + json.dumps(PERSON_AUTHOR, ensure_ascii=False, indent=None)
    new_html, n = pattern.subn(new_author, html, count=1)
    return new_html, n > 0


def append_breadcrumb(html: str, url: str, title: str) -> tuple[str, bool]:
    if '"@type": "BreadcrumbList"' in html:
        return html, False
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ホーム", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "ブログ", "item": f"{BASE_URL}/blog/"},
            {"@type": "ListItem", "position": 3, "name": title, "item": url},
        ],
    }
    block = (
        '  <script type="application/ld+json">\n'
        + json.dumps(breadcrumb, ensure_ascii=False, indent=2).replace("\n", "\n  ")
        + "\n  </script>\n"
    )
    return html.replace("</head>", block + "</head>", 1), True


def build_blog_itemlist_html(articles: list[tuple[str, str]]) -> str:
    """articles = list of (url, title)"""
    itemlist = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": f"{BASE_URL}/blog/#blog",
        "url": f"{BASE_URL}/blog/",
        "name": "SHARKSTARS ブログ",
        "description": "福岡の中小企業・個人事業主向けにホームページ制作・SEO・MEO・Web集客の実践ノウハウを発信。",
        "publisher": {"@id": f"{BASE_URL}/#organization"},
        "inLanguage": "ja-JP",
        "blogPost": [
            {"@type": "BlogPosting", "headline": t, "url": u} for (u, t) in articles
        ],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "ホーム", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "ブログ", "item": f"{BASE_URL}/blog/"},
        ],
    }
    return (
        '  <script type="application/ld+json">\n'
        + json.dumps(itemlist, ensure_ascii=False, indent=2).replace("\n", "\n  ")
        + "\n  </script>\n"
        + '  <script type="application/ld+json">\n'
        + json.dumps(breadcrumb, ensure_ascii=False, indent=2).replace("\n", "\n  ")
        + "\n  </script>\n"
    )


def process_article(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")
    original = html
    fname = path.name
    url = f"{BASE_URL}/blog/{fname}"
    title = extract_title(html, fname)

    results = {"file": fname, "title": title}

    html, c1 = inject_canonical_and_twitter(html, url, title, fname)
    results["canonical_twitter"] = c1

    html, c2 = replace_author_with_person(html)
    results["author_person"] = c2

    html, c3 = append_breadcrumb(html, url, title)
    results["breadcrumb"] = c3

    if html != original:
        path.write_text(html, encoding="utf-8")
        results["written"] = True
    else:
        results["written"] = False
    return results


def process_blog_index(path: Path, articles: list[tuple[str, str]]) -> dict:
    html = path.read_text(encoding="utf-8")
    original = html
    results = {"file": "index.html"}

    html, c1 = inject_canonical_and_twitter(
        html, f"{BASE_URL}/blog/", "ブログ | SHARKSTARS", "index.html"
    )
    results["canonical_twitter"] = c1

    if '"@type": "Blog"' in html and '"@type": "BreadcrumbList"' in html:
        results["blog_itemlist"] = False
    else:
        block = build_blog_itemlist_html(articles)
        html = html.replace("</head>", block + "</head>", 1)
        results["blog_itemlist"] = True

    if html != original:
        path.write_text(html, encoding="utf-8")
        results["written"] = True
    else:
        results["written"] = False
    return results


def main():
    article_files = sorted(
        p for p in BLOG.glob("*.html") if p.name != "index.html"
    )
    summary = []
    articles_for_index: list[tuple[str, str]] = []
    for p in article_files:
        r = process_article(p)
        summary.append(r)
        articles_for_index.append((f"{BASE_URL}/blog/{p.name}", r["title"]))

    idx = process_blog_index(BLOG / "index.html", articles_for_index)
    summary.append(idx)

    for r in summary:
        flags = []
        for k in ("canonical_twitter", "author_person", "breadcrumb", "blog_itemlist"):
            if r.get(k):
                flags.append(k)
        print(f"{r['file']:40s} written={r['written']} patched={','.join(flags) or '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
