n=int(input("Enter a number: "))

if n>100:
    print(oct(n))
elif n<100:
    print(hex(n))
else:
    print(int(n))