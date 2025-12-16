from Components.header import header
from Components import text_selection
data = text_selection.text_selection("text")

def Caesar_cipher():
    error = False
    while True:
        method = data["menu_caesar"]
        header(method)
        if error == True:
            print(data["error_empty_text"])
            print(data["error_empty_key"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        key = input(data["input_unique_key"])
        if not key:
            error = True
            continue
        string_coded = ""
        key = int(key)
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 + key) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 + key) % 26 + 65)
            else:
                string_coded += c
        error = False
        return string, key, string_coded, method