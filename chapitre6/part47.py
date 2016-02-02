print("Quel est votre nom?")
nom = input()
print("De quel sexe êtes vous? (Entrez M ou F)")
sexe = input()

sortie = False

while sortie is False :
    if sexe == "M":
        print("Cher Monsieur",nom,)
        sortie = True
    elif sexe == "F":
        print("Chère Mademoiselle",nom,)
        sortie = True
    else:
        print("Veuillez entrer M ou F")
        sexe = input()