print("Entrez une note.")
nn = input()
print("Entrez la note maximale à attribuer.")
pp = input()

note = int(nn)
lim = int(pp)
ratio = note/lim

if ratio == 1:
    print("SS")
elif 1 > ratio >= 0.95:
    print("S")
elif 0.95 > ratio >= 0.80:
    print("A")
elif 0.80 > ratio >= 0.60:
    print("B")
elif 0.60 > ratio >= 0.50:
    print("C")
elif 0.50 > ratio >= 0.40:
    print("D")
elif 0.40 > ratio >= 0.20:
    print("E")
elif ratio < 0.20:
    print("F")
else:
    print("Entrée non valide")
