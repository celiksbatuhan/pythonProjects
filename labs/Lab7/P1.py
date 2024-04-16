from os import system

students = {}

if __name__ == "__main__":
    while True:
        system("cls")
        print(
            """1. Incarcare informatii despre studenti de la tastatura.
    2. Afisare studenti.
    3. Afisare note.
    4. Afisare studenti si notele obtinute.
    5. Cautare student dupa nume.
    6. Afisare studenti promovati.
    7. Info autor.
    8. Termina program.
        """
        )
        try:
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    quantity_students = int(input("\nEnter the quantity of students: "))
                    print()
                    for i in range(quantity_students):
                        student_data = input(f"Student {i+1}: ").split(",")
                        id, name, grades = (
                            int(student_data[0]),
                            student_data[1],
                            list(map(int, student_data[2].split())),
                        )
                        students[id] = {"name": name, "grades": grades}
                        print(students)
                    input("\n\nPress Enter to continue...")
                case 2:
                    print("\nID\t| STUDENT NAME\n----------------------")
                    for id, info in students.items():
                        print(f"{id}\t| {info['name']}")
                    input("\n\nPress Enter to continue...")
                case 3:
                    print("\nID\t| STUDENT GRADE\\S\n-------------------------")
                    for id, info in students.items():
                        grades = ", ".join(map(str, info["grades"]))
                        print(f"{id}\t| {grades}")
                    input("\n\nPress Enter to continue...")
                case 4:
                    print(
                        "\nID\t| STUDENT NAME\t\t| STUDENT GRADE\\S\n-------------------------------------------------"
                    )
                    for id, info in students.items():
                        grades = ", ".join(map(str, info["grades"]))
                        print(f"{id}\t| {info['name']: <21} | {grades}")
                    input("\n\nPress Enter to continue...")
                case 5:
                    student_name = input("Enter the student's name: ")
                    found = False
                    for id, info in students.items():
                        if info["name"] == student_name:
                            found = True
                            print(
                                "\nID\t| STUDENT NAME\t\t| STUDENT GRADES\n------------------------------------------------"
                            )
                            grades = ", ".join(map(str, info["grades"]))
                            print(f"{id}\t| {info['name']: <21} | {grades}")
                    if not found:
                        input("\nStudent not found...")
                        continue
                    input("\n\nPress Enter to continue...")
                case 6:
                    print(
                        "\nID\t| STUDENT NAME\t\t| AVERAGE\n-----------------------------------------"
                    )
                    for id, info in students.items():
                        avg_grade = sum(info["grades"]) / len(info["grades"])
                        if avg_grade >= 5.0:
                            print(f"{id}\t| {info['name']: <21} | {avg_grade:.2f}")
                    input("\n\nPress Enter to continue...")
                case 7:
                    system("cls")
                    print("CELIK BATUHAN OSMAN - 3114B")
                    input("\n\nPress Enter to continue...")
                case 8:
                    break
                case _:
                    input("Invalid input, please enter a valid number...")
        except ValueError:
            input("Invalid input, please enter a valid number...")
