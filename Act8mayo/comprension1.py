import random
import math
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
print(lista)
lista2=[math.sqrt(j) if j%2==0 else j**2 for j in lista]
print(lista2)
