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

def Vigenere_decipher(keys, string):
    string_decoded = ""
    i = 0

    for c in string:
        if i >= len(keys):
            i = 0

        if 'a' <= c <= 'z':
            base_c = ord('a')
            base_k = ord('a') if 'a' <= keys[i] <= 'z' else ord('A')
            string_decoded += chr(
                (ord(c) - base_c - (ord(keys[i]) - base_k)) % 26 + base_c
            )
            i += 1

        elif 'A' <= c <= 'Z':
            base_c = ord('A')
            base_k = ord('a') if 'a' <= keys[i] <= 'z' else ord('A')
            string_decoded += chr(
                (ord(c) - base_c - (ord(keys[i]) - base_k)) % 26 + base_c
            )
            i += 1

        else:
            string_decoded += c

    return string_decoded


def Vigenere():
    mode = "menu_encryption"
    method = "menu_vigenere"
    error = False
    while True:
        header(method, "vigenere_decipher", mode)
    
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
        string_coded = Vigenere_decipher(keys, string)
        return string, keys, string_coded, method