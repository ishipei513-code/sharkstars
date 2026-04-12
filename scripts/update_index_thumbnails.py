import sys
from bs4 import BeautifulSoup

main_index_path = r'd:\sharkstars\index.html'

with open(main_index_path, 'r', encoding='utf-8') as f:
    main_html = f.read()

soup = BeautifulSoup(main_html, 'html.parser')
cards = soup.select('.demo-card')

replacements = []
for card in cards:
    img_tag = card.select_one('.demo-card-image img')
    link_tag = card.select_one('.demo-card-overlay a') or card.select_one('.demo-card-link')
    
    if img_tag and link_tag:
        old_src = img_tag.get('src')
        href = link_tag.get('href')
        
        if href and href.startswith('demos/') and old_src:
            folder = href.split('/')[1]
            new_src = f"assist/images/thumbnails/{folder}.jpg"
            if old_src != new_src:
                replacements.append((old_src, new_src, folder))

modified_html = main_html
for old_src, new_src, folder in replacements:
    modified_html = modified_html.replace(f'src="{old_src}"', f'src="{new_src}"')

with open(main_index_path, 'w', encoding='utf-8') as f:
    f.write(modified_html)
print(f"Updated {len(replacements)} images in index.html to point to the new screenshots.")
