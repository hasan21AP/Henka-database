import os
from urllib.parse import quote
import pandas as pd

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Openings"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "anime_songs"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "e21a77b9-cb19-4dad-b01c-51c7d6654992"

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

        # 🔹 اسم الأنمي (نظف الاسم)
        answer = file_name.replace(".webm", "")

        rows.append({
            "السؤال": "في أي أنمي هذه الأغنية؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 100
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("anime_songs_questions.xlsx", index=False)

print("Done ✅")