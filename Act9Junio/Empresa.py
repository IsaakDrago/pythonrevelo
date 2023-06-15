from Cliente import *
from Producto import *

class Empresa(Cliente):
    def __init__(self,nombre,telefono, fax):
        super().__init__(nombre,telefono)
        self.__fax=fax
        self.__prodE=[]
    
    def agregarprod(self,nompro):
        self.__prodE.append(nompro)

    def getprod(self):
        return self.__prodE
    
    def descuentoI(self, precioproduc):
        for producto in self.__prodE:
            if producto.getprecio() == precioproduc:
                producto.setprecio(producto.getprecio() - (producto.getprecio() * 0.02))

    # def setnombre(self,nombre):
    #     self.__nombre=nombre

    # def settelefono(self,telefono):
    #     self.__telefono=telefono

    # def setdireccion(self,fax):
    #     self.__fax=fax

    # def getdatos(self):
    #     return f"{self.__nombre}, {self.__telefono}, {self.__fax}"
    
