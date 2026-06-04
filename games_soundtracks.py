import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Games sound track"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "games_soundtracks"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "757b0393-7e7a-4a87-b81b-86630005b093"

rows = []

for file in os.listdir(folder_path):
    if file.endswith(".mp3"):
        file_name = file.strip()

        # 🔹 المسار داخل Firebase
        path = f"{firebase_folder}/{file_name}"

        # 🔹 encoding
        encoded_path = quote(path, safe="")

        # 🔹 الرابط النهائي
        url = f"https://firebasestorage.googleapis.com/v0/b/{bucket}/o/{encoded_path}?alt=media&token={token}"

        # حذف الامتداد
        name = file_name.replace(".mp3", "")

# حذف الرقم + المسافة + الشرطة من البداية
        answer = re.sub(r"^\d+\s*-\s*", "", name)

        rows.append({
            "السؤال": "في اي لعبة هذه الموسيقى؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 250
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("games_soundtracks_questions.xlsx", index=False)

print("Done ✅")