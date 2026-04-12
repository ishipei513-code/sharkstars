import os
import re
from bs4 import BeautifulSoup

file_path = r'd:\sharkstars\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='demo-card')

updated = 0
for card in cards:
    link = card.find('a', class_='demo-card-overlay-btn')
    img = card.find('img')
    if link and img:
        href = link.get('href', '')
        if href.startswith('demos/'):
            folder = href.split('/')[1]
            correct_src = f"assist/images/thumbnails/{folder}.jpg"
            if img.get('src') != correct_src:
                print(f"Updating {img.get('src')} -> {correct_src}")
                img['src'] = correct_src
                updated += 1

if updated > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Successfully updated {updated} thumbnail references in index.html.")
else:
    print("All thumbnails are already correct.")
