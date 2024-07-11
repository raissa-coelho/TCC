import whisper
import sys
import os
import pandas as pd
import csv

# only multilingual support
def single_transcript(file, model_number, output_txt):
    
    match model_number:
        case 1:
            model = whisper.load_model("tiny")
        case 2:
            model = whisper.load_model("base")
        case 3:
            model = whisper.load_model("small")
        case 4:
            model = whisper.load_model("medium")
        case 5:
            model = whisper.load_model("large")
        case _:
            print("Invalid model number")
            sys.exit(1)

    audio = os.path.join(os.getcwd(),"scripts/audio/cleaned_audio", file)
    # Bianca
    transcript = whisper.transcribe(model, audio, language="portuguese", fp16=False, verbose=True)

    out = os.path.join(os.getcwd(), "scripts/results/", output_txt)

    with open(out, "a", newline='', encoding='utf-8') as arq:
        escreve = csv.writer(arq)
        escreve.writerow([file, transcript["text"]])

# main function
def whisp_transcript(dataset, model_number):
    output_txt = "whisp_transcript.csv"
     # Read dataset
    path_complete = os.path.join(os.getcwd(), "scripts/audio/", dataset)
    df = pd.read_csv(path_complete)
    
    print(f'Starting ...')
    # find each file in cleaned_audio folder
    for i in range(len(df)):
        file = df.loc[i, "file_name"]

        single_transcript(file, model_number, output_txt)

    print(f'End.')