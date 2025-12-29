def debug_file(result):
        path = f"key/debug.txt"
        with open(path, "w") as f:
            f.write(str(result))

