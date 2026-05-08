from yt_dlp import YoutubeDL

playlist_url = "https://www.youtube.com/watch?v=e-ORhEE9VVg&list=PLplXQ2cg9B_qrCVd1J_iId5SvP8Kf_BfS"

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