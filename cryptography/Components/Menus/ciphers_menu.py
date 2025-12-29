from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Caesar import Caesar_cipher
from Cipher.Rot import rot
from Cipher.Poly import poly_cipher
from Cipher.Vigenere import vigenere_cipher
from Cipher.Caesar_affine import affine

DISPATCH_CIPHER = {
    1: Caesar_cipher,
    2: rot,
    3: poly_cipher,
    4: vigenere_cipher,
    5: affine,
}

def cipher_menu():
    data = text_selection("text")
    options = [f"{data["menu_caesar"]}", f"{data["menu_rot"]}", f"{data["menu_Caesar_poly"]}", f"{data["menu_vigenere"]}", f"{data["menu_Caesar_affine"]}"]
    description = ["caesar", None, "poly", "vigenere", "affine"]
    result =  arrow_menu(options, "app_title", description)
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_CIPHER.get(result)
    result = action()
    return result
    