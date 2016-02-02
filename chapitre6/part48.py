print("Entrez la longueur du coté A.")
nn = input()
print("Entrez la longueur du coté B.")
mm = input()
print("Entrez la longueur du coté C.")
pp=input()

a = int(nn)
b = int(mm)
c = int(pp)
maxi = 0
sec1 = 0
sec2 = 0

if a >= b and a >= c:
    maxi = a
    sec1 = b
    sec2 = c
elif b >= a and b >= c:
    maxi = b
    sec1 = a
    sec2 = c
else:
    maxi = c
    sec1 = a
    sec2 = b

equilateral = False
rectangle = False
isocele = False
triangle = True

if maxi > sec1 + sec2:
    triangle = False

if maxi == sec1 == sec2:
    equilateral = True

if maxi**2 == sec1**2 + sec2**2:
    rectangle = True

if maxi == sec1:
    isocele = True
elif maxi == sec2:
    isocele = True
elif sec1 == sec2:
    isocele = True

if triangle == False:
    print("Il n'est pas possible de construire un triangle avec ces longueurs")
elif equilateral == True:
    print("Ce triangle est équilatéral.")
elif rectangle == True and isocele == True:
    print("Ce triangle est isocèle rectangle.")
elif rectangle == True:
    print("Ce triangle est rectangle.")
elif isocele == True:
    print("Ce triangle est isocèle.")
else:
    print("Ce triangle est quelconque.")
