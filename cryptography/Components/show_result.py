from Components.header import header
from Components import text_selection
data = text_selection.text_selection("text")

def show_result(result):
        while True:
            header(result[3])
            print(f"{data["text"]} : {result[0]}")
            print(f"{data["key"]} : {result[1]}")
            print(f"{data["coded_text"]} : {result[2]}")
            print(f"{data["method"]} : {result[3]}")
            answer = input(data["save_question"])
            print(answer)
            if answer in ["y", "Y", "yes", "Yes", "YES"]:
                return True
            elif answer in ["n", "N", "no", "No", "NO"]:
                return False
            else:
                print({data["error_invalid_YesOrNo"]})