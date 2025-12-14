def formalize(data):
    data = data.replace(",", " ")
    data = data.split()
    return data

def poly_cipher():
    methode = "Code Cesar polyalphabétique"
    string = input("Veuillez entrer ce qui doit etre chiffré: \n")
    value = input("Veuillez entrer les valeurs de chiffrement séparées par des espaces ou des virgules : \n")
    value = formalize(value)            
    string_coded = ""
    i = 0
    for c in string:
        if i > len(value)- 1:
            i = 0
    #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            string_coded += chr((ord(c) - 97 + int(value[i])) % 26 + 97)
            i += 1
    #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            string_coded += chr((ord(c) - 65 + int(value[i])) % 26 + 65)
            i += 1
        else:
            string_coded += c
    value = " ".join(value)
    return string, value, string_coded, methode

 