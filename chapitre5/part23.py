argent = 100
année = 0
while année < 20:
    année = année + 1
    interets = argent * 1.043 - argent
    argent = argent * 1.043
    print(année,":",interets)
