num1,num2=100,50 #Se crean dos variables y se les asignan dos numeros
#Se muestran en pantalla diferentes operaciones que se pueden realizar con los numero ingresados
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
op=int(input('que operacion?')) #Se crea una nueva variable "op" para preguntar y asignar la operacion deseada
match op: #Con la funcion de matchcase se pueden crear varias opciones segun se halla determinado
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)