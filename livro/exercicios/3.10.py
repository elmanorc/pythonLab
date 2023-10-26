# 1) Solicitar o valor do salário e do percentual de aumento
salario = float(input("Informe o salário: "))
percent_aumento = float(input("Informe o percentual de aumento: "))
# 2) Calcular o valor do aumento e do novo salário
aumento = salario * percent_aumento/100
salario += aumento 
# 3) Mostrar o valor do aumento e do novo salário
print("Aumento de R$ %5.2f. Novo salário é R$ %6.2f. " %(aumento, salario))
