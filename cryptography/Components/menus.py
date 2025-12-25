from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

def main_menu():
    data = text_selection("text")
    options = [f"{data["menu_caesar"]}", f"{data["menu_rot"]}", f"{data["menu_Caesar_poly"]}", f"{data["menu_vigenere"]}", f"{data["menu_Caesar_affine"]}", f"{data["menu_setting"]}"]
    result =  arrow_menu(options, "app_title")
    if result == "escape":
        result = "quit"
    return result

def Rot_menu():
    options = ["ROT13", "ROT47", "ROT18"]
    result =  arrow_menu(options, "menu_rot")
    if result == "escape":
        result = "back"
    return result

def affine_menu():
    data = text_selection("text")
    options = [f"{data["manual_key"]}", f"{data["auto_key"]}"]
    result =  arrow_menu(options, "menu_Caesar_affine")
    if result == "escape":
        result = "back"
    return result
 
def settings_menu(init):
    options = ["Français", "English"]
    if init == True:
        result = arrow_menu(options, None)
    if init == False:
        result = arrow_menu(options, "app_title")
    if result == "escape":
        result = "back"
    return result