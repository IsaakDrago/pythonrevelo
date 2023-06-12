from Empresa import *
from Individual import *
from Producto import *

c1=Empresa("Isy",125367,2243532)
p1=Producto("Refresco","Limonada")
c1.agregarprod(p1)
print(p1.getnompro())
for producto in c1.getprod():
    print(producto.getnompro())
