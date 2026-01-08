#from Components.header import header
#from Components.error_message import error_message
#from Components.input_message import input_message


def Brut_force_Caesar():
    mode = "menu_decryption"
    method = "menu_caesar"
    error = False
    all_possibilities = []
    while True:
        #header(method, "caesar", mode)
        #if error == True:
            #error_message(["error_empty_text"])
        string = input("Entrez le texte à déchiffrer: \n")
        if not string:
            error = True
            continue
        for i in range(0, 26):
            values = Caesar_decipher(string, i)
            all_possibilities.append({"key": i, "text": values})
        return all_possibilities

def Caesar_decipher(string, key):
    while True:
        string_decoded = ""
        key = int(key)
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_decoded += chr((ord(c) - 97 - key) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_decoded += chr((ord(c) - 65 - key) % 26 + 65)
            else:
                string_decoded += c
        return string_decoded