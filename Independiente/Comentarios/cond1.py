#Se crean las variables a las cuales se les va a asignar el numero que se ingrese

x=int(input('ingrese numero'))
y=int(input('ingrese numero'))
z=int(input('ingrese numero'))
#indentación
if x>y: #Se comparan los numeros que se escribieron para cada variable con if
    if x>z:
        print(f'el mayor es {x}') #Si la variable no cumple en el if
                                  #Se genera un else para dar continuidad por el otro camino
    else:
        print(f'el mayor es {z}')
else:
    if y>z:
        print(f'el mayor es {y}')
    else:
        print(f'el mayor es {z}')
#Se muestra en pantalla el numero mayor