x=int(input("Ingrese primer numero"))
y=int(input("Ingrese segundo numero"))
while x%y!=0:
    print("No son factores ingrese numeros nuevamente")
    x=int(input("Ingrese primer numero"))
    y=int(input("Ingrese segundo numero"))
if x%y==0 or y%x==0:
    print("son factores")