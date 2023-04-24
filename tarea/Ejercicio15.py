#Para una competencia se pidio que los concursantes bucaran numeros pares, puedes identificar cuales son los numeros pares,
#Si solo queremos 5, 7, 11, 20 y 34

n = int(input("Introduce el número de números pares que deseas imprimir: "))

contador = 0
numero_actual = 0
while contador < n:
    print(numero_actual)
    numero_actual += 2
    contador += 1
