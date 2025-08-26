def add_task(tasks):
    task=input("Enter the Task:")
    if task in tasks:
        print("Task already exists!." )
    else:
        tasks[task]="Pending"
        print("Task added")
def view_task(tasks):
    if not tasks:
        print("\nNo tasks Available ")
    else:
        print("Your tasks are:\n")
        for task ,status in tasks.items():
            print(f"{task}- {status}")
def mark_done(tasks):
    task=input("Enter task:")
    if task in tasks:
        tasks[task]="Done"
        print("Task completed")
    else:
        print("Task not found")
def delete_task(tasks):
    task=input("Enter task:")
    if task in tasks:
        del tasks[task]
    else:
        print("Task not found")
def main():
    tasks={}
    while True:       
        print("\n--- TO-DO LIST MANAGER ---")
        print("1.  Add Tasks")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
main()