from Cipher.Brut_Force.Scoring.word_detection import word_detection
from Cipher.Brut_Force.Scoring.syllables_detection import syllables_detection

def scoring(all_possibilities):
    best = {
        "score": -1,
        "key": None,
        "text": None,
        "langue": None
    }

    for possibility in all_possibilities:
        text = possibility["text"]

        word_scores = word_detection(text)
        syll_scores = syllables_detection(text)

        total_fr = word_scores["French"] * 2 + syll_scores["French"]
        total_en = word_scores["English"] * 2 + syll_scores["English"]

        if total_fr > total_en:
            total = total_fr
            langue = "French"
        else:
            total = total_en
            langue = "English"

        if total > best["score"]:
            best.update({
                "score": total,
                "key": possibility["key"],
                "text": text,
                "langue": langue
            })

    return best