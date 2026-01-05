import msvcrt
from colorama import Fore, Style, init
from Components.header import header
init(autoreset=True)

def file_options():
    options = [
    {"label": "Header", "enabled": False},
    {"label": "Methode", "enabled": False},
    {"label": "Texte original", "enabled": False},
    {"label": "Clé", "enabled": False},
    {"label": "Texte codé", "enabled": True},
    {"label": "Date et heure", "enabled": False},
    {"label": "Valider", "enabled": False},
    ]
    selected = 0
    while True:
        header("app_title", None, None)
        print("do you want save the file ?")
        
        for i, option in enumerate(options):
            cursor = ">" if i == selected else ""
            check = " ✅" if option["enabled"] else ""
            print(f"{cursor} {option['label']}{check}")

        print(Fore.YELLOW + Style.BRIGHT + f"{options[selected]["label"]} ?")
                
        key = msvcrt.getch()

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
                return options
                 
        elif key == b'\x1b':
            print(options)
            break