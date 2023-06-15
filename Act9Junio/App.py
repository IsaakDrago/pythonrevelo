from Empresa import *
from Individual import *
from Producto import *

c1 =Individual("Isy", 125367, 2243532)
p1 =Producto("Refresco", "Limonada", 2000)
c1.agregarprod(p1)
print(p1.getnompro())

for producto in c1.getprod():
    print(producto.getnompro())

nombre = "Refresco"
c1.descuentoI(nombre)

for producto in c1.getprod():
    if producto.getnompro() == nombre:
        print("Descuento aplicado al producto", producto.getnompro())
        print("Precio actualizado:", producto.getprecio())
