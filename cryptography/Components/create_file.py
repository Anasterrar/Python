import os
import datetime
import pyfiglet

from Components.header import header
from Components.text_selection import text_selection
from Components.file_options import file_options


path = "exports/"
if not os.path.isdir(path):
   os.makedirs(path)

def create_file(result_brut, mode):
    preferences = file_options()
    data = text_selection("text")

    title = pyfiglet.figlet_format(data["app_title"], font="slant")
    date = datetime.datetime.now()
    date = date.strftime("%Y_%m_%d_%H_%M")

    sections = [
        ("header", title),
        ("method", f"{data['method']}: {data[result_brut[3]]}"),
        ("text", f"{data['text']} : {result_brut[0]}"),
        ("key", f"{data['key']} : {result_brut[1]}"),
        ("coded_text", f"{data[mode[1]]} : {result_brut[2]}"),
        ("date", f"{data['date']} : {date}")
    ]

    a = 0
    while True:
        path = f"exports/{date}_{a}.txt"
        if os.path.isfile(path) == True:
            a += 1
        else:
            with open(path, "a") as f:
                for pair in zip(preferences, sections):
                    pref = pair[0]
                    section = pair[1]
                    content = section[1]
                    if pref["enabled"]:
                        f.write(content + "\n")
            header(result_brut[3], None, None)
            print(f"{data["file_saved"]} '{date}_{a}.txt' {data["in"]} {path}")
            input(data["press_enter"])
            break