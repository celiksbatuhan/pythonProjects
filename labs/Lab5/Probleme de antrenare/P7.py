count = 0
n = int(input("Enter a number: "))

for i in range(1, n):
    if n % i == 0:
        count += i

if count == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is NOT a perfect number.")