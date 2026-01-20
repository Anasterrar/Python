from Caesar.Ceasar import Caesar_decrypt
from Scoring.letter_frequency import frequency_score

def formalize(text):
    result = ""
    for c in text:
        if c.isalpha():
            result += c
    return result.lower()

def set_columns(text, len_key):
    text = formalize(text)
    cols = []
    for i in range(0, len_key):
        cols.append("")
    for i, c in enumerate(text):
        cols[i % len_key] += c
    return cols

def top_columns(all_colunms):
    all_cols_results = {} 
    for len_key, columns in all_colunms.items():
        all_cols_results[len_key] = []

        for  col in columns:
            top5 = []

            for caesar in range(26):
                candidate = Caesar_decrypt(col, caesar)
                score = frequency_score(candidate)
                best_score = min(score["French"], score["English"])


                top5.append({
                    "score": best_score,
                    "shift": caesar,
                })

            top5.sort(key=lambda x: x["score"])
            all_cols_results[len_key].append(top5[:1]) #variable
    return all_cols_results
