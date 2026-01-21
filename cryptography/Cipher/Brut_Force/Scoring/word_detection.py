from Cipher.Brut_Force.Scoring.Dictionary.dictionary import DICTIONARIES

def formalize_word(word):
    if "'" in word and len(word) > 1 and word[1] == "'":
        return word[2:]
    return word

def word_detection(text):
    words = text.lower().split()
    scores = {"French": 0, "English": 0}

    for word in words:
        word = formalize_word(word)
        if word in DICTIONARIES["French"]:
            scores["French"] += 1
        if word in DICTIONARIES["English"]:
            scores["English"] += 1

    return scores
