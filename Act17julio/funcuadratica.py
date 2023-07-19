#Funcion cuadratica con manipulacion de errores y otra version sin este caso

import math

def cuadratica_manipulacion(a,b,c):
    try:
        disc=(b**2) -(4*a*c)
        if disc<0:
            raise ValueError("Esta funcion no tiene solucion")
        r1=(-b + math.sqrt(disc))/(2*a)
        r2=(-b - math.sqrt(disc))/(2*a)
        return r1, r2
    except ValueError:
        print("Error")

def cuadratica_normal(a,b,c):
    disc=(b**2) -(4*a*c)
    if disc<0:
        print("No tiene solucion")
        return
    r1=(-b + math.sqrt(disc))/(2*a)
    r2=(-b - math.sqrt(disc))/(2*a)
    return r1, r2

a = float(input("Ingrese numero 'a': "))
b = float(input("Ingrese numero 'b': "))
c = float(input("Ingrese numero 'c': "))

#Funcion 1
solucion1=cuadratica_manipulacion(a,b,c)
print(f"La solucion de la funcion es {solucion1}")

#Funcion 2
solucion2=cuadratica_normal(a,b,c)
print(f"La solucion es {solucion2}")