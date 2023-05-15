# Llenar dos arreglos de n elementos con números generados con la función random.
# Compararlos y decir:
# a. Cuál de los dos tiene la suma más alta
# b. Cuál de los dos tiene el número mayor
# c. Cuál de los dos tiene el número menor
# d. Cuál es el promedio conjunto (uniendo los dos arreglos)
# e. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo
# conjunto
# f. Cuál de los dos tiene mayor cantidad de pares
# g. Cuál de los dos tiene mayor cantidad de impares

import random

def llenarL(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarL(5,30)
l2=llenarL(5,30)

def sumamay(lista):
    suma=0
    for i in lista:
        suma+=i
        total=suma
    return total

def complist(l1,l2):
    totalgen=0
    if sumamay(l1)<sumamay(l2):
        totalgen=sumamay(l2)
    else:
        sumamay(l1)>sumamay(l2)
        totalgen=sumamay(l1)
    return totalgen
    
def mayorL(l1,l2):
    mayor1,mayor2,mgen=0,0,0
    
    for x in l1:
        if x>mayor1:
            mayor1=x
    for i in l2:
        if i>mayor2:
            mayor2=i
    if mayor1>mayor2:
        mgen=mayor1
    elif mayor1==mayor2:
        mgen=mayor1
    else:
        mayor1<mayor2
        mgen=mayor2
    return mgen
        
def menorL(l1,l2):
    menor1,menor2,mengen=1000,1000,0
    for x in l1:
        if x<menor1:
            menor1=x
    for i in l2:
        if i<menor2:
            menor2=i
    if menor1>menor2:
        mengen=menor2
    elif menor1==menor2:
        mengen=menor1
    else:
        menor1<menor2
        mengen=menor1
    return mengen

def prom(l1,l2):
    for i in lista:
        prom=0
        promli1=total1//tam

print(l1)
print(l2)
print(sumamay(l1))
print(sumamay(l2))
print(complist(l1,l2))
print(mayorL(l1,l2))
print(menorL(l1,l2))