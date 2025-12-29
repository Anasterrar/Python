from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Decipher.Caesar import Caesar_Decipher
from Cipher.Rot import rot
from Decipher.Poly import poly_decipher
from Decipher.Vigenere import vigenere_decipher

DISPATCH_DECIPHER = {
    1: Caesar_Decipher,
    2: rot,
    3: poly_decipher,
    4: vigenere_decipher,
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
    