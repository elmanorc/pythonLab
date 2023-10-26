#15) Faça um programa que leia dois números inteiros, A e B, 
# e calcule o valor de A^B sem utilizar o operador **.
A = int(input())
B = int(input())
b = 1
res = 1
while b<=B:
    res *= A
    b += 1
print(res)

# 3^4 = 3*3*3*3 = 81
# A^B = A*A*A...*A (B vezes)

