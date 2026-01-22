import ast
import random
from Components.header import header
from Components.error_message import error_message
from Components.input_message import input_message

def OTP():
    mode = "menu_encryption"
    return One_time_pad(mode)

def One_time_pad_cipher(mode, string):
    if mode == "menu_decryption":
            string = ast.literal_eval(string)
    string_coded = [None] * len(string)
    if mode == "menu_decryption":
        keys = ast.literal_eval(input_message("input_unique_key"))
    else:
        keys = random.sample(range(0, 256), len(string))
    string_coded = [None] * len(string)
    for i in range(0, len(string)):
            string_coded[i] = chr(ord(string[i]) ^ keys[i])
    return string_coded, keys

def One_time_pad(mode):
    method = "menu_otp"
    error = False
    while True:
        header(method, "otp_cipher", mode)
        if error == True:
            error_message(["error_empty_text"])
        string = input_message("input_text")
        if not string:
            error = True
            continue
        result = One_time_pad_cipher(mode, string)
        string_coded = result[0]
        keys = result[1]
        if mode == "menu_decryption":
            string_coded_formated = "".join(string_coded)
            return string, keys, string_coded_formated, method
        else:
            return string, keys, string_coded, method