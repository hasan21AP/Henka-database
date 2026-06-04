import os
import yt_dlp

playlist_url = input("Enter playlist URL: ").strip()

download_folder = "downloads/True Detective"
os.makedirs(download_folder, exist_ok=True)

ydl_opts = {
    # Best 1080p60 video + best audio
    "format": "bv*[height<=1080][fps<=60]+ba/b",

    # Skip videos longer than 6 minutes
    "match_filter": yt_dlp.utils.match_filter_func(
        "duration < 360"
    ),

    # Save path
    "outtmpl": os.path.join(
        download_folder,
        "%(playlist_index)03d - %(title)s.%(ext)s"
    ),

    # Force mp4 output
    "merge_output_format": "mp4",

    # Playlist mode
    "noplaylist": False,

    # Continue on errors
    "ignoreerrors": True,

    # Better filenames on Windows
    "windowsfilenames": True,

    # Use ffmpeg to merge
    "postprocessors": [{
        "key": "FFmpegMerger",
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("Done.")