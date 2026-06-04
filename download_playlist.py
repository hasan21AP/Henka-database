from yt_dlp import YoutubeDL

playlist_url = "https://www.youtube.com/playlist?list=PLic3kGSVdYqPmFLmVrENaLoqW1RGKb3eE"

ydl_opts = {
    "outtmpl": "downloads/%(playlist_title)s/%(playlist_index)02d - %(title).120s.%(ext)s",
    "format": "bestaudio/best",
    "ignoreerrors": True,
    "noplaylist": False,
    "windowsfilenames": True,
    "restrictfilenames": False,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])