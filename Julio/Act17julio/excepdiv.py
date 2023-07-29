#Comparar validacion de un numero ingresado con while vs try-except 
# en el caso de division por cero

print("Con While sin Try-Except")
while True:
    n1=int(input("Ingrese un numero para divisor: "))
    n2=int(input("Ingrese un numero para dividendo: "))
    if n2 !=0:
        r1=n1/n2
        print(f"El resultado es: {r1}")
        break
    # elif n1 or n2 !=int:
    #     print ("No se admiten letras")
    else:
        print("No se puede dividir entre cero")

print("Con While y try-except")
while True:
    try:
        x=int(input("Ingresa un numero para divisor: "))
        y=int(input("Ingresa un numero para dividendo: "))
        r=x/y
        print(f"La division da: {r}")
        break
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("No se permiten letras")
    except:
        print("Otro error")
    