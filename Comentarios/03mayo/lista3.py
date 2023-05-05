import random #Se importa la funcion "Random" para generar numeros aleatorios
lista=[]
cuadrado=[]
tam=random.randint(5,10)#Con "randint" se asigna el tamaño que va a tener la lista de forma aleatoria
print(tam)
for i in range(tam):
    num=random.randrange(100)#Con "ranrange" se asigna el rango de los numeros que se van a generar
    lista.append(num)#Se van añadiendo a la lista los numeros que se van generando
print(lista)

for i in range(len(lista)):
    cuadrado.append(lista[i]**2) #Se asigna que a la variable se le vaya añadiendo el cuadrado de los numeros generados
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)#Se imprimen los resultados
print(sum(lista))