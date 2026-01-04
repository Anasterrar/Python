from Components.header import header
from Components.text_selection import text_selection
from colorama import Fore, Style
import msvcrt
    
def show_result(result):
        data = text_selection("text")
        options = [f"{data["yes"]}", f"{data["no"]}"]
        selected = 0
        while True:
            header(result[3], None, None)
            print(f"{data["method"]} : {data[result[3]]}")
            print(f"{data["text"]} : {result[0]}")
            print(f"{data["key"]} : {result[1]}")
            print(f"{data["coded_text"]} : {result[2]}")
            print(Fore.YELLOW + Style.BRIGHT + data["save_question"])

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
                if selected + 1 == 1:
                    return True
                if selected + 1 == 2:
                    return False