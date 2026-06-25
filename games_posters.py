import os
import re
import mimetypes
from urllib.parse import quote

import pandas as pd

# 🔹 المسار المحلي للصور
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\Games Posters"

# 🔹 بيانات Firebase
bucket = "henka-game.firebasestorage.app"
firebase_folder = "games_posters"

# 🔹 التوكن
token = "97df484a-5953-41b9-b67c-51e2c788667b"

rows = []

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # تجاهل المجلدات
    if not os.path.isfile(file_path):
        continue

    # التأكد أن الملف صورة
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None or not mime_type.startswith("image/"):
        continue

    file_name = file.strip()

    # 🔹 المسار داخل Firebase
    firebase_path = f"{firebase_folder}/{file_name}"

    # 🔹 تحويل المسار إلى URL صالح
    encoded_path = quote(firebase_path, safe="")

    # 🔹 إنشاء رابط Firebase
    url = (
        f"https://firebasestorage.googleapis.com/v0/b/"
        f"{bucket}/o/{encoded_path}?alt=media&token={token}"
    )

    # 🔹 إزالة الامتداد مهما كان
    name = os.path.splitext(file_name)[0]

    # 🔹 حذف الرقم والشرطة من البداية
    # مثال: "001 - GTA V" -> "GTA V"
    answer = re.sub(r"^\d+\s*-\s*", "", name).strip()

    rows.append({
        "السؤال": "ما اسم اللعبة؟",
        "الإجابة": answer,
        "الميديا": url,
        "النقاط": 100
    })

# 🔹 إنشاء ملف Excel
df = pd.DataFrame(rows)
df.to_excel("games_posters_questions.xlsx", index=False)

print(f"Done ✅ Generated {len(rows)} questions.")