ch = "zorglub"
new = ""
last = len(ch) - 1
n = last

for i in ch:
    new = new + ch[n]
    n = n - 1
print(new)