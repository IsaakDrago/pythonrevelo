#A Pedro le mandaron como tarea hacer una calculadora que indique si una suma es mayor o menor que 10
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

res = n1 + n2
mayor10 = res > 10

print("El resultado de la suma es:", res)
if mayor10:
    print("El resultado es mayor que 10.")
else:
    print("El resultado es menor o igual que 10.")