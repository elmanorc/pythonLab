A = int(input())
i = 1
numeros = [0]*(A+1)
X = int(input())
i = 0
while(i<X):
    numeros[int(input())] = 1
    i += 1
i = 1
count = 0
while(i<=A):
    if(numeros[i]==0):
        count += 1
    i += 1
print(count)