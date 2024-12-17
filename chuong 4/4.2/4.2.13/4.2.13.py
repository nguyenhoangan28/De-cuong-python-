t = int(input())

b = []
for i in range(t):
    a = []
    s = input().strip()
    s = list(s)
    d = 1
    for j in range(1, len(s)):
        if s[j-1] == s[j]:
            d += 1
        else:
            a.append(f"{s[j-1]}{d}")
            d = 1
    a.append(f"{s[-1]}{d}")
    b.append("".join(a))
for i in b:
    print(i)

            