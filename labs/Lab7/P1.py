import subprocess

students = {}


def clear_screen():
    subprocess.run("cls", shell=True)


if __name__ == "__main__":
    while True:
        clear_screen()
        print(
            """1. Enter student information.
    2. Display students.
    3. Display grades.
    4. Display students and grades.
    5. Search student by name.
    6. Display passing students.
    7. Author info.
    8. Exit.
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
                    input("\n\nPress Enter to continue...")
                case 2:
                    print(f"\nID\t| STUDENT NAME\n{'-'*22}")
                    for id, info in students.items():
                        print(f"{id}\t| {info['name']}")
                    input("\n\nPress Enter to continue...")
                case 3:
                    print(f"\nID\t| STUDENT GRADE\\S\n{'-'*25}")
                    for id, info in students.items():
                        grades = ", ".join(map(str, info["grades"]))
                        print(f"{id}\t| {grades}")
                    input("\n\nPress Enter to continue...")
                case 4:
                    print(f"\nID\t| STUDENT NAME\t\t| STUDENT GRADE\\S\n{'-'*49}")
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
                                f"\nID\t| STUDENT NAME\t\t| STUDENT GRADE\\S\n{'-'*49}"
                            )
                            grades = ", ".join(map(str, info["grades"]))
                            print(f"{id}\t| {info['name']: <21} | {grades}")
                    if not found:
                        input("\nStudent not found...")
                        continue
                    input("\n\nPress Enter to continue...")
                case 6:
                    print(f"\nID\t| STUDENT NAME\t\t| AVERAGE\n{'-'*41}")
                    for id, info in students.items():
                        avg_grade = sum(info["grades"]) / len(info["grades"])
                        if avg_grade >= 5.0:
                            print(f"{id}\t| {info['name']: <21} | {avg_grade:.2f}")
                    input("\n\nPress Enter to continue...")
                case 7:
                    clear_screen()
                    input("CELIK BATUHAN OSMAN - 3114B")
                case 8:
                    break
                case _:
                    clear_screen()
                    input("Invalid input, please enter a valid number...")
        except ValueError:
            clear_screen()
            input("Invalid input, please enter a valid number...")
