import os
import datetime
import pyfiglet
from Components.header import header
from Components.text_selection import text_selection
from Components.file_options import file_options

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def create_file(result_brut, mode):
    preferences = file_options()
    if not preferences:
        return

    data = text_selection("text")

    title = pyfiglet.figlet_format(data["app_title"], font="slant")
    now = datetime.datetime.now()
    stamp = now.strftime("%Y_%m_%d_%H_%M")
    sections = {
        "header": title,
        "method": f"{data['method']}: {data[result_brut[3]]}",
        "original_text": f"{data['text']} : {result_brut[0]}",
        "key": f"{data['key']} : {result_brut[1]}",
        "coded_text": f"{data[mode[1]]} : {result_brut[2]}",
        "date_and_hour": f"{data['date']} : {stamp}",
    }

    enabled_by_key = {opt["key"]: opt["enabled"] for opt in preferences}

    a = 0
    while True:
        filename = f"{stamp}_{a}.txt"
        path = os.path.join(EXPORT_DIR, filename)

        if os.path.isfile(path):
            a += 1
            continue

        with open(path, "w", encoding="utf-8") as f:
            order = ["header", "method", "original_text", "key", "coded_text", "date_and_hour"]
            for k in order:
                if enabled_by_key.get(k):
                    f.write(sections[k] + "\n")

        header(result_brut[3], None, None)
        print(f"{data['file_saved']} '{filename}' {data['in']} {path}")
        input(data["press_enter"])
        break