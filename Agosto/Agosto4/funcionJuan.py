import mysql.connector

def Columnamas(host, user, password, database, tabla, nueva_columna, tipo_columna)
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()

    # Construir la consulta SQL para agregar la nueva columna
    alter_query = f"ALTER TABLE {tabla} ADD COLUMN {nueva_columna} {tipo_columna}"

    try:
        cursor.execute(alter_query)
        connection.commit()
        print("Se agrego la columna")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
    host = "localhost"
    user = "usuario"
    password = "contraseña"
    database = "base_de_datos"
    tabla = "nombre_de_tabla"
    nueva_columna = "nuevo_nombre_columna"
    tipo_columna = "VARCHAR(255)" 
    Columnamas(host, user, password, database, tabla, nueva_columna, tipo_columna)

def quitarolumna(host, user, password, database, tabla, Nmbrecolumna):
    # Conectarse a la base de datos
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    alter_query = f"ALTER TABLE {tabla} DROP COLUMN {Nmbrecolumna}"

    try:
        cursor.execute(alter_query)
        connection.commit()
        print("Se elimino tabla")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

    host = "localhost"
    user = "usuario"
    password = "contraseña"
    database = "base_de_datos"
    tabla = "nombre_tabla"
    column_name = "nombre_columna_a_eliminar"
    quitarolumna(host, user, password, database, tabla, Nmbrecolumna)