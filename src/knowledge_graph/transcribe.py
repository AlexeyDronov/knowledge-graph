from pathlib import Path
from typing import cast, Dict

def transcribe_audio(audio_path: str | Path, model_s: str = "large"):
    import torch
    from transformers import pipeline

    device = torch.device('mps') if torch.mps.is_available() else torch.device('cpu')

    pipe = pipeline(
        "automatic-speech-recognition",
        model=f"openai/whisper-{model_s}",
        chunk_length_s=30,
        device=device,
    )
    res = cast(Dict[str, str], pipe(str(audio_path)))

    txt_path = audio_path.stem + '.txt'
    with open(Path('transcriptions') / txt_path, 'w') as f_out:
        f_out.write(res['text'])