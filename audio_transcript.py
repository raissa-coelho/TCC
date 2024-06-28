
import os
import sys

import scripts.whisper_a as whisper_a
import scripts.vosk_a as vosk_a
import scripts.clean_audio as clean_audio
import scripts.calcula as calcula

# 1. Transcribe audio
# 2. Clean audio

def op(option, aux, model_number, dataset):

    if option == 1:
        if aux == "whisper":
            whisper_a.whisp_transcript(dataset, model_number)
        elif aux == "vosk":
            vosk_a.vosk_transcript(dataset, model_number)
        else:
            print("Error. No {aux} option available.")
    elif option == 2:
        clean_audio.data_cleaning(aux)
    elif option == 3:
        calcula.measure(dataset, aux)

if __name__ == "__main__": 
    if len(sys.argv) < 3:
        print("""Option 1 - Transcribe audio: 
                 Usage: python audio_transcript.py 1 aux model_number dataset
                 
                 Option 2 - Clean audio:
                 Usage: python audio_transcript.py 2 path_dataset 0 
                 
                 Option 3 - Calculate WER:
                 Usage: python audio_transcript.py 3 aux 0 dataset """)
        sys.exit(1)

    option = int(sys.argv[1])
    aux = str(sys.argv[2])
    aux2 = int(sys.argv[3])
    dataset = str(sys.argv[4])
    op(option, aux, aux2, dataset)