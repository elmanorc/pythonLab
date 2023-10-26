# 17) Faça um programa que leia dez números inteiros 
# e calcule a diferença entre o maior e o menor.
# SEM USAR LISTA!

menor = int(input())
maior = menor
i = 1
while i<=9:
    proximo = int(input())
    if proximo > maior:
        maior = proximo
    elif proximo < menor:
        menor = proximo
    i += 1
print(maior-menor)