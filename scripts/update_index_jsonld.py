#!/usr/bin/env python3
"""Replace index.html Organization+FAQ JSON-LD block with expanded AIO schema.

Idempotent: matches on the opening `<!-- Organization Schema -->` comment and
the closing `</script>` that follows the 4-item FAQ block, swapping the whole
range for the new multi-schema block.
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"

NEW_BLOCK = """  <!-- Organization / LocalBusiness Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": ["Organization", "LocalBusiness", "ProfessionalService"],
    "@id": "https://sharkstars.jp/#organization",
    "name": "SHARKSTARS",
    "alternateName": "シャークスターズ",
    "url": "https://sharkstars.jp/",
    "logo": {"@type": "ImageObject", "url": "https://sharkstars.jp/assist/images/favicon.png"},
    "image": "https://sharkstars.jp/assist/images/ogp.png",
    "description": "福岡拠点の月額制ホームページ制作サービス。初期費用0円・月額3,980円（税込）でサーバー・独自ドメイン・SSL・保守・SEO対策までワンストップ。1週間前後で完成（公開）。",
    "slogan": "初期費用0円・月額3,980円で始める月額制ホームページ",
    "priceRange": "¥3,980/month",
    "currenciesAccepted": "JPY",
    "paymentAccepted": "Credit Card",
    "address": {"@type": "PostalAddress", "addressRegion": "福岡県", "addressCountry": "JP"},
    "areaServed": [
      {"@type": "AdministrativeArea", "name": "福岡県"},
      {"@type": "AdministrativeArea", "name": "福岡市"},
      {"@type": "AdministrativeArea", "name": "北九州市"},
      {"@type": "Country", "name": "日本"}
    ],
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "customer service",
      "email": "sharkstars0513@gmail.com",
      "availableLanguage": ["Japanese"]
    },
    "founder": {
      "@type": "Person",
      "@id": "https://sharkstars.jp/company.html#founder",
      "name": "石橋昇平",
      "jobTitle": "代表・Webディレクター",
      "knowsAbout": ["ホームページ制作", "SEO対策", "MEO対策", "Webマーケティング", "月額制HP制作"],
      "description": "Web制作・SEO/MEO対策 実務8年。福岡の中小企業・個人事業主のデジタル集客を支援。"
    },
    "sameAs": ["https://sharkstars.jp/company.html"]
  }
  </script>

  <!-- WebSite Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": "https://sharkstars.jp/#website",
    "url": "https://sharkstars.jp/",
    "name": "SHARKSTARS",
    "description": "福岡の月額制ホームページ制作サービス",
    "publisher": {"@id": "https://sharkstars.jp/#organization"},
    "inLanguage": "ja-JP"
  }
  </script>

  <!-- Service Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Service",
    "@id": "https://sharkstars.jp/#service",
    "serviceType": "月額制ホームページ制作",
    "name": "SHARKSTARS 月額制ホームページ制作サービス",
    "description": "初期費用0円・月額3,980円（税込）で、サーバー代・独自ドメイン・SSL証明書・保守管理・SEO対策・月1回の軽微な更新までワンストップで提供する月額制HP制作サービス。1週間前後で完成（公開）、50種類以上のデザインテンプレートから選択可能。",
    "provider": {"@id": "https://sharkstars.jp/#organization"},
    "areaServed": {"@type": "AdministrativeArea", "name": "福岡県"},
    "audience": {"@type": "BusinessAudience", "audienceType": "中小企業・個人事業主・開業間もない事業者"},
    "offers": {
      "@type": "Offer",
      "price": "3980",
      "priceCurrency": "JPY",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "price": "3980",
        "priceCurrency": "JPY",
        "unitCode": "MON",
        "name": "月額（税込）"
      },
      "availability": "https://schema.org/InStock",
      "url": "https://sharkstars.jp/#pricing",
      "validFrom": "2025-01-01",
      "eligibleDuration": {"@type": "QuantitativeValue", "value": 12, "unitCode": "MON"}
    },
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "対応業種",
      "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "飲食店ホームページ制作"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "美容室・サロンホームページ制作"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "建設業・工務店ホームページ制作"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "整体院ホームページ制作"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "士業ホームページ制作"}},
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "個人事業主ホームページ制作"}}
      ]
    }
  }
  </script>

  <!-- BreadcrumbList (Top) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://sharkstars.jp/"}
    ]
  }
  </script>

  <!-- FAQ Structured Data (synced with #faq section, 9 items) -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {"@type": "Question", "name": "本当に月額3,980円（税込）以外かかりませんか？", "acceptedAnswer": {"@type": "Answer", "text": "はい、月額3,980円（税込）以外に追加費用は一切かかりません。サーバー代・独自ドメインの取得・更新費・SSL証明書・月1回のテキスト変更・画像変更もすべて含まれています。ただし、大幅なデザイン変更やページ追加をされる場合は、別途オプション料金のご相談をさせていただく場合がございます。"}},
      {"@type": "Question", "name": "途中でデザインをガラッと変えられますか？", "acceptedAnswer": {"@type": "Answer", "text": "テキストや画像の差し替えは月1回まで無料で対応いたします。テンプレートの大幅な変更（別デザインへの切り替え等）は、別途オプション料金にて承ります。まずはお気軽にご相談ください。"}},
      {"@type": "Question", "name": "パソコンが苦手なのですが大丈夫ですか？", "acceptedAnswer": {"@type": "Answer", "text": "もちろん大丈夫です。LINEでのやりとりが中心ですので、スマホからお写真を送っていただくだけで完結します。パソコンの操作は一切不要です。"}},
      {"@type": "Question", "name": "解約したい場合はどうすればいいですか？", "acceptedAnswer": {"@type": "Answer", "text": "最低契約期間は12ヶ月です。12ヶ月未満での途中解約の場合、残存期間×月額3,980円（税込）の違約金が発生いたします。12ヶ月経過後はいつでも解約可能で、違約金はございません。解約のお申し出は1ヶ月前までにお願いいたします。サイトデータの買い取りをご希望の場合は、別途50,000円（税込）にてHTML/CSSファイル一式をお渡しすることも可能です。"}},
      {"@type": "Question", "name": "どのくらいでホームページが完成しますか？", "acceptedAnswer": {"@type": "Answer", "text": "素材（写真・テキスト）をいただいてから1週間前後で完成します。確認のやりとりを含めても、通常2週間以内には公開可能です。"}},
      {"@type": "Question", "name": "独自ドメイン（.comや.jpなど）は使えますか？", "acceptedAnswer": {"@type": "Answer", "text": "御社専用の独自ドメイン（.comや.jpなど）を標準でご用意します。取得・DNS設定・独自SSL・管理はすべて弊社が代行し、通常のドメインであれば取得費・年間更新費も月額3,980円（税込）に含まれます（追加費用なし）。お客様はご希望のドメイン名を選ぶだけです。市場で特に高額なプレミアムドメインのみ、実費を別途申し受けます。"}},
      {"@type": "Question", "name": "インボイス制度（適格請求書）に対応していますか？", "acceptedAnswer": {"@type": "Answer", "text": "現在のところ、インボイス制度（適格請求書発行事業者）への登録は行っておりません。あらかじめご了承いただきますようお願い申し上げます。"}},
      {"@type": "Question", "name": "支払い方法を教えてください。", "acceptedAnswer": {"@type": "Answer", "text": "お支払いはクレジットカード決済（Stripe）のみとなっております。毎月自動引き落としのため、お振込みの手間は一切ございません。Stripeの管理画面より領収書・請求書のダウンロードが可能です。"}},
      {"@type": "Question", "name": "2年目以降も月額3,980円のままですか？", "acceptedAnswer": {"@type": "Answer", "text": "はい、2年目以降もずっと月額3,980円（税込）のままです。値上げはございません。契約は1年ごとの更新制となっており、更新の約1ヶ月前に継続のご確認をさせていただきます。更新時に解約いただくことも可能です。"}}
    ]
  }
  </script>
"""

def main():
    html = INDEX.read_text(encoding="utf-8")
    # Match from the Organization Schema comment up through the FAQ script close.
    pattern = re.compile(
        r"[ \t]*<!--\s*Organization Schema\s*-->\s*\n"
        r".*?"  # everything in between
        r"<script type=\"application/ld\+json\">\s*\n\s*\{\s*\n\s*\"@context\":\s*\"https://schema\.org\",\s*\n\s*\"@type\":\s*\"FAQPage\""
        r".*?</script>\s*\n",
        re.DOTALL,
    )
    m = pattern.search(html)
    if not m:
        if '"@id": "https://sharkstars.jp/#organization"' in html:
            print("Already patched. No-op.")
            return 0
        print("ERROR: could not locate old Organization+FAQ block.", file=sys.stderr)
        return 1
    new_html = html[:m.start()] + NEW_BLOCK + html[m.end():]
    INDEX.write_text(new_html, encoding="utf-8")
    print(f"Patched: {INDEX}")
    print(f"Replaced {m.end() - m.start()} bytes with {len(NEW_BLOCK)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
