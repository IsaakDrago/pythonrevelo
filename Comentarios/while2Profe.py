x,y=3,5 #Se asignan variables y numeros
cont=1 #Se asigna un contador
while not(x%y==0 or y%x==0): #Se define que mientras el ciclo no cumpla con la condicion no acabara el ciclo
    print(f'intento numero {cont}') #Se muestra en pantalla el numero de intentos segun el contador "cont"
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
    cont+=1

print(f'{x} y {y} son factor') #Se muestra en pantalla los numeros que son factores