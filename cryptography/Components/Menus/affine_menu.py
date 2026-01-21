from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

def affine_menu(mode):
    data = text_selection("text")
    options = [f"{data["manual_key"]}", f"{data["auto_key"]}"]
    description = ["affine_manual_cipher", "affine_auto_cipher"]
    result =  arrow_menu(options, "menu_Caesar_affine", description, mode)
    if result == "escape":
        result = "back"
    return result