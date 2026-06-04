import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\WWE Theme Songs"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "wwe_songs"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "0d118d4e-ea5e-4fdf-922a-780fd7fe6ce5"

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
            "السؤال": "من هذا المصارع؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 250
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("wwe_songs_questions.xlsx", index=False)

print("Done ✅")