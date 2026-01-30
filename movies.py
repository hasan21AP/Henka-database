

import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """

ما اسم المدرسة السحرية التي درس فيها هاري بوتر؟,Hogwarts,أفلام,100
من هو العدو الرئيسي لهاري بوتر؟,Voldemort,أفلام,100
ما اسم صديق هاري المقرب ذو الشعر الأحمر؟,Ron Weasley,أفلام,100
ما اسم صديقة هاري الذكية؟,Hermione Granger,أفلام,100
ما اسم لعبة الطيران الشهيرة في هاري بوتر؟,Quidditch,أفلام,100
ما اسم العصا السحرية الخاصة بهاري؟,Holly Wand,أفلام,100
ما اسم منصة القطار السحرية؟,Platform 9¾,أفلام,100
من هو مدير مدرسة Hogwarts؟,Albus Dumbledore,أفلام,100
ما اسم منزل هاري في Hogwarts؟,Gryffindor,أفلام,100
ما اسم البنك السحري في عالم هاري بوتر؟,Gringotts,أفلام,100

من هو البطل الرئيسي في سلسلة Iron Man؟,Tony Stark,أفلام,100
ما اسم الفريق الخارق في أفلام مارفل؟,Avengers,أفلام,100
من هو بطل فيلم Captain America؟,Steve Rogers,أفلام,100
ما اسم مطرقة ثور؟,Mjolnir,أفلام,100
من هو بطل فيلم Spider-Man؟,Peter Parker,أفلام,100
ما اسم الشرير الذي جمع الأحجار في Avengers؟,Thanos,أفلام,100
ما اسم عالم السحرة الذي ينتمي إليه Doctor Strange؟,Sorcerer Supreme,أفلام,100
ما اسم أخت تشالا في Black Panther؟,Shuri,أفلام,100
ما اسم معدن درع Black Panther؟,Vibranium,أفلام,100
ما اسم مدينة Black Panther؟,Wakanda,أفلام,100

من هو بطل أفلام DC الذي يعيش في Gotham؟,Batman,أفلام,100
ما اسم البطل الذي يأتي من كوكب Krypton؟,Superman,أفلام,100
ما اسم البطلة الأمازونية في DC؟,Wonder Woman,أفلام,100
ما اسم فريق الأبطال في DC؟,Justice League,أفلام,100
ما اسم عدو باتمان الشهير ذو الضحكة؟,Joker,أفلام,100
ما اسم مدينة سوبرمان؟,Metropolis,أفلام,100
ما اسم البطل السريع جدًا في DC؟,The Flash,أفلام,100
ما اسم ملك أطلانتس في DC؟,Aquaman,أفلام,100
ما اسم العدو الذي ظهر في Justice League؟,Steppenwolf,أفلام,100
ما اسم البطلة التي تتحكم في السحر في DC؟,Zatanna,أفلام,100

ما اسم الفيلم الذي يحكي قصة سفينة تغرق شهيرة؟,Titanic,أفلام,100
من هو بطل فيلم Titanic؟,Jack Dawson,أفلام,100
ما اسم البطلة في Titanic؟,Rose DeWitt Bukater,أفلام,100
ما اسم فيلم الديناصورات الشهير؟,Jurassic Park,أفلام,100
ما اسم فيلم الأسد الملك؟,The Lion King,أفلام,100
ما اسم فيلم الرسوم الذي يحكي عن لعبة حية؟,Toy Story,أفلام,100
ما اسم الفيلم الذي يدور في عالم الأحلام؟,Inception,أفلام,100
من هو مخرج فيلم Inception؟,Christopher Nolan,أفلام,100
ما اسم الفيلم الذي يحكي عن مافيا إيطالية شهيرة؟,The Godfather,أفلام,100
من هو بطل فيلم The Godfather؟,Michael Corleone,أفلام,100

ما اسم الفيلم الذي يتحدث عن خاتم قوي جدًا؟,The Lord of the Rings,أفلام,100
من هو حامل الخاتم الرئيسي؟,Frodo Baggins,أفلام,100
ما اسم الساحر الرمادي؟,Gandalf,أفلام,100
ما اسم فيلم الفضاء الشهير الذي فيه Darth Vader؟,Star Wars,أفلام,100
من هو والد Luke Skywalker؟,Darth Vader,أفلام,100
ما اسم فيلم الملاكمة الشهير؟,Rocky,أفلام,100
من هو بطل Rocky؟,Rocky Balboa,أفلام,100
ما اسم الفيلم الذي يحكي عن سجين بريء وهروبه؟,The Shawshank Redemption,أفلام,100
من هو بطل فيلم Forrest Gump؟,Forrest Gump,أفلام,100
ما اسم الفيلم الذي يحكي عن مهرج مرعب؟,It,أفلام,100

ما اسم الفيلم الذي تدور أحداثه في مدرسة سحرية غير Hogwarts؟,Fantastic Beasts,أفلام,100
من هو البروفيسور الذي يعلّم الجرع في هاري بوتر؟,Severus Snape,أفلام,100
ما اسم مباراة هاري الأولى في Quidditch؟,Seeker Match,أفلام,100
ما اسم مخلوق هاري الأليف؟,Hedwig,أفلام,100
ما اسم كرة السحر الذهبية في Quidditch؟,Golden Snitch,أفلام,100
ما اسم البطولة في Harry Potter 4؟,Triwizard Tournament,أفلام,100
ما اسم المدرسة المنافسة لـ Hogwarts؟,Durmstrang,أفلام,100
ما اسم مدرسة السحر الفرنسية؟,Beauxbatons,أفلام,100
ما اسم منزل Draco Malfoy؟,Slytherin,أفلام,100
من هو والد Draco Malfoy؟,Lucius Malfoy,أفلام,100

من هو بطل فيلم Doctor Strange؟,Stephen Strange,أفلام,100
ما اسم الشريرة في فيلم WandaVision؟,Agatha Harkness,أفلام,100
ما اسم أخت Natasha Romanoff؟,Yelena Belova,أفلام,100
ما اسم بطل Ant-Man؟,Scott Lang,أفلام,100
ما اسم شخصية Groot الشهيرة؟,Groot,أفلام,100
ما اسم صديق Rocket في Guardians؟,Star-Lord,أفلام,100
ما اسم الشرير في فيلم Loki؟,Kang,أفلام,100
ما اسم حجر الزمن في Infinity Stones؟,Time Stone,أفلام,100
كم عدد Infinity Stones؟,Six,أفلام,100
ما اسم فيلم النهاية ضد Thanos؟,Avengers Endgame,أفلام,100

ما اسم فيلم Batman الذي أخرجه Christopher Nolan؟,The Dark Knight,أفلام,100
من هو الممثل الذي لعب Joker في The Dark Knight؟,Heath Ledger,أفلام,100
ما اسم العدو الذي واجهه Batman في The Dark Knight Rises؟,Bane,أفلام,100
من هي البطلة في فيلم Aquaman؟,Mera,أفلام,100
ما اسم فيلم Superman ضد Batman؟,Batman v Superman,أفلام,100
من هو الشرير في فيلم Man of Steel؟,General Zod,أفلام,100
ما اسم الفيلم الذي فيه Harley Quinn؟,Suicide Squad,أفلام,100
ما اسم البطلة الرئيسية في Birds of Prey؟,Harley Quinn,أفلام,100
من هو العدو البحري لـ Aquaman؟,Black Manta,أفلام,100
ما اسم فيلم Joker الشهير 2019؟,Joker,أفلام,100

ما اسم الفيلم الذي يتحدث عن حلم داخل حلم؟,Inception,أفلام,100
ما اسم بطل Inception؟,Dom Cobb,أفلام,100
ما اسم فيلم الفضاء الذي فيه ثقب أسود؟,Interstellar,أفلام,100
من هو بطل Interstellar؟,Cooper,أفلام,100
ما اسم فيلم يحكي عن مصفوفة وهمية؟,The Matrix,أفلام,100
من هو بطل The Matrix؟,Neo,أفلام,100
ما اسم الفيلم الذي فيه شخصية John Wick؟,John Wick,أفلام,100
من هو الممثل الذي لعب John Wick؟,Keanu Reeves,أفلام,100
ما اسم فيلم القتال في نادي سري؟,Fight Club,أفلام,100
من هو بطل Fight Club؟,Tyler Durden,أفلام,100

ما اسم الفيلم الذي يحكي عن مهرج قاتل في Gotham؟,Joker,أفلام,100
ما اسم الفيلم الذي يحكي عن قاتل متسلسل عبقري؟,Se7en,أفلام,100
ما اسم الفيلم الذي يحكي عن لعبة مميتة؟,Saw,أفلام,100
ما اسم الفيلم الذي يحكي عن وحش فضائي؟,Alien,أفلام,100
ما اسم الفيلم الذي يحكي عن روبوت قاتل من المستقبل؟,Terminator,أفلام,100
من هو بطل Terminator؟,T-800,أفلام,100
ما اسم فيلم السباقات الشهير؟,Fast and Furious,أفلام,100
من هو بطل Fast and Furious الأساسي؟,Dominic Toretto,أفلام,100
ما اسم فيلم القراصنة الشهير؟,Pirates of the Caribbean,أفلام,100
من هو قائد القراصنة الشهير؟,Jack Sparrow,أفلام,100

ما اسم فيلم الرسوم الذي يحكي عن مشاعر داخل العقل؟,Inside Out,أفلام,100
ما اسم فيلم الثلج الشهير من ديزني؟,Frozen,أفلام,100
ما اسم أخت Elsa؟,Anna,أفلام,100
ما اسم فيلم يحكي عن سمكة تبحث عن ابنها؟,Finding Nemo,أفلام,100
ما اسم والد Nemo؟,Marlin,أفلام,100
ما اسم فيلم يحكي عن روبوت صغير في الفضاء؟,WALL-E,أفلام,100
ما اسم فيلم يحكي عن وحش لطيف في الجامعة؟,Monsters University,أفلام,100
ما اسم فيلم يحكي عن بطل خارق من عائلة؟,The Incredibles,أفلام,100
ما اسم فيلم يحكي عن شاب عنكبوت في عالم متعدد؟,Spider-Man Into the Spider-Verse,أفلام,100
ما اسم بطل Spider-Verse الرئيسي؟,Miles Morales,أفلام,100

ما اسم الفيلم الذي ظهر فيه أول مرة Thanos بشكل واضح؟,Avengers Infinity War,أفلام,300
ما اسم الكوكب الذي جاء منه Thor؟,Asgard,أفلام,300
ما اسم أخت Thor الشريرة؟,Hela,أفلام,300
ما اسم سلاح Thor الجديد بعد تدمير Mjolnir؟,Stormbreaker,أفلام,300
ما اسم مملكة Black Panther؟,Wakanda,أفلام,300
من هو العدو الرئيسي في Black Panther؟,Killmonger,أفلام,300
ما اسم المعدن الذي صنع منه درع Black Panther؟,Vibranium,أفلام,300
ما اسم الشرير في Doctor Strange الأول؟,Dormammu,أفلام,300
ما اسم البعد الذي حوصر فيه Dormammu؟,Dark Dimension,أفلام,300
ما اسم الشخصية التي أصبحت Captain America بعد Steve؟,Sam Wilson,أفلام,300

ما اسم فيلم Spider-Man الذي ظهر فيه Mysterio؟,Far From Home,أفلام,300
ما اسم الشرير الحقيقي في Far From Home؟,Quentin Beck,أفلام,300
ما اسم فيلم Spider-Man الذي جمع الأكوان الثلاثة؟,No Way Home,أفلام,300
من هو الشرير الذي عاد من Spider-Man 2؟,Doctor Octopus,أفلام,300
ما اسم الشرير الكهربائي في No Way Home؟,Electro,أفلام,300
ما اسم المنظمة التي يقودها Nick Fury؟,S.H.I.E.L.D,أفلام,300
من هو الشرير في Captain America Winter Soldier؟,The Winter Soldier,أفلام,300
ما الاسم الحقيقي لـ Winter Soldier؟,Bucky Barnes,أفلام,300
ما اسم الحرب التي قسمت Avengers؟,Civil War,أفلام,300
من هو الشرير في Civil War؟,Helmut Zemo,أفلام,300

ما اسم فيلم DC الذي جمع الأبطال لأول مرة؟,Justice League,أفلام,300
من هو الشرير الرئيسي في Justice League؟,Steppenwolf,أفلام,300
ما اسم كوكب Superman الأصلي؟,Krypton,أفلام,300
من هو والد Superman؟,Jor-El,أفلام,300
ما اسم الصحفية التي يحبها Superman؟,Lois Lane,أفلام,300
ما اسم العدو الرئيسي في فيلم The Batman 2022؟,The Riddler,أفلام,300
ما اسم العدو في فيلم Aquaman 2؟,Black Manta,أفلام,300
ما اسم البطلة في فيلم Wonder Woman؟,Diana Prince,أفلام,300
من هو الشرير في Wonder Woman 1984؟,Maxwell Lord,أفلام,300
ما اسم المدينة التي يحميها Batman؟,Gotham,أفلام,300

ما اسم فيلم Harry Potter الذي ظهر فيه Sirius Black؟,Prisoner of Azkaban,أفلام,300
من هو Sirius Black بالنسبة لهاري؟,عرابه,أفلام,300
ما اسم السجن السحري في عالم هاري بوتر؟,Azkaban,أفلام,300
ما اسم الحراس الذين يحرسون Azkaban؟,Dementors,أفلام,300
ما اسم تعويذة Patronus الشهيرة؟,Expecto Patronum,أفلام,300
ما اسم فيلم Harry Potter الذي مات فيه Dumbledore؟,Half-Blood Prince,أفلام,300
من قتل Dumbledore؟,Severus Snape,أفلام,300
ما اسم الأمير نصف الدم؟,Severus Snape,أفلام,300
ما اسم القطعة التي تحتوي جزء من روح Voldemort؟,Horcrux,أفلام,300
كم عدد Horcrux الأساسية؟,Seven,أفلام,300

ما اسم فيلم الخيال العلمي الذي يحكي عن روبوتات تحكم العالم؟,I Robot,أفلام,300
من هو بطل I Robot؟,Will Smith,أفلام,300
ما اسم فيلم يحكي عن ذكاء اصطناعي يقع في الحب؟,Her,أفلام,300
ما اسم فيلم يحكي عن تجربة زمنية تتكرر؟,Edge of Tomorrow,أفلام,300
من هو بطل Edge of Tomorrow؟,Tom Cruise,أفلام,300
ما اسم فيلم الفضاء الذي يواجه فيه البشر كائنات زرقاء؟,Avatar,أفلام,300
ما اسم كوكب Avatar؟,Pandora,أفلام,300
من هو مخرج Avatar؟,James Cameron,أفلام,300
ما اسم فيلم يحكي عن سفينة غرقت شهيرة؟,Titanic,أفلام,300
من هو بطل Titanic؟,Jack Dawson,أفلام,300

ما اسم فيلم Marvel الذي ظهر فيه أول مرة Black Panther؟,Captain America Civil War,أفلام,300
ما اسم فيلم Marvel الذي قدم شخصية Shang-Chi؟,Shang-Chi and the Legend of the Ten Rings,أفلام,300
ما اسم المنظمة التي كانت تتحكم في Shang-Chi؟,Ten Rings,أفلام,300
ما اسم فيلم Marvel الذي تدور أحداثه في مصر؟,Moon Knight,أفلام,300
ما اسم الإله الذي ارتبط بـ Moon Knight؟,Khonshu,أفلام,300
ما اسم فيلم Marvel الذي قدم شخصية Eternals؟,Eternals,أفلام,300
ما اسم العدو في فيلم Eternals؟,Deviants,أفلام,300
ما اسم فيلم Marvel الذي ظهر فيه Kang لأول مرة؟,Ant-Man Quantumania,أفلام,300
ما اسم العالم الذي دخلوا إليه في Quantumania؟,Quantum Realm,أفلام,300
ما اسم فيلم Marvel الذي قدم شخصية Captain Marvel؟,Captain Marvel,أفلام,300

ما اسم الطيار الذي أصبحت Captain Marvel؟,Carol Danvers,أفلام,300
ما اسم العرق الفضائي في Captain Marvel؟,Skrulls,أفلام,300
ما اسم فيلم Avengers الأول؟,The Avengers,أفلام,300
من هو الشرير الرئيسي في Avengers 1؟,Loki,أفلام,300
ما اسم حجر الفضاء؟,Space Stone,أفلام,300
ما اسم حجر العقل؟,Mind Stone,أفلام,300
ما اسم حجر القوة؟,Power Stone,أفلام,300
ما اسم حجر الواقع؟,Reality Stone,أفلام,300
ما اسم حجر الروح؟,Soul Stone,أفلام,300
ما اسم حجر الزمن؟,Time Stone,أفلام,300

ما اسم فيلم DC الذي ظهر فيه Joker مع Batman قديمًا؟,The Dark Knight,أفلام,300
من لعب Joker في فيلم Joker 2019؟,Joaquin Phoenix,أفلام,300
ما اسم فيلم DC الذي ظهر فيه Flash؟,The Flash,أفلام,300
ما اسم فيلم DC الذي قدم شخصية Shazam؟,Shazam!,أفلام,300
من هو الشرير في Shazam؟,Doctor Sivana,أفلام,300
ما اسم فيلم DC الذي قدم Black Adam؟,Black Adam,أفلام,300
من هو بطل Black Adam؟,Dwayne Johnson,أفلام,300
ما اسم مدينة Superman البشرية؟,Metropolis,أفلام,300
ما اسم فيلم Batman الذي ظهر فيه Penguin؟,The Batman,أفلام,300
ما اسم فيلم Batman الذي ظهر فيه Two-Face؟,The Dark Knight,أفلام,300

ما اسم فيلم يحكي عن رحلة في الزمن لإنقاذ البشرية؟,Back to the Future,أفلام,300
من هو بطل Back to the Future؟,Marty McFly,أفلام,300
ما اسم السيارة الزمنية الشهيرة؟,DeLorean,أفلام,300
ما اسم فيلم يحكي عن خاتم يتحكم بالعالم؟,The Lord of the Rings,أفلام,300
من هو حامل الخاتم؟,Frodo Baggins,أفلام,300
ما اسم الساحر الرمادي؟,Gandalf,أفلام,300
ما اسم الشرير في Lord of the Rings؟,Sauron,أفلام,300
ما اسم مخلوق الخاتم؟,Gollum,أفلام,300
ما اسم فيلم يحكي عن ملك أسد؟,The Lion King,أفلام,300
ما اسم والد Simba؟,Mufasa,أفلام,300

ما اسم فيلم Pixar الذي يحكي عن ألعاب حية؟,Toy Story,أفلام,300
ما اسم شخصية رائد الفضاء اللعبة؟,Buzz Lightyear,أفلام,300
ما اسم رعاة البقر اللعبة؟,Woody,أفلام,300
ما اسم فيلم يحكي عن فتى يعيش مع وحوش؟,Spirited Away,أفلام,300
من هو مخرج Spirited Away؟,Hayao Miyazaki,أفلام,300
ما اسم فيلم يحكي عن مدينة متحركة؟,Howl’s Moving Castle,أفلام,300
ما اسم فيلم يحكي عن أميرة محاربة؟,Princess Mononoke,أفلام,300
ما اسم فيلم يحكي عن قط حافلة؟,My Neighbor Totoro,أفلام,300
ما اسم فيلم يحكي عن مهرج قاتل في الصرف الصحي؟,IT,أفلام,300
ما اسم الوحش في IT؟,Pennywise,أفلام,300

ما اسم الفيلم الذي قدّم شخصية Deadpool لأول مرة؟,X-Men Origins Wolverine,أفلام,500
ما اسم الفيلم الذي أصبح فيه Deadpool مشهورًا؟,Deadpool,أفلام,500
من هو الممثل الذي لعب Deadpool؟,Ryan Reynolds,أفلام,500
ما اسم العدو الرئيسي في فيلم Deadpool 1؟,Ajax,أفلام,500
ما اسم الفيلم الذي جمع Deadpool مع Wolverine؟,Deadpool & Wolverine,أفلام,500

ما اسم الفيلم الذي ظهر فيه أول مرة Kang بشكل أساسي؟,Ant-Man and the Wasp Quantumania,أفلام,500
ما اسم النسخة الشريرة من Doctor Strange؟,Strange Supreme,أفلام,500
ما اسم فيلم Marvel الذي حدثت فيه “Multiverse Madness”؟,Doctor Strange in the Multiverse of Madness,أفلام,500
من هي الساحرة التي أصبحت شريرة في Multiverse Madness؟,Wanda Maximoff,أفلام,500
ما اسم كتاب السحر الأسود في Marvel؟,Darkhold,أفلام,500

ما اسم فيلم Marvel الذي مات فيه Iron Man؟,Avengers Endgame,أفلام,500
ما آخر جملة قالها Iron Man قبل موته؟,I am Iron Man,أفلام,500
من هو الشخص الذي ضحى بنفسه للحصول على Soul Stone؟,Black Widow,أفلام,500
أين توجد Soul Stone؟,Vormir,أفلام,500
من هو حارس Vormir؟,Red Skull,أفلام,500

ما اسم فيلم DC الذي ظهر فيه Superman ضد Doomsday؟,Batman v Superman,أفلام,500
ما اسم الوحش الذي قتل Superman؟,Doomsday,أفلام,500
ما اسم الفيلم الذي عاد فيه Superman للحياة؟,Justice League,أفلام,500
من هو الشرير الرئيسي في Zack Snyder Justice League؟,Darkseid,أفلام,500
ما اسم جنود Darkseid؟,Parademons,أفلام,500

ما اسم فيلم Harry Potter الذي ظهر فيه Deathly Hallows؟,Harry Potter and the Deathly Hallows,أفلام,500
ما هي Deathly Hallows الثلاثة؟,العصا الكبرى + حجر القيامة + عباءة الإخفاء,أفلام,500
من هو مالك Elder Wand الحقيقي في النهاية؟,Harry Potter,أفلام,500
من قتل Voldemort؟,انعكاس تعويذته عليه,أفلام,500
ما اسم تعويذة Voldemort القاتلة؟,Avada Kedavra,أفلام,500

ما اسم فيلم Lord of the Rings الأخير؟,Return of the King,أفلام,500
من هو الملك الذي عاد في النهاية؟,Aragorn,أفلام,500
ما اسم معركة النهاية ضد Sauron؟,معركة بوابة Mordor,أفلام,500
ما اسم جبل تدمير الخاتم؟,Mount Doom,أفلام,500
من أسقط الخاتم في النار؟,Gollum,أفلام,500

ما اسم فيلم الخيال العلمي الذي يحكي عن ذكاء اصطناعي يسيطر؟,Ex Machina,أفلام,500
ما اسم الروبوت الأنثوي في Ex Machina؟,Ava,أفلام,500
ما اسم فيلم يحكي عن السفر عبر ثقب دودي؟,Interstellar,أفلام,500
ما اسم الكوكب الذي زاروه وفيه الزمن أسرع؟,Miller’s Planet,أفلام,500
ما اسم شخصية العالم في Interstellar؟,Dr. Mann,أفلام,500

ما اسم فيلم الرعب الذي تدور أحداثه حول راهبة شيطانية؟,The Nun,أفلام,500
ما اسم الشيطان في The Nun؟,Valak,أفلام,500
ما اسم سلسلة الأفلام التي تشمل Annabelle؟,The Conjuring Universe,أفلام,500
ما اسم المحققين في The Conjuring؟,Ed and Lorraine Warren,أفلام,500
ما اسم الدمية المرعبة؟,Annabelle,أفلام,500

ما اسم فيلم يحكي عن قاتل يرتدي قناع أبيض؟,Halloween,أفلام,500
ما اسم القاتل في Halloween؟,Michael Myers,أفلام,500
ما اسم فيلم يحكي عن قاتل في الأحلام؟,A Nightmare on Elm Street,أفلام,500
ما اسم القاتل في Nightmare؟,Freddy Krueger,أفلام,500
ما اسم فيلم يحكي عن قاتل بقناع Ghostface؟,Scream,أفلام,500

ما اسم فيلم IMDb الشهير رقم 1 غالبًا؟,The Shawshank Redemption,أفلام,500
من هو بطل Shawshank Redemption؟,Andy Dufresne,أفلام,500
ما اسم فيلم المافيا الشهير؟,The Godfather,أفلام,500
من هو زعيم عائلة Corleone؟,Vito Corleone,أفلام,500
ما اسم الجزء الذي يعتبر الأفضل في Godfather؟,The Godfather Part II,أفلام,500

ما اسم فيلم IMDb الشهير الذي يحكي عن فارس مظلم؟,The Dark Knight,أفلام,500
من هو الشرير الرئيسي في The Dark Knight؟,Joker,أفلام,500
ما اسم الفيلم الذي يحكي عن حلم داخل حلم؟,Inception,أفلام,500
ما اسم الطوطم الخاص بـ Cobb؟,Spinning Top,أفلام,500
من هو مخرج Inception؟,Christopher Nolan,أفلام,500

ما اسم فيلم يحكي عن عالم مليء بالديناصورات؟,Jurassic Park,أفلام,500
من هو المخرج الشهير لـ Jurassic Park؟,Steven Spielberg,أفلام,500
ما اسم الجزيرة في Jurassic Park؟,Isla Nublar,أفلام,500
ما اسم الديناصور الرئيسي المفترس؟,T-Rex,أفلام,500
ما اسم فيلم Jurassic Park الجديد؟,Jurassic World,أفلام,500

ما اسم فيلم يحكي عن سفينة فضاء تواجه كائنًا قاتلًا؟,Alien,أفلام,500
ما اسم البطلة في Alien؟,Ellen Ripley,أفلام,500
ما اسم الكائن الفضائي؟,Xenomorph,أفلام,500
ما اسم فيلم الخيال العلمي الذي يحكي عن صائد جوائز؟,Blade Runner,أفلام,500
من هو بطل Blade Runner؟,Rick Deckard,أفلام,500

ما اسم فيلم يحكي عن روبوتات تتحول إلى سيارات؟,Transformers,أفلام,500
ما اسم قائد Autobots؟,Optimus Prime,أفلام,500
ما اسم قائد Decepticons؟,Megatron,أفلام,500
ما اسم فيلم يحكي عن روبوت من المستقبل لحماية طفل؟,Terminator 2,أفلام,500
ما اسم الطفل الذي حماه Terminator؟,John Connor,أفلام,500

ما اسم فيلم يحكي عن قاتل مأجور محترف؟,John Wick,أفلام,500
ما اسم الكلب الذي أشعل انتقام John Wick؟,Daisy,أفلام,500
ما اسم المنظمة السرية للقتلة؟,The High Table,أفلام,500
ما اسم الفندق الخاص بالقتلة؟,The Continental,أفلام,500
من هو مدير الفندق؟,Winston,أفلام,500

ما اسم فيلم يحكي عن ملاكمين في نادي سري؟,Fight Club,أفلام,500
ما أول قاعدة في Fight Club؟,لا تتحدث عن Fight Club,أفلام,500
من هو مؤلف Fight Club؟,Chuck Palahniuk,أفلام,500
ما اسم فيلم يحكي عن عقل عبقري في الرياضيات؟,A Beautiful Mind,أفلام,500
من هو بطل الفيلم؟,John Nash,أفلام,500

ما اسم فيلم يحكي عن عبقري يهرب من FBI؟,Catch Me If You Can,أفلام,500
من هو بطل Catch Me If You Can؟,Frank Abagnale,أفلام,500
من لعب دور Frank؟,Leonardo DiCaprio,أفلام,500
من لعب دور المحقق؟,Tom Hanks,أفلام,500
ما اسم فيلم يحكي عن جزيرة فيها مصحة عقلية؟,Shutter Island,أفلام,500

ما اسم فيلم يحكي عن رجل يعيش في عالم مزيف؟,The Truman Show,أفلام,500
من هو بطل Truman Show؟,Jim Carrey,أفلام,500
ما اسم فيلم يحكي عن رحلة انتقام رومانية؟,Gladiator,أفلام,500
من هو بطل Gladiator؟,Maximus,أفلام,500
من هو الإمبراطور الشرير؟,Commodus,أفلام,500

ما اسم فيلم يحكي عن حرب فيتنام نفسية؟,Apocalypse Now,أفلام,500
ما اسم فيلم الحرب العالمية الثانية الشهير؟,Saving Private Ryan,أفلام,500
من هو المخرج؟,Steven Spielberg,أفلام,500
ما اسم فيلم يحكي عن المحرقة النازية؟,Schindler’s List,أفلام,500
من هو بطل الفيلم؟,Oskar Schindler,أفلام,500

ما اسم فيلم يحكي عن قاتل متسلسل عبقري؟,Se7en,أفلام,500
ما اسم الخطيئة الأخيرة في Se7en؟,Envy,أفلام,500
ما اسم فيلم يحكي عن طبيب آكل لحوم البشر؟,The Silence of the Lambs,أفلام,500
ما اسم الطبيب؟,Hannibal Lecter,أفلام,500
من هي المحققة؟,Clarice Starling,أفلام,500

ما اسم فيلم يحكي عن عصابة في شوارع LA؟,Pulp Fiction,أفلام,500
من هو المخرج؟,Quentin Tarantino,أفلام,500
ما اسم فيلم Tarantino عن الحرب العالمية؟,Inglourious Basterds,أفلام,500
من هو الشرير النازي؟,Hans Landa,أفلام,500
ما اسم الفيلم الذي يحكي عن عبد ينتقم؟,Django Unchained,أفلام,500

ما اسم فيلم Pixar الذي يحكي عن رجل عجوز يطير بمنزله؟,Up,أفلام,500
ما اسم الطفل الكشاف؟,Russell,أفلام,500
ما اسم فيلم يحكي عن طبخ فأر؟,Ratatouille,أفلام,500
ما اسم الفأر الطباخ؟,Remy,أفلام,500
ما اسم فيلم يحكي عن موسيقى وعالم الأرواح؟,Coco,أفلام,500

ما اسم الكائن الفضائي الذي خلق قوة العمالقة في فيلم Alien؟,Xenomorph Queen,أفلام,1000
ما اسم الشركة التي كانت وراء أحداث Alien؟,Weyland-Yutani,أفلام,1000
ما اسم النسخة النهائية من نظام Skynet في Terminator؟,Legion,أفلام,1000
ما اسم اليوم الذي بدأ فيه تمرد الآلات في Terminator؟,Judgment Day,أفلام,1000
ما اسم النموذج المتطور الذي تحول إلى معدن سائل؟,T-1000,أفلام,1000

ما اسم المدينة الحقيقية التي بنيت عليها Gotham غالبًا؟,New York + Chicago,أفلام,1000
ما اسم الخطة الفلسفية للـ Joker في The Dark Knight؟,إثبات أن الجميع يمكن أن يصبح فاسدًا,أفلام,1000
ما اسم السجين الذي أنقذ Bruce Wayne في The Dark Knight Rises؟,Bane,أفلام,1000
ما اسم السجن الذي سُجن فيه Bruce؟,The Pit,أفلام,1000
ما اسم الشخصية التي أصبحت Catwoman؟,Selina Kyle,أفلام,1000

ما اسم التعويذة التي كسرت عصا Elder Wand؟,لا توجد تعويذة محددة (كسر يدوي),أفلام,1000
من هو آخر Horcrux تم تدميره؟,Nagini,أفلام,1000
ما اسم حجر القيامة في Deathly Hallows؟,Resurrection Stone,أفلام,1000
ما اسم صاحب عباءة الإخفاء الأصلية؟,Ignotus Peverell,أفلام,1000
من هو الأخ الذي امتلك Elder Wand؟,Antioch Peverell,أفلام,1000

ما اسم اللغة التي تحدث بها Na’vi في Avatar؟,لغة النافي,أفلام,1000
ما اسم الشجرة المقدسة في Avatar؟,Tree of Souls,أفلام,1000
ما اسم المادة النادرة التي يبحث عنها البشر في Pandora؟,Unobtanium,أفلام,1000
ما اسم القبيلة الرئيسية في Avatar؟,Omaticaya,أفلام,1000
ما اسم القائد العسكري البشري؟,Colonel Quaritch,أفلام,1000

ما اسم الخطة النهائية لـ Thanos في Endgame؟,إعادة خلق الكون من الصفر,أفلام,1000
من هو الشخص الذي أعاد نصف الكون للحياة؟,Hulk,أفلام,1000
ما اسم النسخة البديلة من Gamora؟,Gamora 2014,أفلام,1000
ما اسم البعد الذي سافروا إليه لجمع الأحجار؟,Quantum Realm,أفلام,1000
ما اسم النظرية الزمنية المستخدمة؟,Branch Timelines,أفلام,1000

ما اسم الخاتم الذي أعطاه Sauron للبشر؟,Nine Rings for Men,أفلام,1000
ما اسم ملك الساحرات في Lord of the Rings؟,Witch-king of Angmar,أفلام,1000
ما اسم لغة Mordor السوداء؟,Black Speech,أفلام,1000
ما اسم المعركة التي مات فيها Boromir؟,معركة Amon Hen,أفلام,1000
ما اسم والد Aragorn؟,Arathorn,أفلام,1000



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
file_path = os.path.join(os.getcwd(), "movies_series_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
