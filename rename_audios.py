from pathlib import Path
import re

folder = Path(r"G:\Visual_Studio_Work_Place\Python Projects\downloads\Anime Openings That Always Slap")

def clean_title(title):
    # حذف كلمات غير مهمة
    remove_words = [
        "opening", "op", "ending", "ed",
        "official", "video", "full", "hd", "4k"
    ]

    title = title.lower()

    for w in remove_words:
        title = re.sub(rf"\b{w}\b", "", title)

    # قص عند الرموز
    title = re.split(r"[-|•:()\[\]]", title)[0]

    # تنظيف
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = re.sub(r"\s+", " ", title).strip()

    return title.title()

for file in folder.iterdir():
    if not file.is_file():
        continue

    name = file.stem

    cleaned = clean_title(name)

    new_name = cleaned + file.suffix
    new_path = file.with_name(new_name)

    if new_path.exists():
        continue

    file.rename(new_path)
    print(f"{file.name} -> {new_name}")