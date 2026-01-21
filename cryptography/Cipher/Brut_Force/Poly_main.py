from Cipher.Brut_Force.Vigenere_main import Vigenere_main

def Poly_main():
    result = Vigenere_main()
    keys = []
    for c in result[1]:
        keys.append(ord(c))
    return result[0], keys, result[2], result[3]