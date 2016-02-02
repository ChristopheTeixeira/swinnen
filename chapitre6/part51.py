print("Entrez une année.")
nn=input()
an = int(nn)

bissextile = False

if an % 400 == 0:
    bissextile = True
if an % 4 == 0:
    if an % 100 == 0:
        bissextile = False
    else:
        bissextile = True

if bissextile == True:
    print(an, "est une année bissextile.")
else:
    print(an,"n'est pas une année bissextile")