a = 0
b = 32
i = 0
n = 0

while i in range(a,b):
    if i % 3 == 0 or i % 5 == 0:
        n = n + i
    i = i + 1
print(n)