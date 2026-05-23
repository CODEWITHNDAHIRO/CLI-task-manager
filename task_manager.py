tasks = []
while True:
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Exit  ")
    print("3. Add Task")
    choice = input("Enter your choice: ")
    if choice == "2":
        print("Exiting Task Manager. Goodbye!")
        break
    elif choice == "3":
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added successfully.")