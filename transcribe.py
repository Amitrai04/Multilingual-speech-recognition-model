import torch
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf

def transcribe_audio(audio_path):
    processor = WhisperProcessor.from_pretrained("openai/whisper-base")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")

    audio_input, _ = sf.read(audio_path)
    input_features = processor(audio_input, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription
