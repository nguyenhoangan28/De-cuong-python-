
a = float(input())
def gt(n):
    if n ==0:
        return 1
    else:
        s = 1
        for i in range(1, n+1):
            s *= i
        return s
if not (0 < a < 0.01):
    print("nhap lai")
else:
    n = 0
    s = 0
    x = 1/gt((2*n+1))
    while x >= a:
        s += x
        n +=1
        x = 1/gt((2*n+1))
    print(s)