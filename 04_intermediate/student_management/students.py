# a student management system using nested dictonaries and file methods

file="student_log.txt"
students={}

def add_student():
    sclass=int(input('Enter class: '))
    sroll=int(input('Enter roll number: '))
    sname=(input('Enter name: '))
    smarks=int(input('Enter marks: '))
    
    if sclass not in students:
       students[sclass]={}

    students[sclass][sroll]={"name":sname,"marks":smarks}
    with open(file,"a+") as f:               # the functions in string methods take only string, list and int data types
       f.write(f"Class: {sclass}\t Roll Number: {sroll}\t  Name: {sname.title()}\t  Marks: {smarks}\n")


def view_data(students):
   with open(file,"r") as f:
      for line in f:
         if not line:
            print("No data!")
         print(f"{line}\n")


def searchByClass(students):
   sclass=int(input("Enter class: "))
   for Class in students:
      if Class==sclass:
         print(students)


            
def main():
   print("Welcome to student management system!!!\n")
   choice=int(input('choose:\n1. to add a student\n2. to view list\n3. to search a student\n\ta. by roll number\n\tb. by class\n4. to delete a student\n5. to exit '))
   flag=0
   while (flag != -1):
      match choice:
         case 1:
            add_student()
         case 2:
            view_data(students)
         case 'a':
            pass
         case "b":
            pass
         case 4:
            pass
         case 5:
            flag=-1
         case _:
            pass
 