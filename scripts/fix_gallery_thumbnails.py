# -*- coding: utf-8 -*-
"""
demos/index.html のギャラリー各カードの <img src> を、
そのデモサイトの実スクリーンショット（assist/images/thumbnails/<slug>.jpg）に差し替える。
従来は <slug>/assist/images/hero.png（複数デモで重複する仮ヒーロー画像）や
外部 Unsplash URL を参照していたため、鍼灸院と整体院が同じサロン写真になる等の不一致が発生していた。
"""
import re

PATH = 'demos/index.html'

with open(PATH, encoding='utf-8') as f:
    html = f.read()

# href="<slug>/" ... <div class="thumb"><img loading="lazy" src="<OLD>"
pattern = re.compile(
    r'(href=")([a-z0-9-]+)(/"[^>]*>\s*<div class="thumb">\s*<img loading="lazy" src=")([^"]*)(")'
)

def repl(m):
    slug = m.group(2)
    new_src = f'../assist/images/thumbnails/{slug}.jpg'
    return f'{m.group(1)}{slug}{m.group(3)}{new_src}{m.group(5)}'

html2, n = pattern.subn(repl, html)
print(f'replacements: {n}')

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html2)
