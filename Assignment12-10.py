a=int(input("Enter the firat number:"))
b=int(input("Enter the second number:"))
n=a if a<b else b
for i in range(n,0,-1):
    if a%i==0 and b%i==0:
        print(n,':is higest comman factor')
        break
