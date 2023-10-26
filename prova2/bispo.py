x1,y1,x2,y2 = map(int,input().split())
dX = abs(x2-x1)
dY = abs(y2-y1)
if x2==x1 and y2==y1:
    print("0")
elif dX == dY:
    print("1")
elif (x1+y1) % 2 == (x2+y2) % 2:
    print("2")
else:
    print("-1")