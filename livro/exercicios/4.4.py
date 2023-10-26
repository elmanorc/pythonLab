salario = float(input("Informe o salário: "))
aumento = 0
if(salario > 1250):
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f"O aumento será de R$ {aumento}")

