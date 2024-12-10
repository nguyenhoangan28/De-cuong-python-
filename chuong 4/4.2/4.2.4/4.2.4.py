s = input().strip()
s = list(s)
for i in range(0,len(s)):
    print(s[i],end="")
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")
    