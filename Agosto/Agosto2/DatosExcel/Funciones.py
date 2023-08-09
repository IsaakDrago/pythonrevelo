def sumaL(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promedioL(lista):
    return sumaL(lista)/len(lista)

def mayorL(lista):
    mayor=0
    for x in lista:
        if x>mayor:
            mayor=x
    return mayor
        

def menorL(lista):
    menor=100000
    for x in lista:
        if x<menor:
            menor=x
    return menor

def ordenasc(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista
    
def ordendes(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista