def tongchuso(n):
    a = 0
    n = abs(n)
    while n > 0:
        a += n%10
        n //= 10
    return a 
n = int(input())
print(tongchuso(n))