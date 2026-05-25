tasks = []
while True:
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Exit  ")
    print("3. Add Task")
    choice = input("Enter your choice: ")
    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, 1):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{index}. {status} {task['title']}")
    elif choice == "2":
        print("Exiting Task Manager. Goodbye!")
        break
    elif choice == "3":
        new_task = input("Enter the task description: ")
        tasks.append({"title":new_task, "completed":False})
        print(f"Task '{new_task}' added successfully.")
    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            task_number = int(input("Enter the task number to delete: "))
        
            removed = tasks.pop(task_number - 1)
            print(f"Deleted task: {removed['title']}")