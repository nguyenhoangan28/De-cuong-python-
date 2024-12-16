s = input()
so = []
for i in s.split(","):
    so.append(int(i.strip()))
for i in so:
    if i%2!=0:
        print(i, end=" ")
    