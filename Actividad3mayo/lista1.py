import random
lista=[]
tam=random.randint(10,20)
suma=0
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print (lista)

for i in range(len(lista)):
    suma+=lista[i]
    total=suma
    prom=total//len(lista)
print(f"La suma total de los numeros es {total}")
print(f"El promedio es {prom}")

mayor=0
menor=1000000

for i in lista:
    if i > mayor:
        mayor=i
    if i < menor:
        menor=i
print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")


moda=0

for i in lista:
    if lista[i]==lista[i+1]:
        moda
print(f"La moda es {moda}")