# Faça um programa que solicite o preço de uma mercadoria e o percentual
# de desconto. 
preco = float(input("Qual o preço da mercadoria? "))
p_desconto = float(input("Qual o percentual de desconto? "))
#Exiba o valor do desconto e o preço a pagar.
desconto = preco * (p_desconto / 100)
precoFinal = preco - desconto
#print("Desconto / Preço final", desconto, precoFinal)
print("Desconto de R$ %4.2f. Preço final: R$%6.2f" %(desconto, precoFinal) )