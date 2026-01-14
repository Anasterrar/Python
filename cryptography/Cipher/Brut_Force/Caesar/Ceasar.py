def caesar_decrypt(text, key):
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c)-97-key) % 26 + 97)
        elif 'A' <= c <= 'Z':
            result += chr((ord(c)-65-key) % 26 + 65)
        else:
            result += c
    return result
