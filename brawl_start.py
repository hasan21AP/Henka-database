import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

ما اسم الشركة المطورة للعبة Brawl Stars؟,Supercell,Brawl Stars,100
في أي سنة صدرت Brawl Stars عالميًا؟,2018,Brawl Stars,100
ما اسم الشخصية التي تبدأ بها اللعبة؟,Shelly,Brawl Stars,100
ما نوع سلاح Shelly؟,Shotgun,Brawl Stars,100
ما اسم العملة الذهبية في اللعبة؟,Coins,Brawl Stars,100
ما اسم العملة الخضراء؟,Gems,Brawl Stars,100
ما اسم نظام التقدم في اللعبة؟,Trophies,Brawl Stars,100
ما اسم الطور الذي يعتمد على جمع الجواهر؟,Gem Grab,Brawl Stars,100
كم عدد الجواهر للفوز في Gem Grab؟,10,Brawl Stars,100
ما اسم الطور الذي فيه كرة قدم؟,Brawl Ball,Brawl Stars,100
ما اسم الطور الذي يعتمد على النجوم؟,Bounty,Brawl Stars,100
ما اسم الطور الذي يعتمد على البقاء؟,Showdown,Brawl Stars,100
هل Showdown يمكن أن يكون فردي؟,نعم,Brawl Stars,100
كم عدد اللاعبين في Showdown؟,10,Brawl Stars,100
ما اسم القدرة الخاصة للشخصيات؟,Super,Brawl Stars,100
ما اسم الشخصية التي تستخدم مطرقة؟,Frank,Brawl Stars,100
ما اسم الشخصية التي تطلق صواريخ؟,Brock,Brawl Stars,100
ما اسم الشخصية التي تستخدم السم؟,Crow,Brawl Stars,100
ما اسم الشخصية التي تشفي الفريق؟,Poco,Brawl Stars,100
ما اسم الشخصية التي تستخدم قوس؟,Bo,Brawl Stars,100
ما اسم الشخصية التي تستخدم مضرب؟,Bibi,Brawl Stars,100
ما اسم الشخصية التي تضرب من بعيد؟,Piper,Brawl Stars,100
ما اسم الشخصية التي تطلق نار؟,Amber,Brawl Stars,100
ما اسم الشخصية الروبوتية؟,Rico,Brawl Stars,100
ما اسم الشخصية التي تستخدم قنابل؟,Dynamike,Brawl Stars,100
ما اسم الشخصية التي تستخدم دب؟,Nita,Brawl Stars,100
ما اسم الشخصية التي تستخدم برج؟,Jessie,Brawl Stars,100
ما اسم الوضع الذي يعتمد على سرقة الخزنة؟,Heist,Brawl Stars,100
ما اسم الوضع الدفاعي القديم؟,Siege,Brawl Stars,100
ما اسم الشخصية السريعة جداً؟,Leon,Brawl Stars,100
ما اسم نظام المواسم؟,Brawl Pass,Brawl Stars,100
هل اللعبة تحتاج إنترنت؟,نعم,Brawl Stars,100
ما اسم الأحداث اليومية؟,Events,Brawl Stars,100
ما اسم الشخصية التي تستخدم قفازات؟,El Primo,Brawl Stars,100
ما اسم الشخصية التي تستخدم زجاجات؟,Barley,Brawl Stars,100
ما اسم الشخصية التي تستخدم نباتات؟,Rosa,Brawl Stars,100
ما اسم الشخصية التي تطلق ليزر؟,R-T,Brawl Stars,100
ما اسم الشخصية التي تستخدم الثلج؟,Lou,Brawl Stars,100
ما اسم الشخصية التي تتحرك بسرعة كبيرة؟,Max,Brawl Stars,100
ما اسم الشخصية التي تختفي؟,Leon,Brawl Stars,100
ما اسم الشخصية التي تطلق موجة صوت؟,Poco,Brawl Stars,100
ما اسم الشخصية التي تستخدم مظلة؟,Janet,Brawl Stars,100
ما اسم الشخصية التي تستخدم حقائب؟,Griff,Brawl Stars,100
ما اسم الشخصية التي تستخدم مقلاع؟,Carl,Brawl Stars,100
ما اسم الشخصية التي تستخدم بندقية؟,Colt,Brawl Stars,100
ما اسم الشخصية التي تستخدم طائرات صغيرة؟,Nani,Brawl Stars,100
ما اسم الشخصية التي تعتمد على السرعة؟,Max,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الاختفاء؟,Leon,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الشفاء؟,Pam,Brawl Stars,100
ما اسم الشخصية التي تستخدم ظل؟,Tara,Brawl Stars,100
ما اسم الشخصية التي تستخدم كهرباء؟,Belle,Brawl Stars,100
ما اسم الشخصية التي تستخدم كرة نار؟,Amber,Brawl Stars,100
ما اسم الشخصية التي تستخدم صواريخ متعددة؟,Brock,Brawl Stars,100
ما اسم الشخصية التي تستخدم مطرقة ضخمة؟,Frank,Brawl Stars,100
ما اسم الشخصية التي تعتمد على القفز؟,El Primo,Brawl Stars,100
ما اسم الشخصية التي تستخدم سكين؟,Edgar,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الحظ؟,Chester,Brawl Stars,100
ما اسم الشخصية التي تستخدم الماء؟,Eve,Brawl Stars,100
ما اسم الشخصية التي تستخدم الدرع؟,Jacky,Brawl Stars,100
ما اسم الشخصية التي تطلق طاقة؟,Surge,Brawl Stars,100
ما اسم الشخصية التي تتحول؟,Meg,Brawl Stars,100
ما اسم الشخصية التي تعتمد على القنص؟,Piper,Brawl Stars,100
ما اسم الشخصية التي تعتمد على القتال القريب؟,Bull,Brawl Stars,100
ما اسم الشخصية التي تستخدم مضرب كهربائي؟,Bibi,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق سريع؟,Colt,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق بطيء قوي؟,Frank,Brawl Stars,100
ما اسم الشخصية التي تستخدم السم القاتل؟,Crow,Brawl Stars,100
ما اسم الشخصية التي تعتمد على التجميد؟,Lou,Brawl Stars,100
ما اسم الشخصية التي تعتمد على القفز السريع؟,Edgar,Brawl Stars,100
ما اسم الشخصية التي تعتمد على دعم الفريق؟,Poco,Brawl Stars,100
ما اسم الشخصية التي تعتمد على البرج؟,Jessie,Brawl Stars,100
ما اسم الشخصية التي تعتمد على القنابل؟,Dynamike,Brawl Stars,100
ما اسم الشخصية التي تعتمد على التحكم؟,Tara,Brawl Stars,100
ما اسم الشخصية التي تعتمد على السرقة؟,Colette,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الهروب؟,Leon,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الدفاع؟,Jacky,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الهجوم الجماعي؟,Amber,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الرمي؟,Barley,Brawl Stars,100
ما اسم الشخصية التي تعتمد على السرعة القصوى؟,Max,Brawl Stars,100
ما اسم الشخصية التي تعتمد على التحكم بالعقل؟,Willow,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الضرب القريب؟,El Primo,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق متفرق؟,Shelly,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الطيران؟,Janet,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الروبوت؟,Rico,Brawl Stars,100
ما اسم الشخصية التي تعتمد على القفز العالي؟,El Primo,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق نار مستمر؟,Amber,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق بعيد جداً؟,Piper,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الشفاء الذاتي؟,Edgar,Brawl Stars,100
ما اسم الشخصية التي تعتمد على الطاقة؟,Surge,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق كهرباء؟,Belle,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق موجات؟,Poco,Brawl Stars,100
ما اسم الشخصية التي تعتمد على ضربات قوية؟,Bull,Brawl Stars,100
ما اسم الشخصية التي تعتمد على دعم الفريق بالشفاء؟,Pam,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق القوس؟,Bo,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق الطلقات السريعة؟,Colt,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق القنابل المتفجرة؟,Dynamike,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق السم المستمر؟,Crow,Brawl Stars,100
ما اسم الشخصية التي تعتمد على إطلاق النار من مسافة قريبة؟,Shelly,Brawl Stars,100
أي شخصية تكون أقوى في القتال القريب ضد Piper؟,Bull,Brawl Stars,300
أي شخصية تقدر تهرب بسهولة باستخدام الاختفاء؟,Leon,Brawl Stars,300
أي شخصية تعتبر دعم لأنها تشفي الفريق؟,Poco,Brawl Stars,300
أي طور يناسب الشخصيات بعيدة المدى أكثر؟,Bounty,Brawl Stars,300
إذا كنت تحتاج حماية الخزنة أي نوع شخصيات تختار؟,Defensive,Brawl Stars,300
أي شخصية تعتمد على السرعة للهجوم والانسحاب؟,Max,Brawl Stars,300
أي شخصية تعتبر ضعيفة في القتال القريب لكنها قوية من بعيد؟,Piper,Brawl Stars,300
أي شخصية يمكنها استدعاء حيوان يساعدها؟,Nita,Brawl Stars,300
أي طور يحتاج سيطرة على منطقة معينة؟,Hot Zone,Brawl Stars,300
أي شخصية تقدر تكشف الأعداء المختفين؟,Bo,Brawl Stars,300
إذا كان الخصم قريب جداً أي نوع هجوم أفضل؟,Shotgun,Brawl Stars,300
أي شخصية تعتمد على القفز للهجوم؟,El Primo,Brawl Stars,300
أي شخصية تعتبر الأفضل في إبطاء الأعداء؟,Lou,Brawl Stars,300
أي نوع شخصيات مناسب لGem Grab؟,Balanced,Brawl Stars,300
أي شخصية يمكنها ضرب أكثر من عدو بنفس الوقت بسهولة؟,Amber,Brawl Stars,300
أي شخصية تعتبر قوية ضد الشخصيات البطيئة؟,Colt,Brawl Stars,300
أي طور يحتاج تعاون عالي بين الفريق؟,Brawl Ball,Brawl Stars,300
أي شخصية تعتمد على المفاجأة؟,Leon,Brawl Stars,300
أي شخصية تعتمد على إطلاق مستمر يسبب ضغط؟,Amber,Brawl Stars,300
أي شخصية تحتاج مهارة تصويب عالية؟,Piper,Brawl Stars,300
إذا كان الفريق يحتاج علاج مستمر من تختار؟,Pam,Brawl Stars,300
أي شخصية تعتمد على الهجوم الجماعي؟,Frank,Brawl Stars,300
أي شخصية يمكنها ضرب من خلف الجدران؟,Barley,Brawl Stars,300
أي طور يعتبر الأسرع من حيث إنهاء المباراة؟,Showdown,Brawl Stars,300
أي شخصية تعتمد على السيطرة بالمجال؟,Emz,Brawl Stars,300
أي شخصية تعتبر Counter للشخصيات القريبة؟,Shelly,Brawl Stars,300
أي شخصية تعتمد على الهروب بعد الهجوم؟,Crow,Brawl Stars,300
أي طور يتطلب بقاء آخر لاعب؟,Solo Showdown,Brawl Stars,300
أي شخصية تعتبر Tank؟,Bull,Brawl Stars,300
أي شخصية تعتبر Sniper؟,Piper,Brawl Stars,300
أي شخصية يمكنها جذب الأعداء؟,Tara,Brawl Stars,300
أي شخصية تعتمد على السرقة من الأعداء؟,Colette,Brawl Stars,300
أي طور يعتمد على تدمير الهدف بسرعة؟,Heist,Brawl Stars,300
أي شخصية مناسبة لكسر الجدران؟,Brock,Brawl Stars,300
أي شخصية تعتبر الأفضل في الدفاع عن منطقة؟,Jessie,Brawl Stars,300
أي شخصية تعتمد على الهجوم المتفرق؟,Shelly,Brawl Stars,300
أي شخصية تعتبر قوية ضد الفرق المتجمعة؟,Frank,Brawl Stars,300
أي شخصية تعتمد على إطلاق خط مستقيم دقيق؟,Colt,Brawl Stars,300
أي شخصية يمكنها التنقل بسرعة بين الأعداء؟,Mortis,Brawl Stars,300
أي شخصية تعتمد على الهجوم القريب مع سرعة عالية؟,Edgar,Brawl Stars,300
أي طور يحتاج توزيع الأدوار؟,Gem Grab,Brawl Stars,300
أي شخصية تعتبر الأفضل لكشف المناطق؟,Bo,Brawl Stars,300
أي شخصية تعتمد على القنابل للسيطرة؟,Dynamike,Brawl Stars,300
أي شخصية مناسبة للهجوم المفاجئ؟,Leon,Brawl Stars,300
أي شخصية يمكنها تعطيل الخصم لفترة؟,Lou,Brawl Stars,300
أي شخصية تعتبر قوية في المدى المتوسط؟,Nita,Brawl Stars,300
أي شخصية تعتمد على إطلاق مستمر مع ضرر منخفض؟,Amber,Brawl Stars,300
أي شخصية تعتبر الأفضل في دعم الفريق؟,Poco,Brawl Stars,300
أي شخصية يمكنها إجبار الخصم على التراجع؟,Emz,Brawl Stars,300
أي شخصية مناسبة لقتال 1 ضد 1؟,Bull,Brawl Stars,300
أي شخصية تعتمد على التحكم في مساحة اللعب؟,Barley,Brawl Stars,300
أي شخصية يمكنها تغيير نتيجة القتال فجأة؟,Tara,Brawl Stars,300
أي طور يتطلب تسجيل أهداف؟,Brawl Ball,Brawl Stars,300
أي شخصية تعتبر الأفضل ضد Tanks؟,Colette,Brawl Stars,300
أي شخصية تعتمد على إصابة دقيقة جداً؟,Piper,Brawl Stars,300
أي شخصية مناسبة للضغط المستمر على العدو؟,Crow,Brawl Stars,300
أي شخصية يمكنها حماية الفريق ببرج؟,Jessie,Brawl Stars,300
أي شخصية تعتمد على الهجوم من خلف الحواجز؟,Barley,Brawl Stars,300
أي شخصية يمكنها إبطاء حركة الأعداء؟,Lou,Brawl Stars,300
أي شخصية تعتبر الأفضل في القتال الطويل؟,Pam,Brawl Stars,300
أي شخصية تعتمد على القفز للوصول للعدو؟,El Primo,Brawl Stars,300
أي شخصية يمكنها تقليل ضرر العدو؟,Rosa,Brawl Stars,300
أي شخصية تعتبر الأفضل للهجوم الجماعي؟,Frank,Brawl Stars,300
أي شخصية تعتمد على الهجوم السريع ثم الهروب؟,Crow,Brawl Stars,300
أي شخصية مناسبة للعب الدفاعي؟,Jessie,Brawl Stars,300
أي شخصية تعتمد على إطلاق متتالي سريع؟,Colt,Brawl Stars,300
أي شخصية تعتبر الأفضل في كشف الأعداء؟,Bo,Brawl Stars,300
أي شخصية تعتمد على الهجوم المستمر بدون توقف؟,Amber,Brawl Stars,300
أي شخصية مناسبة للعب الفردي؟,Leon,Brawl Stars,300
أي شخصية تعتمد على ضربات قوية وبطيئة؟,Frank,Brawl Stars,300
أي شخصية يمكنها تغيير مجرى المباراة بسرعة؟,Tara,Brawl Stars,300
في Gem Grab وفريقك فيه Tank وSniper، أي نوع شخصية تكمل الفريق؟,Support,Brawl Stars,300
في مواجهة ضد Bull قريب منك، شنو أفضل خيار؟,Shelly,Brawl Stars,300
في خريطة مفتوحة بالكامل، أي نوع شخصيات يكون الأفضل؟,Long Range,Brawl Stars,300
إذا فريقك يندفع كثير ويموت، شنو الحل؟,Healer,Brawl Stars,300
في Bounty، هل الأفضل الهجوم أو الحذر؟,حذر,Brawl Stars,300
إذا الخصم كله قريب (Tanks)، شنو تختار؟,Area Damage,Brawl Stars,300
في Showdown، هل القتال دائمًا أفضل خيار؟,لا,Brawl Stars,300
في Brawl Ball، شنو أهم شيء للفوز؟,Teamwork,Brawl Stars,300
في Heist، هل قتل الخصم أهم من ضرب الخزنة؟,لا,Brawl Stars,300
في Hot Zone، الوقوف داخل المنطقة يعطيك شنو؟,سيطرة,Brawl Stars,300
إذا الخصم بعيد ويضربك، شنو الحل الأفضل؟,اختباء,Brawl Stars,300
في قتال قريب ضد Frank، شنو تستغل؟,بطءه,Brawl Stars,300
أي شخصية تعتبر خطر على الشخصيات البعيدة؟,Assassin,Brawl Stars,300
إذا فريقك كله Damage، شنو ناقصه؟,Tank,Brawl Stars,300
في مواجهة ضد Crow، شنو المشكلة الرئيسية؟,Poison,Brawl Stars,300
إذا خريطة مليانة جدران، شنو تختار؟,Thrower,Brawl Stars,300
في Gem Grab، من يحمل الجواهر الأفضل؟,Tank,Brawl Stars,300
في Showdown، البقاء يعتمد أكثر على شنو؟,Positioning,Brawl Stars,300
إذا الخصم يهاجم بسرعة ويهرب، شنو نوعه؟,Assassin,Brawl Stars,300
في Bounty، الموت يعطي الخصم شنو؟,Stars,Brawl Stars,300
إذا فريقك ضعيف في الدفاع، شنو الحل؟,Defensive,Brawl Stars,300
في مواجهة ضد Piper، وين تكون الأفضلية؟,Close Range,Brawl Stars,300
إذا الخصم يستخدم Amber، شنو أخطر شيء فيها؟,Continuous Fire,Brawl Stars,300
في Brawl Ball، الهدف الأساسي شنو؟,Goals,Brawl Stars,300
إذا فريقك بطيء، شنو تحتاج؟,Speed,Brawl Stars,300
في Heist، أي نوع ضرر أفضل؟,High DPS,Brawl Stars,300
إذا الخصم يختفي فجأة، شنو الشخصية؟,Leon,Brawl Stars,300
في Hot Zone، الخروج من المنطقة يؤدي إلى؟,Loss Control,Brawl Stars,300
إذا الخصم يستخدم Barley، وين تقف؟,Open Area,Brawl Stars,300
في مواجهة ضد El Primo، شنو تتجنب؟,Close Combat,Brawl Stars,300
إذا فريقك محتاج ضغط مستمر، شنو تختار؟,Sustained Damage,Brawl Stars,300
في Bounty، قتل لاعب عنده نجوم عالية يعطيك؟,More Stars,Brawl Stars,300
إذا الخصم عنده Healer، شنو الحل؟,Burst Damage,Brawl Stars,300
في Showdown، الدخول في قتال بدون خطة يعتبر؟,Risk,Brawl Stars,300
إذا فريقك فيه 2 Snipers، شنو ناقص؟,Frontline,Brawl Stars,300
في خريطة ضيقة، أي نوع أفضل؟,Close Range,Brawl Stars,300
إذا الخصم متجمع، شنو أفضل هجوم؟,Area Damage,Brawl Stars,300
في Brawl Ball، التمرير مهم لأنه؟,Faster Play,Brawl Stars,300
إذا الخصم يعتمد على السرعة، شنو تواجهه؟,Control,Brawl Stars,300
في Gem Grab، فقدان اللاعب الحامل للجواهر يعني؟,Loss,Brawl Stars,300
إذا فريقك ضعيف في الهجوم، شنو تحتاج؟,Damage Dealer,Brawl Stars,300
في مواجهة ضد Tank، شنو أفضل أسلوب؟,Kiting,Brawl Stars,300
إذا الخصم عنده Range عالي، شنو الحل؟,Close Gap,Brawl Stars,300
في Showdown، جمع الطاقة يعطيك؟,Advantage,Brawl Stars,300
إذا الخصم يعتمد على الاختباء، شنو تستخدم؟,Vision,Brawl Stars,300
في Bounty، اللعب الفردي غالبًا يؤدي إلى؟,Loss,Brawl Stars,300
إذا فريقك متوازن، شنو ميزته؟,Flexibility,Brawl Stars,300
في Heist، تجاهل الخزنة يؤدي إلى؟,Loss,Brawl Stars,300
إذا الخصم يستخدم Thrower، شنو الحل؟,Jump,Brawl Stars,300
في Hot Zone، السيطرة تعتمد على؟,Presence,Brawl Stars,300
في أي سنة صدرت لعبة Brawl Stars عالميًا؟,2018,Brawl Stars,500
ما اسم نظام فتح الشخصيات الحالي في اللعبة؟,Starr Road,Brawl Stars,500
ما اسم الندرة التي كانت مرتبطة بالـ Brawl Pass؟,Chromatic,Brawl Stars,500
كم أقصى Power Level للشخصية؟,11,Brawl Stars,500
كم عدد Star Powers لكل شخصية؟,2,Brawl Stars,500
كم عدد Gadgets لكل شخصية؟,2,Brawl Stars,500
ما اسم الشخصية التي يمكنها التحول إلى ميكا؟,Meg,Brawl Stars,500
ما اسم الشخصية التي تنقسم إلى جزئين؟,R-T,Brawl Stars,500
ما اسم أول شخصية Legendary في اللعبة؟,Spike,Brawl Stars,500
ما اسم الشركة المالكة لـ Supercell؟,Tencent,Brawl Stars,500
ما اسم النظام الذي ألغى الصناديق؟,Box Removal,Brawl Stars,500
كم الحد الأقصى لTrophies للشخصية الواحدة؟,1250,Brawl Stars,500
ما اسم الطور الذي تم حذفه من اللعبة؟,Siege,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الحظ في هجماتها؟,Chester,Brawl Stars,500
ما اسم الشخصية التي تستخدم بطاقات في هجومها؟,Chester,Brawl Stars,500
ما اسم الشخصية التي تسرق نسبة من صحة العدو؟,Colette,Brawl Stars,500
ما اسم الشخصية التي تستخدم قناع وتطلق ظلال؟,Tara,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الهجوم المستمر بالنار؟,Amber,Brawl Stars,500
ما اسم الشخصية التي يمكنها القفز مباشرة نحو العدو؟,El Primo,Brawl Stars,500
ما اسم الشخصية التي تهاجم باستخدام ثلاث طلقات متتالية؟,Colt,Brawl Stars,500
ما اسم الشخصية التي تستدعي برجًا يطلق النار؟,Jessie,Brawl Stars,500
ما اسم الشخصية التي تستدعي دبًا للهجوم؟,Nita,Brawl Stars,500
ما اسم الشخصية التي تطلق قنابل ترتد؟,Rico,Brawl Stars,500
ما اسم الشخصية التي تعتمد على السم المستمر؟,Crow,Brawl Stars,500
ما اسم الشخصية التي تطلق موجة شفاء للفريق؟,Poco,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الضرب البطيء القوي؟,Frank,Brawl Stars,500
ما اسم الشخصية التي تستخدم زجاجات متفجرة؟,Barley,Brawl Stars,500
ما اسم الشخصية التي تطلق صواريخ بعيدة المدى؟,Brock,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الهجوم من مسافة بعيدة جدًا؟,Piper,Brawl Stars,500
ما اسم الشخصية التي تعتمد على سرعة الحركة العالية؟,Max,Brawl Stars,500
ما اسم الشخصية التي يمكنها الاختفاء مؤقتًا؟,Leon,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق موجات صوت؟,Poco,Brawl Stars,500
ما اسم الشخصية التي تستخدم قوس وسهام؟,Bo,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق سريع متعدد؟,Colt,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق متفرق قريب؟,Shelly,Brawl Stars,500
ما اسم الشخصية التي تعتمد على القتال القريب العالي الضرر؟,Bull,Brawl Stars,500
ما اسم الشخصية التي تعتمد على التجميد؟,Lou,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق كهرباء؟,Belle,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طاقة متزايدة؟,Surge,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الطيران أثناء السوبر؟,Janet,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الحفر تحت الأرض؟,Jacky,Brawl Stars,500
ما اسم الشخصية التي تعتمد على التحكم بالعقول؟,Willow,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الهجوم بالقفز السريع؟,Edgar,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق سكاكين؟,Edgar,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق موجات واسعة؟,Emz,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قنابل ديناميت؟,Dynamike,Brawl Stars,500
ما اسم الشخصية التي تعتمد على دعم الفريق ببرج شفاء؟,Pam,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق نباتات دفاعية؟,Rosa,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق حقائب نقود؟,Griff,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق مقلاع يرتد؟,Carl,Brawl Stars,500
ما اسم الشخصية التي يمكنها استدعاء برج شفاء؟,Pam,Brawl Stars,500
ما اسم الشخصية التي تطلق طلقات ترتد بين الأعداء؟,Rico,Brawl Stars,500
ما اسم الشخصية التي تعتمد على ثلاث قنابل متفجرة؟,Dynamike,Brawl Stars,500
ما اسم الشخصية التي تهاجم باستخدام موجات عطرية؟,Emz,Brawl Stars,500
ما اسم الشخصية التي تعتمد على ضربات سريعة بسكاكين؟,Edgar,Brawl Stars,500
ما اسم الشخصية التي تستخدم كرة معدنية مرتدة؟,Carl,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق النار المستمر دون توقف؟,Amber,Brawl Stars,500
ما اسم الشخصية التي يمكنها الطيران أثناء استخدام السوبر؟,Janet,Brawl Stars,500
ما اسم الشخصية التي تتحول إلى روبوت ضخم عند استخدام السوبر؟,Meg,Brawl Stars,500
ما اسم الشخصية التي يمكنها تقسيم نفسها إلى جزئين؟,R-T,Brawl Stars,500
ما اسم الشخصية التي تستخدم قفازات للقتال القريب؟,El Primo,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق صاعقة كهربائية؟,Belle,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طاقة تتطور مع الوقت؟,Surge,Brawl Stars,500
ما اسم الشخصية التي يمكنها التحكم في الأعداء مؤقتًا؟,Willow,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الهجوم عبر النباتات؟,Rosa,Brawl Stars,500
ما اسم الشخصية التي تستخدم سم مستمر يضعف العدو؟,Crow,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قوس وسهام متفجرة؟,Bo,Brawl Stars,500
ما اسم الشخصية التي تستخدم حقيبة نقود كسلاح؟,Griff,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الهجوم القريب باستخدام Shotgun؟,Shelly,Brawl Stars,500
ما اسم الشخصية التي تعتمد على هجوم قريب قوي جدًا؟,Bull,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق ثلاث طلقات مستقيمة؟,Colt,Brawl Stars,500
ما اسم الشخصية التي يمكنها إطلاق موجة شفاء للفريق؟,Poco,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق صواريخ طويلة المدى؟,Brock,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قنابل من خلف الجدران؟,Barley,Brawl Stars,500
ما اسم الشخصية التي تعتمد على ضربات بطيئة قوية جدًا؟,Frank,Brawl Stars,500
ما اسم الشخصية التي تعتمد على الاختفاء المفاجئ؟,Leon,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قنابل متتالية بسرعة؟,Tick,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق رصاص سريع جدًا؟,Colt,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق نيران واسعة المجال؟,Amber,Brawl Stars,500
ما اسم الشخصية التي تعتمد على القفز للوصول إلى العدو؟,Edgar,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قنابل بعيدة المدى؟,Dynamike,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق موجات تبطئ العدو؟,Lou,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طلقات دقيقة بعيدة جدًا؟,Piper,Brawl Stars,500
ما اسم الشخصية التي تعتمد على سرعة حركة عالية جدًا؟,Max,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق برج يهاجم الأعداء؟,Jessie,Brawl Stars,500
ما اسم الشخصية التي تعتمد على استدعاء دب للهجوم؟,Nita,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق سلاسل كهربائية بين الأعداء؟,Belle,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طلقات تنتشر في خط واسع؟,Shelly,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق موجات صوتية تؤثر على عدة أعداء؟,Poco,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق زجاجات تنفجر عند الاصطدام؟,Barley,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قنابل ترتد وتغير اتجاهها؟,Rico,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طاقة تتجمع ثم تنفجر؟,Nani,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق ضربات متتالية في خط مستقيم؟,Colt,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق نيران مستمرة تغطي مساحة؟,Amber,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قفزات سريعة متكررة؟,Edgar,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق قنابل صغيرة متعددة؟,Tick,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طلقات ترتد بين الجدران؟,Rico,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق موجات تبطئ وتجمّد الأعداء؟,Lou,Brawl Stars,500
ما اسم الشخصية التي تعتمد على إطلاق طلقات بعيدة مع ضرر عالي جدًا؟,Piper,Brawl Stars,500


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
file_path = os.path.join(os.getcwd(), "brawl_starts_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
