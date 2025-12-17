from Cipher import Caesar
from Cipher import Rot
from Cipher import poly
from Cipher import vigenere
from Cipher import Caesar_affine
from Components import menu
from Components import show_result
from Components import create_file
from Components import settings
# -----------------
# Programme
#------------------
while True:
    settings.settings(True)
    a = menu.menu()
    if a == 1:
        result = Caesar.Caesar_cipher()
    elif a == 2:
        m = Rot.Rot_menu()
        result = Rot.select_rot(m)
    elif a == 3:
        result = poly.poly_cipher()
    elif a == 4:
        result = vigenere.vigenere()
    elif a == 5:
        m = Caesar_affine.affine_menu()
        result = Caesar_affine.select_affine(m)
    elif a == 6:
        settings.settings(False)
        continue
    # Resultat
    if show_result.show_result(result) == True:
            create_file.create_file(result)
    
        
