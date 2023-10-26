#Maior par - menor ímpar (números naturais < 1000)
maiorPar = -2
menorImpar = 1001
i = 1
while i<=10:
    n = int(input())
    if n % 2 == 0 and n > maiorPar:
        maiorPar = n
    elif n % 2 == 1 and n < menorImpar:
        menorImpar = n
    i += 1
print(maiorPar-menorImpar)