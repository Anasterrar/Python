def Caesar_decrypt(text, key):
    result = ""
    for c in text:
        #Minuscule
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr((ord(c)-97-key) % 26 + 97)
        #Majuscule
        elif ord(c) >= 65 and ord(c) <= 90:
            result += chr((ord(c)-65-key) % 26 + 65)
        else:
            result += c
    return result
