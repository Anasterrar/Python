from Cipher.Brut_Force.Scoring.word_detection import formalize_word

SYLLABLES = {
    "French": [
        "le","de","re","en","es","on","an","au","ai","et","in","el",
        "al","er","ou","oi","im","ir","em","un","eu","tion","ment",
        "est","ent","age","eur","ise","ant"
    ],
    "English": [
        "th","he","in","er","an","re","on","at","en","nd","ed","ou",
        "ha","to","or","it","is","hi","es","ng","tion","ing","ous",
        "ment","ent","ive","est","ant","ate"
    ]
}

def syllables_detection(text):
    words = text.lower().split()
    scores = {"French": 0, "English": 0}

    for word in words:
        word = formalize_word(word)
        for lang in scores:
            for syl in SYLLABLES[lang]:
                if syl in word:
                    scores[lang] += 1

    return scores
