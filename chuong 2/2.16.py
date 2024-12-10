import math
a, b, c = map(int, input().split())
if a + b > c and b + c > a and c + a > b and a > 0 and b > 0 and c > 0:
    print("3 canh tren tao thanh mot tam giac")
    chuvi = a + b +c
    p = (a + b + c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("chu vi: {0}, dien tich: {1:.2f}".format(chuvi, s))
else:
    print("3 canh tren khong tao thanh mot tam giac")