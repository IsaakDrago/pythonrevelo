n=int(input('ingrese numero')) #Se crea una variable para que se pueda ingresar datos
i=1 #Se asigna una variable contadora
while i<n: #Se evalua si "i" es menor que el numero ingresado
    if i%7==0: #Si al modular "i" en 7 da 0, imprimira lo siguiente
        print(f'{i} es multiplo de 7')
    else: #Si no cumple se imprimira lo siguiente
        print(i)
    i+=1 