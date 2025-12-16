from Components.header import header
import random
from Components import text_selection

def affine_menu():
    data = text_selection.text_selection("text")
    while True:
        options = [f"1. {data["manual_key"]}", f"2. {data["auto_key"]}"]
        header(data["menu_Caesar_affine"])
        for opt in options:
            print(opt)
        answer = input(data["input_menu"])
        if answer.isdigit() == True:
            return int(answer)
        
def select_affine(num):
    auto = False
    if num == 1:
        code = Caesar_affine(auto)
        return code
    elif num == 2:
        auto = True
        code = Caesar_affine(auto)
        return code

def isValidA(a):
    if a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        return True
    else:
        return False

#(ax + b) modulo 26, a premier avec 27
def Caesar_affine(auto):
    data = text_selection.text_selection("text")
    error = False
    while True:
        method = data["menu_Caesar_affine"]
        header(method)
        if error == True:
            print(data["error_empty_text"])
            print(data["error_empty_key"])
            print(data["error_invalid_key_affine"])
        string = input(data["input_text"])
        if not string:
            error = True
            continue
        if auto == True:
            a_key = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
            a = str(random.choice(a_key))
        if auto == False:
            a = input(data["input_first_key"])
        if not a or a.isdigit() == False or isValidA(int(a)) == False:
            error = True
            continue
        b = input(data["input_second_key"])
        if not b or b.isdigit() == False:
            error = True
            continue
        string_coded = ""
        keys = f"a = {a} et b = {b}"
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
