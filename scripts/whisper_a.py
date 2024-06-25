import whisper
import sys

# only multilingual support
def whisp_transcript(audio, model_number):
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

    transcript = whisper.transcribe(model, audio)
    print(transcript["text"])