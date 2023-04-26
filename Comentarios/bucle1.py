i=1 #Se crea una variable "i" y se le asigna 1
sum=0 #Se crea una segunda variable "sum" y se le asigna 0

while i<=5: #Con while se crea un ciclo que indique que mientras "i" sea menor o igual a 5 se repita
    print(i)
    sum=sum+i #Se indica que cada vez que el ciclo se repita, a la variable "sum" 
              #Se le debe sumar lo que corresponda a "i" en el momento
    i+=1 #i=i+1 
print(f'la suma es ={sum}') #Se muestra en pantalla la suma de todos los numero que pasaron por el ciclo