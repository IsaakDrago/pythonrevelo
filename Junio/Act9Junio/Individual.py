from Cliente import *
from Producto import *

class Individual(Cliente):
    def __init__(self,nombre,telefono, direccion):
        super().__init__(nombre,telefono)
        self.__direccion=direccion
        self.__prodI=[]

    def agregarprod(self,nompro):
        self.__prodI.append(nompro)

    def getprod(self):
        return self.__prodI
    
    def descuentoI(self, precioproduc):
        for producto in self.__prodI:
            if producto.getprecio() == precioproduc:
                producto.setprecio(producto.getprecio() - (producto.getprecio() * 0.035))
    #salariodescuento=salario-(salario*0.035)

    # def setnombre(self,nombre):
    #     self.__nombre=nombre

    # def settelefono(self,telefono):
    #     self.__telefono=telefono

    # def setdireccion(self,direccion):
    #     self.__direccion=direccion

    # def getdatos(self):
    #     return f"{self.__nombre}, {self.__telefono}, {self.__direccion}"

    