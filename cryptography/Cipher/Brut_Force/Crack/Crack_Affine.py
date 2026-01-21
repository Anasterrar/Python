from Affine.Caesar_affine import Affine_decrypt
from Scoring.score import scoring
import os

keys_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def print_result(result):
    os.system('cls')
    print(f"\nClé trouvée : {result['key']}")
    print(f"Langue     : {result['langue']}")
    print(f"\nTexte clair:\n{result['text']}")
    input("ok")

def modular_inverse(a):
    a = a % 26
    for x in range (1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def Crack_Affine():
    while True:
        os.system('cls')
        ciphertext = input("Texte chiffré: ")
        print(ciphertext.isalpha())
        if not ciphertext:
            continue
        
        possibilities = []
        for a in keys_a:
            a = modular_inverse(a)
            for b in range(0,26):
                possibilities.append({
                    "key": f"{a}, {b}",
                    "text": Affine_decrypt(ciphertext, a, b)
                })
        result = scoring(possibilities)
        print_result(result)