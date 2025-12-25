import os
import msvcrt
from colorama import Fore, Style
from Components.header import header

def arrow_menu(options, title):
    selected = 0
    while True:
        os.system("cls")
        if title != None:
            header(title, None)
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
            return selected + 1
        elif key == b'\x1b':
            os.system("cls")
            return "escape"