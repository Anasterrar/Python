
def Caesar_affine(string, a, b):
        string_coded = ""
        for c in string:
            #Minuscule
            if ord(c) >= 97 and ord(c) <= 122:
                string_coded += chr((a * (ord(c) - 97 - int(b)) ) % 26 + 97)
            #Majuscule
            elif ord(c) >= 65 and ord(c) <= 90:
                string_coded += chr((a * (ord(c) - 65 - int(b))) % 26 + 65)
            else:
                string_coded += c
        return string_coded
