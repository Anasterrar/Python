from Caesar.Ceasar import caesar_decrypt
from Scoring.score import scoring
import os

def print_result(result):
    os.system('cls')
    print(f"\nClé trouvée : {result['key']}")
    print(f"Langue     : {result['langue']}")
    print(f"\nTexte clair:\n{result['text']}")
    input("ok")

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
            "text": caesar_decrypt(ciphertext, key)
        })
    result = scoring(possibilities)
    print_result(result)


