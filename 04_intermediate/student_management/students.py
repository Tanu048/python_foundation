# a student management system using nested dictonaries and file methods

file="student_log.txt"

#  add the load function to get data from file into dictonary and save function to save data from dictonary to file as when program runs it uses dict and not file hence both load and save are important 

def load_data():
   students={}
   with open(file,"r") as f:
         for line in f:
            sclass,sroll,sname,smarks =line.strip().split(",")
            sclass = int(sclass)
            sroll = int(sroll)
            smarks = int(smarks)   # converting all to int to make access easy
            students.setdefault(sclass,{})  #setdefault creates the dictionary only when needed else uses existing 
            students[sclass][sroll]={"name":sname,"marks":smarks}
   return students
   
def save_data(students):
    with open(file, "w") as f:
        for cls in students:
            for roll in students[cls]:   #or can use roll,s
                s = students[cls][roll]
                f.write(f"{cls},{roll},{s['name']},{s['marks']}\n") 

def add_student(students):
    sclass=int(input('Enter class: '))
    sroll=int(input('Enter roll number: '))
    sname=(input('Enter name: '))
    smarks=int(input('Enter marks: '))
    students.setdefault(sclass,{})
    if sclass not in students:
       students[sclass]={}  #creates a new class if not existing

    students[sclass][sroll]={"name":sname.title(),"marks":smarks}
    save_data(students)


def view_data(students):
   flag=False              #or use error handling 
   for cls in students:
      for roll,s in students[cls].items():         #here roll is a key and s is a value so roll,s is a key value pair in students
         print(f"Class: {cls}\tRoll Number: {roll}\tName: {s['name']}\tMarks: {s['marks']}\n")
         flag=True
   if not flag:
      print("------ Data not found")

def searchByRoll(students):
   roll=int(input("Enter roll number: "))
   found=False
   for cls in students:
      if roll in students[cls]: 
         print(f"------ Found {students[cls][roll]}")
         found=True
   if found==False:
      print("------ student not found")
         
def searchByName(students):
   name=(input("Enter name: "))
   found=False
   for cls in students:
      for roll in students[cls]:
         if name.title() in students[cls][roll]["name"]: 
            print(f"------ Found {cls},{{{roll}}}{students[cls][roll]}")
            found=True
   if not found:
      print("------ student not found")


def delete(students):
   cls=int(input("Enter the class:"))
   roll=int(input("Enter the roll number:"))
   if cls in students and roll in students[cls]:
      del students[cls][roll]           # deletes particular entry
      print("------ Data deleted")
   else:
      print("------ Entry not found")
   save_data(students)
            
def main():
   students=load_data()
   flag=0
   print("-----------------------------------------------------------Welcome to student management system!!!-----------------------------------------------------------\n")
   while (flag != -1):
      choice=float(input('choose:\n1. to add a student \n2. to view list \n3. to search a student \n\t3.1 -> By ROll Number \n\t3.2 -> By Name   \n4. to delete a student\n5. to exit\n'))
      match choice:
         case 1:
            add_student(students)
         case 2:
            view_data(students)
         case 3.1:
            searchByRoll(students)
         case 3.2:
            searchByName(students)
         case 4:
            delete(students)
         case 5:
            print("-----------------------------------------------------------Program ends-----------------------------------------------------------")
            flag=-1
         case _:
            print("\t\tENTER VALID INPUT!!!")

main()