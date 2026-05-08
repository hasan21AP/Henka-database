from pathlib import Path
import unicodedata
import re

# Change this to your songs folder path
FOLDER_PATH = r"G:\Visual_Studio_Work_Place\Python Projects\downloads\My TOP 150 - Video Game Soundtracks"

# True = preview only, False = actually rename files
DRY_RUN = False

def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)

    replacements = {
        "⧸": "/",
        "／": "/",
        "｜": "|",
        "┃": "|",
        "：": ":",
        "＂": '"',
        "“": '"',
        "”": '"',
        "’": "'",
        "‘": "'",
        "؟": "?",
        "？": "?",
        "…": "...",
        "–": "-",
        "—": "-",
        "ْ": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


# Key = smart keyword found inside current filename
# Value = final clean filename without extension
rename_map = {
    "bowerlake": "Fable II - Bowerlake",
    "brotherhood of heroes": "Call of Duty WWII - A Brotherhood of Heroes",
    "a son's path": "God of War Ragnarok - A Son's Path",
    "watering hole in the harbor": "The Witcher 3 - A Watering Hole in the Harbor",
    "delphinus delphis": "ABZU - Delphinus Delphis",
    "danza alla daggers": "Assassin's Creed Syndicate - Danza Alla Daggers",
    "age of empires iv main theme": "Age of Empires IV - Main Theme",
    "alanwake - the clicker": "Alan Wake - The Clicker",
    "alan wake - the clicker": "Alan Wake - The Clicker",
    "alpha centauri": "Stellaris - Alpha Centauri",
    "amerzone": "Amerzone The Explorer's Legacy - Journey",
    "amethyst": "Trailer Music - Amethyst",
    "anthem - legion": "Anthem - Legion Of Dawn",
    "legion of dawn": "Anthem - Legion Of Dawn",
    "aplague": "A Plague Tale Innocence - Brother",
    "plaguetale - brother": "A Plague Tale Innocence - Brother",
    "arise - life": "Arise A Simple Story - Life",
    "steampunk ascent": "ARK Survival Evolved - Steampunk Ascent Main Theme",
    "wasteland war": "ARK Survival Evolved - Wasteland War Main Theme",
    "beer and friends": "Assassin's Creed III - Beer and Friends",
    "city of jerusalem": "Assassin's Creed - City of Jerusalem",
    "odyssey": "Assassin's Creed Odyssey - The Flight",
    "dreams of venice": "Assassin's Creed II - Dreams of Venice",
    "ezio's family": "Assassin's Creed II - Ezio's Family",
    "pyrates beware": "Assassin's Creed IV Black Flag - Pyrates Beware",
    "daughter of no one": "Assassin's Creed Mirage - Daughter of No One",
    "winds bazaar": "Assassin's Creed Mirage - The Wind's Bazaar",
    "wind's bazaar": "Assassin's Creed Mirage - The Wind's Bazaar",
    "legions of blood": "Assassin's Creed Origins - Legions of Blood",
    "jarls karls": "Assassin's Creed Valhalla - Jarls Karls and Thralls",
    "jarls, karls": "Assassin's Creed Valhalla - Jarls Karls and Thralls",
    "at sea": "Spiritfarer - At Sea",
    "old time battles": "Baldur's Gate 3 - Old Time Battles",
    "in case of trouble": "Bastion - In Case of Trouble",
    "battlefield theme": "Battlefield - Theme Chamber Version",
    "solomon": "Battlefield 3 - Solomon's Theme",
    "under no flag": "Battlefield V - Under No Flag",
    "welcome to fyrestone": "Borderlands - Welcome to Fyrestone",
    "byzantium": "Assassin's Creed Revelations - Byzantium",
    "baba yetu": "Civilization IV - Baba Yetu",
    "aurora's theme": "Child of Light - Aurora's Theme",
    "start a cult": "Cult of the Lamb - Start a Cult",
    "inkwell hell": "Cuphead - Inkwell Hell",
    "cyberpunk2077": "Cyberpunk 2077 - The Rebel Path",
    "rebel path": "Cyberpunk 2077 - The Rebel Path",
    "makers theme": "Darksiders II - The Makers Theme",
    "prisoner's awakening": "Dead Cells - Prisoner's Awakening",
    "deep space travels": "Stellaris - Deep Space Travels",
    "aurigas song": "Endless Legend - Auriga's Song",
    "auriga's song": "Endless Legend - Auriga's Song",
    "pillars of eternity": "Pillars of Eternity - Eora",
    "eora": "Pillars of Eternity - Eora",
    "bowerstone": "Fable - Bowerstone",
    "far cry 3": "Far Cry 3 - Main Theme",
    "farcry5": "Far Cry 5 - Now That This Old World Is Ending",
    "old world is ending": "Far Cry 5 - Now That This Old World Is Ending",
    "immortals fenyx": "Immortals Fenyx Rising - Fenyx's Dawn",
    "fenyx's dawn": "Immortals Fenyx Rising - Fenyx's Dawn",
    "finalfantasy13": "Final Fantasy XIII - Main Theme",
    "final fantasy xiii": "Final Fantasy XIII - Main Theme",
    "forgotten beast": "Dwarf Fortress - Forgotten Beast",
    "sunflower farm": "Ghost of a Tale - The Sunflower Farm",
    "gris": "GRIS - Pt 1",
    "last goodbye": "This War of Mine - The Last Goodbye",
    "soviet connection": "GTA IV - Soviet Connection",
    "mirage": "Jusant - Mirage",
    "hades - no escape": "Hades - No Escape",
    "no escape": "Hades - No Escape",
    "haloinfinite": "Halo Infinite - The Road",
    "halo infinite": "Halo Infinite - The Road",
    "the road": "Halo Infinite - The Road",
    "halowars": "Halo Wars - Spirit of Fire",
    "spirit of fire": "Halo Wars - Spirit of Fire",
    "home sweet home": "Beyond Good and Evil - Home Sweet Home",
    "dragon age": "Dragon Age Origins - Main Theme",
    "finding the pattern": "Everybody's Gone to the Rapture - Finding the Pattern",
    "journey - nascence": "Journey - Nascence",
    "nascence": "Journey - Nascence",
    "kingdomcome - blow": "Kingdom Come Deliverance - Blow",
    "kingdomcome - the dynasty": "Kingdom Come Deliverance - The Dynasty",
    "the dynasty": "Kingdom Come Deliverance - The Dynasty",
    "last light": "Baldur's Gate 3 - Last Light Tavern Version",
    "lazy afternoons": "Kingdom Hearts II - Lazy Afternoons",
    "legacy": "Tom Clancy's The Division - Legacy",
    "mass effect theme": "Mass Effect - Main Theme",
    "mass effect - main": "Mass Effect - Main Theme",
    "mass effect - the normandy": "Mass Effect - The Normandy",
    "masseffect - the normandy": "Mass Effect - The Normandy",
    "the normandy": "Mass Effect - The Normandy",
    "medal of honor (main theme)": "Medal of Honor - Main Theme",
    "allied assault": "Medal of Honor Allied Assault - Main Theme",
    "operation market garden": "Medal of Honor - Operation Market Garden",
    "melatonin - followers": "Melatonin - Followers",
    "followers": "Melatonin - Followers",
    "memories of memories": "TUNIC - Memories of Memories",
    "ori - im there too": "Ori and the Blind Forest - I'm There Too",
    "i'm there too": "Ori and the Blind Forest - I'm There Too",
    "lost in the storm": "Ori and the Blind Forest - Lost in the Storm",
    "ku's first flight": "Ori and the Will of the Wisps - Ku's First Flight",
    "timber hearth": "Outer Wilds - Timber Hearth",
    "past/present suite": "TV Series - Andor - Past Present Suite",
    "red dead redemption 2 mountain banjo": "Red Dead Redemption 2 - Mountain Banjo",
    "mountain banjo": "Red Dead Redemption 2 - Mountain Banjo",
    "riseoftheronin": "Rise of the Ronin - Loneliness",
    "loneliness": "Rise of the Ronin - Loneliness",
    "seaofthieves": "Sea of Thieves - A New Dawn",
    "a new dawn": "Sea of Thieves - A New Dawn",
    "shanghaied": "Trailer Music - Shanghaied",
    "silver for monsters": "The Witcher 3 - Silver for Monsters",
    "sims - mall rat": "The Sims - Mall Rat",
    "mall rat": "The Sims - Mall Rat",
    "sneakydriver": "Trailer Music - Sneaky Driver",
    "sneaky driver": "Trailer Music - Sneaky Driver",
    "spider-man": "Marvel's Spider-Man - Main Theme",
    "spiritfarer (main theme)": "Spiritfarer - Main Theme",
    "suicide mission": "Mass Effect 2 - Suicide Mission",
    "that's the way it is": "Red Dead Redemption 2 - That's the Way It Is",
    "canadian photographer": "A Plague Tale Innocence - The Canadian Photographer",
    "flight of the pigeon": "Battlefield 1 - The Flight of the Pigeon",
    "last of us part ii": "The Last of Us Part II - Main Theme",
    "megapithecus": "ARK Survival Evolved - The Megapithecus",
    "mountain trail": "Sea of Stars - The Mountain Trail Day",
    "myrtle gardens": "Humankind - The Myrtle Gardens",
    "ninth realm": "God of War - The Ninth Realm",
    "nearly peaceful place": "The Witcher 2 - A Nearly Peaceful Place",
    "titanfall2": "Titanfall 2 - Cosmology",
    "cosmology": "Titanfall 2 - Cosmology",
    "traverse town": "Kingdom Hearts - Traverse Town",
    "trine 2": "Trine 2 - Main Theme",
    "uncharted3": "Uncharted 3 - Nate's Theme",
    "nate's theme 3": "Uncharted 3 - Nate's Theme",
    "uncharted - nates theme": "Uncharted - Nate's Theme",
    "nate's theme": "Uncharted - Nate's Theme",
    "march of the moa": "Warframe - March of the Moa",
    "we are magonia": "Ghostrunner II - Loading",
    "we will not be forgotten": "The Banner Saga - We Will Not Be Forgotten",
    "wine-dark seas": "Assassin's Creed Odyssey - Wine-Dark Seas",
    "mystery man": "The Witcher 3 - Mystery Man",
    "studzanki": "World of Tanks - Studzianki",
    "studzianki": "World of Tanks - Studzianki",
    "you're... immortal": "The Witcher 3 - You're Immortal",
    "youre... immortal": "The Witcher 3 - You're Immortal",
    "temple of time": "The Legend of Zelda - Temple of Time",

    # Extra songs from the playlist screenshots
    "the ninth realm": "God of War - The Ninth Realm",
    "ori, lost in the storm": "Ori and the Blind Forest - Lost in the Storm",
    "world of tanks original soundtrack": "World of Tanks - Studzianki",
    "fallout 4 main theme": "Fallout 4 - Main Theme",
    "skogen": "Fe - Skogen",
    "between the fog": "Fe - Between the Fog",
    "brother": "A Plague Tale Innocence - Brother",
    "the beach, 7am": "The Sims - The Beach 7am",
    "march of the moa": "Warframe - March of the Moa",
}

# Normalize mapping keys once
normalized_map = {normalize(k): v for k, v in rename_map.items()}

def find_match(file_stem: str):
    name = normalize(file_stem)

    # Prefer longer keys first so "nate's theme 3" wins before "nate's theme"
    for key in sorted(normalized_map.keys(), key=len, reverse=True):
        if key in name:
            return normalized_map[key]

    return None

def safe_target_path(path: Path, new_stem: str) -> Path:
    target = path.with_name(new_stem + path.suffix)

    if not target.exists():
        return target

    counter = 2
    while True:
        candidate = path.with_name(f"{new_stem} ({counter}){path.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1

folder = Path(FOLDER_PATH)

if not folder.exists():
    raise FileNotFoundError(f"Folder not found: {folder}")

renamed = 0
skipped = 0

for file in folder.iterdir():
    if not file.is_file():
        continue

    new_stem = find_match(file.stem)

    if not new_stem:
        print(f"[SKIP] No mapping: {file.name}")
        skipped += 1
        continue

    if normalize(file.stem) == normalize(new_stem):
        print(f"[OK] Already clean: {file.name}")
        continue

    new_path = safe_target_path(file, new_stem)

    if DRY_RUN:
        print(f"[PREVIEW] {file.name}  ->  {new_path.name}")
    else:
        file.rename(new_path)
        print(f"[RENAMED] {file.name}  ->  {new_path.name}")

    renamed += 1

print("-" * 60)
print(f"Preview/Renamed count: {renamed}")
print(f"Skipped count: {skipped}")
print("Done.")
