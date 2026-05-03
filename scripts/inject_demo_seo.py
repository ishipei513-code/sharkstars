"""
Inject SEO scaffolding (canonical / og:* / twitter:* / JSON-LD) into all demo
sites under demos/<slug>/index.html.

Skips:
- gallery-01, gallery-02 (Astro builds — handled separately)
- Any demo whose <head> already contains rel="canonical" or og:title

Usage:
    python scripts/inject_demo_seo.py [--dry-run] [--only slug1,slug2]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMOS = ROOT / "demos"
SITE_BASE = "https://sharkstars.jp"
FALLBACK_OGP = f"{SITE_BASE}/assist/images/ogp.png"
ASTRO_DEMOS = {"gallery-01", "gallery-02"}

# slug -> (brand_name, schema_type, has_faq)
DEMO_MAP: dict[str, tuple[str, str, bool]] = {
    "agency-01":       ("LUMIÈRE ENTERTAINMENT",  "EntertainmentBusiness",      False),
    "bakery-01":       ("Boulangerie Komugi",     "Bakery",                      False),
    "bankin-01":       ("SPEED GARAGE",           "AutoBodyShop",                False),
    "bar-01":          ("Bar NOCTURNE",           "BarOrPub",                    False),
    "cafe-01":         ("COFFEE ROASTERS",        "CafeOrCoffeeShop",            True),
    "carshop-01":      ("イイダオートサービス",    "AutoRepair",                  True),
    "cleaning-01":     ("ピカピカクリーンサービス","HomeAndConstructionBusiness", True),
    "construction-01": ("匠工房",                 "GeneralContractor",           True),
    "cooking-01":      ("Cooking Studio 旬彩",    "LocalBusiness",               True),
    "dance-01":        ("VIBE DANCE STUDIO",      "DanceSchool",                 False),
    "denki-01":        ("サンライズ電気",          "Electrician",                 True),
    "dental-01":       ("アクアデンタルクリニック","Dentist",                     False),
    "detective-01":    ("探偵事務所TRUTH",         "ProfessionalService",         False),
    "eikaiwa-01":      ("GLOBAL SPEAK 英会話スクール","EducationalOrganization",  False),
    "esthe-01":        ("LUCE",                   "BeautySalon",                 True),
    "french-01":       ("L'Étoile",               "Restaurant",                  False),
    "fudosan-01":      ("アーバンエステート株式会社","RealEstateAgent",           False),
    "fuyouhin-01":     ("クリーン・レンジャー",     "LocalBusiness",              False),
    "garden-01":       ("緑心造園",                "LocalBusiness",              True),
    "gym-01":          ("IRON CORE",              "ExerciseGym",                 True),
    "gyosei-01":       ("みらい総合行政書士事務所","ProfessionalService",         False),
    "hoikuen-01":      ("にじいろ保育園",          "Preschool",                   False),
    "influencer-01":   ("HARUKA",                 "Person",                      False),
    "itcompany-01":    ("株式会社TECH VISION",    "Organization",                False),
    "izakaya-01":      ("炭火と鮮魚 魚心",         "Restaurant",                  False),
    "juku-01":         ("みらい個別指導塾",        "EducationalOrganization",     True),
    "kaitai-01":       ("株式会社ビルド・ブレイカー","GeneralContractor",         False),
    "kitchencar-01":   ("THE BULL BURGER",        "Restaurant",                  False),
    "lawfirm-01":      ("あおぞら総合法律事務所",  "LegalService",                True),
    "lawyer-01":       ("さくら法律事務所",        "LegalService",                False),
    "matsueku-01":     ("Ciel Eyelash & Eyebrow", "BeautySalon",                 False),
    "mensep-01":       ("BLACKOUT MEN'S SALON",   "HealthAndBeautyBusiness",     False),
    "model-01":        ("Yuki Tanaka",            "Person",                      False),
    "nail-01":         ("Lumière Nail",           "BeautySalon",                 True),
    "painter-01":      ("株式会社 高橋塗装",       "HomeAndConstructionBusiness", True),
    "petsalon-01":     ("Dog Salon Fluffy",       "LocalBusiness",               True),
    "photostudio-01":  ("LUMIERE PHOTO STUDIO",   "LocalBusiness",               False),
    "piano-01":        ("アリアピアノ教室",        "MusicSchool",                 True),
    "programming-01":  ("CODE HORIZON",           "EducationalOrganization",     False),
    "ramen-01":        ("麺屋 烈火",               "Restaurant",                  False),
    "recruit-01":      ("STARTUP INC.",           "Organization",                False),
    "reform-01":       ("株式会社スマイルリフォーム","HomeAndConstructionBusiness",True),
    "restaurant-01":   ("和食レストラン 響 -HIBIKI-","Restaurant",               False),
    "salon-01":        ("Belle",                  "HairSalon",                   True),
    "seitai-01":       ("こもれび整体院",          "MedicalBusiness",             False),
    "shikaku-01":      ("QUALIA ACADEMY",         "EducationalOrganization",     False),
    "shinkyu-01":      ("堂島東洋鍼灸院",          "MedicalBusiness",             False),
    "shodo-01":        ("青柳書道教室",            "EducationalOrganization",     False),
    "soccer-01":       ("FC SHARK サッカースクール","SportsActivityLocation",     False),
    "suidou-01":       ("アクア・エマージェンシー","Plumber",                     False),
    "sushi-01":        ("鮨 銀波",                 "Restaurant",                  False),
    "tantei-01":       ("シークレット・アイ探偵事務所","ProfessionalService",     True),
    "tax-01":          ("ネクストビジョン税理士法人","AccountingService",         False),
    "vet-01":          ("あおぞら動物病院",        "VeterinaryCare",              False),
    "wagashi-01":      ("御菓子司 結心堂",         "Bakery",                      False),
    "whitening-01":    ("BLANC TEETH",            "HealthAndBeautyBusiness",     False),
    "yakiniku-01":     ("焼肉 煌",                 "Restaurant",                  False),
    "yoga-01":         ("Studio Prana",           "SportsActivityLocation",      True),
}


def html_attr_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def extract_existing(html: str) -> tuple[str | None, str | None]:
    title_m = re.search(r"<title>(.*?)</title>", html, re.S)
    desc_m = re.search(r'<meta\s+name="description"\s+content="(.*?)"\s*/?>', html, re.S | re.I)
    title = title_m.group(1).strip() if title_m else None
    desc = desc_m.group(1).strip() if desc_m else None
    return title, desc


def has_seo_already(html: str) -> bool:
    return bool(re.search(r'rel="canonical"|og:title', html, re.I))


def has_viewport(html: str) -> bool:
    return bool(re.search(r'<meta\s+name="viewport"', html, re.I))


def build_seo_block(slug: str, title: str, description: str, ogp_url: str,
                    brand: str, schema_type: str, has_faq: bool,
                    needs_viewport: bool) -> str:
    canonical = f"{SITE_BASE}/demos/{slug}/"
    title_e = html_attr_escape(title)
    desc_e = html_attr_escape(description)
    brand_e = html_attr_escape(brand)

    jsonld = {
        "@context": "https://schema.org",
        "@type": schema_type,
        "@id": f"{canonical}#org",
        "name": brand,
        "url": canonical,
        "description": description,
        "image": ogp_url,
        "inLanguage": "ja-JP",
        "areaServed": {"@type": "Country", "name": "日本"},
    }
    jsonld_str = json.dumps(jsonld, ensure_ascii=False, indent=2)

    parts = []
    if needs_viewport:
        parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    parts.extend([
        f'<link rel="canonical" href="{canonical}">',
        f'<meta property="og:title" content="{title_e}">',
        f'<meta property="og:description" content="{desc_e}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:locale" content="ja_JP">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:site_name" content="{brand_e}">',
        f'<meta property="og:image" content="{ogp_url}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title_e}">',
        f'<meta name="twitter:description" content="{desc_e}">',
        f'<meta name="twitter:image" content="{ogp_url}">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<script type="application/ld+json">\n{jsonld_str}\n</script>',
    ])
    return "\n  " + "\n  ".join(parts) + "\n"


def inject(slug: str, dry_run: bool = False) -> str:
    if slug in ASTRO_DEMOS:
        return f"SKIP {slug}: astro build"
    if slug not in DEMO_MAP:
        return f"SKIP {slug}: not in mapping"

    path = DEMOS / slug / "index.html"
    if not path.exists():
        return f"SKIP {slug}: missing index.html"

    html = path.read_text(encoding="utf-8")
    if has_seo_already(html):
        return f"SKIP {slug}: already has SEO"

    title, desc = extract_existing(html)
    if not title or not desc:
        return f"SKIP {slug}: missing title or description"

    brand, schema_type, has_faq = DEMO_MAP[slug]
    hero_local = (DEMOS / slug / "assist" / "images" / "hero.png").exists()
    yoga_hero = (DEMOS / slug / "assist" / "images" / "yoga_hero.png").exists()
    if hero_local:
        ogp_url = f"{SITE_BASE}/demos/{slug}/assist/images/hero.png"
    elif yoga_hero:
        ogp_url = f"{SITE_BASE}/demos/{slug}/assist/images/yoga_hero.png"
    else:
        ogp_url = FALLBACK_OGP

    needs_viewport = not has_viewport(html)
    block = build_seo_block(slug, title, desc, ogp_url, brand, schema_type, has_faq, needs_viewport)

    # Insert AFTER the closing > of <meta name="description" ...>
    pattern = re.compile(r'(<meta\s+name="description"\s+content="[^"]*"\s*/?>)', re.I)
    new_html, n = pattern.subn(lambda m: m.group(1) + block, html, count=1)
    if n != 1:
        return f"SKIP {slug}: could not find description tag for insertion"

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")
    return f"OK   {slug}: injected ({len(block)} bytes; brand={brand}; schema={schema_type})"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--only", help="comma-separated slug filter")
    args = p.parse_args()

    only = set(args.only.split(",")) if args.only else None
    slugs = sorted(d.name for d in DEMOS.iterdir() if d.is_dir())
    results = []
    for slug in slugs:
        if only and slug not in only:
            continue
        results.append(inject(slug, dry_run=args.dry_run))
    for r in results:
        print(r)
    print(f"\nTotal: {len(results)} processed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
