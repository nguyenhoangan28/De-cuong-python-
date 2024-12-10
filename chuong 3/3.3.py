def hh(n):
    s = 0
    if n <= 1:
        return False
    else:
        for i in range(1,n):
            if n % i == 0:
                s += i
        if s == n:
            return True
        else:
            return False
a, b = map(int, input().split())
for i in range(a, b+1):
    if hh(i):
        print(i, end=" ")