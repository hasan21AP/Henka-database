import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

في لعبة Dark Souls، ما اسم الجملة الشهيرة عند الموت؟,You Died,ألعاب,100
في لعبة Elden Ring، ما اسم العالم المفتوح الرئيسي؟,The Lands Between,ألعاب,100
في لعبة Bloodborne، ما اسم المدينة الرئيسية؟,Yharnam,ألعاب,100
في لعبة Sekiro، ما اسم البطل؟,Wolf,ألعاب,100
في لعبة Dark Souls، ما اسم العملة التي تجمعها من الأعداء؟,Souls,ألعاب,100
في لعبة Elden Ring، ما اسم العملة المستخدمة للتطوير؟,Runes,ألعاب,100
في لعبة Bloodborne، ما اسم العملة الأساسية؟,Blood Echoes,ألعاب,100
في لعبة Sekiro، ما نوع سلاح البطل الرئيسي؟,Katana,ألعاب,100
ما اسم الشركة المطورة لسلسلة Dark Souls؟,FromSoftware,ألعاب,100
ما اسم مخرج أغلب ألعاب السولز الشهيرة؟,Hidetaka Miyazaki,ألعاب,100
في Dark Souls، ما اسم نقاط الحفظ والراحة؟,Bonfires,ألعاب,100
في Elden Ring، ما اسم نقاط الراحة؟,Sites of Grace,ألعاب,100
في Bloodborne، ما اسم السلاح الذي يتحول بين شكلين؟,Trick Weapon,ألعاب,100
في Sekiro، ما اسم الذراع الصناعية للبطل؟,Shinobi Prosthetic,ألعاب,100
في Dark Souls، ما اسم أول زعيم مشهور في اللعبة الأولى؟,Asylum Demon,ألعاب,100
في Elden Ring، ما اسم أول زعيم صعب مشهور في بداية اللعبة؟,Margit,ألعاب,100
في Bloodborne، ما اسم أول زعيم رئيسي مشهور؟,Cleric Beast,ألعاب,100
في Sekiro، ما اسم الزعيم الذي يقطع ذراع البطل؟,Genichiro,ألعاب,100
ما اسم لعبة السولز التي تدور في عالم قوطي مرعب؟,Bloodborne,ألعاب,100
ما اسم لعبة السولز التي تعتمد على الساموراي والشينوبي؟,Sekiro,ألعاب,100
ما اسم لعبة FromSoftware التي صدرت قبل Dark Souls وتعتبر بداية الأسلوب؟,Demon’s Souls,ألعاب,100
في Demon’s Souls، ما اسم المنطقة المركزية؟,Nexus,ألعاب,100
في Dark Souls، ما اسم المدينة المليئة بالموتى في البداية؟,Undead Burg,ألعاب,100
في Elden Ring، ما اسم الحصان الذي تركبه؟,Torrent,ألعاب,100
في Bloodborne، ما اسم الصيادين في اللعبة؟,Hunters,ألعاب,100
في Sekiro، ما اسم لقب البطل؟,One-Armed Wolf,ألعاب,100
ما اسم اللعبة التي تحتوي على شخصية Melina؟,Elden Ring,ألعاب,100
ما اسم اللعبة التي تحتوي على شخصية Lady Maria؟,Bloodborne,ألعاب,100
ما اسم اللعبة التي تحتوي على شخصية Solaire؟,Dark Souls,ألعاب,100
ما اسم اللعبة التي تحتوي على شخصية Malenia؟,Elden Ring,ألعاب,100
في Dark Souls، ما اسم العبارة الشهيرة المرتبطة بـ Solaire؟,Praise the Sun,ألعاب,100
في Elden Ring، ما اسم شجرة العالم الضخمة؟,Erdtree,ألعاب,100
في Bloodborne، ما اسم حلم الصياد؟,Hunter’s Dream,ألعاب,100
في Sekiro، ما اسم نظام كسر توازن العدو؟,Posture,ألعاب,100
في ألعاب السولز، ما اسم الزعيم الكبير الذي تقاتله؟,Boss,ألعاب,100
في ألعاب السولز، ما اسم اللاعب عندما يغزو عالم لاعب آخر؟,Invader,ألعاب,100
في Dark Souls، ما اسم القوارير التي تعالج اللاعب؟,Estus Flask,ألعاب,100
في Elden Ring، ما اسم القارورة التي تعالج الصحة؟,Flask of Crimson Tears,ألعاب,100
في Bloodborne، ما اسم أداة العلاج الأساسية؟,Blood Vial,ألعاب,100
في Sekiro، ما اسم أداة العلاج الأساسية؟,Healing Gourd,ألعاب,100
ما اسم لعبة السولز التي تحتوي على The Tarnished؟,Elden Ring,ألعاب,100
ما اسم الشخصية الرئيسية في Elden Ring؟,Tarnished,ألعاب,100
ما اسم الشخصية الرئيسية في Dark Souls غالبًا؟,Chosen Undead,ألعاب,100
ما اسم الشخصية الرئيسية في Bloodborne؟,Hunter,ألعاب,100
في Elden Ring، ما اسم السلاح الأسطوري الذي تستخدمه Malenia؟,Hand of Malenia,ألعاب,100
في Bloodborne، ما اسم سلاح المنشار الشهير؟,Saw Cleaver,ألعاب,100
في Sekiro، ما اسم أداة الخطاف؟,Grappling Hook,ألعاب,100
ما اسم لعبة السولز التي تحتوي على Firelink Shrine؟,Dark Souls,ألعاب,100
ما اسم لعبة السولز التي تحتوي على Roundtable Hold؟,Elden Ring,ألعاب,100
ما اسم لعبة السولز التي تحتوي على Ashina؟,Sekiro,ألعاب,100

