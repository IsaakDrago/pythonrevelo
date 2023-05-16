def calcular_cuartiles(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    
    c1 = int(n * 0.25)
    c2= int(n * 0.5)
    c3 = int(n * 0.75)
    
    q1 = lista_ordenada[c1]
    q2 = lista_ordenada[c2]
    q3 = lista_ordenada[c3]
    
    return q1, q2, q3
mi_lista = [12, 45, 67, 89, 23, 56, 78, 90, 34]
cuartil1, cuartil2, cuartil3 = calcular_cuartiles(mi_lista)
print("Q1:", cuartil1)
print("Q2:", cuartil2)
print("Q3:", cuartil3)
