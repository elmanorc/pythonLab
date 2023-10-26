x = int(input())
i = 2
c = True
d = 1
while i <= x/2:
  if x % i == 0:
    c = False
    d = i
    break
  i+=1
if(c):
  print(x)
else:
  print(d)
