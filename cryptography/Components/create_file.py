import os
import datetime
from Components.header import header
from Components.text_selection import text_selection
from Components.file_options import file_options
import pyfiglet


path = "exports/"
if not os.path.isdir(path):
   os.makedirs(path)

def create_file(result_brut):
    preference = file_options()
    data = text_selection("text")
    title = pyfiglet.figlet_format(data["app_title"], font="slant")
    date = str(datetime.datetime.now())
    result_formatted = [f"{data["method"]}: {data[result_brut[3]]}",
                        f"{data["text"]} : {result_brut[0]}",
                        f"{data["key"]} : {str(result_brut[1])}",
                        f"{data["coded_text"]} :{result_brut[2]}"]
    a = 1
    i = 1
    file_name = f"{data[result_brut[3]]}_{date}"
    file_name.replace(" ", "")
    while True:
        path = f"exports/key{a}.txt"
        if os.path.isfile(path) == True:
            a += 1
        else:
            with open(path, "a") as f:
                if preference[0]["enabled"] == True:
                    f.write(title + "\n")
                for line in result_formatted:
                    if preference[i]["enabled"] == True:
                        f.write(line + "\n")
                    i += 1
                if preference[5]["enabled"] == True:
                    f.write(f"{data["date"]} : {date}")
            header(result_brut[3], None, None)
            print(f"{data["file_saved"]} '{file_name}_{a}.txt' {data["in"]}")
            input(data["press_enter"])
            break