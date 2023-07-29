#A continuacion se presenta una pequeña encuesta sobre las comidas mas populares de Colombia.
#Escoge la comida que mas te guste
print("¿Cuál es tu comida favorita de la gastronomia colombiana?")
print("1. Bandeja Paisa")
print("2. Sancocho")
print("3. Lechona")
print("4. Ajiaco")
print("5. Tamales")

eleccion = input("Introduce el número de tu elección: ")

if eleccion == "1":
    print("Este es una manjar caracteristico de Antioquia y uno de los platos mas reconocidos de Colombia.")
elif eleccion == "2":
    print("Su receta varia segun la region, este se suele preparar con distintos tipos de carne. Es sencilla pero deliciosa.")
elif eleccion == "3":
    print("Este es uno de los platos que mas llaman la atencion de los extranjeros, debido a su curiosa presentacion.")
elif eleccion == "4":
    print("Este plato consta de 3 tipos de papa, pollo, alcaparras, mazorca, aguacate y arroz, en la gastronomia colombiana los caldos son muy importantes")
elif eleccion == "5":
    print("Los tamales son perfectos para un desayuno o una rica merienda")
else:
    print("Lo siento, no reconocí tu elección. Por favor, selecciona una opción válida.")
