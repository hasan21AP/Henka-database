from pathlib import Path
import unicodedata

FOLDER_PATH = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\My TOP 150 - Video Game Soundtracks"
DRY_RUN = True

def normalize(text):
    # Convert weird unicode chars to normal ones
    text = unicodedata.normalize("NFKD", text)

    replacements = {
        "⧸": "/",
        "｜": "|",
        "：": ":",
        "＂": '"',
        "’": "'",
        "‘": "'",
        "…": "...",
        "؟": "?",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text.strip().lower()


# نفس mapping القديم متاعك (ما تغيرهش)
rename_map = {
    # حط هنا القائمة الكبيرة القديمة كاملة كما هي
    "4 Bowerlake": "Fable - Bowerlake",
    "A Brotherhood of Heroes": "Call of Duty WWII - A Brotherhood of Heroes",
    "A Watering Hole in the Harbor": "The Witcher 3 - A Watering Hole in the Harbor",
    "ABZU - Delphinus Delphis - As Noted": "ABZU - Delphinus Delphis",
    "Age of Empires IV Main Theme": "Age of Empires IV - Main Theme",
    "AlanWake - The Clicker": "Alan Wake - The Clicker",
    "Alpha Centauri (From Stellaris Original Game Soundtrack)": "Stellaris - Alpha Centauri",
    "Amethyst": "Trailer Music - Amethyst",

    # زيد الباقي من القائمة الكبيرة...

    # هذه الإضافات اللي كانت SKIP بسبب الرموز
    "4  Bowerlake": "Fable - Bowerlake",
    "A Son's Path (From ＂God of War Ragnarök＂ Soundtrack)": "God of War Ragnarok - A Son's Path",
    "AC Syndicate OST ⧸ Austin Wintory  - Danza alla Daggers": "Assassin's Creed Syndicate - Danza Alla Daggers",
    "Amerzone： The Explorer's Legacy - OST - Journey - Inon Zur & Ori Zur": "Amerzone The Explorer's Legacy - Journey",
    "Assassin's Creed 2 OST ⧸ Jesper Kyd - Dreams of Venice (Track 13)": "Assassin's Creed II - Dreams of Venice",
    "Assassin's Creed 2 OST ⧸ Jesper Kyd - Ezio's Family (Track 03)": "Assassin's Creed II - Ezio's Family",
    "Assassin's Creed ｜ Assassin's Creed Odyssey (OST) ｜ The Flight": "Assassin's Creed Odyssey - The Flight",
    "Assassins Creed Valhalla - Jarls Karls And Thralls": "Assassin's Creed Valhalla - Jarls Karls and Thralls",
    "Assassin’s Creed 3 ⧸ Lorne Balfe - Beer and Friends (Track 20)": "Assassin's Creed III - Beer and Friends",
    "Cult of the Lamb  - Start a Cult": "Cult of the Lamb - Start a Cult",
    "Cœur de pirate - Aurora's Theme ｜｜ Child of Light": "Child of Light - Aurora's Theme",
    "Guillaume Ferran - Mirage ｜ Jusant Official Soundtrack": "Jusant - Mirage",
    "Home Sweet Home ｜ Beyond Good and Evil 20th Anniversary (OST) ｜ Christophe Héral": "Beyond Good and Evil - Home Sweet Home",
    "Inon Zur - Main Theme ｜ Dragon Age： Origins (OST)": "Dragon Age Origins - Main Theme",
    "Jessica Curry - Finding the Pattern ｜ Everybody's Gone to the Rapture (Original Soundtrack)": "Everybody's Gone to the Rapture - Finding the Pattern",
    "Medal Of Honor： Allied Assault (Main Theme)": "Medal of Honor Allied Assault - Main Theme",
    "Past⧸Present Suite": "TV Series - Andor - Past Present Suite",
    "Silver For Monsters....": "The Witcher 3 - Silver for Monsters",
    "Spiritfarer (Main Theme) -  Max LL": "Spiritfarer - Main Theme",
    "The Ninth Realm (From ＂God of War＂ Soundtrack)": "God of War - The Ninth Realm",
    "The Witcher 2 Soundtrack ｜ A Nearly Peaceful Place ｜ The Witcher 2 OST Music": "The Witcher 2 - A Nearly Peaceful Place",
    "World of Tanks Original Soundtrack： Studzianki": "World of Tanks - Studzianki",
    "You're... Immortal？": "The Witcher 3 - You're Immortal",
}


folder = Path(FOLDER_PATH)

for file in folder.iterdir():
    if not file.is_file():
        continue

    original_name = file.stem
    normalized_name = normalize(original_name)

    if normalized_name not in rename_map:
        print(f"[SKIP] No mapping: {file.name}")
        continue

    new_name = rename_map[normalized_name] + file.suffix
    new_path = file.with_name(new_name)

    if new_path.exists():
        print(f"[SKIP] Already exists: {new_name}")
        continue

    if DRY_RUN:
        print(f"[PREVIEW] {file.name}  ->  {new_name}")
    else:
        file.rename(new_path)
        print(f"[RENAMED] {file.name}  ->  {new_name}")

print("Done.")