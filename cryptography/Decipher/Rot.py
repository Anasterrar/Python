from Cipher.Rot import Rot_menu, select_rot

def rot_decipher():
    mode = "menu_decryption"
    m = Rot_menu(mode)
    if m == "back":
        return None
    return select_rot(m, mode)