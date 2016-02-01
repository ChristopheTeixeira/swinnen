ch = "laval"
new = ""
last = len(ch) - 1
n = last

for i in ch:
    new = new + ch[n]
    n = n - 1
if ch == new:
    print(ch,"est un palindrome")
else:
    print(ch,"n'est pas un palindrome")
