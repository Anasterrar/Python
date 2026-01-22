from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def formalize(string):
    for c in string:
        if c.isalpha() == False:
            string = string.replace(c, '')
    return string

def valid_key_vigenere(keys):
    valid_space = [" ", ","]
    alpha = 0
    for key in keys:
        if key.isalpha():
            alpha += 1
        if not key.isalpha():
            if key not in valid_space:
                return False
    if alpha > 0:
        return True

def Vigenere_cipher(keys, string):
    string_coded = ""
    i = 0
    for c in string:
        if i > len(keys)- 1:
            i = 0
        #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            if ord(keys[i]) >= 97 and ord(keys[i]) <= 122:
                string_coded += chr((ord(c) - 97 + ord(keys[i]) - 97) % 26 + 97)
            elif ord(keys[i]) >= 65 and ord(keys[i]) <= 90:
                string_coded += chr((ord(c) - 97 + ord(keys[i]) - 65) % 26 + 97)
            i += 1
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            if ord(keys[i]) >= 97 and ord(keys[i]) <= 122:
                string_coded += chr((ord(c) - 65 + ord(keys[i]) - 97) % 26 + 65)
            elif ord(keys[i]) >= 65 and ord(keys[i]) <= 90:
                string_coded += chr((ord(c) - 65 + ord(keys[i]) - 65) % 26 + 65)
            i += 1
        else:
            string_coded += c
    return string_coded

def Vigenere():
    mode = "menu_encryption"
    method = "menu_vigenere"
    error = False
    while True:
        header(method, "vigenere_cipher", mode)
        if error == True:
            error_message(["error_empty_text", "error_empty_key"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        keys = input_message("input_word_key")    
        if not keys or valid_key_vigenere(keys) == False:
            error = True
            continue        
        keys = formalize(keys)     
        string_coded = Vigenere_cipher(keys, string)
        return string, keys, string_coded, method