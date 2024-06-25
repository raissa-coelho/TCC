
import os
import sys

import scripts.whisper_a as whisper_a
import scripts.vosk_a as vosk_a

# 1. Transcribe audio
# 2. Clean audio

def op(option, aux, model_number):

    if option == 1:
        if aux == "whisper":
            audio = "cleaned_audio.wav"
            whisper_a.whisp_transcript(audio, model_number)
        elif aux == "vosk":
            audio = "cleaned_audio.wav"
            vosk_a.vosk_transcript(audio, model_number)

if __name__ == "__main__": 
    if len(sys.argv) < 3:
        print("""Option 1 - Transcribe audio with Whisper
                 Usage: python audio_transcript.py option model""")
        sys.exit(1)

    option = int(sys.argv[1])
    aux = str(sys.argv[2])
    model_number = int(sys.argv[3])
    op(option, aux, model_number)