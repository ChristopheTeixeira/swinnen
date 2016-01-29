a=0
while a < 199:
    a=a+1
    if a % 3 == 0 and a % 5 == 0:
        print("BipMeuh")
    elif a % 3 == 0:
        print("Bip")
    elif a % 5 == 0:
        print("Meuh")
    else:
        print(a)