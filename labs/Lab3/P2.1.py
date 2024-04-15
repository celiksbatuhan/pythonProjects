sum=0
i=1
n=int(input(f"Enter number {i}: "))
while n!=0:
    sum+=n
    i+=1
    n = int(input(f"Enter number {i}: "))
print(f"Sum of the numbers = {sum}")
