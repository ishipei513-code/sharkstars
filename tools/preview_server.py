# -*- coding: utf-8 -*-
"""ローカルプレビュー用サーバー（キャッシュ無効）

  python tools/preview_server.py            -> http://127.0.0.1:8787/
  python tools/preview_server.py 8080        -> ポート指定

`python -m http.server` だと Cache-Control が付かず、ブラウザが
Last-Modified からヒューリスティックにキャッシュしてしまい、CSS/JS を
書き換えても画面に反映されない。制作中はこちらを使う。
"""
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    extensions_map = dict(SimpleHTTPRequestHandler.extensions_map)
    extensions_map['.webp'] = 'image/webp'
    extensions_map['.svg'] = 'image/svg+xml'
    extensions_map['.mp4'] = 'video/mp4'

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

    def log_message(self, fmt, *args):
        if '404' in (fmt % args):
            sys.stderr.write("404 %s\n" % (args[0] if args else ''))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8787
    directory = sys.argv[2] if len(sys.argv) > 2 else '.'
    handler = partial(NoCacheHandler, directory=directory)
    srv = ThreadingHTTPServer(('127.0.0.1', port), handler)
    print('preview: http://127.0.0.1:%d/  (no-cache)' % port)
    srv.serve_forever()


if __name__ == '__main__':
    main()
