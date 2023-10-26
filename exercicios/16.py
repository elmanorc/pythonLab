#16) Faça um programa que leia três números inteiros, 
# A, B e n, e calcule o valor de (AB)^n sem utilizar 
# o operador **.
# (2*3)^3 = 216
A = int(input())
B = int(input())
n = int(input())
i = 1
AB = A*B
ABn = 1
while i<=n:
    ABn *= A*B
    i += 1
print(ABn)