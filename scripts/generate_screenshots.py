import os
import glob
from playwright.sync_api import sync_playwright
import time

def main():
    demos_dir = os.path.abspath('demos')
    thumbnails_dir = os.path.abspath(os.path.join('assist', 'images', 'thumbnails'))
    
    os.makedirs(thumbnails_dir, exist_ok=True)
    
    index_files = glob.glob(os.path.join(demos_dir, '*', 'index.html'))
    print(f"Found {len(index_files)} demo sites.")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Using a typical laptop viewport
        context = browser.new_context(viewport={'width': 1280, 'height': 853})
        page = context.new_page()
        
        for file_path in index_files:
            folder_name = os.path.basename(os.path.dirname(file_path))
            
            # Specific handling for the custom cafe-01 if needed, but let's just make everything .jpg
            # Even if cafe-01 was .png in index, let's just generate a .jpg for uniformity
            out_path = os.path.join(thumbnails_dir, f"{folder_name}.jpg")
            
            file_url = f"file:///{file_path.replace(os.sep, '/')}"
            try:
                # Wait until network is mostly idle to ensure fonts/images load
                page.goto(file_url, wait_until="networkidle")
                # Add a brief explicit sleep just to ensure Unsplash hero images resolve
                time.sleep(1.5)
                
                # Take screenshot
                page.screenshot(path=out_path, type="jpeg", quality=50)
                print(f"Captured: {folder_name}")
            except Exception as e:
                print(f"Failed to capture {folder_name}: {e}")
                
        browser.close()

if __name__ == '__main__':
    main()
