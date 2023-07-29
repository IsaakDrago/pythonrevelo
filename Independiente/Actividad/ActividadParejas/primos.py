a=int(input("Escriba un numero: "))
if a<2:
    primo=False
else:
    primo=True
    for i in range(2,int(a**0.5)+1):
        if i%a==0:
            primo=False
            break
if primo:
    print(f"{a} es primo")
else:
    print(f"{a} no es un numero primo")