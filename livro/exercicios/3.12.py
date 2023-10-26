#Escreva um programa que calcule o tempo de uma viagem de carro. 
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distância = float(input("Qual a distância em km: "))
velocidade_média = float(input("Qual a velocidade média em km/h: "))
tempo = distância / velocidade_média
print("O tempo de viagem será de %f horas", tempo)