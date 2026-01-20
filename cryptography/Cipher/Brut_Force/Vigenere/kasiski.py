import math
def formalize(text):
    result = ""
    for c in text:
        if c.isalpha():
            result += c
    return result.lower()

def kasiski(text):
    text = formalize(text)
    paternes = []
    trigrams = {}
    for i in range(len(text) - 3): #variable
        trigrams.setdefault(text[i: i + 3], []).append(i) #variable
    for trigram, positions in trigrams.items():
        if len(positions) >= 2:
            distances = calcule_distances(positions)
            possible_len = calcule_all_possibles_len(distances)
            paternes.append({
                "paterne": trigram, 
                "positions" : positions,
                "distances": distances,
                "possibles_len": possible_len,
                })
    return paternes

def calcule_distances(positions):
    distances = []
    for i in range(0, len(positions) - 1):
        distances.append(positions[i + 1] - positions[i])
    return distances


def calcule_all_possibles_len(distances):
    possible_len = []
    pgcd = math.gcd(*distances)
    for i in range(1, pgcd + 1):
        if pgcd % i == 0 and 2 <= i <= 60: #variable
             possible_len.append(i)
    return possible_len

def calcul_possibles_len(paternes):
    possibles_len = []
    for paterne in paternes:
        for length in paterne['possibles_len']:
            possibles_len.append(length)
    possibles_len = sorted(list(set(possibles_len)))
    return possibles_len


