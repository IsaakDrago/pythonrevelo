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
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista
    
def ordendes(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista
    
# def modaL(lista):
#       moda=0
#       for i in lista:
#          if len(lista)==i:
#              moda=i 
#       return lista
def modaL(lista):
    frecuencias = {}
    moda = None
    max_frecuencia = 0

    for i in lista:
        frecuencias[i] = frecuencias.get(i, 0) + 1
        if frecuencias[i] > max_frecuencia:
            moda = i
            max_frecuencia = frecuencias[i]

    return moda

def medL(lista):
    m=(len(lista))
    if m%2==0:
        mediana=(lista[m//2-1]+lista[m//2])/2
    else:
        mediana=lista[m//2]
    return mediana
    
l1=llenarL(5,20)
print(l1)
print(sumaL(l1))
print(promedioL(l1))
print(mayorL(l1))
print(menorL(l1))
print(ordenasc(l1))
print(ordendes(l1))
print(modaL(l1))
print(medL(l1))