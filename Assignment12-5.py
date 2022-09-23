N=int(input("Enter the number:"))
for x in range(N,N**N,1):
    for i in range(2,x):
        if (x+1)%i==0:
            break
    else:
        print(x+1)
        break

