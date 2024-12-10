import math
a, b, c = map(float,input().split())
if a == 0:
    if b == 0:
        if c == 0:
            print("VSN")
        else:
            print("VN")
    else:
        x = -c/b 
        print("x = {0:.2f}".format(x))
else:
    denta = b**2 - 4*a*c 
    if denta < 0:
        print("VN")
    elif denta == 0:
        x = -b/(2*a)
        print("pt co nghiem kep: x1 = x2 = {0:.2f}".format(x))
    else:
        x1 = (-b - math.sqrt(denta))/(2*a)
        x2 = (-b + math.sqrt(denta))/(2*a)
        print("x1 = {0:.2f}, x2 = {1:.2f}".format(x1,x2))

