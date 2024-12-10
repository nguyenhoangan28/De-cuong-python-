
a1, b1, c1 = map(float,input().split())
a2, b2, c2 = map(float,input().split())

d = a1*b2 - b1*a2
dx = c1*b2 - b1*c2
dy = a1*c2 - c1*a2
if d == 0:
    if dx != 0 or dy != 0:
        print("VN")
    else:
        print("VSN")
else:
    x = dx/d
    y = dy/d
    print("x = {0:.2f}, y = {1:.2f}".format(x,y))
    