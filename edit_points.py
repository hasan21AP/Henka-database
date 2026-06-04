import os
import pandas as pd

# Folder path
folder_path = r"G:\Visual_Studio_Work_Place\Python Projects"

# Files you want to modify
target_files = [
    "anime_songs_questions.xlsx",
    "games_soundtracks_questions.xlsx",
    "songs_questions.xlsx",
    "spacetoon_songs_questions.xlsx"
]

# New points value
new_points = 250

# Points column name
points_column = "النقاط"

for file_name in target_files:
    file_path = os.path.join(folder_path, file_name)

    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Check if column exists
        if points_column in df.columns:
            # Replace all values
            df[points_column] = new_points

            # Save file
            df.to_excel(file_path, index=False)

            print(f"Updated: {file_name}")

        else:
            print(f"'النقاط' column not found in: {file_name}")

    except Exception as e:
        print(f"Error in {file_name}: {e}")

print("Done.")