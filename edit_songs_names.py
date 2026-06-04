import os
import re

folder = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\True Detective"

for filename in os.listdir(folder):

    old_path = os.path.join(folder, filename)

    # Skip folders
    if not os.path.isfile(old_path):
        continue

    name, ext = os.path.splitext(filename)

    # Remove leading numbers like:
    # 130 -
    # 001 -
    # 55 -
    new_name = re.sub(r'^\d+\s*-\s*', '', name).strip()

    # Rebuild filename
    new_filename = new_name + ext

    new_path = os.path.join(folder, new_filename)

    # Skip if same name
    if old_path == new_path:
        continue

    # If file already exists
    if os.path.exists(new_path):
        print(f"Skipped (already exists): {new_filename}")
        continue

    try:
        os.rename(old_path, new_path)
        print(f"Renamed:")
        print(f"  OLD: {filename}")
        print(f"  NEW: {new_filename}")
        print("-" * 50)

    except Exception as e:
        print(f"Error renaming {filename}")
        print(e)
        print("-" * 50)

print("Finished.")