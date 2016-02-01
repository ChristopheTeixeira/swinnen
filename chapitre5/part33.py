ch = "gaston"
new = ""
last = len(ch) - 1
n = 0

for i in ch:
    if n == last:
        new = new + i
        n = n + 1
    else:
        new = new + i + "*"
        n = n + 1
print(new)