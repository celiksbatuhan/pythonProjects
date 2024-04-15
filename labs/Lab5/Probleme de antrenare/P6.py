sum_even_numbers = 0
product_odd_numbers = 1

numbers = list(map(int, input("Enter numbers as many as you want: ").split()))

for number in numbers:
    if number % 2 == 0:
        sum_even_numbers += number
    else:
        product_odd_numbers *= number

print(f"The arithmetic mean of the even numbers: {sum_even_numbers/len(numbers)}\nThe product of odd numbers {product_odd_numbers}")
