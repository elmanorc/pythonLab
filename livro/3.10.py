salario = float(input("Salário atual: "))
aumento = float(input("Porcentagem de aumento: "))
valorAumento = salario*aumento/100
novoSalario = salario + valorAumento
print("Valor do aumento: %5.2f" %valorAumento)
print("Novo salário: %7.2f" %novoSalario)
