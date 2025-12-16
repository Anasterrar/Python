import os
import json
from Components.header import title

def settings():
        #Cree le dossier config et le fichier setting si necessaire
        path = "config/"
        if not os.path.isdir(path):
            os.makedirs(path)
        path_file = "config/settings.json"
        if os.path.isfile(path_file) == False:
            with open(path_file, "w") as f:
                    json.dump({"language": ""}, f)

        title("Language")
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

