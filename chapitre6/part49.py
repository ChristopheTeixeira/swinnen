from math import *

print("Entrez un nombre")
nn = input()
nombre = int(nn)

if nombre >= 0:
    print(sqrt(nombre))
else:
    print("La racine de ce nombre ne peut être calculé.")
