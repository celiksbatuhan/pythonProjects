import os

matrix = []
matrix_transposed = []
name_matrix = ''
column, row = 0, 0


def print_matrix(array):
    for LINE in array:
        for number in LINE:
            print(number, end=' ')
        print()


def transposed_matrix(array, array_transposed, rows, columns):
    for i in range(rows):
        for j in range(columns):
            array_transposed[j][i] = array[i][j]


while True:
    os.system("cls")
    print("""
1. Citire matrice de la tastatura (pe linii).
2. Afisare matrice.
3. Creare si afisare lista de elemente maxime de pe linii.
4. Creare si afisare lista de elemente maxime de pe coloane.
5. Afisare matrice transpusa.
6. Adauga linie.
7. Adauga coloana.
8. Sterge linie.
9. Sterge coloana.
10. Liniarizare matrice (creare si afisare vector rezultat).
0. Exit.
    """)
    try:
        match int(input("Enter your choice: ")):
            case 1:
                name_matrix = input("\nEnter the name of the matrix: ")
                row, column = map(int, input("\nEnter row and column: ").split())
                matrix = [[0 for i in range(column)] for j in range(row)]
                print(f"Enter {column} number/s for each time!!", end='\n\n')
                for index, line in enumerate(matrix):
                    matrix[index] = list(map(int, input(f"row {index+1}: ").split()))
                input("\nPress Enter to continue...")
            case 2:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                input("\nPress Enter to continue...")
            case 3:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                print("\nMax numbers are: ", end='')
                for line in matrix:
                    print(max(line), end=' ')
                input("\n\nPress Enter to continue...")
            case 4:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                matrix_transposed = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
                transposed_matrix(matrix, matrix_transposed, len(matrix), len(matrix[0]))
                print("\nMax numbers are: ", end='')
                for line in matrix_transposed:
                    print(max(line), end=' ')
                input("\n\nPress Enter to continue...")
            case 5:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                print(f"\nTransposed({name_matrix})= ")
                matrix_transposed = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
                transposed_matrix(matrix, matrix_transposed, len(matrix), len(matrix[0]))
                print_matrix(matrix_transposed)
                input("\nPress Enter to continue...")
            case 6:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                new_row = list(map(int, input(f"\nEnter {len(matrix[0])} values for new row: ").split()))
                matrix.append(new_row)
                print(f"\nNew({name_matrix})=")
                print_matrix(matrix)
                input("\nPress Enter to continue...")
            case 7:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                new_column = list(map(int, input(f"\nEnter {len(matrix)} values for new column: ").split()))
                for i in range(len(matrix)):
                    matrix[i].append(new_column[i])
                print(f"\nNew({name_matrix})=")
                print_matrix(matrix)
                input("\nPress Enter to continue...")
            case 8:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                deleted_row = int(input("\nWhat row you want to delete?: "))
                matrix.pop(deleted_row-1)
                print(f"\nNew({name_matrix})=")
                print_matrix(matrix)
                input("\nPress Enter to continue...")
            case 9:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                deleted_column = int(input("\nWhat column you want to delete?: "))
                for i in range(len(matrix)):
                    matrix[i].pop(deleted_column-1)
                print(f"\nNew({name_matrix})=")
                print_matrix(matrix)
                input("\nPress Enter to continue...")
            case 10:
                print(f"\n{name_matrix}=")
                print_matrix(matrix)
                print("\nMatrix linearization: ", end='')
                for line in matrix:
                    for number in line:
                        print(number, end=' ')
                input("\n\nPress Enter to continue...")
            case 0:
                break
            case _:
                print("Enter a number [1, 10]!")
                input("\nPress Enter to continue...")
                continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
