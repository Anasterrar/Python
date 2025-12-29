from Components.arrow_menu import arrow_menu

def Rot_menu():
    options = ["ROT13", "ROT47", "ROT18"]
    description = ["rot13", "rot47", "rot18"]
    result =  arrow_menu(options, "menu_rot", description)
    if result == "escape":
        result = "back"
    return result
