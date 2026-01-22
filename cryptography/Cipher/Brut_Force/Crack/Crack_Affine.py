from Cipher.Decipher.Caesar_affine import Affine_decipher
from Cipher.Brut_Force.Scoring.score import scoring
from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

keys_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def modular_inverse(a):
    a = a % 26
    for x in range (1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def Crack_Affine():
    method = "menu_crack_affine"
    mode = "menu_decryption"
    error = False
    while True:
        header(method, "affine_cipher", mode)
        if error == True:
            error_message(["error_empty_text"])
        text = input_message("input_text")

        if not text:
            error = True
            continue
        
        possibilities = []
        for a in keys_a:
            a = modular_inverse(a)
            for b in range(0,26):
                possibilities.append({
                    "key": f"{a}, {b}",
                    "text": Affine_decipher(a, b, text)
                })
        result = scoring(possibilities)
        return text, result["key"], result["text"], method