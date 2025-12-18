from Components.header import header
from Components.text_selection import text_selection

def menu():
    data = text_selection("text")
    while True:
        options = [f"1. {data["menu_caesar"]}", f"2. {data["menu_rot"]}", f"3. {data["menu_Caesar_poly"]}", f"4. {data["menu_vigenere"]}", f"5. {data["menu_Caesar_affine"]}", f"6. {data["menu_setting"]}"]
        header("app_title", None)
        for opt in options:
            print(opt)
        answer = input(data["input_menu"])
        if answer.isdigit() == True:
            return int(answer)