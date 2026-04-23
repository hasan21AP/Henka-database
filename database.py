import pandas as pd
import sqlite3
from pathlib import Path

# اسم قاعدة البيانات
db_file = "henka-version-4.6.db"

# الاتصال بقاعدة البيانات
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# المجلد الحالي
current_folder = Path(".")

# البحث عن كل ملفات Excel التي تنتهي بـ _questions.xlsx
excel_files = current_folder.glob("*_questions.xlsx")

for excel_path in excel_files:
    try:
        # اسم الملف بدون الامتداد
        file_stem = excel_path.stem
        # مثال: anime_questions
        table_name = file_stem

        print(f"Processing: {excel_path.name} -> Table: {table_name}")

        # قراءة ملف Excel
        df = pd.read_excel(excel_path)

        # التحقق من الأعمدة المطلوبة
        required_columns = ["السؤال", "الإجابة", "النقاط"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"العمود '{col}' غير موجود في الملف {excel_path.name}")

        # إنشاء الجدول إذا لم يكن موجودًا
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{table_name}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            points INTEGER NOT NULL
        )
        ''')

        # إدراج البيانات
        for _, row in df.iterrows():
            question = str(row["السؤال"]).strip()
            answer = str(row["الإجابة"]).strip()
            points = int(row["النقاط"])

            cursor.execute(
                f'INSERT INTO "{table_name}" (question, answer, points) VALUES (?, ?, ?)',
                (question, answer, points)
            )

        print(f"Done: {excel_path.name}")

    except Exception as e:
        print(f"Error in file {excel_path.name}: {e}")

# حفظ التغييرات وإغلاق الاتصال
conn.commit()
conn.close()

print("All Excel files processed successfully!")