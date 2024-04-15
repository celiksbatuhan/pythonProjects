sum=0
x=input("Enter a value for x: ")
n=int(input("Enter a value for n: "))
for i in range(1,n+1):
    sum += int(i * x)
    print(i*x,end=' + ') if i!=n else print(f"{i*x} = {sum}")

