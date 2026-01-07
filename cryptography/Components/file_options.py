import os
import json
import msvcrt
from colorama import Fore, Style, init
init(autoreset=True)

from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message

def error_options(options):
    a = 0
    for line in options:
        if line["enabled"] == True:
            a +=1
    if a == 0:
        return True
    else:
        return False
    
def save_options(options):
    path_file = "config/last_save.json"
    if os.path.isfile(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            try:
                last = json.load(f)
            except json.JSONDecodeError:
                last = {}
    else:
        last = {}
    last["options"] = options
    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(last, f, indent=4, ensure_ascii=False)

def previous_options():
    path_file = "config/last_save.json"
    if os.path.isfile(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            previous = json.load(f)
            if len(previous["options"]) > 0:
                return previous["options"]
    else :
        return None

def previous_list(previous):
    previous_line = []
    for line in previous:
        if line["enabled"] == True:
            previous_line.append(line["label"])
    return previous_line
    
    
def file_options():
    data = text_selection("text")
    options = [
    {"label": "Header", "enabled": False},
    {"label": "Methode", "enabled": False},
    {"label": "Texte original", "enabled": False},
    {"label": "Clé", "enabled": False},
    {"label": "Texte codé", "enabled": True},
    {"label": "Date et heure", "enabled": False},
    {"label": "Valider", "enabled": False},
    ]
    previous_choice = previous_options()
    selected = 0
    error = False
    while True:
        header("app_title", None, None)

        if previous_choice != None:
            print(Fore.YELLOW + Style.BRIGHT + data["input_choice"])
            print(data["input_previous_choice"] + "\n" + str(previous_list(previous_choice)))
            print(Fore.MAGENTA + "───────────────────────────────")
        
        if error == True:
            error_message(["error_invalid_selection"])
            
        for i, option in enumerate(options):
            cursor = ">" if i == selected else ""
            check = " ✅" if option["enabled"] else ""
            print(f"{cursor} {option['label']}{check}")

        print(Fore.YELLOW + Style.BRIGHT + f"{options[selected]["label"]} ?")
                
        key = msvcrt.getch()

        if key == b's':
            return previous_choice

        if key == b'\xe0':
            key2 = msvcrt.getch()
                
            if key2 == b'H':
                selected = (selected - 1) % len(options)
                print(selected)
            elif key2 == b'P':
                    selected = (selected + 1) % len(options)

        elif key == b'\r':
            if selected < len(options) - 1:
                options[selected]["enabled"] = not options[selected]["enabled"]
            
            if selected == len(options) - 1:
                if error_options(options) == True:
                    error = True
                    continue
                else:
                    save_options(options)
                    return options
                 
        elif key == b'\x1b':
            print(options)
            break