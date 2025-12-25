import os
import json
from Components.menus import settings_menu

def run_settings():
    return settings(False)

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
            selected = settings_menu(True)
            lang = "fr" if selected == 1 else "en"
            with open("config/settings.json", "w", encoding="utf-8") as f:
                json.dump({"language": lang}, f)
    if init == False :
        selected = settings_menu(False)
        lang = "fr" if selected == 1 else "en"
        with open("config/settings.json", "w", encoding="utf-8") as f:
            json.dump({"language": lang}, f)