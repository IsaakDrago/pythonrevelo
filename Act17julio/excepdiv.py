#Comparar validacion de un numero ingresado con while vs try-except 
# en el caso de division por cer

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
    