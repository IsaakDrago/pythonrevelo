import mysql.connector
from funcion import *

base=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_project"
)

cursor=base.cursor()

def descriptabla():
    nombretabla = input("De qué tabla quieres su descripción?: ")
    aux = f"DESCRIBE {nombretabla}"
    cursor.execute(aux)
    
    for columna in cursor:
        print(columna)

insertarDatos(base,cursor)














# print(type(base))
# cursor.execute("describe candidato")
# print(cursor)
# for data in cursor:
#     print(data)
