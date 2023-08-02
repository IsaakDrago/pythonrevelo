import os

def nuevoarchivo(nombrearchivo):
    if not os.path.exists(nombrearchivo):
        with open(nombrearchivo, "w") as archivo:
            print("El archivo se creo")
    else:
        print("El archivo ya existe")

def agregardatos(nombrearchivo):
    with open(nombrearchivo, "a") as archivo:
        identificacion = int(input("Ingrese su numero de identificacion: "))
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = int(input("Ingrese su telefono: "))
        datos = f"Identificacion: {identificacion}\nNombre: {nombre}\nApellido: {apellido}\nTelefono: {telefono}\n"
        archivo.write(datos)

def contarcaracteres(nombrearchivo):
    with open(nombrearchivo, "r") as archivo:
        contenido = archivo.read()
        cantidad = len(contenido)
        print(f"El archivo tiene {cantidad} caracteres.")

print('1-Agregar nuevo archivo')
print('2-Agregar datos a un archivo')
print('3-Contar los caracteres de un archivo')
op = int(input('¿Qué quiere hacer? '))

if op == 1:
    agregararchivo = nuevoarchivo(input("Escriba el nombre del nuevo archivo: "))
elif op == 2:
    dardatos = input("En que archivo quiere guardar los datos: ")
    agregardatos(dardatos)
elif op == 3:
    contar = input("A que archivo va a contar: ")
    contarcaracteres(contar)
