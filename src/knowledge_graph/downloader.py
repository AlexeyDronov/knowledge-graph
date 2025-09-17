from __future__ import annotations
from pathlib import Path

def download_audio(url: str, output_dir: str | Path):
    import yt_dlp

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(output_path / '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 1. Extracts video info without downloading
        info = ydl.extract_info(url, download=False)
        # 2. Downloads the audio
        ydl.download([url])
        # 3. Extract the path where the video was stored
        downloaded_path = Path(ydl.prepare_filename(info)).with_suffix('.mp3')
        return downloaded_path
