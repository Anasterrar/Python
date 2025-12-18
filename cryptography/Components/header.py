import os
import pyfiglet
from colorama import Fore, Style, init
from Components import text_selection
init(autoreset=True)

def title(text):
    data = text_selection.text_selection("text")
    os.system("cls")
    header = pyfiglet.figlet_format(data[text], font="slant")
    print(Fore.CYAN + header)
    return

def instruction():
    data = text_selection.text_selection("text")
    print(Fore.MAGENTA + "───────────────────────────────")
    print(f"🌍 {data["language"]}")
    print(Fore.YELLOW + data["header_message1"])
    print(Fore.YELLOW + data["header_message2"])
    print(Fore.MAGENTA + "───────────────────────────────")

def explication(text2):
    data = text_selection.text_selection("explication")
    data2 = text_selection.text_selection("text")
    print(Fore.YELLOW + data2["description"])
    print(data[text2]["description"])
    print(Fore.YELLOW + data2["formula"])
    print(data[text2]["formula"])
    print(Fore.YELLOW + data2["example"])
    print(data[text2]["example"])

def header(text, text2):
    title(text)
    instruction()
    if text2 == None:
        return
    explication(text2)