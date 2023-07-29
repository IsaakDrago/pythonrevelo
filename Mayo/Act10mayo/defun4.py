import random

def llenarL(n):
    num=[]
    while len(num)<n:
        numero=random.randint(1, n)
        if numero not in num:
            num.append(numero)
        else:
            print(f"El número {numero} ya está en la lista.")
    return num
mi_lista = llenarL(10)
print(mi_lista)
