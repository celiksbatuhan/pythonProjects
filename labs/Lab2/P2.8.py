a = int(input("a="))
b = int(input("b="))

if a == 0:
    if b == 0:
        print("Ecuatie indeterminata. Are infinitate de solutii")
    else:
        print("Ecuatie imposibila. Nu are solutii")
else:
    x = -b/a
    print(f"Solutia ecuatiei {a}x+{b}=0 este {x}")