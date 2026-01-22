from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def formalize(data):
    data = data.replace(",", " ")
    data = data.split()
    return data

def valid_key_poly(keys):
    valid_space = [" ", ","]
    digit = 0
    for key in keys:
        if key.isdigit():
            digit += 1
        if not key.isdigit():
            if key not in valid_space:
                return False
    if digit > 0:
        return True

def Poly_decipher(keys, string):
    string_coded = ""
    i = 0
    for c in string:
        if i > len(keys)- 1:
            i = 0
        #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            string_coded += chr((ord(c) - 97 - int(keys[i])) % 26 + 97)
            i += 1
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            string_coded += chr((ord(c) - 65 - int(keys[i])) % 26 + 65)
            i += 1
        else:
            string_coded += c
    return string_coded

def Poly():
    mode = "menu_encryption"
    method = "menu_Caesar_poly"
    error = False
    while True:
        header(method, "poly_decipher", mode)
        if error == True:
            error_message(["error_empty_text", "error_empty_key"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        keys = input_message("input_multiple_key")
        if not keys or valid_key_poly(keys) == False:
            error = True
            continue 
        keys = formalize(keys)
        string_coded = Poly_decipher(keys, string)
        keys = " ".join(keys)
        return string, keys, string_coded, method