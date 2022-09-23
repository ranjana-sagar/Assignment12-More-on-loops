N=int(input("Enter the number:"))
for i in range(2,N):
    if N%i==0:
        print(N,":it is not prime")
        break
else:
    print(N,":this is prime number")
