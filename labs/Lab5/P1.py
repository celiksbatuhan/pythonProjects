import os
import random

vector = []
n = 0

while True:
    os.system("cls")
    print("""
A. Generare vector de n-elemente.
B. Afisare vector generat.
C. Afisare elemente > decat media aritmetica a elementelor vectorului.
D. Determinare valoare maximă şi pozitia aceasteia în tablou.
E. Deplasare elemente cu x-pozitii; x-citit de la tastatura.
F. Eliminare elemente care nu apartin intervalului [a,b].
G. Info autor.
H. exit.
    """)
    match input("Enter your choice: ").lower():
        case 'a':
            n = int(input("\nEnter n: "))
            vector = [0 for i in range(n)]
            for i in range(n):
                vector[i] = random.randint(1, 20)
            input("\nPress Enter to continue...")
        case 'b':
            print(f"\n{vector}")
            input("\nPress Enter to continue...")
        case 'c':
            sum_vector = 0
            for number in vector:
                sum_vector += number
            average_vector = sum_vector/n
            print(f"\n{vector}")
            print(f"\nAverage of vector: {average_vector}\nNumbers greater than average: ", end='')
            for number in vector:
                if number > average_vector:
                    print(number, end=' ')
            input("\n\nPress Enter to continue...")
        case 'd':
            print(f"\n{vector}")
            max_number = max(vector)
            max_number_position = 0
            for index, number in enumerate(vector, start=1):
                if number == max_number:
                    max_number_position = index
            print(f"\nThe maximum number is {max_number} and the position is {max_number_position}.")
            input("\nPress Enter to continue...")
        case 'e':
            print(f"\n{vector}")
            x = int(input("\nx: "))
            if 0 < x < n:
                new_vector = [number for number in vector]
                print(f"\n{new_vector[x:]}{new_vector[:x]}")
            else:
                print(f"\n---------\n0 < x < {n}\n---------")
            input("\nPress Enter to continue...")
        case 'f':
            print(f"\n{vector}")
            a, b = map(int, input("\nEnter a and b: ").split())
            for index, number in enumerate(vector):
                if a <= number <= b:
                    vector[index] = 0
        case 'g':
            print("\nCELIK BATUHAN OSMAN - 3114B")
            input("\nPress Enter to continue...")
        case 'h':
            break
