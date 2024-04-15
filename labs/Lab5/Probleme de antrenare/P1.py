import math


def combination(n, m):
    return math.factorial(n) / (math.factorial(m) * math.factorial(n - m))


for m in range(1, 11):
    result = combination(10, m)
    print(f"combination of 10 taken {m}: {result}")