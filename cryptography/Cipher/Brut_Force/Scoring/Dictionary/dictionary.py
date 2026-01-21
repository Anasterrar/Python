def load_dictionaries():
    return {
        "French": set(open(r"Cipher/Brut_Force/Scoring/Dictionary/francais.txt", encoding="utf-8").read().lower().split()),
        "English": set(open("Cipher/Brut_Force/Scoring/Dictionary/english.txt", encoding="utf-8").read().lower().split())
    }

DICTIONARIES = load_dictionaries()
