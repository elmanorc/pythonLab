distancia = float(input("Qual a distância em km? "))
preco = 0
if(distancia <= 200):
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f"O preço da passagem é de R${preco}")

