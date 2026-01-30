import pandas as pd
import sqlite3

# تحميل ملف Excel
excel_file = "wwe_questions.xlsx"  # تأكد من وضع اسم ملفك الصحيح
df = pd.read_excel(excel_file)

# الاتصال بقاعدة البيانات
conn = sqlite3.connect("henka-version-4_1.db")  # تأكد من أن قاعدة بياناتك موجودة
cursor = conn.cursor()

# التحقق من أن الجدول موجود
cursor.execute('''
CREATE TABLE IF NOT EXISTS wwe_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    points INTEGER NOT NULL
)
''')

# إدراج البيانات من Excel إلى SQLite
for index, row in df.iterrows():
    cursor.execute("INSERT INTO wwe_questions (question, answer, points) VALUES (?, ?, ?)",
                   (row["السؤال"], row["الإجابة"], row["النقاط"]))

# حفظ التغييرات
conn.commit()
conn.close()

print("Insert data done!")
