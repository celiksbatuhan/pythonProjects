from os import system


file_path = r"C:\Users\batuh\Desktop\Lab PCLP2\pythonProjects\labs\Lab8\students.txt"

students = {}


def load_students():
    system("cls")
    try:
        with open(file_path, "r") as file:
            for line in file:
                student_data = line.strip().split(",")
                id, name, grades = (
                    int(student_data[0]),
                    student_data[1],
                    list(map(int, student_data[2].split())),
                )
                students[id] = {"name": name, "grades": grades}
                print(f"Student {id} loaded.")
        if not students:
            print("No student data found.")
    except FileNotFoundError:
        print("No file found.")
    input("\nPress Enter to continue...")


def delete_students():
    deleted_student_id = int(input("\nEnter the ID: "))
    if deleted_student_id not in students:
        input("\nStudent is not found.")
        return
    students.pop(deleted_student_id)
    input("\nStudent information is deleted from file.")


def save_students():
    with open(file_path, "w") as file:
        for id, info in students.items():
            if len(info["grades"]) < 5:
                for i in range(5 - len(info["grades"])):
                    info["grades"].append(0)
            grades = " ".join(map(str, info["grades"]))
            file.write(f"{id},{info['name']},{grades}\n")


def print_students():
    print(f"\nID\t| STUDENT NAME\t\t| STUDENT GRADES\n{'-'*48}")
    for id, info in students.items():
        grades = ", ".join(map(str, info["grades"]))
        print(f"{id}\t| {info['name']: <21} | {grades}")


if __name__ == "__main__":
    load_students()
    while True:
        system("cls")
        print(
            """1. Enter student information to file.
2. Save student information to file.
3. Delete stundent information from file.
4. Display students.
5. Search student by name.
6. Author info.
7. Exit.
        """
        )
        try:
            match int(input("Enter your choice: ")):
                case 1:
                    print_students()
                    quantity_students = int(input("\nEnter the quantity of students: "))
                    for i in range(quantity_students):
                        print()
                        student_data = input(f"Student {i+1}: ").split(",")
                        id, name, grades = (
                            int(student_data[0]),
                            student_data[1],
                            list(map(int, student_data[2].split())),
                        )
                        students[id] = {"name": name, "grades": grades}
                    input("\nPress Enter to continue...")
                case 2:
                    save_students()
                    input("\nStudent information is saved to file.")
                case 3:
                    print_students()
                    delete_students()
                case 4:
                    print_students()
                    input("\nPress Enter to continue...")
                case 5:
                    student_name = input("\nEnter the student's name: ")
                    found = False
                    for id, info in students.items():
                        if info["name"] == student_name:
                            found = True
                            print(f"\nID\t| STUDENT NAME\t\t| STUDENT GRADES\n{'-'*48}")
                            grades = ", ".join(map(str, info["grades"]))
                            print(f"{id}\t| {info['name']: <21} | {grades}")
                    if not found:
                        input("\nStudent not found...")
                        continue
                    input("\nPress Enter to continue...")
                case 6:
                    system("cls")
                    input("CELIK BATUHAN OSMAN - 3114B")
                case 7:
                    save_students()
                    system("cls")
                    print("Goodbye...")
                    break
                case _:
                    system("cls")
                    input("Invalid input, please enter a valid number...")
        except ValueError:
            system("cls")
            input("Invalid input, please enter a valid value...")
