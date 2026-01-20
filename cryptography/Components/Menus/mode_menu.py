from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Components.Menus.ciphers_menu import cipher_menu
from Components.Menus.deciphers_menu import decipher_menu


from Components.settings import run_settings

DISPATCH_MODE = {
    1: cipher_menu,
    2: decipher_menu,
    3: run_settings
}

def mode_menu():
    data = text_selection("text")
    options = [f"{data["menu_encryption"]}", f"{data["menu_decryption"]}", f"{data["menu_setting"]}", 'brut_force_method_menu']
    result =  arrow_menu(options, "app_title", None, None)
    if result == "escape":
        result = "quit"
    return result