from Cipher.Brut_Force.Crack.Crack_Vigenere import Crack_Vigenere
from Cipher.Brut_Force.Vigenere.kasiski import kasiski
from Cipher.Brut_Force.Vigenere.Vigenere_decrypt import Vigenere_decrypt
from Cipher.Brut_Force.Scoring.score import scoring
import os
import time

PARAM_PROFILES = [
    {"top": 1,  "len_max": 80, "ngram": 3},
    {"top": 2,  "len_max": 14, "ngram": 3},
    {"top": 3,  "len_max": 9,  "ngram": 3},
    {"top": 4,  "len_max": 7,  "ngram": 3},
    {"top": 5,  "len_max": 6,  "ngram": 3},
    {"top": 6,  "len_max": 5,  "ngram": 3},
    {"top": 7,  "len_max": 5,  "ngram": 3},
    {"top": 8,  "len_max": 5,  "ngram": 3},
    {"top": 9,  "len_max": 4,  "ngram": 2},
    {"top": 10, "len_max": 4,  "ngram": 2},
    {"top": 11, "len_max": 4,  "ngram": 2},
    {"top": 12, "len_max": 4,  "ngram": 2},
    {"top": 13, "len_max": 4,  "ngram": 2},
]

def formalize(text: str) -> str:
    return "".join(c for c in text if c.isalpha()).lower()

def print_result(text, best):
    text_decoded = Vigenere_decrypt(text, best["key"])
    key_alp = "".join(chr(65 + k) for k in best["key"])
    print(f"\n---------------Clé: {key_alp}---------------\n")
    print(f"\n---------------longueur de la clé: {len(key_alp)}---------------\n")
    print(f"Texte décodé:  \n{text_decoded}")

def Vigenere_main():
    while True:
        os.system('cls')
        text = input("text : ")
        start = time.perf_counter()

        formalized_text = formalize(text)
        if len(formalized_text) < 20:
            print("Texte trop court pour Kasiski (pas assez de répétitions).")
            input("ok")
            continue

        kasiski_cache = {}

        bests = []
        for profile in PARAM_PROFILES:

            key_cache = (profile["ngram"], profile["len_max"])
            if key_cache not in kasiski_cache:
                kasiski_cache[key_cache] = kasiski(formalized_text, profile["len_max"], profile["ngram"])

            paternes = kasiski_cache[key_cache]
            if paternes is None:
                continue

            params = {
                "text": text,
                "len": len(text),
                "formalized_text": formalized_text,
                "top": profile["top"],
                "len_max": profile["len_max"],
                "Ngram": profile["ngram"],
                "Paternes": paternes,
                "len_kasiski": len(paternes),
            }

            result = Crack_Vigenere(params)
            bests.append(result)

        if not bests:
            print("Erreur: pas de solution (aucun pattern détecté / texte trop court).")
            input("ok")
            continue

        best = scoring(bests)
        print_result(text, best)

        end = time.perf_counter()
        print(f"\n⏱ Temps écoulé : {end - start:.3f} secondes")
        input("ok")