def formalize(text):
    result = ""
    for c in text:
        if c.isalpha():
            result += c
    return result.lower()