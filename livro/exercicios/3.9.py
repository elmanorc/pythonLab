dias = int(input("Digite a qtde de dias: "))
horas = int(input("Digite a qtde de horas: "))
minutos = int(input("Digite a qtde de minutos: "))
segundos = int(input("Digite a qtde de segundos: "))
#total_segundos = segundos + 60*minutos + 60*60*horas + 24*60*60*dias
#total_segundos = segundos + 60*(minutos + 60*horas + 24*60*dias)
total_segundos = segundos + 60*(minutos + 60*(horas + 24*dias))
print(total_segundos)