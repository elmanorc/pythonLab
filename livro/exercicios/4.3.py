#Ler três números inteiros e mostrar o maior e menor
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
menor = a
maior = a
if(b > maior):
    maior = b
elif(b < menor):
    menor = b
if(c > maior):
    maior = c
elif(c < menor):
    menor = c
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")