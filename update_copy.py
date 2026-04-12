import re

file_path = r'd:\sharkstars\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. HERO MAIN COPY
text = re.sub(
    r'<h1 class="hero-title">.*?</h1>',
    '<h1 class="hero-title">\n          初期費用0円。<br>\n          あなたのお店に、<br>\n          プロ品質のWebサイトを。\n        </h1>',
    text,
    flags=re.DOTALL
)

# 1. HERO SUB COPY
text = re.sub(
    r'<p class="hero-subtitle">.*?50種類のデモから選ぶだけで、最短3日で公開。.*?</p>',
    '<p class="hero-subtitle">\n          ずっと月額5,000円（税込5,500円）のみ。サーバー代も、面倒な保守管理もすべてお任せください。<br>\n          50種類以上のデザインから選ぶだけで、最短3日であなたのビジネスがWeb上に誕生します。\n        </p>',
    text,
    flags=re.DOTALL
)

# 1. HERO BADGE
text = re.sub(
    r'<div class="hero-badge">\s*<span class="hero-badge-dot"></span>\s*新規お申し込み受付中\s*</div>',
    '<div class="hero-badge">\n          ＼ 専門知識は一切不要 ／\n        </div>',
    text,
    flags=re.DOTALL
)

# 2. PROBLEMS HEADING
text = re.sub(
    r'<h2 class="section-title fade-in">こんなお悩み、ありませんか？</h2>',
    '<h2 class="section-title fade-in">Webサイトのことで、こんなモヤモヤを抱えていませんか？</h2>',
    text
)

# 2. PROBLEMS LIST
old_problems = r'<div class="thought-bubbles">\s*<div class="thought-bubble">HP作成したいな・・・</div>\s*<div class="thought-bubble">費用高いな・・・</div>\s*<div class="thought-bubble">自分の社名、サービス名でググっても上位に表示されない</div>\s*<div class="thought-bubble">HPを新しくしたいな・・・</div>\s*<div class="thought-bubble">Googleマップ入れたいな・・・</div>\s*</div>'
new_problems = '''<div class="thought-bubbles">
          <div class="thought-bubble">「ホームページは欲しいけど、初期費用が高すぎる…」</div>
          <div class="thought-bubble">「維持費や更新料など、後から不透明な請求が来ないか不安」</div>
          <div class="thought-bubble">「社名やお店の名前で検索しても、何も出てこない」</div>
          <div class="thought-bubble">「今のサイトが古くてスマホで見づらい。リニューアルしたい」</div>
          <div class="thought-bubble">「パソコンが苦手で、自分で作ったり管理したりするのは無理」</div>
        </div>'''
text = re.sub(old_problems, new_problems, text)

# 2. PROBLEMS ANSWER
old_prob_alert = r'<div class="problems-alert">.*?<span class="small-note">※既存のコードは全てリニューアルします。</span></p>\s*</div>\s*</div>'
new_prob_alert = '''<div class="problems-alert">
          <p class="alert-lead">
            専門知識の壁につけ込むような、<br>
            <span class="highlight-red">高額な制作契約やSEO対策に消耗するのは終わりにしましょう。</span>
          </p>
          <div class="alert-action">
            <p>SHARKSTARSなら、適正価格で高品質なWeb環境への<br><strong>「新規開設」も「乗り換え」もスムーズです。</strong></p>
          </div>
        </div>'''
text = re.sub(old_prob_alert, new_prob_alert, text, flags=re.DOTALL)

# 3. REASONS 
text = text.replace(
    '<h3 class="reason-title">初期費用ゼロの明朗会計</h3>',
    '<h3 class="reason-title">追加請求なし。初期費用ゼロの「完全定額制」</h3>'
)
text = text.replace(
    '<p class="reason-desc">\n            ずっと月額5,000円（税込5,500円）のみ。サーバー代やドメイン維持費も込み。追加料金の心配は一切ありません。\n          </p>',
    '<p class="reason-desc">\n            ずっと月額5,000円（税込5,500円）のワンプラン。サーバー代や独自ドメイン維持費、SSL化（セキュリティ対策）まで全て込み。目に見えない追加費用の心配は一切ありません。\n          </p>'
)

