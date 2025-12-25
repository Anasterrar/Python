import os
from Cipher.Caesar import Caesar_cipher
from Cipher.Rot import rot
from Cipher.Poly import poly_cipher
from Cipher.Vigenere import vigenere_cipher
from Cipher.Caesar_affine import affine
from Components.menus import main_menu
from Components.show_result import show_result
from Components.create_file import create_file
from Components.settings import run_settings, settings

DISPATCH_MAIN = {
    1: Caesar_cipher,
    2: rot,
    3: poly_cipher,
    4: vigenere_cipher,
    5: affine,
    6: run_settings,
}
# -----------------
# Programme
#------------------
while True:
    settings(True)
    choice = main_menu()
    if choice == "quit":
          os.system("cls")
          break
    action = DISPATCH_MAIN.get(choice)
    if action is None:
          continue
    result = action()
    if result is None:
          continue
    # Resultat
    if show_result(result) == True:
            create_file(result)