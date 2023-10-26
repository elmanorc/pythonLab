#5) Faça um programa que imprima os 20 primeiros números
# da sequência 1, 2, 4, 8, 16, 32, …
exp = 0
while exp<19:
    print(2**exp, end=', ')
    exp += 1
print(2**exp, end=' ')
