from Cipher.Cipher.Rot import Rot_menu, select_rot

def Rot():
    mode = "menu_decryption"
    m = Rot_menu(mode)
    if m == "back":
        return None
    return select_rot(m, mode)