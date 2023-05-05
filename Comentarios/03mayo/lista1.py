#[], {}, (), {()}
x=100
print(type(x)) #La funcion type sirve para mostrar que tipo de dato almacena la variable en el momento
x='Soacha'
print(type(x))
lista=['python',100,[1,2,3,[]],'a']#A una lista se le pueden agregar diferentes tipos de datos, e incluso sublistas.
print(type(lista))
print(len(lista))#Con la funcion "len" se puede contar el numero de datos que hay almacenados en la lista
print(lista[0])#Se puede especificar el dato que se necesita imprimir usando [] y dciciendo su posicion en la lista
print(lista[1])#La posicion en positivo inicia desde "0" hasta "n-1"
print(lista[3])
print(lista[-4])#Si la posicion es indicada en negativo se inicia desde "-1" siendo este el ultimo dato de la lista

del lista[-2]#Con la funcion "del" se puede borrar algun elemento de la lista indicando su poscicion
print(lista)

"""
cuenta1=cuenta()
cuenta2=cuenta()
cuenta3=cuenta()

cuenta1.deposit()
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""