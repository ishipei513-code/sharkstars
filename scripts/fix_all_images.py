import os
import re
import urllib.request
import urllib.error
import random

base_dir = r"d:\sharkstars\demos"
report_path = r"d:\sharkstars\broken_images_report.csv"

# Known valid pools (from previous runs)
mappings = {
    "matsueku-01": ["salon-01", "esthe-01", "whitening-01"],
    "nail-01": ["salon-01", "esthe-01", "whitening-01"],
    "izakaya-01": ["sushi-01", "yakiniku-01", "restaurant-01"],
    "cleaning-01": ["suidou-01", "reform-01", "fuyouhin-01", "construction-01"],
    "painter-01": ["construction-01", "reform-01"],
    "kaitai-01": ["construction-01", "reform-01"],
    "bankin-01": ["carshop-01"],
    "dance-01": ["gym-01", "yoga-01"],
    "dental-01": ["whitening-01", "shikaku-01"],
    "eikaiwa-01": ["juku-01", "shikaku-01"],
    "gyosei-01": ["lawyer-01", "tax-01", "lawfirm-01"],
    "hoikuen-01": ["juku-01", "eikaiwa-01"],
    "kitchencar-01": ["cafe-01", "bakery-01", "cake-01"],
    "ramen-01": ["izakaya-01", "yakiniku-01", "sushi-01", "restaurant-01"],
    "salon-01": ["salon-01", "esthe-01"],
    "seitai-01": ["shinkyu-01", "salon-01"],
    "wagashi-01": ["wagashi-01"],
    "photostudio-01": ["photostudio-01"],
    "bar-01": ["bar-01", "izakaya-01"],
    "cafe-01": ["cafe-01", "bakery-01"]
}

# 1. Collect all valid Unsplash base URLs
valid_urls_by_site = {}
cache = {}

def check_url(url):
    if url in cache: return cache[url]
    try:
        req = urllib.request.Request(url, method="HEAD", headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        cache[url] = (res.getcode() == 200)
    except Exception:
        cache[url] = False
    return cache[url]

print("Collecting valid URLs across the workspace...")
for folder in os.listdir(base_dir):
    site_dir = os.path.join(base_dir, folder)
    if not os.path.isdir(site_dir): continue
    
    html_path = os.path.join(site_dir, "index.html")
    if not os.path.exists(html_path): continue
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We only need the base photo ID to check if it's valid
    matches = re.finditer(r'(https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+)', content)
    for m in matches:
        u = m.group(1)
        if u not in cache:
            # For speed, check the standard format
            test_url = f"{u}?w=10"
            if check_url(test_url):
                valid_urls_by_site.setdefault(folder, []).append(u)

def get_replacement(site):
    pools = [site] + mappings.get(site, [])
    valid = []
    for p in pools:
        valid.extend(valid_urls_by_site.get(p, []))
    if not valid:
        valid.extend(valid_urls_by_site.get("cafe-01", []))
        valid.extend(valid_urls_by_site.get("salon-01", []))
    
    if valid:
        img = random.choice(valid)
        return f"{img}?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    return "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"

print("Fixing broken/malformed URLs...")
total_fixed = 0

for folder in os.listdir(base_dir):
    site_dir = os.path.join(base_dir, folder)
    if not os.path.isdir(site_dir): continue
    
    files_to_check = []
    html_path = os.path.join(site_dir, "index.html")
    if os.path.exists(html_path):
        files_to_check.append(html_path)
    
    css_dir = os.path.join(site_dir, "assist", "css")
    if os.path.exists(css_dir):
        for cf in os.listdir(css_dir):
            if cf.endswith(".css"):
                files_to_check.append(os.path.join(css_dir, cf))
    
    for fpath in files_to_check:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        orig_content = content
        
        # 1. Fix malformed "=rb-4... " URLs
        malformed_regex = r'(=rb-4\.0\.3&auto=format&fit=crop&w=800&q=80)'
        def replace_malformed(m):
            global total_fixed
            total_fixed += 1
            print(f"[{folder}] Fixed malformed URL in {os.path.basename(fpath)}")
            return get_replacement(folder)
        
        content = re.sub(malformed_regex, replace_malformed, content)
        
        # 2. Fix 401/404 Unsplash URLs
        def replace_unsplash(m):
            global total_fixed
            full_match = m.group(0)
            base_url = m.group(1)
            
            if not check_url(f"{base_url}?w=10"):
                total_fixed += 1
                print(f"[{folder}] Replaced broken URL: {base_url[:40]}...")
                return get_replacement(folder)
            return full_match
            
        unsplash_regex = r'(https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+)(?:\?[^"\'\)\s]*)?'
        content = re.sub(unsplash_regex, replace_unsplash, content)
        
        if content != orig_content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

print(f"All done! Total fixes applied: {total_fixed}")
