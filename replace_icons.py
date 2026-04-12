import sys

with open(r'd:\sharkstars\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace checks
text = text.replace(
    '<i data-lucide="check" class="icon-check"></i>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" class="icon-check"><polyline points="20 6 9 17 4 12" /></svg>'
)

# Replace search
text = text.replace(
    '<i data-lucide="search"></i>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>'
)

# Replace share-2
text = text.replace(
    '<i data-lucide="share-2"></i>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>'
)

# Replace zap
text = text.replace(
    '<i data-lucide="zap"></i>',
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>'
)

with open(r'd:\sharkstars\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Icons replaced with inline SVG!")
