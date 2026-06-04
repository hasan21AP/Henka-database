from yt_dlp import YoutubeDL

video_url = "https://www.youtube.com/watch?v=mfFnCL_fdU4&list=PLu2SKVHcRFLobuTmDMG9z5cZNzrogLbn5&index=54"

ydl_opts = {
    "outtmpl": "downloads/%(title).120s.%(ext)s",
    "format": "bestaudio/best",
    "noplaylist": True,
    "windowsfilenames": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])