في Dark Souls، ما اسم الزعيمين الشهيرين في Anor Londo؟,Ornstein and Smough,ألعاب,300
في Elden Ring، ما اسم الزعيمة التي تقول إنها لم تعرف الهزيمة؟,Malenia,ألعاب,300
في Bloodborne، ما اسم الزعيم الموجود أعلى Grand Cathedral؟,Vicar Amelia,ألعاب,300
في Sekiro، ما اسم الزعيم الموجود فوق قلعة Ashina؟,Genichiro Ashina,ألعاب,300
في Demon’s Souls، ما اسم الزعيم الشهير في Shrine of Storms؟,Old Hero,ألعاب,300
في Dark Souls، ما اسم المدينة الذهبية الشهيرة؟,Anor Londo,ألعاب,300
في Elden Ring، ما اسم أول منطقة كبيرة بعد البداية؟,Limgrave,ألعاب,300
في Bloodborne، ما اسم المنطقة التي تبدأ منها اللعبة؟,Central Yharnam,ألعاب,300
في Sekiro، ما اسم العشيرة الحاكمة في اللعبة؟,Ashina,ألعاب,300
في Dark Souls، ما اسم التنين العاري الشهير؟,Seath the Scaleless,ألعاب,300
في Elden Ring، ما اسم نصف الإله صاحب المطرقة والفأس؟,Godrick,ألعاب,300
في Bloodborne، ما اسم الزعيم الصياد القديم في بداية اللعبة؟,Father Gascoigne,ألعاب,300
في Sekiro، ما اسم السيدة العجوز التي تقاتلها في Hirata Estate؟,Lady Butterfly,ألعاب,300
في Dark Souls، ما اسم المنطقة السامة الشهيرة؟,Blighttown,ألعاب,300
في Elden Ring، ما اسم المنطقة الحمراء المصابة بالعفن؟,Caelid,ألعاب,300
في Bloodborne، ما اسم المنطقة الكابوسية المرتبطة بالعلماء؟,Nightmare of Mensis,ألعاب,300
في Sekiro، ما اسم القرد الزعيم الشهير؟,Guardian Ape,ألعاب,300
في Dark Souls، ما اسم العهد المرتبط بـ Solaire؟,Warrior of Sunlight,ألعاب,300
في Elden Ring، ما اسم السحر الأزرق الشهير الذي يطلق شعاعًا قويًا؟,Comet Azur,ألعاب,300
في Bloodborne، ما اسم الإحصائية التي تؤثر على الأسلحة النارية؟,Bloodtinge,ألعاب,300
في Sekiro، ما اسم الضربة التي تقتل العدو بعد كسر توازنه؟,Deathblow,ألعاب,300
في Dark Souls، ما اسم الشخصية التي تقول Praise the Sun؟,Solaire of Astora,ألعاب,300
في Elden Ring، ما اسم رفيقة اللاعب في بداية الرحلة؟,Melina,ألعاب,300
في Bloodborne، ما اسم الدمية التي تساعد اللاعب على التطوير؟,The Doll,ألعاب,300
في Sekiro، ما اسم السيد الصغير الذي يحميه Wolf؟,Kuro,ألعاب,300
في Demon’s Souls، ما اسم الزعيم الذي يشبه الفارس الضخم في البداية؟,Tower Knight,ألعاب,300
في Dark Souls، ما اسم الزعيم الأخير في اللعبة الأولى؟,Gwyn,ألعاب,300
في Elden Ring، ما اسم الزعيم الأخير قبل النهاية الأساسية؟,Elden Beast,ألعاب,300
في Bloodborne، ما اسم الزعيم النهائي السري؟,Moon Presence,ألعاب,300
في Sekiro، ما اسم الزعيم النهائي الشهير؟,Isshin,ألعاب,300
في Dark Souls III، ما اسم الزعيم الأخير؟,Soul of Cinder,ألعاب,300
في Dark Souls، ما اسم الفرسان السود؟,Black Knights,ألعاب,300
في Elden Ring، ما اسم الفارس الذهبي في بداية اللعبة؟,Tree Sentinel,ألعاب,300
في Bloodborne، ما اسم الوحوش الكبيرة القديمة؟,Great Ones,ألعاب,300
في Sekiro، ما اسم الهجوم الذي يجب القفز فوقه أو تفاديه؟,Perilous Attack,ألعاب,300
في Elden Ring، ما اسم تقنية استدعاء الأرواح؟,Spirit Ashes,ألعاب,300
في Dark Souls، ما اسم الزعيم الذئب الكبير؟,Great Grey Wolf Sif,ألعاب,300
في Bloodborne، ما اسم السيف القمري الشهير؟,Holy Moonlight Sword,ألعاب,300
في Sekiro، ما اسم أداة التصدي للرماح؟,Mikiri Counter,ألعاب,300
في Demon’s Souls، ما اسم النظام الذي يغير صعوبة العالم؟,World Tendency,ألعاب,300
في Dark Souls II، ما اسم المنطقة المركزية؟,Majula,ألعاب,300
في Dark Souls III، ما اسم المنطقة المركزية؟,Firelink Shrine,ألعاب,300
في Elden Ring، ما اسم المدينة الملكية؟,Leyndell,ألعاب,300
في Bloodborne، ما اسم الإضافة الشهيرة للعبة؟,The Old Hunters,ألعاب,300
في Sekiro، ما اسم نهاية التخلي عن Kuro؟,Shura Ending,ألعاب,300
في Elden Ring، ما اسم زعيم النجوم الشهير؟,Starscourge Radahn,ألعاب,300
في Dark Souls، ما اسم الزعيم الموجود في Painted World؟,Crossbreed Priscilla,ألعاب,300
في Bloodborne، ما اسم الصياد الشهير في الإضافة؟,Lady Maria,ألعاب,300
في Sekiro، ما اسم الثعبان العملاق؟,Great Serpent,ألعاب,300
في Elden Ring، ما اسم شخصية نصف الذئب؟,Blaidd,ألعاب,300

