hora = int(input())
minutos = int(input())

hora = hora % 12
anguloHora = hora*30 + minutos*0.5
anguloMinutos = minutos*6

angulo = anguloHora - anguloMinutos;
if(angulo<0):
    angulo *= -1

if(angulo>180):
    angulo = 360 - angulo
print(angulo)
