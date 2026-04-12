import os
import re
from bs4 import BeautifulSoup

main_index_path = r'd:\sharkstars\index.html'

with open(main_index_path, 'r', encoding='utf-8') as f:
    main_html = f.read()

# Since we don't want to completely rewrite the file with bs4's formatter if we can avoid it,
# we will use bs4 just to find the URLs, and then replace them in the raw string.
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
            demo_path = os.path.join(r'd:\sharkstars', href.replace('/', '\\'))
            if os.path.exists(demo_path):
                try:
                    with open(demo_path, 'r', encoding='utf-8') as df:
                        demo_html = df.read()
                    
                    demo_soup = BeautifulSoup(demo_html, 'html.parser')
                    hero_url = None
                    hero_section = demo_soup.select_one('.hero')
                    
                    if hero_section:
                        # 1. Look for img tag
                        hero_img = hero_section.select_one('img')
                        if hero_img and hero_img.get('src'):
                            hero_url = hero_img['src']
                        else:
                            # 2. Look for style="background-image: url(...)"
                            bg_match = re.search(r"background-image\s*:\s*url\(\s*['\"]?(https://images\.unsplash\.com/[^'\")]+)['\"]?\s*\)", str(hero_section))
                            if bg_match:
                                hero_url = bg_match.group(1)
                            
                    if not hero_url:
                        # Fallback: find any unsplash image in the whole file
                        all_match = re.search(r"https://images\.unsplash\.com/[^'\" >]+", demo_html)
                        if all_match:
                            hero_url = all_match.group(0)

                    if hero_url and hero_url != old_src:
                        replacements.append((old_src, hero_url, href))
                except Exception as e:
                    print(f'Error reading {demo_path}: {e}')

# Perform replacements on the raw HTML
modified_html = main_html
for old_src, new_src, href in replacements:
    # We replace precisely the old_src inside the demo-card block.
    # To be safe, we just replace the exact string `src="{old_src}"` -> `src="{new_src}"`
    # However, multiple cards might have the same placeholder image originally?
    # No, they are usually site-specific like `assist/images/thumbnails/cafe-01.jpg`
    # Let's just do a global replace for the old_src string because they should be unique files.
    # To be extremely safe, we do string replacement.
    modified_html = modified_html.replace(f'src="{old_src}"', f'src="{new_src}"')
    print(f'Mapped {href}: {old_src} -> {new_src[:60]}...')

if modified_html != main_html:
    with open(main_index_path, 'w', encoding='utf-8') as f:
        f.write(modified_html)
    print(f'Successfully updated {len(replacements)} images in index.html.')
else:
    print('No modifications needed.')
