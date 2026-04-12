import re

file_path = r'd:\sharkstars\demos\salon-01\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace hero
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/hero.png' if '1521590832167' in m.group(0) else m.group(0), text)
# Replace philosophy
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/concept.png' if '1560066984' in m.group(0) else m.group(0), text)
# Replace cuts/treatments
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/bob.png' if '1522337660859' in m.group(0) else m.group(0), text)
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/color.png' if '1562322140' in m.group(0) else m.group(0), text)
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/spa.png' if '1515377905703' in m.group(0) else m.group(0), text)

# Replace Gallery
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/bob.png' if '1519699047748' in m.group(0) else m.group(0), text)
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', lambda m: 'assist/images/color.png' if '1620601633519' in m.group(0) else m.group(0), text)

# By this point all unsplash images should be replaced. Let me just replace ALL unsplash with hero just in case any were missed.
text = re.sub(r'https://images.unsplash.com/photo-[^"]+', 'assist/images/hero.png', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated image src in salon-01/index.html")