text = text.replace(
    '<h3 class="reason-title">選んで渡すだけで完成</h3>',
    '<h3 class="reason-title">デザインを選んで、写真と文章を「渡すだけ」</h3>'
)
text = text.replace(
    '<p class="reason-desc">\n            豊富なデモサイトからデザインを選んで、写真と文章を送るだけ。難しい操作は一切不要です。\n          </p>',
    '<p class="reason-desc">\n            50種類以上のハイクオリティなデモサイトから、お店のイメージに合うものを選ぶだけ。あとは写真と文章をLINEやメールで送付いただければ、プロが綺麗に組み上げます。\n          </p>'
)

text = text.replace(
    '<h3 class="reason-title">面倒な管理はすべてお任せ</h3>',
    '<h3 class="reason-title">サーバーもセキュリティも「完全丸投げ」でOK</h3>'
)
text = text.replace(
    '<p class="reason-desc">\n            サーバー保守・セキュリティ対策から月1回の軽微な更新まで、運用に必要なことは全てお任せください。\n          </p>',
    '<p class="reason-desc">\n            専門的な保守管理、システム監視、万が一のトラブル対応などは全て弊社が代行します。お客様は本業であるビジネスに専念していただけます。\n          </p>'
)

# 4. PRICING
text = text.replace(
    '<p>月額費用は「Web上の店舗の家賃（サーバー・維持管理等）と警備代（セキュリティ対策）」として頂戴しております。<br class="sp-none">使わない機能や過剰なサービスを省いた、誠実な限界価格です。</p>',
    '<p>※月額費用は「Web上の店舗の家賃（サーバー代等）と警備代（セキュリティ維持）」として頂戴しております。<br class="sp-none">使わない機能への上乗せを極限まで削ぎ落とした、誠実な限界価格です。</p>'
)
# Wait, let's use a regex to be safe about the pricing note
text = re.sub(
    r'<div class="pricing-note-box">\s*<p>.*?</div>',
    '<div class="pricing-note-box">\n          <p>※月額費用は「Web上の店舗の家賃（サーバー代等）と警備代（セキュリティ維持）」として頂戴しております。<br class="sp-none">使わない機能への上乗せを極限まで削ぎ落とした、誠実な限界価格です。</p>\n        </div>',
    text,
    flags=re.DOTALL
)

# PRICING STANDARD FEATURES
old_std = r'<div class="pricing-details-grid">.*?<div class="pricing-detail-box option-box fade-in">'
new_std = '''<div class="pricing-details-grid">
        
        <div class="pricing-detail-box fade-in">
          <h3 class="detail-title">初期0円で叶う<br>「基本の5ページ」</h3>
          <p class="detail-desc">標準的な構成で、最短3日で開設可能。</p>
          <ul class="detail-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>トップページ</strong><span>デザイン一覧から選ぶだけ</span></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>サービス紹介 / 料金</strong></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>会社概要 / 店舗情報（Map込）</strong></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>お問い合わせ（LINE/メール）</strong></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>フリーページ（1P選択）</strong><span>よくある質問、事例、各種規約など</span></div></li>
          </ul>
        </div>

        <div class="pricing-detail-box fade-in" style="animation-delay: 0.1s;">
          <h3 class="detail-title">他社なら有料級の<br>「最強・標準装備」</h3>
          <p class="detail-desc">見えない部分まで徹底サポート。</p>
          <ul class="detail-list highlight-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>プロの内部SEO対策</strong><span>検索エンジンに評価される構造化</span></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>SNS・LINE連携（OGP）</strong><span>シェアした時に綺麗なサムネイル表示</span></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>ストレスゼロの高速表示</strong><span>サクサク動く最新Web技術の実装</span></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>スマホ完全対応 (レスポンシブ)</strong></div></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg> <div><strong>SSL通信 (セキュリティ対策)</strong></div></li>
          </ul>
        </div>

        <div class="pricing-detail-box option-box fade-in">'''
