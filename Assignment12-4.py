N1=int(input("Enter the first number:"))
N2=int(input("Enter the last number:"))
for x in range(N1,N2+1):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=',')
