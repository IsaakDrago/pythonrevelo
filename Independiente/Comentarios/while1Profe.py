# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1 #Se define variable y se le asigna valor
cont=0
sum=0
menor=1000000
mayor=0
while num!=0: #Se define un while "num" que evalua que "num" sea diferente de 0
    num=int(input('ingrese numero')) #Se pide el ingreso de un numero para asignarlo a la variable "num"
    cont=cont+1 #Se asigna que al contador se le sume de 1 cada vez que pase por el ciclo
    sum=sum+num #Se asigna que a "sum" se le sume lo que vaya en la variable "num"
    if num>mayor: #Con if se evalua que "num" sea mayor que "mayor"
        mayor=num #Se le asigna a "mayor" lo que vaya en la variable "num"
    if num<menor and num!=0: #Si "num" es menor que "menor" y es diferente de 0
        menor=num #Se le asigna a "menor"

print(f'fueron ingresados {cont-1} numeros') #Mostrara en pantalla la cantidad de datos ingresados
print(f'La suma es {sum}') #Mostrara en pantalla la suma de los numeros ingresados
print(f'El promedio es {sum/(cont-1)}')
print(f'El mayor es {mayor}')
print(f'El menor es {menor}')