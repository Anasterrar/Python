from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Decipher.Caesar import Caesar
from Cipher.Decipher.Rot import Rot
from Cipher.Decipher.Poly import Poly
from Cipher.Decipher.Vigenere import Vigenere
from Cipher.Decipher.Caesar_affine import Affine
from Cipher.Decipher.One_time_pad import OTP

DISPATCH_DECIPHER = {
    1: Caesar,
    2: Rot,
    3: Poly,
    4: Vigenere,
    5: Affine,
    6: OTP,
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