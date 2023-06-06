class Persona :
    def __init__(self,nombre,documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__curso=[]
    
    def getnombre(self):
        return self.__nombre
    
    def setnombre(self,nombre):
        self.__nombre =nombre
    
    def getdocumento(self):
        return self.__documento
    
    def setdocumento(self,documento):
        self.__documento =documento
        
    def getambos(self):
        return f"{self.__nombre}, {self.__documento}"
    
    def getcurso(self):
        self.__curso=[]
    
    def setcurso(self):
        self.__curso.append(curs)
        
curs=int(input("Escriba el curso"))

# p=Persona ("Ana",123)
# print(p.getnombre())
# print(p.getdocumento())
# p.setnombre("Maria")
# p.setdocumento(455)
# print(p.getnombre())
# print(p.getdocumento())
# q=Persona ("Pedro",321)
# print(q.getnombre())
# print(q.getdocumento())
# q.setnombre("Martin")
# q.setdocumento(901)
# print(q.getnombre())
# print(q.getdocumento())

k=Persona("Lukas", 145)
print(k.getambos())
print(k.getcurso())
k.setcurso()
print(k.getcurso())

