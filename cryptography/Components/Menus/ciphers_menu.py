from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Cipher.Caesar import Caesar_cipher
from Cipher.Cipher.Rot import rot_cipher
from Cipher.Cipher.Poly import poly_cipher
from Cipher.Cipher.Vigenere import vigenere_cipher
from Cipher.Cipher.Caesar_affine import affine
from Cipher.Cipher.One_time_pad import OTP_Cipher

DISPATCH_CIPHER = {
    1: Caesar_cipher,
    2: rot_cipher,
    3: poly_cipher,
    4: vigenere_cipher,
    5: affine,
    6: OTP_Cipher,
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