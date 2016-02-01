nb = [32, 5, 12, 8, 3, 75, 2, 15]
n=0
tot=0

while n < len(nb)-1:
    if nb[n] > tot:
        tot = nb[n]
        print(tot)

    n = n + 1

print("le plus grand élément de cette liste est", tot, ".")
