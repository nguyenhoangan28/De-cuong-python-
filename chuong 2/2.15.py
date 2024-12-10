x = float(input())
ep = float(input())
def gt(n):
    if n ==0:
        return 1
    else:
        s = 1
        for i in range(1, n+1):
            s *= i
        return s
if not (0 < ep < 1):
    print("nhap lai")
else:
    n = 0
    s = 0
    a = x**n/gt(n)
    while abs(a) >= ep:
        s += a
        n += 1
        a = x**n/gt(n)
    print("{0:.2f}".format(s))