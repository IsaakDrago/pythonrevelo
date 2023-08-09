def actualizarRegistro(nbase, ncursor, nombretabla, columna_actualizar, nuevo_valor, columna_condicion, valor_condicion):
    consulta = f"UPDATE {nombretabla} SET {columna_actualizar} = '{nuevo_valor}' WHERE {columna_condicion} = '{valor_condicion}'"
    
    try:
        ncursor.execute(consulta)
        nbase.commit()
        print("Registro actualizado exitosamente")
    except Exception as e:
        print("Error:", str(e))

def eliminarRegistros(nbase, ncursor, nombretabla, columna_condicion, valor_condicion):
    consulta = f"DELETE FROM {nombretabla} WHERE {columna_condicion} = '{valor_condicion}'"
    
    try:
        ncursor.execute(consulta)
        nbase.commit()
        print("Registros eliminados exitosamente")
    except Exception as e:
        print("Error:", str(e))