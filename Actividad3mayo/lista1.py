import random
lista=[]
tam=random.randint(10,20)
suma=0
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print (lista)

#PROMEDIO
for i in range(len(lista)):
    suma+=lista[i]
    total=suma
    prom=total//len(lista)
print(f"La suma total de los numeros es {total}")
print(f"El promedio es {prom}")

#MAYOR Y MENOR
mayor=0
menor=1000000

for i in lista:
    if i > mayor:
        mayor=i
    if i < menor:
        menor=i
print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")

#MODA
moda=0
for i in lista:
    if tam==i:
        moda=i 
print(f"La moda es {moda}")

#MEDIANA
lista.sort()
print(lista)
m=(len(lista))
if m%2==0:
    mediana=(lista[m//2-1]+lista[m//2])/2
else:
    mediana=lista[m//2]
print (f"La mediana es {mediana}")

#DESVIACION ESTANDAR
for i in lista:
    resta=i-prom
    cuadrado=resta**2
    division=cuadrado//suma
    print(division)