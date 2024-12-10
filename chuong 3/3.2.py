def ngto(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        return True
n = int(input())
for i in range(n+1):
    if ngto(i):
        print(i, end=" ")