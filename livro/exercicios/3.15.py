#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, 
#calcule quantos dias de vida um fumante perderá.
#Exiba o total em dias.

#1) Entrada dos dados
quantidade_cigarros_dia = int(input("Quantos cigarros por dia? "))
quantos_anos = float(input("Quantos anos já fumou?"))
#2) Processamento
quantidade_total_cigarros = quantos_anos * 365 * quantidade_cigarros_dia
tempo_perdido_minutos = quantidade_total_cigarros * 10
tempo_perdido_dias = tempo_perdido_minutos / (24 * 60)
#3) Saída
print("Você já fumou %d cigarros e já perdeu %.2f dias de vida."
%(quantidade_total_cigarros, tempo_perdido_dias))