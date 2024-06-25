import os
from pydub import AudioSegment

# Function to clean audio with pydub
def clean_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    cleaned_audio = audio.low_pass_filter(1000)
    cleaned_audio = audio.high_pass_filter(1000)
    cleaned_audio.export(output_file, format="wav")
    pass

if __name__ == "__main__":
    input_file = "scripts/audio/018.wav"
    output_file = "cleaned_audio.wav"
    clean_audio(input_file, output_file)