class Empleado :
    suma=0
    cont=0
    def __init__(self,nombre,cargo,salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario=salario
        Empleado.cont+=1
        Empleado.suma+=salario

    def getnombre(self):
        return self.__nombre
    
    def setnombre(self,nombre):
        self.__nombre =nombre
    
    def getcargo(self):
        return self.__cargo
    
    def setcargo(self,cargo):
        self.__cargo =cargo
    
    def getsalario(self):
        return self.__salario
    
    def setsalario(self,salario):
        self.__salario=salario
        
    def ganhora(self):
        horasdia = 8
        diassemana = 5
        semanasmes = 4
        return self.__salario / (horasdia * diassemana * semanasmes)

    def incipc(self):
        ipcmax=0.1312
        ipcmin=0.1612
        if self.__salario>1800000:
            r=self.__salario*ipcmax
            return r
        else:
            self.__salario<=1800000
            r=self.__salario*ipcmin
            
        salact=self.__salario+r
        return salact
    
    def horextra(self):
        horasmax=2
        diassemana=5
        salario=self.__salario / (horasmax * diassemana)
        horas=int(input("Ingrese la cantidad de horas extras: "))
        horasextra=horas 
        if horas>horasmax*diassemana:
            return print("El numero es invalido")
        else:
            horas<=horasmax * diassemana
        incsalario=horasextra * salario
        return incsalario

    def promedio():
        if Empleado.cont==0:
            return print("No hay empleados")
        else:
            prom=Empleado.suma/Empleado.cont
            return prom

e1=Empleado("Pedro","Gerente",3000000)
print("El salario del empleado es", e1.getsalario())
print("Salario por hora del empleado:", e1.ganhora())
print("El incremento al salario segun el ipc es de: ", e1.incipc())
print("El salario total es de: ",e1.getsalario()+e1.incipc())
salario_extra = e1.horextra()
print(f"El salario extra por horas extras es de:", salario_extra)

e2=Empleado("Lukas","Jefe",1000000)
print("El salario del empleado es", e2.getsalario())
print("Salario por hora del empleado:", e2.ganhora())
print("El incremento al salario segun el ipc es de: ", e2.incipc())
print("El salario total es de: ",e2.getsalario()+e2.incipc())
salario_extra = e2.horextra()
print(f"El salario extra por horas extras es de:", salario_extra)

sumasalarios=Empleado.suma
print("La suma de los salarios es de:", sumasalarios)

promsalarios=Empleado.promedio()
print("El promedio de los salarios es:", promsalarios)