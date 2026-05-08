import subprocess
from pathlib import Path

folder = Path(r"G:\Visual_Studio_Work_Place\Python Projects\downloads\شارات أعمال سبيستون")

ffmpeg_path = r"C:\ffmpeg-8.1.1\bin\ffmpeg.exe" # عدل حسب مكانك

for file in folder.glob("*.mp4"):
    output_file = file.with_suffix(".webm")

    command = [
        ffmpeg_path,
        "-i", str(file),
        "-vn",
        "-c:a", "libopus",
        "-b:a", "192k",
        str(output_file)
    ]

    print(f"Converting: {file.name}")
    subprocess.run(command)

print("Done ✅")