import json

def text_selection(file):
    with open("config/settings.json", "r", encoding="utf-8") as (f):
            settings = json.load(f)
            language = settings.get("language")

    with open(f"text/{file}_{language}.json", "r", encoding="utf-8") as (f):
            data = json.load(f)
    return data
