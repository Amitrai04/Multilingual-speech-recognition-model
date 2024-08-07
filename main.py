import sys
import argparse
from transcribe import transcribe_audio
from query_rag import query_rag

def main(audio_file):
    transcription = transcribe_audio(audio_file)
    print("Transcription:", transcription)
    
    response = query_rag(transcription)
    print("RAG Response:", response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio and query RAG model.")
    parser.add_argument("--audio_file", type=str, required=True, help="Path to the audio file.")
    args = parser.parse_args()
    
    main(args.audio_file)
