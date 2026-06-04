import re
import subprocess
from pathlib import Path


# Put any TikTok video URL or profile URL here
URL = "https://www.tiktok.com/@lilium_creative/video/7629745089056705812"

OUTPUT_DIR = "tiktok_downloads"


def extract_profile_url(url: str) -> str:
    match = re.search(r"tiktok\.com/@([^/]+)", url)
    if not match:
        raise ValueError("Could not find TikTok username in the URL")

    username = match.group(1)
    return f"https://www.tiktok.com/@{username}"


def download_profile_videos(profile_url: str):
    Path(OUTPUT_DIR).mkdir(exist_ok=True)

    command = [
        "yt-dlp",
        profile_url,

        # Download best video/audio
        "-f", "best",

        # File name: caption/title + video id
        "-o", f"{OUTPUT_DIR}/%(title).120s [%(id)s].%(ext)s",

        # Avoid downloading same video twice
        "--download-archive", f"{OUTPUT_DIR}/downloaded.txt",

        # Save metadata beside video
        "--write-info-json",

        # Continue even if one video fails
        "--ignore-errors",

        # Better filenames for Windows
        "--windows-filenames",
    ]

    subprocess.run(command, check=False)


if __name__ == "__main__":
    profile_url = extract_profile_url(URL)
    print(f"Downloading from: {profile_url}")
    download_profile_videos(profile_url)