في Dark Souls، ما اسم الشعلة التي تدور حولها قصة العالم؟,First Flame,ألعاب,500
في Elden Ring، ما اسم الملكة التي كسرت الخاتم العظيم؟,Queen Marika,ألعاب,500
في Bloodborne، ما اسم الدم القديم الذي سبب لعنة المدينة؟,Old Blood,ألعاب,500
في Sekiro، ما اسم مصدر الخلود المرتبط بـ Kuro؟,Dragon’s Heritage,ألعاب,500
في Demon’s Souls، ما اسم الكيان القديم المرتبط بالضباب؟,The Old One,ألعاب,500
في Dark Souls، ما اسم اللورد الذي ضحى بنفسه لإطالة عصر النار؟,Gwyn,ألعاب,500
في Elden Ring، ما اسم الزوج والجانب الآخر لـ Marika؟,Radagon,ألعاب,500
في Bloodborne، ما اسم المدرسة التي درست الأسرار الكونية؟,Byrgenwerth,ألعاب,500
في Sekiro، ما اسم الزعيم الذي يظهر من جسد Genichiro في النهاية؟,Isshin the Sword Saint,ألعاب,500
في Dark Souls، ما اسم الفارس الذي تحرس روحه قبر Artorias؟,Sif,ألعاب,500
في Elden Ring، ما اسم الإلهة المرتبطة بالعفن القرمزي؟,Malenia,ألعاب,500
في Bloodborne، ما اسم الزعيم في نهاية إضافة The Old Hunters؟,Orphan of Kos,ألعاب,500
في Sekiro، ما اسم النهاية التي يتحول فيها Wolf إلى Shura؟,Shura,ألعاب,500
في Demon’s Souls، ما اسم الزعيم الذي يتحكم فيه لاعب آخر أحيانًا؟,Old Monk,ألعاب,500
في Dark Souls III، ما اسم الزعيم الراقص في Lothric؟,Dancer of the Boreal Valley,ألعاب,500
في Elden Ring، ما اسم المدينة الأبدية تحت الأرض؟,Nokron,ألعاب,500
في Bloodborne، ما اسم الزعيم الذي يظهر في Hunter’s Dream؟,Gehrman,ألعاب,500
في Sekiro، ما اسم القرد الذي تقاتله بعد قطع رأسه؟,Guardian Ape,ألعاب,500
في Dark Souls، ما اسم ملكة الفوضى المرتبطة بـ Bed of Chaos؟,Witch of Izalith,ألعاب,500
في Elden Ring، ما اسم زعيم Volcano Manor؟,Rykard,ألعاب,500
في Bloodborne، ما اسم الكائن الذي يجعل الناس يرون الحقيقة الكونية؟,Insight,ألعاب,500
في Sekiro، ما اسم أداة الذراع التي تطلق الشوريكن؟,Loaded Shuriken,ألعاب,500
في Dark Souls II، ما اسم الملك المفقود في Drangleic؟,Vendrick,ألعاب,500
في Dark Souls III، ما اسم الأميرين الزعيمين قرب نهاية اللعبة؟,Lorian and Lothric,ألعاب,500
في Elden Ring، ما اسم القلعة التي يحكمها Godrick؟,Stormveil Castle,ألعاب,500
في Bloodborne، ما اسم المنطقة التي تحتوي على أمغدالا؟,Nightmare Frontier,ألعاب,500
في Sekiro، ما اسم المنطقة التي تحتوي على Fountainhead Palace؟,Fountainhead Palace,ألعاب,500
في Demon’s Souls، ما اسم الفارس الأسود الشهير كزعيم اختياري؟,Old King Doran,ألعاب,500
في Dark Souls، ما اسم الزعيم الذي يمثل بقايا Nito؟,Gravelord Nito,ألعاب,500
في Elden Ring، ما اسم زعيم الدم الشهير؟,Mohg,ألعاب,500
في Bloodborne، ما اسم الملكة المرتبطة بـ Vilebloods؟,Annalise,ألعاب,500
في Sekiro، ما اسم عدو Ashina العجوز الذي يستخدم الرمح والسيف؟,Isshin Ashina,ألعاب,500
في Dark Souls III، ما اسم الزعيم الموجود في Painted World of Ariandel؟,Sister Friede,ألعاب,500
في Elden Ring، ما اسم السيف الشهير المرتبط بـ Ranni؟,Dark Moon Greatsword,ألعاب,500
في Bloodborne، ما اسم السلاح الذي يستخدمه Gehrman؟,Burial Blade,ألعاب,500
في Sekiro، ما اسم التقنية التي تسمح بدوس الطعنات؟,Mikiri Counter,ألعاب,500
في Demon’s Souls، ما اسم أول زعيم في Boletarian Palace؟,Phalanx,ألعاب,500
في Dark Souls، ما اسم المدينة الغارقة في الظلام داخل الإضافة؟,Oolacile,ألعاب,500
في Elden Ring، ما اسم التنين ذو الرأسين المرتبط بالزمن؟,Dragonlord Placidusax,ألعاب,500
في Bloodborne، ما اسم الصيادة التي تحمي Astral Clocktower؟,Lady Maria,ألعاب,500
في Sekiro، ما اسم الراهب الفاسد؟,Corrupted Monk,ألعاب,500
في Dark Souls II، ما اسم الزعيم القديم المرتبط بالتنانين؟,Ancient Dragon,ألعاب,500
في Dark Souls III، ما اسم التنين المجهول الشهير؟,Nameless King,ألعاب,500
في Elden Ring، ما اسم الزعيم الذي يقول Together we will devour the gods؟,Rykard,ألعاب,500
في Bloodborne، ما اسم الطائفة التي تقف خلف Healing Church؟,Healing Church,ألعاب,500
في Sekiro، ما اسم والد Wolf بالتبني؟,Owl,ألعاب,500
في Demon’s Souls، ما اسم العالم الأول في اللعبة؟,Boletarian Palace,ألعاب,500
في Dark Souls، ما اسم الزعيم الذي يحرس الجرس في الأعلى؟,Bell Gargoyles,ألعاب,500
في Elden Ring، ما اسم الزعيمة المرتبطة بالقمر في Academy of Raya Lucaria؟,Rennala,ألعاب,500
في Bloodborne، ما اسم الكابوس الخاص بالصيادين القدماء؟,Hunter’s Nightmare,ألعاب,500


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
file_path = os.path.join(os.getcwd(), "soles_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
