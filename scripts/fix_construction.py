import sys
from bs4 import BeautifulSoup

file_path = r'd:\sharkstars\demos\construction-01\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Logo
html = html.replace('<div class="logo">サンライズ電気</div>', '<div class="logo">匠工房</div>')

# Replace Hero H1
html = html.replace('<h1>電気のこと、<br>お任せください。</h1>', '<h1>確かな技術力を、<br>あなたの空間へ。</h1>')

# Replace Hero Image
# The old image might be any of the denki-01 variants, let's just find the img src in <div class="bg">
import re
html = re.sub(
    r'<div class="bg"><img src="[^"]+"></div>',
    '<div class="bg"><img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"></div>',
    html
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed construction-01 HTML.")
