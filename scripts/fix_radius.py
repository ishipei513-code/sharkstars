import re

css_path = r'd:\sharkstars\assist\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Lines to keep border-radius: buttons, pills, circles
# We want to REMOVE border-radius from non-button elements
# But we need to be careful - keep border-radius for:
# - .btn*, .gallery-tab, .hero-badge (pill buttons)
# - elements with border-radius: 50% (circles)
# - hamburger spans (border-radius: 3px)
# - .scroll-top

skip_lines = set()
for i, line in enumerate(lines):
    stripped = line.strip()
    if 'border-radius' in stripped:
        val = stripped
        # Keep these
        if '50%' in val or '100px' in val or '3px' in val:
            continue
        # Check context - look back up to 10 lines to find the selector
        context = ''
        for j in range(max(0, i-10), i):
            context += lines[j]
        # Keep for buttons, tabs, scroll-top, hamburger
        if any(k in context for k in ['btn', 'gallery-tab', 'scroll-top', 'hamburger', '.logo']):
            continue
        # Remove all other border-radius
        skip_lines.add(i)

new_lines = []
for i, line in enumerate(lines):
    if i in skip_lines:
        continue
    new_lines.append(line)

with open(css_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f'Removed border-radius from {len(skip_lines)} lines')
