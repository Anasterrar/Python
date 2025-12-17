from Components.header import header
from Components import text_selection

def Rot_menu():
    data = text_selection.text_selection("text")
    while True:
        options = ["1. ROT13", "2. ROT47", "3. ROT18"]
        header("menu_rot", None)
        for opt in options:
            print(opt)
        answer = input(data["input_menu"])
        if answer.isdigit() == True:
            return int(answer)

def select_rot(num):
    if num == 1:
        code = Rot13_cipher()
        return code
    elif num == 2:
        code = Rot47_cipher()
        return code
    elif num == 3:
        code = Rot18_cipher()
        return code

def Rot13_cipher():
    data = text_selection.text_selection("text")
    error = False
    while True:
        method = data["menu_rot13"]
        header("menu_rot13", "rot13")
        if error == True:
            print(data["error_empty_text"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        key = 13
        string_coded = ""
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
        return string, key, string_coded, method, "menu_rot13"

def Rot47_cipher():
    data = text_selection.text_selection("text")
    error = False
    while True:
        method = data["menu_rot47"]
        header("menu_rot47", "rot47")
        if error == True:
            print(data["error_empty_text"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        key = 47
        string_coded = ""
        for c in string:
            #Minuscule
            if ord(c) >= 33 and ord(c) <= 126:
                string_coded += chr((ord(c) - 33 + key) % 94 + 33)
            else:
                string_coded += c
        error = False
        return string, key, string_coded, method, "menu_rot47"

def Rot18_cipher():
    data = text_selection.text_selection("text")
    error = False
    while True:
        method = data["menu_rot18"]
        header("menu_rot18", "rot18")
        if error == True:
            print(data["error_empty_text"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        key1 = 13
        key2 = 5
        keys = f"{key1} {data["rot_for_key1"]} {key2} {data["rot_for_key2"]}"
        string_coded = ""
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 + key1) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 + key1) % 26 + 65)
            #Chiffre
            elif ord(c) >= 48 and ord(c) <= 57:
                string_coded += chr((ord(c) - 48 + key2) % 10 + 48)
            else:
                string_coded += c
        error = False
        return string, keys, string_coded, method, "menu_rot18"