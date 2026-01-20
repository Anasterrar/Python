from Vigenere.vigenere import Vigenere_decrypt
from Vigenere.kasiski import kasiski
from Vigenere.columns import set_columns, top_columns
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

def extract_shift(all_cols_results, possibles_len):
    all_shift_by_cols = []
    for lenght in possibles_len:
        shift_by_cols = []
        for col_result in all_cols_results[lenght]:
            shift_by_col = []
            for shift in col_result:
                shift_by_col.append(shift["shift"])
            shift_by_cols.append(shift_by_col)
        all_shift_by_cols.append( shift_by_cols)
    return all_shift_by_cols  

def Vigenere_main():
    while True:
        os.system("cls")
        text = input("text: ")
        start = time.perf_counter()
        formalized_text = formalize(text)

        #Detection des paternes
        paternes = kasiski(text)
        
        #Detection des tailles de clés possibles
        possibles_len = calcul_possibles_len(paternes)

        #Création des colonnes
        all_colunms = {}
        for lenght in possibles_len:
            all_colunms[lenght] = set_columns(formalized_text, lenght)

        #Scoring des colonnes (meilleur clé césar, shift)
        all_cols_results = top_columns(all_colunms)

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
        text_decoded = Vigenere_decrypt(text, best["key"])

        #Clé
        key_alp = ""
        for key_num in best["key"]: 
            key_alp += chr(65 + key_num)

        #Print du résulat
        print(f"\n---------------Clé: {key_alp}---------------\n")
        print(f"\n---------------longueur de la clé: {len(key_alp)}---------------\n")
        print(f"Texte décodé:  \n {text_decoded}")
        end = time.perf_counter()
        print(f"\n⏱ Temps écoulé : {end - start:.3f} secondes")
        input("ok")

Vigenere_main()