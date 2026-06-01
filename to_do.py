file_name="tasks.txt"

def load_tasks():
    try:
        with open(file_name,'r') as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def store_tasks(tasks):
    with open(file_name,'w')as file:
        for task in tasks:
            file.write(task+'\n')

tasks=load_tasks()

while True:
    print("_____ To Do List _____")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove task")
    print("4.  Exit")

    choice=int(input("Enter your choice"))

    if choice==1:
        task=input("Enter your Task:")
        tasks.append(task)
        store_tasks(tasks)
        print("Task added successfully")
    elif choice==2:
        if not tasks:
            print("No tasks available to view")
        else:
            print("\n Your tasks")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
    elif choice==3:
        if not tasks:
            print("No task available to remove")
        else:
            print("\n Your Tasks")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}.{task}")
            try:
                index=int(input("Enter task number to remove:"))-1
                removed=tasks.pop(index)
                store_tasks(tasks)
                print(f"{removed} removed successfully")
            except (ValueError,IndexError):
                print("Invalid task number")
    elif choice==4:
        print("Do to list app End")
        break
    else:
        print("Invalid choice,try again")
        
        