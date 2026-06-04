import os
from urllib.parse import quote
import pandas as pd

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Anime OST"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "anime_osts"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "9a4b0797-0708-4fbd-82c0-e16086f77e8b"

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

        # 🔹 اسم الأنمي (نظف الاسم)
        answer = file_name.replace(".mp3", "")

        rows.append({
            "السؤال": "في أي أنمي هذا الأوست؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 250
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("anime_osts_questions.xlsx", index=False)

print("Done ✅")