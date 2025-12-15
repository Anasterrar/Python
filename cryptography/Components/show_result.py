from Components.header import header

def show_result(result):
        while True:
            header(result[3])
            print(f"Texte : {result[0]}")
            print(f"Clé : {result[1]}")
            print(f"Texte codé : {result[2]}")
            print(f"Methode : {result[3]}")
            answer = input("Voulez-vous stocker ces informations dans un fichier texte ? (y/n): ")
            print(answer)
            if answer in ["y", "Y", "yes", "Yes", "YES"]:
                return True
            elif answer in ["n", "N", "no", "No", "NO"]:
                return False
            else:
                print("⚠️ Repondez par 'y'(yes) ou 'n'(no)")