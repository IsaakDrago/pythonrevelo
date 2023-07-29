i=int(input("Ingrese el numero con el que iniciara: "))
f=int(input("Ingrese el numero con el que terminara: "))
c=int(input("Ingrese el numero de cuanto crecera o decrecera, este ultimo en negativo: "))
f=f+1
for s in range(i,f,c):
    print(s)