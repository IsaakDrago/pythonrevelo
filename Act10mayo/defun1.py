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

cont=0
num=int(input("Ingrese un numero: "))
while num not in l1:
        print(f"El numero {num} no esta en la lista")
        num=int(input("Ingrese un nuevo numero: "))
for i in range(len(l1)):
    if num==l1[i]:
        break
print(f"El numero {num} si esta en la lista")

for i in l1:
     if i==num:
         cont+=1
print(f"El numero se repite {cont} veces")

for i in range(len(l1)):
     if num == l1[i]:
        print(f'{l1[i]} esta en la posicion {i}')