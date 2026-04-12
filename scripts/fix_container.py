import sys

with open(r'd:\sharkstars\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<div class="l-container">', '<div class="container">')

with open(r'd:\sharkstars\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed container class securely.")
