import os
import re

folder_path = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\My TOP 150 - Video Game Soundtracks"

for file in os.listdir(folder_path):
    if file.lower().endswith(".mp3"):
        old_path = os.path.join(folder_path, file)

        # حذف الرقم + المسافة + الشرطة من البداية
        new_name = re.sub(r"^\d+\s*-\s*", "", file)

        new_path = os.path.join(folder_path, new_name)

        # إعادة التسمية
        os.rename(old_path, new_path)

        print(f"Renamed: {file} -> {new_name}")

print("Done ✅")