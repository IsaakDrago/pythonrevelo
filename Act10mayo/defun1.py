import random

def llenarL(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumaL(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioL(lista):
    return sumaL(lista)/len(lista)

def mayorL(lista):
    mayor=0
    for x in lista:
        if x>mayor:
            mayor=x
    return mayor
        

def menorL(lista):
    menor=100000
    for x in lista:
        if x<menor:
            menor=x
    return menor

def ordenasc(lista):
    aux=0
    for i in range():
        for j in range(i+1,tam):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista[aux]
    
    
l1=llenarL(5,20)
print(l1)
print(sumaL(l1))
print(promedioL(l1))
print(mayorL(l1))
print(menorL(l1))
print(ordenasc(l1))