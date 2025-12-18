from Components.text_selection import text_selection

def input_message(text):
    data = text_selection("text")
    return input(data[text])