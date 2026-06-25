import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.worldometers.info/geography/flags-of-the-world/"
folder = "flags"
os.makedirs(folder, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

for img in soup.select("img"):
    country = img.get("alt", "").strip()

    if not country:
        continue

    img_url = img.get("src")
    if not img_url:
        continue

    img_url = urljoin(url, img_url)

    safe_name = re.sub(r'[\\/*?:"<>|]', "", country)
    file_path = os.path.join(folder, f"{safe_name}.png")

    img_data = requests.get(img_url, headers=headers).content

    with open(file_path, "wb") as f:
        f.write(img_data)

    print(f"Downloaded: {safe_name}")

print("Done.")