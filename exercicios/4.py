# 4) Faça um programa que imprima os 50 primeiros números
# da sequência 1, 5, 9, 13, 17, …
i = 1 #qtde de números impressos na tela
n = 1
while i<=49:
    print(n, end=', ')
    i += 1
    n += 4
print(n, end=' ')