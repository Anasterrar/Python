from Components.arrow_menu import arrow_menu

def settings_menu(init):
    options = ["Français", "English"]
    if init == True:
        result = arrow_menu(options, None, None)
    if init == False:
        result = arrow_menu(options, "app_title", None, None)
    if result == "escape":
        result = "back"
    return result