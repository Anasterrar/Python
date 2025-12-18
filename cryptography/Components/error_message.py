from Components.text_selection import text_selection

def error_message(errors):
    data = text_selection("text")
    for error in errors:
        print(data[error])

