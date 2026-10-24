# -*- coding: utf-8 -*-
"""アセットのキャッシュ対策バージョンを一括で付け替える。

  python tools/bump_assets.py client/marin 261024ae

CSS/JS だけでなく **画像にも** 付ける。
ファイル名を変えずに中身だけ差し替えると、ブラウザは古い画像を出し続ける。
本番（ロリポップ）は Cache-Control を返さないため、ヒューリスティックに
長くキャッシュされる。実際、ヒーロー写真を差し替えてもスマホで変わらなかった。
"""
import glob
import io
import os
import re
import sys

IMG_EXT = r'(?:webp|jpg|jpeg|png|svg|mp4)'


def bump(root, ver):
    n_html = n_css = 0

    for f in sorted(glob.glob(os.path.join(root, '*.html'))):
        s = io.open(f, encoding='utf-8').read()
        o = s
        # CSS / JS
        s = re.sub(r'(href="css/[a-z0-9_-]+\.css)(\?v=[^"]*)?"', r'\1?v=%s"' % ver, s)
        s = re.sub(r'(src="js/[a-z0-9_-]+\.js)(\?v=[^"]*)?"', r'\1?v=%s"' % ver, s)
        # 画像（src / srcset / インラインの background-image）
        # 直前が「/」や英数字のものは絶対URL（OGP・JSON-LD の image）なので触らない。
        # サイト内の参照は必ず "images/... と相対で書いてある。
        s = re.sub(r'(?<![/\w.-])(images/[A-Za-z0-9_.-]+\.%s)(\?v=[^"\')\s,]*)?' % IMG_EXT,
                   r'\1?v=%s' % ver, s)
        # OGP／JSON-LD の image はSNS・検索側のキャッシュ単位なので、クエリは絶対に付けない。
        # 付けるとバージョンを上げるたびに別画像として再取得され、構造化データも揺れる。
        s = re.sub(r'(sharkstars\.jp/[^"\s]*\.%s)\?v=[^"\s]*' % IMG_EXT, r'\1', s)
        if s != o:
            io.open(f, 'w', encoding='utf-8', newline='\n').write(s)
            n_html += 1

    for f in sorted(glob.glob(os.path.join(root, 'css', '*.css'))):
        s = io.open(f, encoding='utf-8').read()
        o = s
        s = re.sub(r"(\.\./images/[A-Za-z0-9_.-]+\.%s)(\?v=[^'\")\s]*)?" % IMG_EXT,
                   r'\1?v=%s' % ver, s)
        if s != o:
            io.open(f, 'w', encoding='utf-8', newline='\n').write(s)
            n_css += 1

    print('バージョン %s を付与： HTML %d ファイル / CSS %d ファイル' % (ver, n_html, n_css))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('usage: python tools/bump_assets.py <dir> <version>')
    bump(sys.argv[1], sys.argv[2])
