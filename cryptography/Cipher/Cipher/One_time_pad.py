import ast
import random
from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def OTP_Cipher():
    mode = "menu_encryption"
    return One_time_pad(mode)

def One_time_pad(mode):
    method = "menu_otp"
    error = False
    while True:
        header(method, "otp", mode)
        if error == True:
            error_message(["error_empty_text", "error_empty_key"])
        string = input_message("input_text")
        print(string)
        if not string:
            error = True
            continue
        if mode == "menu_decryption":
            string = ast.literal_eval(string)
        string_coded = [None] * len(string)
        if mode == "menu_decryption":
            keys = ast.literal_eval(input_message("input_unique_key"))
        else:
            keys = random.sample(range(0, 256), len(string))
        for i in range(0, len(string)):
            string_coded[i] = chr(ord(string[i]) ^ keys[i])
        if mode == "menu_decryption":
            string_coded_formated = "".join(string_coded)
            return string, keys, string_coded_formated, method
        else:
            return string, keys, string_coded, method