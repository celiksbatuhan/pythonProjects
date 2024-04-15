sum_numbers = 0
product_numbers = 1
n = int(input("Enter a number: "))

for i in range(1, n+1):
    product_numbers *= i
    sum_numbers += product_numbers
    print(f"{product_numbers}", end='')
    if i != n:
        print(f"+", end='')

print(f"={sum_numbers}")
