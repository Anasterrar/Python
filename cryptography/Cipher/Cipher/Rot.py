from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message
from Components.Menus.rot_menu import Rot_menu
mode = "menu_encryption"

#------------Menu------------#

def Rot():
    mode = "menu_encryption"
    m = Rot_menu(mode)
    if m == "back":
        return None
    return select_rot(m, mode)

def select_rot(num, mode):
    if num == 1:
        code = Rot13(mode)
        return code
    elif num == 2:
        code = Rot47(mode)
        return code
    elif num == 3:
        code = Rot18(mode)
        return code

#--------------------Cipher---------------------#

#------------Rot 13-----------#
def Rot13_cipher(string):
    string_coded = ""
    for c in string:
        #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            string_coded += chr((ord(c) - 97 + 13) % 26 + 97)
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            string_coded += chr((ord(c) - 65 + 13) % 26 + 65)
        else:
            string_coded += c
    return string_coded

def Rot13(mode):
    error = False
    while True:
        method = "menu_rot13"
        header(method, "rot13_cipher", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        string_coded = Rot13_cipher(string)
        return string, 13, string_coded, method
    
#------------Rot 47-----------#
def Rot47_cipher(string):
    string_coded = ""
    for c in string:
        #Minuscule
        if ord(c) >= 33 and ord(c) <= 126:
            string_coded += chr((ord(c) - 33 + 47) % 94 + 33)
        else:
            string_coded += c
    return string_coded

def Rot47(mode):
    error = False
    while True:
        method = "menu_rot47"
        header(method, "rot47_cipher", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        string_coded = Rot47_cipher
        return string, 47, string_coded, method

#------------Rot 18-----------#
def Rot18_cipher(string):
    string_coded = ""
    for c in string:
        #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            string_coded += chr((ord(c) - 97 + 13) % 26 + 97)
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            string_coded += chr((ord(c) - 65 + 13) % 26 + 65)
        #Chiffre
        elif ord(c) >= 48 and ord(c) <= 57:
            string_coded += chr((ord(c) - 48 + 5) % 10 + 48)
        else:
            string_coded += c
    return string_coded

def Rot18(mode):
    data = text_selection("text")
    error = False
    while True:
        method = "menu_rot18"
        header("menu_rot18", "rot18_cipher", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        keys = f"13 {data["rot_for_key1"]} 5 {data["rot_for_key2"]}"
        string_coded = Rot18_cipher(string)
        return string, keys, string_coded, method