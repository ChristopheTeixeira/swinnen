a, b = 0, 0
while(b<20):
    b = b + 1
    a = b * 7
    if a % 3 == 0:
        print(a, "*")
    else:
        print(a)
