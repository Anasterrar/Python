from Cipher import Caesar
from Cipher import Rot
from Cipher import poly
from Cipher import vigenere
from Components import header
from Components import menu
from Components import show_result
from Components import create_file
import os

# -----------------
# Programme
#------------------
while True:
    a = menu.menu()
    if a == 1:
        result = Caesar.Caesar_cipher()
        if show_result.show_result(result) == True:
            create_file.create_file(result)
    elif a == 2:
        m = Rot.Rot_menu()
        result = Rot.select_rot(m)
        if show_result.show_result(result) == True:
            create_file.create_file(result)
    elif a == 3:
        result = poly.poly_cipher()
        if show_result.show_result(result) == True:
            create_file.create_file(result)
    elif a == 4:
        result = vigenere.vigenere()
        if show_result.show_result(result) == True:
            create_file.create_file(result)

    
        
