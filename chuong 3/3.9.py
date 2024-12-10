def thapluc(n):
    if n== 0:
        return "0"
    hexchar = "0123456789ABCDEF"
    hexd = ""
    while n > 0:
        a = n%16
        hexd = hexchar[a] + hexd
        n //=16
    return hexd
n = int(input())
print(thapluc(n))