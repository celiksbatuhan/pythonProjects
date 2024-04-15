import os
import math

m, n = 0, 0

while True:
    os.system('cls')
    print("""
1. citire + afisare numere (2 functii).
2. patrate perfecte.
3. nr. prime.
4. nr. divizibile cu n si m.
5. cmmdc.
6. exit.
    """)

    match int(input("Enter your choice: ")):
        case 1:
            m, n = map(int, input("Enter m and n [m, n]: ").split())
            print(f"[{m}, {n}]")
            input("\nPress Enter to continue...")
        case 2:
            print(f"Perfect squares between [{m}, {n}]: ", end='')
            for i in range(1, abs(n)+1):
                if m <= i**2 <= n:
                    print(i**2, end=' ')
            input("\n\nPress Enter to continue...")
        case 3:
            print(f"Prime numbers between [{m}, {n}]: ", end='')
            for i in range(m, n+1):
                count = 0
                for j in range(2, i):
                    if i % j != 0:
                        count += 1
                if count == i - 2:
                    print(i, end=' ')
            input("\n\nPress Enter to continue...")
        case 4:
            print(f"4 digit numbers those dividable with {m} and {n}: ", end='')
            for i in range(1000, 10000):
                if i % m == 0 and i % n == 0:
                    print(i, end=' ')
            input("\n\nPress Enter to continue...")
        case 5:
            cmmdc = 0
            print(f"The greatest common factor of {m} and {n} is: ", end='')
            if n > m:
                least_number = m
            else:
                least_number = n
            for i in range(1, least_number+1):
                if m % i == 0 and n % i == 0:
                    cmmdc = i
            print(cmmdc)
            input("\nPress Enter to continue...")
        case 6:
            break
