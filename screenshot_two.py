import os
from playwright.sync_api import sync_playwright
import time

def take_screenshot(p, folder, file_path):
    thumbnails_dir = os.path.abspath(os.path.join('assist', 'images', 'thumbnails'))
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1280, 'height': 853})
    page = context.new_page()
    
    out_path = os.path.join(thumbnails_dir, f"{folder}.jpg")
    file_url = f"file:///{file_path.replace(os.sep, '/')}"
    
    try:
        page.goto(file_url, wait_until="networkidle")
        time.sleep(2.0) # give it extra time for nice fade-in typography
        page.screenshot(path=out_path, type="jpeg", quality=60)
        print(f"Captured {folder} successfully.")
    except Exception as e:
        print(f"Failed to capture {folder}: {e}")
        
    browser.close()

def main():
    with sync_playwright() as p:
        take_screenshot(p, 'denki-01', os.path.abspath(r'demos\denki-01\index.html'))
        take_screenshot(p, 'construction-01', os.path.abspath(r'demos\construction-01\index.html'))

if __name__ == '__main__':
    main()
