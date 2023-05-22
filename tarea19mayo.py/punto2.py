# 2- Hacer diccionarios español ingles, ingles español de animales. 
#Escriba funciones que permitan alimentar estos diccionarios y usarlos. Genere un menú para cada una de las 4 opciones.
# Alimentar cada diccionario (2 funciones)
# Usar cada diccionario (2 funciones)

def espanoling(diccionario):
    palabra=input("Ingrese el animal en español: ")
    traduc=input("Ingrese la traduccion de el animal en ingles: ")
    diccionario[palabra]=traduc
    return diccionario

def inglesesp(diccionario):
    diccionario={}
    palabra=input("Ingrese el animal en ingles: ")
    traduc=input("Ingrese la traduccion de el animal en español: ")
    diccionario[palabra]=traduc
    return diccionario

def traduciraingles(diccionario):
    animalesp=input("Ingresa el nombre del animal en español: ")
    
    if animalesp in diccionario:
        animaling=diccionario[animalesp]
        print(f"La traducción de '{animalesp}' es '{animaling}'.")
    else:
        print(f"No se encontró una traducción para '{animalesp}'.")

def traduciraespanol(diccionario):
    animaling=input("Ingresa el nombre del animal en ingles: ")
    
    if animaling in diccionario:
        animalesp=diccionario[animaling]
        print(f"La traducción de '{animaling}' es '{animalesp}'.")
    else:
        print(f"No se encontró una traducción para '{animaling}'.")

dicesping={}
dicingesp={}

print('1-Alimentar diccionario español-ingles')
print('2-Alimentar diccionario ingles-español')
print('3-Consultar diccionario español-ingles')
print('4-Consultar diccionario ingles-español')
op=int(input('¿Que quiere hacer?'))
match op:
    case 1:
        dicesping=espanoling(dicesping)
        print(dicesping)
    case 2:
        dicingesp=inglesesp(dicingesp)
        print(dicingesp)
    case 3:
        traduciraingles(dicesping)
    case 4:
        traduciraespanol(dicingesp)


