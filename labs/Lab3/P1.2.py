n=int(input("Enter a value for n: "))
print("\na.")
for i in range(n,-1,-1):
    print(i,end=' ')
print("\nb.")
for i in range(n+1):
    if i%2==1:
        print(i,end=' ')
print("\nc.")
factorial=1
for i in range(1,n+1):
    factorial*=i
print(f"factorial of {n} = {factorial}")
print("d.")
sum=0
x=int(input("Enter a value for x: "))
for i in range(n+1):
    if i%x==0 and i!=0:
        print(i,end=' ')
        sum+=i
print(f"\nSum = {sum}")
