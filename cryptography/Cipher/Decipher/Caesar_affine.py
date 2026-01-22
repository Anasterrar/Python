from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message

valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def isValidA(a):
    if a in valid_a:
        return True
    else:
        return False
    
def modular_inverse(a):
    a = a % 26
    for x in range (1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def Affine_decipher(a, b, string):
    string_coded = ""
    for c in string:
        #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            string_coded += chr((a * (ord(c) - 97 - int(b)) ) % 26 + 97)
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            string_coded += chr((a * (ord(c) - 65 - int(b))) % 26 + 65)
        else:
            string_coded += c
        
    return string_coded

def Affine():
    mode = "menu_decryption"
    data = text_selection("text")
    error = False
    while True:
        method = "menu_Caesar_affine"
        header(method, "affine_decipher", mode)
        if error == True:
            error_message(["error_empty_text", "error_empty_key", "error_invalid_key_affine"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        a = input_message("input_first_key")
        if not a or a.isdigit() == False or isValidA(int(a)) == False:
            error = True
            continue
        a = modular_inverse(int(a))
        b = input_message("input_second_key")
        if not b or b.isdigit() == False:
            error = True
            continue
        string_coded = Affine_decipher(a , b, string)
        keys = f"a = {a} {data["and"]} b = {b}"
        error = False
        return string, keys, string_coded, method