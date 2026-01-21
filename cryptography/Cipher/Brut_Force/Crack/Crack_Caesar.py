from Cipher.Brut_Force.Caesar.Ceasar import Caesar_decrypt
from Cipher.Brut_Force.Scoring.score import scoring
from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def Crack_Ceasar():
    method = "menu_crack_caesar"
    mode = "menu_decryption"
    error = False
    while True:
        header(method, "crack_caesar", mode)
        if error == True:
            error_message(["error_empty_text"])
        text = input_message("input_text")

        if not text:
            error = True
            continue
        
        possibilities = []
        for key in range(26):
            possibilities.append({
                "key": key,
                "text": Caesar_decrypt(text, key)
            })
        result = scoring(possibilities)
        return text, result["key"], result["text"], method