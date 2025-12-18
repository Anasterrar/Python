from Components.header import header
from Components.text_selection import text_selection
from Components.error_message import error_message
from Components.input_message import input_message


def show_result(result):
        data = text_selection("text")
        error = False
        while True:
            header(result[3], None)
            print(f"{data["text"]} : {result[0]}")
            print(f"{data["key"]} : {result[1]}")
            print(f"{data["coded_text"]} : {result[2]}")
            print(f"{data["method"]} : {data[result[3]]}")
            if error == True:
                error_message(["error_invalid_YesOrNo"])
            answer = input_message("save_question")
            print(answer)
            if answer in ["y", "Y", "yes", "Yes", "YES"]:
                return True
            elif answer in ["n", "N", "no", "No", "NO"]:
                return False
            else:
                error = True