import os
import json
import msvcrt
from colorama import Fore, Style, init
init(autoreset=True)
from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message

LAST_SAVE_PATH = os.path.join("config", "last_save.json")

def error_options(options):
    return sum(1 for opt in options if opt["key"] != "validate" and opt["enabled"]) == 0

def save_options(options):
    os.makedirs("config", exist_ok=True)

    last = {}
    if os.path.isfile(LAST_SAVE_PATH):
        with open(LAST_SAVE_PATH, "r", encoding="utf-8") as f:
            try:
                last = json.load(f)
            except json.JSONDecodeError:
                last = {}

    last["options"] = options
    with open(LAST_SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(last, f, indent=4, ensure_ascii=False)

def previous_options():
    if not os.path.isfile(LAST_SAVE_PATH):
        return None

    try:
        with open(LAST_SAVE_PATH, "r", encoding="utf-8") as f:
            previous = json.load(f)
        opts = previous.get("options")
        if isinstance(opts, list) and len(opts) > 0:
            return opts
    except (json.JSONDecodeError, OSError):
        return None

    return None

def previous_list(previous):
    return [line["label"] for line in previous if line.get("enabled")]

def file_options():
    data = text_selection("text")
    options = [
        {"key": "header",        "label": data["header"],        "enabled": False},
        {"key": "method",        "label": data["method"],        "enabled": False},
        {"key": "original_text", "label": data["original_text"], "enabled": False},
        {"key": "key",           "label": data["key"],           "enabled": False},
        {"key": "coded_text",    "label": data["coded_text"],    "enabled": True},
        {"key": "date_and_hour", "label": data["date_and_hour"], "enabled": False},
        {"key": "validate",      "label": data["Validate"],      "enabled": False},
    ]

    previous_choice = previous_options()
    selected = 0
    error = False

    while True:
        os.system("cls")
        header("app_title", None, None)

        if previous_choice is not None:
            print(Fore.YELLOW + Style.BRIGHT + data["input_choice"])
            print(data["input_previous_choice"] + "\n" + str(previous_list(previous_choice)))
            print(Fore.MAGENTA + "───────────────────────────────")

        if error:
            error_message(["error_invalid_selection"])
            error = False

        for i, option in enumerate(options):
            cursor = ">" if i == selected else " "
            check = " ✅" if option["enabled"] else ""
            print(f"{cursor} {option['label']}{check}")

        print(Fore.YELLOW + Style.BRIGHT + f"{options[selected]['label']} ?")

        key = msvcrt.getch()

        if key in (b's', b'S'):
            return previous_choice

        if key == b'\x1b':
            return None

        if key == b'\xe0':
            key2 = msvcrt.getch()
            if key2 == b'H':   # up
                selected = (selected - 1) % len(options)
            elif key2 == b'P': # down
                selected = (selected + 1) % len(options)

        elif key == b'\r':
            if options[selected]["key"] != "validate":
                options[selected]["enabled"] = not options[selected]["enabled"]
            else:
                if error_options(options):
                    error = True
                    continue
                save_options(options)
                return options