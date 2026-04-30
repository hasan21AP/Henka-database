import os
import re
import time
import requests
import pandas as pd

IMAGES_DIR = "anime_images"
OUTPUT_FILE = "anime_characters.xlsx"
TARGET_COUNT = 200

os.makedirs(IMAGES_DIR, exist_ok=True)

def safe_filename(name):
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_") + ".jpg"

def download_image(image_url, save_path):
    response = requests.get(image_url, timeout=20)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(response.content)

existing_files = set(os.listdir(IMAGES_DIR))
new_questions = []

page = 1

while len(new_questions) < TARGET_COUNT:
    print(f"Fetching page {page}...")

    url = "https://api.jikan.moe/v4/characters"
    params = {
        "page": page,
        "limit": 25,
        "order_by": "favorites",
        "sort": "desc"
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json().get("data", [])

    if not data:
        break

    for character in data:
        if len(new_questions) >= TARGET_COUNT:
            break

        name = character.get("name", "").strip()
        image_url = character.get("images", {}).get("jpg", {}).get("image_url", "")

        if not name or not image_url:
            continue

        filename = safe_filename(name)
        save_path = os.path.join(IMAGES_DIR, filename)

        # Skip characters already downloaded
        if filename in existing_files or os.path.exists(save_path):
            print(f"Skipped existing: {name}")
            continue

        try:
            download_image(image_url, save_path)

            new_questions.append({
                "السؤال": "من هذه الشخصية؟",
                "الصورة": save_path,
                "الإجابة": name,
                "التصنيف": "شخصيات الأنمي",
                "النقاط": 100
            })

            existing_files.add(filename)
            print(f"Downloaded {len(new_questions)}/{TARGET_COUNT}: {name}")

            time.sleep(1)

        except Exception as e:
            print(f"Failed: {name} -> {e}")
            continue

    page += 1
    time.sleep(1)

df = pd.DataFrame(new_questions, columns=[
    "السؤال",
    "الصورة",
    "الإجابة",
    "التصنيف",
    "النقاط"
])

df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl")

print("Done!")
print(f"Downloaded: {len(df)} new images")
print(f"Excel file: {OUTPUT_FILE}")
print(f"Images folder: {IMAGES_DIR}")