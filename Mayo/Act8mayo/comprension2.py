import random

apre=random.randint(20,30)
lista=[round(random.random()*5,2) for i in range(apre)]
lista.sort()
print(f"Las notas de los estudiantes son: {lista}")
aprob=[x for x in lista if x>=3]
print(f"Las notas de los que aprobaron son: {aprob}")
reprob=[x for x in lista if x<3]
print(f"Las notas de los que reprobaron son: {reprob}")
# reb=lista[:3]
# print(reb)
li1=[x for x in lista if x>0 and x<1]
li2=[x for x in lista if x>=1 and x<2]
li3=[x for x in lista if x>=2 and x<3]
li4=[x for x in lista if x>=3 and x<4]
li5=[x for x in lista if x>=4 and x<=5]

print(f"Grupo de los que tienen 0 a 1{li1}")
print(f"Grupo de los que tienen 1 a 2{li2}")
print(f"Grupo de los que tienen 2 a 3{li3}")
print(f"Grupo de los que tienen 3 a 4{li4}")
print(f"Grupo de los que tienen 4 a 5{li5}")
long=len(aprob)
sum1=[li4+li5]
print(sum1)
