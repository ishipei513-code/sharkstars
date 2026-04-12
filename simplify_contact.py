import os
from bs4 import BeautifulSoup

main_index_path = r'd:\sharkstars\index.html'

with open(main_index_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_tag = '<div class="contact-wrapper fade-in">'
end_tag = '<!-- ============================================'
# Note: the end of section is </section> before SECTION 8: LEGAL OR FOOTER

start_idx = text.find(start_tag)
end_idx = text.find('</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    old_block = text[start_idx:end_idx]
    
    new_block = """<div class="contact-wrapper fade-in">
        <!-- Left: LINE Info -->
        <div class="contact-form-card" style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
          <h3 class="contact-info-title" style="margin-bottom: 24px;">LINEで気軽に無料相談 🎯</h3>
          <p class="contact-info-desc" style="margin-bottom: 32px;">
            個人店オーナー様・職人の皆様に一番人気のご連絡方法です。<br>
            スマホからサクッとメッセージを送るだけ。<br>
            お返事は通常24時間以内にお送りいたします。
          </p>
          <a href="https://lin.ee/PCsXnGd" class="contact-line-btn" id="contact-line-btn" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M19.365 9.863c.349 0 .63.285.63.631 0 .345-.281.63-.63.63H17.61v1.125h1.755c.349 0 .63.283.63.63 0 .344-.281.629-.63.629h-2.386c-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63h2.386c.349 0 .63.285.63.63 0 .349-.281.63-.63.63H17.61v1.125h1.755zm-3.855 3.016c0 .27-.174.51-.432.596-.064.021-.133.031-.199.031-.211 0-.391-.09-.51-.25l-2.443-3.317v2.94c0 .344-.279.629-.631.629-.346 0-.626-.285-.626-.629V8.108c0-.27.173-.51.43-.595.06-.023.136-.033.194-.033.195 0 .375.104.515.254l2.449 3.32V8.108c0-.345.282-.63.63-.63.345 0 .63.285.63.63v4.771zm-5.741 0c0 .344-.282.629-.631.629-.345 0-.627-.285-.627-.629V8.108c0-.345.282-.63.63-.63.346 0 .628.285.628.63v4.771zm-2.466.629H4.917c-.345 0-.63-.285-.63-.629V8.108c0-.345.285-.63.63-.63.348 0 .63.285.63.63v4.141h1.756c.348 0 .629.283.629.63 0 .344-.282.629-.629.629M24 10.314C24 4.943 18.615.572 12 .572S0 4.943 0 10.314c0 4.811 4.27 8.842 10.035 9.608.391.082.923.258 1.058.59.12.301.079.766.038 1.08l-.164 1.02c-.045.301-.24 1.186 1.049.645 1.291-.539 6.916-4.078 9.436-6.975C23.176 14.393 24 12.458 24 10.314" />
            </svg>
            公式LINEで無料相談
          </a>
        </div>

        <!-- Right: Email Info -->
        <div class="contact-form-card" style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
          <h3 class="contact-info-title" style="margin-bottom: 24px;">メールでご相談・お見積り ✉️</h3>
          <p class="contact-info-desc" style="margin-bottom: 32px;">
            仕様書などファイルを添付したい場合や、<br>
            LINEをお使いでない方はメールでお送りください。<br>
            担当者が直接内容を確認してご返信いたします。
          </p>
          <a href="mailto:sharkstars0513@gmail.com" class="btn-primary" style="padding: 16px 32px; font-size: 1.1rem; border-radius: 100px;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width:24px; height:24px; margin-right:8px;">
              <rect x="2" y="4" width="20" height="16" rx="2"></rect>
              <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>
            </svg>
            メールを作成する
          </a>
        </div>
      </div>
    </div>
"""
    
    text = text.replace(old_block, new_block)
    with open(main_index_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Contact section simplified successfully.")
else:
    print("Could not find the target HTML tags.")
