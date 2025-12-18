import msvcrt
import os
from Components.header import header
from Components.text_selection import text_selection
from colorama import Fore, Style, init

def menu():
    data = text_selection("text")
    selected = 0
    while True:
        options = [f"{data["menu_caesar"]}", f"{data["menu_rot"]}", f"{data["menu_Caesar_poly"]}", f"{data["menu_vigenere"]}", f"{data["menu_Caesar_affine"]}", f"{data["menu_setting"]}"]
        header("app_title", None)
        for i, option in enumerate(options):
            if i == selected:
                print(f"▶️ {" "}{option}")
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
            return None
