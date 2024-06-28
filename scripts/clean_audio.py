import os
import pandas as pd
from pydub import AudioSegment

# Function to clean audio with pydub
def clean_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    cleaned_audio = audio.low_pass_filter(1000)
    cleaned_audio = audio.high_pass_filter(1000)
    cleaned_audio.export(output_file, format="wav")
    pass

def data_cleaning(path_dataset):
    # Read dataset
    path_complete = os.path.join(os.getcwd(), path_dataset)
    df = pd.read_csv(path_complete)
    
    # Clean audio
    for i in range(len(df)):
        file = df.loc[i, "file_name"]
        input_file = os.path.join(os.getcwd(),"scripts/audio/pt/clips", file)

        folder = "scripts/audio/cleaned_audio"
        output_file = os.path.join(os.getcwd(), folder, file)
        
        clean_audio(input_file, output_file)