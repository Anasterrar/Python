from Components.header import header
import random

def affine_menu():
    while True:
        options = ["1. Clé manuelle (avancé)", "2. Clé automatique (recommandé)"]
        header("Caesar affine")
        for opt in options:
            print(opt)
        answer = input("Entrez le numero de la methode de cryptage : ")
        if answer.isdigit() == True:
            return int(answer)
        
def select_affine(num):
    auto = False
    if num == 1:
        code = Caesar_affine(auto)
        return code
    elif num == 2:
        auto = True
        code = Caesar_affine(auto)
        return code

def isValidA(a):
    if a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        return True
    else:
        return False

#(ax + b) modulo 26, a premier avec 27
def Caesar_affine(auto):
    error = False
    while True:
        methode = "Caesar affine"
        header(methode)
        if error == True:
            print("❌ La chaine de carractere doit contenir au moins une lettre.")
            print("❌ Les valeur de chiffrement doivent contenir au moins un chiffre.")
            print("❌ La premiere valeur de chiffrement doit etre premiere avec 26 (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)")
        string = input("Veuillez entrer ce qui doit etre chiffré: \n")
        if not string:
            error = True
            continue
        if auto == True:
            a_value = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
            a = str(random.choice(a_value))
        if auto == False:
            a = input("Veuillez entrer la premiere valeur de chiffrement: \n")
        if not a or a.isdigit() == False or isValidA(int(a)) == False:
            error = True
            continue
        b = input("Veuillez entrer la deuxieme valeur de chiffrement: \n")
        if not b or b.isdigit() == False:
            error = True
            continue
        string_coded = ""
        key = f"a = {a} et b = {b}"
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((int(a) * (ord(c) - 97) + int(b)) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((int(a) * (ord(c) - 65) + int(b)) % 26 + 65)
            else:
                string_coded += c
        error = False
        return string, key, string_coded, methode
