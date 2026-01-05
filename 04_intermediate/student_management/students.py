# a student management system using nested dictonaries and file methods

file="student_log.txt"

#  add the load function to get data from file into dictonary and save function to save data from dictonary to file as when program runs it uses dict and not file hence both load and save are important 

def load_data():
   students={}
   with open(file,"w+") as f:
         for line in f:
            sclass,sroll,sname,smarks =line.strip().split(",")
            students.setdefault(sclass,{})
            students[sclass][sroll]={"name":sname,"marks":smarks}
   return students
   
def save_data(students):
    with open(file, "a+") as f:
        for cls in students:
            for roll in students[cls]:
                s = students[cls][roll]
                f.write(f"{cls},{roll},{s['name']},{s['marks']}\n")

def add_student():
    sclass=int(input('Enter class: '))
    sroll=int(input('Enter roll number: '))
    sname=(input('Enter name: '))
    smarks=int(input('Enter marks: '))
    students={sclass:{sroll:{"name":sname,"marks":smarks}}}
    if sclass not in students:
       students[sclass]={}

    students[sclass][sroll]={"name":sname.title(),"marks":smarks}
    save_data(students)


def view_data(students):
   for cls in students:
      for roll,s in students[cls].items():         #here roll is a key and s is a value so roll,s is a key value pair in students
         print(f"Class: {cls}\tRoll Number: {roll}\tName: {s['name']}\tMarks: {s['marks']}\n")


def searchByRoll(students):
   roll=(input("Enter roll number: "))
   for cls in students:
      if roll in students[cls]: 
         print(f"Found {students[cls][roll]}")
      else:
         print("Student not found.")
         
def searchByName(students):
   name=(input("Enter name: "))
   for cls in students:
      for roll in students[cls]:
         if name.title() in students[cls][roll]["name"]: 
            print(f"Found {cls},{{{roll}}}{students[cls][roll]}")
         else:
            print("Student not found.")


def delete(students):
   cls=input("Enter the class:")
   roll=input("Enter the roll number:")
   if cls in students and roll in students[cls]:
      del students[cls][roll]
   else:
      print("entry not found.")
   save_data(students)
   
            
def main():
   students=load_data()
   flag=0
   print("Welcome to student management system!!!\n")
   while (flag != -1):
      choice=int(input('choose:\n1. to add a student \n2. to view list \n3. to search a student \n\ta.By ROll Number \n\tb.By Name   \n4. to delete a student\n5. to exit '))
      match choice:
         case 1:
            add_student()
         case 2:
            view_data(students)
         case 'a':
            searchByRoll(students)
         case 'b':
            searchByName(students)
         case 4:
            delete(students)
         case 5:
            flag=-1
         case _:
            print("Enter valid inputs!!!")

students=load_data()
add_student()
add_student()
delete(students)