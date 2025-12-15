import os
from Components.header import header

def Rot_menu():
    while True:
        options = ["1. ROT13", "2. ROT47", "3. ROT18"]
        header("ROT")
        for opt in options:
            print(opt)
        answer = input("Entrez le numero de la methode de cryptage : ")
        if answer.isdigit() == True:
            return int(answer)

def select_rot(num):
    if num == 1:
        code = Rot13_cipher()
        return code
    elif num == 2:
        code = Rot47_cipher()
        return code
    elif num == 3:
        code = Rot18_cipher()
        return code

def Rot13_cipher():
    error = False
    while True:
        methode = "ROT 13"
        header(methode)
        if error == True:
            print("❌ La chaine de carractere doit contenir au moins une lettre.")
        string = input("Veuillez entrer ce qui doit etre chiffré: \n")
        if not string:
            error = True
            continue
        value = 13
        string_coded = ""
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 + value) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 + value) % 26 + 65)
            else:
                string_coded += c
        error = False
        return string, value, string_coded, methode

def Rot47_cipher():
    error = False
    while True:
        methode = "ROT 47"
        header(methode)
        if error == True:
            print("❌ La chaine de carractere doit contenir au moins une lettre.")
        string = input("Veuillez entrer ce qui doit etre chiffré: \n")
        if not string:
            error = True
            continue
        value = 47
        string_coded = ""
        for c in string:
            #Minuscule
            if ord(c) >= 33 and ord(c) <= 126:
                string_coded += chr((ord(c) - 33 + value) % 94 + 33)
            else:
                string_coded += c
        error = False
        return string, value, string_coded, methode

def Rot18_cipher():
    error = False
    while True:
        methode = "ROT 18"
        header(methode)
        if error == True:
            print("❌ La chaine de carractere doit contenir au moins une lettre.")
        string = input("Veuillez entrer ce qui doit etre chiffré: \n")
        if not string:
            error = True
            continue
        value1 = 13
        value2 = 5
        values = f"{value1} pour les lettres et {value2} pour les chiffres"
        string_coded = ""
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((ord(c) - 97 + value1) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((ord(c) - 65 + value1) % 26 + 65)
            #Chiffre
            elif ord(c) >= 48 and ord(c) <= 57:
                string_coded += chr((ord(c) - 48 + value2) % 10 + 48)
            else:
                string_coded += c
        error = False
        return string, values, string_coded, methode