x=int(input("Escriba un numero: "))
y=int(input("Escriba otro numero: "))
r=0
while x==y or y==x:
    print("Son iguales, vuelva a intentarlo.")
    x=int(input("Escriba un numero: "))
    y=int(input("Escriba otro numero: "))
if x>y:
        print(f"El numero mayor es {x}")
        r=x-y
        while r>=y:
               print(f"El resultado de la resta va en {r}")
               r-=y
        print(f"La resta final es {r}")
elif y>x:
        print(f"El numero mayor es {y}")
        r=y-x
        while r>=x:
               print(f"El resultado de la resta va en {r}")
               r-=x
        print (f"El resultado final es {r}")