def Vigenere_decrypt(text, keys):
    result = ""
    i = 0
    for c in text:
        if i > len(keys) - 1:
            i = 0
        #Minuscule
        if 'a' <= c <= 'z':
            base = ord('a')
            result += chr((ord(c) - base - keys[i]) % 26 + base)
            i = (i + 1) % len(keys)
        elif 'A' <= c <= 'Z':
            base = ord('A')
            result += chr((ord(c) - base - keys[i]) % 26 + base)
            i = (i + 1) % len(keys)
        else:
            result += c
    return result