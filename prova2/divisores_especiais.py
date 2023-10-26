N = int(input())
L = int(input())
i = 1
q = 0
while i<=N:
    if N % i == 0 and i >= L:
        q += 1
    i += 1
print(q)