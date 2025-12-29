from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message
from Components.Menus.rot_menu import Rot_menu
mode = "menu_encryption"

def rot():
    m = Rot_menu()
    if m == "back":
        return None
    return select_rot(m)

def select_rot(num):
    mode = "menu_encryption"
    if num == 1:
        code = Rot13_cipher(mode)
        return code
    elif num == 2:
        code = Rot47_cipher(mode)
        return code
    elif num == 3:
        code = Rot18_cipher(mode)
        return code

def Rot13_cipher():
    error = False
    while True:
        method = "menu_rot13"
        header(method, "rot13", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
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
        return string, key, string_coded, method

def Rot47_cipher():
    error = False
    while True:
        method = "menu_rot47"
        header(method, "rot47", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
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
        return string, key, string_coded, method

def Rot18_cipher():
    data = text_selection("text")
    error = False
    while True:
        method = "menu_rot18"
        header("menu_rot18", "rot18", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
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
        return string, keys, string_coded, method