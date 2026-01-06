#from Components.debug_file import debug_file

def debug_file(result):
        path = f"exports/debug.txt"
        with open(path, "a") as f:
            f.write(str(result))