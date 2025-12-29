from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def Caesar_Decipher():
    method = "menu_caesar"
    error = False
    while True:
        header(method, "caesar")
        if error == True:
            error_message(["error_empty_text", "error_empty_key"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        key = input_message("input_unique_key")
        if not key:
            error = True
            continue
        string_coded = ""
        key = int(key)
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 - key) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 - key) % 26 + 65)
            else:
                string_coded += c
        error = False
        return string, key, string_coded, method