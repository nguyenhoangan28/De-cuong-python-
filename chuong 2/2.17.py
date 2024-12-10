import math
x1, y1, x2, y2, x3, y3 = map(float, input().split())
a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
if a + b > c and b + c > a and c + a > b and a > 0 and b > 0 and c > 0:
    print("3 diem tren tao thanh mot tam giac")
else:
    print("3 diem tren khong tao thanh mot tam giac")