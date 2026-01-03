import os
from Components.header import header
from Components.text_selection import text_selection

path = "key/"
if not os.path.isdir(path):
   os.makedirs(path)

def create_file(result_brut):
    data = text_selection("text")
    result_formatted = f"{data["method"]}: {data[result_brut[3]]}\n{data["text"]} : {result_brut[0]}\n{data["key"]} : {str(result_brut[1])}\n\n{data["coded_text"]} :\n{result_brut[2]}"
    a = 1
    while True:
        path = f"key/key{a}.txt"
        if os.path.isfile(path) == True:
            a += 1
        else:
            with open(path, "w") as f:
                f.write(result_formatted)
            header(result_brut[3], None, None)
            print(f"{data["file_saved"]} 'key{a}.txt' {data["in"]}")
            input(data["press_enter"])
            break