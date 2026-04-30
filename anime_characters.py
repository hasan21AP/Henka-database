import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/11/516835.jpg,Spike Spiegel,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/15/264961.jpg,Faye Valentine,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/284121.jpg,Edward Wong,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Lelouch Lamperouge,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Monkey D. Luffy,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Roronoa Zoro,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Nami,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Uzumaki Naruto,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Uchiha Sasuke,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Haruno Sakura,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Eren Yeager,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Mikasa Ackerman,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Levi Ackerman,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Light Yagami,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,L Lawliet,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Near,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Ichigo Kurosaki,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Rukia Kuchiki,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Orihime Inoue,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Goku,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Vegeta,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Gohan,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Killua Zoldyck,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Gon Freecss,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Hisoka,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Edward Elric,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Alphonse Elric,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Roy Mustang,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Saitama,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Genos,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Tanjiro Kamado,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Nezuko Kamado,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Zenitsu Agatsuma,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Inosuke Hashibira,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Kakashi Hatake,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Itachi Uchiha,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Obito Uchiha,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Madara Uchiha,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Asta,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Yuno,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Noelle Silva,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Rimuru Tempest,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Shinra Kusakabe,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Arthur Boyle,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/9/131317.jpg,Kenshin Himura,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/7/284123.jpg,Yagami Taichi,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/2/241413.jpg,Kaneki Ken,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/10/216895.jpg,Arima Kishou,شخصيات الأنمي,100
from هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/13/284122.jpg,Todoroki Shoto,شخصيات الأنمي,100
من هذه الشخصية؟,https://cdn.myanimelist.net/images/characters/3/328016.jpg,Midoriya Izuku,شخصيات الأنمي,100

"""

# تحويل البيانات النصية إلى قائمة من الأسطر
lines = data.strip().split("\n")

# تحويل كل سطر إلى قائمة فرعية بعد التحقق من صحة عدد الأعمدة
questions_list = [line.split(",") for line in lines if len(line.split(",")) == 5]

# تعريف أسماء الأعمدة
columns = ["السؤال", "الصورة", "الإجابة", "التصنيف", "النقاط"]

# تحويل القائمة إلى DataFrame
df = pd.DataFrame(questions_list, columns=columns)

# تحديد مسار حفظ الملف في نفس مجلد الكود
file_path = os.path.join(os.getcwd(), "anime_characters_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
