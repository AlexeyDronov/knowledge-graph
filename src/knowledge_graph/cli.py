from __future__ import annotations
from typer import Typer, Argument, Option, echo
from typing_extensions import Annotated
# from rich import print
from pathlib import Path
# import subprocess
# import logging
# import sys
# from typing import Optional

app = Typer()

@app.command()
def download(
    url: Annotated[str, Option()],
    output_dir: Annotated[Path, Argument()] = Path('audio_files')
):
    from knowledge_graph import download_audio

    echo(f"Downloading from URL {url}")
    out = download_audio(url, output_dir)
    echo(f"File stored at {out}")

@app.command()
def transcribe(file: Annotated[Path, Option()]):
    echo(f"Transcribing file {file}")

if __name__ == "__main__":
    app()