p1, p2, p3 = map(int, input().split())
t1, t2, t3 = map(int, input().split())
penalidade = int(input())
acertos = 0
if(t1>0):
  acertos += 1
if(t2>0):
  acertos += 1
if(t3>0):
  acertos += 1
print(acertos)
multa = 0
if (p1>0):
  multa += p1-1
if (p2>0):
  multa += p2-1
if (p3>0):
  multa += p3-1
tempo = t1+t2+t3+penalidade*multa
print(tempo)
