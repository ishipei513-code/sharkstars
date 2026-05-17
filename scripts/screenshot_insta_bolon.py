import os, time
from playwright.sync_api import sync_playwright

OUT = os.path.abspath(os.path.join('client', 'bolon-shareee', 'images'))
TARGETS = [
    ("https://www.instagram.com/b.villea.fukuoka/", "insta-bvillea.jpg"),
    ("https://www.instagram.com/motoko0204/",        "insta-motoko.jpg"),
    ("https://www.instagram.com/barian0204/",        "insta-barian.jpg"),
]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

WALL_MARKERS = ["制限されたプロフィール", "Restricted profile",
                "このページはご利用いただけません", "Sorry, this page"]

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(viewport={'width': 1120, 'height': 1000},
                                   user_agent=UA, locale="ja-JP")
        page = ctx.new_page()
        for url, name in TARGETS:
            out = os.path.join(OUT, name)
            status = "ok"
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                time.sleep(6)
                body = page.inner_text("body")[:4000]
                if any(m in body for m in WALL_MARKERS):
                    status = "WALLED (no logged-out content)"
                    print(f"{name}: {status}")
                    continue
                # remove signup/login dialog + dark backdrop scrim
                page.evaluate("""() => {
                  const vw = innerWidth, vh = innerHeight;
                  document.querySelectorAll('body *').forEach(e => {
                    const s = getComputedStyle(e);
                    if (s.position !== 'fixed' && s.position !== 'absolute') return;
                    const r = e.getBoundingClientRect();
                    const covers = r.width >= vw*0.9 && r.height >= vh*0.6;
                    const bg = s.backgroundColor || '';
                    const dim = bg.startsWith('rgba') && !bg.endsWith(', 0)');
                    const isDialog = e.getAttribute('role') === 'dialog';
                    if ((isDialog || (covers && (dim || parseInt(s.zIndex||0) >= 5)))
                        && !e.querySelector('header')) e.remove();
                  });
                  document.body.style.overflow = 'auto';
                  document.documentElement.style.filter = 'none';
                  document.body.style.filter = 'none';
                }""")
                time.sleep(1)
                header = page.locator("header").first
                if header.count() > 0 and header.is_visible():
                    header.screenshot(path=out, type="jpeg", quality=85)
                    status = "ok (header crop)"
                else:
                    page.screenshot(path=out, type="jpeg", quality=85,
                                    clip={"x": 0, "y": 60, "width": 1120, "height": 430})
                    status = "ok (viewport crop fallback)"
                print(f"{name}: {status}")
            except Exception as e:
                print(f"{name}: FAILED {type(e).__name__}")
        browser.close()

if __name__ == '__main__':
    main()
