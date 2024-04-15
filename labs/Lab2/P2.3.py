n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))
if (n1+n2==2*n3 or n2+n3==2*n1 or n3+n1==2*n2) and n1!=n2!=n3:
    print("They are consecutive numbers.")
else:
    print("They are NOT consecutive numbers.")