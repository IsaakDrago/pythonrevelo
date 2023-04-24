#Con lo siguiente calcularemos los numeros que hay desde un numero inicial hasta un numero final

num_ini = int(input("Introduce el número inicial: "))
num_fin = int(input("Introduce el número final: "))

contador = num_ini
while contador <= num_fin:
    print(contador)
    contador += 1