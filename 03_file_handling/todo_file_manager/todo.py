file="task.txt"

print("Welcome to the task manager")

def add_task(task):    
    f=open(file,'a')
    f.write(f"[ ]{task}\n")
    f.close()

def list_items():
    f=open(file,'r')
    f=f.read()
    print(f)    

def complete_task(task):
    with open(file,'r') as f:
        for line in f: 
            if line==task:
                print(line)

def del_task(task):
    with open(file,'r') as f:
        for line in file: 
            if line==task:
                print(line)




i=0
while i!=-1:
    i=int(input("CHOOSE:\n1.Add task\n2.See list\n3.Complete task\n4.Delete task\n5.Exit\n"))
    match i:
        case 1:
            task=input("Enter task: ")
            add_task(task)
        case 2:
            list_items()
        case 3:
            task=input('Enter completed task: ')
            complete_task(task)
        case 4:
            task=input("Enter task to delete: ")
            del_task(task)
        case 5:
            i=-1
            print("PROGRAM QUITS!!!")
        