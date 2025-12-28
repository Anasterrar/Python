from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

def Rot_menu():
    options = ["ROT13", "ROT47", "ROT18"]
    result =  arrow_menu(options, "menu_rot")
    if result == "escape":
        result = "back"
    return result
