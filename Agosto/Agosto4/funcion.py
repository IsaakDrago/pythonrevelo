import mysql.connector

def insertarDatos(nbase, ncursor):
    nro_identificacion=input('digite su numero de documento: ')
    nombre=input('digite sus nombre: ')
    apellidos=input('digite sus apellidos: ')
    correo=input('digite su correo electronico: ')
    telefono=input('digite su numero telefonico: ')
    aux = "INSERT INTO candidato (nro_identificacion, nombre, apellidos, correo_electronico, telefono) VALUES ('"+ nro_identificacion +"','"+ nombre +"','"+ apellidos +"','"+ correo +"','"+ telefono +"')"
    #values = (nro_identificacion, nombre, apellidos, correo, telefono)
    ncursor.execute(aux)
    nbase.commit()

def consultaSelect(nbase, ncursor, nombretabla):
    consulta = f"SELECT * FROM {nombretabla}"
    ncursor.execute(consulta)
    for fila in ncursor:
        print(fila)
    nbase.commit()

def modifTabla(nbase, ncursor, nombretabla):
    columna = input("Nombre de la columna: ")
    tipo = input("Que tipo de dato va a ser?: ")
    
    print("Que quiere hacer?: ")
    print("1-Agregar una columna")
    print("2-Modificar una columna")
    print("3-Eliminar una columna")
    op = int(input())
    
    try:
        if op == 1:
            consulta = f"ALTER TABLE {nombretabla} ADD {columna} {tipo}"
            print("Se ha agregado la nueva columna")
        elif op == 2:
            consulta = f"ALTER TABLE {nombretabla} MODIFY {columna} {tipo}"
            print("Se modifico con exito")
        elif op == 3:
            consulta = f"ALTER TABLE {nombretabla} DROP COLUMN {columna}"
            print("Se elimino la columna")
        else:
            print("Opcion no valida")
            return
        
        ncursor.execute(consulta)
        nbase.commit()
        print("Operacion exitosa")
    except Exception as e:
        print("Error:", str(e))
    finally:
        ncursor.close()
        nbase.close()