class Persona:
    def __init__(self, dptoreside, estrato, nomcolegio, puntlectura, puntmatematicas):
        self.__dptoreside = dptoreside
        self.__estrato = self.entero(estrato)
        self.__nomcolegio = nomcolegio
        self.__puntlect = self.entero(puntlectura)
        self.__puntmat = self.entero(puntmatematicas)

    def entero(self, valor):
        try:
            return int(valor)
        except ValueError:
            return 0

    def verDatos(self):
        return f"Departamento Residencia: {self.__dptoreside}, Estrato: {self.__estrato}, Nombre Colegio: {self.__nomcolegio}, Puntaje Lectura Critica: {self.__puntlect}, Puntaje Matematica: {self.__puntmat}"

    def getDpto(self):
        return self.__dptoreside
    def getEstrato(self):
        return self.__estrato
    def getColegio(self):
        return self.__nomcolegio
    def getPuntLectura(self):
        return self.__puntlect
    def getPuntMatematicas(self):
        return self.__puntmat