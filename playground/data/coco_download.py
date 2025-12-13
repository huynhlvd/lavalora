import json
import os
import requests
from tqdm import tqdm

# -------- CONFIG --------
JSON_FILE = "/workspace/lavalora/playground/data/llava_instruct_50.json"            # your JSON file
OUTPUT_DIR = "/workspace/lavalora/playground/data/coco/train2017"  # where images will be saved
BASE_URL = "http://images.cocodataset.org/train2017"
# ------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(JSON_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Collect unique image names
image_names = sorted({item["image"] for item in data if "image" in item})

print(f"Found {len(image_names)} unique images")

for img_name in tqdm(image_names):
    url = f"{BASE_URL}/{img_name}"
    out_path = os.path.join(OUTPUT_DIR, img_name)

    if os.path.exists(out_path):
        continue  # skip already downloaded

    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(r.content)
    except Exception as e:
        print(f"Failed to download {img_name}: {e}")

print("Download finished")
