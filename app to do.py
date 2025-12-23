tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet!\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def remove_task():
    show_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        tasks.pop(num - 1)
        print("Task removed!\n")
    except:
        print("Invalid choice!\n")

def todo_app():
    print("=== Simple To-Do App ===")
    
    while True:
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Select option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Try again.\n")

todo_app()
