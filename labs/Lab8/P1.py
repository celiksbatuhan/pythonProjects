from calendar import c
import subprocess

subprocess.run("cls", shell=True)

# C:\Users\batuh\Desktop\Lab PCLP2\pythonProjects\labs\Lab8\students.txt
file_path = input("Enter the file path: ")

students = {}


def clear_screen():
    subprocess.run("cls", shell=True)


def load_students():
    clear_screen()
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
            input("No student data found.")
            return None
    except FileNotFoundError:
        input("No file found.")
        return None
    input("\nPress Enter to continue...")


def get_student_info(i):
    student_data = input(f"\nStudent {i+1} (ID,Name,Grades): ").split(",")
    if len(student_data) != 3:
        clear_screen()
        input("Invalid input format. Please provide ID, Name, and Grades.")
        return None
    try:
        id, name, grades = (
            int(student_data[0]),
            student_data[1],
            list(map(int, student_data[2].split())),
        )
        grades = grades + [0] * (5 - len(grades))
        return id, name, grades
    except ValueError:
        clear_screen()
        input("Invalid input format. Please provide numeric ID and Grades.")
        return None


def save_students():
    with open(file_path, "w") as file:
        for id, info in students.items():
            grades = info["grades"] + [0] * (5 - len(info["grades"]))
            file.write(f"{id},{info['name']},{' '.join(map(str, grades))}\n")


def delete_student():
    print_students()
    deleted_student_id = int(input("\nEnter the ID to delete: "))
    if deleted_student_id in students:
        del students[deleted_student_id]
        clear_screen()
        input("Student information is deleted from file.")
    else:
        clear_screen()
        input("Student not found.")


def print_students():
    print(f"ID\t| STUDENT NAME\t\t| STUDENT GRADES\n{'-'*48}")
    for id, info in students.items():
        grades = ", ".join(map(str, info["grades"]))
        print(f"{id}\t| {info['name']: <21} | {grades}")


if __name__ == "__main__":
    load_students()
    while True:
        clear_screen()
        print(
            """1. Enter student information to file.
2. Save student information to file.
3. Delete student information from file.
4. Display students.
5. Search student by name.
6. Author info.
7. Exit.
        """
        )
        try:
            choice = int(input("Enter your choice: "))
            clear_screen()
            if choice == 1:
                print_students()
                quantity_students = int(input("\nEnter the quantity of students: "))
                if quantity_students < 1:
                    clear_screen()
                    input("Invalid quantity.")
                    continue
                for i in range(quantity_students):
                    student_info = get_student_info(i)
                    if student_info:
                        id, name, grades = student_info
                        students[id] = {"name": name, "grades": grades}
            elif choice == 2:
                save_students()
                input("Student information is saved to file.")
            elif choice == 3:
                delete_student()
            elif choice == 4:
                print_students()
                input("\nPress Enter to continue...")
            elif choice == 5:
                student_name = input("Enter the student's name: ")
                found = False
                for id, info in students.items():
                    if info["name"] == student_name:
                        found = True
                        print(f"\nID\t| STUDENT NAME\t\t| STUDENT GRADES\n{'-'*48}")
                        grades = ", ".join(map(str, info["grades"]))
                        print(f"{id}\t| {info['name']: <21} | {grades}")
                        break
                if not found:
                    clear_screen()
                    input("Student not found.")
                    continue
                input("\nPress Enter to continue...")

            elif choice == 6:
                clear_screen()
                input("CELIK BATUHAN OSMAN - 3114B")
            elif choice == 7:
                clear_screen()
                print("Goodbye...")
                break
            else:
                clear_screen()
                input("Invalid input, please enter a valid number.")
        except ValueError:
            clear_screen()
            input("Invalid input, please enter a valid value.")
