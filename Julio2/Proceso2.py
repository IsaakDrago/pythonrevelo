from os import strerror
def nuevoarchivo(nombrearchivo):
            try:
                with open(nombrearchivo, "x") as f:
                    print ("El archivo ya fue creado")
            except FileExistsError:
                print ("El archivo ya existe")
                
def agregardatos(archivo):
            identificacion=(int(input("Ingrese su numero de identificacion")))
            nombre=input("Ingrese su nombre")
            apellido=input("Ingrese su apellido")
            telefono=int(input("Ingrese su telefono"))
            archivo=open(arch, "w+t")
            archivo.write(identificacion,nombre,apellido,telefono)
            archivo.close()

