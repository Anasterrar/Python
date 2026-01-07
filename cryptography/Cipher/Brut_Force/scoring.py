import os

paths = ["francais.txt", "english.txt"]

def formalize_word(word):
    if "'" in word and word[1] == "'":  
        word = word[2:]
    return(word)

def probable_language(langue_words):
    if langue_words[0]['words'] > langue_words[1]['words']:
        probable_language = langue_words[0]['language']
    if langue_words[0]['words'] == langue_words[1]['words']:
        probable_language = "indéterminé"
    if langue_words[0]['words'] < langue_words[1]['words']:
        probable_language = langue_words[1]['language']
    return probable_language

def is_in_dictionary(text):
    words = text.lower().split()
    langue_words = [
        {'language': 'French', 'words' : 0},
        {'language': 'English', 'words' : 0},
    ]
    number_of_word = 0

    for langue, path in zip(langue_words, paths):
        with open (path, 'r') as file:
            dictionary = set(w.lower() for w in file.read().split())
            for word in words:
                formalize_word(word)
                if word in dictionary:
                    number_of_word += 1
                    langue['words'] += 1
    return number_of_word, langue_words


def syllables_detection(text):
    words = text.lower().split()
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

    langue_syllables = [
        {'language': 'French', 'syllables' : 0},
        {'language': 'English', 'syllables' : 0},
    ]
    number_of_syllables = 0
    for langue, syllables in zip(langue_syllables, syllables_by_langue):
        for word in words:
            formalize_word(word)
            for syllable in syllables:
                if syllable in word:
                    print(word)
                    print(langue["language"] + " " + syllable)
                    number_of_syllables += 1
                    langue['syllables'] += 1
    return number_of_syllables, langue_syllables



result = syllables_detection("Bonjour")
print(result)

