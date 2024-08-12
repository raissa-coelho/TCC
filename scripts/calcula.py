
import os
import sys
import pandas as pd
import csv
import jiwer

def measure(ground_truth, aux):
    referencia = []
    hipotese = []

    if aux == "whisper":
        hypothesis = "whisp_transcript_small.csv"
    elif aux == "vosk":
        hypothesis = "vosk_transcript.csv"

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
    				            jiwer.RemoveEmptyStrings(),
                               jiwer.RemoveMultipleSpaces(),
                               jiwer.ToLowerCase(),
                               jiwer.Strip()])

    transform_ref = [transform(ref) for ref in referencia]
    transform_hyp = [transform(hyp) for hyp in hipotese]

    #for i in range(len(transform_ref)):
    #    print(f'File: {i+1}')
    #    print(f'Reference: {transform_ref[i]}')
    #    print(f'Hypothesis: {transform_hyp[i]}')
    #    print()

    #out = jiwer.process_words(transform_ref, transform_hyp)
    #print(jiwer.visualize_alignment(out))

    # Calculate WER - Word Error Rate
    wer = jiwer.wer(transform_ref, transform_hyp)
    print(f'WER: {wer} -- {wer * 100:.2f}%')

    # Calculate MER - Match Error Rate
    mer = jiwer.mer(transform_ref, transform_hyp)
    print(f'MER: {mer} -- {mer * 100:.2f}%')

    # Calculate WIL - Word Information Lost
    wil = jiwer.wil(transform_ref, transform_hyp)
    print(f'WIL: {wil} -- {wil * 100:.2f}%')

    # Calculate WIP - Word Information Preserved
    wip = jiwer.wip(transform_ref, transform_hyp)
    print(f'WIP: {wip} -- {wip * 100:.2f}%')

    # Calculate CER - Character Error Reference
    cer = jiwer.cer(transform_ref, transform_hyp)
    print(f'CER: {cer} -- {cer * 100:.2f}%')

    path_out = "/home/hworld/Downloads/Raissa - TCC/TCC/scripts/results/"
    
    output = os.path.join(path_out, "whisper_small.txt")
    
    wer1 = f'{wer* 100:.2f}'
    mer1 = f'{mer* 100:.2f}'
    wil1 = f'{wil* 100:.2f}'
    wip1 = f'{wip* 100:.2f}'
    cer1 = f'{cer* 100:.2f}'
    
    with open(output, 'w') as f:
        f.write('Whisper Small' + '\n')
        f.write('Wer: ' + wer1 + '%' + '\n')
        f.write('Mer: ' + mer1 + '%' + '\n')
        f.write('Wil: ' + wil1 + '%' + '\n')
        f.write('Wip: ' + wip1 + '%' + '\n')
        f.write('Cer: ' + cer1 + '%')
