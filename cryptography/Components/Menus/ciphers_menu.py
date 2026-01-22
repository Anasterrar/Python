from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Cipher.Caesar import Caesar
from Cipher.Cipher.Rot import Rot
from Cipher.Cipher.Poly import Poly
from Cipher.Cipher.Vigenere import Vigenere
from Cipher.Cipher.Caesar_affine import Affine
from Cipher.Cipher.One_time_pad import OTP

DISPATCH_CIPHER = {
    1: Caesar,
    2: Rot,
    3: Poly,
    4: Vigenere,
    5: Affine,
    6: OTP,
}

def cipher_menu():
    mode = "menu_encryption", "coded_text"
    data = text_selection("explication")
    options = [f"{data["caesar_cipher"]["title"]}",
               f"{data["rot_cipher"]["title"]}",
               f"{data["poly_cipher"]["title"]}",
               f"{data["vigenere_cipher"]["title"]}",
               f"{data["affine_cipher"]["title"]}",
               f"{data["otp_cipher"]["title"]}"]
    
    description = ["caesar_cipher", "rot_cipher", "poly_cipher", "vigenere_cipher", "affine_cipher", "otp_cipher"]
    result =  arrow_menu(options, "app_title", description, mode[0])
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_CIPHER.get(result)
    result = action()
    return result, mode