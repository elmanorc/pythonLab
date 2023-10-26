# 7) Faça um programa que imprima a sequência abaixo:
# 1/3 + 2/5 + 3/7 + 4/9 + ... + ?/99
num = 1
den = 3
while den!=99:
    print(f"{num}/{den} + ", end='')
    num += 1
    den += 2
print(f"{num}/{den}", end='')
