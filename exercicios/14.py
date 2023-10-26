# 14) Faça um programa que leia dois números inteiros e calcule
# o produto desses números sem utilizar o operador * ou /
A = int(input())
B = int(input())
i = 1
prod = 0
while i<=B:
    prod += A
    i += 1
print(prod)