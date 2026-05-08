import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Spacetoon Arabic songs"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "spacetoon_songs"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "084ec4e8-bf2a-4b7d-b239-8f82e8a180b4"

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
            "السؤال": "ما اسم شارة البداية من سبيستون؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 100
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("spacetoon_songs_questions.xlsx", index=False)

print("Done ✅")