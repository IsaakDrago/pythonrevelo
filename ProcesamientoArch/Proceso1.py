from os import strerror 

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)} #Se crea un diccionario de llaves den letras y valores como numeros
counters.update({str(num): 0 for num in range(10)})
counters['caracter especial'] = 0
file_name = input("Ingresa el nombre del archivo a analizar: ") #Se pide que ingrese el nombre del archivo
try: #Se inicia try para prevenir posibles errores
    file = open(file_name, "rt") #Se intenta abrir el archivo en modo lectura
    for line in file: #Se recorre cada linea
        for char in line: #Se recorren los caracteres de la linea
            # Si es una letra...
            if char.isalpha(): #Se verifica si es letra
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1 #Si es letra se pasa a minuscula y se suma 1 al contador.
            elif char.isdigit():
                counters[char] += 1
            else:
                counters['caracter especial'] += 1
    
    file.close() #Se cierra el archivo
    # Demos salida a los contadores.
    for char in counters.keys(): #Se recorren las llaves del diccionario
        c = counters[char] #Se obtiene el numero del contador para la letra actual
        if c > 0: #Si el contador es mayor a 0
            print(char, '->', c) #Se imprime la letra y el numero del contador
except IOError as e: #Al error IOError se le apoda e
    print("Se produjo un error de E/S: ", strerror(e.errno)) #Si ocurre un error se muestra el mesaje
