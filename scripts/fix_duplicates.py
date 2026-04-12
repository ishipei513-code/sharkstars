import os
import re

updates = {
    'denki-01': 'https://images.unsplash.com/photo-1621905251189-08b45d6a269e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'detective-01': 'https://images.unsplash.com/photo-1583324113626-70df0f4deaab?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'whitening-01': 'https://images.unsplash.com/photo-1536848148679-24b5006b0d91?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'shinkyu-01': 'https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'restaurant-01': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'nail-01': 'https://images.unsplash.com/photo-1519014816548-bf5fe059e98b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'yoga-01': 'https://images.unsplash.com/photo-1599901860904-17e08c27dc97?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80',
    'shikaku-01': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
}

for site, new_url in updates.items():
    file_path = f"d:\\sharkstars\\demos\\{site}\\index.html"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the hero section and replace the background-image or img src.
    # In shikaku-01, there might be NO image. If not found, we can insert it if it uses img.
    # Actually, we can just replace ANY unsplash image in the file. If no unsplash exists (shikaku-01), we just do a more complex replace or print.
    match = re.search(r"https://images\.unsplash\.com/[^'\" >|]+", content)
    if match:
        content = content.replace(match.group(0), new_url)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {site} hero image.")
    elif site == 'shikaku-01':
        # Let's insert a hero background image manually to the hero-bg style
        print(f"Fixing shikaku-01 manually since no unsplash url found.")
        # Attempt to find `<div class="hero-bg"></div>`
        content = re.sub(r'<div class="hero-bg">', f'<div class="hero-bg" style="background-image: url(\'{new_url}\');">', content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"No unsplash image found in {site}.")
