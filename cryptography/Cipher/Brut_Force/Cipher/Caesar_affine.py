'''from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message'''

    
def modular_inverse(a):
    a = a % 26
    for x in range (1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def Brut_force_Caesar():
    mode = "menu_decryption"
    method = "menu_Caesar_affine"
    keys_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    all_possibilities = []
    #data = text_selection("text")
    #error = False
    while True:     
        '''header(method, "affine", mode)
        if error == True:
            error_message(["error_empty_text", "error_empty_key", "error_invalid_key_affine"])'''
        string = input("Entrez le texte à déchiffrer: \n")
        if not string:
            error = True
            continue
        for a in keys_a:
            a = modular_inverse(a)
            for b in range(0, 26):
                values = Caesar_affine(string, a, b)
                all_possibilities.append({"key": [a, b], "text": values[0]})
        return all_possibilities
                

def Caesar_affine(string, a, b):
        string_coded = ""
        keys = f"a = {a} and b = {b}"
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((a * (ord(c) - 97 - int(b)) ) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((a * (ord(c) - 65 - int(b))) % 26 + 65)
            else:
                string_coded += c
        error = False
        return string_coded, keys
