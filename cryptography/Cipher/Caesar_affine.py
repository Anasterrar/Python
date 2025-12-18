import random
import msvcrt
from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message
from colorama import Fore, Style, init

def affine_menu():
    data = text_selection("text")
    selected = 0
    while True:
        options = [f"{data["manual_key"]}", f"{data["auto_key"]}"]
        header("menu_Caesar_affine", None)
        for i, option in enumerate(options):
            if i == selected:
                print(f"> {" "}{option}")
            else:
                print(f"  {option}")
        print(Fore.YELLOW + Style.BRIGHT + f"{options[selected]} ?")

        key = msvcrt.getch()
        
        if key == b'\xe0':
            key2 = msvcrt.getch()
          
            if key2 == b'H':
                selected = (selected - 1) % len(options)
                print(selected)
            elif key2 == b'P':
                selected = (selected + 1) % len(options)
        elif key == b'\r':
            return selected + 1
        elif key == b'\x1b':
            return None
        
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
