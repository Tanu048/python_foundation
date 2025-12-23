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
    with open(file, "r") as f:
        tasks = f.readlines()

    for i, word in enumerate(tasks):
        if task.lower() in word.lower() and "[ ]" in word:
            tasks[i] = word.replace("[ ]", "[x]", 1)
            break

    with open(file, "w") as f:
        f.writelines(tasks)


    


def del_task(word):
    with open(file, "r") as f:
        tasks = f.readlines()

    tasks = [task for task in tasks if word.lower() not in task.lower()]

    with open(file, "w") as f:
        f.writelines(tasks)





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
            word=input("Enter task to delete: ")
            del_task(word)
        case 5:
            i=-1
            print("PROGRAM QUITS!!!")
        