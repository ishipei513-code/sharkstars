# -*- coding: utf-8 -*-
"""client/marin を本番（Xserver）へFTPSでアップロードする。

認証情報は FileZilla の sitemanager.xml から読むだけで、標準出力には一切出さない。

  python tools/deploy_marin.py --probe            接続と遠隔のディレクトリ構成だけ確認（無変更）
  python tools/deploy_marin.py --deploy           marin_new へ上げて marin と入れ替える
  python tools/deploy_marin.py --rollback <stamp> 入れ替えを戻す

入れ替え方式：
  1. client/marin_new へ全ファイルをアップロード
  2. client/marin → client/marin_old_<stamp> にリネーム
  3. client/marin_new → client/marin にリネーム
  旧版はサーバーに残るので、問題があれば --rollback で戻せる。
  単純上書きにしないのは、旧版の images/*.jpg がゴミとして残るため。
"""
import argparse
import ftplib
import os
import posixpath
import re
import ssl
import sys
import time
from base64 import b64decode

LOCAL_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'client', 'marin')
SITE_HINTS = ('sharkstars', 'xserver', 'xsrv')


def load_site(hint=None):
    """FileZillaの保存済みサイトから接続先を1件返す。値は呼び出し元でも表示しないこと。"""
    path = os.path.join(os.environ['APPDATA'], 'FileZilla', 'sitemanager.xml')
    if not os.path.exists(path):
        sys.exit('sitemanager.xml が見つかりません: %s' % path)
    xml = open(path, encoding='utf-8', errors='replace').read()

    sites = []
    for block in re.findall(r'<Server>(.*?)</Server>', xml, re.S):
        def tag(name):
            m = re.search(r'<%s[^>]*>(.*?)</%s>' % (name, name), block, re.S)
            return m.group(1).strip() if m else ''
        name = re.findall(r'</\w+>\s*([^<>]+)\s*$', block)
        pw = tag('Pass')
        if '<Pass encoding="base64"' in block and pw:
            try:
                pw = b64decode(pw).decode('utf-8', 'replace')
            except Exception:
                pw = ''
        sites.append({
            'name': (name[-1].strip() if name else ''),
            'host': tag('Host'),
            'port': int(tag('Port') or 21),
            'user': tag('User'),
            'pass': pw,
            'protocol': tag('Protocol'),
            'remote_dir': tag('RemoteDir'),
        })

    if not sites:
        sys.exit('保存済みサイトが0件でした。')

    def score(s):
        blob = (s['name'] + ' ' + s['host']).lower()
        return sum(2 for h in SITE_HINTS if h in blob) + (1 if s['pass'] else 0)

    if hint:
        cand = [s for s in sites if hint.lower() in (s['name'] + ' ' + s['host']).lower()]
        if not cand:
            sys.exit('"%s" に一致するサイトがありません。' % hint)
    else:
        cand = sites
    cand.sort(key=score, reverse=True)

    print('保存済みサイト %d件。使用する接続先：' % len(sites))
    s = cand[0]
    print('  name=%s  host=%s  port=%s  user=%s  pass=%s'
          % (s['name'] or '(無名)', mask_host(s['host']), s['port'], mask(s['user']),
             '保存あり' if s['pass'] else '**保存なし**'))
    if not s['pass']:
        sys.exit('パスワードが保存されていません。FileZillaでパスワードを保存するか、別の方法で。')
    return s


class LolipopFTP_TLS(ftplib.FTP_TLS):
    """ftplib の storbinary はデータ接続を閉じる前に TLS の unwrap をするが、
    ロリポップ側が先にソケットを切るため ConnectionResetError になる。
    unwrap しない版に差し替える（転送自体は完了しているので実害はない）。"""

    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
        self.voidcmd('TYPE I')
        conn = self.transfercmd(cmd, rest)
        try:
            while True:
                buf = fp.read(blocksize)
                if not buf:
                    break
                conn.sendall(buf)
                if callback:
                    callback(buf)
        finally:
            try:
                conn.close()
            except Exception:
                pass
        return self.voidresp()


def mask(v):
    if not v:
        return '(空)'
    return v[:2] + '*' * max(len(v) - 3, 1) + v[-1:]


