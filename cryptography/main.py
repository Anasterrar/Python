import os
import Caesar
import Rot
import pyfiglet
import poly
from colorama import Fore, Style, init
init(autoreset=True)

path = "key/"
if not os.path.isdir(path):
   os.makedirs(path)

def header(text):
    header = pyfiglet.figlet_format(text, font="slant")
    print(Fore.CYAN + header)
    print(Fore.MAGENTA + "───────────────────────────────")
    print(Fore.YELLOW + "Coder un texte")
    print(Fore.YELLOW + "💡 Ctrl+C pour quitter")
    print(Fore.MAGENTA + "───────────────────────────────")
    return

def menu():
    options = ["1. César classique", "2. Chiffrement ROT", "3. César polyalphabétique", "4. Chiffre de Vigenère", "5. César affine" ]
    os.system("cls")
    header("Cryptography")
    for opt in options:
        print(opt)
    answer = input("Entrez le numero de la methode de cryptage : ")
    if answer.isdigit() == True:
        return int(answer)
    else:
        menu()

def show_result(result):
        print(f"Texte : {result[0]}")
        print(f"Clé : {result[1]}")
        print(f"Texte codé : {result[2]}")
        print(f"Methode : {result[3]}")
        while True:
            answer = input("Voulez-vous stocker ces informations dans un fichier texte ? (y/n): ")
            print(answer)
            if answer in ["y", "Y", "yes", "Yes", "YES"]:
                return True
            elif answer in ["n", "N", "no", "No", "NO"]:
                return False
            else:
                print("⚠️ Repondez par 'y'(yes) ou 'n'(no)")

def createFile(data):
    formated_data = f"Text : {data[0]}\nKey : {str(data[1])}\nCoded text : {data[2]}\nMethode: {data[3]}"
    a = 1
    while True:
        path = f"key/key{a}.txt"
        if os.path.isfile(path) == True:
            a += 1
        else:
            with open(path, "w") as f:
                f.write(formated_data)
            print(f"Votre fichier 'key{a}.txt' à été créé dans le dossier key")
            input("Appuyez sur entrer pour continuer")
            break

# -----------------
# Programme
#------------------
while True:
    a = menu()
    if a == 1:
        os.system("cls")
        header("Caesar cipher")
        code = Caesar.Caesar_cipher()
        os.system("cls")
        header("Caesar cipher")
        b = show_result(code)
        if b == True:
            creatFile(code)
    elif a == 2:
        os.system("cls")
        header("Rot")
        m = Rot.Rot_menu()
        print(m)
        os.system("cls")
        header("Rot")
        code = Rot.select_rot(m)
        print(code)
        os.system("cls")
        header("Rot")
        b = show_result(code)
        if b == True:
            createFile(code)
    elif a == 3:
        os.system("cls")
        header("Chiffrement polyalphabétique")
        code = poly.poly_cipher()
        os.system("cls")
        header("Chiffrement polyalphabétique")
        b = show_result(code)
        if b == True:
            createFile(code)
        
