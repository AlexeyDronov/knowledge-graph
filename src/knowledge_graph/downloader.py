def download_audio(url: str, ):
    import yt_dlp
    import os, pathlib

    target_dir = pathlib.Path(os.getcwd() + 'audio_files')
    target_dir.mkdir(exist_ok=True, parents=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio_files/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(info)
        ydl.download(url)
        