def mask_host(h):
    parts = h.split('.')
    if len(parts) < 2:
        return mask(h)
    return mask(parts[0]) + '.' + '.'.join(parts[1:])


def connect(site):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    last = None
    for mode in ('ftps', 'ftp'):
        try:
            if mode == 'ftps':
                ftp = LolipopFTP_TLS(context=ctx)
            else:
                ftp = ftplib.FTP()
            ftp.connect(site['host'], site['port'], timeout=30)
            ftp.login(site['user'], site['pass'])
            if mode == 'ftps':
                ftp.prot_p()
            ftp.set_pasv(True)
            print('接続OK（%s）' % ('FTPS 明示的' if mode == 'ftps' else '平文FTP'))
            return ftp
        except Exception as e:
            last = e
            try:
                ftp.close()
            except Exception:
                pass
    sys.exit('接続に失敗しました: %s' % last)


def find_webroot(ftp, site):
    """client/marin を含むディレクトリを探す。"""
    candidates = []
    if site['remote_dir']:
        # FileZillaの RemoteDir は "1 0 5 xxxxx" のような独自書式
        parts = re.findall(r'\d+\s+(.+)', site['remote_dir'])
        raw = re.sub(r'^\d+(\s+\d+)*\s*', '', site['remote_dir'])
        seg = [p for p in re.split(r'\s+', raw) if p]
        if seg:
            candidates.append('/' + '/'.join(seg))
    # ロリポップはFTPルート直下にサイトごとのフォルダが並ぶ（/sharkstars が sharkstars.jp の公開先）
    candidates += ['/sharkstars', '/sharkstars.jp/public_html', '/public_html', '/']
    for base in candidates:
        try:
            ftp.cwd(base)
        except Exception:
            continue
        try:
            names = ftp.nlst()
        except Exception:
            continue
        if 'client' in names or 'index.html' in names:
            print('公開ディレクトリ: %s' % base)
            return base
    sys.exit('公開ディレクトリを特定できませんでした。候補: %s' % candidates)


def walk_local():
    files = []
    for root, dirs, names in os.walk(LOCAL_ROOT):
        dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__')]
        for n in names:
            full = os.path.join(root, n)
            rel = os.path.relpath(full, LOCAL_ROOT).replace('\\', '/')
            files.append((full, rel))
    return sorted(files, key=lambda t: t[1])


def ensure_dir(ftp, path):
    cur = ''
    for seg in path.strip('/').split('/'):
        cur += '/' + seg
        try:
            ftp.mkd(cur)
        except ftplib.error_perm as e:
            if not str(e).startswith('550'):
                raise


def rmtree(ftp, path):
    """リモートのディレクトリを中身ごと消す（存在しなければ何もしない）。"""
    try:
        ftp.cwd(path)
    except Exception:
        return
    entries = []
    try:
        ftp.retrlines('MLSD ' + path, entries.append)
    except Exception:
        entries = None
    if entries is None:
        for name in ftp.nlst(path):
            base = posixpath.basename(name)
            if base in ('.', '..'):
                continue
            child = posixpath.join(path, base)
            try:
                ftp.delete(child)
            except Exception:
                rmtree(ftp, child)
    else:
        for line in entries:
            facts, _, name = line.partition('; ')
            name = name.strip()
            if name in ('.', '..'):
                continue
            child = posixpath.join(path, name)
            if 'type=dir' in facts:
                rmtree(ftp, child)
            elif 'type=file' in facts:
                try:
                    ftp.delete(child)
                except Exception:
                    pass
    try:
        ftp.rmd(path)
    except Exception:
        pass


