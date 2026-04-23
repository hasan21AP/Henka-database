

import pandas as pd
import os

# البيانات النصية تحتوي على جميع الأسئلة
data = """
What is the normal resting heart rate range in adults?,60-100 bpm,طب,100
Which chamber of the heart pumps blood into the aorta?,Left ventricle,طب,100
What is the functional unit of the kidney?,Nephron,طب,100
Which cranial nerve is responsible for vision?,Optic nerve (CN II),طب,100
What is the normal pH range of arterial blood?,7.35-7.45,طب,100
Which electrolyte is primarily responsible for action potentials?,Sodium (Na+),طب,100
What is the main neurotransmitter at the neuromuscular junction?,Acetylcholine,طب,100
Which part of the brain regulates balance?,Cerebellum,طب,100
What is the medical term for low blood sugar?,Hypoglycemia,طب,100
Which organ is primarily affected in hepatitis?,Liver,طب,100
What is the normal hemoglobin range in adult males?,13-17 g/dL,طب,100
Which artery supplies the brain?,Carotid artery,طب,100
What is the Latin term for inflammation of the appendix?,Appendicitis,طب,100
Which hormone lowers blood glucose levels?,Insulin,طب,100
What type of joint is the knee?,Hinge joint,طب,100
Which vitamin deficiency causes rickets?,Vitamin D,طب,100
What is the medical term for high blood pressure?,Hypertension,طب,100
Which cells produce antibodies?,B lymphocytes,طب,100
What is the main function of red blood cells?,Oxygen transport,طب,100
Which organ stores bile?,Gallbladder,طب,100
What is the normal body temperature in Celsius?,37°C,طب,100
Which part of the neuron conducts impulses away from the cell body?,Axon,طب,100
What is the term for excessive urination?,Polyuria,طب,100
Which drug class is used to reduce inflammation?,NSAIDs,طب,100
What is the antidote for opioid overdose?,Naloxone,طب,100
Which bacteria is commonly associated with gastric ulcers?,Helicobacter pylori,طب,100
What is the pharmacological effect of beta-blockers?,Decrease heart rate,طب,100
Which route of drug administration avoids first-pass metabolism?,Intravenous (IV),طب,100
What is the half-life of a drug?,Time to reduce concentration by half,طب,100
Which organ is responsible for drug metabolism?,Liver,طب,100
What is the main function of platelets?,Blood clotting,طب,100
Which cranial nerve controls facial expressions?,Facial nerve (CN VII),طب,100
What is the medical term for difficulty breathing?,Dyspnea,طب,100
Which part of the heart receives oxygenated blood from the lungs?,Left atrium,طب,100
What is the primary function of the large intestine?,Water absorption,طب,100
Which hormone is secreted by the thyroid gland?,Thyroxine (T4),طب,100
What is the term for slow heart rate?,Bradycardia,طب,100
Which type of muscle is found in the heart?,Cardiac muscle,طب,100
What is the medical term for vomiting?,Emesis,طب,100
Which organ produces insulin?,Pancreas,طب,100
What is the term for inflammation of the liver?,Hepatitis,طب,100
Which white blood cells are primarily involved in allergic reactions?,Eosinophils,طب,100
What is the normal range of oxygen saturation (SpO2)?,95-100%,طب,100
Which bone protects the brain?,Skull,طب,100
What is the functional unit of the lung?,Alveolus,طب,100
What is the medical term for nosebleed?,Epistaxis,طب,100
Which drug is commonly used as an antipyretic?,Paracetamol,طب,100
What is the term for inflammation of the joints?,Arthritis,طب,100
Which electrolyte is important for muscle contraction?,Calcium (Ca2+),طب,100
What is the medical term for fainting?,Syncope,طب,100
Which organ is responsible for producing urine?,Kidney,طب,100
What is the term for high blood calcium levels?,Hypercalcemia,طب,100
Which structure connects the throat to the stomach?,Esophagus,طب,100
What is the pharmacological class of amoxicillin?,Penicillin antibiotic,طب,100
Which condition is characterized by airway inflammation and bronchoconstriction?,Asthma,طب,100
What is the term for low blood pressure?,Hypotension,طب,100
Which part of the brain controls breathing?,Medulla oblongata,طب,100
What is the medical term for inflammation of the stomach?,Gastritis,طب,100
Which vitamin is important for blood clotting?,Vitamin K,طب,100
What is the route of administration under the tongue?,Sublingual,طب,100
A patient with low hemoglobin is likely suffering from what condition?,Anemia,طب,100
Which organ is most affected in myocardial infarction?,Heart,طب,100
A deficiency in insulin leads to which disease?,Diabetes mellitus,طب,100
What is the medical term for high blood sugar?,Hyperglycemia,طب,100
Which structure carries oxygenated blood from lungs to heart?,Pulmonary veins,طب,100
A patient with wheezing and shortness of breath likely has?,Asthma,طب,100
What is the normal respiratory rate in adults?,12-20 breaths/min,طب,100
Which organ is primarily responsible for detoxification?,Liver,طب,100
What is the term for inflammation of the bronchi?,Bronchitis,طب,100
Which drug is commonly used as an analgesic?,Ibuprofen,طب,100
What is the main function of white blood cells?,Immune الدفاع,طب,100
Which part of the brain controls voluntary movement?,Cerebrum,طب,100
What is the term for blood in urine?,Hematuria,طب,100
Which gland secretes adrenaline?,Adrenal gland,طب,100
A patient with persistent cough and fever may have?,Infection,طب,100
What is the term for low sodium levels?,Hyponatremia,طب,100
Which organ is affected in cirrhosis?,Liver,طب,100
What is the main function of the pancreas in digestion?,Secrete digestive enzymes,طب,100
Which structure prevents backflow of blood in veins?,Valves,طب,100
What is the term for difficulty swallowing?,Dysphagia,طب,100
Which drug is used to treat bacterial infections?,Antibiotics,طب,100
What is the normal range of blood glucose (fasting)?,70-100 mg/dL,طب,100
Which part of the eye controls the amount of light entering?,Iris,طب,100
What is the term for inflammation of the kidney?,Nephritis,طب,100
Which electrolyte imbalance can cause cardiac arrhythmias?,Potassium imbalance,طب,100
What is the route of drug administration into muscle?,Intramuscular (IM),طب,100
Which organ is responsible for gas exchange?,Lungs,طب,100
What is the term for rapid breathing?,Tachypnea,طب,100
Which condition involves decreased bone density?,Osteoporosis,طب,100
What is the main effect of diuretics?,Increase urine output,طب,100
A patient presents with tachycardia and low blood pressure. What is the likely condition?,Shock,طب,300
Which electrolyte imbalance is most associated with cardiac arrhythmias?,Potassium imbalance,طب,300
A patient with exophthalmos is most likely suffering from?,Graves disease,طب,300
What type of hypoxia occurs when hemoglobin cannot bind oxygen?,Anemic hypoxia,طب,300
Which drug class is used to treat hypertension by blocking angiotensin II receptors?,ARBs,طب,300
A deficiency of intrinsic factor leads to which condition?,Pernicious anemia,طب,300
Which part of the nephron is responsible for most water reabsorption?,Proximal convoluted tubule,طب,300
What is the mechanism of action of beta-blockers?,Block beta-adrenergic receptors,طب,300
A patient with elevated TSH and low T4 likely has?,Hypothyroidism,طب,300
Which bacteria is gram-positive and causes pneumonia?,Streptococcus pneumoniae,طب,300
What type of anemia is characterized by large red blood cells?,Macrocytic anemia,طب,300
Which artery is most commonly occluded in myocardial infarction?,Left anterior descending artery,طب,300
What is the pharmacological effect of ACE inhibitors?,Reduce angiotensin II production,طب,300
A patient with jaundice likely has dysfunction in which organ?,Liver,طب,300
Which hormone increases blood calcium levels?,Parathyroid hormone (PTH),طب,300
What is the primary neurotransmitter in the parasympathetic system?,Acetylcholine,طب,300
Which condition is associated with decreased bone mineral density?,Osteoporosis,طب,300
What type of drug is warfarin?,Anticoagulant,طب,300
A patient with polyuria and polydipsia may have?,Diabetes mellitus,طب,300
Which structure in the brain regulates body temperature?,Hypothalamus,طب,300
What is the most common cause of iron deficiency anemia?,Chronic blood loss,طب,300
Which drug is used as a bronchodilator in asthma?,Salbutamol,طب,300
What is the effect of aldosterone on the kidneys?,Increase sodium reabsorption,طب,300
Which condition results from excess cortisol?,Cushing syndrome,طب,300
What type of shock is caused by severe infection?,Septic shock,طب,300
Which vitamin deficiency leads to neurological symptoms and anemia?,Vitamin B12,طب,300
What is the main function of HDL?,Remove cholesterol from tissues,طب,300
Which organ is primarily affected in nephrotic syndrome?,Kidney,طب,300
What is the mechanism of action of NSAIDs?,Inhibit cyclooxygenase (COX),طب,300
A patient with chest pain radiating to the left arm likely has?,Myocardial infarction,طب,300
A patient with hyperkalemia is at risk of developing what complication?,Cardiac arrhythmias,طب,300
Which condition is characterized by insulin resistance?,Type 2 diabetes mellitus,طب,300
A patient presents with fatigue, pallor, and low MCV. What is the likely diagnosis?,Iron deficiency anemia,طب,300
What is the mechanism of action of metformin?,Decrease hepatic glucose production,طب,300
Which hormone is released in response to low blood pressure?,Renin,طب,300
A patient with severe dehydration will have what change in hematocrit?,Increased hematocrit,طب,300
Which part of the ECG represents ventricular depolarization?,QRS complex,طب,300
What is the primary cause of peptic ulcer disease?,Helicobacter pylori,طب,300
Which drug class is commonly used to reduce gastric acid secretion?,Proton pump inhibitors,طب,300
A patient with hypothyroidism may present with?,Weight gain,طب,300
Which electrolyte abnormality is seen in Addison disease?,Hyperkalemia,طب,300
What is the function of surfactant in the lungs?,Reduce surface tension,طب,300
A patient with unilateral weakness may have damage to which system?,Central nervous system,طب,300
Which condition is associated with increased intracranial pressure?,Brain tumor,طب,300
What is the main function of insulin?,Decrease blood glucose,طب,300
Which type of hypersensitivity is mediated by IgE?,Type I hypersensitivity,طب,300
A patient with productive cough and fever likely has?,Pneumonia,طب,300
Which enzyme is elevated in myocardial infarction?,Troponin,طب,300
What is the pharmacological action of diuretics?,Increase urine excretion,طب,300
Which condition is characterized by airway obstruction that is reversible?,Asthma,طب,300
A patient with low platelet count is at risk of?,Bleeding,طب,300
Which structure filters blood in the kidney?,Glomerulus,طب,300
What is the main cause of cirrhosis worldwide?,Chronic hepatitis,طب,300
Which drug is used to treat hypertension by reducing heart rate?,Beta-blockers,طب,300
A patient with severe allergic reaction requires which immediate treatment?,Epinephrine,طب,300
What is the effect of cortisol on metabolism?,Increase blood glucose,طب,300
Which organ is affected in pancreatitis?,Pancreas,طب,300
What is the most common cause of acute renal failure?,Hypoperfusion,طب,300
Which condition is associated with increased uric acid?,Gout,طب,300
What is the mechanism of action of statins?,Inhibit HMG-CoA reductase,طب,300
A patient presents with chest pain, ST elevation on ECG, and elevated troponin. What is the diagnosis?,STEMI,طب,500
A patient with metabolic acidosis has decreased pH and decreased HCO3-. What is the primary cause?,Acidosis due to bicarbonate loss or acid accumulation,طب,500
Which drug is contraindicated in patients with asthma due to bronchoconstriction risk?,Non-selective beta-blockers,طب,500
A patient presents with weight loss, heat intolerance, and low TSH. What is the diagnosis?,Hyperthyroidism,طب,500
Which condition results from increased preload and decreased cardiac output?,Heart failure,طب,500
A patient with microcytic anemia has low ferritin. What is the likely cause?,Iron deficiency anemia,طب,500
What is the mechanism of action of calcium channel blockers?,Inhibit calcium influx in cardiac and smooth muscle,طب,500
A patient with sudden unilateral facial droop likely has damage to which nerve?,Facial nerve (CN VII),طب,500
Which condition causes respiratory alkalosis?,Hyperventilation,طب,500
A patient with elevated LDL and low HDL is at risk of?,Atherosclerosis,طب,500
What is the pharmacological action of ACE inhibitors?,Block conversion of angiotensin I to II,طب,500
A patient presents with polyuria, hypernatremia, and low ADH. What is the diagnosis?,Diabetes insipidus,طب,500
Which organ is primarily responsible for gluconeogenesis?,Liver,طب,500
A patient with decreased GFR will have what effect on creatinine?,Increased creatinine,طب,500
What is the mechanism behind edema in nephrotic syndrome?,Loss of plasma proteins,طب,500
A patient presents with severe abdominal pain radiating to the back and elevated amylase. Diagnosis?,Acute pancreatitis,طب,500
Which electrolyte imbalance causes muscle weakness and arrhythmias?,Hypokalemia,طب,500
What is the primary cause of secondary hypertension?,Renal disease,طب,500
A patient with jaundice and elevated bilirubin likely has dysfunction in which pathway?,Bilirubin metabolism,طب,500
Which drug class is used to reduce cholesterol synthesis?,Statins,طب,500
A patient presents with fever, neck stiffness, and photophobia. Diagnosis?,Meningitis,طب,500
What is the effect of aldosterone excess?,Sodium retention and potassium loss,طب,500
A patient with low PaO2 but normal hemoglobin likely has?,Hypoxic hypoxia,طب,500
Which condition leads to decreased insulin production?,Type 1 diabetes mellitus,طب,500
What is the primary cause of peptic ulcer complications?,H. pylori infection,طب,500
A patient with prolonged bleeding time but normal platelet count likely has?,Platelet dysfunction,طب,500
Which structure is damaged in Parkinson disease?,Substantia nigra,طب,500
What is the mechanism of action of loop diuretics?,Inhibit Na-K-2Cl transporter,طب,500
A patient with confusion, tremor, and asterixis likely has?,Hepatic encephalopathy,طب,500
Which condition is associated with increased intracranial pressure and papilledema?,Brain tumor,طب,500
A patient presents with low pH, high PaCO2, and normal HCO3-. What is the diagnosis?,Respiratory acidosis,طب,500
A diabetic patient with fruity breath and high glucose likely has?,Diabetic ketoacidosis,طب,500
Which drug is first-line for acute anaphylaxis?,Epinephrine,طب,500
A patient with hyperthyroidism is treated with which drug to reduce hormone synthesis?,Methimazole,طب,500
A patient with increased PT and INR likely has deficiency in which vitamin?,Vitamin K,طب,500
Which condition is characterized by decreased surfactant production?,Neonatal respiratory distress syndrome,طب,500
A patient presents with muscle cramps and positive Trousseau sign. Diagnosis?,Hypocalcemia,طب,500
Which structure is primarily affected in multiple sclerosis?,Myelin sheath,طب,500
A patient with chronic alcohol use and confusion likely has deficiency of?,Vitamin B1 (Thiamine),طب,500
Which organ failure leads to uremia?,Kidney failure,طب,500
A patient with high TSH and high T4 suggests?,Secondary hyperthyroidism,طب,500
Which drug is used to inhibit platelet aggregation?,Aspirin,طب,500
A patient with bounding pulse and wide pulse pressure likely has?,Aortic regurgitation,طب,500
What is the mechanism of action of heparin?,Activate antithrombin III,طب,500
A patient with sudden vision loss in one eye likely has?,Retinal artery occlusion,طب,500
Which electrolyte imbalance causes tetany?,Hypocalcemia,طب,500
A patient with severe vomiting develops which acid-base disorder?,Metabolic alkalosis,طب,500
Which condition causes increased intracranial pressure and Cushing triad?,Brain hemorrhage,طب,500
A patient with low hemoglobin and high reticulocyte count suggests?,Hemolytic anemia,طب,500
Which drug is used to treat tuberculosis?,Rifampicin,طب,500
A patient with decreased cardiac output activates which system?,Renin-angiotensin system,طب,500
Which hormone is responsible for water reabsorption in kidneys?,ADH,طب,500
A patient with bradycardia and hypotension after beta-blocker overdose should receive?,Glucagon,طب,500
Which condition is associated with increased ESR?,Inflammation,طب,500
A patient with chronic cough, night sweats, and weight loss likely has?,Tuberculosis,طب,500
Which electrolyte is most abundant intracellularly?,Potassium,طب,500
A patient with high ammonia levels likely has dysfunction in?,Liver,طب,500
Which drug class reduces gastric acid by blocking histamine receptors?,H2 blockers,طب,500
A patient with flank pain and hematuria likely has?,Kidney stones,طب,500
Which structure is responsible for insulin secretion?,Beta cells of pancreas,طب,500
A 65-year-old male presents with crushing chest pain radiating to the left arm, sweating, and nausea. ECG shows ST elevation. What is the next best step?,Immediate reperfusion therapy (PCI),طب,1000
A patient with diabetes presents with polyuria, polydipsia, Kussmaul breathing, and high glucose. What is the primary pathology?,Diabetic ketoacidosis,طب,1000
A patient presents with low pH, low HCO3-, and compensatory low PaCO2. What is the diagnosis?,Metabolic acidosis with respiratory compensation,طب,1000
A patient with hypertension is given ACE inhibitors and develops dry cough. What is the cause?,Bradykinin accumulation,طب,1000
A 30-year-old female presents with fatigue, weight gain, cold intolerance, high TSH, and low T4. Diagnosis?,Primary hypothyroidism,طب,1000
A patient presents with sudden severe headache "worst of life". What is the likely diagnosis?,Subarachnoid hemorrhage,طب,1000
A patient with chronic alcohol use presents with confusion, ataxia, and ophthalmoplegia. Diagnosis?,Wernicke encephalopathy,طب,1000
A patient has hypercalcemia, kidney stones, and bone pain. What is the diagnosis?,Hyperparathyroidism,طب,1000
A patient presents with increased PT, PTT, and bleeding. What is the likely deficiency?,Vitamin K deficiency,طب,1000
A patient with asthma is given a non-selective beta-blocker and develops bronchospasm. Why?,Beta-2 receptor blockade,طب,1000
A patient presents with edema, proteinuria, and hypoalbuminemia. Diagnosis?,Nephrotic syndrome,طب,1000
A patient with liver cirrhosis develops confusion and asterixis. What is the cause?,Ammonia accumulation,طب,1000
A patient presents with fever, hypotension, and warm skin. What type of shock?,Septic shock,طب,1000
A patient with hyperkalemia shows peaked T waves on ECG. What is the immediate treatment?,Calcium gluconate,طب,1000
A patient presents with progressive dyspnea and bilateral crackles. Diagnosis?,Congestive heart failure,طب,1000
A patient with decreased ADH secretion presents with polyuria and hypernatremia. Diagnosis?,Diabetes insipidus,طب,1000
A patient presents with microcytic anemia and low ferritin. What is the cause?,Iron deficiency,طب,1000
A patient with tuberculosis is treated with rifampicin. What is a major side effect?,Hepatotoxicity,طب,1000
A patient presents with high LDL and plaque formation. What is the underlying pathology?,Atherosclerosis,طب,1000
A patient presents with increased intracranial pressure and papilledema. What is the next step?,Immediate CT scan,طب,1000
A patient presents with metabolic alkalosis after prolonged vomiting. What is the cause?,Loss of gastric acid,طب,1000
A patient with autoimmune destruction of beta cells develops?,Type 1 diabetes mellitus,طب,1000
A patient with sudden unilateral weakness and speech difficulty. Diagnosis?,Stroke,طب,1000
A patient with chronic NSAID use develops gastric ulcer. What is the mechanism?,COX inhibition reducing prostaglandins,طب,1000
A patient presents with hematuria and flank pain. What is the most likely diagnosis?,Renal stones,طب,1000
A patient with increased uric acid presents with joint pain in big toe. Diagnosis?,Gout,طب,1000
A patient with high T3 and T4 and low TSH. Diagnosis?,Primary hyperthyroidism,طب,1000
A patient with prolonged immobilization develops leg swelling and pain. Diagnosis?,Deep vein thrombosis,طب,1000
A patient presents with decreased GFR and elevated creatinine. What is the condition?,Renal failure,طب,1000
A patient with acute bacterial infection presents with high neutrophils. What is this called?,Neutrophilia,طب,1000


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
file_path = os.path.join(os.getcwd(), "medicine_questions.xlsx")

# حفظ البيانات في ملف Excel مع التأكد من استخدام مكتبة openpyxl
df.to_excel(file_path, index=False, engine="openpyxl")

print(f" تم حفظ {len(df)} سؤال في ملف {file_path} بنجاح!")
