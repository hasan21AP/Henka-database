import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\flags"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "flags"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "20c9520e-0983-4ec3-9c08-209ef6904048"

rows = []

for file in os.listdir(folder_path):
    if file.endswith(".png"):
        file_name = file.strip()

        # 🔹 المسار داخل Firebase
        path = f"{firebase_folder}/{file_name}"

        # 🔹 encoding
        encoded_path = quote(path, safe="")

        # 🔹 الرابط النهائي
        url = f"https://firebasestorage.googleapis.com/v0/b/{bucket}/o/{encoded_path}?alt=media&token={token}"

        # حذف الامتداد
        name = file_name.replace(".png", "")

# حذف الرقم + المسافة + الشرطة من البداية
        answer = re.sub(r"^\d+\s*-\s*", "", name)

        rows.append({
            "السؤال": "ما هي الدولة؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 100
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("flags_questions.xlsx", index=False)

print("Done ✅")