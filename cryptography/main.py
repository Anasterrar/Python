from Cipher.Caesar import Caesar_cipher
from Cipher.Rot import select_rot
from Cipher.Poly import poly_cipher
from Cipher.Vigenere import vigenere
from Cipher.Caesar_affine import select_affine
from Components.menus import main_menu, Rot_menu, affine_menu
from Components.show_result import show_result
from Components.create_file import create_file
from Components.settings import settings
# -----------------
# Programme
#------------------
while True:
    settings(True)
    a = main_menu()
    if a == 1:
        result = Caesar_cipher()
    elif a == 2:
        m = Rot_menu()
        result = select_rot(m)
    elif a == 3:
        result = poly_cipher()
    elif a == 4:
        result = vigenere()
    elif a == 5:
        m = affine_menu()
        result = select_affine(m)
    elif a == 6:
        settings(False)
        continue
    elif a == None:
         break
    # Resultat
    if show_result(result) == True:
            create_file(result)
    
        
