def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b
n = int(input())
s = 0
for i in range(1, n+1):
    s += fibo(i)
    print(fibo(i), end=" ")
print()
print(s)