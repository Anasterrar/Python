from Cipher.Brut_Force.Caesar.Ceasar import Caesar_decrypt
from Cipher.Brut_Force.Scoring.score import scoring
import os

def print_result(result):
    os.system('cls')
    print(f"\nClé trouvée : {result['key']}")
    print(f"Langue     : {result['langue']}")
    print(f"\nTexte clair:\n{result['text']}")
    input("ok")

def Crack_Ceasar():
    while True:
        os.system('cls')
        ciphertext = input("Texte chiffré: ")
        print(ciphertext.isalpha())
        if not ciphertext:
            continue
        possibilities = []
        for key in range(26):
            possibilities.append({
                "key": key,
                "text": Caesar_decrypt(ciphertext, key)
            })
        result = scoring(possibilities)
        print_result(result)