# 11) Faça um programa que leia um número natural N e informe se ele
# é ou não um número PRIMO.
# PRIMOS: 2, 3, 5, 7, 11, 13, 17, 19, 23
# N: 24 (1, 2, 3, 4, 6, 8, 12, 24)

#1) INÍCIO (ENTRADA DOS DADOS E DECLARAÇÃO DE VARIÁVEIS)
N = int(input())
d = 2
ehPrimo = True

#2) PROCESSAMENTO
if N<2:
    ehPrimo = False
while d < N/2:
    if N % d == 0:
        ehPrimo = False
        break
    d += 1
#3) SAÍDA
if ehPrimo:
    print("É PRIMO.")
else:
    print("NÃO É PRIMO.")