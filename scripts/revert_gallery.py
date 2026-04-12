import os
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
            if folder == 'cafe-01':
                new_src = "assist/images/demo-cafe.png"
            elif folder == 'dental-01':
                new_src = "https://images.unsplash.com/photo-1606811841689-23dfddce3e95?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
            elif folder == 'reform-01':
                new_src = "https://images.unsplash.com/photo-1484154218962-a197022b5858?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
            elif folder == 'tantei-01':
                new_src = "https://images.unsplash.com/photo-1558021211-6d1403321394?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
            elif folder == 'tax-01':
                new_src = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80"
                
            if old_src != new_src:
                replacements.append((old_src, new_src, folder))

modified_html = main_html
for old_src, new_src, folder in replacements:
    modified_html = modified_html.replace(f'src="{old_src}"', f'src="{new_src}"')

with open(main_index_path, 'w', encoding='utf-8') as f:
    f.write(modified_html)
print(f"Reverted {len(replacements)} images in index.html to local thumbnails via safe Python encoding.")
