from Persona import *
import csv
personas=[]
with open("Agosto\Agosto2\DatosExcel\personasdata.csv") as icfes:
    csvReader=csv.reader(icfes)
    for row in csvReader:
        #print(row)
        objeto=Persona(row[0],row[1],row[2],row[3],row[4])
        #print(objeto.verDatos())
        personas.append(objeto)
        

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
        if int(x)>mayor:
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

estratos=[p.getEstrato() for p in personas]
puntajeslectura=[p.getPuntLectura() for p in personas]
puntajesmatematicas=[p.getPuntMatematicas() for p in personas]
ordenascendentelectura=[p.getPuntLectura() for p in personas]
ordenascendentematematicas=[p.getPuntMatematicas() for p in personas]
sumalectura=[p.getPuntLectura() for p in personas]
sumamatematicas=[p.getPuntMatematicas() for p in personas]

with open("Agosto\Agosto2\DatosExcel\guardado.txt", "w") as datos:
    datos.write("Estrato mas alto: " + str(mayorL(estratos)) + "\n")
    datos.write("Estrato mas bajo: " + str(menorL(estratos)) + "\n")
    datos.write("Promedio de estrato: " + str(promedioL(estratos)) + "\n")

    datos.write("Puntaje mas alto de lectura critica: " + str(mayorL(puntajeslectura)) + "\n")
    datos.write("Puntaje mas bajo de lectura critica: " + str(menorL(puntajeslectura)) + "\n")
    datos.write("Promedio de puntaje de lectura critica: " + str(promedioL(puntajeslectura)) + "\n")

    datos.write("Puntaje mas alto de matematicas: " + str(mayorL(puntajesmatematicas)) + "\n")
    datos.write("Puntaje mas bajo de matematicas: " + str(menorL(puntajesmatematicas)) + "\n")
    datos.write("Promedio de puntaje de matematicas: " + str(promedioL(puntajesmatematicas)) + "\n")

    datos.write("El orden de forma ascendente de lectura critica es: " + str(ordenasc(puntajeslectura)) + "\n")
    datos.write("El orden de forma ascendente de matematicas es: " + str(ordenasc(puntajesmatematicas)) + "\n")

    datos.write("La suma de lectura critica es: " + str(sumaL(puntajeslectura)) + "\n")
    datos.write("La suma de matematicas es: " + str(sumaL(puntajesmatematicas)) + "\n")

print("Guardado :)")


# print("Estrato mas alto:", mayorL(estratos))
# print("Estrato mas bajo:", menorL(estratos))
# print("Promedio de estrato:", promedioL(estratos))

# print("Puntaje mas alto de lectura critica:", mayorL(puntajeslectura))
# print("Puntaje mas bajo de lectura critica:", menorL(puntajeslectura))
# print("Promedio de puntaje de lectura critica:",promedioL(puntajeslectura))

# print("Puntaje mas alto de matematicas:", mayorL(puntajesmatematicas))
# print("Puntaje mas bajo de matematicas:", menorL(puntajesmatematicas))
# print("Promedio de puntaje de matematicas:", promedioL(puntajesmatematicas))

# print("El orden de forma ascendente de lectura critica es:", ordenasc(puntajeslectura))

# print("El orden de forma ascendente de matematicas es:", ordenasc(puntajesmatematicas))

# print("La suma de lectura critica es:", sumaL(puntajeslectura))
# print("La suma de matematicas es:", sumaL(puntajesmatematicas))
