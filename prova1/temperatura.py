unidade=input()
convert=input()
graus=float(input())

if unidade == 'c' or unidade=='C':
    if convert=='f' or convert=='F':
        print(f'{(graus*9/5)+32:.3f}')
    else:
        print('Conversão inválida')
elif unidade == 'f' or unidade=='F':
    if convert=='c' or convert=='C':
        print(f'{(graus-32)*(5/9):.3f}')
    else:
        print('Conversão inválida')
else:
    print('Unidade inválida')