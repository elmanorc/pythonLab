#10) Faça um programa que leia um número natural N e 
# imprima a lista de todos os seus divisores.
n = int(input("Digite um número positivo: "))
i = 1
while i<=n/2:
    if(n % i == 0):
        print(i)
    i += 1
print(n)