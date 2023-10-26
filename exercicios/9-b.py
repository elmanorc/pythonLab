# Faça um programa que imprima a sequência dos 20 primeiros 
# números da sequência de Fibonacci
# a  b  b
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
a = 0
b = 1
print('0, 1, ', end='')
count = 2
while count<20:
    count += 1
    b = a + b
    a = b - a
    print(b, end=', ')