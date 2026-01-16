from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Cipher.Brut_Force.Caesar.Ceasar import Brut_force_Caesar

DISPATCH_BRUT_FORCE_METHOD = {
    1: Brut_force_Caesar,
}

def brut_force_method_menu():
    mode = "menu_decryption", "coded_text"
    data = text_selection("explication")
    #options = [f"{data["caesar"]["title"]}", f"{data["rot"]["title"]}", f"{data["poly"]["title"]}", f"{data["vigenere"]["title"]}", f"{data["affine"]["title"]}", f"{data["otp"]["title"]}"]
    options = [f"Brut Force Ceasar"]
    description = ["caesar"]
    result =  arrow_menu(options, "app_title", description, mode[0])
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_BRUT_FORCE_METHOD.get(result)
    result = action()
    return result, mode