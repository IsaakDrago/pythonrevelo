n = int(input("Ingrese la cantidad de números para crear la serie de fibonacci: "))
fibo=[0,1]
while len(fibo) < n:
    cont=fibo[-1]+fibo[-2]
    fibo.append(cont)
print(f"La serie de Fibonacci es {fibo}")
