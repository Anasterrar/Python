import os
import json
import msvcrt
from Components.header import header
from colorama import Fore, Style, init

def settings(init):
        if init == True:
            #Cree le dossier config et le fichier setting si necessaire
            path = "config/"
            if not os.path.isdir(path):
                os.makedirs(path)
            path_file = "config/settings.json"
            if os.path.isfile(path_file) == False:
                with open(path_file, "w") as f:
                        json.dump({"language": ""}, f)

            #Configure la langue, anglais par defaut si erreur
            with open("config/settings.json", "r") as (f):
                settings = json.load(f)
                lang = settings.get("language")
            if not lang or lang not in ["fr", "en"]:
                print("Choose language / Choisissez la langue")
                print("1. Français")
                print("2. English")
                choice = input("> ")
                lang = "fr" if choice == "1" else "en"
                with open("config/settings.json", "w", encoding="utf-8") as f:
                    json.dump({"language": lang}, f)
        if init == False :
            selected = 0
            while True:
                header("app_title", None)
                print("Choose language / Choisissez la langue")
                options = ["Français", "English"]
                for i, option in enumerate(options):
                    if i == selected:
                        print(f"> {" "}{option}")
                    else:
                        print(f"  {option}")
                print(Fore.YELLOW + Style.BRIGHT + f"{options[selected]} ?")

                key = msvcrt.getch()
        
                if key == b'\xe0':
                    key2 = msvcrt.getch()
                
                    if key2 == b'H':
                        selected = (selected - 1) % len(options)
                        print(selected)
                    elif key2 == b'P':
                        selected = (selected + 1) % len(options)
                elif key == b'\r':
                    lang = "fr" if selected == 0 else "en"
                    with open("config/settings.json", "w", encoding="utf-8") as f:
                        json.dump({"language": lang}, f)
                        break
                    
                elif key == b'\x1b':
                    return None
             

