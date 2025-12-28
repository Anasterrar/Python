from Components.text_selection import text_selection
from Components.arrow_menu import arrow_menu

from Decipher.Caesar import Caesar_Decipher

DISPATCH_DECIPHER = {
    1: Caesar_Decipher,
}

def decipher_menu():
    data = text_selection("text")
    options = [f"{data["menu_caesar"]}"]
    result =  arrow_menu(options, "app_title")
    if result == "escape":
        result = "quit"
        return result
    action = DISPATCH_DECIPHER.get(result)
    result = action()
    return result
    