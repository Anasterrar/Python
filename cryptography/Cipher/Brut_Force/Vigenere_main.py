from Crack.Crack_Vigenere import Crack_Vigenere
from Vigenere.kasiski import kasiski
import os

PARAM_PROFILES = [
    {"top": 1,  "len_max": 60},
    {"top": 2,  "len_max": 15},
    {"top": 3,  "len_max": 10},
    {"top": 4,  "len_max": 8},
    {"top": 5,  "len_max": 7},
    {"top": 6,  "len_max": 7},
    {"top": 8,  "len_max": 6},
    {"top": 10, "len_max": 5},
    {"top": 13, "len_max": 5},
]

def formalize(text):
    result = ""
    for c in text:
        if c.isalpha():
            result += c
    return result.lower()

def set_top_len_ngram(text_len):
    # Texte très long → très facile
    if text_len > 400:
        return {"top": 1, "len_max": 100, "ngram" : 3}

    # Texte long
    if text_len > 250:
        return {"top": 2, "len_max": 16, "ngram" : 3}

    # Texte moyen
    if text_len > 150:
        return {"top": 5, "len_max": 7, "ngram" : 3}

    # Texte court
    if text_len > 80:
        return {"top": 10, "len_max": 5, "ngram" : 3}

    # Texte très court
    return {"top": 15, "len_max": 4, "ngram" : 2}

def get_params(string):
    params = {}
    params["text"] = string
    params["len"] = len(string)
    params["formalized_text"] = formalize(string)
    top_len_ngram = set_top_len_ngram(params["len"])
    params["top"] = top_len_ngram["top"]
    params["len_max"] = top_len_ngram["len_max"]
    params["Ngram"] = top_len_ngram["ngram"]
    params["Paternes"] = kasiski(params["formalized_text"], params["len_max"], params["Ngram"])
    if params["Paternes"] is not None:
        params["len_kasiski"] = len(params["Paternes"])
    return(params)

def Vigenere_main():
    while True:
        os.system('cls')
        text = input("text : ")
        params = get_params(text)
        if params["Paternes"] == None:
            print("Aucun paterne trouvé dans ce texte, le crack est impossible")
            input("ok")
            continue
        Crack_Vigenere(params)
        input("ok")
Vigenere_main()


