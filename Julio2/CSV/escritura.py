import csv

personas=[
    ["Revelo", "Manrique","Isaac","3143921580"],
    ["Ramirez", "Calderon","Daniela","314693274"],
    ["Alvarez", "Bermudez","Santiago","318093197"],
]

with open("Julio2\CSV\personasesc.csv", "w", newline="") as f:
    writer= csv.writer(f, delimiter= ";")
    writer.writerow(personas)
    writer.writerows(personas)