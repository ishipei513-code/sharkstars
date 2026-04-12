import re

file_path = r'd:\sharkstars\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Card 11 (Belle / salon-01) mapping:
text = re.sub(
    r'<img src="assist/images/thumbnails/nail-01\.jpg"([^>]*>)(\s*)<div class="demo-card-overlay">(\s*)<a href="demos/salon-01/index\.html"',
    r'<img src="assist/images/thumbnails/salon-01.jpg"\1\2<div class="demo-card-overlay">\3<a href="demos/salon-01/index.html"',
    text
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("regex replace for salon-01 completed.")
