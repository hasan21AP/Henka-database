import os
import re
import time
import requests

IMAGES_DIR = "football_players_images"
os.makedirs(IMAGES_DIR, exist_ok=True)

PLAYERS = [
    # Premier League (أسماء أدق)
    "Declan Rice", "Kai Havertz", "Leandro Trossard", "Ben White", "Oleksandr Zinchenko",
    "Dominik Szoboszlai", "Alexis Mac Allister", "Curtis Jones", "Ibrahima Konate",
    "Joao Palhinha", "Eberechi Eze", "Michael Olise", "Jarrod Bowen", "Lucas Paqueta",
    "Pedro Neto", "Matheus Cunha", "Hwang Hee-chan",

    # La Liga
    "Joselu", "Dani Carvajal", "Nacho Fernandez footballer", "Fran Garcia footballer",
    "Fermin Lopez", "Lamine Yamal", "Inigo Martinez", "Alejandro Balde",
    "Yangel Herrera", "Aleix Garcia", "Borja Iglesias",

    # Serie A
    "Gleison Bremer", "Danilo footballer 1991", "Adrien Rabiot",
    "Weston McKennie", "Federico Chiesa", "Arkadiusz Milik",
    "Stefan de Vrij", "Francesco Acerbi", "Henrikh Mkhitaryan",
    "Davide Frattesi", "Giacomo Raspadori", "Matteo Politano",

    # Bundesliga
    "Jonathan Tah", "Edmond Tapsoba", "Patrik Schick",
    "Niclas Fullkrug", "Julian Brandt", "Emre Can",
    "Karim Adeyemi", "Sebastien Haller footballer",
    "Christopher Nkunku", "Dani Olmo footballer",

    # Ligue 1
    "Warren Zaire-Emery", "Bradley Barcola", "Vitinha footballer 2000",
    "Fabian Ruiz", "Lucas Hernandez", "Presnel Kimpembe",

    # Others Europe
    "Orkun Kokcu", "Kerem Akturkoglu", "Dusan Tadic",
    "Edin Dzeko", "Romelu Lukaku", "Ciro Immobile",
    "Sergej Milinkovic-Savic", "Filip Kostic", "Dusan Vlahovic",
    "Teun Koopmeiners", "Marten de Roon", "Giorgio Scalvini",
    "Charles De Ketelaere", "Noa Lang",

    # Young talents
    "Arda Guler", "Endrick footballer", "Vitor Roque",
    "Xavi Simons", "Rayan Cherki", "Evan Ferguson",
    "Benjamin Sesko", "Mathys Tel", "Alejandro Garnacho",
    "Facundo Buonanotte"
]


def safe_filename(name):
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_") + ".jpg"


def get_wikipedia_thumbnail(player_name):
    title = player_name.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"

    headers = {
        "User-Agent": "HenkaGame/1.0"
    }

    response = requests.get(url, headers=headers, timeout=20)

    if response.status_code != 200:
        return None

    data = response.json()

    thumbnail = data.get("thumbnail", {})
    image_url = thumbnail.get("source")

    return image_url


def download_image(image_url, save_path):
    headers = {
        "User-Agent": "HenkaGame/1.0"
    }

    response = requests.get(image_url, headers=headers, timeout=20)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(response.content)


downloaded = 0
failed = []

for player in PLAYERS:
    filename = safe_filename(player)
    save_path = os.path.join(IMAGES_DIR, filename)

    if os.path.exists(save_path):
        print(f"Skipped existing: {filename}")
        continue

    try:
        image_url = get_wikipedia_thumbnail(player)

        if not image_url:
            print(f"No image found: {player}")
            failed.append(player)
            continue

        download_image(image_url, save_path)

        downloaded += 1
        print(f"Downloaded {downloaded}: {filename}")

        time.sleep(1)

    except Exception as e:
        print(f"Failed: {player} -> {e}")
        failed.append(player)
        time.sleep(2)


print("\nDone!")
print(f"Downloaded: {downloaded}")
print(f"Images folder: {IMAGES_DIR}")

if failed:
    print("\nFailed players:")
    for name in failed:
        print("-", name)