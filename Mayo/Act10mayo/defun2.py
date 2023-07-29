def serfib(n):
    fibo=[0,1]
    while fibo[-1]<n:
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[:-1]
n = int(input("Ingrese la cantidad de números para crear la serie de fibonacci: "))
print(serfib(n))