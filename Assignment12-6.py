N=int(input("Enter the number:"))
x=2
a=1
while a<=N:
    i=2
    while i<x:
        if x%i==0:
            break
        i+=1
    else:
        print(x,end=',')
        a+=1
    x+=1    
 
