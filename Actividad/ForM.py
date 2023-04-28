n=int(input("Ingrese el numero con el que terminara: "))
c=int(input("Ingrese el numero de cuanto crecera o decrecera, este ultimo en negativo: "))
m=int(input("Ingrese el numero para multiplo: "))
for s in range(0,n,c):
    if s%m==0:
        print(f"Un multiplo de {m} es {s}")