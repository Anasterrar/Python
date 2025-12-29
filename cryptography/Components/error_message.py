from Components.text_selection import text_selection
from colorama import Fore

def error_message(errors):
    data = text_selection("text")
    for error in errors:
        print(data[error])
    print(Fore.MAGENTA + "───────────────────────────────")