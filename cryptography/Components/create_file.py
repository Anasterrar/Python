import os
from Components.header import header

path = "key/"
if not os.path.isdir(path):
   os.makedirs(path)

def create_file(data):
    formated_data = f"Text : {data[0]}\nKey : {str(data[1])}\nCoded text : {data[2]}\nMethode: {data[3]}"
    a = 1
    while True:
        path = f"key/key{a}.txt"
        if os.path.isfile(path) == True:
            a += 1
        else:
            with open(path, "w") as f:
                f.write(formated_data)
            print(f"Votre fichier 'key{a}.txt' à été créé dans le dossier key")
            input("Appuyez sur entrer pour continuer")
            break