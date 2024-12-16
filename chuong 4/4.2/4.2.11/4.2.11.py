import re
s = input()
x = re.findall(r"\d+",s)
a = list(map(int ,x))
print(max(a))