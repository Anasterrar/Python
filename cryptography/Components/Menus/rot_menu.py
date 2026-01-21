from Components.arrow_menu import arrow_menu

def Rot_menu(mode):
    options = ["ROT13", "ROT47", "ROT18"]
    description = ["rot13_cipher", "rot47_cipher", "rot18_cipher"]
    result =  arrow_menu(options, "menu_rot", description, mode)
    if result == "escape":
        result = "back"
    return result