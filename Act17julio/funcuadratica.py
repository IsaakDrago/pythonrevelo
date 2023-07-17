#Funcion cuadratica con manipulacion de errores y otra version sin este caso

from math import sqrt

def cuadratica(x,y,z):
    fun=(y**2) -(4*x*z)
    r1=(-y-math.sqrt(fun))/(2*x)
    # r2=(-y+math.sqrt(fun))/(2*x)
    return (r1)

pru=cuadratica(2,4,6)
print(pru)
    