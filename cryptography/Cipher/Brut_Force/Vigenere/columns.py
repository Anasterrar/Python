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

def top_columns(all_colunms, Top):
    all_cols_results = {} 
    for len_key, columns in all_colunms.items():
        all_cols_results[len_key] = []

        for  col in columns:
            topN = []

            for caesar in range(26):
                candidate = Caesar_decrypt(col, caesar)
                score = frequency_score(candidate)
                best_score = min(score["French"], score["English"])


                topN.append({
                    "score": best_score,
                    "shift": caesar,
                })

            topN.sort(key=lambda x: x["score"])
            all_cols_results[len_key].append(topN[:Top]) #variable
    return all_cols_results

def extract_shift(all_cols_results, possibles_len):
    all_shift_by_cols = []
    for lenght in possibles_len:
        shift_by_cols = []
        for col_result in all_cols_results[lenght]:
            shift_by_col = []
            for shift in col_result:
                shift_by_col.append(shift["shift"])
            shift_by_cols.append(shift_by_col)
        all_shift_by_cols.append( shift_by_cols)
    return all_shift_by_cols  