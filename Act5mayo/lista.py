import random
lista=[]
tam=random.randint(15,20)
cont=0
numero=0
num=0

print(tam)
for i in range(tam):
    num=random.randrange(0,9)
    lista.append(num)
print(lista)
num=int(input("Ingrese un numero de 0 a 9: "))
while num not in lista:
        print(f"El numero {num} no esta en la lista")
        num=int(input("Ingrese un nuevo numero: "))
for i in range(tam):
    if num==lista[i]:
        break
print(f"El numero {num} si esta en la lista")

for i in lista:
    if i==num:
        cont+=1
print(f"El numero se repite {cont} veces")

for i in range(len(lista)):
    if num == lista[i]:
        print(f'{lista[i]} esta en la posicion {i}')