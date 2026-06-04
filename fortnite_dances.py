import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Fortnite Dances"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "fortnite_dances"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "403857b1-56d1-4472-a9ac-0cc156fe70a8"

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
            "السؤال": "خمن الرقصة؟!",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 300
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("fortnite_dances_questions.xlsx", index=False)

print("Done ✅")