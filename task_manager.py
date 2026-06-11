import json
import os
TASKS_FILE = "tasks.json"
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(TASKS_FILE, "W") as f:
        json.dump(tasks, f , indent=2)
tasks = load_tasks() # this replaces tasks =[]


tasks = []
while True:
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Exit  ")
    print("3. Add Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
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
    elif choice == "5":
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            task_number = int(input("Enter the task number to mark as completed: "))
            tasks[task_number - 1]["completed"] = True
            print(f"Marked task '{tasks[task_number - 1]['title']}' as completed.")
            choice = input("Enter your choice: ")
    if choice == "1":
        if not tasks:
            print("No tasks available.")
        # ... your existing view tasks logic ...
        
    elif choice == "2":
        print("Goodbye! Thanks for using Task Manager.")
        break  # This breaks the while True loop and exits the script