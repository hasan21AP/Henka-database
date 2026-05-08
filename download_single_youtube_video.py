from yt_dlp import YoutubeDL

video_url = "https://www.youtube.com/watch?v=5RVEM8-UKlg&list=RD5RVEM8-UKlg&start_radio=1"

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