# a student management system using nested dictonaries and file methods

data_logs = "student_log.txt"

#  add the load function to get data from file into dictonary and save function to save data from dictonary to file as when program runs it uses dict and not file hence both load and save are important


def load_data():
    students = {}
    try:
        with open(data_logs, "r") as f:
            for line in f:
                try:
                    sclass, sroll, sname, smarks = line.strip().split(",")
                    students.setdefault(
                        sclass, {}
                    )  # setdefault creates the dictionary only when needed else uses existing
                    students[sclass][sroll] = {"name": sname, "marks": int(smarks)}
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File does not exist. A new file will be created on save.")
    return students


def save_data(students):
    with open(data_logs, "w") as f:
        for cls in students:
            for roll in students[cls]:  # or can use roll,s
                s = students[cls][roll]
                f.write(f"{cls},{roll},{s['name']},{s['marks']}\n")


def add_student(students):
    try:
        sclass = input("Enter class: ")
        sroll = input("Enter roll number: ")
        sname = input("Enter name: ")
        smarks = int(input("Enter marks: "))
    except ValueError:
        print("Enter valid data types(integers for marks rest strings)")
        return

    if sclass not in students:
        students[sclass] = {}  # creates a new class if not existing
    if sroll in students[sclass]:
        print("student already exists")
        return

    students[sclass][sroll] = {
        "name": sname.lower(),
        "marks": smarks,
    }  # students = { class : { roll : {name, marks} } }

    save_data(students)


def view_data(students):
    if not students:
        print("------ Data not found")
    for cls in students:
        for roll, s in students[
            cls
        ].items():  # here roll is a key and s is a value so roll,s is a key value pair in students
            print(
                f"Class: {cls}\tRoll Number: {roll}\tName: {s['name']}\tMarks: {s['marks']}\n"
            )


def searchByRoll(students):
    roll = input("Enter roll number: ")
    found = False
    for cls in students:
        if roll in students[cls]:
            print(f"------ Found {students[cls][roll]}")
            found = True
    if found == False:
        print("------ student not found")


def searchByName(students):
    name = input("Enter name: ")
    found = False
    for cls in students:
        for roll in students[cls]:
            if name.lower() in students[cls][roll]["name"]:
                print(f"------ Found {cls},{{{roll}}}{students[cls][roll]}")
                found = True
    if not found:
        print("------ student not found")


def delete_student(students):
    cls = input("Enter the class:")
    roll = input("Enter the roll number:")
    if cls in students and roll in students[cls]:
        del students[cls][roll]  # deletes particular entry
        print("------ Data deleted")
        if cls in students and not students[cls]:
            del students[cls]
    else:
        print("------ Entry not found")
    save_data(students)


def main():
    students = load_data()
    flag = 0
    print(f"{"-"*50}Welcome to student management system!!!{"-"*70}\n")
    while flag != -1:
        choice = input(
            "choose:\n1. to add a student \n2. to view list \n3. to search a student\n4. to delete a student\n5. to exit\n"
        )
        match choice:
            case "1":
                add_student(students)
            case "2":
                view_data(students)
            case "3":
                sub = input("a. By Roll\nb. By Name\nChoose: ")
                if sub == "a":
                    searchByRoll(students)
                elif sub == "b":
                    searchByName(students)
            case "4":
                delete_student(students)
            case "5":
                print(f"{"-"*60}Program ends{"-"*60}")
                flag = -1
            case _:
                print("\t\tENTER VALID INPUT!!!")


main()
