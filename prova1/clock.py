a,b=input().split()
a,b=int(a),int(b)
x=a*60/12
r=x-(x-b)
u=5*r/60
rf=(r-u)*6
if rf>180:
    print(360-rf)
else:
    print(rf)
