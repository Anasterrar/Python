from Components.header import header

def menu():
    options = ["1. César classique", "2. Chiffrement ROT", "3. César polyalphabétique", "4. Chiffre de Vigenère", "5. César affine" ]
    header("Cryptography")
    for opt in options:
        print(opt)
    answer = input("Entrez le numero de la methode de cryptage : ")
    if answer.isdigit() == True:
        return int(answer)
    else:
        menu()