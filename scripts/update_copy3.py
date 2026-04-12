import re

file_path = r'd:\sharkstars\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Optional Pricing Update Note
old_note = r'<!-- 3\. オプション -->.*?</div>\s*</div>\s*</section>'
new_note = '''<!-- 3. オプション・お約束 -->
      <div class="pricing-update-box fade-in" id="pricing-note">
        <h3>💡 なぜここまで安いのか？</h3>
        <p>
          一般的な制作会社では、実際には行わない「更新作業」を名目に高額な月額費用を請求するケースが見受けられます。<br><br>
          SHARKSTARSは維持管理に必要な実費のみを月額とし、テキスト変更などは「必要な時に、必要な分だけ」お支払いいただく明朗会計を採用しています。無駄な中間マージンを排除し、誠実な価格でサービスを提供し続けます。
        </p>
      </div>
    </div>
  </section>'''
text = re.sub(old_note, new_note, text, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
print("Option pricing note fixed.")
