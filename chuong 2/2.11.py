n = int(input())
def gt(n):
    if n ==0:
        return 1
    else:
        s = 1
        for i in range(1, n+1):
            s *= i
        return s
s = 0
for i in range(1, n+1):
    s += gt(i)
print(s)