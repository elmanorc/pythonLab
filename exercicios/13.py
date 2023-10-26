# 13) Faça um programa que leia dez números inteiros calcule a média entre eles.
# SEM USAR LISTA!
numero = 0
i = 1
soma = 0
N = 10
while i<=N:
    numero = int(input())
    soma += numero
    i += 1
media = soma / N
print(f"{media}")