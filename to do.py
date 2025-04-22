
def todolist():
    tasks=[]
    while True:
        print("1.Add tasks")
        print("2.remove task")
        print("3.Show tasks")
        print("4.Quit")
        choice=input("Enter your choice:-")
        if choice=="1":
            task = input("enter task:")
            tasks.append(task)
        elif choice=="2":
            task= input("enter task to remove")
            if task in tasks:
                tasks.remove(task)
            else:
                print("task not found")
        elif choice =="3":
            print("Tasks:")
            for task in tasks:
                print("*"+task)
        elif choice=="4":
            break
        else:
            print("invalid")
todolist()