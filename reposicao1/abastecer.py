porcentagem = float(input())
capacidade = float(input())
consumo = float(input())
distancia = float(input())
volumeAtual = capacidade * porcentagem/100
autonomia = consumo * volumeAtual

reserva = consumo*2

if(distancia+reserva > autonomia):
    print("VA PRO POSTO")
else:
    distanciaSobra = autonomia - distancia
    print("%.1f" %(100*distanciaSobra/capacidade))