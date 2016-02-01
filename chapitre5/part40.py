nb = [32, 5, 12, 8, 3, 75, 2, 15]
nb1 = []
nb2 = []
n = 0

while n < len(nb):
    if nb[n] % 2 == 0:
        nb1.append(nb[n])
    else:
        nb2.append(nb[n])
    n = n + 1
print(nb1)
print(nb2)
