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

def consultaSelect(nbase,ncursor,nombretabla):
    nombretabla=input("En que tabla quiere hacer la consulta?: ")
    aux=f"SELECT * FROM {nombretabla}"
    ncursor.execute(aux)
    nbase.commit

def modifTabla(nbase,ncursor, nombretabla):
    nombretabla=input("Que tabla?: ")
    columna=input("Nombre de la columna: ")
    tipo=input("Que tipo de dato va a ser?: ")
    op=print ("Que quiere hacer?: ")
    print ("1-Agregar una columna")
    print ("2-Modificar una columna")
    print ("3-Eliminar una columna")
    match op:
        case 1:
            print ("Se ha agregado la nueva columna")
            f"ALTER TABLE {nombretabla} ADD {columna} {tipo}"
        case 2:
            op=f"ALTER TABLE {nombretabla} MODIFY {columna} {tipo}"
            print ("Se modifico con exito")
        case 3:
            op=f"ALTER TABLE {nombretabla} DROP {columna}"
            print ("Se elimino la tabla")
    try:
        ncursor.execute()
        nbase.commit()
    except Exception as e:
        print("Error:", str(e))
    finally:
        ncursor.close()
        nbase.close()
        
