
import os
import sys
import pandas as pd
import csv
import jiwer

def wer(ground_truth, hypothesis):
    referencia = []
    hipotese = []

    gt = os.path.join(os.getcwd(), "scripts/audio/", ground_truth)
    hypo = os.path.join(os.getcwd(), "scripts/results/", hypothesis)

    with open(gt, "r", encoding='utf-8') as f:
        ler = csv.DictReader(f)
        for linha in ler:
            referencia.append(linha["transcript"])
    
    with open(hypo, "r", encoding='utf-8') as f:
        ler = csv.DictReader(f)
        for linha in ler:
            hipotese.append(linha["transcript"])
    
    transform = jiwer.Compose([jiwer.RemovePunctuation(), 
                               jiwer.RemoveMultipleSpaces(),
                               jiwer.ToLowerCase(),
                               jiwer.Strip()])

    wer = jiwer.wer(referencia, hipotese, truth_transform=transform, hypothesis_transform=transform)
    print(f'WER: {wer}')