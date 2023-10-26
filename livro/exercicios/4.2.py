#Escreva um programa que pergunte a velocidade do carro de um 
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário 
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 
#80 km/h.

#1) ENTRADA
velocidade = float(input("Qual a velocidade do carro?"))
#2) PROCESSAMENTO
foiMultado = False
multa = 0
if(velocidade > 80):
    foiMultado = True
    multa = (velocidade - 80) * 5
#3) SAÍDA
if(foiMultado):
    print("Você foi multado. Valor a pagar: R$ %.2f." %multa)