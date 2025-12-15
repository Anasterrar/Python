from Components.header import header

def formalize(data):
    for c in data:
        if c.isalpha() == False:
            data = data.replace(c, '')
    return data

def vigenere():
    error = False
    while True:
        methode = "Vigenere"
        string_coded = ""
        i = 0
        header(methode)
        if error == True:
             print("❌ La chaine de carractere doit contenir au moins une lettre.")
             print("❌ La clé doit contenir au moins une lettre.")
        string = input("Veuillez entrer ce qui doit etre chiffré: \n")
        if not string:
            error = True
            continue
        value = input("Veuillez entrer la clé de chiffrement (mot): \n")            
        value = formalize(value)
        if not value:
            error = True
            return
        for c in string:
            if i > len(value)- 1:
                i = 0
            #Minuscule
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
        error = False
        return string, value, string_coded, methode
