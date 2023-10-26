#1) Entrada dos dados
x = float(input("Primeiro número: "))
y = float(input("Segundo número: "))
op = input("Qual operação? +, -, x, / : ")

#2) Processamento
resultado = 0
if op == '+':
    resultado = x+y
elif op == '-':
    resultado = x-y
elif op == 'x':
    resultado = x*y
elif op == '/':
    resultado = x/y
else:
    print("Operação inválida!")
    resultado = 0
#3)Saída
print(f"Resultado = {resultado}")
