# tamaño lista (por pueblo): minimo 200 maximo 2500.{validación}
# Llenar Icfes {Resultados. 100 - 500}
# Hallar valor de cada cuartil
# Hallar valor de cada quintil
# Promedio por cada cuartil
# Promedio por cada quintil
# Mayor y menor por separado de cada cuartil y quintil respectivamente
# Generar listas separadas por cuartil y quintil

import random

def llenarL(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
l1=llenarL(200,500)
def ordenasc(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista
print(ordenasc(l1))

#CUARTILES
def cuartil(lista):
    orde=ordenasc(lista)
    n=len(orde)
    c1=int(n*0.25)
    c2=int(n*0.5)
    c3=int(n*0.75)
    q1=orde[c1]
    q2=orde[c2]
    q3=orde[c3]
    return q1,q2,q3
cuartil1, cuartil2, cuartil3 = cuartil(l1)
print("Q1:", cuartil1)
print("Q2:", cuartil2)
print("Q3:", cuartil3)

#QUINTILES
# def quintil(lista):
#     orde=ordenasc(lista)
#     n=len(orde)
#     c1=int(n*0.2)
#     c2=int(n*0.4)
#     c3=int(n*0.6)
#     c4=int(n*0.8)
#     k1=orde[c1]
#     k2=orde[c2]
#     k3=orde[c3]
#     k4=orde[c4]
#     return k1,k2,k3,k4
# quintil1, quintil2, quintil3, quintil4 = quintil(l1)
# print("K1:", quintil1)
# print("K2:", quintil2)
# print("K3:", quintil3)
# print("K4:", quintil4)