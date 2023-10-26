dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))
segundos = segundos + minutos*60 + horas*60*60 + dias*24*60*60
#segundos = segundos + 60*(minutos + horas*60 + dias*24*60)
#segundos = segundos + 60*(minutos + 60*(horas + dias*24))

print(segundos)