import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

ما اسم الشركة المطورة للعبة Clash Royale؟,Supercell,Clash Royale,100
في أي سنة صدرت Clash Royale؟,2016,Clash Royale,100
ما اسم العملة الذهبية في اللعبة؟,Gold,Clash Royale,100
ما اسم العملة الخضراء؟,Gems,Clash Royale,100
كم عدد البطاقات في الدك؟,8,Clash Royale,100
ما اسم البرج الرئيسي؟,King Tower,Clash Royale,100
ما اسم الأبراج الجانبية؟,Princess Towers,Clash Royale,100
كم إكسير يبدأ به اللاعب؟,5,Clash Royale,100
ما الحد الأقصى للإكسير؟,10,Clash Royale,100
ما اسم الوحدة التي تطلق سهام؟,Archers,Clash Royale,100
ما اسم الوحدة التي تحمل درع وسيف؟,Knight,Clash Royale,100
ما اسم الوحدة التي تطلق نيران؟,Wizard,Clash Royale,100
ما اسم الوحدة العملاقة البطيئة؟,Giant,Clash Royale,100
ما اسم الوحدة التي تطير وتطلق نار؟,Baby Dragon,Clash Royale,100
ما اسم الوحدة التي تقفز نحو الأبراج؟,Hog Rider,Clash Royale,100
ما اسم البطاقة التي تطلق صاعقة؟,Zap,Clash Royale,100
ما اسم البطاقة التي تسبب ضرر كبير للأبراج؟,Rocket,Clash Royale,100
ما اسم البطاقة التي تعالج الوحدات؟,Heal Spirit,Clash Royale,100
ما اسم البطاقة التي تجمد الأعداء؟,Freeze,Clash Royale,100
ما اسم الوحدة السريعة جدًا؟,Minions,Clash Royale,100
ما اسم الوحدة التي تطلق كرات نارية؟,Fireball,Clash Royale,100
ما اسم الوحدة التي تهاجم من بعيد بدقة؟,Musketeer,Clash Royale,100
ما اسم الوحدة التي تنقسم إلى اثنين عند الموت؟,Skeletons,Clash Royale,100
ما اسم الوحدة التي تحمل مدفع؟,Cannon,Clash Royale,100
ما اسم البطاقة التي تستدعي جيش من الهياكل؟,Skeleton Army,Clash Royale,100
ما اسم الوحدة التي تطلق من الهواء؟,Minion Horde,Clash Royale,100
ما اسم البطاقة التي تدفع الأعداء للخلف؟,Log,Clash Royale,100
ما اسم الوحدة التي تهاجم جماعيًا؟,Barbarians,Clash Royale,100
ما اسم البطاقة التي تخلق إعصار؟,Tornado,Clash Royale,100
ما اسم الوحدة التي تتحرك تحت الأرض؟,Miner,Clash Royale,100
ما اسم البطاقة التي تطلق كرة نار صغيرة؟,Fire Spirits,Clash Royale,100
ما اسم الوحدة التي تحمل قنبلة؟,Bomber,Clash Royale,100
ما اسم البطاقة التي تستدعي فارس مظلم؟,Dark Prince,Clash Royale,100
ما اسم البطاقة التي تستدعي ساحرة؟,Witch,Clash Royale,100
ما اسم البطاقة التي تستدعي تنين كهربائي؟,Electro Dragon,Clash Royale,100
ما اسم البطاقة التي تستدعي تنين نار؟,Inferno Dragon,Clash Royale,100
ما اسم البطاقة التي تهاجم الأبراج فقط؟,Hog Rider,Clash Royale,100
ما اسم البطاقة التي تهاجم من بعيد جدًا؟,Princess,Clash Royale,100
ما اسم البطاقة التي تطلق سهم جماعي؟,Arrows,Clash Royale,100
ما اسم البطاقة التي تسرع الوحدات؟,Rage,Clash Royale,100
ما اسم البطاقة التي تخلق نسخ من الوحدات؟,Clone,Clash Royale,100
ما اسم البطاقة التي تدمر الوحدات الصغيرة؟,Zap,Clash Royale,100
ما اسم البطاقة التي تعيد توزيع الوحدات؟,Tornado,Clash Royale,100
ما اسم البطاقة التي تضرب البرج مباشرة؟,Rocket,Clash Royale,100
ما اسم البطاقة التي تستدعي برج دفاعي؟,Cannon,Clash Royale,100
ما اسم البطاقة التي تستدعي مبنى دفاعي؟,Tesla,Clash Royale,100
ما اسم البطاقة التي تطلق كهرباء؟,Electro Wizard,Clash Royale,100
ما اسم البطاقة التي تعتمد على السم؟,Poison,Clash Royale,100
ما اسم البطاقة التي تهاجم بسرعة عالية؟,Goblin Gang,Clash Royale,100
ما اسم البطاقة التي تعتمد على الطيران؟,Minions,Clash Royale,100
ما اسم الوحدة التي تحمل رمح؟,Spear Goblins,Clash Royale,100
ما اسم الوحدة التي ترمي قنابل من بعيد؟,Bomber,Clash Royale,100
ما اسم الوحدة التي تطير في مجموعة صغيرة؟,Minions,Clash Royale,100
ما اسم الوحدة التي تطير في مجموعة كبيرة؟,Minion Horde,Clash Royale,100
ما اسم الوحدة التي تهاجم بسرعة بسكين؟,Goblins,Clash Royale,100
ما اسم البطاقة التي تستدعي ثلاثة جنود؟,Barbarians,Clash Royale,100
ما اسم البطاقة التي تستدعي هيكل عظمي واحد قوي؟,Skeleton King,Clash Royale,100
ما اسم البطاقة التي تطلق نار على منطقة؟,Fireball,Clash Royale,100
ما اسم البطاقة التي تسبب ضرر بمرور الوقت؟,Poison,Clash Royale,100
ما اسم البطاقة التي تضرب بالكهرباء؟,Zap,Clash Royale,100
ما اسم البطاقة التي تطلق سهم جماعي؟,Arrows,Clash Royale,100
ما اسم البطاقة التي تدفع الوحدات للأمام؟,Log,Clash Royale,100
ما اسم البطاقة التي تبني برج يطلق نار؟,Inferno Tower,Clash Royale,100
ما اسم البطاقة التي تبني مدفع أرضي؟,Cannon,Clash Royale,100
ما اسم البطاقة التي تبني برج كهرباء؟,Tesla,Clash Royale,100
ما اسم الوحدة التي تهاجم الأبراج فقط بسرعة؟,Hog Rider,Clash Royale,100
ما اسم الوحدة التي تستدعي هيكل عظمي صغير؟,Skeletons,Clash Royale,100
ما اسم البطاقة التي تستدعي مجموعة هياكل؟,Skeleton Army,Clash Royale,100
ما اسم البطاقة التي تنسخ الوحدات؟,Clone,Clash Royale,100
ما اسم البطاقة التي تسرع الوحدات؟,Rage,Clash Royale,100
ما اسم البطاقة التي تجمد كل شيء؟,Freeze,Clash Royale,100
ما اسم البطاقة التي تطلق صاعقة قوية؟,Lightning,Clash Royale,100
ما اسم الوحدة التي تطير وتضرب بالكهرباء؟,Electro Dragon,Clash Royale,100
ما اسم الوحدة التي تطلق قذائف من بعيد؟,Mortar,Clash Royale,100
ما اسم الوحدة التي تطلق نار مستمرة؟,Inferno Dragon,Clash Royale,100
ما اسم الوحدة التي تهاجم من مسافة بعيدة جدًا؟,Princess,Clash Royale,100
ما اسم الوحدة التي تقفز فوق النهر؟,Bandit,Clash Royale,100
ما اسم الوحدة التي تحمل فأس؟,Executioner,Clash Royale,100
ما اسم الوحدة التي تهاجم من الجو بنار؟,Baby Dragon,Clash Royale,100
ما اسم الوحدة التي تطلق سهمين معًا؟,Archers,Clash Royale,100
ما اسم الوحدة التي تستخدم قوس طويل؟,Princess,Clash Royale,100
ما اسم البطاقة التي تخلق إعصار؟,Tornado,Clash Royale,100
ما اسم البطاقة التي تستدعي برميل من السماء؟,Goblin Barrel,Clash Royale,100
ما اسم البطاقة التي تستدعي عملاق يحمل قنبلة؟,Giant Skeleton,Clash Royale,100
ما اسم البطاقة التي تطلق أرواح نار؟,Fire Spirits,Clash Royale,100
ما اسم البطاقة التي تطلق أرواح كهرباء؟,Electro Spirit,Clash Royale,100
ما اسم البطاقة التي تطلق أرواح جليد؟,Ice Spirit,Clash Royale,100
ما اسم الوحدة التي تتحرك بسرعة عالية جدًا؟,Bandit,Clash Royale,100
ما اسم الوحدة التي تعتمد على السم؟,Poison,Clash Royale,100
ما اسم البطاقة التي تستدعي مجموعة Goblins؟,Goblin Gang,Clash Royale,100
ما اسم البطاقة التي تبني فرن؟,Furnace,Clash Royale,100
ما اسم البطاقة التي تستدعي تنينين؟,Skeleton Dragons,Clash Royale,100
ما اسم البطاقة التي تستدعي ساحرتين؟,Witch,Clash Royale,100
ما اسم البطاقة التي تستدعي برج يطلق قنابل؟,Bomb Tower,Clash Royale,100
ما اسم البطاقة التي تطلق موجة جليدية؟,Ice Wizard,Clash Royale,100
ما اسم البطاقة التي تطلق سهم كهربائي؟,Electro Wizard,Clash Royale,100
ما اسم البطاقة التي تطلق نار قوية على هدف واحد؟,Inferno Tower,Clash Royale,100
ما اسم البطاقة التي تطلق قنابل كبيرة؟,Rocket,Clash Royale,100
ما اسم البطاقة التي تهاجم مجموعة كبيرة؟,Arrows,Clash Royale,100
ما اسم البطاقة التي تعتمد على الضرر الجماعي؟,Fireball,Clash Royale,100
إذا عندك Hog Rider والخصم عنده Cannon، شنو الحل الأفضل؟,Spell,Clash Royale,300
في مواجهة ضد Minion Horde، شنو تستخدم مباشرة؟,Arrows,Clash Royale,300
إذا الخصم يستخدم Skeleton Army، شنو أفضل رد سريع؟,Zap,Clash Royale,300
في مواجهة ضد Inferno Tower، شنو يوقفه؟,Zap,Clash Royale,300
إذا الخصم عنده Princess بعيدة، شنو الحل؟,Spell,Clash Royale,300
في مواجهة ضد Giant، شنو أفضل دفاع؟,Inferno Tower,Clash Royale,300
إذا الخصم يلعب Goblin Barrel، شنو أفضل رد؟,Log,Clash Royale,300
في مواجهة ضد Baby Dragon، شنو نوع الهجوم الأفضل؟,Air Defense,Clash Royale,300
إذا الخصم يستخدم Freeze، شنو المشكلة الأساسية؟,Immobilization,Clash Royale,300
في Heist، شنو الأفضل؟ ضرب الخزنة أو قتل العدو؟,Tower Damage,Clash Royale,300
إذا الخصم عنده Wizard، شنو أفضل مواجهته؟,Single Target,Clash Royale,300
في مواجهة ضد Pekka، شنو تستخدم لتشتيته؟,Swarm,Clash Royale,300
إذا الخصم يستخدم Balloon، شنو أفضل رد؟,Air Defense,Clash Royale,300
في مواجهة ضد Skeleton Army، شنو نوع الهجوم الأفضل؟,Splash,Clash Royale,300
إذا الخصم يلعب Miner، وين يظهر غالبًا؟,Back Tower,Clash Royale,300
في مواجهة ضد Bandit، شنو لازم تتجنب؟,Line Dash,Clash Royale,300
إذا الخصم يلعب Rage، شنو يزيد؟,Speed,Clash Royale,300
في مواجهة ضد Executioner، شنو تتجنب؟,Line Position,Clash Royale,300
إذا الخصم عنده Tornado، شنو ممكن يسوي؟,Pull Units,Clash Royale,300
في مواجهة ضد Electro Wizard، شنو تأثيره؟,Reset,Clash Royale,300
إذا الخصم يلعب Clone، شنو أفضل رد؟,Splash,Clash Royale,300
في مواجهة ضد Mortar، شنو الهدف؟,Destroy Building,Clash Royale,300
إذا الخصم يلعب Furnace، شنو تنتج؟,Fire Spirits,Clash Royale,300
في مواجهة ضد Goblin Barrel، شنو مكانه؟,Tower,Clash Royale,300
إذا الخصم يستخدم Lightning، شنو يستهدف؟,3 Targets,Clash Royale,300
في مواجهة ضد Tesla، متى يظهر؟,When Active,Clash Royale,300
إذا الخصم يلعب Poison، شنو تأثيره؟,Damage Over Time,Clash Royale,300
في مواجهة ضد X-Bow، شنو الهدف؟,Destroy Fast,Clash Royale,300
إذا الخصم يلعب Skeletons، شنو أفضل رد؟,Splash,Clash Royale,300
في مواجهة ضد Valkyrie، شنو نوعها؟,Splash Damage,Clash Royale,300
إذا الخصم يلعب Log، شنو يسوي؟,Push Back,Clash Royale,300
في مواجهة ضد Inferno Dragon، شنو يسوي؟,Ramp Damage,Clash Royale,300
إذا الخصم يلعب Rocket، شنو يستهدف؟,High Value,Clash Royale,300
في مواجهة ضد Mini Pekka، شنو قوته؟,High Damage,Clash Royale,300
إذا الخصم يلعب Heal Spirit، شنو يسوي؟,Heal Units,Clash Royale,300
في مواجهة ضد Skeleton King، شنو يسوي؟,Spawn Skeletons,Clash Royale,300
إذا الخصم يلعب Electro Spirit، شنو يسوي؟,Chain Damage,Clash Royale,300
في مواجهة ضد Ice Spirit، شنو يسوي؟,Freeze,Clash Royale,300
إذا الخصم يلعب Fire Spirits، شنو يسوي؟,Explode,Clash Royale,300
في مواجهة ضد Goblin Gang، شنو نوعه؟,Swarm,Clash Royale,300
إذا الخصم يلعب Cannon، شنو نوعه؟,Building,Clash Royale,300
في مواجهة ضد Bomb Tower، شنو يسوي؟,Splash Damage,Clash Royale,300
إذا الخصم يلعب Barbarian Barrel، شنو يسوي؟,Roll Damage,Clash Royale,300
في مواجهة ضد Royal Giant، شنو يستهدف؟,Buildings,Clash Royale,300
إذا الخصم يلعب Lava Hound، شنو نوعه؟,Tank Air,Clash Royale,300
في مواجهة ضد Night Witch، شنو تستدعي؟,Bats,Clash Royale,300
إذا الخصم يلعب Bats، شنو نوعهم؟,Air Swarm,Clash Royale,300
في مواجهة ضد Goblins، شنو نوعهم؟,Ground Swarm,Clash Royale,300
إذا الخصم يلعب Archers، شنو ميزتهم؟,Range,Clash Royale,300
في مواجهة ضد Knight، شنو نوعه؟,Tank,Clash Royale,300
إذا الخصم لعب Inferno Dragon على Giant، شنو يوقفه مباشرة؟,Reset,Clash Royale,300
في مواجهة ضد Balloon، وين يستهدف؟,Buildings,Clash Royale,300
إذا الخصم يلعب Hog Rider، شنو يقدر يوقفه؟,Building,Clash Royale,300
في مواجهة ضد Pekka، شنو أفضل طريقة لتأخيره؟,Kite,Clash Royale,300
إذا الخصم يلعب X-Bow، شنو نوعه؟,Siege,Clash Royale,300
في مواجهة ضد Lava Hound، شنو يجي بعد موته؟,Pups,Clash Royale,300
إذا الخصم يلعب Miner، شنو نوعه؟,Chip Damage,Clash Royale,300
في مواجهة ضد Skeleton Army، شنو أقوى Counter؟,Splash Damage,Clash Royale,300
إذا الخصم يلعب Wizard، شنو نوعه؟,Splash Damage,Clash Royale,300
في مواجهة ضد Electro Dragon، شنو تأثيره؟,Chain Lightning,Clash Royale,300
إذا الخصم يلعب Freeze، شنو يوقف؟,Movement,Clash Royale,300
في مواجهة ضد Rage، شنو يزيد؟,Attack Speed,Clash Royale,300
إذا الخصم يلعب Clone، شنو ضعف النسخ؟,Low HP,Clash Royale,300
في مواجهة ضد Tornado، شنو يسوي؟,Pull Units,Clash Royale,300
إذا الخصم يلعب Lightning، كم هدف يضرب؟,3,Clash Royale,300
في مواجهة ضد Rocket، شنو نوعه؟,High Damage Spell,Clash Royale,300
إذا الخصم يلعب Fireball، شنو نوعه؟,Medium Spell,Clash Royale,300
في مواجهة ضد Zap، شنو تأثيره الأساسي؟,Reset,Clash Royale,300
إذا الخصم يلعب Log، شنو يسوي؟,Knockback,Clash Royale,300
في مواجهة ضد Poison، شنو تأثيره؟,Area Damage,Clash Royale,300
إذا الخصم يلعب Bandit، شنو قدرتها؟,Dash,Clash Royale,300
في مواجهة ضد Royal Ghost، شنو ميزته؟,Invisible,Clash Royale,300
إذا الخصم يلعب Mega Knight، شنو يسوي عند النزول؟,Area Damage,Clash Royale,300
في مواجهة ضد Sparky، شنو يوقفها؟,Reset,Clash Royale,300
إذا الخصم يلعب Electro Wizard، شنو يسوي؟,Reset,Clash Royale,300
في مواجهة ضد Inferno Tower، شنو نوع ضرره؟,Increasing Damage,Clash Royale,300
إذا الخصم يلعب Tesla، وين يختفي؟,Underground,Clash Royale,300
في مواجهة ضد Cannon Cart، شنو يصير لما ينكسر؟,Becomes Unit,Clash Royale,300
إذا الخصم يلعب Goblin Barrel، شنو نوعه؟,Chip Damage,Clash Royale,300
في مواجهة ضد Skeleton Barrel، شنو ينزل بعده؟,Skeletons,Clash Royale,300
إذا الخصم يلعب Battle Ram، شنو يطلع بعده؟,Barbarians,Clash Royale,300
في مواجهة ضد Ram Rider، شنو تسوي؟,Slow Enemy,Clash Royale,300
إذا الخصم يلعب Electro Giant، شنو ميزته؟,Reflect Damage,Clash Royale,300
في مواجهة ضد Ice Golem، شنو يسوي عند الموت؟,Slow,Clash Royale,300
إذا الخصم يلعب Golem، شنو يطلع بعده؟,Golemites,Clash Royale,300
في مواجهة ضد Elixir Golem، شنو يعطي الخصم؟,Elixir,Clash Royale,300
إذا الخصم يلعب Three Musketeers، كم عددهم؟,3,Clash Royale,300
في مواجهة ضد Royal Hogs، كم عددهم؟,4,Clash Royale,300
إذا الخصم يلعب Minions، كم عددهم؟,3,Clash Royale,300
في مواجهة ضد Minion Horde، كم عددهم؟,6,Clash Royale,300
إذا الخصم يلعب Skeletons، كم عددهم؟,3,Clash Royale,300
في مواجهة ضد Goblin Gang، كم عددهم؟,5,Clash Royale,300
إذا الخصم يلعب Barbarians، كم عددهم؟,5,Clash Royale,300
في مواجهة ضد Elite Barbarians، كم عددهم؟,2,Clash Royale,300
إذا الخصم يلعب Archers، كم عددهم؟,2,Clash Royale,300
في مواجهة ضد Fire Spirits، كم عددهم؟,3,Clash Royale,300
إذا الخصم يلعب Electro Spirit، كم عددهم؟,1,Clash Royale,300
في مواجهة ضد Ice Spirit، كم عددهم؟,1,Clash Royale,300
إذا الخصم يلعب Skeleton Dragons، كم عددهم؟,2,Clash Royale,300
كم أقصى Elixir يمكن تخزينه؟,10,Clash Royale,500
كم عدد البطاقات في الدك؟,8,Clash Royale,500
كم عدد الأبراج في بداية المباراة؟,3,Clash Royale,500
كم مدة المباراة الأساسية بالدقائق؟,3,Clash Royale,500
كم مدة الـ Overtime؟,2,Clash Royale,500
كم عدد Princess Towers؟,2,Clash Royale,500
كم Elixir يكلف Hog Rider؟,4,Clash Royale,500
كم Elixir يكلف Pekka؟,7,Clash Royale,500
كم Elixir يكلف Golem؟,8,Clash Royale,500
كم Elixir يكلف Rocket؟,6,Clash Royale,500
كم Elixir يكلف Lightning؟,6,Clash Royale,500
كم Elixir يكلف Fireball؟,4,Clash Royale,500
كم Elixir يكلف Zap؟,2,Clash Royale,500
كم Elixir يكلف Log؟,2,Clash Royale,500
كم Elixir يكلف Freeze؟,4,Clash Royale,500
كم Elixir يكلف Clone؟,3,Clash Royale,500
كم Elixir يكلف Tornado؟,3,Clash Royale,500
كم Elixir يكلف Poison؟,4,Clash Royale,500
كم Elixir يكلف Miner؟,3,Clash Royale,500
كم Elixir يكلف Balloon؟,5,Clash Royale,500
كم Elixir يكلف Inferno Tower؟,5,Clash Royale,500
كم Elixir يكلف Tesla؟,4,Clash Royale,500
كم Elixir يكلف Cannon؟,3,Clash Royale,500
كم Elixir يكلف X-Bow؟,6,Clash Royale,500
كم Elixir يكلف Mortar؟,4,Clash Royale,500
كم Elixir يكلف Goblin Barrel؟,3,Clash Royale,500
كم Elixir يكلف Skeleton Army؟,3,Clash Royale,500
كم Elixir يكلف Minion Horde؟,5,Clash Royale,500
كم Elixir يكلف Barbarians؟,5,Clash Royale,500
كم Elixir يكلف Elite Barbarians؟,6,Clash Royale,500
كم Elixir يكلف Archers؟,3,Clash Royale,500
كم Elixir يكلف Knight؟,3,Clash Royale,500
كم Elixir يكلف Valkyrie؟,4,Clash Royale,500
كم Elixir يكلف Mini Pekka؟,4,Clash Royale,500
كم Elixir يكلف Wizard؟,5,Clash Royale,500
كم Elixir يكلف Executioner؟,5,Clash Royale,500
كم Elixir يكلف Electro Wizard؟,4,Clash Royale,500
كم Elixir يكلف Baby Dragon؟,4,Clash Royale,500
كم Elixir يكلف Inferno Dragon؟,4,Clash Royale,500
كم Elixir يكلف Mega Knight؟,7,Clash Royale,500
كم Elixir يكلف Sparky؟,6,Clash Royale,500
كم Elixir يكلف Bandit؟,3,Clash Royale,500
كم Elixir يكلف Royal Ghost؟,3,Clash Royale,500
كم Elixir يكلف Ram Rider؟,5,Clash Royale,500
كم Elixir يكلف Battle Ram؟,4,Clash Royale,500
كم Elixir يكلف Giant؟,5,Clash Royale,500
كم Elixir يكلف Royal Giant؟,6,Clash Royale,500
كم Elixir يكلف Lava Hound؟,7,Clash Royale,500
كم Elixir يكلف Electro Giant؟,7,Clash Royale,500
كم Elixir يكلف Elixir Golem؟,3,Clash Royale,500
أي بطاقة تعيد شحن Sparky مباشرة؟,Zap,Clash Royale,500
أي بطاقة تعيد شحن Inferno Dragon؟,Electro Wizard,Clash Royale,500
أي بطاقة تعيد شحن Inferno Tower؟,Electro Spirit,Clash Royale,500
أي بطاقة يمكنها إيقاف Prince أثناء الشحن؟,Ice Spirit,Clash Royale,500
أي بطاقة يمكنها إيقاف Battle Ram قبل الاصطدام؟,Log,Clash Royale,500
أي بطاقة تكشف Miner بدون Spell؟,Skeletons,Clash Royale,500
أي بطاقة يمكنها ضرب الهواء والأرض معًا؟,Musketeer,Clash Royale,500
أي بطاقة لا يمكنها ضرب الوحدات الجوية؟,Knight,Clash Royale,500
أي بطاقة تطلق ضرر يتزايد مع الوقت؟,Inferno Dragon,Clash Royale,500
أي بطاقة تسبب ضررًا جماعيًا دائريًا عند الموت؟,Ice Golem,Clash Royale,500
أي بطاقة تطلق هجوم خطي يخترق الأعداء؟,Executioner,Clash Royale,500
أي بطاقة يمكنها جذب جميع الوحدات لنقطة واحدة؟,Tornado,Clash Royale,500
أي بطاقة تستهدف الأبراج فقط من الجو؟,Balloon,Clash Royale,500
أي بطاقة تستهدف الأبراج فقط من الأرض؟,Hog Rider,Clash Royale,500
أي بطاقة تعطي Elixir للخصم عند تدميرها؟,Elixir Golem,Clash Royale,500
أي بطاقة تنقسم إلى وحدتين بعد الموت؟,Golem,Clash Royale,500
أي بطاقة تنتج وحدات صغيرة بعد الموت؟,Lava Hound,Clash Royale,500
أي بطاقة يمكنها الاختفاء مؤقتًا؟,Royal Ghost,Clash Royale,500
أي بطاقة تعتمد على الاندفاع Dash؟,Bandit,Clash Royale,500
أي بطاقة تهاجم بسلسلة كهربائية بين الأعداء؟,Electro Dragon,Clash Royale,500
أي بطاقة تطلق ثلاث طلقات متتالية؟,Hunter,Clash Royale,500
أي بطاقة تعتمد على الهجوم القريب مع ضرر انفجاري؟,Bomber,Clash Royale,500
أي بطاقة تطلق ضررًا مستمرًا على منطقة؟,Poison,Clash Royale,500
أي بطاقة توقف الهجوم مؤقتًا بالتجميد؟,Freeze,Clash Royale,500
أي بطاقة تدفع الوحدات للخلف؟,Log,Clash Royale,500
أي بطاقة تسبب Knockback من الجو؟,Fireball,Clash Royale,500
أي بطاقة تعتمد على الضرر المباشر العالي للأبراج؟,Rocket,Clash Royale,500
أي بطاقة يمكنها سحب الوحدات وتغيير مسارها؟,Tornado,Clash Royale,500
أي بطاقة تعتمد على الهجوم المتزايد ضد نفس الهدف؟,Inferno Tower,Clash Royale,500
أي بطاقة يمكنها ضرب هدفين عند النزول؟,Electro Wizard,Clash Royale,500
أي بطاقة تعتمد على Spawn Damage عند النزول؟,Mega Knight,Clash Royale,500
أي بطاقة تهاجم من تحت الأرض مباشرة؟,Miner,Clash Royale,500
أي بطاقة تعتمد على رمي البراميل من السماء؟,Goblin Barrel,Clash Royale,500
أي بطاقة تتحول من مبنى إلى وحدة؟,Cannon Cart,Clash Royale,500
أي بطاقة تهاجم بخط مستقيم طويل جدًا؟,Magic Archer,Clash Royale,500
أي بطاقة تعتمد على الهجوم الدائري حولها؟,Valkyrie,Clash Royale,500
أي بطاقة تستدعي وحدات باستمرار؟,Furnace,Clash Royale,500
أي بطاقة تهاجم فقط الأهداف الأرضية؟,Mini Pekka,Clash Royale,500
أي بطاقة تهاجم فقط الأهداف الجوية؟,Minions,Clash Royale,500
أي بطاقة تعتمد على الضرر المتفجر عند الوصول؟,Balloon,Clash Royale,500
أي بطاقة تعتمد على استهداف المباني فقط؟,Royal Giant,Clash Royale,500
أي بطاقة تعتمد على إصابة متعددة للأعداء بخط؟,Executioner,Clash Royale,500
أي بطاقة تطلق ضررًا سريعًا ثم تختفي؟,Fire Spirits,Clash Royale,500
أي بطاقة تطلق ضررًا متسلسلًا بين الأعداء؟,Electro Spirit,Clash Royale,500
أي بطاقة يمكنها تجميد هدف واحد لفترة قصيرة؟,Ice Spirit,Clash Royale,500
أي بطاقة تعتمد على عدد كبير من الوحدات الصغيرة؟,Skeleton Army,Clash Royale,500
أي بطاقة تعتمد على الضرر العالي لهدف واحد؟,Mini Pekka,Clash Royale,500
أي بطاقة تعتمد على القفز للوصول للعدو؟,Mega Knight,Clash Royale,500
أي بطاقة تعتمد على إطلاق مستمر بعيد المدى؟,X-Bow,Clash Royale,500

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
file_path = os.path.join(os.getcwd(), "class_royal_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
