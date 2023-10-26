l = int(input())
c = int(input())
#posicoes possiveis = 8
total = 0
if( l+2 < 9 and c+1 < 9):
    total += 1
if( c-1 > 0 and l+2 < 9):
    total += 1
if( l+1 < 9 and c+2 < 9):
    total += 1
if( c-2 > 0 and l+1 < 9):
    total += 1
if( l-1 > 0 and c+2 < 9):
    total += 1
if( l-1 > 0 and c-2 > 0):
    total += 1
if( l-2 > 0 and c+1 < 9):
    total += 1
if( l-2 > 0 and c-1 > 0):
    total += 1
print(total)