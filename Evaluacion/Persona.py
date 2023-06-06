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
        return self.__curso
    
<<<<<<< HEAD:Act2Junio/Persona.py
    def setcurso(self):
        self.__curso.append(curs)
=======
    def setcurso(self,curso):
        self.__curso.append(curso)
>>>>>>> 9cbba72ca85baca13fa429ffa06a6f3b8869bcc7:Evaluacion/Persona.py
        
    def elimcurso(self,curso):
        self.__curso.remove(curso)

    def busccurso(self,curso):
        if curso in self.__curso:
            return (f"Si tiene el curso de {curso}")
        else:
            print(f"No tiene el curso de {curso}")
    
    def modificarcurso(self,curso):
        self.__curso

k=Persona("Lukas", 145)
print(k.getambos())
#print(k.getcurso())
k.setcurso("Matematicas")
k.setcurso("Ingles")
k.setcurso("Ciencias")
k.setcurso("Etica")
print(k.getcurso())
k.elimcurso("Matematicas")
k.elimcurso("Etica")
print(k.getcurso())
print(k.busccurso("Ingles"))
print(k.busccurso("Sociales"))