text = re.sub(old_std, new_std, text, flags=re.DOTALL)

# PRICING OPTION NOTE
# Replace the optional update note with the "Why so cheap?" note
old_opt = r'<div class="pricing-detail-box option-box fade-in">.*?</div>\s*</div>\s*</section>'
new_opt = '''<div class="pricing-detail-box option-box fade-in" style="animation-delay: 0.2s;">
          <h3 class="detail-title">💡 なぜここまで安いのか？</h3>
          <ul class="detail-list">
            <li><div>一般的な制作会社では、実際には行わない「更新作業」を名目に高額な月額費用を請求するケースが見受けられます。<br><br>SHARKSTARSは維持管理に必要な実費のみを月額とし、テキスト変更などは「必要な時に、必要な分だけ」お支払いいただく明朗会計を採用しています。無駄な中間マージンを排除し、誠実な価格でサービスを提供し続けます。</div></li>
          </ul>
        </div>
      </div>
    </div>
  </section>'''
text = re.sub(old_opt, new_opt, text, flags=re.DOTALL)

# 5. FLOW / CONTACT
text = text.replace(
    'まずはお気軽にご連絡ください。「こんなサイト作れる？」といったご相談でも大歓迎です。',
    'まずはお気軽にご連絡ください。「こんなサイト作れる？」「乗り換えの相談に乗ってほしい」といったご相談も大歓迎です。無理な営業は一切行いません。'
)

text = re.sub(
    r'<h3 class="contact-info-title"[^>]*>LINEで気軽に無料相談 🎯</h3>\s*<p class="contact-info-desc"[^>]*>.*?公式LINEで無料相談',
    '''<h3 class="contact-info-title" style="margin-bottom: 24px;">LINEで気軽に無料相談 🎯</h3>
          <p class="contact-info-desc" style="margin-bottom: 32px;">
            <strong style="color: #d12e2e; display: block; margin-bottom: 8px;">＼ スマホから1分で完了 ／ 最も選ばれているご連絡方法です。</strong>
            個人店オーナー様・職人の皆様に一番人気のご連絡方法です。<br>
            スマホからサクッとメッセージを送るだけ。<br>
            お返事は通常24時間以内にお送りいたします。
          </p>
          <a href="https://lin.ee/PCsXnGd" class="contact-line-btn" id="contact-line-btn" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.629-.63.629h-2.386c-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63h2.386c.349 0 .63.285.63.63 0 .349-.281.63-.63.63H17.61v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629V8.108c0-.27.173-.51.43-.595.06-.023.136-.033.194-.033.195 0 .375.104.515.254l2.449 3.32V8.108c0-.345.282-.63.63-.63.345 0 .63.285.63.63v4.771zm-5.741 0c0 .344-.282.629-.631.629-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63.346 0 .628.285.628.63v4.771zm-2.466.629H4.917c-.345 0-.63-.285-.63-.629V8.108c0-.345.285-.63.63-.63.348 0 .63.285.63.63v4.141h1.756c.348 0 .629.283.629.63 0 .344-.282.629-.629.629M24 10.314C24 4.943 18.615.572 12 .572S0 4.943 0 10.314c0 4.811 4.27 8.842 10.035 9.608.391.082.923.258 1.058.59.12.301.079.766.038 1.08l-.164 1.02c-.045.301-.24 1.186 1.049.645 1.291-.539 6.916-4.078 9.436-6.975C23.176 14.393 24 12.458 24 10.314" />
            </svg>
            公式LINEで無料相談''',
    text,
    flags=re.DOTALL
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Copywriting update complete.")
