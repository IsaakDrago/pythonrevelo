num1=1
while num1 <=1000:
    cont=0
    i=1
    sum=0
    while i<num1:
        if num1%i==0:
            sum+=1
        i+=1
        if num1==sum:
            print("el numero es perfecto", num1)
        num1+=1