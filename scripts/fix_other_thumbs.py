import re

file_path = r'd:\sharkstars\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Cafe-01
text = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-[^"]+"([^>]*>)(\s*)<div class="demo-card-overlay">(\s*)<a href="demos/cafe-01/index\.html"',
    r'<img src="assist/images/thumbnails/cafe-01.jpg"\1\2<div class="demo-card-overlay">\3<a href="demos/cafe-01/index.html"',
    text
)

# Cooking-01
text = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-[^"]+"([^>]*>)(\s*)<div class="demo-card-overlay">(\s*)<a href="demos/cooking-01/index\.html"',
    r'<img src="assist/images/thumbnails/cooking-01.jpg"\1\2<div class="demo-card-overlay">\3<a href="demos/cooking-01/index.html"',
    text
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("regex replace for cafe & cooking completed.")
