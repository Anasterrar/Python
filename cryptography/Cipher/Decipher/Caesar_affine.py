from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message

def isValidA(a):
    if a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        return True
    else:
        return False
    
def modular_inverse(a):
    a = a % 26
    for x in range (1, 26):
        if (a * x) % 26 == 1:
            return x
    return None

def Caesar_affine():
    mode = "menu_decryption"
    data = text_selection("text")
    error = False
    while True:
        method = "menu_Caesar_affine"
        header(method, "affine", mode)
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
        string_coded = ""
        keys = f"a = {a} {data["and"]} b = {b}"
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
        return string, keys, string_coded, method