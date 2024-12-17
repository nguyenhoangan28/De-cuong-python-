import re

S = input().strip()

n = re.findall(r'\d+', S)

for i in range(len(n)):
    n[i] = str(int(n[i]))
n.sort(key=int)

a = []
j = 0 

i = 0
while i < len(S):
    if S[i].isdigit():
        a.append(n[j])
        j += 1
        while i < len(S) and S[i].isdigit():
            i += 1
    else:
        a.append(S[i])
        i += 1

print(''.join(a))
