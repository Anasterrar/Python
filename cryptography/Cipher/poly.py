from Components.header import header
from Components import text_selection

def formalize(data):
    data = data.replace(",", " ")
    data = data.split()
    return data

def poly_cipher():
    data = text_selection.text_selection("text")
    error = False
    while True:
        method = data["menu_Caesar_poly"]
        header(method)
        if error == True:
            print(data["error_empty_text"])
            print(data["error_empty_key"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        key = input(data["input_multiple_key"])
        if not key:
            error = True
            continue 
        string_coded = ""
        i = 0
        for c in string:
            if i > len(key)- 1:
                i = 0
        #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 + int(key[i])) % 26 + 97)
                i += 1
        #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 + int(key[i])) % 26 + 65)
                i += 1
            else:
                string_coded += c
        key = " ".join(key)
        error = False
        return string, key, string_coded, method

 