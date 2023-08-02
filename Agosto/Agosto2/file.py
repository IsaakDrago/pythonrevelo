try:
    contador=0
    stream=open("Agosto\Agosto2\himno.txt", 'r', encoding='utf-8')
    linea=stream.readline()

    while linea!="":
        print(f"{contador} {linea}")
        linea=stream.readline()
        contador +=1
except IOError as e:
    print("Error")

