L = int(input())
K = int(input())
l = L
k = K
total_quadrados = 0
while l>0 and k>0:
    total_quadrados += l*k
    l -= 1
    k -= 1
print(total_quadrados)