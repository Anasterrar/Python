from Cipher.Brut_Force.Crack.Crack_Vigenere import Crack_Vigenere
from Cipher.Brut_Force.Vigenere.kasiski import kasiski
from Cipher.Brut_Force.Vigenere.Vigenere_decrypt import Vigenere_decrypt
from Cipher.Brut_Force.Scoring.score import scoring
from Components.error_message import error_message
from Components.input_message import input_message
from Components.text_selection import text_selection
from colorama import Fore, Style
from Components.header import header

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

def Vigenere():
    data = text_selection("text")
    method = "menu_crack_vigenere"
    mode = "menu_decryption"
    error = False
    while True:
        header(method, "poly_cipher", mode)
        if error == True:
            error_message(["error_empty_text"])
        text = input_message("input_text")

        if not text:
            error = True
            continue

        formalized_text = formalize(text)
        if len(formalized_text) < 20:
            print(data["error_text_too_shoort"])
            input(data["press_enter"])
            continue

        kasiski_cache = {}
        print(Fore.YELLOW + Style.BRIGHT + data["waiting"])
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
            print(data["error_text_too_shoort"])
            input(data["press_enter"])
            continue

        best = scoring(bests)
        text_decoded = Vigenere_decrypt(text, best["key"])
        keys = "".join(chr(65 + k) for k in best["key"])
        
        return text, keys, text_decoded, method
    
def Vigenere_main():
    result = Vigenere()
    return result