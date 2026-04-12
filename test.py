import re
with open(r'd:\sharkstars\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero = re.search(r'<h1 class=\"hero-title\">(.*?)</h1>', text, re.DOTALL)
if hero: print("HERO:", repr(hero.group(1)))

sub = re.search(r'<p class=\"hero-subtitle\">(.*?)</p>', text, re.DOTALL)
if sub: print("SUBTITLE:", repr(sub.group(1)))

badge = re.search(r'<div class=\"hero-badge\">.*?</div>', text, re.DOTALL)
if badge: print("BADGE:", repr(badge.group(0)))

prob = re.search(r'<div class=\"problems-content fade-in\">.*?</div>\s*</div>\s*</div>\s*</section>', text, re.DOTALL)
if prob: print("PROB:", repr(prob.group(0)[:300])) # just print the first 300 chars or write it to a file
