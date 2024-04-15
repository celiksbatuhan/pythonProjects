import cmath

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

delta = b**2-4*a*c

if delta > 0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print(f"ecutia are solutiile x1={x1}, si x2={x2}")
elif delta == 0:
    x = -b/2*a
    print(f"ecuatia are o solutie reala x={x}")
else:
    x1 = (-b + cmath.sqrt(delta))/(2*a)
    x2 = (-b - cmath.sqrt(delta))/(2*a)

    print(f"solutiile complexe ale ecuatii sunt x1={x1}, x2={x2}")
