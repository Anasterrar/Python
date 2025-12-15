from Components.header import header

def Caesar_cipher():
    error = False
    while True:
        methode = "Caesar cipher"
        header(methode)
        if error == True:
            print("❌ La chaine de carractere doit contenir au moins une lettre.")
            print("❌ La valeur de chifferement doit contenir au moins un chiffre.")
        string = input("Veuillez entrer ce qui doit etre chiffré: \n")
        if not string:
            error = True
            continue
        value = input("Veuillez entrer la valeur de chiffrement: \n")
        if not value:
            error = True
            continue
        string_coded = ""
        value = int(value)
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