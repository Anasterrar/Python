from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def formalize(data):
    data = data.replace(",", " ")
    data = data.split()
    return data

def poly_cipher():
    mode = "menu_encryption"
    error = False
    while True:
        method = "menu_Caesar_poly"
        header(method, "poly", mode)
        if error == True:
            error_message(["error_empty_text", "error_empty_key"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        keys = input_message("input_multiple_key")
        keys = formalize(keys)
        if not keys:
            error = True
            continue 
        string_coded = ""
        i = 0
        for c in string:
            if i > len(keys)- 1:
                i = 0
        #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 + int(keys[i])) % 26 + 97)
                i += 1
        #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 + int(keys[i])) % 26 + 65)
                i += 1
            else:
                string_coded += c
        keys = " ".join(keys)
        error = False
        return string, keys, string_coded, method