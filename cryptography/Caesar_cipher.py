def Caesar_cipher():
    string = input("Veuillez entrer ce qui doit etre chiffré: \n")
    value = int(input("Veuillez entrer la valeur de chiffrement: \n"))
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
    return string, value, string_coded