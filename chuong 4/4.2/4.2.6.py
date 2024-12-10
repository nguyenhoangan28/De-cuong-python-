s = input()
s = list(s)
a = []
b = []
for i in range(len(s)):
    d = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            d += 1 
    a.append("{0}: {1}".format(s[i], d))
for i in a:
    if i not in b:
        b.append(i)
print(", ".join(b))
            