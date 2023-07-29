x=int(input("Escriba un numero: "))
y=int(input("Escriba otro numero: "))
r=0
while x==y or y==x:
    print("Son iguales, vuelva a intentarlo.")
    x=int(input("Escriba un numero: "))
    y=int(input("Escriba otro numero: "))
if x>y:
        print(f"El numero mayor es {x}")

elif y>x:
        print(f"El numero mayor es {y}")