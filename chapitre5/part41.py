noms = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
nomcr = []
nomln = []
n = 0

while n < len(noms):
    if len(noms[n]) < 6:
        nomcr.append(noms[n])
    else:
        nomln.append(noms[n])
    n = n + 1

print(nomcr)
print(nomln)
