import random
lista1,lista2=[],[]
tam=random.randint(10,20)
tam2=random.randint(10,20)
num=0
suma1,suma2,sumprom=0,0,0
mayor1,mayor2=0,0
menor1,menor2=0,0
promc,promli1,promli2=0,0,0
par1,par2,impar1,impar2=0,0,0,0
for i in range(tam):
    num=random.randrange(0,20)
    lista1.append(num)
print(f"lista 1 {lista1}")
for j in range(tam2):
    num=random.randrange(0,20)
    lista2.append(num)
print(f"lista 2 {lista2}")

for i in range(tam):
    suma1+=lista1[i]
    total1=suma1

for j in range(tam2):
    suma2+=lista2[j]
    total2=suma2

#SUMA MAS ALTA
if total1>total2:
    print(f"La lista 1 tiene la suma mas alta siendo de {total1}")
else:
    print(f"La lista 2 tiene la suma mas alta siendo de {total2}")

#NUMERO MAYOR
for i in lista1:
    if i>mayor1:
        mayor1=i

for j in lista2:
    if j>mayor2:
        mayor2=j

if mayor1>mayor2:
    print(f"El numero mayor entre las 2 listas es {mayor1} de la lista 1")
elif mayor1==mayor2:
    print(f"El numero mayor entre ambas listas es igual y es {mayor1}")
else:
    print(f"El numero mayor entre las 2 listas es {mayor2} de la lista 2")

#PROMEDIO
for i in range(tam):
    promli1=total1//tam

for i in range(tam2):
    promli2=total2//tam2

sumprom=promli1+promli2
promc=sumprom//2
print(f"El promedio en conjunto es de {promc}")

if promli1>promc:
    print(f"El promedio de la lista 1 esta por encima del promedio en conjunto al ser de {promli1}")
elif promli1==promc:
    print(f"El promedio de la lista 1 es igual al promedio en conjunto siendo de {promli1}")
else:
    print(f"El promedio de la lista 1 esta por debajo del promedio en conjunto al ser de {promli1}")

if promli2>promc:
    print(f"El promedio de la lista 2 esta por encima del promedio en conjunto al ser de {promli2}")
elif promli2==promc:
    print(f"El promedio de la lista 2 es igual al promedio en conjunto siendo de {promli2}")
else:
    print(f"El promedio de la lista 2 esta por debajo del promedio en conjunto al ser de {promli2}")

#PARES E IMPARES

for i in lista1:
    if i%2==0:
        par1+=1
    else:
        impar1+=1
#print(f"La cantidad de pares en la lista 1 es de {par1}")
#print(f"La cantidad de impares en las lista 1 es de {impar1}")

for j in lista2:
    if j%2==0:
        par2+=1
    else:
        impar2+=1
#print(f"La cantidad de pares en la lista 2 es de {par2}")
#print(f"La cantidad de impares en la lista 2 es de {impar2}")

if par1>par2:
    print(f"La lista 1 tiene mas pares con {par1}")
elif par1==par2:
    print(f"Ambas listas tienen la misma cantidad de pares con {par1}")
else:
    print(f"La lista 2 tiene mas pares con {par2}")

if impar1>impar2:
    print(f"La lista 1 tiene mas impares con {impar1}")
elif par1==par2:
    print(f"Ambas listas tienen la misma cantidad de impares con {impar1}")
else:
    print(f"La lista 2 tiene mas impares con {impar2}")