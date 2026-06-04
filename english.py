import pandas as pd
import os


# البيانات النصية تحتوي على جميع الأسئلة
data = """


ما معنى كلمة "improve" في الجملة: I want to improve my English this year؟,يحسن أو يطور,الإنجليزي,100
ما معنى كلمة "borrow" في الجملة: Can I borrow your pen for a minute؟,يستعير,الإنجليزي,100
ما معنى كلمة "advice" في الجملة: My teacher gave me useful advice؟,نصيحة,الإنجليزي,100
ما معنى كلمة "crowded" في الجملة: The bus was crowded after school؟,مزدحم,الإنجليزي,100
ما معنى كلمة "polite" في الجملة: The boy was polite to the guests؟,مهذب,الإنجليزي,100
ما معنى كلمة "careless" في الجملة: He made a careless mistake in the test؟,غير منتبه أو مهمل,الإنجليزي,100
ما معنى كلمة "decide" في الجملة: We need to decide where to eat؟,يقرر,الإنجليزي,100
ما معنى كلمة "avoid" في الجملة: Try to avoid eating too much sugar؟,يتجنب,الإنجليزي,100
ما معنى كلمة "arrive" في الجملة: They will arrive at the airport soon؟,يصل,الإنجليزي,100
ما معنى كلمة "explain" في الجملة: Please explain the rule again؟,يشرح,الإنجليزي,100
ما معنى كلمة "choose" في الجملة: You can choose any book you like؟,يختار,الإنجليزي,100
ما معنى كلمة "prepare" في الجملة: I need to prepare for the meeting؟,يستعد أو يحضر,الإنجليزي,100
ما معنى كلمة "forget" في الجملة: Do not forget your homework؟,ينسى,الإنجليزي,100
ما معنى كلمة "remember" في الجملة: I remember his name now؟,يتذكر,الإنجليزي,100
ما معنى كلمة "invite" في الجملة: She will invite her friends to the party؟,يدعو,الإنجليزي,100
ما معنى كلمة "accept" في الجملة: He accepted the invitation happily؟,يقبل,الإنجليزي,100
ما معنى كلمة "refuse" في الجملة: She refused to answer the question؟,يرفض,الإنجليزي,100
ما معنى كلمة "repair" في الجملة: My father can repair the old radio؟,يصلح,الإنجليزي,100
ما معنى كلمة "protect" في الجملة: A helmet can protect your head؟,يحمي,الإنجليزي,100
ما معنى كلمة "support" في الجملة: His family supported his dream؟,يدعم أو يساند,الإنجليزي,100
ما معنى كلمة "collect" في الجملة: The children collect shells at the beach؟,يجمع,الإنجليزي,100
ما معنى كلمة "receive" في الجملة: I received a message from my cousin؟,يستلم,الإنجليزي,100
ما معنى كلمة "send" في الجملة: Please send the file tonight؟,يرسل,الإنجليزي,100
ما معنى كلمة "return" في الجملة: I will return the book tomorrow؟,يعيد أو يرجع,الإنجليزي,100
ما معنى كلمة "share" في الجملة: They share one computer at home؟,يشارك,الإنجليزي,100
ما معنى كلمة "promise" في الجملة: He promised to help me later؟,يعد,الإنجليزي,100
ما معنى كلمة "believe" في الجملة: I believe your story؟,يصدق أو يؤمن,الإنجليزي,100
ما معنى كلمة "notice" في الجملة: Did you notice the new sign؟,يلاحظ,الإنجليزي,100
ما معنى كلمة "follow" في الجملة: Follow the instructions carefully؟,يتبع,الإنجليزي,100
ما معنى كلمة "allow" في الجملة: The teacher allowed us to leave early؟,يسمح,الإنجليزي,100
ما معنى كلمة "finish" في الجملة: I finished my project before dinner؟,ينهي,الإنجليزي,100
ما معنى كلمة "continue" في الجملة: We will continue the lesson tomorrow؟,يستمر أو يواصل,الإنجليزي,100
ما معنى كلمة "practice" في الجملة: You should practice speaking every day؟,يتدرب أو يمارس,الإنجليزي,100
ما معنى كلمة "repeat" في الجملة: Can you repeat the last sentence؟,يكرر,الإنجليزي,100
ما معنى كلمة "compare" في الجملة: Compare the two answers carefully؟,يقارن,الإنجليزي,100
ما معنى كلمة "describe" في الجملة: Describe your room in three sentences؟,يصف,الإنجليزي,100
ما معنى كلمة "discover" في الجملة: Scientists discovered a new planet؟,يكتشف,الإنجليزي,100
ما معنى كلمة "expect" في الجملة: I expect him to come on time؟,يتوقع,الإنجليزي,100
ما معنى كلمة "cost" في الجملة: How much does this jacket cost؟,يكلف أو سعره,الإنجليزي,100
ما معنى كلمة "save" في الجملة: She saves money every month؟,يدخر أو يحفظ,الإنجليزي,100
ما معنى كلمة "spend" في الجملة: I spend two hours studying English؟,يقضي أو ينفق حسب السياق,الإنجليزي,100
ما معنى كلمة "waste" في الجملة: Do not waste your time on small problems؟,يضيع أو يهدر,الإنجليزي,100
ما معنى كلمة "healthy" في الجملة: Eating vegetables is healthy؟,صحي,الإنجليزي,100
ما معنى كلمة "sick" في الجملة: He felt sick after lunch؟,مريض أو يشعر بالغثيان,الإنجليزي,100
ما معنى كلمة "tired" في الجملة: I was tired after the long trip؟,متعب,الإنجليزي,100
ما معنى كلمة "busy" في الجملة: My mother is busy at work today؟,مشغول,الإنجليزي,100
ما معنى كلمة "quiet" في الجملة: The library was quiet in the morning؟,هادئ,الإنجليزي,100
ما معنى كلمة "noisy" في الجملة: The street was noisy at night؟,مزعج أو كثير الضوضاء,الإنجليزي,100
ما معنى كلمة "simple" في الجملة: The question was simple for most students؟,بسيط,الإنجليزي,100
ما معنى كلمة "difficult" في الجملة: This exercise is difficult for beginners؟,صعب,الإنجليزي,100
ما معنى كلمة "useful" في الجملة: This app is useful for learning words؟,مفيد,الإنجليزي,100
ما معنى كلمة "useless" في الجملة: The broken charger is useless now؟,غير مفيد أو عديم الفائدة,الإنجليزي,100
ما معنى كلمة "dangerous" في الجملة: Driving too fast is dangerous؟,خطير,الإنجليزي,100
ما معنى كلمة "safe" في الجملة: This road is safe during the day؟,آمن,الإنجليزي,100
ما معنى كلمة "honest" في الجملة: She is honest with her friends؟,صادق أو أمين,الإنجليزي,100
ما معنى كلمة "patient" في الجملة: A good teacher is patient with students؟,صبور,الإنجليزي,100
ما معنى كلمة "lazy" في الجملة: He was too lazy to clean his room؟,كسول,الإنجليزي,100
ما معنى كلمة "brave" في الجملة: The firefighter was brave؟,شجاع,الإنجليزي,100
ما معنى كلمة "clever" في الجملة: That was a clever solution؟,ذكي,الإنجليزي,100
ما معنى كلمة "friendly" في الجملة: The new student is friendly؟,ودود,الإنجليزي,100
ما معنى كلمة "serious" في الجملة: He looked serious during the meeting؟,جاد,الإنجليزي,100
ما معنى كلمة "fresh" في الجملة: The bread is fresh this morning؟,طازج,الإنجليزي,100
ما معنى كلمة "empty" في الجملة: The bottle is empty؟,فارغ,الإنجليزي,100
ما معنى كلمة "full" في الجملة: The box is full of toys؟,ممتلئ,الإنجليزي,100
ما معنى كلمة "heavy" في الجملة: This bag is too heavy to carry؟,ثقيل,الإنجليزي,100
ما معنى كلمة "light" في الجملة: The suitcase is light and easy to move؟,خفيف,الإنجليزي,100
ما معنى كلمة "wide" في الجملة: The river is very wide here؟,واسع أو عريض,الإنجليزي,100
ما معنى كلمة "narrow" في الجملة: The street is narrow and old؟,ضيق,الإنجليزي,100
ما معنى كلمة "deep" في الجملة: The lake is deep in the middle؟,عميق,الإنجليزي,100
ما معنى كلمة "shallow" في الجملة: The water is shallow near the beach؟,ضحل أو غير عميق,الإنجليزي,100
ما معنى كلمة "smooth" في الجملة: The table feels smooth؟,ناعم أو أملس,الإنجليزي,100
ما معنى كلمة "rough" في الجملة: The wall feels rough؟,خشن,الإنجليزي,100
ما معنى كلمة "nearby" في الجملة: There is a pharmacy nearby؟,قريب أو في الجوار,الإنجليزي,100
ما معنى كلمة "far" في الجملة: The school is far from my house؟,بعيد,الإنجليزي,100
ما معنى كلمة "early" في الجملة: She arrived early for the exam؟,مبكرا,الإنجليزي,100
ما معنى كلمة "late" في الجملة: He was late for class again؟,متأخر,الإنجليزي,100
ما معنى كلمة "usually" في الجملة: I usually drink tea in the morning؟,عادة,الإنجليزي,100
ما معنى كلمة "rarely" في الجملة: He rarely eats fast food؟,نادرا,الإنجليزي,100
ما معنى كلمة "often" في الجملة: We often visit our grandparents؟,غالبا أو كثيرا,الإنجليزي,100
ما معنى كلمة "almost" في الجملة: I almost missed the bus؟,تقريبا أو كاد أن,الإنجليزي,100
ما معنى كلمة "already" في الجملة: She has already finished her work؟,بالفعل أو مسبقا,الإنجليزي,100
ما معنى كلمة "perhaps" في الجملة: Perhaps we can meet after lunch؟,ربما,الإنجليزي,100
ما معنى كلمة "instead" في الجملة: I drank water instead of soda؟,بدلا من ذلك,الإنجليزي,100
ما معنى كلمة "although" في الجملة: Although it was raining we went outside؟,رغم أن,الإنجليزي,100
ما معنى كلمة "because" في الجملة: I stayed home because I was tired؟,لأن,الإنجليزي,100
ما معنى كلمة "during" في الجملة: Do not talk during the movie؟,أثناء,الإنجليزي,100
ما معنى كلمة "before" في الجملة: Wash your hands before eating؟,قبل,الإنجليزي,100
ما معنى كلمة "after" في الجملة: Call me after school؟,بعد,الإنجليزي,100
ما معنى كلمة "without" في الجملة: He left without saying goodbye؟,بدون,الإنجليزي,100
ما معنى كلمة "through" في الجملة: We walked through the park؟,عبر أو خلال,الإنجليزي,100
ما معنى كلمة "towards" في الجملة: The dog ran towards the gate؟,نحو أو باتجاه,الإنجليزي,100
ما معنى كلمة "beside" في الجملة: She sat beside her sister؟,بجانب,الإنجليزي,100
ما معنى كلمة "behind" في الجملة: The keys are behind the door؟,خلف,الإنجليزي,100
ما معنى كلمة "between" في الجملة: The bank is between the school and the market؟,بين,الإنجليزي,100
ما معنى كلمة "inside" في الجملة: The phone is inside the bag؟,داخل,الإنجليزي,100
ما معنى كلمة "outside" في الجملة: The children are playing outside the house؟,خارج,الإنجليزي,100
ما معنى كلمة "enough" في الجملة: We have enough chairs for everyone؟,كاف أو بما يكفي,الإنجليزي,100
ما معنى كلمة "several" في الجملة: I called him several times؟,عدة,الإنجليزي,100
ما معنى كلمة "whole" في الجملة: She read the whole story؟,كامل,الإنجليزي,100
ما معنى كلمة "own" في الجملة: He wants to start his own business؟,خاص به,الإنجليزي,100

ما معنى كلمة "suggest" في الجملة: I suggest visiting the museum tomorrow؟,يقترح,الإنجليزي,100
ما معنى كلمة "agree" في الجملة: I agree with your opinion about the movie؟,يوافق,الإنجليزي,100
ما معنى كلمة "disagree" في الجملة: They disagree about the best solution؟,يختلف أو لا يوافق,الإنجليزي,100
ما معنى كلمة "complain" في الجملة: Customers complain when the service is slow؟,يشتكي,الإنجليزي,100
ما معنى كلمة "apologize" في الجملة: You should apologize for being late؟,يعتذر,الإنجليزي,100
ما معنى كلمة "admire" في الجملة: I admire people who work hard؟,يعجب ب أو يحترم,الإنجليزي,100
ما معنى كلمة "respect" في الجملة: Students should respect their teachers؟,يحترم,الإنجليزي,100
ما معنى كلمة "trust" في الجملة: I trust my best friend؟,يثق ب,الإنجليزي,100
ما معنى كلمة "doubt" في الجملة: I doubt that he will come today؟,يشك,الإنجليزي,100
ما معنى كلمة "guess" في الجملة: Can you guess the answer؟,يخمن,الإنجليزي,100
ما معنى كلمة "solve" في الجملة: We need to solve this problem quickly؟,يحل,الإنجليزي,100
ما معنى كلمة "check" في الجملة: Please check your answer before you submit it؟,يفحص أو يتأكد,الإنجليزي,100
ما معنى كلمة "search" في الجملة: I will search for the missing file؟,يبحث,الإنجليزي,100
ما معنى كلمة "find" في الجملة: Did you find your keys؟,يجد,الإنجليزي,100
ما معنى كلمة "lose" في الجملة: Do not lose your ticket؟,يفقد,الإنجليزي,100
ما معنى كلمة "hide" في الجملة: The cat likes to hide under the bed؟,يختبئ أو يخفي,الإنجليزي,100
ما معنى كلمة "carry" في الجملة: Can you carry this box for me؟,يحمل,الإنجليزي,100
ما معنى كلمة "push" في الجملة: Push the door to open it؟,يدفع,الإنجليزي,100
ما معنى كلمة "pull" في الجملة: Pull the rope slowly؟,يسحب,الإنجليزي,100
ما معنى كلمة "throw" في الجملة: Do not throw stones at the window؟,يرمي,الإنجليزي,100
ما معنى كلمة "catch" في الجملة: Try to catch the ball؟,يمسك أو يلتقط,الإنجليزي,100
ما معنى كلمة "kick" في الجملة: He kicked the ball into the goal؟,يركل,الإنجليزي,100
ما معنى كلمة "climb" في الجملة: They climbed the hill before sunset؟,يتسلق,الإنجليزي,100
ما معنى كلمة "jump" في الجملة: The child jumped over the small wall؟,يقفز,الإنجليزي,100
ما معنى كلمة "cross" في الجملة: Be careful when you cross the street؟,يعبر,الإنجليزي,100
ما معنى كلمة "drive" في الجملة: My uncle can drive a truck؟,يقود,الإنجليزي,100
ما معنى كلمة "ride" في الجملة: She can ride a bicycle well؟,يركب,الإنجليزي,100
ما معنى كلمة "fly" في الجملة: Birds fly high in the sky؟,يطير,الإنجليزي,100
ما معنى كلمة "swim" في الجملة: He learned to swim last summer؟,يسبح,الإنجليزي,100
ما معنى كلمة "wear" في الجملة: You should wear a coat in winter؟,يرتدي,الإنجليزي,100
ما معنى كلمة "fit" في الجملة: These shoes fit me perfectly؟,يناسب المقاس,الإنجليزي,100
ما معنى كلمة "match" في الجملة: Your shirt does not match your shoes؟,يناسب أو يتماشى مع,الإنجليزي,100
ما معنى كلمة "clean" في الجملة: Please clean your desk before leaving؟,ينظف,الإنجليزي,100
ما معنى كلمة "wash" في الجملة: Wash the dishes after dinner؟,يغسل,الإنجليزي,100
ما معنى كلمة "dry" في الجملة: Dry your hands with this towel؟,يجفف,الإنجليزي,100
ما معنى كلمة "fill" في الجملة: Fill the cup with water؟,يملأ,الإنجليزي,100
ما معنى كلمة "cover" في الجملة: Cover the food to keep it warm؟,يغطي,الإنجليزي,100
ما معنى كلمة "open" في الجملة: Open the window please؟,يفتح,الإنجليزي,100
ما معنى كلمة "close" في الجملة: Close the door quietly؟,يغلق,الإنجليزي,100
ما معنى كلمة "lock" في الجملة: Lock the car before you leave؟,يقفل,الإنجليزي,100
ما معنى كلمة "unlock" في الجملة: Use this key to unlock the gate؟,يفتح القفل,الإنجليزي,100
ما معنى كلمة "build" في الجملة: They will build a new school here؟,يبني,الإنجليزي,100
ما معنى كلمة "break" في الجملة: Be careful not to break the glass؟,يكسر,الإنجليزي,100
ما معنى كلمة "damage" في الجملة: The storm damaged the roof؟,يتلف أو يضر,الإنجليزي,100
ما معنى كلمة "paint" في الجملة: We will paint the room blue؟,يطلي أو يرسم,الإنجليزي,100
ما معنى كلمة "design" في الجملة: She wants to design a new logo؟,يصمم,الإنجليزي,100
ما معنى كلمة "create" في الجملة: The team created a simple app؟,ينشئ أو يبتكر,الإنجليزي,100
ما معنى كلمة "delete" في الجملة: Do not delete this important message؟,يحذف,الإنجليزي,100
ما معنى كلمة "copy" في الجملة: Copy the address into your notebook؟,ينسخ,الإنجليزي,100
ما معنى كلمة "print" في الجملة: I need to print this document؟,يطبع,الإنجليزي,100
ما معنى كلمة "record" في الجملة: The camera can record video in high quality؟,يسجل,الإنجليزي,100
ما معنى كلمة "upload" في الجملة: Upload the photo to the website؟,يرفع على الإنترنت,الإنجليزي,100
ما معنى كلمة "download" في الجملة: I will download the lesson at home؟,ينزل من الإنترنت,الإنجليزي,100
ما معنى كلمة "install" في الجملة: You need to install the app first؟,يثبت,الإنجليزي,100
ما معنى كلمة "update" في الجملة: Update the software to fix the error؟,يحدث,الإنجليزي,100
ما معنى كلمة "connect" في الجملة: Connect the charger to the phone؟,يوصل أو يربط,الإنجليزي,100
ما معنى كلمة "disconnect" في الجملة: Disconnect the cable before moving the computer؟,يفصل الاتصال,الإنجليزي,100
ما معنى كلمة "charge" في الجملة: I need to charge my phone tonight؟,يشحن,الإنجليزي,100
ما معنى كلمة "switch" في الجملة: Switch off the lights before sleeping؟,يطفئ أو يبدل,الإنجليزي,100
ما معنى كلمة "press" في الجملة: Press the red button to start؟,يضغط,الإنجليزي,100
ما معنى كلمة "type" في الجملة: Type your password carefully؟,يكتب على لوحة المفاتيح,الإنجليزي,100
ما معنى كلمة "enter" في الجملة: Enter your name in the box؟,يدخل,الإنجليزي,100
ما معنى كلمة "select" في الجملة: Select the correct answer؟,يختار أو يحدد,الإنجليزي,100
ما معنى كلمة "cancel" في الجملة: I had to cancel the trip because of rain؟,يلغي,الإنجليزي,100
ما معنى كلمة "join" في الجملة: I want to join the football team؟,ينضم,الإنجليزي,100
ما معنى كلمة "leave" في الجملة: We should leave the house early؟,يغادر,الإنجليزي,100
ما معنى كلمة "stay" في الجملة: I will stay at my aunt's house tonight؟,يبقى أو يقيم,الإنجليزي,100
ما معنى كلمة "move" في الجملة: They will move to a bigger apartment؟,ينتقل أو يتحرك,الإنجليزي,100
ما معنى كلمة "rent" في الجملة: They rent a small house near the beach؟,يستأجر,الإنجليزي,100
ما معنى كلمة "own" في الجملة: She owns a small shop downtown؟,يمتلك,الإنجليزي,100
ما معنى كلمة "sell" في الجملة: My neighbor wants to sell his car؟,يبيع,الإنجليزي,100
ما معنى كلمة "buy" في الجملة: I need to buy a new notebook؟,يشتري,الإنجليزي,100
ما معنى كلمة "pay" في الجملة: You can pay by card؟,يدفع المال,الإنجليزي,100
ما معنى كلمة "earn" في الجملة: He earns money by fixing bikes؟,يكسب المال,الإنجليزي,100
ما معنى كلمة "win" في الجملة: Our team can win the match؟,يفوز,الإنجليزي,100
ما معنى كلمة "lose" في الجملة: They might lose the game if they play badly؟,يخسر,الإنجليزي,100
ما معنى كلمة "train" في الجملة: The players train every evening؟,يتدرب,الإنجليزي,100
ما معنى كلمة "rest" في الجملة: You should rest after the long walk؟,يرتاح,الإنجليزي,100
ما معنى كلمة "relax" في الجملة: I like to relax after studying؟,يسترخي,الإنجليزي,100
ما معنى كلمة "exercise" في الجملة: Doctors say we should exercise regularly؟,يمارس الرياضة,الإنجليزي,100
ما معنى كلمة "breathe" في الجملة: Breathe slowly when you feel nervous؟,يتنفس,الإنجليزي,100
ما معنى كلمة "smile" في الجملة: She smiled when she saw the gift؟,يبتسم,الإنجليزي,100
ما معنى كلمة "laugh" في الجملة: The joke made everyone laugh؟,يضحك,الإنجليزي,100
ما معنى كلمة "cry" في الجملة: The baby started to cry؟,يبكي,الإنجليزي,100
ما معنى كلمة "shout" في الجملة: Do not shout in the classroom؟,يصرخ,الإنجليزي,100
ما معنى كلمة "whisper" في الجملة: She whispered the answer to her friend؟,يهمس,الإنجليزي,100
ما معنى كلمة "listen" في الجملة: Listen carefully to the instructions؟,يستمع,الإنجليزي,100
ما معنى كلمة "reply" في الجملة: Please reply to my email today؟,يرد,الإنجليزي,100
ما معنى كلمة "ask" في الجملة: Ask the teacher if you do not understand؟,يسأل,الإنجليزي,100
ما معنى كلمة "answer" في الجملة: Answer the question in English؟,يجيب,الإنجليزي,100
ما معنى كلمة "read" في الجملة: Read the paragraph twice؟,يقرأ,الإنجليزي,100
ما معنى كلمة "write" في الجملة: Write your name at the top of the page؟,يكتب,الإنجليزي,100
ما معنى كلمة "spell" في الجملة: Can you spell your last name؟,يتهجى,الإنجليزي,100
ما معنى كلمة "translate" في الجملة: Translate this sentence into Arabic؟,يترجم,الإنجليزي,100
ما معنى كلمة "learn" في الجملة: I want to learn a new language؟,يتعلم,الإنجليزي,100
ما معنى كلمة "teach" في الجملة: My brother can teach me math؟,يعلم,الإنجليزي,100
ما معنى كلمة "study" في الجملة: I study English every night؟,يدرس,الإنجليزي,100
ما معنى كلمة "pass" في الجملة: She worked hard to pass the exam؟,ينجح في,الإنجليزي,100
ما معنى كلمة "fail" في الجملة: He did not want to fail the test؟,يفشل أو يرسب,الإنجليزي,100
ما معنى كلمة "imagine" في الجملة: Imagine living on the moon؟,يتخيل,الإنجليزي,100
ما معنى كلمة "hope" في الجملة: I hope you feel better soon؟,يأمل,الإنجليزي,100


ما معنى كلمة "offer" في الجملة: They offered me a glass of water؟,يعرض أو يقدم,الإنجليزي,100
ما معنى كلمة "order" في الجملة: I ordered a sandwich at the cafe؟,يطلب شراء,الإنجليزي,100
ما معنى كلمة "serve" في الجملة: The waiter served the food quickly؟,يقدم الطعام,الإنجليزي,100
ما معنى كلمة "taste" في الجملة: This soup tastes salty؟,مذاقه أو يتذوق,الإنجليزي,100
ما معنى كلمة "smell" في الجملة: The flowers smell beautiful؟,تكون لها رائحة,الإنجليزي,100
ما معنى كلمة "boil" في الجملة: Boil the water before you make tea؟,يغلي,الإنجليزي,100
ما معنى كلمة "cook" في الجملة: My sister can cook pasta very well؟,يطبخ,الإنجليزي,100
ما معنى كلمة "slice" في الجملة: Slice the bread before serving it؟,يقطع إلى شرائح,الإنجليزي,100
ما معنى كلمة "mix" في الجملة: Mix the eggs with the milk؟,يخلط,الإنجليزي,100
ما معنى كلمة "add" في الجملة: Add some salt to the soup؟,يضيف,الإنجليزي,100
ما معنى كلمة "remove" في الجملة: Remove your shoes before entering the room؟,يزيل أو ينزع,الإنجليزي,100
ما معنى كلمة "include" في الجملة: The price includes breakfast؟,يشمل أو يتضمن,الإنجليزي,100
ما معنى كلمة "contain" في الجملة: This bottle contains orange juice؟,يحتوي على,الإنجليزي,100
ما معنى كلمة "require" في الجملة: This job requires good communication skills؟,يتطلب,الإنجليزي,100
ما معنى كلمة "depend" في الجملة: Children depend on their parents؟,يعتمد على,الإنجليزي,100
ما معنى كلمة "happen" في الجملة: What happened after the game؟,يحدث,الإنجليزي,100
ما معنى كلمة "appear" في الجملة: A message appeared on the screen؟,يظهر,الإنجليزي,100
ما معنى كلمة "disappear" في الجملة: The sun disappeared behind the clouds؟,يختفي,الإنجليزي,100
ما معنى كلمة "seem" في الجملة: She seems happy today؟,يبدو,الإنجليزي,100
ما معنى كلمة "become" في الجملة: He became famous after the competition؟,يصبح,الإنجليزي,100
ما معنى كلمة "grow" في الجملة: Plants grow faster in sunlight؟,ينمو,الإنجليزي,100
ما معنى كلمة "raise" في الجملة: Please raise your hand before speaking؟,يرفع,الإنجليزي,100
ما معنى كلمة "drop" في الجملة: Do not drop the glass on the floor؟,يسقط أو يوقع,الإنجليزي,100
ما معنى كلمة "fall" في الجملة: Leaves fall from trees in autumn؟,يسقط,الإنجليزي,100
ما معنى كلمة "stand" في الجملة: Please stand near the door؟,يقف,الإنجليزي,100
ما معنى كلمة "sit" في الجملة: Sit on the chair and wait؟,يجلس,الإنجليزي,100
ما معنى كلمة "lie" في الجملة: He likes to lie on the sofa after work؟,يستلقي,الإنجليزي,100
ما معنى كلمة "wake" في الجملة: I wake up early on school days؟,يستيقظ,الإنجليزي,100
ما معنى كلمة "sleep" في الجملة: I usually sleep at eleven o'clock؟,ينام,الإنجليزي,100
ما معنى كلمة "dream" في الجملة: She dreams about traveling the world؟,يحلم,الإنجليزي,100
ما معنى كلمة "plan" في الجملة: We plan to visit the city next week؟,يخطط,الإنجليزي,100
ما معنى كلمة "organize" في الجملة: They organized a small event at school؟,ينظم,الإنجليزي,100
ما معنى كلمة "manage" في الجملة: She manages a small team at work؟,يدير,الإنجليزي,100
ما معنى كلمة "control" في الجملة: Try to control your anger؟,يسيطر على أو يتحكم في,الإنجليزي,100
ما معنى كلمة "handle" في الجملة: He can handle difficult situations calmly؟,يتعامل مع,الإنجليزي,100
ما معنى كلمة "lead" في الجملة: The captain will lead the team today؟,يقود,الإنجليزي,100
ما معنى كلمة "guide" في الجملة: The map will guide us to the hotel؟,يرشد,الإنجليزي,100
ما معنى كلمة "warn" في الجملة: The sign warns drivers about the sharp turn؟,يحذر,الإنجليزي,100
ما معنى كلمة "remind" في الجملة: Please remind me to call Ali؟,يذكر,الإنجليزي,100
ما معنى كلمة "encourage" في الجملة: My coach encouraged me to keep training؟,يشجع,الإنجليزي,100
ما معنى كلمة "force" في الجملة: Nobody can force you to join the club؟,يجبر,الإنجليزي,100
ما معنى كلمة "permit" في الجملة: This ticket permits you to enter the museum؟,يسمح,الإنجليزي,100
ما معنى كلمة "forbid" في الجملة: The school forbids smoking inside the building؟,يمنع,الإنجليزي,100
ما معنى كلمة "prefer" في الجملة: I prefer tea to coffee؟,يفضل,الإنجليزي,100
ما معنى كلمة "hate" في الجملة: I hate waiting in long lines؟,يكره,الإنجليزي,100
ما معنى كلمة "enjoy" في الجملة: We enjoy watching documentaries؟,يستمتع ب,الإنجليزي,100
ما معنى كلمة "miss" في الجملة: I miss my old friends؟,يشتاق إلى,الإنجليزي,100
ما معنى كلمة "need" في الجملة: I need more time to finish؟,يحتاج,الإنجليزي,100
ما معنى كلمة "wish" في الجملة: I wish you success in your exam؟,يتمنى,الإنجليزي,100
ما معنى كلمة "fear" في الجملة: Some children fear the dark؟,يخاف من,الإنجليزي,100
ما معنى كلمة "worry" في الجملة: Do not worry about the small mistake؟,يقلق,الإنجليزي,100
ما معنى كلمة "surprise" في الجملة: Her visit surprised everyone؟,يفاجئ,الإنجليزي,100
ما معنى كلمة "interest" في الجملة: Science books interest him؟,يثير اهتمام,الإنجليزي,100
ما معنى كلمة "bore" في الجملة: Long lectures bore some students؟,يشعر بالملل,الإنجليزي,100
ما معنى كلمة "confuse" في الجملة: This rule can confuse beginners؟,يربك أو يحيّر,الإنجليزي,100
ما معنى كلمة "matter" في الجملة: Your opinion matters to me؟,يهم,الإنجليزي,100
ما معنى كلمة "mean" في الجملة: What does this word mean؟,يعني,الإنجليزي,100
ما معنى كلمة "sound" في الجملة: Your idea sounds interesting؟,يبدو أو صوته,الإنجليزي,100
ما معنى كلمة "touch" في الجملة: Do not touch the hot pan؟,يلمس,الإنجليزي,100
ما معنى كلمة "hold" في الجملة: Hold the baby carefully؟,يمسك أو يحمل,الإنجليزي,100
ما معنى كلمة "shake" في الجملة: Shake the bottle before drinking؟,يهز,الإنجليزي,100
ما معنى كلمة "bend" في الجملة: Bend your knees when you lift something heavy؟,يثني أو ينحني,الإنجليزي,100
ما معنى كلمة "stretch" في الجملة: Stretch your arms before exercise؟,يمد أو يتمدد,الإنجليزي,100
ما معنى كلمة "point" في الجملة: Point to the correct picture؟,يشير إلى,الإنجليزي,100
ما معنى كلمة "nod" في الجملة: She nodded to show agreement؟,يهز رأسه بالموافقة,الإنجليزي,100
ما معنى كلمة "wave" في الجملة: The children waved goodbye؟,يلوح باليد,الإنجليزي,100
ما معنى كلمة "pack" في الجملة: Pack your clothes before the trip؟,يحزم أو يجهز,الإنجليزي,100
ما معنى كلمة "unpack" في الجملة: I unpacked my bag after arriving؟,يفرغ الحقيبة,الإنجليزي,100
ما معنى كلمة "hang" في الجملة: Hang your coat on the hook؟,يعلق,الإنجليزي,100
ما معنى كلمة "fold" في الجملة: Fold the paper in half؟,يطوي,الإنجليزي,100
ما معنى كلمة "wrap" في الجملة: Wrap the gift before the party؟,يلف,الإنجليزي,100
ما معنى كلمة "tie" في الجملة: Tie your shoes before running؟,يربط,الإنجليزي,100
ما معنى كلمة "untie" في الجملة: Untie the rope slowly؟,يفك الرباط,الإنجليزي,100
ما معنى كلمة "measure" في الجملة: Measure the table before buying it؟,يقيس,الإنجليزي,100
ما معنى كلمة "weigh" في الجملة: Weigh the bag before traveling؟,يزن,الإنجليزي,100
ما معنى كلمة "count" في الجملة: Count the chairs in the room؟,يعد أو يحسب,الإنجليزي,100
ما معنى كلمة "calculate" في الجملة: Calculate the total price carefully؟,يحسب,الإنجليزي,100
ما معنى كلمة "estimate" في الجملة: Estimate the cost before you start؟,يقدر تقريبا,الإنجليزي,100
ما معنى كلمة "divide" في الجملة: Divide the cake into six pieces؟,يقسم,الإنجليزي,100
ما معنى كلمة "multiply" في الجملة: Multiply the number by five؟,يضرب في الحساب,الإنجليزي,100
ما معنى كلمة "increase" في الجملة: Prices increase during busy seasons؟,يزداد أو يزيد,الإنجليزي,100
ما معنى كلمة "decrease" في الجملة: The temperature will decrease tonight؟,ينخفض أو يقل,الإنجليزي,100
ما معنى كلمة "reduce" في الجملة: Try to reduce the amount of sugar in your tea؟,يقلل,الإنجليزي,100
ما معنى كلمة "compare" في الجملة: Compare the old price with the new one؟,يقارن,الإنجليزي,100
ما معنى كلمة "mark" في الجملة: Mark the correct answer with a circle؟,يضع علامة,الإنجليزي,100
ما معنى كلمة "underline" في الجملة: Underline the important words in the text؟,يضع خطا تحت,الإنجليزي,100
ما معنى كلمة "circle" في الجملة: Circle the word that does not belong؟,يضع دائرة حول,الإنجليزي,100
ما معنى كلمة "correct" في الجملة: Correct the mistakes in your essay؟,يصحح,الإنجليزي,100
ما معنى كلمة "impress" في الجملة: Her presentation impressed the teachers؟,يبهر أو يترك انطباعا جيدا,الإنجليزي,100
ما معنى كلمة "improvement" في الجملة: There is clear improvement in your writing؟,تحسن أو تطور,الإنجليزي,100
ما معنى كلمة "choice" في الجملة: You made the right choice؟,اختيار,الإنجليزي,100
ما معنى كلمة "decision" في الجملة: It was a difficult decision for the family؟,قرار,الإنجليزي,100
ما معنى كلمة "reason" في الجملة: What is the reason for your absence؟,سبب,الإنجليزي,100
ما معنى كلمة "result" في الجملة: The result of the test was excellent؟,نتيجة,الإنجليزي,100
ما معنى كلمة "example" في الجملة: Give me one example of a polite sentence؟,مثال,الإنجليزي,100
ما معنى كلمة "mistake" في الجملة: Everyone can make a mistake؟,خطأ,الإنجليزي,100
ما معنى كلمة "chance" في الجملة: This is your chance to try again؟,فرصة,الإنجليزي,100
ما معنى كلمة "purpose" في الجملة: The purpose of this lesson is to improve listening؟,هدف أو غرض,الإنجليزي,100
ما معنى كلمة "habit" في الجملة: Reading before bed is a good habit؟,عادة,الإنجليزي,100
ما معنى كلمة "skill" في الجملة: Speaking clearly is an important skill؟,مهارة,الإنجليزي,100
ما معنى كلمة "goal" في الجملة: My goal is to speak English fluently؟,هدف,الإنجليزي,100


ما معنى كلمة "ability" في الجملة: She has the ability to learn languages quickly؟,قدرة,الإنجليزي,100
ما معنى كلمة "accident" في الجملة: There was a small accident on the road؟,حادث,الإنجليزي,100
ما معنى كلمة "address" في الجملة: Please write your address clearly؟,عنوان,الإنجليزي,100
ما معنى كلمة "adult" في الجملة: Children must come with an adult؟,شخص بالغ,الإنجليزي,100
ما معنى كلمة "advantage" في الجملة: Knowing English is an advantage when traveling؟,ميزة أو فائدة,الإنجليزي,100
ما معنى كلمة "afraid" في الجملة: The little girl was afraid of the dog؟,خائف,الإنجليزي,100
ما معنى كلمة "amount" في الجملة: The amount of water in the bottle is small؟,كمية,الإنجليزي,100
ما معنى كلمة "ancient" في الجملة: We visited an ancient castle in the city؟,قديم جدا أو أثري,الإنجليزي,100
ما معنى كلمة "annoyed" في الجملة: He was annoyed because of the loud music؟,منزعج,الإنجليزي,100
ما معنى كلمة "area" في الجملة: This area is quiet at night؟,منطقة,الإنجليزي,100
ما معنى كلمة "argue" في الجملة: They often argue about small things؟,يتجادل,الإنجليزي,100
ما معنى كلمة "arrangement" في الجملة: We made an arrangement to meet at five؟,ترتيب أو اتفاق,الإنجليزي,100
ما معنى كلمة "attention" في الجملة: Please pay attention to the teacher؟,انتباه,الإنجليزي,100
ما معنى كلمة "available" في الجملة: The doctor is available after two o'clock؟,متاح,الإنجليزي,100
ما معنى كلمة "average" في الجملة: The average score in the class was high؟,متوسط,الإنجليزي,100
ما معنى كلمة "behavior" في الجملة: His behavior in class was excellent؟,سلوك,الإنجليزي,100
ما معنى كلمة "benefit" في الجملة: Exercise has many benefits for health؟,فائدة,الإنجليزي,100
ما معنى كلمة "border" في الجملة: The town is near the border؟,حد أو حدود,الإنجليزي,100
ما معنى كلمة "branch" في الجملة: The bird sat on a tree branch؟,غصن أو فرع,الإنجليزي,100
ما معنى كلمة "bright" في الجملة: The room is bright because of the large windows؟,مضيء,الإنجليزي,100
ما معنى كلمة "calm" في الجملة: Try to stay calm during the exam؟,هادئ,الإنجليزي,100
ما معنى كلمة "careful" في الجملة: Be careful when you use the knife؟,حذر أو منتبه,الإنجليزي,100
ما معنى كلمة "cause" في الجملة: Heavy rain can cause traffic problems؟,يسبب,الإنجليزي,100
ما معنى كلمة "certain" في الجملة: I am certain that I left my phone here؟,متأكد,الإنجليزي,100
ما معنى كلمة "challenge" في الجملة: Learning a new language can be a challenge؟,تحدي,الإنجليزي,100
ما معنى كلمة "comfortable" في الجملة: This chair is very comfortable؟,مريح,الإنجليزي,100
ما معنى كلمة "common" في الجملة: This mistake is common among beginners؟,شائع,الإنجليزي,100
ما معنى كلمة "community" في الجملة: The community helped clean the park؟,مجتمع محلي,الإنجليزي,100
ما معنى كلمة "condition" في الجملة: The car is in good condition؟,حالة,الإنجليزي,100
ما معنى كلمة "confidence" في الجملة: Practice can increase your confidence؟,ثقة بالنفس,الإنجليزي,100
ما معنى كلمة "conversation" في الجملة: We had a short conversation after class؟,محادثة,الإنجليزي,100
ما معنى كلمة "corner" في الجملة: The shop is on the corner of the street؟,زاوية,الإنجليزي,100
ما معنى كلمة "culture" في الجملة: Traveling helps you understand another culture؟,ثقافة,الإنجليزي,100
ما معنى كلمة "customer" في الجملة: The customer asked for a refund؟,زبون أو عميل,الإنجليزي,100
ما معنى كلمة "daily" في الجملة: Walking is part of my daily routine؟,يومي,الإنجليزي,100
ما معنى كلمة "delay" في الجملة: The flight had a delay because of bad weather؟,تأخير,الإنجليزي,100
ما معنى كلمة "detail" في الجملة: Read every detail before signing the paper؟,تفصيل,الإنجليزي,100
ما معنى كلمة "direction" في الجملة: He walked in the wrong direction؟,اتجاه,الإنجليزي,100
ما معنى كلمة "distance" في الجملة: The distance between the two cities is short؟,مسافة,الإنجليزي,100
ما معنى كلمة "double" في الجملة: The price is double what I expected؟,ضعف أو مضاعف,الإنجليزي,100
ما معنى كلمة "effort" في الجملة: Success needs time and effort؟,جهد,الإنجليزي,100
ما معنى كلمة "electric" في الجملة: We bought an electric car last year؟,كهربائي,الإنجليزي,100
ما معنى كلمة "emergency" في الجملة: Call this number in an emergency؟,حالة طارئة,الإنجليزي,100
ما معنى كلمة "energy" في الجملة: I do not have enough energy to run today؟,طاقة,الإنجليزي,100
ما معنى كلمة "entrance" في الجملة: The entrance to the museum is on the left؟,مدخل,الإنجليزي,100
ما معنى كلمة "environment" في الجملة: We should protect the environment؟,البيئة,الإنجليزي,100
ما معنى كلمة "equipment" في الجملة: The team needs new equipment for training؟,معدات,الإنجليزي,100
ما معنى كلمة "event" في الجملة: The school event starts at ten؟,حدث أو فعالية,الإنجليزي,100
ما معنى كلمة "exact" في الجملة: Tell me the exact time of the meeting؟,دقيق أو محدد,الإنجليزي,100
ما معنى كلمة "excellent" في الجملة: Her answer was excellent؟,ممتاز,الإنجليزي,100
ما معنى كلمة "expensive" في الجملة: This phone is too expensive for me؟,غالي,الإنجليزي,100
ما معنى كلمة "experience" في الجملة: She has experience in teaching children؟,خبرة أو تجربة,الإنجليزي,100
ما معنى كلمة "factory" في الجملة: My uncle works in a car factory؟,مصنع,الإنجليزي,100
ما معنى كلمة "fair" في الجملة: The teacher made a fair decision؟,عادل,الإنجليزي,100
ما معنى كلمة "familiar" في الجملة: This name sounds familiar to me؟,مألوف,الإنجليزي,100
ما معنى كلمة "famous" في الجملة: The city is famous for its old market؟,مشهور,الإنجليزي,100
ما معنى كلمة "favor" في الجملة: Can you do me a small favor؟,معروف أو خدمة,الإنجليزي,100
ما معنى كلمة "field" في الجملة: The children played football in the field؟,حقل أو ملعب,الإنجليزي,100
ما معنى كلمة "final" في الجملة: This is the final question in the test؟,نهائي أو أخير,الإنجليزي,100
ما معنى كلمة "flat" في الجملة: The road is flat and easy to walk on؟,مستو,الإنجليزي,100
ما معنى كلمة "foreign" في الجملة: She wants to learn a foreign language؟,أجنبي,الإنجليزي,100
ما معنى كلمة "freedom" في الجملة: Many people value freedom of speech؟,حرية,الإنجليزي,100
ما معنى كلمة "general" في الجملة: He gave a general answer to the question؟,عام,الإنجليزي,100
ما معنى كلمة "gentle" في الجملة: Be gentle with the small kitten؟,لطيف أو رقيق,الإنجليزي,100
ما معنى كلمة "giant" في الجملة: They saw a giant statue in the square؟,ضخم أو عملاق,الإنجليزي,100
ما معنى كلمة "guest" في الجملة: We prepared a room for the guest؟,ضيف,الإنجليزي,100
ما معنى كلمة "helpful" في الجملة: The guide was helpful during the trip؟,مساعد أو مفيد,الإنجليزي,100
ما معنى كلمة "huge" في الجملة: They live in a huge house near the sea؟,ضخم,الإنجليزي,100
ما معنى كلمة "human" في الجملة: Clean water is a basic human need؟,إنساني أو بشري,الإنجليزي,100
ما معنى كلمة "idea" في الجملة: That is a smart idea؟,فكرة,الإنجليزي,100
ما معنى كلمة "ill" في الجملة: He was ill and could not go to school؟,مريض,الإنجليزي,100
ما معنى كلمة "important" في الجملة: Sleep is important for your health؟,مهم,الإنجليزي,100
ما معنى كلمة "impossible" في الجملة: It is impossible to finish this in one minute؟,مستحيل,الإنجليزي,100
ما معنى كلمة "information" في الجملة: The website has useful information؟,معلومات,الإنجليزي,100
ما معنى كلمة "intelligent" في الجملة: Dolphins are intelligent animals؟,ذكي,الإنجليزي,100
ما معنى كلمة "journey" في الجملة: The journey took five hours by bus؟,رحلة,الإنجليزي,100
ما معنى كلمة "kind" في الجملة: It was kind of you to help her؟,لطيف أو طيب,الإنجليزي,100
ما معنى كلمة "knowledge" في الجملة: Reading increases your knowledge؟,معرفة,الإنجليزي,100
ما معنى كلمة "language" في الجملة: Arabic is a beautiful language؟,لغة,الإنجليزي,100
ما معنى كلمة "local" في الجملة: We bought bread from a local bakery؟,محلي,الإنجليزي,100
ما معنى كلمة "machine" في الجملة: This machine cuts paper quickly؟,آلة,الإنجليزي,100
ما معنى كلمة "main" في الجملة: The main reason is lack of time؟,رئيسي,الإنجليزي,100
ما معنى كلمة "market" في الجملة: The market is full of fresh fruit؟,سوق,الإنجليزي,100
ما معنى كلمة "material" في الجملة: This bag is made of strong material؟,مادة أو خامة,الإنجليزي,100
ما معنى كلمة "memory" في الجملة: My grandmother has a strong memory؟,ذاكرة,الإنجليزي,100
ما معنى كلمة "method" في الجملة: This method makes learning easier؟,طريقة,الإنجليزي,100
ما معنى كلمة "modern" في الجملة: They live in a modern apartment؟,حديث أو عصري,الإنجليزي,100
ما معنى كلمة "moment" في الجملة: Wait here for a moment؟,لحظة,الإنجليزي,100
ما معنى كلمة "necessary" في الجملة: A passport is necessary for international travel؟,ضروري,الإنجليزي,100
ما معنى كلمة "normal" في الجملة: It is normal to feel nervous before a test؟,طبيعي,الإنجليزي,100
ما معنى كلمة "object" في الجملة: There is a strange object under the table؟,شيء أو جسم,الإنجليزي,100
ما معنى كلمة "opinion" في الجملة: Everyone has a different opinion about the story؟,رأي,الإنجليزي,100
ما معنى كلمة "ordinary" في الجملة: It was an ordinary day at school؟,عادي,الإنجليزي,100
ما معنى كلمة "patient" في الجملة: The patient waited for the doctor؟,مريض,الإنجليزي,100
ما معنى كلمة "peaceful" في الجملة: The village is peaceful in the evening؟,هادئ أو مسالم,الإنجليزي,100
ما معنى كلمة "perfect" في الجملة: The weather was perfect for a picnic؟,مثالي,الإنجليزي,100
ما معنى كلمة "popular" في الجملة: Football is popular in many countries؟,شائع أو محبوب,الإنجليزي,100
ما معنى كلمة "possible" في الجملة: It is possible to finish early؟,ممكن,الإنجليزي,100
ما معنى كلمة "private" في الجملة: This is a private message؟,خاص,الإنجليزي,100
ما معنى كلمة "public" في الجملة: The park is open to the public؟,عام أو للجميع,الإنجليزي,100
ما معنى كلمة "quality" في الجملة: The quality of this camera is high؟,جودة,الإنجليزي,100
ما معنى كلمة "quick" في الجملة: She gave a quick answer؟,سريع,الإنجليزي,100
ما معنى كلمة "recent" في الجملة: I read a recent article about space؟,حديث أو مؤخرا,الإنجليزي,100
ما معنى كلمة "regular" في الجملة: Regular exercise is good for your body؟,منتظم,الإنجليزي,100
ما معنى كلمة "special" في الجملة: Today is a special day for our family؟,خاص أو مميز,الإنجليزي,100

ما معنى كلمة "separate" في الجملة: Keep the clean clothes separate from the dirty ones؟,منفصل أو يفصل,الإنجليزي,100
ما معنى كلمة "similar" في الجملة: The two phones look similar؟,متشابه,الإنجليزي,100
ما معنى كلمة "single" في الجملة: I made a single mistake in the test؟,واحد أو منفرد,الإنجليزي,100
ما معنى كلمة "solid" في الجملة: The table is made of solid wood؟,صلب أو متين,الإنجليزي,100
ما معنى كلمة "strange" في الجملة: I heard a strange noise outside؟,غريب,الإنجليزي,100
ما معنى كلمة "suitable" في الجملة: This jacket is suitable for cold weather؟,مناسب,الإنجليزي,100
ما معنى كلمة "terrible" في الجملة: The weather was terrible yesterday؟,سيئ جدا,الإنجليزي,100
ما معنى كلمة "thin" في الجملة: The paper is very thin؟,رقيق أو نحيف حسب السياق,الإنجليزي,100
ما معنى كلمة "thick" في الجملة: The book is thick and heavy؟,سميك,الإنجليزي,100
ما معنى كلمة "tiny" في الجملة: A tiny bird sat on the window؟,صغير جدا,الإنجليزي,100
ما معنى كلمة "valuable" في الجملة: This old watch is very valuable؟,قيّم أو ثمين,الإنجليزي,100
ما معنى كلمة "weak" في الجملة: He felt weak after being sick؟,ضعيف,الإنجليزي,100
ما معنى كلمة "wise" في الجملة: My grandfather gave me wise advice؟,حكيم,الإنجليزي,100
ما معنى كلمة "wonderful" في الجملة: We had a wonderful time at the beach؟,رائع,الإنجليزي,100
ما معنى كلمة "wrong" في الجملة: Your answer is wrong؟,خاطئ,الإنجليزي,100
ما معنى كلمة "active" في الجملة: She is active and plays sports every day؟,نشيط,الإنجليزي,100
ما معنى كلمة "asleep" في الجملة: The baby is asleep in the room؟,نائم,الإنجليزي,100
ما معنى كلمة "awake" في الجملة: I was still awake at midnight؟,مستيقظ,الإنجليزي,100
ما معنى كلمة "blind" في الجملة: The blind man used a stick to walk؟,كفيف,الإنجليزي,100
ما معنى كلمة "deaf" في الجملة: The deaf student uses sign language؟,أصم,الإنجليزي,100
ما معنى كلمة "equal" في الجملة: The two teams have equal points؟,متساو,الإنجليزي,100
ما معنى كلمة "female" في الجملة: The female doctor spoke kindly to the patient؟,أنثى أو امرأة,الإنجليزي,100
ما معنى كلمة "male" في الجملة: The male singer has a deep voice؟,ذكر أو رجل,الإنجليزي,100
ما معنى كلمة "married" في الجملة: My brother is married and has two children؟,متزوج,الإنجليزي,100
ما معنى كلمة "proud" في الجملة: His parents were proud of his success؟,فخور,الإنجليزي,100
ما معنى كلمة "ready" في الجملة: Are you ready for the trip؟,جاهز,الإنجليزي,100
ما معنى كلمة "responsible" في الجملة: She is responsible for organizing the files؟,مسؤول,الإنجليزي,100
ما معنى كلمة "rich" في الجملة: The city is rich in history؟,غني,الإنجليزي,100
ما معنى كلمة "successful" في الجملة: The event was successful؟,ناجح,الإنجليزي,100
ما معنى كلمة "thirsty" في الجملة: I am thirsty after running؟,عطشان,الإنجليزي,100
ما معنى كلمة "upset" في الجملة: He was upset after losing his phone؟,منزعج أو حزين,الإنجليزي,100
ما معنى كلمة "worried" في الجملة: She was worried about the exam؟,قلق,الإنجليزي,100
ما معنى كلمة "alive" في الجملة: The fish is still alive؟,حي,الإنجليزي,100
ما معنى كلمة "alone" في الجملة: He walked home alone؟,وحيد أو بمفرده,الإنجليزي,100
ما معنى كلمة "asleep" في الجملة: The cat was asleep on the chair؟,نائم,الإنجليزي,100
ما معنى كلمة "broken" في الجملة: The window is broken؟,مكسور أو تالف,الإنجليزي,100
ما معنى كلمة "central" في الجملة: The hotel is in a central location؟,مركزي,الإنجليزي,100
ما معنى كلمة "clear" في الجملة: The instructions are clear؟,واضح,الإنجليزي,100
ما معنى كلمة "complete" في الجملة: The report is complete now؟,كامل أو مكتمل,الإنجليزي,100
ما معنى كلمة "correct" في الجملة: Your answer is correct؟,صحيح,الإنجليزي,100
ما معنى كلمة "direct" في الجملة: We took a direct flight to London؟,مباشر,الإنجليزي,100
ما معنى كلمة "dry" في الجملة: The clothes are dry now؟,جاف,الإنجليزي,100
ما معنى كلمة "extra" في الجملة: I need extra time to finish the work؟,إضافي,الإنجليزي,100
ما معنى كلمة "false" في الجملة: The story was false؟,غير صحيح أو زائف,الإنجليزي,100
ما معنى كلمة "fast" في الجملة: This train is very fast؟,سريع,الإنجليزي,100
ما معنى كلمة "favorite" في الجملة: Pizza is my favorite food؟,مفضل,الإنجليزي,100
ما معنى كلمة "free" في الجملة: The ticket is free for children؟,مجاني,الإنجليزي,100
ما معنى كلمة "future" في الجملة: He wants to become an engineer in the future؟,المستقبل,الإنجليزي,100
ما معنى كلمة "half" في الجملة: I ate half of the sandwich؟,نصف,الإنجليزي,100
ما معنى كلمة "hard" في الجملة: She worked hard to pass the exam؟,بجد أو بقوة,الإنجليزي,100
ما معنى كلمة "helpful" في الجملة: This map is helpful for tourists؟,مفيد,الإنجليزي,100
ما معنى كلمة "high" في الجملة: The mountain is very high؟,عال أو مرتفع,الإنجليزي,100
ما معنى كلمة "hungry" في الجملة: I am hungry after school؟,جائع,الإنجليزي,100
ما معنى كلمة "inside" في الجملة: Keep the medicine inside the box؟,داخل,الإنجليزي,100
ما معنى كلمة "junior" في الجملة: He is a junior member of the team؟,أصغر أو مبتدئ,الإنجليزي,100
ما معنى كلمة "low" في الجملة: The wall is low enough to climb؟,منخفض,الإنجليزي,100
ما معنى كلمة "lucky" في الجملة: You are lucky to find your wallet؟,محظوظ,الإنجليزي,100
ما معنى كلمة "maximum" في الجملة: The maximum number of players is ten؟,الحد الأقصى,الإنجليزي,100
ما معنى كلمة "minimum" في الجملة: The minimum age is eighteen؟,الحد الأدنى,الإنجليزي,100
ما معنى كلمة "missing" في الجملة: One page is missing from the book؟,مفقود أو ناقص,الإنجليزي,100
ما معنى كلمة "natural" في الجملة: Honey is a natural sweetener؟,طبيعي,الإنجليزي,100
ما معنى كلمة "official" في الجملة: This is the official website of the school؟,رسمي,الإنجليزي,100
ما معنى كلمة "original" في الجملة: This is the original version of the song؟,أصلي,الإنجليزي,100
ما معنى كلمة "personal" في الجملة: Do not share your personal information online؟,شخصي,الإنجليزي,100
ما معنى كلمة "physical" في الجملة: Football requires physical strength؟,بدني أو جسدي,الإنجليزي,100
ما معنى كلمة "pleasant" في الجملة: We had a pleasant evening with our friends؟,لطيف أو ممتع,الإنجليزي,100
ما معنى كلمة "positive" في الجملة: Try to keep a positive attitude؟,إيجابي,الإنجليزي,100
ما معنى كلمة "practical" في الجملة: This course gives practical skills؟,عملي,الإنجليزي,100
ما معنى كلمة "present" في الجملة: Only ten students were present today؟,حاضر أو موجود,الإنجليزي,100
ما معنى كلمة "real" في الجملة: This is a real problem for many people؟,حقيقي,الإنجليزي,100
ما معنى كلمة "recently" في الجملة: I recently started learning Spanish؟,مؤخرا,الإنجليزي,100
ما معنى كلمة "same" في الجملة: We are in the same class؟,نفس أو ذاته,الإنجليزي,100
ما معنى كلمة "senior" في الجملة: She is a senior engineer at the company؟,كبير أو أعلى رتبة,الإنجليزي,100
ما معنى كلمة "sharp" في الجملة: Be careful with the sharp knife؟,حاد,الإنجليزي,100
ما معنى كلمة "silent" في الجملة: The room became silent after the announcement؟,صامت أو ساكت,الإنجليزي,100
ما معنى كلمة "soft" في الجملة: The pillow is soft؟,ناعم أو لين,الإنجليزي,100
ما معنى كلمة "sour" في الجملة: The lemon tastes sour؟,حامض,الإنجليزي,100
ما معنى كلمة "straight" في الجملة: Go straight until you reach the bank؟,مباشرة أو مستقيم,الإنجليزي,100
ما معنى كلمة "strong" في الجملة: This rope is strong enough to hold the box؟,قوي,الإنجليزي,100
ما معنى كلمة "sweet" في الجملة: This cake is very sweet؟,حلو,الإنجليزي,100
ما معنى كلمة "tall" في الجملة: The building is very tall؟,طويل,الإنجليزي,100
ما معنى كلمة "tight" في الجملة: These shoes are too tight؟,ضيق,الإنجليزي,100
ما معنى كلمة "true" في الجملة: The information is true؟,صحيح أو حقيقي,الإنجليزي,100
ما معنى كلمة "usual" في الجملة: He came at his usual time؟,معتاد,الإنجليزي,100
ما معنى كلمة "wet" في الجملة: My shoes are wet because of the rain؟,مبلل,الإنجليزي,100
ما معنى كلمة "wooden" في الجملة: They sat on a wooden bench؟,خشبي,الإنجليزي,100
ما معنى كلمة "carefully" في الجملة: Read the question carefully before answering؟,بحذر أو بانتباه,الإنجليزي,100
ما معنى كلمة "clearly" في الجملة: Speak clearly so everyone can hear you؟,بوضوح,الإنجليزي,100
ما معنى كلمة "easily" في الجملة: She solved the puzzle easily؟,بسهولة,الإنجليزي,100
ما معنى كلمة "finally" في الجملة: We finally arrived at the hotel؟,أخيرا,الإنجليزي,100
ما معنى كلمة "quickly" في الجملة: He quickly closed the window؟,بسرعة,الإنجليزي,100
ما معنى كلمة "slowly" في الجملة: Walk slowly on the wet floor؟,ببطء,الإنجليزي,100
ما معنى كلمة "suddenly" في الجملة: Suddenly the lights went off؟,فجأة,الإنجليزي,100
ما معنى كلمة "together" في الجملة: We studied together for the exam؟,معا,الإنجليزي,100
ما معنى كلمة "tomorrow" في الجملة: The meeting will be tomorrow morning؟,غدا,الإنجليزي,100
ما معنى كلمة "tonight" في الجملة: I will call you tonight؟,الليلة,الإنجليزي,100
ما معنى كلمة "yesterday" في الجملة: I saw him yesterday at the market؟,أمس,الإنجليزي,100
ما معنى كلمة "abroad" في الجملة: She wants to study abroad next year؟,في الخارج,الإنجليزي,100
ما معنى كلمة "indoors" في الجملة: We stayed indoors because it was raining؟,داخل المبنى,الإنجليزي,100
ما معنى كلمة "outdoors" في الجملة: Children should play outdoors sometimes؟,في الخارج أو الهواء الطلق,الإنجليزي,100
ما معنى كلمة "forward" في الجملة: Move forward three steps؟,إلى الأمام,الإنجليزي,100
ما معنى كلمة "backward" في الجملة: Take one step backward؟,إلى الخلف,الإنجليزي,100
ما معنى كلمة "near" في الجملة: The pharmacy is near the school؟,قريب من,الإنجليزي,100
ما معنى كلمة "among" في الجملة: She sat among her friends؟,بين مجموعة,الإنجليزي,100
ما معنى كلمة "against" في الجملة: The ladder is against the wall؟,مقابل أو مستند إلى,الإنجليزي,100
ما معنى كلمة "beyond" في الجملة: The village is beyond the hills؟,وراء أو أبعد من,الإنجليزي,100
ما معنى كلمة "except" في الجملة: Everyone came except Ahmed؟,ما عدا,الإنجليزي,100

ما معنى phrasal verb "figure out" في الجملة: I finally figured out how to fix the error؟,يفهم أو يجد الحل,الإنجليزي,300
ما معنى phrasal verb "turn down" في الجملة: She turned down the job offer because it was too far؟,يرفض,الإنجليزي,300
ما معنى كلمة "reliable" في الجملة: We need a reliable person to manage the project؟,موثوق,الإنجليزي,300
ما معنى كلمة "disappointed" في الجملة: He was disappointed when his team lost the match؟,محبط أو خائب الأمل,الإنجليزي,300
ما معنى idiom "keep an eye on" في الجملة: Please keep an eye on my bag while I buy coffee؟,يراقب أو ينتبه إلى,الإنجليزي,300
ما معنى idiom "out of the blue" في الجملة: She called me out of the blue after five years؟,بشكل مفاجئ,الإنجليزي,300
ما معنى phrasal verb "give up" في الجملة: Do not give up even if the exam is difficult؟,يستسلم أو يتوقف عن المحاولة,الإنجليزي,300
ما معنى phrasal verb "look after" في الجملة: My sister looks after the children on weekends؟,يعتني ب,الإنجليزي,300
ما معنى phrasal verb "run into" في الجملة: I ran into my old teacher at the mall؟,يقابل بالصدفة,الإنجليزي,300
ما معنى كلمة "confident" في الجملة: She felt confident before the interview؟,واثق من نفسه,الإنجليزي,300
ما معنى كلمة "generous" في الجملة: My uncle is generous and always helps others؟,كريم,الإنجليزي,300
ما معنى كلمة "selfish" في الجملة: It was selfish to take all the food without asking؟,أناني,الإنجليزي,300
ما معنى كلمة "curious" في الجملة: The child was curious about how the machine works؟,فضولي أو محب للاستطلاع,الإنجليزي,300
ما معنى كلمة "anxious" في الجملة: She felt anxious before the final exam؟,قلق أو متوتر,الإنجليزي,300
ما معنى كلمة "grateful" في الجملة: I am grateful for your help؟,ممتن أو شاكر,الإنجليزي,300
ما معنى كلمة "jealous" في الجملة: He became jealous when his friend won the prize؟,غيور,الإنجليزي,300
ما معنى كلمة "embarrassed" في الجملة: I felt embarrassed when I forgot her name؟,محرج,الإنجليزي,300
ما معنى كلمة "exhausted" في الجملة: After the long trip we were exhausted؟,مرهق جدا,الإنجليزي,300
ما معنى كلمة "relieved" في الجملة: She felt relieved after hearing the good news؟,مرتاح بعد قلق,الإنجليزي,300
ما معنى كلمة "frustrated" في الجملة: He felt frustrated because the computer kept crashing؟,محبط أو منزعج من الفشل,الإنجليزي,300
ما معنى كلمة "impressed" في الجملة: The manager was impressed by her presentation؟,معجب أو منبهر,الإنجليزي,300
ما معنى كلمة "annoying" في الجملة: That repeated noise is really annoying؟,مزعج,الإنجليزي,300
ما معنى كلمة "awkward" في الجملة: There was an awkward silence after his joke؟,محرج أو غير مريح,الإنجليزي,300
ما معنى كلمة "accurate" في الجملة: The report gives accurate information about the results؟,دقيق أو صحيح,الإنجليزي,300
ما معنى كلمة "brief" في الجملة: The teacher gave a brief explanation before the test؟,مختصر,الإنجليزي,300
ما معنى كلمة "urgent" في الجملة: This is an urgent message so please reply quickly؟,عاجل,الإنجليزي,300
ما معنى كلمة "minor" في الجملة: It was only a minor problem and we fixed it quickly؟,بسيط أو صغير,الإنجليزي,300
ما معنى كلمة "major" في الجملة: Losing the main file was a major issue؟,كبير أو مهم,الإنجليزي,300
ما معنى كلمة "typical" في الجملة: It is typical of him to arrive five minutes late؟,معتاد أو متوقع منه,الإنجليزي,300
ما معنى كلمة "rare" في الجملة: It is rare to see snow in this city؟,نادر,الإنجليزي,300
ما معنى كلمة "common sense" في الجملة: Use common sense when you share information online؟,تفكير منطقي أو بديهة,الإنجليزي,300
ما معنى كلمة "evidence" في الجملة: The police found evidence near the car؟,دليل,الإنجليزي,300
ما معنى كلمة "solution" في الجملة: We need a better solution to this problem؟,حل,الإنجليزي,300
ما معنى كلمة "opportunity" في الجملة: This course is a great opportunity to improve your skills؟,فرصة,الإنجليزي,300
ما معنى كلمة "responsibility" في الجملة: Taking care of the equipment is your responsibility؟,مسؤولية,الإنجليزي,300
ما معنى كلمة "requirement" في الجملة: Experience is not a requirement for this beginner job؟,شرط أو متطلب,الإنجليزي,300
ما معنى كلمة "achievement" في الجملة: Winning the competition was a great achievement؟,إنجاز,الإنجليزي,300
ما معنى كلمة "failure" في الجملة: He learned a lot from his failure؟,فشل,الإنجليزي,300
ما معنى كلمة "progress" في الجملة: She made good progress in English this month؟,تقدم أو تطور,الإنجليزي,300
ما معنى كلمة "pressure" في الجملة: He works well under pressure؟,ضغط,الإنجليزي,300
ما معنى كلمة "deadline" في الجملة: We must finish the report before the deadline؟,موعد نهائي للتسليم,الإنجليزي,300
ما معنى كلمة "schedule" في الجملة: My schedule is full this week؟,جدول أو مواعيد,الإنجليزي,300
ما معنى كلمة "appointment" في الجملة: I have an appointment with the dentist at three؟,موعد,الإنجليزي,300
ما معنى كلمة "available" في الجملة: The manager is not available right now؟,متاح,الإنجليزي,300
ما معنى كلمة "flexible" في الجملة: The company offers flexible working hours؟,مرن,الإنجليزي,300
ما معنى كلمة "efficient" في الجملة: This new system is faster and more efficient؟,فعال أو كفء,الإنجليزي,300
ما معنى كلمة "effective" في الجملة: This medicine is effective for headaches؟,مؤثر أو يعطي نتيجة,الإنجليزي,300
ما معنى كلمة "complicated" في الجملة: The instructions were too complicated for beginners؟,معقد,الإنجليزي,300
ما معنى كلمة "convenient" في الجملة: Online payment is convenient for many customers؟,مريح أو مناسب,الإنجليزي,300
ما معنى كلمة "affordable" في الجملة: We found an affordable hotel near the beach؟,بسعر مناسب,الإنجليزي,300
ما معنى كلمة "expensive" في الجملة: The repair was more expensive than I expected؟,غالي,الإنجليزي,300
ما معنى كلمة "valuable" في الجملة: His advice was valuable for my project؟,قيّم أو مفيد جدا,الإنجليزي,300
ما معنى كلمة "essential" في الجملة: Water is essential for life؟,ضروري أو أساسي,الإنجليزي,300
ما معنى كلمة "optional" في الجملة: The final activity is optional not required؟,اختياري,الإنجليزي,300
ما معنى كلمة "temporary" في الجملة: This is a temporary solution until we fix the system؟,مؤقت,الإنجليزي,300
ما معنى كلمة "permanent" في الجملة: They are looking for a permanent place to live؟,دائم,الإنجليزي,300
ما معنى كلمة "visible" في الجملة: The sign is clearly visible from the road؟,مرئي أو واضح للعين,الإنجليزي,300
ما معنى كلمة "invisible" في الجملة: The tiny mark was almost invisible؟,غير مرئي,الإنجليزي,300
ما معنى كلمة "sensitive" في الجملة: Be careful because this topic is sensitive؟,حساس,الإنجليزي,300
ما معنى كلمة "reasonable" في الجملة: The price seems reasonable for this quality؟,معقول,الإنجليزي,300
ما معنى كلمة "unusual" في الجملة: It is unusual for him to miss class؟,غير معتاد,الإنجليزي,300
ما معنى كلمة "ordinary" في الجملة: He turned an ordinary idea into a successful business؟,عادي,الإنجليزي,300
ما معنى كلمة "remarkable" في الجملة: Her improvement in one month was remarkable؟,ملحوظ أو رائع,الإنجليزي,300
ما معنى كلمة "responsible" في الجملة: He is responsible for checking the equipment؟,مسؤول عن,الإنجليزي,300
ما معنى كلمة "careless" في الجملة: A careless driver can cause serious accidents؟,مهمل أو غير منتبه,الإنجليزي,300
ما معنى كلمة "thoughtful" في الجملة: It was thoughtful of her to bring food for everyone؟,مراعي أو لطيف التفكير,الإنجليزي,300
ما معنى كلمة "stubborn" في الجملة: He is stubborn and never changes his mind؟,عنيد,الإنجليزي,300
ما معنى كلمة "modest" في الجملة: Although she is successful she remains modest؟,متواضع,الإنجليزي,300
ما معنى كلمة "arrogant" في الجملة: Nobody likes working with arrogant people؟,متكبر,الإنجليزي,300
ما معنى كلمة "mature" في الجملة: She gave a mature answer to the problem؟,ناضج,الإنجليزي,300
ما معنى كلمة "immature" في الجملة: His immature behavior annoyed the whole team؟,غير ناضج,الإنجليزي,300
ما معنى phrasal verb "pick up" في الجملة: I will pick up my brother from school؟,يأخذ أو يلتقط شخصا,الإنجليزي,300
ما معنى phrasal verb "drop off" في الجملة: Can you drop me off near the station؟,يوصل شخصا وينزله,الإنجليزي,300
ما معنى phrasal verb "find out" في الجملة: I need to find out why the app stopped working؟,يكتشف أو يعرف,الإنجليزي,300
ما معنى phrasal verb "bring up" في الجملة: She brought up an important point during the meeting؟,يطرح موضوعا,الإنجليزي,300
ما معنى phrasal verb "come back" في الجملة: He came back home after midnight؟,يرجع أو يعود,الإنجليزي,300
ما معنى phrasal verb "go over" في الجملة: Let us go over the lesson before the quiz؟,يراجع,الإنجليزي,300
ما معنى phrasal verb "look for" في الجملة: I am looking for my glasses؟,يبحث عن,الإنجليزي,300
ما معنى phrasal verb "set up" في الجملة: We need to set up the computer before the class؟,يجهز أو يعد,الإنجليزي,300
ما معنى phrasal verb "turn on" في الجملة: Turn on the lights when you enter the room؟,يشغل,الإنجليزي,300
ما معنى phrasal verb "turn off" في الجملة: Please turn off the TV before sleeping؟,يطفئ,الإنجليزي,300
ما معنى phrasal verb "write down" في الجملة: Write down the address before you forget it؟,يدون أو يكتب,الإنجليزي,300
ما معنى phrasal verb "fill in" في الجملة: Please fill in this form with your information؟,يملأ بيانات,الإنجليزي,300
ما معنى phrasal verb "calm down" في الجملة: Calm down and explain what happened slowly؟,يهدأ,الإنجليزي,300
ما معنى phrasal verb "show up" في الجملة: He did not show up for the meeting؟,يحضر أو يظهر,الإنجليزي,300
ما معنى phrasal verb "hang out" في الجملة: We usually hang out at the park after school؟,يقضي وقتا مع الأصدقاء,الإنجليزي,300
ما معنى phrasal verb "get along" في الجملة: She gets along well with her classmates؟,ينسجم أو يتفاهم,الإنجليزي,300
ما معنى idiom "break the ice" في الجملة: He told a funny story to break the ice؟,يكسر حاجز الصمت أو التوتر,الإنجليزي,300
ما معنى idiom "a piece of cake" في الجملة: The test was a piece of cake for her؟,سهل جدا,الإنجليزي,300
ما معنى idiom "once in a blue moon" في الجملة: We go camping once in a blue moon؟,نادرا جدا,الإنجليزي,300
ما معنى idiom "better late than never" في الجملة: He finally apologized better late than never؟,أن تأتي متأخرا أفضل من ألا تأتي,الإنجليزي,300
ما معنى idiom "hit the books" في الجملة: I need to hit the books tonight before the exam؟,يدرس بجد,الإنجليزي,300
ما معنى idiom "call it a day" في الجملة: We finished the work and decided to call it a day؟,ينهي العمل لهذا اليوم,الإنجليزي,300
ما معنى idiom "in the same boat" في الجملة: We are all in the same boat before the final exam؟,في نفس الموقف أو المشكلة,الإنجليزي,300
ما معنى idiom "spill the beans" في الجملة: Do not spill the beans about the surprise party؟,يفشي السر,الإنجليزي,300
ما معنى idiom "under the weather" في الجملة: I stayed home because I was under the weather؟,يشعر بالمرض,الإنجليزي,300
ما معنى idiom "cost an arm and a leg" في الجملة: That new laptop costs an arm and a leg؟,غالي جدا,الإنجليزي,300

ما معنى phrasal verb "put off" في الجملة: We had to put off the meeting until Monday؟,يؤجل,الإنجليزي,300
ما معنى phrasal verb "take off" في الجملة: The plane will take off at six in the morning؟,تقلع الطائرة,الإنجليزي,300
ما معنى phrasal verb "get over" في الجملة: It took her weeks to get over the flu؟,يتعافى من,الإنجليزي,300
ما معنى phrasal verb "deal with" في الجملة: The manager knows how to deal with angry customers؟,يتعامل مع,الإنجليزي,300
ما معنى phrasal verb "look into" في الجملة: The company will look into the complaint؟,يفحص أو يحقق في,الإنجليزي,300
ما معنى phrasal verb "carry on" في الجملة: Please carry on with your work while I am away؟,يواصل أو يستمر,الإنجليزي,300
ما معنى phrasal verb "give back" في الجملة: I need to give back the book tomorrow؟,يعيد,الإنجليزي,300
ما معنى phrasal verb "take care of" في الجملة: She takes care of her younger brother after school؟,يعتني ب,الإنجليزي,300
ما معنى phrasal verb "turn up" في الجملة: He turned up late to the party؟,يحضر أو يظهر,الإنجليزي,300
ما معنى phrasal verb "break down" في الجملة: Our car broke down on the way to the airport؟,يتعطل,الإنجليزي,300
ما معنى phrasal verb "look up" في الجملة: I looked up the word in the dictionary؟,يبحث عن معلومة,الإنجليزي,300
ما معنى phrasal verb "give away" في الجملة: They gave away old clothes to charity؟,يتبرع أو يعطي مجانا,الإنجليزي,300
ما معنى phrasal verb "run out of" في الجملة: We ran out of milk this morning؟,ينفد منه,الإنجليزي,300
ما معنى phrasal verb "come up with" في الجملة: She came up with a clever idea for the project؟,يبتكر أو يقترح,الإنجليزي,300
ما معنى phrasal verb "put up with" في الجملة: I cannot put up with this noise anymore؟,يتحمل,الإنجليزي,300
ما معنى phrasal verb "look forward to" في الجملة: I look forward to seeing you next week؟,يتطلع إلى,الإنجليزي,300
ما معنى phrasal verb "get rid of" في الجملة: We need to get rid of these old boxes؟,يتخلص من,الإنجليزي,300
ما معنى phrasal verb "catch up" في الجملة: I need to catch up on the lessons I missed؟,يعوض ما فاته,الإنجليزي,300
ما معنى phrasal verb "work out" في الجملة: We finally worked out the answer together؟,يحل أو ينجح في فهم,الإنجليزي,300
ما معنى phrasal verb "take over" في الجملة: She will take over the team next month؟,يتولى المسؤولية,الإنجليزي,300
ما معنى idiom "on the other hand" في الجملة: The hotel is cheap but on the other hand it is far from the center؟,من ناحية أخرى,الإنجليزي,300
ما معنى idiom "so far so good" في الجملة: The project is difficult but so far so good؟,الأمور جيدة حتى الآن,الإنجليزي,300
ما معنى idiom "at the last minute" في الجملة: He changed his plan at the last minute؟,في آخر لحظة,الإنجليزي,300
ما معنى idiom "in a hurry" في الجملة: She left the house in a hurry؟,على عجلة,الإنجليزي,300
ما معنى idiom "from time to time" في الجملة: I visit my old school from time to time؟,من حين لآخر,الإنجليزي,300
ما معنى idiom "all of a sudden" في الجملة: All of a sudden the lights went out؟,فجأة,الإنجليزي,300
ما معنى idiom "by the way" في الجملة: By the way I saw your brother yesterday؟,بالمناسبة,الإنجليزي,300
ما معنى idiom "in advance" في الجملة: Please book your ticket in advance؟,مسبقا,الإنجليزي,300
ما معنى idiom "on purpose" في الجملة: He did not break the cup on purpose؟,عمدا,الإنجليزي,300
ما معنى idiom "by mistake" في الجملة: I sent the message to the wrong person by mistake؟,عن طريق الخطأ,الإنجليزي,300
ما معنى idiom "in trouble" في الجملة: He will be in trouble if he misses the exam؟,في مشكلة,الإنجليزي,300
ما معنى idiom "out of order" في الجملة: The elevator is out of order today؟,معطل,الإنجليزي,300
ما معنى idiom "on time" في الجملة: The train arrived on time؟,في الوقت المحدد,الإنجليزي,300
ما معنى idiom "in charge of" في الجملة: Sara is in charge of the school event؟,مسؤول عن,الإنجليزي,300
ما معنى idiom "in common" في الجملة: The two friends have many interests in common؟,مشترك,الإنجليزي,300
ما معنى idiom "in fact" في الجملة: I thought the test was easy but in fact it was difficult؟,في الحقيقة,الإنجليزي,300
ما معنى idiom "for sure" في الجملة: I do not know for sure if he is coming؟,بالتأكيد أو بشكل مؤكد,الإنجليزي,300
ما معنى idiom "no matter what" في الجملة: I will support you no matter what happens؟,مهما حدث,الإنجليزي,300
ما معنى idiom "as soon as possible" في الجملة: Please call me as soon as possible؟,في أسرع وقت ممكن,الإنجليزي,300
ما معنى idiom "little by little" في الجملة: Little by little his English became better؟,شيئا فشيئا,الإنجليزي,300
ما معنى كلمة "determined" في الجملة: She was determined to pass the driving test؟,مصمم أو عازم,الإنجليزي,300
ما معنى كلمة "patient" في الجملة: You need to be patient when learning a new skill؟,صبور,الإنجليزي,300
ما معنى كلمة "independent" في الجملة: He became independent after starting his first job؟,مستقل,الإنجليزي,300
ما معنى كلمة "dependent" في الجملة: The project is dependent on good internet access؟,معتمد على,الإنجليزي,300
ما معنى كلمة "logical" في الجملة: Her explanation was clear and logical؟,منطقي,الإنجليزي,300
ما معنى كلمة "creative" في الجملة: The designer found a creative solution؟,مبدع,الإنجليزي,300
ما معنى كلمة "practical" في الجملة: His plan is practical and easy to follow؟,عملي,الإنجليزي,300
ما معنى كلمة "professional" في الجملة: She wrote a professional email to the company؟,مهني أو احترافي,الإنجليزي,300
ما معنى كلمة "personal" في الجملة: He shared a personal story during the lesson؟,شخصي,الإنجليزي,300
ما معنى كلمة "social" في الجملة: Social skills are important at work؟,اجتماعي,الإنجليزي,300
ما معنى كلمة "mental" في الجملة: Stress can affect your mental health؟,ذهني أو نفسي,الإنجليزي,300
ما معنى كلمة "emotional" في الجملة: The movie had an emotional ending؟,عاطفي أو مؤثر,الإنجليزي,300
ما معنى كلمة "serious" في الجملة: This is a serious problem that needs attention؟,خطير أو جاد,الإنجليزي,300
ما معنى كلمة "strict" في الجملة: The coach is strict but fair؟,صارم,الإنجليزي,300
ما معنى كلمة "fair" في الجملة: The judge made a fair decision؟,عادل,الإنجليزي,300
ما معنى كلمة "unfair" في الجملة: It is unfair to blame him alone؟,غير عادل,الإنجليزي,300
ما معنى كلمة "legal" في الجملة: It is legal to park here after six؟,قانوني,الإنجليزي,300
ما معنى كلمة "illegal" في الجملة: It is illegal to drive without a license؟,غير قانوني,الإنجليزي,300
ما معنى كلمة "official" في الجملة: The official results will be announced tomorrow؟,رسمي,الإنجليزي,300
ما معنى كلمة "unofficial" في الجملة: I heard an unofficial report about the match؟,غير رسمي,الإنجليزي,300
ما معنى كلمة "public" في الجملة: The information is available to the public؟,عام أو للجمهور,الإنجليزي,300
ما معنى كلمة "private" في الجملة: Please keep this conversation private؟,خاص,الإنجليزي,300
ما معنى كلمة "basic" في الجملة: The course teaches basic computer skills؟,أساسي,الإنجليزي,300
ما معنى كلمة "advanced" في الجملة: This is an advanced English class؟,متقدم,الإنجليزي,300
ما معنى كلمة "specific" في الجملة: Please give me a specific example؟,محدد,الإنجليزي,300
ما معنى كلمة "general" في الجملة: He only gave a general idea of the plan؟,عام,الإنجليزي,300
ما معنى كلمة "exactly" في الجملة: I know exactly what you mean؟,بالضبط,الإنجليزي,300
ما معنى كلمة "approximately" في الجملة: The trip takes approximately two hours؟,تقريبا,الإنجليزي,300
ما معنى كلمة "particularly" في الجملة: I particularly enjoyed the last chapter؟,خصوصا أو بشكل خاص,الإنجليزي,300
ما معنى كلمة "mainly" في الجملة: The course is mainly for beginners؟,بشكل رئيسي,الإنجليزي,300
ما معنى كلمة "mostly" في الجملة: The audience was mostly students؟,في الغالب,الإنجليزي,300
ما معنى كلمة "completely" في الجملة: I completely forgot about the appointment؟,تماما,الإنجليزي,300
ما معنى كلمة "partly" في الجملة: The accident was partly my fault؟,جزئيا,الإنجليزي,300
ما معنى كلمة "properly" في الجملة: The machine will not work properly without power؟,بشكل صحيح,الإنجليزي,300
ما معنى كلمة "directly" في الجملة: She spoke directly to the manager؟,مباشرة,الإنجليزي,300
ما معنى كلمة "indirectly" في الجملة: The new rule indirectly affected small shops؟,بشكل غير مباشر,الإنجليزي,300
ما معنى كلمة "immediately" في الجملة: Please leave the building immediately؟,فورا,الإنجليزي,300
ما معنى كلمة "eventually" في الجملة: After many tries he eventually solved the problem؟,في النهاية,الإنجليزي,300
ما معنى كلمة "recently" في الجملة: They recently opened a new restaurant nearby؟,مؤخرا,الإنجليزي,300
ما معنى كلمة "currently" في الجملة: She is currently working on a new project؟,حاليا,الإنجليزي,300
ما معنى كلمة "previously" في الجملة: I previously worked in a small company؟,سابقا,الإنجليزي,300
ما معنى كلمة "normally" في الجملة: I normally wake up before seven؟,عادة,الإنجليزي,300
ما معنى كلمة "rarely" في الجملة: He rarely speaks during meetings؟,نادرا,الإنجليزي,300
ما معنى كلمة "frequently" في الجملة: The website is frequently updated؟,بشكل متكرر,الإنجليزي,300
ما معنى كلمة "occasionally" في الجملة: We occasionally eat dinner outside؟,أحيانا,الإنجليزي,300
ما معنى كلمة "constantly" في الجملة: The baby was constantly crying last night؟,باستمرار,الإنجليزي,300
ما معنى كلمة "gradually" في الجملة: His health gradually improved after the operation؟,تدريجيا,الإنجليزي,300
ما معنى كلمة "suddenly" في الجملة: The weather suddenly changed in the afternoon؟,فجأة,الإنجليزي,300
ما معنى كلمة "clearly" في الجملة: She clearly explained the problem to the team؟,بوضوح,الإنجليزي,300
ما معنى كلمة "honestly" في الجملة: Honestly I do not agree with this decision؟,بصراحة,الإنجليزي,300
ما معنى كلمة "fortunately" في الجملة: Fortunately no one was hurt in the accident؟,لحسن الحظ,الإنجليزي,300
ما معنى كلمة "unfortunately" في الجملة: Unfortunately the event was canceled؟,للأسف,الإنجليزي,300
ما معنى كلمة "probably" في الجملة: He will probably arrive before dinner؟,على الأرجح,الإنجليزي,300
ما معنى كلمة "certainly" في الجملة: This will certainly help your English؟,بالتأكيد,الإنجليزي,300
ما معنى كلمة "possibly" في الجملة: We could possibly meet after work؟,ربما أو من الممكن,الإنجليزي,300
ما معنى كلمة "obviously" في الجملة: Obviously we need more time to finish؟,من الواضح,الإنجليزي,300
ما معنى كلمة "apparently" في الجملة: Apparently the shop closes at eight؟,على ما يبدو,الإنجليزي,300
ما معنى كلمة "actually" في الجملة: I thought he was angry but actually he was tired؟,في الحقيقة,الإنجليزي,300

ما معنى phrasal verb "back up" في الجملة: You should back up your files before updating the system؟,يحفظ نسخة احتياطية,الإنجليزي,300
ما معنى phrasal verb "log in" في الجملة: You must log in before you can see your account؟,يسجل الدخول,الإنجليزي,300
ما معنى phrasal verb "log out" في الجملة: Do not forget to log out after using a public computer؟,يسجل الخروج,الإنجليزي,300
ما معنى phrasal verb "sign up" في الجملة: I want to sign up for the English course؟,يسجل أو يشترك,الإنجليزي,300
ما معنى phrasal verb "cut down on" في الجملة: He is trying to cut down on sugar؟,يقلل من,الإنجليزي,300
ما معنى phrasal verb "eat out" في الجملة: We usually eat out on Friday nights؟,يأكل خارج البيت,الإنجليزي,300
ما معنى phrasal verb "warm up" في الجملة: Players should warm up before the match؟,يقوم بتمارين إحماء,الإنجليزي,300
ما معنى phrasal verb "cool down" في الجملة: Walk slowly to cool down after running؟,يهدأ الجسم بعد التمرين,الإنجليزي,300
ما معنى phrasal verb "try on" في الجملة: She wants to try on the jacket before buying it؟,يجرب الملابس,الإنجليزي,300
ما معنى phrasal verb "pay back" في الجملة: I will pay back the money next week؟,يرد المال,الإنجليزي,300
ما معنى phrasal verb "save up" في الجملة: He is saving up to buy a new laptop؟,يدخر المال,الإنجليزي,300
ما معنى phrasal verb "take out" في الجملة: Please take out the trash before dinner؟,يخرج أو يرمي خارجا,الإنجليزي,300
ما معنى phrasal verb "clean up" في الجملة: We need to clean up the room after the party؟,ينظف ويرتب,الإنجليزي,300
ما معنى phrasal verb "move on" في الجملة: After the mistake he decided to move on and try again؟,يتجاوز الأمر ويكمل,الإنجليزي,300
ما معنى phrasal verb "hold on" في الجملة: Hold on for a minute while I check the file؟,ينتظر قليلا,الإنجليزي,300
ما معنى phrasal verb "get back" في الجملة: I will get back to you after I speak to the manager؟,يرد لاحقا أو يعود,الإنجليزي,300
ما معنى phrasal verb "slow down" في الجملة: Slow down because the road is wet؟,يخفف السرعة,الإنجليزي,300
ما معنى phrasal verb "speed up" في الجملة: We need to speed up the process to finish today؟,يسرع,الإنجليزي,300
ما معنى phrasal verb "break up" في الجملة: The teacher broke up the students into small groups؟,يقسم إلى مجموعات,الإنجليزي,300
ما معنى phrasal verb "mix up" في الجملة: I mixed up the two addresses؟,يخلط أو يربك بين شيئين,الإنجليزي,300
ما معنى idiom "make up your mind" في الجملة: You need to make up your mind before noon؟,يتخذ قرارا,الإنجليزي,300
ما معنى idiom "take it easy" في الجملة: You look tired so take it easy today؟,يسترخي أو لا يجهد نفسه,الإنجليزي,300
ما معنى idiom "hang in there" في الجملة: The work is hard but hang in there؟,اصبر ولا تستسلم,الإنجليزي,300
ما معنى idiom "go the extra mile" في الجملة: She always goes the extra mile for her customers؟,يبذل جهدا إضافيا,الإنجليزي,300
ما معنى idiom "learn the ropes" في الجملة: It took me a week to learn the ropes at my new job؟,يتعلم أساسيات العمل,الإنجليزي,300
ما معنى idiom "on the right track" في الجملة: Your writing is improving so you are on the right track؟,في الطريق الصحيح,الإنجليزي,300
ما معنى idiom "the ball is in your court" في الجملة: I sent the offer and now the ball is in your court؟,الدور عليك لاتخاذ القرار,الإنجليزي,300
ما معنى idiom "miss the point" في الجملة: He answered quickly but missed the point of the question؟,لا يفهم الفكرة الأساسية,الإنجليزي,300
ما معنى idiom "get the point" في الجملة: I get the point but I still disagree؟,يفهم المقصود,الإنجليزي,300
ما معنى idiom "make sense" في الجملة: Your explanation makes sense now؟,يكون منطقيا أو مفهوما,الإنجليزي,300
ما معنى idiom "no wonder" في الجملة: No wonder you are tired after working all day؟,ليس غريبا أو من الطبيعي,الإنجليزي,300
ما معنى idiom "on second thought" في الجملة: On second thought I will stay home tonight؟,بعد إعادة التفكير,الإنجليزي,300
ما معنى idiom "in the long run" في الجملة: Saving money now will help you in the long run؟,على المدى الطويل,الإنجليزي,300
ما معنى idiom "in the short run" في الجملة: In the short run this plan may cost more؟,على المدى القصير,الإنجليزي,300
ما معنى idiom "day by day" في الجملة: Day by day his pronunciation became clearer؟,يوما بعد يوم,الإنجليزي,300
ما معنى idiom "step by step" في الجملة: The teacher explained the method step by step؟,خطوة بخطوة,الإنجليزي,300
ما معنى idiom "right away" في الجملة: Please send the report right away؟,فورا,الإنجليزي,300
ما معنى idiom "for now" في الجملة: For now we will use the old computer؟,في الوقت الحالي,الإنجليزي,300
ما معنى idiom "at first" في الجملة: At first I did not understand the rule؟,في البداية,الإنجليزي,300
ما معنى idiom "in the end" في الجملة: In the end we chose the cheaper option؟,في النهاية,الإنجليزي,300
ما معنى كلمة "adapt" في الجملة: It took me time to adapt to the new school؟,يتأقلم أو يتكيف,الإنجليزي,300
ما معنى كلمة "adjust" في الجملة: Adjust the volume if the sound is too loud؟,يضبط أو يعدل,الإنجليزي,300
ما معنى كلمة "announce" في الجملة: The school will announce the results tomorrow؟,يعلن,الإنجليزي,300
ما معنى كلمة "approach" في الجملة: We need a new approach to solve this issue؟,أسلوب أو طريقة,الإنجليزي,300
ما معنى كلمة "approve" في الجملة: The manager approved our request؟,يوافق رسميا,الإنجليزي,300
ما معنى كلمة "arrange" في الجملة: Can you arrange the chairs before the guests arrive؟,يرتب أو ينظم,الإنجليزي,300
ما معنى كلمة "attempt" في الجملة: He made another attempt to solve the puzzle؟,محاولة,الإنجليزي,300
ما معنى كلمة "avoidance" في الجملة: Avoidance of hard work will not help you improve؟,تجنب,الإنجليزي,300
ما معنى كلمة "balance" في الجملة: She tries to balance work and study؟,يوازن,الإنجليزي,300
ما معنى كلمة "compare" في الجملة: Compare the two plans before choosing one؟,يقارن,الإنجليزي,300
ما معنى كلمة "complaint" في الجملة: The hotel received a complaint about the noise؟,شكوى,الإنجليزي,300
ما معنى كلمة "concern" في الجملة: Safety is our main concern during the trip؟,قلق أو أمر مهم,الإنجليزي,300
ما معنى كلمة "confirm" في الجملة: Please confirm your email address؟,يؤكد,الإنجليزي,300
ما معنى كلمة "consider" في الجملة: We should consider all options before deciding؟,يفكر في أو يأخذ بعين الاعتبار,الإنجليزي,300
ما معنى كلمة "contact" في الجملة: Contact me if you need help؟,يتواصل مع,الإنجليزي,300
ما معنى كلمة "deliver" في الجملة: The company will deliver the package tomorrow؟,يوصل أو يسلم,الإنجليزي,300
ما معنى كلمة "develop" في الجملة: Reading can develop your vocabulary؟,يطور,الإنجليزي,300
ما معنى كلمة "effect" في الجملة: The medicine had a strong effect on the pain؟,تأثير,الإنجليزي,300
ما معنى كلمة "focus" في الجملة: Try to focus on the main idea؟,يركز,الإنجليزي,300
ما معنى كلمة "identify" في الجملة: Can you identify the mistake in this sentence؟,يحدد أو يتعرف على,الإنجليزي,300
ما معنى كلمة "ignore" في الجملة: Do not ignore important warnings؟,يتجاهل,الإنجليزي,300
ما معنى كلمة "imagine" في الجملة: Imagine a city without cars؟,يتخيل,الإنجليزي,300
ما معنى كلمة "influence" في الجملة: Friends can influence your decisions؟,يؤثر على,الإنجليزي,300
ما معنى كلمة "inform" في الجملة: Please inform the office if you will be absent؟,يبلغ أو يخبر رسميا,الإنجليزي,300
ما معنى كلمة "investigate" في الجملة: The police will investigate the accident؟,يحقق في,الإنجليزي,300
ما معنى كلمة "manage" في الجملة: She managed to finish the work before midnight؟,ينجح في أو يتمكن من,الإنجليزي,300
ما معنى كلمة "mention" في الجملة: He did not mention the price during the call؟,يذكر,الإنجليزي,300
ما معنى كلمة "organize" في الجملة: They organized the files by date؟,ينظم,الإنجليزي,300
ما معنى كلمة "participate" في الجملة: Many students participated in the competition؟,يشارك,الإنجليزي,300
ما معنى كلمة "perform" في الجملة: The singer performed well on stage؟,يؤدي أو يقدم عرضا,الإنجليزي,300
ما معنى كلمة "persuade" في الجملة: She persuaded him to try again؟,يقنع,الإنجليزي,300
ما معنى كلمة "prevent" في الجملة: Good planning can prevent many problems؟,يمنع,الإنجليزي,300
ما معنى كلمة "provide" في الجملة: The website provides free lessons؟,يوفر أو يقدم,الإنجليزي,300
ما معنى كلمة "recommend" في الجملة: I recommend this book for beginners؟,يوصي أو ينصح,الإنجليزي,300
ما معنى كلمة "reduce" في الجملة: We need to reduce the number of mistakes؟,يقلل,الإنجليزي,300
ما معنى كلمة "refuse" في الجملة: He refused to discuss the problem؟,يرفض,الإنجليزي,300
ما معنى كلمة "release" في الجملة: The company will release a new update next week؟,يطلق أو يصدر,الإنجليزي,300
ما معنى كلمة "replace" في الجملة: We need to replace the broken screen؟,يستبدل,الإنجليزي,300
ما معنى كلمة "request" في الجملة: You can request more information by email؟,يطلب رسميا,الإنجليزي,300
ما معنى كلمة "resolve" في الجملة: They resolved the issue after a short meeting؟,يحل مشكلة,الإنجليزي,300
ما معنى كلمة "respond" في الجملة: Please respond to the message today؟,يرد أو يستجيب,الإنجليزي,300
ما معنى كلمة "review" في الجملة: Review your notes before the exam؟,يراجع,الإنجليزي,300
ما معنى كلمة "select" في الجملة: Select the best answer from the list؟,يختار أو يحدد,الإنجليزي,300
ما معنى كلمة "separate" في الجملة: Separate the important papers from the old ones؟,يفصل,الإنجليزي,300
ما معنى كلمة "struggle" في الجملة: Many beginners struggle with pronunciation؟,يعاني أو يجد صعوبة,الإنجليزي,300
ما معنى كلمة "submit" في الجملة: Submit your homework before Friday؟,يسلم أو يقدم,الإنجليزي,300
ما معنى كلمة "support" في الجملة: The data supports our idea؟,يدعم,الإنجليزي,300
ما معنى كلمة "treat" في الجملة: The doctor treated the patient carefully؟,يعالج,الإنجليزي,300
ما معنى كلمة "trustworthy" في الجملة: We need a trustworthy person to keep the documents؟,جدير بالثقة,الإنجليزي,300
ما معنى كلمة "volunteer" في الجملة: She volunteered to help clean the beach؟,يتطوع,الإنجليزي,300
ما معنى كلمة "witness" في الجملة: A witness saw what happened in the street؟,شاهد,الإنجليزي,300
ما معنى كلمة "worthwhile" في الجملة: The course was difficult but worthwhile؟,يستحق الجهد أو مفيد,الإنجليزي,300
ما معنى كلمة "accurately" في الجملة: Please measure the distance accurately؟,بدقة,الإنجليزي,300
ما معنى كلمة "briefly" في الجملة: He briefly explained the plan before leaving؟,باختصار,الإنجليزي,300
ما معنى كلمة "carelessly" في الجملة: He carelessly deleted the wrong file؟,بإهمال,الإنجليزي,300
ما معنى كلمة "successfully" في الجملة: They successfully completed the project؟,بنجاح,الإنجليزي,300
ما معنى كلمة "seriously" في الجملة: You should take this warning seriously؟,بجدية,الإنجليزي,300
ما معنى كلمة "nearly" في الجملة: I nearly missed the train this morning؟,كاد أن أو تقريبا,الإنجليزي,300
ما معنى كلمة "hardly" في الجملة: I could hardly hear him because of the noise؟,بالكاد,الإنجليزي,300

ما معنى phrasal verb "bring back" في الجملة: This song brings back memories of my childhood؟,يعيد إلى الذاكرة,الإنجليزي,300
ما معنى phrasal verb "call back" في الجملة: I will call you back after the meeting؟,يتصل لاحقا,الإنجليزي,300
ما معنى phrasal verb "check in" في الجملة: We need to check in at the hotel before six؟,يسجل الوصول,الإنجليزي,300
ما معنى phrasal verb "check out" في الجملة: We checked out of the hotel early in the morning؟,يغادر الفندق أو يسجل الخروج,الإنجليزي,300
ما معنى phrasal verb "come in" في الجملة: Please come in and sit down؟,يدخل,الإنجليزي,300
ما معنى phrasal verb "come out" في الجملة: The new movie will come out next Friday؟,يصدر أو يظهر,الإنجليزي,300
ما معنى phrasal verb "fall behind" في الجملة: He fell behind in math after missing two weeks of school؟,يتأخر عن المستوى,الإنجليزي,300
ما معنى phrasal verb "get away" في الجملة: We want to get away for a quiet weekend؟,يذهب بعيدا للراحة,الإنجليزي,300
ما معنى phrasal verb "get in" في الجملة: What time did the train get in yesterday؟,يصل,الإنجليزي,300
ما معنى phrasal verb "get off" في الجملة: We got off the bus near the museum؟,ينزل من وسيلة نقل,الإنجليزي,300
ما معنى phrasal verb "get on" في الجملة: The children got on the bus quickly؟,يركب وسيلة نقل,الإنجليزي,300
ما معنى phrasal verb "give in" في الجملة: After a long discussion he finally gave in؟,يستسلم أو يوافق تحت ضغط,الإنجليزي,300
ما معنى phrasal verb "go ahead" في الجملة: You can go ahead and start without me؟,يبدأ أو يتابع,الإنجليزي,300
ما معنى phrasal verb "grow up" في الجملة: She grew up in a small village near the sea؟,يكبر أو ينشأ,الإنجليزي,300
ما معنى phrasal verb "hand in" في الجملة: Please hand in your homework before leaving؟,يسلم,الإنجليزي,300
ما معنى phrasal verb "hold back" في الجملة: Fear should not hold you back from trying؟,يمنع أو يعيق,الإنجليزي,300
ما معنى phrasal verb "keep away" في الجملة: Keep away from the broken glass؟,يبتعد عن,الإنجليزي,300
ما معنى phrasal verb "let down" في الجملة: I do not want to let my team down؟,يخذل,الإنجليزي,300
ما معنى phrasal verb "look out" في الجملة: Look out because the floor is wet؟,ينتبه أو يحذر,الإنجليزي,300
ما معنى phrasal verb "pass away" في الجملة: Her grandfather passed away last year؟,يتوفى,الإنجليزي,300
ما معنى idiom "a matter of time" في الجملة: With enough practice it is only a matter of time before you improve؟,مسألة وقت فقط,الإنجليزي,300
ما معنى idiom "at risk" في الجملة: Without quick action the project is at risk؟,في خطر,الإنجليزي,300
ما معنى idiom "back and forth" في الجملة: We sent emails back and forth all morning؟,ذهابا وإيابا أو تكرارا,الإنجليزي,300
ما معنى idiom "behind schedule" في الجملة: The construction work is behind schedule؟,متأخر عن الجدول,الإنجليزي,300
ما معنى idiom "by heart" في الجملة: She knows the poem by heart؟,عن ظهر قلب,الإنجليزي,300
ما معنى idiom "face to face" في الجملة: I prefer to discuss serious problems face to face؟,وجها لوجه,الإنجليزي,300
ما معنى idiom "for a while" في الجملة: I have not seen him for a while؟,لمدة من الوقت,الإنجليزي,300
ما معنى idiom "from scratch" في الجملة: They built the website from scratch؟,من الصفر,الإنجليزي,300
ما معنى idiom "in detail" في الجملة: The teacher explained the answer in detail؟,بالتفصيل,الإنجليزي,300
ما معنى idiom "in person" في الجملة: You must sign the paper in person؟,شخصيا,الإنجليزي,300
ما معنى idiom "in progress" في الجملة: The repair work is still in progress؟,قيد التنفيذ,الإنجليزي,300
ما معنى idiom "in public" في الجملة: He feels nervous when speaking in public؟,أمام الناس أو علنا,الإنجليزي,300
ما معنى idiom "in return" في الجملة: She helped me and asked for nothing in return؟,بالمقابل,الإنجليزي,300
ما معنى idiom "in shape" في الجملة: He exercises every day to stay in shape؟,بلياقة جيدة,الإنجليزي,300
ما معنى idiom "in touch" في الجملة: We stayed in touch after graduation؟,على تواصل,الإنجليزي,300
ما معنى idiom "just in case" في الجملة: Take an umbrella just in case it rains؟,احتياطا,الإنجليزي,300
ما معنى idiom "on average" في الجملة: On average I study English for one hour a day؟,في المتوسط,الإنجليزي,300
ما معنى idiom "on sale" في الجملة: These shoes are on sale this week؟,معروض للبيع بسعر مخفض,الإنجليزي,300
ما معنى idiom "out of date" في الجملة: This information is out of date؟,قديم أو غير محدث,الإنجليزي,300
ما معنى idiom "up to date" في الجملة: Keep your software up to date؟,محدث أو حديث,الإنجليزي,300
ما معنى كلمة "access" في الجملة: Students have access to the online library؟,إمكانية الوصول,الإنجليزي,300
ما معنى كلمة "analyze" في الجملة: We need to analyze the results carefully؟,يحلل,الإنجليزي,300
ما معنى كلمة "aware" في الجملة: Are you aware of the new rules؟,مدرك أو على علم,الإنجليزي,300
ما معنى كلمة "beneficial" في الجملة: Regular reading is beneficial for vocabulary؟,مفيد,الإنجليزي,300
ما معنى كلمة "capable" في الجملة: She is capable of leading the team؟,قادر,الإنجليزي,300
ما معنى كلمة "combine" في الجملة: The app combines learning and games؟,يجمع بين,الإنجليزي,300
ما معنى كلمة "complex" في الجملة: This is a complex problem with many causes؟,معقد,الإنجليزي,300
ما معنى كلمة "conclusion" في الجملة: The conclusion of the report was clear؟,استنتاج أو خاتمة,الإنجليزي,300
ما معنى كلمة "connection" في الجملة: There is a strong connection between sleep and focus؟,علاقة أو اتصال,الإنجليزي,300
ما معنى كلمة "consistent" في الجملة: Her work is consistent and reliable؟,ثابت المستوى أو منتظم,الإنجليزي,300
ما معنى كلمة "constant" في الجملة: The constant noise made it hard to study؟,مستمر أو دائم,الإنجليزي,300
ما معنى كلمة "contribute" في الجملة: Everyone should contribute to the group project؟,يساهم,الإنجليزي,300
ما معنى كلمة "cooperate" في الجملة: The two teams need to cooperate to finish on time؟,يتعاون,الإنجليزي,300
ما معنى كلمة "critical" في الجملة: Timing is critical in this experiment؟,مهم جدا أو حاسم,الإنجليزي,300
ما معنى كلمة "debate" في الجملة: The students had a debate about online learning؟,نقاش أو مناظرة,الإنجليزي,300
ما معنى كلمة "define" في الجملة: Can you define this word in simple English؟,يعرف أو يحدد معنى,الإنجليزي,300
ما معنى كلمة "demand" في الجملة: There is high demand for skilled engineers؟,طلب أو حاجة كبيرة,الإنجليزي,300
ما معنى كلمة "demonstrate" في الجملة: The teacher demonstrated how to use the tool؟,يوضح عمليا,الإنجليزي,300
ما معنى كلمة "dependable" في الجملة: He is dependable and always finishes his tasks؟,يمكن الاعتماد عليه,الإنجليزي,300
ما معنى كلمة "deserve" في الجملة: She deserves praise for her hard work؟,يستحق,الإنجليزي,300
ما معنى كلمة "detect" في الجملة: The system can detect errors automatically؟,يكتشف أو يرصد,الإنجليزي,300
ما معنى كلمة "discuss" في الجملة: We will discuss the plan after lunch؟,يناقش,الإنجليزي,300
ما معنى كلمة "distracted" في الجملة: He was distracted by his phone during class؟,مشتت الانتباه,الإنجليزي,300
ما معنى كلمة "divide" في الجملة: The teacher divided the class into four groups؟,يقسم,الإنجليزي,300
ما معنى كلمة "encounter" في الجملة: You may encounter problems when installing the program؟,يواجه أو يصادف,الإنجليزي,300
ما معنى كلمة "environmental" في الجملة: The company supports environmental projects؟,بيئي,الإنجليزي,300
ما معنى كلمة "evaluate" في الجملة: The manager will evaluate our performance؟,يقيم,الإنجليزي,300
ما معنى كلمة "examine" في الجملة: The doctor examined the patient carefully؟,يفحص,الإنجليزي,300
ما معنى كلمة "expand" في الجملة: The company plans to expand into new markets؟,يتوسع,الإنجليزي,300
ما معنى كلمة "explanation" في الجملة: Her explanation made the lesson easier؟,شرح أو تفسير,الإنجليزي,300
ما معنى كلمة "feature" في الجملة: The new phone has a useful security feature؟,ميزة أو خاصية,الإنجليزي,300
ما معنى كلمة "feedback" في الجملة: The teacher gave us helpful feedback on our essays؟,ملاحظات أو تقييم,الإنجليزي,300
ما معنى كلمة "function" في الجملة: What is the main function of this button؟,وظيفة,الإنجليزي,300
ما معنى كلمة "generate" في الجملة: The program can generate reports automatically؟,ينشئ أو يولد,الإنجليزي,300
ما معنى كلمة "highlight" في الجملة: The report highlights the main risks؟,يسلط الضوء على,الإنجليزي,300
ما معنى كلمة "impact" في الجملة: Social media has a strong impact on teenagers؟,تأثير,الإنجليزي,300
ما معنى كلمة "indicate" في الجملة: Dark clouds indicate that it may rain؟,يشير إلى أو يدل على,الإنجليزي,300
ما معنى كلمة "industry" في الجملة: The car industry is changing quickly؟,صناعة أو قطاع,الإنجليزي,300
ما معنى كلمة "initial" في الجملة: The initial plan was simple but effective؟,أولي أو مبدئي,الإنجليزي,300
ما معنى كلمة "instruction" في الجملة: Read each instruction before answering؟,تعليمة أو توجيه,الإنجليزي,300
ما معنى كلمة "lack" في الجملة: Lack of sleep can affect your focus؟,نقص أو قلة,الإنجليزي,300
ما معنى كلمة "maintain" في الجملة: You need to maintain your car regularly؟,يحافظ على أو يصون,الإنجليزي,300
ما معنى كلمة "monitor" في الجملة: Nurses monitor the patient's condition every hour؟,يراقب أو يتابع,الإنجليزي,300
ما معنى كلمة "negative" في الجملة: Try not to focus only on negative comments؟,سلبي,الإنجليزي,300
ما معنى كلمة "obvious" في الجملة: It was obvious that he was tired؟,واضح,الإنجليزي,300
ما معنى كلمة "obtain" في الجملة: You need to obtain permission before entering؟,يحصل على,الإنجليزي,300
ما معنى كلمة "outcome" في الجملة: The outcome of the meeting was positive؟,نتيجة,الإنجليزي,300
ما معنى كلمة "policy" في الجملة: The school has a strict attendance policy؟,سياسة أو نظام,الإنجليزي,300
ما معنى كلمة "predict" في الجملة: It is hard to predict the weather here؟,يتنبأ أو يتوقع,الإنجليزي,300
ما معنى كلمة "priority" في الجملة: Safety is our first priority؟,أولوية,الإنجليزي,300
ما معنى كلمة "procedure" في الجملة: Follow the correct procedure when using the machine؟,إجراء أو طريقة رسمية,الإنجليزي,300
ما معنى كلمة "purpose" في الجملة: The purpose of the survey is to understand customers؟,هدف أو غرض,الإنجليزي,300
ما معنى كلمة "reaction" في الجملة: His reaction to the news was surprising؟,رد فعل,الإنجليزي,300
ما معنى كلمة "recognize" في الجملة: I did not recognize him with his new haircut؟,يتعرف على,الإنجليزي,300
ما معنى كلمة "recover" في الجملة: It took her a month to recover from the illness؟,يتعافى,الإنجليزي,300
ما معنى كلمة "refer" في الجملة: The word they refers to the students in this sentence؟,يشير إلى,الإنجليزي,300
ما معنى كلمة "reject" في الجملة: The company rejected his application؟,يرفض,الإنجليزي,300
ما معنى كلمة "remove" في الجملة: Remove the old battery before installing the new one؟,يزيل أو ينزع,الإنجليزي,300
ما معنى كلمة "represent" في الجملة: This chart represents the sales for one year؟,يمثل,الإنجليزي,300
ما معنى كلمة "require" في الجملة: This task requires patience and focus؟,يتطلب,الإنجليزي,300
ما معنى كلمة "resource" في الجملة: The library is a useful resource for students؟,مورد أو مصدر مفيد,الإنجليزي,300
ما معنى كلمة "significant" في الجملة: There was a significant improvement in her speaking؟,كبير أو ملحوظ,الإنجليزي,300
ما معنى كلمة "strategy" في الجملة: We need a new strategy to attract customers؟,استراتيجية أو خطة,الإنجليزي,300
ما معنى كلمة "temporary" في الجملة: They found temporary housing after the storm؟,مؤقت,الإنجليزي,300
ما معنى كلمة "trend" في الجملة: Online learning has become a popular trend؟,اتجاه أو موضة,الإنجليزي,300

ما معنى phrasal verb "point out" في الجملة: The teacher pointed out three mistakes in my essay؟,يشير إلى أو يوضح,الإنجليزي,300
ما معنى phrasal verb "sort out" في الجملة: We need to sort out this problem before Friday؟,يحل أو يرتب مشكلة,الإنجليزي,300
ما معنى phrasal verb "rule out" في الجملة: The doctor ruled out a serious illness after the tests؟,يستبعد,الإنجليزي,300
ما معنى phrasal verb "carry out" في الجملة: The team carried out the experiment carefully؟,ينفذ أو يجري,الإنجليزي,300
ما معنى phrasal verb "go through" في الجملة: She went through a difficult time last year؟,يمر بتجربة صعبة,الإنجليزي,300
ما معنى phrasal verb "get through" في الجملة: I finally got through the long report؟,ينهي بصعوبة أو ينجز,الإنجليزي,300
ما معنى phrasal verb "look back on" في الجملة: He looks back on his school days with happiness؟,يتذكر الماضي,الإنجليزي,300
ما معنى phrasal verb "cut off" في الجملة: The village was cut off after the heavy snow؟,يعزل أو يقطع الاتصال,الإنجليزي,300
ما معنى phrasal verb "leave out" في الجملة: Do not leave out any important details؟,يحذف أو يترك,الإنجليزي,300
ما معنى phrasal verb "read through" في الجملة: Read through the instructions before you start؟,يقرأ بالكامل وبانتباه,الإنجليزي,300
ما معنى phrasal verb "run away" في الجملة: The dog ran away when it heard the loud noise؟,يهرب,الإنجليزي,300
ما معنى phrasal verb "stand out" في الجملة: Her creative design stood out from the others؟,يتميز أو يبرز,الإنجليزي,300
ما معنى phrasal verb "team up" في الجملة: The two students teamed up for the science project؟,يتعاون أو يشكل فريقا,الإنجليزي,300
ما معنى phrasal verb "try out" في الجملة: I want to try out this new app؟,يجرب,الإنجليزي,300
ما معنى phrasal verb "turn into" في الجملة: The small idea turned into a successful business؟,يتحول إلى,الإنجليزي,300
ما معنى phrasal verb "use up" في الجملة: We used up all the paper during the activity؟,يستهلك بالكامل,الإنجليزي,300
ما معنى phrasal verb "watch out" في الجملة: Watch out for cars when you cross the road؟,ينتبه ويحذر,الإنجليزي,300
ما معنى phrasal verb "work on" في الجملة: She is working on improving her pronunciation؟,يعمل على أو يطور,الإنجليزي,300
ما معنى phrasal verb "write back" في الجملة: I emailed the company but they did not write back؟,يرد كتابة,الإنجليزي,300
ما معنى phrasal verb "zoom in" في الجملة: Zoom in to read the small text on the screen؟,يقرب الصورة,الإنجليزي,300
ما معنى idiom "a fresh start" في الجملة: Moving to a new city gave him a fresh start؟,بداية جديدة,الإنجليزي,300
ما معنى idiom "around the corner" في الجملة: The final exam is around the corner؟,قريب الحدوث,الإنجليزي,300
ما معنى idiom "at all costs" في الجملة: We must protect the data at all costs؟,بأي ثمن,الإنجليزي,300
ما معنى idiom "back to normal" في الجملة: After the storm life slowly went back to normal؟,عاد إلى الوضع الطبيعي,الإنجليزي,300
ما معنى idiom "better safe than sorry" في الجملة: Take a backup of the file better safe than sorry؟,الاحتياط أفضل من الندم,الإنجليزي,300
ما معنى idiom "do your best" في الجملة: Do your best even if the task is hard؟,ابذل أفضل ما لديك,الإنجليزي,300
ما معنى idiom "easy does it" في الجملة: Easy does it when you carry the glass box؟,تمهل وتعامل بحذر,الإنجليزي,300
ما معنى idiom "for good" في الجملة: He decided to leave the company for good؟,نهائيا,الإنجليزي,300
ما معنى idiom "give someone a hand" في الجملة: Can you give me a hand with these boxes؟,يساعد,الإنجليزي,300
ما معنى idiom "have no idea" في الجملة: I have no idea where I left my keys؟,لا يعرف إطلاقا,الإنجليزي,300
ما معنى idiom "in a good mood" في الجملة: She was in a good mood after hearing the news؟,في مزاج جيد,الإنجليزي,300
ما معنى idiom "in a bad mood" في الجملة: He was in a bad mood because he missed the bus؟,في مزاج سيئ,الإنجليزي,300
ما معنى idiom "in no time" في الجملة: With this tool you can finish the task in no time؟,بسرعة كبيرة,الإنجليزي,300
ما معنى idiom "it depends" في الجملة: It depends on how much time we have؟,الأمر يعتمد على الظروف,الإنجليزي,300
ما معنى idiom "keep in mind" في الجملة: Keep in mind that the office closes early today؟,ضع في اعتبارك,الإنجليزي,300
ما معنى idiom "make a difference" في الجملة: Small changes can make a difference in your health؟,يحدث فرقا,الإنجليزي,300
ما معنى idiom "more or less" في الجملة: The two designs are more or less the same؟,تقريبا,الإنجليزي,300
ما معنى idiom "no doubt" في الجملة: No doubt this is the best option for us؟,بلا شك,الإنجليزي,300
ما معنى idiom "off the top of my head" في الجملة: Off the top of my head I can name five examples؟,من الذاكرة بدون تحضير,الإنجليزي,300
ما معنى idiom "on a budget" في الجملة: We are traveling on a budget this summer؟,بميزانية محدودة,الإنجليزي,300
ما معنى كلمة "alternative" في الجملة: We need an alternative plan in case it rains؟,بديل,الإنجليزي,300
ما معنى كلمة "annual" في الجملة: The company holds an annual meeting every December؟,سنوي,الإنجليزي,300
ما معنى كلمة "assistance" في الجملة: Please ask the staff for assistance if needed؟,مساعدة,الإنجليزي,300
ما معنى كلمة "benefit" في الجملة: The main benefit of this method is speed؟,فائدة,الإنجليزي,300
ما معنى كلمة "candidate" في الجملة: She is a strong candidate for the job؟,مرشح,الإنجليزي,300
ما معنى كلمة "capacity" في الجملة: The hall has a capacity of two hundred people؟,سعة أو قدرة استيعاب,الإنجليزي,300
ما معنى كلمة "circumstance" في الجملة: We may change the plan depending on the circumstance؟,ظرف أو حالة,الإنجليزي,300
ما معنى كلمة "commitment" في الجملة: Success requires commitment and patience؟,التزام,الإنجليزي,300
ما معنى كلمة "competition" في الجملة: The competition between the teams was strong؟,منافسة,الإنجليزي,300
ما معنى كلمة "component" في الجملة: The battery is an important component of the device؟,مكون أو جزء,الإنجليزي,300
ما معنى كلمة "concept" في الجملة: The teacher explained the concept with examples؟,مفهوم,الإنجليزي,300
ما معنى كلمة "conflict" في الجملة: There was a conflict between the two schedules؟,تعارض أو خلاف,الإنجليزي,300
ما معنى كلمة "consequence" في الجملة: Every decision has a consequence؟,نتيجة أو عاقبة,الإنجليزي,300
ما معنى كلمة "consumer" في الجملة: The new law protects the consumer؟,مستهلك,الإنجليزي,300
ما معنى كلمة "criteria" في الجملة: The judges used clear criteria to choose the winner؟,معايير,الإنجليزي,300
ما معنى كلمة "decline" في الجملة: Sales began to decline after the price increase؟,ينخفض أو يتراجع,الإنجليزي,300
ما معنى كلمة "definitely" في الجملة: I will definitely attend the workshop؟,بالتأكيد,الإنجليزي,300
ما معنى كلمة "device" في الجملة: This device measures temperature accurately؟,جهاز,الإنجليزي,300
ما معنى كلمة "efficiently" في الجملة: The team worked efficiently and finished early؟,بكفاءة,الإنجليزي,300
ما معنى كلمة "estimate" في الجملة: We need to estimate the total cost before starting؟,يقدر تقريبا,الإنجليزي,300
ما معنى كلمة "evident" في الجملة: It was evident that she had practiced a lot؟,واضح,الإنجليزي,300
ما معنى كلمة "factor" في الجملة: Sleep is an important factor in concentration؟,عامل,الإنجليزي,300
ما معنى كلمة "finance" في الجملة: He studied finance at university؟,تمويل أو مالية,الإنجليزي,300
ما معنى كلمة "goal" في الجملة: The main goal is to reduce waste؟,هدف,الإنجليزي,300
ما معنى كلمة "income" في الجملة: His monthly income increased after the promotion؟,دخل,الإنجليزي,300
ما معنى كلمة "instance" في الجملة: Give me one instance where this rule applies؟,مثال أو حالة,الإنجليزي,300
ما معنى كلمة "issue" في الجملة: We discussed the issue during the meeting؟,مسألة أو مشكلة,الإنجليزي,300
ما معنى كلمة "layout" في الجملة: The layout of the website is simple and clear؟,تصميم أو ترتيب,الإنجليزي,300
ما معنى كلمة "limit" في الجملة: There is a limit to how much weight the shelf can hold؟,حد,الإنجليزي,300
ما معنى كلمة "maintenance" في الجملة: Regular maintenance keeps the machine working well؟,صيانة,الإنجليزي,300
ما معنى كلمة "manual" في الجملة: Read the manual before using the machine؟,دليل الاستخدام,الإنجليزي,300
ما معنى كلمة "objective" في الجملة: The objective of the lesson is to improve speaking؟,هدف,الإنجليزي,300
ما معنى كلمة "ordinary" في الجملة: The meal looked ordinary but tasted amazing؟,عادي,الإنجليزي,300
ما معنى كلمة "participant" في الجملة: Each participant received a certificate؟,مشارك,الإنجليزي,300
ما معنى كلمة "percentage" في الجملة: A large percentage of students passed the exam؟,نسبة مئوية,الإنجليزي,300
ما معنى كلمة "permission" في الجملة: You need permission to use this room؟,إذن أو تصريح,الإنجليزي,300
ما معنى كلمة "potential" في الجملة: This idea has great potential؟,إمكانية أو قابلية للنجاح,الإنجليزي,300
ما معنى كلمة "practicality" في الجملة: We discussed the practicality of the new plan؟,مدى العملية أو قابلية التطبيق,الإنجليزي,300
ما معنى كلمة "prediction" في الجملة: His prediction about the result was correct؟,تنبؤ,الإنجليزي,300
ما معنى كلمة "preference" في الجملة: Everyone has a different preference for food؟,تفضيل,الإنجليزي,300
ما معنى كلمة "principle" في الجملة: Honesty is an important principle in our work؟,مبدأ,الإنجليزي,300
ما معنى كلمة "profit" في الجملة: The shop made a good profit this month؟,ربح,الإنجليزي,300
ما معنى كلمة "proposal" في الجملة: The committee accepted her project proposal؟,مقترح,الإنجليزي,300
ما معنى كلمة "purchase" في الجملة: Keep the receipt after every purchase؟,عملية شراء,الإنجليزي,300
ما معنى كلمة "range" في الجملة: The store offers a wide range of products؟,نطاق أو مجموعة,الإنجليزي,300
ما معنى كلمة "refund" في الجملة: I asked for a refund because the product was broken؟,استرداد المال,الإنجليزي,300
ما معنى كلمة "relevant" في الجملة: Please include only relevant information in your answer؟,ذو صلة أو متعلق بالموضوع,الإنجليزي,300
ما معنى كلمة "reminder" في الجملة: I set a reminder for the meeting؟,تذكير,الإنجليزي,300
ما معنى كلمة "reputation" في الجملة: The restaurant has a good reputation for service؟,سمعة,الإنجليزي,300
ما معنى كلمة "reservation" في الجملة: We made a reservation at the hotel؟,حجز,الإنجليزي,300
ما معنى كلمة "risk" في الجملة: There is a risk of losing data without backups؟,خطر أو احتمال ضرر,الإنجليزي,300
ما معنى كلمة "section" في الجملة: Read the first section of the article؟,قسم أو جزء,الإنجليزي,300
ما معنى كلمة "source" في الجملة: What is the source of this information؟,مصدر,الإنجليزي,300
ما معنى كلمة "statement" في الجملة: His statement was short and clear؟,تصريح أو عبارة,الإنجليزي,300
ما معنى كلمة "structure" في الجملة: The structure of the essay is clear؟,بنية أو تنظيم,الإنجليزي,300
ما معنى كلمة "summary" في الجملة: Write a short summary of the story؟,ملخص,الإنجليزي,300
ما معنى كلمة "target" في الجملة: Our target is to finish fifty questions today؟,هدف محدد,الإنجليزي,300
ما معنى كلمة "task" في الجملة: This task requires focus and patience؟,مهمة,الإنجليزي,300
ما معنى كلمة "technical" في الجملة: The article uses some technical terms؟,تقني أو فني,الإنجليزي,300
ما معنى كلمة "topic" في الجملة: The topic of today's lesson is travel؟,موضوع,الإنجليزي,300
ما معنى كلمة "transfer" في الجملة: You can transfer the file to another computer؟,ينقل,الإنجليزي,300
ما معنى كلمة "version" في الجملة: This is the latest version of the app؟,نسخة أو إصدار,الإنجليزي,300
ما معنى كلمة "weakness" في الجملة: Speaking is my main weakness in English؟,نقطة ضعف,الإنجليزي,300

أكمل التعبير الصحيح في الجملة: After months of arguing they finally decided to bury the ____ and work together؟,hatchet بمعنى ينسون الخلاف ويتصالحون,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He looked calm but I could tell he was walking on ____ around his strict manager؟,eggshells بمعنى يتصرف بحذر شديد,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The company tried to sweep the problem under the ____ instead of solving it؟,rug بمعنى يخفي المشكلة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She got promoted after years of proving that she could hold her ____؟,own بمعنى تثبت قدرتها بنفسها,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: Do not count your chickens before they ____؟,hatch بمعنى لا تستبق النتائج,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His apology sounded nice but actions speak louder than ____؟,words بمعنى الأفعال أهم من الكلام,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: When the scandal became public the CEO had to face the ____؟,music بمعنى يواجه العواقب,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: I did not want to make waves so I kept my opinion to ____؟,myself بمعنى احتفظت برأيي لنفسي,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The new employee was thrown in at the deep ____ on his first day؟,end بمعنى وُضع في موقف صعب مباشرة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She kept changing her story so I smelled a ____؟,rat بمعنى شعرت أن هناك شيئا مريبا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The project failed because too many people were cutting ____؟,corners بمعنى يختصرون العمل بطريقة سيئة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He always takes credit for other people's work and it really gets under my ____؟,skin بمعنى يزعجني جدا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The manager told us to get the ball ____ before the deadline؟,rolling بمعنى نبدأ العمل,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: I was skeptical at first but the evidence tipped the ____؟,scales بمعنى رجح الكفة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: You should not put all your eggs in one ____؟,basket بمعنى لا تعتمد على خيار واحد فقط,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The negotiations hit a ____ when neither side accepted the offer؟,wall بمعنى وصلت لطريق مسدود,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He tried to explain but he only made matters ____؟,worse بمعنى زاد الوضع سوءا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She refused to help and left us high and ____؟,dry بمعنى تركتنا في موقف صعب بدون مساعدة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His plan sounds good but the devil is in the ____؟,details بمعنى المشكلة في التفاصيل الدقيقة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We need to read between the ____ to understand what he really means؟,lines بمعنى نفهم المعنى الخفي,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: I will give him the benefit of the ____ this time؟,doubt بمعنى أصدقه رغم الشك,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The politician tried to dodge the ____ during the interview؟,question بمعنى يتهرب من السؤال,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: Her comments added fuel to the ____ and made the argument worse؟,fire بمعنى زادت المشكلة اشتعالا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We were not ready so the announcement caught us off ____؟,guard بمعنى فاجأنا بدون استعداد,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He has a tendency to jump to ____ without checking the facts؟,conclusions بمعنى يتسرع في الحكم,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The report helped put things into ____؟,perspective بمعنى يوضح الصورة بشكل متوازن,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: After losing the contract the team had to go back to the drawing ____؟,board بمعنى يبدأ التخطيط من جديد,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She took his support for ____ and never thanked him؟,granted بمعنى اعتبرته مضمونا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The small mistake snowballed into a major ____؟,crisis بمعنى تحولت إلى أزمة كبيرة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: I do not want to burn my ____ with my old company؟,bridges بمعنى أقطع علاقاتي بشكل سيئ,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The deal is not final yet so do not get your hopes ____؟,up بمعنى لا ترفع توقعاتك كثيرا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He tried to play it ____ after making a serious mistake؟,cool بمعنى يتظاهر بالهدوء,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The new evidence cast doubt ____ his original story؟,on بمعنى جعل قصته محل شك,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The committee decided to phase ____ the old system gradually؟,out بمعنى يلغي تدريجيا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We need to narrow ____ the list to three candidates؟,down بمعنى يقلص الخيارات,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She managed to pull ____ a difficult presentation with little preparation؟,off بمعنى تنجح في إنجاز شيء صعب,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The company had to lay ____ several workers after the losses؟,off بمعنى يفصل من العمل,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His argument does not hold ____ under careful analysis؟,up بمعنى لا يصمد أو لا يكون مقنعا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The lawyer tried to poke holes ____ the witness's story؟,in بمعنى يكشف نقاط الضعف,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We should not brush ____ his concerns as unimportant؟,off بمعنى يتجاهل باستخفاف,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The team needs to iron ____ a few issues before launch؟,out بمعنى يحل التفاصيل والمشاكل الصغيرة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She backed ____ of the agreement at the last minute؟,out بمعنى انسحبت من الاتفاق,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He came ____ as rude although he did not mean to؟,across بمعنى بدا للآخرين,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The new rule brought ____ a lot of confusion؟,about بمعنى تسبب في,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: I could not put my finger ____ what felt wrong؟,on بمعنى أحدد بالضبط,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The speaker drifted ____ topic several times؟,off بمعنى خرج عن الموضوع,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The plan fell ____ because nobody followed through؟,apart بمعنى فشل أو انهار,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The evidence does not add ____ to a convincing case؟,up بمعنى لا يبدو منطقيا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We need to step ____ and look at the bigger picture؟,back بمعنى نتراجع ونفكر بهدوء,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He tried to talk me ____ quitting my job؟,into بمعنى يقنعني أن أفعل,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She talked him ____ making a risky decision؟,out of بمعنى أقنعته ألا يفعل,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The manager cracked ____ on employees who arrived late؟,down بمعنى اتخذ إجراءات صارمة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He brushed ____ the criticism and continued his work؟,aside بمعنى تجاهل النقد,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The issue boils ____ to poor communication؟,down بمعنى يتلخص في,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We need to follow ____ on every customer complaint؟,up بمعنى نتابع بعد ذلك,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She owned ____ to her mistake during the meeting؟,up بمعنى اعترفت بالخطأ,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The company is struggling to keep ____ with demand؟,up بمعنى يواكب,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He tried to pass ____ the fake watch as original؟,off بمعنى يقدمه على أنه حقيقي,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The evidence points ____ a different conclusion؟,to بمعنى يشير إلى,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We have to account ____ every missing item؟,for بمعنى يفسر أو يبرر,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The results line ____ with our expectations؟,up بمعنى تتوافق مع,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: He lashed ____ at his coworkers after the stressful meeting؟,out بمعنى انفجر غضبا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: She is reluctant ____ accept the offer without more details؟,to بمعنى مترددة في,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: His constant criticism began to ____ her confidence؟,undermine بمعنى يضعف تدريجيا,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The results were too ____ to ignore؟,significant بمعنى مهم أو ملحوظ,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The explanation was clear but not entirely ____؟,accurate بمعنى دقيق,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: She remained ____ despite the pressure from her team؟,composed بمعنى هادئة ومتماسكة,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: His answer was vague and lacked ____؟,substance بمعنى مضمون أو قيمة حقيقية,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The company needs to ____ its strategy before entering the market؟,revise بمعنى يراجع ويعدل,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The judge said the evidence was not ____ enough؟,conclusive بمعنى حاسم أو قاطع,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: Her argument was persuasive but slightly ____؟,biased بمعنى منحاز,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The instructions were ____ and caused confusion؟,ambiguous بمعنى غامضة أو تحتمل أكثر من معنى,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The decision had ____ consequences for the whole team؟,serious بمعنى عواقب مهمة أو خطيرة,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: He showed ____ by admitting that he was wrong؟,integrity بمعنى نزاهة أو أمانة,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The project is ____ on receiving funding next month؟,dependent بمعنى معتمد على,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: His comments were ____ to the topic and helped the discussion؟,relevant بمعنى مرتبطة بالموضوع,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The old method is no longer ____ in modern workplaces؟,applicable بمعنى قابل للتطبيق,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The team made a ____ effort to finish before midnight؟,collective بمعنى جماعي أو مشترك,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The witness gave a ____ account of what happened؟,detailed بمعنى مفصل,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: His behavior was ____ with the company values؟,inconsistent بمعنى غير متوافق,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The new evidence helped ____ the original theory؟,confirm بمعنى يؤكد,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The problem is difficult but not ____؟,insurmountable بمعنى مستحيل التغلب عليه,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: She gave a ____ response instead of answering directly؟,diplomatic بمعنى لبق وحذر,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The sudden change caused ____ among the employees؟,uncertainty بمعنى عدم يقين,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: His refusal to cooperate was a major ____؟,obstacle بمعنى عقبة,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: We need a more ____ approach to solve this issue؟,systematic بمعنى منظم ومنهجي,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: Her tone was calm but slightly ____؟,sarcastic بمعنى ساخر,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The data is useful but not ____ enough for a final decision؟,sufficient بمعنى كاف,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The new policy may ____ small businesses if applied too quickly؟,burden بمعنى يثقل أو يضغط على,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The speaker tried to ____ the importance of teamwork؟,emphasize بمعنى يؤكد على,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The two reports ____ each other and cannot both be true؟,contradict بمعنى يتعارضان,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: His apology seemed ____ because he repeated the same mistake؟,insincere بمعنى غير صادق,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The risk is low but still ____؟,present بمعنى موجود,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The manager asked for a ____ explanation of the delay؟,plausible بمعنى معقول أو قابل للتصديق,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: Her success was not accidental but the result of ____ effort؟,consistent بمعنى مستمر ومنتظم,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The plan is ambitious but ____ with enough resources؟,feasible بمعنى قابل للتنفيذ,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: He gave an answer that was technically correct but ____؟,misleading بمعنى مضلل,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The mistake was minor but it had a ____ effect on the final result؟,noticeable بمعنى ملحوظ,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The proposal needs more ____ before we can approve it؟,clarity بمعنى وضوح,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The argument was based on an ____ assumption؟,incorrect بمعنى افتراض خاطئ,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: She was ____ to share personal information with strangers؟,hesitant بمعنى مترددة,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The team reached a ____ after hours of discussion؟,compromise بمعنى حل وسط,الإنجليزي,500
أكمل الكلمة الصحيحة في الجملة: The evidence was ____ and did not support the claim؟,weak بمعنى ضعيف,الإنجليزي,500

أكمل المثل الصحيح في الجملة: What goes around comes ____؟,around بمعنى كما تدين تدان,الإنجليزي,500
ما معنى saying "What goes around comes around" في الجملة: He treated people badly and then lost their trust what goes around comes around؟,كما تدين تدان,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Actions speak louder than ____؟,words بمعنى الأفعال أقوى من الكلام,الإنجليزي,500
ما معنى saying "Actions speak louder than words" في الجملة: He promised to help but did nothing actions speak louder than words؟,الأفعال أهم من الوعود,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Better late than ____؟,never بمعنى أن تأتي متأخرا أفضل من ألا تأتي,الإنجليزي,500
ما معنى saying "Better late than never" في الجملة: She apologized after a year better late than never؟,التأخر أفضل من عدم الفعل نهائيا,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Honesty is the best ____؟,policy بمعنى الصراحة أفضل طريق,الإنجليزي,500
ما معنى saying "Honesty is the best policy" في الجملة: Tell the truth now honesty is the best policy؟,الصدق أفضل تصرف,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Practice makes ____؟,perfect بمعنى التدريب يؤدي إلى الإتقان,الإنجليزي,500
ما معنى saying "Practice makes perfect" في الجملة: Keep speaking English every day practice makes perfect؟,كثرة التدريب تجعلك أفضل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: No pain no ____؟,gain بمعنى لا مكسب بدون تعب,الإنجليزي,500
ما معنى saying "No pain no gain" في الجملة: Training is hard but no pain no gain؟,لا تحصل على نتيجة بدون جهد,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Time is ____؟,money بمعنى الوقت ثمين,الإنجليزي,500
ما معنى saying "Time is money" في الجملة: Do not waste the morning time is money؟,الوقت له قيمة كبيرة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Knowledge is ____؟,power بمعنى المعرفة قوة,الإنجليزي,500
ما معنى saying "Knowledge is power" في الجملة: Read more because knowledge is power؟,العلم يعطي قوة وفهما,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The early bird catches the ____؟,worm بمعنى من يبدأ مبكرا يفوز بالفرصة,الإنجليزي,500
ما معنى saying "The early bird catches the worm" في الجملة: Apply before everyone else the early bird catches the worm؟,المبادر يحصل على الفرصة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not judge a book by its ____؟,cover بمعنى لا تحكم على الشيء من مظهره,الإنجليزي,500
ما معنى saying "Do not judge a book by its cover" في الجملة: The old shop looks simple but sells great food do not judge a book by its cover؟,لا تحكم من الشكل الخارجي,الإنجليزي,500
أكمل المثل الصحيح في الجملة: When in Rome do as the Romans ____؟,do بمعنى احترم عادات المكان الذي أنت فيه,الإنجليزي,500
ما معنى saying "When in Rome do as the Romans do" في الجملة: Follow their customs when in Rome do as the Romans do؟,تصرف حسب عادات المكان,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Two heads are better than ____؟,one بمعنى رأيان أفضل من رأي واحد,الإنجليزي,500
ما معنى saying "Two heads are better than one" في الجملة: Let us solve it together two heads are better than one؟,التعاون يعطي أفكارا أفضل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Rome was not built in a ____؟,day بمعنى الإنجازات الكبيرة تحتاج وقتا,الإنجليزي,500
ما معنى saying "Rome was not built in a day" في الجملة: Do not rush your progress Rome was not built in a day؟,النجاح الكبير يحتاج صبرا ووقتا,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The grass is always greener on the other ____؟,side بمعنى الناس تظن أن حال غيرها أفضل,الإنجليزي,500
ما معنى saying "The grass is always greener on the other side" في الجملة: He thinks every other job is better the grass is always greener on the other side؟,نميل لاعتقاد أن حياة الآخرين أفضل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not put all your eggs in one ____؟,basket بمعنى لا تعتمد على خيار واحد فقط,الإنجليزي,500
ما معنى saying "Do not put all your eggs in one basket" في الجملة: Invest in different ideas do not put all your eggs in one basket؟,وزع المخاطر ولا تعتمد على شيء واحد,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A picture is worth a thousand ____؟,words بمعنى الصورة أبلغ من كلام كثير,الإنجليزي,500
ما معنى saying "A picture is worth a thousand words" في الجملة: Show them the chart a picture is worth a thousand words؟,الصورة تشرح أكثر من الكلام الطويل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not count your chickens before they ____؟,hatch بمعنى لا تفرح بالنتيجة قبل حدوثها,الإنجليزي,500
ما معنى saying "Do not count your chickens before they hatch" في الجملة: Wait until the deal is signed do not count your chickens before they hatch؟,لا تعتمد على نتيجة لم تحدث بعد,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Every cloud has a silver ____؟,lining بمعنى في كل محنة جانب إيجابي,الإنجليزي,500
ما معنى saying "Every cloud has a silver lining" في الجملة: Losing that job led him to a better one every cloud has a silver lining؟,حتى المشكلة قد تحمل خيرا,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Where there is a will there is a ____؟,way بمعنى من لديه إرادة يجد طريقة,الإنجليزي,500
ما معنى saying "Where there is a will there is a way" في الجملة: She studied at night and passed where there is a will there is a way؟,الإرادة القوية تجد الحل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: All that glitters is not ____؟,gold بمعنى ليس كل ما يلمع ذهبا,الإنجليزي,500
ما معنى saying "All that glitters is not gold" في الجملة: The offer looked perfect but had hidden fees all that glitters is not gold؟,المظهر الجميل لا يعني أن الشيء جيد,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Beggars cannot be ____؟,choosers بمعنى من يحتاج لا يبالغ في الاختيار,الإنجليزي,500
ما معنى saying "Beggars cannot be choosers" في الجملة: This is the only room available beggars cannot be choosers؟,عند قلة الخيارات لا يمكن التشدد,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Easy come easy ____؟,go بمعنى ما يأتي بسهولة يذهب بسهولة,الإنجليزي,500
ما معنى saying "Easy come easy go" في الجملة: He won money and spent it in one day easy come easy go؟,الشيء السهل الحصول قد يضيع بسرعة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Better safe than ____؟,sorry بمعنى الاحتياط أفضل من الندم,الإنجليزي,500
ما معنى saying "Better safe than sorry" في الجملة: Save a backup before updating better safe than sorry؟,خذ احتياطك حتى لا تندم,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Look before you ____؟,leap بمعنى فكر قبل أن تتصرف,الإنجليزي,500
ما معنى saying "Look before you leap" في الجملة: Read the contract first look before you leap؟,لا تتخذ قرارا قبل التفكير,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The pen is mightier than the ____؟,sword بمعنى الكلمة أقوى من السلاح,الإنجليزي,500
ما معنى saying "The pen is mightier than the sword" في الجملة: His article changed public opinion the pen is mightier than the sword؟,الفكر والكلام قد يكونان أقوى من القوة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Birds of a feather flock ____؟,together بمعنى المتشابهون يجتمعون,الإنجليزي,500
ما معنى saying "Birds of a feather flock together" في الجملة: All the creative students became friends birds of a feather flock together؟,الأشخاص المتشابهون ينجذبون لبعض,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A friend in need is a friend ____؟,indeed بمعنى الصديق الحقيقي يظهر وقت الشدة,الإنجليزي,500
ما معنى saying "A friend in need is a friend indeed" في الجملة: He helped me when everyone left a friend in need is a friend indeed؟,الصديق وقت الضيق,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Out of sight out of ____؟,mind بمعنى بعيد عن العين بعيد عن التفكير,الإنجليزي,500
ما معنى saying "Out of sight out of mind" في الجملة: I stopped using the app after hiding it out of sight out of mind؟,ما لا تراه غالبا تنساه,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Strike while the iron is ____؟,hot بمعنى استغل الفرصة في وقتها,الإنجليزي,500
ما معنى saying "Strike while the iron is hot" في الجملة: The client is interested now strike while the iron is hot؟,تحرك عندما تكون الفرصة مناسبة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The best of both ____؟,worlds بمعنى الجمع بين ميزتين,الإنجليزي,500
ما معنى saying "The best of both worlds" في الجملة: Working remotely with a good salary gives her the best of both worlds؟,الحصول على فائدتين في نفس الوقت,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A blessing in ____؟,disguise بمعنى خير مخفي داخل مشكلة,الإنجليزي,500
ما معنى saying "A blessing in disguise" في الجملة: Missing that train was a blessing in disguise because it broke down later؟,مشكلة ظاهرها سيئ لكنها تنتهي بخير,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The last ____؟,straw بمعنى آخر شيء يجعل الشخص لا يتحمل أكثر,الإنجليزي,500
ما معنى saying "The last straw" في الجملة: The third delay was the last straw for the customer؟,القشة التي قصمت ظهر البعير,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Once bitten twice ____؟,shy بمعنى من يتأذى مرة يصبح أكثر حذرا,الإنجليزي,500
ما معنى saying "Once bitten twice shy" في الجملة: After losing money in that deal he checks everything now once bitten twice shy؟,التجربة السيئة تجعل الشخص حذرا,الإنجليزي,500
أكمل المثل الصحيح في الجملة: You cannot have your cake and eat it ____؟,too بمعنى لا يمكنك جمع خيارين متناقضين,الإنجليزي,500
ما معنى saying "You cannot have your cake and eat it too" في الجملة: You want freedom and full control from others you cannot have your cake and eat it too؟,لا يمكنك الحصول على كل شيء في نفس الوقت,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Too many cooks spoil the ____؟,broth بمعنى كثرة المتدخلين تفسد العمل,الإنجليزي,500
ما معنى saying "Too many cooks spoil the broth" في الجملة: Ten people edited the same design and ruined it too many cooks spoil the broth؟,كثرة الآراء قد تفسد النتيجة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The squeaky wheel gets the ____؟,grease بمعنى من يشتكي يحصل على الاهتمام,الإنجليزي,500
ما معنى saying "The squeaky wheel gets the grease" في الجملة: He kept reporting the issue until they fixed it the squeaky wheel gets the grease؟,من يرفع صوته يحصل غالبا على الحل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Curiosity killed the ____؟,cat بمعنى الفضول الزائد قد يسبب مشكلة,الإنجليزي,500
ما معنى saying "Curiosity killed the cat" في الجملة: Stop opening private files curiosity killed the cat؟,الفضول في غير مكانه قد يضرك,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Necessity is the mother of ____؟,invention بمعنى الحاجة تدفع للاختراع,الإنجليزي,500
ما معنى saying "Necessity is the mother of invention" في الجملة: They built a cheap tool because they had no money necessity is the mother of invention؟,الحاجة تجعل الناس يبتكرون,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Blood is thicker than ____؟,water بمعنى رابطة العائلة أقوى,الإنجليزي,500
ما معنى saying "Blood is thicker than water" في الجملة: He chose to help his brother first blood is thicker than water؟,العائلة لها أولوية قوية,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A watched pot never ____؟,boils بمعنى الانتظار بقلق يجعل الوقت يبدو أطول,الإنجليزي,500
ما معنى saying "A watched pot never boils" في الجملة: Stop refreshing the page every second a watched pot never boils؟,الترقب المستمر يجعل الانتظار أصعب,الإنجليزي,500
أكمل المثل الصحيح في الجملة: There is no smoke without ____؟,fire بمعنى لا توجد شائعة غالبا بلا سبب,الإنجليزي,500
ما معنى saying "There is no smoke without fire" في الجملة: Everyone is talking about the problem there is no smoke without fire؟,وجود إشارات كثيرة يدل غالبا على سبب حقيقي,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The apple does not fall far from the ____؟,tree بمعنى الولد يشبه أهله,الإنجليزي,500
ما معنى saying "The apple does not fall far from the tree" في الجملة: He became a great mechanic like his father the apple does not fall far from the tree؟,الشخص غالبا يشبه والديه أو عائلته,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not bite the hand that ____ you؟,feeds بمعنى لا تؤذ من يساعدك,الإنجليزي,500
ما معنى saying "Do not bite the hand that feeds you" في الجملة: He insulted the person who gave him the job do not bite the hand that feeds you؟,لا تسيء لمن يدعمك,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Absence makes the heart grow ____؟,fonder بمعنى البعد يزيد الشوق,الإنجليزي,500
ما معنى saying "Absence makes the heart grow fonder" في الجملة: She missed her family more after moving abroad absence makes the heart grow fonder؟,البعد قد يزيد المحبة والاشتياق,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The customer is always ____؟,right بمعنى الزبون يجب أن يعامل كأنه على حق,الإنجليزي,500
ما معنى saying "The customer is always right" في الجملة: The shop replaced the product quickly because the customer is always right؟,خدمة الزبون يجب أن تكون أولوية,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Money does not grow on ____؟,trees بمعنى المال لا يأتي بسهولة,الإنجليزي,500
ما معنى saying "Money does not grow on trees" في الجملة: Stop buying things you do not need money does not grow on trees؟,لا تهدر المال لأنه صعب الكسب,الإنجليزي,500
أكمل المثل الصحيح في الجملة: There is no such thing as a free ____؟,lunch بمعنى لا شيء مجاني فعلا,الإنجليزي,500
ما معنى saying "There is no such thing as a free lunch" في الجملة: The free app collects your data there is no such thing as a free lunch؟,كل شيء له مقابل بطريقة ما,الإنجليزي,500
أكمل المثل الصحيح في الجملة: If it is not broken do not ____ it؟,fix بمعنى لا تغير شيئا يعمل جيدا,الإنجليزي,500
ما معنى saying "If it is not broken do not fix it" في الجملة: The system works well so if it is not broken do not fix it؟,لا تعبث بشيء ناجح بدون حاجة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: You reap what you ____؟,sow بمعنى تحصد ما تزرع,الإنجليزي,500
ما معنى saying "You reap what you sow" في الجملة: He studied seriously and passed you reap what you sow؟,نتائجك تأتي من أفعالك,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not make a mountain out of a ____؟,molehill بمعنى لا تضخم مشكلة صغيرة,الإنجليزي,500
ما معنى saying "Do not make a mountain out of a molehill" في الجملة: It is only a small mistake do not make a mountain out of a molehill؟,لا تكبر الموضوع أكثر من حجمه,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Let sleeping dogs ____؟,lie بمعنى لا تفتح مشكلة قديمة,الإنجليزي,500
ما معنى saying "Let sleeping dogs lie" في الجملة: Do not mention that old argument let sleeping dogs lie؟,اترك المشاكل القديمة بدون إثارتها,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Slow and steady wins the ____؟,race بمعنى الثبات والصبر يؤديان للنجاح,الإنجليزي,500
ما معنى saying "Slow and steady wins the race" في الجملة: Study a little every day slow and steady wins the race؟,الاستمرار الهادئ أفضل من العجلة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: When the going gets tough the tough get ____؟,going بمعنى الأقوياء يتحركون عند الصعوبات,الإنجليزي,500
ما معنى saying "When the going gets tough the tough get going" في الجملة: The deadline is hard but when the going gets tough the tough get going؟,وقت الشدة يظهر أصحاب العزيمة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Fortune favors the ____؟,bold بمعنى الحظ يساعد الشجعان,الإنجليزي,500
ما معنى saying "Fortune favors the bold" في الجملة: She took the risk and succeeded fortune favors the bold؟,الجرأة قد تجلب الفرص,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Great minds think ____؟,alike بمعنى العقول العظيمة تفكر بشكل متشابه,الإنجليزي,500
ما معنى saying "Great minds think alike" في الجملة: We both had the same idea great minds think alike؟,نقال عندما يفكر شخصان بنفس الطريقة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: If you play with fire you get ____؟,burned بمعنى من يخاطر بتهور يتأذى,الإنجليزي,500
ما معنى saying "If you play with fire you get burned" في الجملة: He kept lying to his boss if you play with fire you get burned؟,التصرف الخطير أو الخاطئ له عواقب,الإنجليزي,500

ما معنى كلمة "scrutinize" في الجملة: The auditor scrutinized every invoice before approving the payment؟,يفحص بدقة شديدة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The new policy opened the door ____ future reforms؟,to بمعنى مهد الطريق إلى,الإنجليزي,500
ما معنى saying "Do not throw the baby out with the bathwater" في الجملة: The system has problems but do not throw the baby out with the bathwater؟,لا تتخلص من الشيء المفيد بسبب عيوبه,الإنجليزي,500
ما معنى phrasal verb "phase out" في الجملة: The company will phase out old devices by the end of the year؟,يلغي تدريجيا,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A chain is only as strong as its weakest ____؟,link بمعنى قوة المجموعة تعتمد على أضعف جزء,الإنجليزي,500
ما معنى كلمة "meticulous" في الجملة: She is meticulous when checking legal documents؟,دقيق جدا ومنتبه للتفاصيل,الإنجليزي,500
ما معنى idiom "read the room" في الجملة: He kept joking during a serious meeting because he could not read the room؟,يفهم الجو والموقف حوله,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The manager asked us to flesh ____ the proposal before presenting it؟,out بمعنى يضيف تفاصيل ويطوره,الإنجليزي,500
ما معنى كلمة "obsolete" في الجملة: This software is obsolete and no longer receives updates؟,قديم ولم يعد مستخدما,الإنجليزي,500
ما معنى saying "The road to hell is paved with good intentions" في الجملة: His plan caused harm although he meant well the road to hell is paved with good intentions؟,النوايا الحسنة لا تكفي إذا كانت النتائج سيئة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: Her promotion came after years of paying her ____؟,dues بمعنى تعب واجتهد لفترة طويلة ليستحق النجاح,الإنجليزي,500
ما معنى كلمة "resilient" في الجملة: The team remained resilient after several failures؟,قادر على التعافي والصمود,الإنجليزي,500
ما معنى phrasal verb "zero in on" في الجملة: The investigation zeroed in on one suspicious transaction؟,يركز بدقة على,الإنجليزي,500
أكمل المثل الصحيح في الجملة: You can lead a horse to water but you cannot make it ____؟,drink بمعنى يمكنك النصح لكن لا تجبر الشخص على الاستفادة,الإنجليزي,500
ما معنى كلمة "contentious" في الجملة: The new tax law became a contentious topic in parliament؟,مثير للجدل,الإنجليزي,500
ما معنى idiom "move the goalposts" في الجملة: Every time we met the requirements they moved the goalposts؟,يغير الشروط بعد الاتفاق,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The report shed light ____ several hidden risks؟,on بمعنى أوضح وكشف,الإنجليزي,500
ما معنى كلمة "tentative" في الجملة: We made a tentative agreement until the final contract is ready؟,مبدئي أو غير نهائي,الإنجليزي,500
ما معنى saying "Do not cross that bridge until you come to it" في الجملة: Stop worrying about next year do not cross that bridge until you come to it؟,لا تقلق من مشكلة قبل وقتها,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The criticism was harsh but she took it on the ____؟,chin بمعنى تقبلته بصبر وشجاعة,الإنجليزي,500
ما معنى كلمة "impartial" في الجملة: A judge must remain impartial during the trial؟,محايد وغير منحاز,الإنجليزي,500
ما معنى phrasal verb "weed out" في الجملة: The interview process weeds out unqualified applicants؟,يستبعد غير المناسبين,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Still waters run ____؟,deep بمعنى الشخص الهادئ قد يكون عميق التفكير,الإنجليزي,500
ما معنى كلمة "redundant" في الجملة: Several steps in the process became redundant after automation؟,زائد عن الحاجة,الإنجليزي,500
ما معنى idiom "throw someone under the bus" في الجملة: He threw his coworker under the bus to protect himself؟,يلقي اللوم على غيره لحماية نفسه,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The team managed to scrape ____ enough money to finish the project؟,together بمعنى يجمع بصعوبة,الإنجليزي,500
ما معنى كلمة "pragmatic" في الجملة: We need a pragmatic solution instead of a perfect theory؟,عملي وواقعي,الإنجليزي,500
ما معنى saying "If the shoe fits wear it" في الجملة: I did not name anyone but if the shoe fits wear it؟,إذا كان الكلام ينطبق عليك فاعترف به,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The CEO wanted to nip the problem in the ____؟,bud بمعنى يعالج المشكلة مبكرا قبل أن تكبر,الإنجليزي,500
ما معنى كلمة "lucrative" في الجملة: Cybersecurity has become a lucrative career field؟,مربح جدا,الإنجليزي,500
ما معنى phrasal verb "iron out" في الجملة: We need to iron out the final details before launch؟,يعالج التفاصيل والمشاكل الصغيرة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Too little too ____؟,late بمعنى جاء متأخرا وغير كاف,الإنجليزي,500
ما معنى كلمة "skeptical" في الجملة: Investors were skeptical about the unrealistic profit forecast؟,متشكك وغير مقتنع بسهولة,الإنجليزي,500
ما معنى idiom "bite off more than you can chew" في الجملة: He accepted five projects at once and bit off more than he could chew؟,يتحمل أكثر مما يستطيع,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His argument rests ____ a false assumption؟,on بمعنى يعتمد على,الإنجليزي,500
ما معنى كلمة "detrimental" في الجملة: Poor sleep can be detrimental to concentration؟,ضار أو مؤذ,الإنجليزي,500
ما معنى saying "A fool and his money are soon parted" في الجملة: He bought a useless product again a fool and his money are soon parted؟,الأحمق يخسر ماله بسهولة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: She tried to keep the project ____ after the leader resigned؟,afloat بمعنى يحافظ عليه من الفشل,الإنجليزي,500
ما معنى كلمة "coherent" في الجملة: His explanation was coherent and easy to follow؟,منطقي ومترابط,الإنجليزي,500
ما معنى phrasal verb "back down" في الجملة: He refused to back down despite strong criticism؟,يتراجع عن موقفه,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The proof is in the ____؟,pudding بمعنى النتيجة العملية هي الدليل الحقيقي,الإنجليزي,500
ما معنى كلمة "superficial" في الجملة: The article gave only a superficial analysis of the issue؟,سطحي وغير عميق,الإنجليزي,500
ما معنى idiom "put someone on the spot" في الجملة: The question put him on the spot during the meeting؟,يضعه في موقف محرج ومفاجئ,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The company tried to play ____ the seriousness of the leak؟,down بمعنى يقلل من أهمية,الإنجليزي,500
ما معنى كلمة "volatile" في الجملة: The market became volatile after the political announcement؟,متقلب وغير مستقر,الإنجليزي,500
ما معنى saying "You cannot teach an old dog new tricks" في الجملة: He refuses to use email you cannot teach an old dog new tricks؟,يصعب تغيير عادات شخص اعتاد طريقة قديمة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The decision was made behind closed ____؟,doors بمعنى في السر وليس علنا,الإنجليزي,500
ما معنى كلمة "credible" في الجملة: The witness gave a credible account of the accident؟,موثوق وقابل للتصديق,الإنجليزي,500
ما معنى phrasal verb "single out" في الجملة: The teacher singled out one essay for special praise؟,يختار أو يميز شخصا من بين المجموعة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not bite off more than you can ____؟,chew بمعنى لا تحمل نفسك فوق طاقتها,الإنجليزي,500
ما معنى كلمة "inadequate" في الجملة: The safety measures were inadequate for such a risky task؟,غير كاف,الإنجليزي,500
ما معنى idiom "have the upper hand" في الجملة: After the new evidence the lawyer had the upper hand؟,يمتلك الأفضلية أو السيطرة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The scandal took a toll ____ the company's reputation؟,on بمعنى أثر سلبا على,الإنجليزي,500
ما معنى كلمة "conventional" في الجملة: He rejected conventional methods and tried a new approach؟,تقليدي أو معتاد,الإنجليزي,500
ما معنى saying "People who live in glass houses should not throw stones" في الجملة: He criticized others for mistakes he also makes people who live in glass houses should not throw stones؟,لا تنتقد عيوبا موجودة فيك أيضا,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The plan looks good on ____ but may fail in practice؟,paper بمعنى نظريا فقط,الإنجليزي,500
ما معنى كلمة "subtle" في الجملة: There was a subtle difference between the two statements؟,دقيق أو غير واضح بسهولة,الإنجليزي,500
ما معنى phrasal verb "map out" في الجملة: We mapped out the whole strategy before starting؟,يخطط بالتفصيل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Many hands make light ____؟,work بمعنى التعاون يجعل العمل أسهل,الإنجليزي,500
ما معنى كلمة "inevitable" في الجملة: Without maintenance system failure was inevitable؟,حتمي ولا يمكن تجنبه,الإنجليزي,500
ما معنى idiom "go down in flames" في الجملة: The proposal went down in flames after the budget review؟,يفشل بشكل واضح وقوي,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The speaker glossed ____ the most controversial part of the report؟,over بمعنى يتجاهل أو يمر عليه بسرعة,الإنجليزي,500
ما معنى كلمة "assertive" في الجملة: She was assertive without being rude؟,واثق وحازم في التعبير,الإنجليزي,500
ما معنى saying "The squeaky wheel gets the grease" في الجملة: He kept asking for support until they helped him the squeaky wheel gets the grease؟,من يطالب بصوت واضح يحصل على الاهتمام,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The investor pulled the ____ on the deal after seeing the risks؟,plug بمعنى أوقفه أو ألغاه,الإنجليزي,500
ما معنى كلمة "ambivalent" في الجملة: She felt ambivalent about moving abroad؟,لديه مشاعر متضاربة,الإنجليزي,500
ما معنى phrasal verb "lay out" في الجملة: The report lays out the main causes of the failure؟,يعرض أو يوضح بشكل منظم,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The bigger they are the harder they ____؟,fall بمعنى كلما كان الشخص أقوى كان سقوطه أكبر,الإنجليزي,500
ما معنى كلمة "compelling" في الجملة: She presented a compelling argument for the new policy؟,مقنع وقوي,الإنجليزي,500
ما معنى idiom "a double edged sword" في الجملة: Social media is a double edged sword for businesses؟,شيء له فائدة وضرر معا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: We need to strike a balance ____ speed and quality؟,between بمعنى يوازن بين,الإنجليزي,500
ما معنى كلمة "rigorous" في الجملة: The experiment followed a rigorous testing process؟,صارم ودقيق,الإنجليزي,500
ما معنى saying "There are plenty of fish in the sea" في الجملة: Do not be upset about one rejection there are plenty of fish in the sea؟,هناك فرص أو أشخاص آخرون كثيرون,الإنجليزي,500
أكمل idiom الصحيح في الجملة: He was trying to have it both ____؟,ways بمعنى يريد ميزتين متعارضتين معا,الإنجليزي,500
ما معنى كلمة "discreet" في الجملة: Be discreet when discussing confidential information؟,حذر ويحافظ على السرية,الإنجليزي,500
ما معنى phrasal verb "fall through" في الجملة: The deal fell through after the bank refused funding؟,يفشل أو لا يكتمل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A leopard cannot change its ____؟,spots بمعنى الطبع لا يتغير بسهولة,الإنجليزي,500
ما معنى كلمة "hostile" في الجملة: The audience became hostile after the unfair decision؟,عدائي أو غير ودي,الإنجليزي,500
ما معنى idiom "get cold feet" في الجملة: He got cold feet before signing the contract؟,يتراجع بسبب الخوف أو التردد,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The problem stems ____ poor planning and weak communication؟,from بمعنى ينتج من أو سببه,الإنجليزي,500
ما معنى كلمة "ambiguous" في الجملة: The instructions were ambiguous and led to different answers؟,غامض ويحتمل أكثر من معنى,الإنجليزي,500
ما معنى saying "Never look a gift horse in the mouth" في الجملة: They offered free help so never look a gift horse in the mouth؟,لا تنتقد الهدية أو المساعدة المجانية,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The two companies are neck and ____ in the market؟,neck بمعنى متقاربان جدا في المنافسة,الإنجليزي,500
ما معنى كلمة "profound" في الجملة: The discovery had a profound impact on modern medicine؟,عميق أو كبير التأثير,الإنجليزي,500
ما معنى phrasal verb "pull through" في الجملة: The patient pulled through after a difficult operation؟,يتعافى أو ينجو,الإنجليزي,500
أكمل المثل الصحيح في الجملة: No news is good ____؟,news بمعنى عدم وجود أخبار سيئة قد يكون أمرا جيدا,الإنجليزي,500
ما معنى كلمة "scarce" في الجملة: Clean water became scarce during the drought؟,نادر أو قليل,الإنجليزي,500
ما معنى idiom "keep your ear to the ground" في الجملة: A good manager keeps his ear to the ground؟,يبقى منتبها لما يحدث حوله,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The company came under fire ____ its poor safety record؟,for بمعنى تعرضت لانتقاد بسبب,الإنجليزي,500
ما معنى كلمة "tenacious" في الجملة: Her tenacious attitude helped her finish the difficult project؟,مثابر ولا يستسلم,الإنجليزي,500
ما معنى saying "You made your bed now lie in it" في الجملة: He ignored advice and failed you made your bed now lie in it؟,تحمل نتيجة قراراتك,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The plan is still in its ____؟,infancy بمعنى في بدايته المبكرة,الإنجليزي,500
ما معنى كلمة "flawed" في الجملة: The conclusion was based on flawed data؟,معيب أو فيه أخطاء,الإنجليزي,500
ما معنى phrasal verb "set aside" في الجملة: The judge set aside the earlier decision؟,يلغي أو يضع جانبا حسب السياق,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Half a loaf is better than no ____؟,bread بمعنى القليل أفضل من لا شيء,الإنجليزي,500
ما معنى كلمة "notorious" في الجملة: The area is notorious for traffic jams؟,سيئ السمعة أو مشهور بشيء سلبي,الإنجليزي,500
ما معنى idiom "a storm in a teacup" في الجملة: The argument was a storm in a teacup and ended quickly؟,مشكلة صغيرة تم تضخيمها,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The final decision hinges ____ the test results؟,on بمعنى يعتمد على بشكل حاسم,الإنجليزي,500
ما معنى كلمة "plausible" في الجملة: His explanation sounded plausible but needed proof؟,معقول وقابل للتصديق,الإنجليزي,500
ما معنى saying "The ends do not justify the means" في الجملة: Cheating to win is wrong because the ends do not justify the means؟,الغاية لا تبرر الوسيلة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The project was hanging by a ____ after the budget cuts؟,thread بمعنى في وضع خطر جدا,الإنجليزي,500

ما معنى كلمة "nuance" في الجملة: The translation missed the nuance of the original sentence؟,فرق دقيق في المعنى,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His sudden silence spoke ____؟,volumes بمعنى كان له معنى واضح وكبير,الإنجليزي,500
ما معنى saying "A stitch in time saves nine" في الجملة: Fix the small leak now because a stitch in time saves nine؟,حل المشكلة مبكرا يمنع مشاكل أكبر,الإنجليزي,500
ما معنى phrasal verb "clamp down on" في الجملة: The school decided to clamp down on cheating؟,يتخذ إجراءات صارمة ضد,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The deal looked promising but it fell at the final ____؟,hurdle بمعنى فشل في المرحلة الأخيرة,الإنجليزي,500
ما معنى كلمة "equivocal" في الجملة: His answer was equivocal and did not confirm anything؟,غامض أو غير حاسم,الإنجليزي,500
ما معنى idiom "the writing is on the wall" في الجملة: Sales kept falling so the writing was on the wall؟,علامات الفشل أو النهاية واضحة,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The witness refused to back ____ his earlier statement؟,up بمعنى يدعم أو يؤكد,الإنجليزي,500
ما معنى كلمة "concede" في الجملة: He had to concede that his opponent made a strong point؟,يعترف على مضض,الإنجليزي,500
ما معنى saying "You cannot judge a fish by its ability to climb a tree" في الجملة: He is bad at exams but great at design you cannot judge a fish by its ability to climb a tree؟,لا تقيم شخصا بمعيار لا يناسب قدراته,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The team was caught between two ____؟,fires بمعنى عالق بين مشكلتين أو ضغطين,الإنجليزي,500
ما معنى كلمة "dismissive" في الجملة: Her dismissive attitude made the students afraid to ask questions؟,مستخف أو غير مهتم,الإنجليزي,500
ما معنى phrasal verb "bear out" في الجملة: The final data bore out our original prediction؟,يؤكد أو يثبت صحة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Empty vessels make the most ____؟,noise بمعنى الأقل معرفة أكثر كلاما,الإنجليزي,500
ما معنى كلمة "precarious" في الجملة: The company is in a precarious financial position؟,غير مستقر أو محفوف بالخطر,الإنجليزي,500
ما معنى idiom "pull the wool over someone's eyes" في الجملة: He tried to pull the wool over the client's eyes with fake numbers؟,يخدع شخصا أو يضلله,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The new evidence turned the case on its ____؟,head بمعنى قلب الفهم أو الوضع تماما,الإنجليزي,500
ما معنى كلمة "alleviate" في الجملة: The new medicine helped alleviate the patient's pain؟,يخفف أو يقلل,الإنجليزي,500
ما معنى saying "The devil can cite scripture for his purpose" في الجملة: He used facts selectively to defend himself the devil can cite scripture for his purpose؟,يمكن استغلال الكلام الصحيح لخدمة هدف سيئ,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The lawyer picked ____ the contract line by line؟,apart بمعنى يفحص وينتقد كل جزء,الإنجليزي,500
ما معنى كلمة "elusive" في الجملة: A clear solution remained elusive despite many meetings؟,صعب المنال أو صعب الوصول إليه,الإنجليزي,500
ما معنى idiom "a bitter pill to swallow" في الجملة: Losing the final after leading all game was a bitter pill to swallow؟,حقيقة مؤلمة يصعب قبولها,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The truth will ____ out؟,come بمعنى الحقيقة ستظهر في النهاية,الإنجليزي,500
ما معنى كلمة "diligent" في الجملة: The diligent student reviewed every mistake before the exam؟,مجتهد ومنتظم,الإنجليزي,500
ما معنى phrasal verb "come under" في الجملة: The company came under pressure after the report؟,يتعرض إلى,الإنجليزي,500
أكمل idiom الصحيح في الجملة: His apology was too little too ____؟,late بمعنى غير كاف وجاء متأخرا,الإنجليزي,500
ما معنى كلمة "indifferent" في الجملة: He seemed indifferent to the team's concerns؟,غير مهتم أو لا يبالي,الإنجليزي,500
ما معنى saying "The pot calling the kettle black" في الجملة: He accused her of being late though he is always late the pot calling the kettle black؟,ينتقد عيبا موجودا فيه,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The CEO tried to put a positive spin ____ the bad results؟,on بمعنى يعرضه بطريقة إيجابية,الإنجليزي,500
ما معنى كلمة "compromise" في الجملة: Both sides accepted a compromise after long negotiations؟,حل وسط,الإنجليزي,500
ما معنى idiom "throw caution to the wind" في الجملة: He threw caution to the wind and invested all his savings؟,يتصرف بجرأة دون احتياط,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The plan did not pan ____ as expected؟,out بمعنى ينجح أو يسير كما كان متوقعا,الإنجليزي,500
ما معنى كلمة "intricate" في الجملة: The engineer explained the intricate design of the circuit؟,معقد ودقيق التفاصيل,الإنجليزي,500
ما معنى saying "A rolling stone gathers no moss" في الجملة: He keeps changing jobs and never builds expertise a rolling stone gathers no moss؟,من لا يستقر لا يجمع خبرة أو مسؤوليات,الإنجليزي,500
أكمل idiom الصحيح في الجملة: She was skating on thin ____ when she criticized the director publicly؟,ice بمعنى تخاطر في وضع حساس,الإنجليزي,500
ما معنى كلمة "undermine" في الجملة: Constant doubt can undermine a team's confidence؟,يضعف تدريجيا,الإنجليزي,500
ما معنى phrasal verb "stamp out" في الجملة: The organization wants to stamp out corruption؟,يقضي على تماما,الإنجليزي,500
أكمل المثل الصحيح في الجملة: One man's trash is another man's ____؟,treasure بمعنى ما يراه شخص بلا قيمة قد يراه آخر ثمينا,الإنجليزي,500
ما معنى كلمة "tenuous" في الجملة: The link between the two events is tenuous at best؟,ضعيف أو غير مؤكد,الإنجليزي,500
ما معنى idiom "split hairs" في الجملة: They spent an hour splitting hairs over tiny wording changes؟,يدقق في فروق صغيرة جدا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His excuse did not hold ____ under questioning؟,water بمعنى لم يكن مقنعا أو منطقيا,الإنجليزي,500
ما معنى كلمة "vindicate" في الجملة: The new evidence vindicated her after months of blame؟,يثبت براءته أو صحة موقفه,الإنجليزي,500
ما معنى saying "Do not put the cart before the horse" في الجملة: Do not hire staff before you have funding do not put the cart before the horse؟,لا تعكس ترتيب الأمور الطبيعي,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The team had to tighten its ____ after losing money؟,belt بمعنى يقلل المصاريف,الإنجليزي,500
ما معنى كلمة "cumbersome" في الجملة: The old approval process was slow and cumbersome؟,معقد ومرهق في الاستخدام,الإنجليزي,500
ما معنى phrasal verb "gear up for" في الجملة: The company is gearing up for a major launch؟,يستعد ل,الإنجليزي,500
أكمل المثل الصحيح في الجملة: If you cannot stand the heat get out of the ____؟,kitchen بمعنى إن لم تتحمل الضغط فاترك المكان,الإنجليزي,500
ما معنى كلمة "sporadic" في الجملة: The internet connection was sporadic during the storm؟,متقطع وغير منتظم,الإنجليزي,500
ما معنى idiom "take the wind out of someone's sails" في الجملة: The harsh comment took the wind out of his sails before the presentation؟,يحبط حماسه أو ثقته,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The manager signed ____ on the final design؟,off بمعنى وافق رسميا,الإنجليزي,500
ما معنى كلمة "discrepancy" في الجملة: There was a discrepancy between the invoice and the payment record؟,اختلاف أو عدم تطابق,الإنجليزي,500
ما معنى saying "The nail that sticks out gets hammered down" في الجملة: He avoided drawing attention at work because the nail that sticks out gets hammered down؟,الشخص المختلف أو البارز قد يتعرض للضغط,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The project went off the ____ after the leader left؟,rails بمعنى خرج عن السيطرة,الإنجليزي,500
ما معنى كلمة "implicit" في الجملة: There was an implicit agreement not to discuss salaries؟,ضمني وغير مصرح به,الإنجليزي,500
ما معنى phrasal verb "water down" في الجملة: The final report watered down the criticism؟,يخفف أو يضعف حدة الكلام,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The speech struck a ____ with young voters؟,chord بمعنى أثّر فيهم أو لامس مشاعرهم,الإنجليزي,500
ما معنى كلمة "explicit" في الجملة: The instructions were explicit and left no room for confusion؟,صريح وواضح جدا,الإنجليزي,500
ما معنى saying "Familiarity breeds contempt" في الجملة: They stopped respecting the rules after years in the company familiarity breeds contempt؟,كثرة الاعتياد قد تقلل الاحترام,الإنجليزي,500
أكمل idiom الصحيح في الجملة: He had to eat humble ____ after his prediction failed؟,pie بمعنى يعترف بخطئه بتواضع,الإنجليزي,500
ما معنى كلمة "marginal" في الجملة: The change had only a marginal effect on performance؟,بسيط أو هامشي,الإنجليزي,500
ما معنى phrasal verb "phase in" في الجملة: The school will phase in the new system gradually؟,يدخل تدريجيا,الإنجليزي,500
أكمل المثل الصحيح في الجملة: A rising tide lifts all ____؟,boats بمعنى التحسن العام يفيد الجميع,الإنجليزي,500
ما معنى كلمة "complicit" في الجملة: He was complicit in hiding the mistake from the client؟,متورط أو مشارك في الخطأ,الإنجليزي,500
ما معنى idiom "a slap on the wrist" في الجملة: The punishment was just a slap on the wrist؟,عقوبة خفيفة جدا,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The numbers paint a grim ____ for the company؟,picture بمعنى تعطي صورة سيئة أو مقلقة,الإنجليزي,500
ما معنى كلمة "substantiate" في الجملة: You need evidence to substantiate your claim؟,يثبت بالأدلة,الإنجليزي,500
ما معنى saying "Charity begins at home" في الجملة: Help your family first charity begins at home؟,ابدأ بمساعدة الأقربين,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The consultant laid ____ the risks clearly؟,out بمعنى عرض ووضح,الإنجليزي,500
ما معنى كلمة "exacerbate" في الجملة: Ignoring small errors can exacerbate the problem؟,يزيد الأمر سوءا,الإنجليزي,500
ما معنى idiom "go out on a limb" في الجملة: She went out on a limb by supporting the unpopular idea؟,يجازف بموقف غير مضمون,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The darkest hour is just before the ____؟,dawn بمعنى الفرج قد يأتي بعد أشد لحظة,الإنجليزي,500
ما معنى كلمة "counterproductive" في الجملة: Too much pressure can be counterproductive for students؟,يعطي نتيجة عكسية,الإنجليزي,500
ما معنى phrasal verb "level with" في الجملة: I need you to level with me about the real problem؟,يصارح بصدق,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The CEO was walking a tight ____ during the crisis؟,rope بمعنى يحاول التوازن في موقف حساس,الإنجليزي,500
ما معنى كلمة "convoluted" في الجملة: The explanation was so convoluted that nobody understood it؟,معقد ومتشابك,الإنجليزي,500
ما معنى saying "Do not let the perfect be the enemy of the good" في الجملة: Launch the useful version now do not let the perfect be the enemy of the good؟,لا تؤخر الشيء الجيد بسبب البحث عن الكمال,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The company is on the brink ____ bankruptcy؟,of بمعنى على وشك,الإنجليزي,500
ما معنى كلمة "incisive" في الجملة: Her incisive question exposed the weakness in the plan؟,دقيق وقوي يكشف الحقيقة,الإنجليزي,500
ما معنى idiom "miss the boat" في الجملة: He waited too long to apply and missed the boat؟,يفوّت الفرصة,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The new evidence calls ____ question the original conclusion؟,into بمعنى يجعل الأمر موضع شك,الإنجليزي,500
ما معنى كلمة "pervasive" في الجملة: The company had a pervasive culture of fear؟,منتشر في كل مكان,الإنجليزي,500
ما معنى saying "A bird in the hand is worth two in the bush" في الجملة: Take the secure job offer a bird in the hand is worth two in the bush؟,الشيء المضمون أفضل من احتمال غير مضمون,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The deal was dead in the ____ after the legal review؟,water بمعنى فشل ولم يعد قابلا للاستمرار,الإنجليزي,500
ما معنى كلمة "astute" في الجملة: Her astute observations helped the team avoid a costly mistake؟,ذكي وحسن الملاحظة,الإنجليزي,500
ما معنى phrasal verb "push back against" في الجملة: Employees pushed back against the unfair policy؟,يعترض أو يقاوم,الإنجليزي,500
أكمل المثل الصحيح في الجملة: You cannot make an omelet without breaking ____؟,eggs بمعنى لا تحقيق لشيء دون بعض الخسائر,الإنجليزي,500
ما معنى كلمة "dubious" في الجملة: The offer sounded dubious because it promised huge profits quickly؟,مشكوك فيه,الإنجليزي,500
ما معنى idiom "a hard nut to crack" في الجملة: This encryption problem is a hard nut to crack؟,مشكلة صعبة الحل,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The final report put the matter ____ rest؟,to بمعنى أنهى الجدل,الإنجليزي,500
ما معنى كلمة "rescind" في الجملة: The company rescinded the offer after reviewing his documents؟,يلغي رسميا,الإنجليزي,500
ما معنى saying "Bad news travels fast" في الجملة: Everyone heard about the mistake within an hour bad news travels fast؟,الأخبار السيئة تنتشر بسرعة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The proposal was a tough ____ to sell to investors؟,sell بمعنى صعب الإقناع,الإنجليزي,500
ما معنى كلمة "disgruntled" في الجملة: Disgruntled employees complained about the new schedule؟,غير راض أو مستاء,الإنجليزي,500
ما معنى phrasal verb "fall back on" في الجملة: If the plan fails we can fall back on our savings؟,يعتمد على كخطة بديلة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Make hay while the sun ____؟,shines بمعنى استغل الفرصة وهي متاحة,الإنجليزي,500
ما معنى كلمة "imminent" في الجملة: The company warned employees about imminent changes؟,وشيك أو قريب الحدوث,الإنجليزي,500
ما معنى idiom "the elephant in the room" في الجملة: Everyone discussed small issues and ignored the elephant in the room؟,المشكلة الواضحة التي يتجنب الجميع ذكرها,الإنجليزي,500

ما معنى كلمة "aberration" في الجملة: The sudden drop in sales was an aberration not a long term trend؟,حالة شاذة أو غير طبيعية,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The company had to bite the ____ after ignoring the problem for months؟,bullet بمعنى يواجه أمرا صعبا بشجاعة,الإنجليزي,500
ما معنى saying "Haste makes waste" في الجملة: He rushed the report and made many errors haste makes waste؟,العجلة تسبب الأخطاء والخسارة,الإنجليزي,500
ما معنى phrasal verb "hammer out" في الجملة: The two sides hammered out an agreement after hours of debate؟,يتوصل إلى اتفاق بعد نقاش صعب,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: Her argument cut ____ the noise and focused on the real issue؟,through بمعنى يتجاوز التشويش ويصل للمهم,الإنجليزي,500
ما معنى كلمة "candid" في الجملة: The manager gave a candid assessment of the team's performance؟,صريح ومباشر,الإنجليزي,500
ما معنى idiom "a blessing in disguise" في الجملة: Losing the job was a blessing in disguise because he found a better career؟,شيء يبدو سيئا لكنه يحمل خيرا,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The team needs to shore ____ its security before launch؟,up بمعنى يقوي ويدعم,الإنجليزي,500
ما معنى كلمة "erratic" في الجملة: His attendance became erratic after he started working nights؟,غير منتظم أو متقلب,الإنجليزي,500
ما معنى saying "You cannot have it both ways" في الجملة: You want privacy and full public attention you cannot have it both ways؟,لا يمكنك جمع خيارين متعارضين,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Do not burn your ____ before you need them؟,bridges بمعنى لا تقطع علاقات قد تحتاجها لاحقا,الإنجليزي,500
ما معنى كلمة "fallacy" في الجملة: The conclusion was based on a common logical fallacy؟,مغالطة أو خطأ منطقي,الإنجليزي,500
ما معنى phrasal verb "drum up" في الجملة: The startup tried to drum up interest before the product launch؟,يجذب أو يثير اهتماما,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The issue was pushed to the back ____ during the crisis؟,burner بمعنى تم تأجيله لأنه أقل أولوية,الإنجليزي,500
ما معنى كلمة "frugal" في الجملة: She is frugal and avoids unnecessary spending؟,مقتصد ولا يصرف كثيرا,الإنجليزي,500
ما معنى idiom "jump on the bandwagon" في الجملة: Many companies jumped on the bandwagon after AI became popular؟,يتبع موجة منتشرة لأنها رائجة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The new evidence blew the case wide ____؟,open بمعنى كشفه وغيّر مجراه تماما,الإنجليزي,500
ما معنى كلمة "gratuitous" في الجملة: His comment was gratuitous and added nothing useful to the discussion؟,غير ضروري أو بلا سبب واضح,الإنجليزي,500
ما معنى saying "Fine feathers make fine birds" في الجملة: He looked rich because of his suit fine feathers make fine birds؟,المظهر الجميل قد يجعل الشخص يبدو أفضل,الإنجليزي,500
ما معنى phrasal verb "phase down" في الجملة: The factory will phase down production over six months؟,يقلل تدريجيا,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The proposal was dead on ____ after the budget review؟,arrival بمعنى فشل من البداية,الإنجليزي,500
ما معنى كلمة "haphazard" في الجملة: The files were arranged in a haphazard way with no clear order؟,عشوائي وغير منظم,الإنجليزي,500
ما معنى idiom "not hold a candle to" في الجملة: The sequel does not hold a candle to the original film؟,لا يقترب من مستوى شيء آخر,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The company wants to roll ____ the new feature next month؟,out بمعنى يطلق أو ينشر,الإنجليزي,500
ما معنى كلمة "impeccable" في الجملة: Her timing and pronunciation were impeccable during the speech؟,مثالي وخال من الأخطاء,الإنجليزي,500
ما معنى saying "The proof of the pudding is in the eating" في الجملة: The idea sounds good but the proof of the pudding is in the eating؟,الحكم الحقيقي يكون من التجربة والنتيجة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: His mistake set ____ a chain reaction across the whole system؟,off بمعنى تسبب في بدء,الإنجليزي,500
ما معنى كلمة "judicious" في الجملة: The judge made a judicious decision after hearing both sides؟,حكيم ومتزن,الإنجليزي,500
ما معنى idiom "keep someone at arm's length" في الجملة: She kept the dishonest partner at arm's length؟,يبقيه بعيدا ولا يثق به تماما,الإنجليزي,500
ما معنى phrasal verb "ferret out" في الجملة: The investigator ferreted out the hidden source of the leak؟,يكتشف شيئا مخفيا بعد بحث,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Cleanliness is next to ____؟,godliness بمعنى النظافة قيمة مهمة جدا,الإنجليزي,500
ما معنى كلمة "laconic" في الجملة: His laconic reply made everyone wonder what he really thought؟,قليل الكلام ومختصر جدا,الإنجليزي,500
ما معنى idiom "a red herring" في الجملة: The argument about price was a red herring that distracted us from safety؟,موضوع مضلل يصرف الانتباه عن المهم,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The harsh review tore ____ his argument completely؟,apart بمعنى ينتقد بشدة ويفككه,الإنجليزي,500
ما معنى كلمة "mundane" في الجملة: The job involved many mundane tasks like sorting emails؟,عادي وممل,الإنجليزي,500
ما معنى saying "Old habits die hard" في الجملة: He still prints every email old habits die hard؟,العادات القديمة يصعب تركها,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The final decision is still anyone's ____؟,guess بمعنى لا أحد يعرف النتيجة,الإنجليزي,500
ما معنى كلمة "negligible" في الجملة: The difference in speed was negligible in daily use؟,ضئيل جدا ولا يكاد يذكر,الإنجليزي,500
ما معنى phrasal verb "sift through" في الجملة: We sifted through hundreds of applications to find the best candidates؟,يفرز ويفحص بعناية,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The plan gives us little room ____ error؟,for بمعنى مجال قليل للخطأ,الإنجليزي,500
ما معنى كلمة "opaque" في الجملة: The company's decision making process was opaque to employees؟,غامض وغير شفاف,الإنجليزي,500
ما معنى idiom "in the driver's seat" في الجملة: After winning the contract the startup was in the driver's seat؟,في موقع السيطرة أو القرار,الإنجليزي,500
ما معنى saying "A penny saved is a penny earned" في الجملة: Avoid small waste every day a penny saved is a penny earned؟,توفير المال كأنه كسب مال,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The crisis forced the team to buckle ____ and work seriously؟,down بمعنى يبدأ العمل بجدية,الإنجليزي,500
ما معنى كلمة "parsimonious" في الجملة: The researcher preferred a parsimonious explanation with fewer assumptions؟,موجز أو قليل الافتراضات,الإنجليزي,500
ما معنى idiom "a flash in the pan" في الجملة: The product was popular for one week and then disappeared a flash in the pan؟,نجاح مؤقت وقصير,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Hope for the best prepare for the ____؟,worst بمعنى تفاءل لكن استعد للأسوأ,الإنجليزي,500
ما معنى كلمة "quandary" في الجملة: The manager was in a quandary about whether to cut costs or hire more staff؟,حيرة بين خيارات صعبة,الإنجليزي,500
ما معنى phrasal verb "root out" في الجملة: The organization tried to root out corruption from its departments؟,يستأصل أو يقضي على من الجذور,الإنجليزي,500
أكمل idiom الصحيح في الجملة: His criticism hit too close to ____؟,home بمعنى لمس نقطة حساسة أو حقيقية,الإنجليزي,500
ما معنى كلمة "recalcitrant" في الجملة: The recalcitrant employee refused to follow the new procedure؟,عنيد ورافض للطاعة,الإنجليزي,500
ما معنى saying "One good turn deserves another" في الجملة: She helped me last week so I helped her move one good turn deserves another؟,المعروف يرد بمعروف,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The company cashed ____ on the sudden demand for home delivery؟,in بمعنى يستفيد ماديا من فرصة,الإنجليزي,500
ما معنى كلمة "scrupulous" في الجملة: A scrupulous accountant checks every number honestly؟,دقيق وأمين جدا,الإنجليزي,500
ما معنى idiom "a wolf in sheep's clothing" في الجملة: The friendly investor was a wolf in sheep's clothing؟,شخص يبدو طيبا لكنه خطير أو مخادع,الإنجليزي,500
أكمل المثل الصحيح في الجملة: The customer is king but ____ has limits؟,service بمعنى خدمة العميل مهمة لكن لها حدود,الإنجليزي,500
ما معنى كلمة "tacit" في الجملة: There was a tacit understanding that nobody would mention the mistake؟,ضمني وغير مصرح به,الإنجليزي,500
ما معنى phrasal verb "scale back" في الجملة: The company scaled back the project after costs increased؟,يقلص أو يخفض,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The two leaders finally saw eye to ____ on the budget؟,eye بمعنى اتفقا في الرأي,الإنجليزي,500
ما معنى كلمة "untenable" في الجملة: His position became untenable after the facts were revealed؟,غير قابل للدفاع أو الاستمرار,الإنجليزي,500
ما معنى saying "Least said soonest mended" في الجملة: Do not keep arguing least said soonest mended؟,قلة الكلام تساعد على إصلاح الخلاف بسرعة,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The lawsuit cast a shadow ____ the company's reputation؟,over بمعنى أثر سلبا وأثار الشك,الإنجليزي,500
ما معنى كلمة "viable" في الجملة: The idea is interesting but not commercially viable yet؟,قابل للتطبيق أو قابل للنجاح,الإنجليزي,500
ما معنى idiom "go against the grain" في الجملة: His proposal went against the grain of traditional thinking؟,يخالف المعتاد أو الرأي السائد,الإنجليزي,500
ما معنى phrasal verb "pin down" في الجملة: We could not pin down the exact cause of the failure؟,يحدد بدقة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Misery loves ____؟,company بمعنى الحزين يحب من يشاركه حالته,الإنجليزي,500
ما معنى كلمة "whimsical" في الجملة: The design looked whimsical but still practical؟,غريب أو خيالي بطريقة لطيفة,الإنجليزي,500
ما معنى idiom "throw in the towel" في الجملة: After three failed attempts he threw in the towel؟,يستسلم ويتوقف عن المحاولة,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The plan hinges ____ approval from the board؟,on بمعنى يعتمد على,الإنجليزي,500
ما معنى كلمة "zealous" في الجملة: She was zealous in defending the rights of workers؟,متحمس ومندفع بقوة,الإنجليزي,500
ما معنى saying "Little strokes fell great oaks" في الجملة: Study a little daily little strokes fell great oaks؟,الجهد الصغير المستمر يحقق نتائج كبيرة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: He had a chip on his ____ after being rejected twice؟,shoulder بمعنى لديه حساسية أو غضب قديم,الإنجليزي,500
ما معنى كلمة "arbitrary" في الجملة: The rule seemed arbitrary because nobody explained the reason؟,عشوائي أو بلا سبب واضح,الإنجليزي,500
ما معنى phrasal verb "play into" في الجملة: His angry reaction played into their plan to make him look unstable؟,يخدم خطة غيره دون قصد,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The data flies in the face ____ their claims؟,of بمعنى يعارض بوضوح,الإنجليزي,500
ما معنى كلمة "brevity" في الجملة: The speech was praised for its brevity and clarity؟,الإيجاز أو الاختصار,الإنجليزي,500
ما معنى idiom "have an axe to grind" في الجملة: His criticism sounded personal because he had an axe to grind؟,لديه دافع شخصي أو ضغينة,الإنجليزي,500
أكمل المثل الصحيح في الجملة: All good things must come to an ____؟,end بمعنى كل شيء جميل ينتهي,الإنجليزي,500
ما معنى كلمة "cursory" في الجملة: A cursory look at the data missed several serious errors؟,سريع وسطحي,الإنجليزي,500
ما معنى phrasal verb "tease out" في الجملة: The researcher tried to tease out the real cause from the data؟,يستخرج بصعوبة أو يميز بدقة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: The negotiations are hanging in the ____؟,balance بمعنى نتيجتها غير محسومة,الإنجليزي,500
ما معنى كلمة "defunct" في الجملة: The website links to a defunct service that no longer exists؟,متوقف ولم يعد يعمل,الإنجليزي,500
ما معنى saying "You can catch more flies with honey than with vinegar" في الجملة: Be polite when asking for help you can catch more flies with honey than with vinegar؟,اللطف يحقق نتائج أفضل من القسوة,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The issue cropped ____ again during the final review؟,up بمعنى ظهر فجأة,الإنجليزي,500
ما معنى كلمة "egregious" في الجملة: The report contained an egregious error that changed the conclusion؟,فادح أو سيئ جدا,الإنجليزي,500
ما معنى idiom "a storm is brewing" في الجملة: Employees are angry and a storm is brewing inside the company؟,هناك مشكلة كبيرة على وشك الحدوث,الإنجليزي,500
أكمل المثل الصحيح في الجملة: If wishes were horses beggars would ____؟,ride بمعنى التمني وحده لا يغير الواقع,الإنجليزي,500
ما معنى كلمة "futile" في الجملة: Arguing with someone who refuses facts is futile؟,بلا فائدة أو عبثي,الإنجليزي,500
ما معنى phrasal verb "boil over" في الجملة: Tension boiled over after the unfair decision؟,ينفجر غضبا أو يخرج عن السيطرة,الإنجليزي,500
أكمل idiom الصحيح في الجملة: She kept the client ____ the loop during the delay؟,in بمعنى أبقته على اطلاع,الإنجليزي,500
ما معنى كلمة "glaring" في الجملة: There was a glaring mistake in the final calculation؟,واضح جدا وفاضح,الإنجليزي,500
ما معنى saying "A house divided against itself cannot stand" في الجملة: The team kept fighting internally a house divided against itself cannot stand؟,الانقسام الداخلي يؤدي إلى الفشل,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The company hiked ____ prices after demand increased؟,up بمعنى رفع السعر,الإنجليزي,500
ما معنى كلمة "hinder" في الجملة: Poor communication can hinder progress on complex projects؟,يعيق أو يعرقل,الإنجليزي,500
ما معنى idiom "the tip of the iceberg" في الجملة: These errors are only the tip of the iceberg؟,جزء صغير ظاهر من مشكلة أكبر,الإنجليزي,500
أكمل التعبير الصحيح في الجملة: The failure dealt a blow ____ investor confidence؟,to بمعنى أضر بشدة,الإنجليزي,500
ما معنى كلمة "inert" في الجملة: The proposal remained inert because nobody took action؟,ساكن أو بلا نشاط,الإنجليزي,500
ما معنى phrasal verb "paper over" في الجملة: The manager tried to paper over the conflict with a quick apology؟,يغطي المشكلة مؤقتا دون حل حقيقي,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Pride comes before a ____؟,fall بمعنى التكبر يسبق السقوط,الإنجليزي,500
ما معنى كلمة "lucid" في الجملة: Her lucid explanation made the complex topic easy to understand؟,واضح وسهل الفهم,الإنجليزي,500
ما معنى idiom "not see the forest for the trees" في الجملة: He focused on tiny errors and could not see the forest for the trees؟,يضيع الصورة الكبيرة بسبب التفاصيل,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The final numbers did not square ____ with his earlier statement؟,with بمعنى لا تتوافق مع,الإنجليزي,500
ما معنى كلمة "moot" في الجملة: The question became moot after the project was canceled؟,غير مهم أو لم يعد له أثر عملي,الإنجليزي,500
ما معنى saying "The show must go on" في الجملة: The speaker was late but the show must go on؟,يجب الاستمرار رغم المشاكل,الإنجليزي,500
أكمل idiom الصحيح في الجملة: His plan went up in ____ after the funding was cut؟,smoke بمعنى فشل أو ضاع تماما,الإنجليزي,500
ما معنى كلمة "novel" في الجملة: The engineer proposed a novel solution to the battery problem؟,جديد ومبتكر,الإنجليزي,500
ما معنى phrasal verb "wring out" في الجملة: The consultant tried to wring out every possible saving from the budget؟,يستخرج بأقصى جهد,الإنجليزي,500
أكمل المثل الصحيح في الجملة: Seeing is ____؟,believing بمعنى الرؤية تجعل التصديق أسهل,الإنجليزي,500
ما معنى كلمة "ostensible" في الجملة: The ostensible reason for the meeting was budget planning؟,ظاهري أو معلن وليس بالضرورة الحقيقي,الإنجليزي,500
ما معنى idiom "a shot in the dark" في الجملة: My answer was a shot in the dark because I had no data؟,تخمين بدون معلومات كافية,الإنجليزي,500
أكمل phrasal verb الصحيح في الجملة: The team will hash ____ the details tomorrow؟,out بمعنى يناقش التفاصيل حتى يصل لاتفاق,الإنجليزي,500
ما معنى كلمة "perfunctory" في الجملة: He gave a perfunctory apology without real regret؟,شكلي وبلا اهتمام حقيقي,الإنجليزي,500
ما معنى saying "Many a little makes a mickle" في الجملة: Save small amounts every week many a little makes a mickle؟,الأشياء الصغيرة تتجمع لتصنع شيئا كبيرا,الإنجليزي,500



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
file_path = os.path.join(os.getcwd(), "english_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")