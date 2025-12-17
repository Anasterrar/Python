from Components.header import header
from Components import text_selection

def formalize(string):
    for c in string:
        if c.isalpha() == False:
            string = string.replace(c, '')
    return string

def vigenere():
    data = text_selection.text_selection("text")
    error = False
    while True:
        method = data["menu_vigenere"]
        header("menu_vigenere", "vigenere")
        string_coded = ""
        i = 0
        if error == True:
            print(data["error_empty_text"])
            print(data["error_empty_key"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        key = input(data["input_word_key"])            
        key = formalize(key)
        if not key:
            error = True
            return
        for c in string:
            if i > len(key)- 1:
                i = 0
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                if ord(key[i]) >= 97 and ord(key[i]) <= 122:
                    string_coded += chr((ord(c) - 97 + ord(key[i]) - 97) % 26 + 97)
                elif ord(key[i]) >= 65 and ord(key[i]) <= 90:
                    string_coded += chr((ord(c) - 97 + ord(key[i]) - 65) % 26 + 97)
                i += 1
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                if ord(key[i]) >= 97 and ord(key[i]) <= 122:
                    string_coded += chr((ord(c) - 65 + ord(key[i]) - 97) % 26 + 65)
                elif ord(key[i]) >= 65 and ord(key[i]) <= 90:
                    string_coded += chr((ord(c) - 65 + ord(key[i]) - 65) % 26 + 65)
                i += 1
            else:
                string_coded += c
        error = False
        return string, key, string_coded, method, "menu_vigenere"
