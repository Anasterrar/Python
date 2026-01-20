def Affine_decrypt(text, a, b):
        result = ""
        for c in text:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                result += chr((a * (ord(c) - 97 - int(b)) ) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                result += chr((a * (ord(c) - 65 - int(b))) % 26 + 65)
            else:
                result += c
        return result
