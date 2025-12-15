def formalize(data):
    for c in data:
        if c.isalpha() == False:
            data = data.replace(c, '')
    return data

def vigenere():
    methode = "Vigenère"
    string = input("Veuillez entrer ce qui doit etre chiffré: \n")
    if not string:
        print("❌ La chaine de carractere doit contenir au moins une lettre.")
        return
    value = input("Veuillez entrer la clé de chiffrement (mot): \n")            
    string_coded = ""
    i = 0
    value = formalize(value)
    if not value:
        print("❌ La clé doit contenir au moins une lettre.")
        return
    for c in string:
        #Minuscule
        if i > len(value)- 1:
            i = 0
        if ord(c) >= 97 and ord(c) <= 122:
            if ord(value[i]) >= 97 and ord(value[i]) <= 122:
                string_coded += chr((ord(c) - 97 + ord(value[i]) - 97) % 26 + 97)
            elif ord(value[i]) >= 65 and ord(value[i]) <= 90:
                string_coded += chr((ord(c) - 97 + ord(value[i]) - 65) % 26 + 97)
            i += 1
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            if ord(value[i]) >= 97 and ord(value[i]) <= 122:
                string_coded += chr((ord(c) - 65 + ord(value[i]) - 97) % 26 + 65)
            elif ord(value[i]) >= 65 and ord(value[i]) <= 90:
                string_coded += chr((ord(c) - 65 + ord(value[i]) - 65) % 26 + 65)
            i += 1
        else:
            string_coded += c
    print(string_coded)
    return string, value, string_coded, methode
