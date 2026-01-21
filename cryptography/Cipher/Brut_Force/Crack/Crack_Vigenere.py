from Vigenere.Vigenere_decrypt import Vigenere_decrypt
from Vigenere.kasiski import kasiski
from Vigenere.columns import set_columns, top_columns, extract_shift
from Vigenere.kasiski import calcul_possibles_len
from Scoring.letter_frequency import frequency_score
from Scoring.score import scoring
from itertools import product
import time
import os

def formalize(text):
    result = ""
    for c in text:
        if c.isalpha():
            result += c
    return result.lower()

def Crack_Vigenere(params):
    while True:
        text = params["text"]
        start = time.perf_counter()
        formalized_text = params["formalized_text"]

        #Detection des paternes
        paternes = params["Paternes"]
        
        #Detection des tailles de clés possibles
        possibles_len = calcul_possibles_len(paternes)

        #Création des colonnes
        all_colunms = {}
        for lenght in possibles_len:
            all_colunms[lenght] = set_columns(formalized_text, lenght)

        #Scoring des colonnes (meilleur clé césar, shift)
        all_cols_results = top_columns(all_colunms, params["top"])

        #extraction des shift par colonne
        all_shift_by_cols = extract_shift(all_cols_results, possibles_len)
        candidates = []
        for i in range(len(possibles_len)):
            for combinaison in product(*all_shift_by_cols[i]):
                text_dec = Vigenere_decrypt(text[:150], list(combinaison))
                candidates.append({
                    "text": text_dec, 
                    "key" : list(combinaison)
                    })

        #Scoring
        for candidate in candidates:
            freq = frequency_score(candidate["text"])
            score = min(freq["French"], freq["English"])
            candidate["score"] = score
        candidates.sort(key=lambda x: x["score"])
        shortlist = candidates[:50]   # variable
        best = scoring(shortlist)
        return best

