#Un programa que diga cuantas letras tiene cada linea del coro del himno de soacha
#Escriba la respuesta en otro archivo
try:
    lista=[]
    contador=0
    letras = open("Agosto\Agosto2\coro.txt", "r", encoding="utf-8")
    for linea in letras.readlines():
        for caracter in linea:
            contador +=1
        print(contador)
        contador=0
        lista.append(contador)
    
    conteo= open("Agosto\Agosto2\conteo.txt", "w", encoding="utf-8")
    conteo.write(lista)
    conteo.close()
except IOError as e:
    print("Error", e)