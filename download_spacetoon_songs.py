from yt_dlp import YoutubeDL

playlist_url = "https://www.youtube.com/playlist?list=PLbwI0LE0f2MH2neOMmvmQJHdPgw_iuQO9"

ydl_opts = {
    "outtmpl": "downloads/%(playlist_title)s/%(playlist_index)02d - %(title).120s.%(ext)s",
    "format": "bestaudio[ext=webm]/bestaudio",
    "ignoreerrors": True,
    "noplaylist": False,
    "windowsfilenames": True,

    "extractor_args": {
        "youtube": {
            "player_client": ["web", "android"]
        }
    },

    "js_runtimes": {
        "deno": {}
    },
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])