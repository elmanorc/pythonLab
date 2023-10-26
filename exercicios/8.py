# 8) Faça um programa que calcule a soma da sequência abaixo:
# 2/3 + 4/9 + 8/27 + 16/81 + ... 1024/? = soma
num = 2
den = 3
soma = 0
while num < 1024:
    print(f"{num}/{den} + ",end='')
    soma += num/den
    num *= 2
    den *= 3
print(f"{num}/{den} = ",end='')
soma += num/den
print(soma)
