# Faça um programa que imprima a sequência dos 20 primeiros 
# números da sequência de Fibonacci
#    a  b  
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
a = 0
b = 1
print(a, end=', ')
print(b, end=', ')
count = 2
while count<20:
    count += 1
    c = a + b
    a = b
    b = c
    print(c, end=', ')
