import os
from urllib.parse import quote
import pandas as pd

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Cartoons"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "cartoons_songs"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "31f13670-78d2-4e64-aea5-816dc6cd3a0d"

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
        answer = file_name.replace(".webm", "")

        rows.append({
            "السؤال": "في أي كرتون هذه الأغنية؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 250
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("cartoons_songs_questions.xlsx", index=False)

print("Done ✅")