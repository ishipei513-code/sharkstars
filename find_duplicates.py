import os, re, collections
from bs4 import BeautifulSoup

demos_dir = r"d:\sharkstars\demos"
urls = {}

for folder in os.listdir(demos_dir):
    folder_path = os.path.join(demos_dir, folder)
    if os.path.isdir(folder_path):
        index_path = os.path.join(folder_path, "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            hero = soup.select_one('.hero')
            
            # Simple unstructured search if pure regex covers things well
            # First try inside .hero, then globally
            match = None
            if hero:
                match = re.search(r"https://images\.unsplash\.com/[^'\" >|]+", str(hero))
            if not match:
                match = re.search(r"https://images\.unsplash\.com/[^'\" >|]+", content)
                
            if match:
                url = match.group(0).split('?')[0] # ignore query params like ?w=1920
                urls[folder] = url
            else:
                urls[folder] = "None"

inv_map = collections.defaultdict(list)
for k, v in urls.items():
    inv_map[v].append(k)

for url, folders in inv_map.items():
    if len(folders) > 1:
        print(f"DUPLICATE URL: {url}")
        print(f"  Used by: {', '.join(folders)}")
    elif url == "None":
        print(f"NO IMAGE URL: {', '.join(folders)}")
