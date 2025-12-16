import os
import pyfiglet
from colorama import Fore, Style, init
from Components import text_selection
init(autoreset=True)

def title(text):
    os.system("cls")
    header = pyfiglet.figlet_format(text, font="slant")
    print(Fore.CYAN + header)
    return

def instruction():
    data = text_selection.text_selection("text")
    print(Fore.MAGENTA + "───────────────────────────────")
    print(Fore.YELLOW + data["header_message1"])
    print(Fore.YELLOW + data["header_message2"])
    print(Fore.MAGENTA + "───────────────────────────────")

def header(text):
    title(text)
    instruction()