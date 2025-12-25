# Calculatrice
import os
import pyfiglet
import json
from colorama import Fore, Style, init
init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def header_():
    header = pyfiglet.figlet_format("CALCULATRICE", font="slant")
    print(Fore.CYAN + header)
    print(Fore.YELLOW + "💡 Ctrl+C pour quitter")
    print(Fore.YELLOW + "💡 H pour historique des calculs")
    print(Fore.MAGENTA + "───────────────────────────────")
    return

def show_history(hist):
    clear()
    header_()
    print(Fore.GREEN + "📜 Historique des 10 derniers résultats :")
    print(Fore.MAGENTA + "───────────────────────────────")
    if len(hist) == 0:
        print(Fore.RED + "Aucun historique disponible.")
    else:
        for i, h in enumerate(hist, start=1):
            print(Fore.CYAN + f"{i}. {h}")
    print(Fore.MAGENTA + "───────────────────────────────")
    input(Fore.YELLOW + "\n👉 Appuie sur Entrée pour revenir")
    clear()

def isValidNum(num):
    num = formalize(num)
    if num.count(".") > 1:
        print(Fore.RED + "⚠️ Plus d'une virgule. Veuillez entrer un nombre valide")
        return False
    num_no_dot = num.replace(".", "")
    if num_no_dot.isdigit() == False:
        print(Fore.RED + " ⚠️ Veuillez entrer un nombre")
        return False
    else:
        return True

def isFloat(num):
    return ("." in num or "," in num)

def formalize(num):
    num = num.replace(",", ".")
    num = num.replace(" ", "")
    return num

def isValidSign(sign):
    sign = formalize(sign)
    if sign not in ["+", "-", "x", "X", "/", ":", "**", "^", "*"]:
        print(Fore.RED + "💀 Veuillez entrer un signe valide")
        return False
    else:
        return True

def calcul(a, o , b):
    if o == "+": return a + b
    if o == "-": return a - b
    if o in ["x", "X", "*"]: return a * b
    if o in ["/", ":"]: return a / b
    if o in ["**", "^"]: return a ** b

def reload():
    print("👉 Appuie sur Entrée pour un autre calcul")
    continuer = input()
    if continuer == "":
        clear()
        return True
    else:
        return False

def intOrFloat(num):
    return float(num) if isFloat(num) else int(num)

def num():
    # Nombre 1
    a = input("👉 Entrez le premier nombre (ou H pour historique) : ")
    if a.upper() == "H":
        return "H"
    a = formalize(a)
    if not isValidNum(a):
        return
    a = intOrFloat(a)
    print(a)
    # Signe
    o = input("👉 Entrez l'opération (+, -, x, /, **): ")
    if not isValidSign(o):
        return
    o = formalize(o)
    print(a, o)
    # Nombre 2
    b = input("👉 Entrez le deuxieme nombre: ")
    b = formalize(b)
    if not isValidNum(b):
        return
    b = intOrFloat(b)
    if o == "/" and b == 0:
        print("Erreur : division par zéro impossible")
        return
    print(a, o, b)
    # Résultat
    print(Fore.GREEN + "───────────────────────────────")
    resultat = calcul(a, o, b)
    if isinstance(resultat, float) and resultat.is_integer():
        print(f"🟰 {int(resultat)}")
    else:
        print(f"🟰 {resultat}")
    print(Fore.GREEN + "───────────────────────────────\n")
    operation_str = f"{a} {o} {b} = {resultat}"
    return operation_str

# --------------------
# Programme principal
# --------------------

operation_str = None
historic = []
with open("historic.json", "r") as f:
        historic = json.load(f)
while True:
    clear()
    header_()
    # Affichage du calcul précédent
    if operation_str is not None:
        print(Fore.YELLOW + f"🕘 Calcule précédent : {operation_str}")
        print(Fore.MAGENTA + "───────────────────────────────")
    # Calcul
    result = num()
    # Si l'utilisateur demande l'historique
    if result == "H":
        show_history(historic)
        continue
    # Si erreur ou entrée invalide → recommencer
    if result is None:
        continue
    # result = operation_str
    operation_str = result
    # Ajout dans historique
    if len(historic) >= 10:
        historic.pop(0)
    historic.append(operation_str)
    with open("historic.json", "w") as f:
        json.dump(historic, f)
    # Reload
    if not reload():
        break