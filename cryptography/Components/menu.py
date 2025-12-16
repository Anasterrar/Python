from Components import header
from Components import text_selection
data = text_selection.text_selection("text")

def menu():
    options = [f"1. {data["menu_caesar"]}", f"2. {data["menu_rot"]}", f"3. {data["menu_Caesar_poly"]}", f"4. {data["menu_vigenere"]}", f"5. {data["menu_Caesar_affine"]}"]
    header.header(data["app_title"])
    for opt in options:
        print(opt)
    answer = input(data["input_menu"])
    if answer.isdigit() == True:
        return int(answer)
    else:
        menu()