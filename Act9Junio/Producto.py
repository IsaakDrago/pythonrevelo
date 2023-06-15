class Producto:
    def __init__(self, nompro, descripcion, precio):
        self.__nompro = nompro
        self.__descripcion = descripcion
        self.__precio = precio
    
    def setnompro(self, nompro):
        self.__nompro = nompro

    def getnompro(self):
        return self.__nompro
    
    def setprecio(self, precio):
        self.__precio = precio

    def getprecio(self):
        return self.__precio
    
    def getdescripcion(self):
        return self.__descripcion
