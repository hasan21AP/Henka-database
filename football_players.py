import os
import urllib.parse
import pandas as pd

IMAGES_DIR = "football_players_images"
OUTPUT_FILE = "football_players_firebase_questions.xlsx"

BASE_URL = "https://firebasestorage.googleapis.com/v0/b/henka-game.firebasestorage.app/o/football_players_images%2F"
TOKEN = "637d7f53-fb63-4868-b97f-c5aa90fe69f6"

def answer_from_filename(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace("_", " ")
    return name.title()

rows = []

for filename in sorted(os.listdir(IMAGES_DIR)):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        continue

    encoded_filename = urllib.parse.quote(filename)
    image_url = f"{BASE_URL}{encoded_filename}?alt=media&token={TOKEN}"

    rows.append({
        "السؤال": "من هذا اللاعب؟",
        "الصورة": image_url,
        "الإجابة": answer_from_filename(filename),
        "التصنيف": "لاعبين كرة القدم",
        "النقاط": 100
    })

df = pd.DataFrame(rows, columns=["السؤال", "الصورة", "الإجابة", "التصنيف", "النقاط"])
df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl")

print(f"Done: {len(df)} questions saved to {OUTPUT_FILE}")