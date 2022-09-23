a=-1
b=1
for i in range(1,int(input("Enter the number:"))+1):
    c=a+b
    print(c,end=',')
    a=b
    b=c
    
