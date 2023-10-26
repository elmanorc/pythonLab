#Progressão PA, PG

N = int(input())
a = int(input())
b = int(input())
kPA = b - a
kPG = b/a
ehPA = True
ehPG = True
i = 3
while i<=N:
    c = int(input())
    if (kPA != c-b):
        ehPA = False
    else:
        kPA = c-b
    if (kPG != c/b):
        ehPG = False
    else:
        kPG = c/b
    if not ehPA and not ehPG:
        break
    b = c
    i += 1
if not ehPA and not ehPG:
    print("NENHUMA")
elif not ehPG:
    print(f"PA {kPA}")
else:
    print("PG %2.3f" %kPG)
