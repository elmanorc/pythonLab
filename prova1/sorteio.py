p1 = input()
p2 = input()
n1 = int(input())
n2 = int(input())
sorteio = int(input())
d1 = sorteio-n1
if(d1<0):
    d1 *= -1
d2 = sorteio-n2
if(d2<0):
    d2 *= -1
if(d1<d2):
    print(p1)
elif(d1>d2):
    print(p2)
else:
    print(p1)
    print(p2)