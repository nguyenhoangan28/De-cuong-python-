s = input()
x = input()
s = list(s)
d = 0
for i in range(len(s)):
    if s[i] == x:
        d += 1
print("{0}: {1}".format(x,d))