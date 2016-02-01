t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]
t3 = []
n = 0
while n < 12:
    t3.append(t2[n])
    t3.append(t1[n])
    n = n + 1
print(t3)