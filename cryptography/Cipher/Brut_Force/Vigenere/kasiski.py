import math

def kasiski(formalized_text, len_max, ngram, fallback=True):
    text = formalized_text 

    for attempt in range(2 if fallback else 1):
        paternes = []
        grams = {}

        for i in range(len(text) - (ngram - 1)):
            grams.setdefault(text[i:i + ngram], []).append(i)

        for gram, positions in grams.items():
            if len(positions) >= 2:
                distances = calcule_distances(positions)
                possible_len = calcule_all_possibles_len(distances, len_max)

                if possible_len: 
                    paternes.append({
                        "paterne": gram,
                        "positions": positions,
                        "distances": distances,
                        "possibles_len": possible_len,
                    })

        if paternes:
            return paternes
        ngram = 2 if ngram == 3 else 3

    return None

def calcule_distances(positions):
    distances = []
    for i in range(0, len(positions) - 1):
        distances.append(positions[i + 1] - positions[i])
    return distances

def calcule_all_possibles_len(distances, len_max):
    possible_len = []
    pgcd = math.gcd(*distances)
    for i in range(1, pgcd + 1):
        if pgcd % i == 0 and 2 <= i <= len_max:
             possible_len.append(i)
    return possible_len

def calcul_possibles_len(paternes):
    possibles_len = []
    for paterne in paternes:
        for length in paterne['possibles_len']:
            possibles_len.append(length)
    possibles_len = sorted(list(set(possibles_len)))
    return possibles_len