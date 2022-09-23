a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
for i in range(a if a>b else b,(a*b)+1):
    if i%a==0 and i%b==0:
        print(i,"is least comman multiple")
        break
