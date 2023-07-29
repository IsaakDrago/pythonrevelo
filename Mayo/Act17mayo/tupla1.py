import random


tam=random.randint(5,15)
t=()
for i in range(tam):
    n=random.randrange(100)
    t+=(n,)
print (t)

t1=len(t)//2
print(t1)
tu=t [:t1]
print(tu)