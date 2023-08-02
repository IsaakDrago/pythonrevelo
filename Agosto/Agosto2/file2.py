try:
    contador=0
    stream=open("Agosto\Agosto2\himno.txt", 'r', encoding='utf-8')

    for linea in stream.readlines():
        print(linea)
except IOError as e:
    print("Error", e)