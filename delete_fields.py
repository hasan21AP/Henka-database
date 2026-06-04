import pandas as pd

# File path
file_path = r"G:\Visual_Studio_Work_Place\Python Projects\games_questions.xlsx"

# Read Excel file
df = pd.read_excel(file_path)

# Remove rows where only التصنيف contains "ألعاب"
# and the rest of the important columns are empty

df = df[
    ~(
        (df["التصنيف"] == "ألعاب") &
        (df["السؤال"].isna()) &
        (df["الإجابة"].isna()) &
        (df["النقاط"].isna())
    )
]

# Save file
df.to_excel(file_path, index=False)

print("Empty rows removed successfully.")