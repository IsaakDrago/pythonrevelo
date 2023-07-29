lista=[]#Si no se pone nada dentro de [] se crea como una lista vacia
lista.append(100)#Con la funcion append se agregan datos a la lista en la ultima posicion
lista.append(50)
lista.append(-100)
lista.append(20)
lista.append(5)

print(lista)
lista.insert(-2,'prueba') #Con la funcion insert tambien se pueden agregar datos
print(lista)              #Primeramente indicando la posicion en la que se desea agregar el dato
                          #Los datos que estaban antes en esa posicion se desplazan hacia la siguiente posicion 