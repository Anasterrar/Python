def load_dictionaries():
    return {
        "French": set(open("francais.txt", encoding="utf-8").read().lower().split()),
        "English": set(open("english.txt", encoding="utf-8").read().lower().split())
    }

DICTIONARIES = load_dictionaries()
