import os
import pyfiglet
import unicodedata
from colorama import Fore, init, Back
from Components.text_selection import text_selection
init(autoreset=True)

def normalize_text(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

def title(text):
    data = text_selection("text")

    os.system("cls")
    title = pyfiglet.figlet_format(normalize_text(data[text]), font="slant")
    print(Fore.CYAN + title)
    print(f"🌍 {data["language"]}")

def instruction(t, mode):
    data = text_selection("text")

    print(Fore.MAGENTA + "───────────────────────────────")
    if mode:
        if mode == "menu_encryption":
            emoji = "🔒"
        if mode == "menu_decryption":
            emoji = "🔓"
        print(f"{emoji} {data[mode]}")
    else:
        print(Fore.YELLOW + data["header_message1"])

    if t == "esc":
        print(Fore.YELLOW + data["header_message4"])
        print(Fore.YELLOW + data["header_message2"])
    else:
        print(Fore.YELLOW + data["header_message4"])
        print(Fore.YELLOW + data["header_message3"])
    print(Fore.MAGENTA + "───────────────────────────────")

def explication(text2):
    data = text_selection("explication")
    data2 = text_selection("text")

    print(Fore.YELLOW + data2["method"])
    print(data[text2]["title"])
    print(Fore.YELLOW + data2["description"])
    print(data[text2]["description"])
    print(Fore.YELLOW + data2["formula"])
    print(Back.WHITE + Fore.BLACK + data[text2]["formula"])
    print(Fore.YELLOW + data2["example"])
    print(data[text2]["example"])
    print(Fore.MAGENTA + "───────────────────────────────")

def header(text, text2, mode):
    title(text)
    if text2 == None:
        instruction("esc", mode)
        return
    instruction("C", mode)
    explication(text2)