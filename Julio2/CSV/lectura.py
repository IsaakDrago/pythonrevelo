import csv

with open("Julio2\CSV\personaslec.csv") as f:
    reader=csv.reader(f, delimiter=",")
    for a in reader:
        print("Apellido 1: {0}, Apellido2: {1}, Nombre: {2}, Ciudad: {3}".format(a[0], a[1], a[2], a[3]))