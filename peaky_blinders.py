import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Peaky Blinders"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "tv_shows_moments"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "93fd0eec-c732-4c33-92e6-3a88d72de029"

rows = []

for file in os.listdir(folder_path):
    if file.endswith(".mp4"):
        file_name = file.strip()

        # 🔹 المسار داخل Firebase
        path = f"{firebase_folder}/{file_name}"

        # 🔹 encoding
        encoded_path = quote(path, safe="")

        # 🔹 الرابط النهائي
        url = f"https://firebasestorage.googleapis.com/v0/b/{bucket}/o/{encoded_path}?alt=media&token={token}"

        # حذف الامتداد
        name = file_name.replace(".mp4", "")

# حذف الرقم + المسافة + الشرطة من البداية
        answer = re.sub(r"^\d+\s*-\s*", "", name)

        rows.append({
            "السؤال": "خمن المسلسل مع ذكر الحدث؟!",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 300
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("peaky_blinders_questions.xlsx", index=False)

print("Done ✅")