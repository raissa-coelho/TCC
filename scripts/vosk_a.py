
import vosk
import wave
import json

import os
import pandas as pd

# https://alphacephei.com/vosk/models
# model_number: 1 - vosk-model-small-pt-0.3
# model_number: 2 - vosk-model-pt-fb-v0.1.1-20220516_2113

def single_transcript(audio, model_number, output_txt):
    
    if model_number == 1:
        model = vosk.Model("/home/raissa/Documents/TCC/TCC/scripts/models/vosk-model-small-pt-0.3")
    elif model_number == 2:
        model = vosk.Model("/home/raissa/Documents/TCC/TCC/scripts/models/vosk-model-pt-fb-v0.1.1-20220516_2113")
    else:
        print("Invalid model number.")
        exit(1)

    wf = wave.open(audio, "rb")
    
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)
    
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            results.append(json.loads(result))

    f_result = json.loads(rec.FinalResult())
    results.append(f_result)

    for result in results:
        if "text" in result:
            print(f'Transcript:',result["text"])

def vosk_transcript(dataset, model_number):
    output_txt = "vosk_transcript.txt"
    # Read dataset
    path_complete = os.path.join(os.getcwd(), "scripts/audio/", dataset)
    df = pd.read_csv(path_complete)

     # find each file in cleaned_audio folder
    for i in range(len(df)):
        file = df.loc[i, "file_name"]
        input_file = os.path.join(os.getcwd(),"scripts/audio/cleaned_audio", file)

        single_transcript(input_file, model_number, output_txt)