# scripts/collect_trinity_images.py
# 現行TRINITYサイト(グーペ)とアメブロから画像URLを抽出しダウンロードする（乗り換え前の素材回収）
import re, os, urllib.request

PAGES = [
    "https://www.trinity-fukuoka.com/",
    "https://www.trinity-fukuoka.com/free/nantucket-basket",
    "https://www.trinity-fukuoka.com/free/about",
    "https://ameblo.jp/trinity345/",
]
OUT = "client/trinity/images/source"
UA = {"User-Agent": "Mozilla/5.0 (image backup before Goope cancellation)"}

os.makedirs(OUT, exist_ok=True)
seen = set()
for page in PAGES:
    try:
        html = urllib.request.urlopen(urllib.request.Request(page, headers=UA), timeout=20).read().decode("utf-8", "ignore")
    except Exception as e:
        print(f"SKIP {page}: {e}")
        continue
    urls = re.findall(r'https?://(?:img\.goope\.jp|cdn\.goope\.jp|stat\.ameba\.jp/user_images)[^\s"\'<>]+?\.(?:jpe?g|png)', html)
    print(f"{page} -> {len(urls)} urls")
    for u in urls:
        if u in seen:
            continue
        seen.add(u)
        name = re.sub(r'[^A-Za-z0-9._-]', '_', u.split('/')[-1])[-60:]
        try:
            urllib.request.urlretrieve(u, os.path.join(OUT, name))
            print("OK ", u)
        except Exception as e:
            print("NG ", u, e)
print(f"done: {len(os.listdir(OUT))} files")
