from __future__ import annotations
from typer import Typer, Option, echo
from typing_extensions import Annotated
from typing import Union
# from rich import print
from pathlib import Path
# import subprocess
# import logging
# import sys
# from typing import Optional

app = Typer()

@app.command()
def download(url: Annotated[str, Option()]):
    from knowledge_graph import download_audio
    echo(f"Downloading from URL {url}")
    download_audio(url)

@app.command()
def transcribe(file: Annotated[Path, Option()]):
    echo(f"Transcribing file {file}")

if __name__ == "__main__":
    app()