for i in range(11): #Se define la variable "i" y un rango con un numero de demas para el que se requiere
    if i%3==0: #Con un if se puede poner la condicion de que module los numeros en 3
        print(f'{i} es multiplo de 3') #Mostrara en pantalla los numero que al modularse por 3 den 0 con un comentario
    else:
        print(i) #Si el numero no cumple con dar 0 solo lo mostrara sin comentarios adicionales

for j in range(1,11): #Cuando se ponen 2 numeros separados por comas, se tomara que el 1ro sea el inicio del rango y el 2do sea el fin del mismo
    print(j) #Se muestra en pantalla el resultado

for k in range(0,11,2): #Cuando hay 3 numeros, se repite lo anterior y el 3er numero es la cantidad que ira aumentado mientras se ejecute
    print(k)

for i in range(20,0,-2): #Para un rango que sea decreciente de pone el numero mayor 1ro, el menor de 2do y el 3ro como numero negativo
    print(i)