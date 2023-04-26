num=1
cont=0
suma=0
prom=0
while num!=0:
    num=int(input("Ingrese numero"))
    cont=cont+1
    suma=suma+num
    prom=suma/cont
    mayor=max(num)
    
print(f"Fueron ingresados {cont-1} numeros")
print(f"La suma de los numeros es: {suma}")
print(f"El promedio es: {prom}")
print(f"El numero mayor: {mayor}")