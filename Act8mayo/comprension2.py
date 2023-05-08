import random

apre=random.randint(20,30)
lista=[round(random.random()*5,2) for i in range(apre)]
print(lista)

aprob=[x for x in lista if x>=3]
print(aprob)
reprob=[x for x in lista if x<3]
print(reprob)
# li1=[x for x in lista if x>0 and x<1]
# li2=[x for x in lista if x>=1 and x<2]
# li3=[x for x in lista if x>=2 and x<3]
# li4=[x for x in lista if x>=3 and x<4]
# li5=[x for x in lista if x>=4 and x<=5]

print(li1)
print(li2)
print(li3)
print(li4)
print(li5)
