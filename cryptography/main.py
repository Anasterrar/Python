import os
from Components.show_result import show_result
from Components.create_file import create_file
from Components.settings import settings
from Components.Menus import mode_menu

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
            continue

      # si action() renvoie (payload, mode)
      if not isinstance(result, (tuple, list)) or len(result) < 2:
            continue

      payload, mode = result
      if payload is None or payload in ("quit", "back"):
            continue

      if show_result(payload, mode):
            create_file(payload, mode)
