import os
import pyfiglet
from colorama import Fore, Style, init
init(autoreset=True)

def header(text):
    os.system("cls")
    header = pyfiglet.figlet_format(text, font="slant")
    print(Fore.CYAN + header)
    print(Fore.MAGENTA + "───────────────────────────────")
    print(Fore.YELLOW + "Coder un texte")
    print(Fore.YELLOW + "💡 Ctrl+C pour quitter")
    print(Fore.MAGENTA + "───────────────────────────────")
    return