def upload(ftp, webroot, stamp):
    files = walk_local()
    total = sum(os.path.getsize(f) for f, _ in files)
    print('アップロード対象: %d ファイル / %.2f MB' % (len(files), total / 1024 / 1024))

    staging = posixpath.join(webroot, 'client', 'marin_new')
    rmtree(ftp, staging)   # 前回の失敗分が残っていても作り直す
    ensure_dir(ftp, staging)

    made = set()
    done = 0
    for full, rel in files:
        d = posixpath.dirname(rel)
        if d and d not in made:
            ensure_dir(ftp, posixpath.join(staging, d))
            made.add(d)
        with open(full, 'rb') as fh:
            ftp.storbinary('STOR ' + posixpath.join(staging, rel), fh, blocksize=1 << 16)
        done += 1
        if done % 10 == 0 or done == len(files):
            print('  %d/%d  %s' % (done, len(files), rel))

    # 枚数の突き合わせ
    remote_count = count_remote(ftp, staging)
    print('アップロード完了。リモート実ファイル数=%d / ローカル=%d' % (remote_count, len(files)))
    if remote_count != len(files):
        sys.exit('ファイル数が一致しません。入れ替えは中止しました（marin_new に残っています）。')

    live = posixpath.join(webroot, 'client', 'marin')
    backup = posixpath.join(webroot, 'client', 'marin_old_' + stamp)
    try:
        ftp.rename(live, backup)
        print('旧版を退避: client/marin → client/marin_old_%s' % stamp)
    except Exception as e:
        print('旧版の退避をスキップ（存在しない？）: %s' % e)
    ftp.rename(staging, live)
    print('入れ替え完了: client/marin_new → client/marin')


def count_remote(ftp, path):
    n = 0
    stack = [path]
    while stack:
        cur = stack.pop()
        entries = []
        try:
            ftp.retrlines('MLSD ' + cur, entries.append)
        except Exception:
            try:
                ftp.cwd(cur)
                for name in ftp.nlst():
                    base = posixpath.basename(name)
                    if base in ('.', '..'):
                        continue
                    try:
                        ftp.cwd(posixpath.join(cur, base))
                        stack.append(posixpath.join(cur, base))
                    except Exception:
                        n += 1
            except Exception:
                pass
            continue
        for line in entries:
            facts, _, name = line.partition('; ')
            name = name.strip()
            if name in ('.', '..'):
                continue
            if 'type=dir' in facts:
                stack.append(posixpath.join(cur, name))
            elif 'type=file' in facts:
                n += 1
    return n


def rollback(ftp, webroot, stamp):
    live = posixpath.join(webroot, 'client', 'marin')
    backup = posixpath.join(webroot, 'client', 'marin_old_' + stamp)
    ftp.rename(live, posixpath.join(webroot, 'client', 'marin_failed_' + time.strftime('%H%M%S')))
    ftp.rename(backup, live)
    print('ロールバック完了: marin_old_%s → marin' % stamp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--probe', action='store_true')
    ap.add_argument('--deploy', action='store_true')
    ap.add_argument('--rollback', metavar='STAMP')
    ap.add_argument('--site', help='サイト名/ホストの一部で絞り込む')
    ap.add_argument('--webroot', help='公開ディレクトリを明示（例 /sharkstars）')
    a = ap.parse_args()

    site = load_site(a.site)
    ftp = connect(site)
    try:
        webroot = a.webroot or find_webroot(ftp, site)
        if a.probe:
            ftp.cwd(posixpath.join(webroot, 'client'))
            print('client/ の中身: %s' % ', '.join(sorted(ftp.nlst())[:40]))
            try:
                ftp.cwd(posixpath.join(webroot, 'client', 'marin'))
                print('client/marin の中身: %s' % ', '.join(sorted(ftp.nlst())))
                ftp.cwd(posixpath.join(webroot, 'client', 'marin', 'images'))
                imgs = sorted(ftp.nlst())
                jpgs = [i for i in imgs if i.lower().endswith(('.jpg', '.jpeg'))]
                print('images/ 計%d件、うち .jpg が %d件' % (len(imgs), len(jpgs)))
                if jpgs:
                    print('  旧jpg例: %s' % ', '.join(jpgs[:12]))
            except Exception as e:
                print('client/marin の走査に失敗: %s' % e)
            return
        stamp = time.strftime('%Y%m%d')
        if a.rollback:
            rollback(ftp, webroot, a.rollback)
        elif a.deploy:
            upload(ftp, webroot, stamp)
        else:
            print('--probe / --deploy / --rollback のどれかを指定してください。')
    finally:
        try:
            ftp.quit()
        except Exception:
            pass


if __name__ == '__main__':
    main()
