from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Brut_Force.Caesar_main import Caesar_main
from Cipher.Brut_Force.Poly_main import Poly_main
from Cipher.Brut_Force.Vigenere_main import Vigenere_main
from Cipher.Brut_Force.Affine_main import Affine_main

DISPATCH_BRUT_FORCE_METHOD = {
    1: Caesar_main,
    2: Poly_main,
    3: Vigenere_main,
    4: Affine_main,  
}

def crack_menu():
    mode = "menu_decryption", "coded_text"
    data = text_selection("explication")
    options = [f"{data["crack_caesar"]["title"]}",
               f"{data["crack_poly"]["title"]}",
               f"{data["crack_vigenere"]["title"]}",
               f"{data["crack_affine"]["title"]}"]
    description = ["crack_caesar", "crack_poly", "crack_vigenere", "crack_affine"]
    result =  arrow_menu(options, "app_title", description, mode[0])
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_BRUT_FORCE_METHOD.get(result)
    result = action()
    return result, mode