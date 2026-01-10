from Cipher.Caesar_affine import Brut_force_Caesar

paths = ["francais.txt", "english.txt"]

def formalize_word(word):
    if "'" in word and word[1] == "'":  
        word = word[2:]
    return(word)

def language(words, syllables):
    result = probable_language(words[1], "words" )
    if result == "indéterminé":
        result = probable_language(syllables[1], "syllables")
    return result

def probable_language(langue, unity):
    if langue[0][unity] > langue[1][unity]:
        probable_language = langue[0]['language']
    if langue[0][unity] == langue[1][unity]:
        probable_language = "indéterminé"
    if langue[0][unity] < langue[1][unity]:
        probable_language = langue[1]['language']
    return probable_language

def word_detection(text):
    words = text.lower().split()
    langue_words = [
        {'language': 'French', 'words' : 0},
        {'language': 'English', 'words' : 0},
    ]
    count_word = 0

    for langue, path in zip(langue_words, paths):
        with open (path, 'r') as file:
            dictionary = set(w.lower() for w in file.read().split())
            for word in words:
                formalize_word(word)
                if word in dictionary:
                    count_word += 1
                    langue['words'] += 1
    return count_word, langue_words

def syllables_detection(text):
    words = text.lower().split()

    langue_syllables = [
        {'language': 'French', 'syllables' : 0},
        {'language': 'English', 'syllables' : 0},
    ]

    freq_syllables_fr = [
    "le", "de", "re", "en", "es", "on", "an", "au",
    "ai", "et", "in", "el", "al", "er", "ou", "oi",
    "im", "ir", "em", "un", "eu", "tion", "ment",
    "est", "ent", "age", "eur", "ise", "ant"
    ]

    freq_syllables_en = [
    "th", "he", "in", "er", "an", "re", "on", "at", "en", "nd",
    "ed", "ou", "ha", "to", "or", "it", "is", "hi", "es", "ng",
    "tion", "ing", "ous", "ment", "ent", "ive", "est", "ant", "ate"
    ]

    syllables_by_langue = (freq_syllables_fr, freq_syllables_en)

    count_syllables = 0
    for langue, syllables in zip(langue_syllables, syllables_by_langue):
        for word in words:
            word = formalize_word(word)
            for syllable in syllables:
                if syllable in word:
                    count_syllables += 1
                    langue['syllables'] += 1
    return count_syllables, langue_syllables

def scoring(all_possibilities):
    best = {
        "score" : 0,
        "key": None,
        "text": None,
        "langue": None
    }
    for possibility in all_possibilities:
        word_score = word_detection(possibility["text"])
        syllables_score = syllables_detection(possibility["text"])
        total_score = word_score[0] * 2 + syllables_score[0]
        if total_score > best["score"]:
            best["score"] = total_score
            best["text"] = possibility["text"]
            best["key"] = possibility["key"]
            best["langue"] = language(word_score, syllables_score)
    return best

result = Brut_force_Caesar()
print(scoring(result))