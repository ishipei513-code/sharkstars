import os
from playwright.sync_api import sync_playwright
import time

def main():
    thumbnails_dir = os.path.abspath(os.path.join('assist', 'images', 'thumbnails'))
    file_path = os.path.abspath(r'demos\construction-01\index.html')
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 853})
        page = context.new_page()
        
        out_path = os.path.join(thumbnails_dir, "construction-01.jpg")
        file_url = f"file:///{file_path.replace(os.sep, '/')}"
        
        try:
            page.goto(file_url, wait_until="networkidle")
            time.sleep(1.5)
            page.screenshot(path=out_path, type="jpeg", quality=50)
            print("Captured construction-01 successfully.")
        except Exception as e:
            print(f"Failed to capture: {e}")
            
        browser.close()

if __name__ == '__main__':
    main()
