import re
s = input()
x = re.findall(r"\d+",s)
a = list(map(int ,x))
print(sum(a))