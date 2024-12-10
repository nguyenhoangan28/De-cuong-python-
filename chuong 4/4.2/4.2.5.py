s = input()
s = list(s)
hoa = 0
thuong = 0
so = 0
for i in range(len(s)):
    if s[i] >= "A" and s[i] <= "Z":
        hoa += 1 
    if s[i] >= "a" and s[i] <= "z":
        thuong += 1 
    if s[i] >= "0" and s[i] <= "0":
        so += 1 
print("hoa: {0}\nthuong: {1}\nso: {2}".format(hoa, thuong,so))