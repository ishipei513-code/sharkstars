import re

file_path = r'd:\sharkstars\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Card 21 mapping:
text = re.sub(
    r'<img src="assist/images/thumbnails/denki-01\.jpg"([^>]*>)(\s*)<div class="demo-card-overlay">(\s*)<a href="demos/construction-01/index\.html"',
    r'<img src="assist/images/thumbnails/construction-01.jpg"\1\2<div class="demo-card-overlay">\3<a href="demos/construction-01/index.html"',
    text
)

# Card 47 mapping (detective-01):
text = re.sub(
    r'<img src="assist/images/thumbnails/denki-01\.jpg"([^>]*>)(\s*)<div class="demo-card-overlay">(\s*)<a href="demos/detective-01/index\.html"',
    r'<img src="assist/images/thumbnails/detective-01.jpg"\1\2<div class="demo-card-overlay">\3<a href="demos/detective-01/index.html"',
    text
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("regex replace completed.")
