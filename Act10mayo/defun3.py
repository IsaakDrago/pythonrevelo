import random

def genum(ant, sig):
    sigui=((ant // 10)+1)*10
    rango=min(sigui, sig)-(ant+1)
    if rango<=0:
        return ant+1
    else:
        return random.randrange(ant+ 1, min(sigui,sig))

def llenarL(n):
    lista=[]
    maximo=100 
    anterior=-1
    for i in range(n):
        numero=genum(anterior, maximo)
        lista.append(numero)
        anterior=numero
    return lista

n=int(input("Escribir un rango de maximo 100: "))
lista=llenarL(n)
print(lista)
