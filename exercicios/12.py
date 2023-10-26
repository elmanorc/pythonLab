# 12) Faça um programa que leia um número natutal N e informe 
# se ele é um número perfeito. Número perfeito é aquele que 
# é igual a soma de todos os seus divisores naturais menores que ele.
# Exemplo: 6 = 1 + 2 + 3. 28 = 1 + 2 + 4 + 7 + 14
N = int(input("Digite um número: "))
d = 1
soma = 0
while d <= N/2:
    if N % d == 0:
        soma += d
    d += 1
if N == soma:
    print(f"{N} é perfeito.")
else:
    print(f"{N} não é perfeito.")

