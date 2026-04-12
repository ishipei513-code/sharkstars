import os
from playwright.sync_api import sync_playwright
import time

def take_screenshot(p, file_path):
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={'width': 1280, 'height': 853})
    page = context.new_page()
    
    out_path = os.path.abspath('index_hero_preview.jpg')
    file_url = f"file:///{file_path.replace(os.sep, '/')}"
    
    try:
        page.goto(file_url, wait_until="networkidle")
        time.sleep(2.0)
        page.screenshot(path=out_path, type="jpeg", quality=60)
        print("Captured index_hero_preview successfully.")
    except Exception as e:
        print(f"Failed to capture index: {e}")
        
    browser.close()

def main():
    with sync_playwright() as p:
        take_screenshot(p, os.path.abspath('index.html'))

if __name__ == '__main__':
    main()
