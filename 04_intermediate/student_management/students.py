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
    with open(file,"w") as f:
       f.write(str(students))

def view_data(students):
   with open(file,"r") as f:
      for line in f:
         if not line:
            print("No data")
            return
         else:
            print(line)

print("Welcome to student management system!!!\n")
choice=input('choose:\n1. to add a student\n2. to view list\n3. to search a student\n\ta. by roll number\n\tb. by class\n')   
match choice:
   case 1:
      add_student()
   case 2:
        view_data()
   case 'a':
        pass
   case default:
      pass 
