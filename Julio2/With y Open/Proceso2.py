import os
def nuevoarchivo(nombrearchivo):
            if not os.path.exists(nombrearchivo):
                    archivo=open(nombrearchivo, "w")
                    print ("El archivo se creo")
            else:
                print ("El archivo ya existe")

def agregardatos(nombrearchivo):
            archivo=open(nombrearchivo, "a")
            identificacion=(int(input("Ingrese su numero de identificacion: ")))
            nombre=input("Ingrese su nombre: ")
            apellido=input("Ingrese su apellido: ")
            telefono=int(input("Ingrese su telefono: "))
            datos= f"Identificacion: {identificacion}\n Nombre:{nombre}\n Apellido: {apellido}\n Telefono: {telefono}\n"
            archivo.write(datos)
            archivo.close()

def contarcaracteres(nombrearchivo):
        archivo=open(nombrearchivo, "r")
        contador=archivo.read()
        cantidad=len(contador)
        print(f"El archivo tiene {cantidad} caracteres.")
        archivo.close()


print('1-Agregar nuevo archivo')
print('2-Agregar datos a un archivo')
print('3-Contar los caracteres de un archivo')
op=int(input('¿Que quiere hacer? '))
match op:
    case 1:
        agregararchivo=nuevoarchivo(input("Escriba el nombre del nuevo archivo: "))
    case 2:
        dardatos=input("En que archivo quiere guardar los datos: ")
        agregardatos(dardatos)
    case 3:
        contar=input("A que archivo va a contar: ")
        contarcaracteres(contar)
