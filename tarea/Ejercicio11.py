#Tendras que adivinar cual es el numero secreto que sera asignado aleatoriamente
import random

num_sec = random.randint(1, 10)

adivinado = False
intentos = 0

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1
    
    if intento == num_sec:
        print("¡Correcto! El número secreto era", num_sec)
        print("Lo lograste en", intentos, "intentos.")
        adivinado = True
    elif intento < num_sec:
        print("Incorrecto. El número secreto es mayor que", intento)
    else:
        print("Incorrecto. El número secreto es menor que", intento)
