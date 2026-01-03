from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Decipher.Caesar import Caesar_Decipher
from Cipher.Decipher.Rot import rot_decipher
from Cipher.Decipher.Poly import poly_decipher
from Cipher.Decipher.Vigenere import vigenere_decipher
from Cipher.Decipher.Caesar_affine import Caesar_affine

DISPATCH_DECIPHER = {
    1: Caesar_Decipher,
    2: rot_decipher,
    3: poly_decipher,
    4: vigenere_decipher,
    5: Caesar_affine,
}

def decipher_menu():
    mode = "menu_decryption"
    data = text_selection("explication")
    options = [f"{data["caesar"]["title"]}", f"{data["rot"]["title"]}", f"{data["poly"]["title"]}", f"{data["vigenere"]["title"]}", f"{data["affine"]["title"]}"]
    description = ["caesar", "rot", "poly", "vigenere", "affine"]
    result =  arrow_menu(options, "app_title", description, mode)
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_DECIPHER.get(result)
    result = action()
    return result
    