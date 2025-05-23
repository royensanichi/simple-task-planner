import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("===============")
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("===============")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print(f'Task "{task}" added.')
    else:
        print("Empty task not added.")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return
    show_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            confirmation = input(f"Delete {tasks[index]} ? Y / N :") 
            if confirmation == "Y":
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f'Task "{removed}" deleted.')
            else :
                print ('Deletion Canceled.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("""--------------------------
SanichiDev Daily Planner - Simple-To-Do List
1. Show tasks
2. Add task
3. Delete task
4. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
