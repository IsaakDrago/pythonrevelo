# 1- Funcion Recibe un diccionario y una palabra que representa la clave (key), 
#y nos retorna el valor asociado y el tipo de dato de ese valor. Si no existe debe indicarlo

def obtener_valor_tipo(diccionario, clave):
    if clave in diccionario:
        valor = diccionario[clave]
        tipo = type(valor).__name__
        return valor, tipo
    else:
        return None, None