import os
from urllib.parse import quote
import pandas as pd
import re

# 🔹 المسار المحلي
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\المصحف كامل للقارىء سعود الشريم"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "quran_audio"

# ⚠️ نفس التوكن (لو كلهن نفس الشيء)
token = "de5e0d77-755f-4c79-b232-ddf5ec66f97a"

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
            "السؤال": "في أي سورة هذه الآيات؟",
            "الإجابة": answer,
            "الميديا": url,
            "النقاط": 250
        })

# 🔹 تحويل إلى Excel
df = pd.DataFrame(rows)
df.to_excel("quran_audio_questions.xlsx", index=False)

print("Done ✅")