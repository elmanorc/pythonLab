s = input()
i = 0
v = 0
c = 0
while i<len(s):
    if s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U":
        v += 1
    elif s[i] != " ":
        c += 1
    i += 1
if v>c:
    print("V")
elif v==c:
    print("=")
else:
    print("C")