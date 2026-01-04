import os
from Components.show_result import show_result
from Components.create_file import create_file
from Components.settings import settings
from Components.Menus import mode_menu
from Components.debug_file import debug_file

# -----------------
# Programme
#------------------
while True:
    settings(True)
    choice = mode_menu.mode_menu()
    if choice == "quit":
          os.system("cls")
          break
    action = mode_menu.DISPATCH_MODE.get(choice)
    if action is None:
          continue
    result = action()
    if result is None or result == "quit":
          debug_file("None")
          continue
    debug_file("TRUE")
    # Resultat
    if show_result(result) == True:
            create_file(result)