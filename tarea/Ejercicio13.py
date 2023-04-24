#Con esto podremos sumar todos los numeros que hay antes del numero que se ponga

n = int(input("Introduce un número entero positivo: "))

suma = 0
for i in range(1, n+1):
    suma += i

print("La suma de los primeros", n, "números enteros positivos es:", suma)
