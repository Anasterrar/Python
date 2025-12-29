import random
from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message
from Components.Menus.affine_menu import affine_menu

def affine():
    m = affine_menu()
    if m == "back":
        return None
    return select_affine(m)

def select_affine(num):
    auto = False
    if num == 1:
        code = Caesar_affine(auto)
    elif num == 2:
        auto = True
        code = Caesar_affine(auto)
    return code

def isValidA(a):
    if a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        return True
    else:
        return False

def Caesar_affine(auto):
    data = text_selection("text")
    error = False
    while True:
        method = "menu_Caesar_affine"
        header(method, "affine")
        if error == True:
            error_message(["error_empty_text", "error_empty_key", "error_invalid_key_affine"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        if auto == True:
            a_key = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
            a = str(random.choice(a_key))
        if auto == False:
            a = input_message("input_first_key")
        if not a or a.isdigit() == False or isValidA(int(a)) == False:
            error = True
            continue
        b = input_message("input_second_key")
        if not b or b.isdigit() == False:
            error = True
            continue
        string_coded = ""
        keys = f"a = {a} {data["and"]} b = {b}"
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((int(a) * (ord(c) - 97) + int(b)) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((int(a) * (ord(c) - 65) + int(b)) % 26 + 65)
            else:
                string_coded += c
        error = False
        return string, keys, string_coded, method