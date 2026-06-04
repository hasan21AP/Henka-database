import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

في لعبة Hollow Knight، ما اسم بطل اللعبة؟,The Knight,ألعاب,100
في Hollow Knight، ما اسم المملكة التي تدور فيها الأحداث؟,Hallownest,ألعاب,100
ما اسم الشركة المطورة للعبة Hollow Knight؟,Team Cherry,ألعاب,100
في Hollow Knight، ما اسم الشخصية الأنثوية المقنعة الشهيرة؟,Hornet,ألعاب,100
ما اسم العملة داخل Hollow Knight؟,Geo,ألعاب,100
في Hollow Knight، ما اسم السلاح الأساسي للبطل؟,Nail,ألعاب,100
ما اسم الشخصية التي تبيع الخرائط؟,Cornifer,ألعاب,100
في Hollow Knight، ما اسم زوجة Cornifer التي تبيع الأدوات؟,Iselda,ألعاب,100
ما اسم المنطقة الرئيسية الأولى في اللعبة؟,Dirtmouth,ألعاب,100
في Hollow Knight، ما اسم المنطقة الخضراء الشهيرة؟,Greenpath,ألعاب,100
ما اسم المدينة الممطرة الشهيرة في Hollow Knight؟,City of Tears,ألعاب,100
في Hollow Knight، ما اسم المنطقة المليئة بالفطريات؟,Fungal Wastes,ألعاب,100
ما اسم المنطقة المظلمة المليئة بالعناكب؟,Deepnest,ألعاب,100
في Hollow Knight، ما اسم نقاط التنقل السريع؟,Stag Stations,ألعاب,100
ما اسم الحشرة التي تنقل اللاعب بين المحطات؟,The Last Stag,ألعاب,100
في Hollow Knight، ما اسم التعويذات التي تعطي قدرات إضافية؟,Charms,ألعاب,100
ما اسم القدرة التي تسمح بالاندفاع؟,Mothwing Cloak,ألعاب,100
في Hollow Knight، ما اسم القدرة التي تسمح بالقفز المزدوج؟,Monarch Wings,ألعاب,100
ما اسم الكائنات الصغيرة التي ينقذها اللاعب؟,Grubs,ألعاب,100
في Hollow Knight، ما اسم الزعيم النهائي الأساسي؟,The Hollow Knight,ألعاب,100

في Hollow Knight، ما اسم الزعيم الثلاثي الشهير في Fungal Wastes؟,Mantis Lords,ألعاب,300
ما اسم الأداة التي تسمح للبطل بدخول الأحلام؟,Dream Nail,ألعاب,300
في Hollow Knight، ما اسم الشخصية التي تمنح اللاعب Dream Nail؟,Seer,ألعاب,300
ما اسم الملك الذي حكم مملكة Hallownest؟,Pale King,ألعاب,300
في Hollow Knight، ما اسم مصدر العدوى البرتقالية؟,The Radiance,ألعاب,300
ما اسم العدوى التي أصابت مملكة Hallownest؟,The Infection,ألعاب,300
في Hollow Knight، ما اسم الزعيم الموجود في City of Tears ويستخدم قوى الأرواح؟,Soul Master,ألعاب,300
ما اسم المنطقة البلورية في Hollow Knight؟,Crystal Peak,ألعاب,300
في Hollow Knight، ما اسم الزعيم الموجود داخل Crystal Peak؟,Crystal Guardian,ألعاب,300
ما اسم المنطقة التي يوجد فيها White Palace؟,Ancient Basin,ألعاب,300
في Hollow Knight، ما اسم المكان العميق الذي وُلدت فيه الـ Vessels؟,The Abyss,ألعاب,300
ما اسم الزعيم الذي يقلد شكل البطل داخل Deepnest؟,Nosk,ألعاب,300
في Hollow Knight، ما اسم الزعيم الموجود داخل Hive؟,Hive Knight,ألعاب,300
ما اسم المنطقة التي تحتوي على النحل؟,The Hive,ألعاب,300
في Hollow Knight، ما اسم الشخصية التي تبيع Charms؟,Salubra,ألعاب,300
ما اسم الحداد الذي يطور سلاح الـ Nail؟,Nailsmith,ألعاب,300
في Hollow Knight، ما اسم المادة المطلوبة لتطوير الـ Nail؟,Pale Ore,ألعاب,300
ما اسم أقوى تطوير لسلاح الـ Nail؟,Pure Nail,ألعاب,300
في Hollow Knight، ما اسم الكولوسيوم القتالي؟,Colosseum of Fools,ألعاب,300
ما اسم الشخصية التي تدعي أنها أعظم محارب؟,Zote,ألعاب,300

في Hollow Knight، ما اسم الزعيم النهائي الحقيقي المرتبط بالنهاية السرية؟,The Radiance,ألعاب,500
ما اسم النسخة الأصعب من Radiance في Godmaster؟,Absolute Radiance,ألعاب,500
في Hollow Knight، ما اسم والدة Hornet؟,Herrah the Beast,ألعاب,500
ما اسم والد Hornet؟,Pale King,ألعاب,500
في Hollow Knight، من هم الثلاثة الذين ختموا The Hollow Knight؟,Dreamers,ألعاب,500
ما اسم الـ Dreamer الموجود في Deepnest؟,Herrah,ألعاب,500
في Hollow Knight، ما اسم الـ Dreamer الموجود في Fog Canyon؟,Monomon,ألعاب,500
ما اسم الـ Dreamer الموجود في City of Tears؟,Lurien,ألعاب,500
في Hollow Knight، ما اسم النسخة الأقوى من Soul Master؟,Soul Tyrant,ألعاب,500
ما اسم النسخة الأقوى من Broken Vessel؟,Lost Kin,ألعاب,500
في Hollow Knight، ما اسم النسخة الحلمية من Zote؟,Grey Prince Zote,ألعاب,500
ما اسم الزعيم المرتبط بفرقة Grimm Troupe؟,Grimm,ألعاب,500
في Hollow Knight، ما اسم النسخة الأصعب من Grimm؟,Nightmare King Grimm,ألعاب,500
ما اسم الزعيم الموجود في Royal Waterways؟,Dung Defender,ألعاب,500
في Hollow Knight، ما اسم النسخة الحلمية من Dung Defender؟,White Defender,ألعاب,500
ما اسم المنطقة التي تحتوي على Hunter’s Journal؟,Greenpath,ألعاب,500
في Hollow Knight، ما اسم القدرة المطورة لـ Vengeful Spirit؟,Shade Soul,ألعاب,500
ما اسم القدرة المطورة لـ Desolate Dive؟,Descending Dark,ألعاب,500
في Hollow Knight، ما اسم القدرة المطورة لـ Howling Wraiths؟,Abyss Shriek,ألعاب,500
ما اسم القدرة التي تسمح بالاندفاع عبر الأعداء والظلال؟,Shade Cloak,ألعاب,500

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
file_path = os.path.join(os.getcwd(), "hollow_night_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
