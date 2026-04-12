import re

file_path = r'd:\sharkstars\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Pricing Standard Features (full-width)
old_full = r'<div class="pricing-detail-box fade-in full-width">.*?</div>\s*</div>\s*</div>\s*</div>'
new_full = '''<div class="pricing-detail-box fade-in full-width">
          <h3 class="detail-title text-center">他社なら有料級の「最強・標準装備」</h3>
          <p class="detail-desc text-center mb-medium">見えない部分まで徹底サポート。</p>
          <div class="detail-features-flex">
            <div class="df-item">
              <div class="df-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
              <div class="df-text">
                <strong>プロの内部SEO対策</strong><span>検索エンジンに正しく評価されるための「見えない土台作り（構造化など）」を標準で実装します。</span>
              </div>
            </div>
            <div class="df-item">
              <div class="df-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg></div>
              <div class="df-text">
                <strong>SNS・LINE連携（OGP）</strong><span>リンクをシェアした際、魅力的なサムネイル画像が表示されるよう最適化し、クリック率を高めます。</span>
              </div>
            </div>
            <div class="df-item">
              <div class="df-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg></div>
              <div class="df-text">
                <strong>ストレスゼロの高速表示</strong><span>最新のWeb技術により、お客様を待たせない「サクサク動く」快適な閲覧体験を提供します。</span>
              </div>
            </div>
          </div>
        </div>
      </div>'''
text = re.sub(old_full, new_full, text, flags=re.DOTALL)

# Fix Optional Pricing Update Note
old_note = r'<!-- 3\. 更新・追加料金について -->\s*<div class="pricing-update-box fade-in" id="pricing-note">.*?</section>'
new_note = '''<!-- 3. 更新・追加料金について -->
      <div class="pricing-update-box fade-in" id="pricing-note">
        <h3>💡 なぜここまで安いのか？</h3>
        <p>
          一般的な制作会社では、実際には行わない「更新作業」を名目に高額な月額費用を請求するケースが見受けられます。<br><br>
          SHARKSTARSは維持管理に必要な実費のみを月額とし、テキスト変更などは「必要な時に、必要な分だけ」お支払いいただく明朗会計を採用しています。
        </p>
      </div>
    </div>
  </section>'''
text = re.sub(old_note, new_note, text, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Standard features and opt pricing note updated.")
