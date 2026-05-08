import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Top Songs of the Decade Playlist (2010-2019)"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "songs"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "649fe6e0-05b5-4639-acb2-022f90180412"

rows = []

for file in os.listdir(folder_path):
    if file.endswith(".webm"):
        file_name = file.strip()

        # 🔹 المسار داخل Firebase
        path = f"{firebase_folder}/{file_name}"

        # 🔹 encoding
        encoded_path = quote(path, safe="")

        # 🔹 الرابط النهائي
        url = f"https://firebasestorage.googleapis.com/v0/b/{bucket}/o/{encoded_path}?alt=media&token={token}"

        # حذف الامتداد
        name = file_name.replace(".webm", "")

# حذف الرقم + المسافة + الشرطة من البداية
        answer = re.sub(r"^\d+\s*-\s*", "", name)

        rows.append({
            "السؤال": "ما اسم الأغنية؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 100
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("songs_questions.xlsx", index=False)

print("Done ✅")