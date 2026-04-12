import re

html_path = r'd:\sharkstars\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

hero_match = re.search(r'<section class="hero" id="hero">.*?</section>', text, re.DOTALL)
if hero_match:
    print(hero_match.group(0))
