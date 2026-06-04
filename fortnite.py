import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

في لعبة Fortnite، ما اسم الشركة المطورة للعبة؟,Epic Games,ألعاب,100
في Fortnite، ما نوع طور اللعب الأشهر؟,باتل رويال,ألعاب,100
ما اسم العملة داخل لعبة Fortnite؟,V-Bucks,ألعاب,100
في Fortnite، كم لاعب يبدأ عادة في مباراة الباتل رويال؟,100,ألعاب,100
ما اسم الحافلة الطائرة في Fortnite؟,Battle Bus,ألعاب,100
في Fortnite، ما اسم العاصفة التي تضيق منطقة اللعب؟,Storm,ألعاب,100
ما اسم الأداة المستخدمة لكسر الأشياء وجمع الموارد؟,Pickaxe,ألعاب,100
في Fortnite، ما اسم تذكرة الجوائز الموسمية؟,Battle Pass,ألعاب,100
ما اسم الطور الذي أزال البناء من اللعبة؟,Zero Build,ألعاب,100
في Fortnite، ما اسم الطور الإبداعي؟,Creative,ألعاب,100
ما اسم الشخصية الشهيرة التي تشبه الموزة؟,Peely,ألعاب,100
في Fortnite، ما اسم الشخصية السمكية الشهيرة؟,Fishstick,ألعاب,100
ما اسم الشخصية الذهبية الشهيرة في Fortnite؟,Midas,ألعاب,100
في Fortnite، ما اسم الرقصات والحركات داخل اللعبة؟,Emotes,ألعاب,100
ما اسم العنصر الذي يعالج الصحة بالكامل؟,Medkit,ألعاب,100
في Fortnite، ما اسم الدرع الصغير؟,Mini Shield,ألعاب,100
ما اسم السيارة أو الجهاز الذي يعيد إحياء أعضاء الفريق؟,Reboot Van,ألعاب,100
في Fortnite، ما اسم البطاقة التي تسقط من اللاعب بعد موته في الفريق؟,Reboot Card,ألعاب,100
ما اسم السلاح المستخدم للقنص من بعيد؟,Sniper,ألعاب,100
في Fortnite، ما اسم البندقية القريبة الشهيرة؟,Shotgun,ألعاب,100

في Fortnite، ما اسم المنطقة الشهيرة ذات الأبراج؟,Tilted Towers,ألعاب,300
ما اسم المكعب البنفسجي الشهير في Fortnite؟,Kevin the Cube,ألعاب,300
في Fortnite، ما اسم الحدث الذي انتهى بالثقب الأسود؟,The End,ألعاب,300
ما اسم المنظمة التي كان يقودها Midas؟,Ghost,ألعاب,300
في Fortnite، ما اسم المنظمة المنافسة لـ Ghost؟,Shadow,ألعاب,300
ما اسم السلاح الأسطوري المرتبط بـ Midas؟,Drum Gun,ألعاب,300
في Fortnite، ما اسم الشخصية القططية القوية؟,Meowscles,ألعاب,300
ما اسم الشخصية التي تقود The Seven؟,The Foundation,ألعاب,300
في Fortnite، من أدى شخصية The Foundation؟,The Rock,ألعاب,300
ما اسم المنظمة الغامضة التي كانت تتحكم بالجزيرة؟,IO,ألعاب,300
في Fortnite، ما اسم قائدة IO الشهيرة؟,Doctor Slone,ألعاب,300
ما اسم الحدث الموسيقي الخاص بـ Travis Scott؟,Astronomical,ألعاب,300
في Fortnite، ما اسم الحدث الموسيقي الخاص بـ Ariana Grande؟,Rift Tour,ألعاب,300
ما اسم الشرير الضخم من Marvel الذي هاجم الجزيرة؟,Galactus,ألعاب,300
في Fortnite، ما اسم السيف الضوئي القادم من Star Wars؟,Lightsaber,ألعاب,300
ما اسم شخصية Star Wars التي ظهرت داخل Fortnite كعدو قوي؟,Darth Vader,ألعاب,300
في Fortnite، ما اسم المطرقة القوية التي ظهرت في Chapter 4؟,Shockwave Hammer,ألعاب,300
ما اسم الكاتانا السريعة التي ظهرت في Chapter 4؟,Kinetic Blade,ألعاب,300
في Fortnite، ما اسم المدينة المستقبلية اليابانية في Chapter 4؟,Mega City,ألعاب,300
ما اسم العنصر الشهير الذي يعيد الصحة والدرع بالكامل؟,Chug Jug,ألعاب,300

في Fortnite، ما اسم أول خريطة رئيسية في Chapter 1؟,Athena,ألعاب,500
ما اسم خريطة Chapter 2 في Fortnite؟,Apollo,ألعاب,500
في Fortnite، ما اسم خريطة Chapter 3؟,Artemis,ألعاب,500
ما اسم الحدث الذي قلب الخريطة في نهاية Chapter 2؟,The Flip,ألعاب,500
في Fortnite، ما اسم الروبوت العملاق الذي قاتل الوحش؟,Mecha Team Leader,ألعاب,500
ما اسم الوحش العملاق الذي قاتل الروبوت في حدث Final Showdown؟,Devourer,ألعاب,500
في Fortnite، ما اسم الحدث الذي جمع الروبوت والوحش؟,Final Showdown,ألعاب,500
ما اسم الملك الجليدي في Fortnite؟,Ice King,ألعاب,500
في Fortnite، ما اسم المنطقة الثلجية التي احتوت قلعة الجليد؟,Polar Peak,ألعاب,500
ما اسم المركبة الطائرة التي ظهرت في Season 7؟,X-4 Stormwing,ألعاب,500
في Fortnite، ما اسم الشخصية الغامضة المرتبطة بقيادة IO؟,Geno,ألعاب,500
ما اسم المجموعة التي كانت تحاول حماية الجزيرة من IO؟,The Seven,ألعاب,500
في Fortnite، ما اسم قائدة القصة التي خانت اللاعبين في بعض الأحداث؟,Doctor Slone,ألعاب,500
ما اسم المدينة التي دمرها البركان في Chapter 1؟,Tilted Towers,ألعاب,500
في Fortnite، ما اسم السلاح القوي جدًا الذي يستخدمه القناصون لمسافات بعيدة؟,Heavy Sniper Rifle,ألعاب,500
ما اسم القوس المتفجر الشهير في Fortnite؟,Boom Bow,ألعاب,500
في Fortnite، ما اسم السلاح المستقبلي الذي يطلق شعاعًا قويًا؟,Rail Gun,ألعاب,500
ما اسم النسخة الذهبية من شخصية Peely؟,Golden Peely,ألعاب,500
في Fortnite، ما اسم ابنة Midas؟,Jules,ألعاب,500
ما اسم الوضع الذي أصبح مشهورًا لأنه أزال أهم ميزة قديمة في Fortnite؟,Zero Build,ألعاب,500

"""

# تحويل البيانات النصية إلى قائمة من الأسطر
lines = data.strip().split("\n")

# تحويل كل سطر إلى قائمة فرعية بعد التحقق من صحة عدد الأعمدة
questions_list = [line.split(",") for line in lines if len(line.split(",")) == 4]

# تعريف أسماء الأعمدة
columns = ["السؤال", "الإجابة", "التصنيف", "النقاط"]

# تحويل القائمة إلى DataFrame
df = pd.DataFrame(questions_list, columns=columns)

# تحديد مسار حفظ الملف في نفس مجلد الكود
file_path = os.path.join(os.getcwd(), "fortnite_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
