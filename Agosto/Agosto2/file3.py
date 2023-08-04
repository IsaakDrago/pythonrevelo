#Un programa que diga cuantas letras tiene cada linea del coro del himno de soacha
#Escriba la respuesta en otro archivo
try:
    lista=[]
    letras = open("Agosto\Agosto2\coro.txt", "r", encoding="utf-8")
    for linea in letras.readlines():
        contador=0
        for caracter in linea:
            contador +=1
        print(contador)
        lista.append(contador)
    letras.close()
    conteo = open("Agosto/Agosto2/conteo.txt", "w", encoding="utf-8")
    for num in lista:
        conteo.write(str(num) + "\n")
    conteo.close()
except IOError as e:
    print("Error", e)