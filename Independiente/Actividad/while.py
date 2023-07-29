n=int(input("Ingrese hata que numero quiere que se repita"))
y=0

while y<=n:
    y+=1
    if y%7==0:
        print(f"El numero {y} es multiplo de 7")
    else:
        print(f"{y}")