A = int(input())
B = int(input())
a = 1
x = 0
while(a<=A):
    b = B
    while(b>=1):
        x += A*B
        b -= 1
    a += 1
print(x)

