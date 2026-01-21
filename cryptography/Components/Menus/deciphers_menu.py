from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Decipher.Caesar import Caesar_Decipher
from Cipher.Decipher.Rot import rot_decipher
from Cipher.Decipher.Poly import poly_decipher
from Cipher.Decipher.Vigenere import vigenere_decipher
from Cipher.Decipher.Caesar_affine import Caesar_affine
from Cipher.Decipher.One_time_pad import OTP_Decipher

DISPATCH_DECIPHER = {
    1: Caesar_Decipher,
    2: rot_decipher,
    3: poly_decipher,
    4: vigenere_decipher,
    5: Caesar_affine,
    6: OTP_Decipher,
}

def decipher_menu():
    mode = "menu_decryption", "decoded_text"
    data = text_selection("explication")
    options = [f"{data["caesar_decipher"]["title"]}",
               f"{data["rot_decipher"]["title"]}", f"{data["poly_decipher"]["title"]}",
               f"{data["vigenere_decipher"]["title"]}",
               f"{data["affine_decipher"]["title"]}",
               f"{data["otp_decipher"]["title"]}"]
    description = ["caesar_decipher", "rot_decipher", "poly_decipher", "vigenere_decipher", "affine_decipher", "otp_decipher"]
    result =  arrow_menu(options, "app_title", description, mode[0])
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_DECIPHER.get(result)
    result = action()
    return result, mode