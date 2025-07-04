import random

tasks = []

def generate_id():
    return str(random.randint(1000, 9999))

def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    status = input("Enter status (New/Completed): ").capitalize()
    tag = input("Enter tag (High/Low): ").capitalize()

    task = {
        "id": generate_id(),
        "name": name,
        "description": description,
        "status": status,
        "tag": tag
    }

    tasks.append(task)
    print("Task added successfully.\n")

def search_task():
    user_input = input("Enter task ID or Name: ")
    found = False
    for task in tasks:
        if task["id"] == user_input or task["name"] == user_input:
            print(task)
            found = True
            break
    if not found:
        print("Task not found.\n")

def delete_task():
    user_input = input("Enter task ID or Name to delete: ")
    found = False
    for task in tasks:
        if task["id"] == user_input or task["name"] == user_input:
            tasks.remove(task)
            print("Task deleted.\n")
            found = True
            break
    if not found:
        print("Task not found.\n")

def update_status():
    user_input = input("Enter task ID or Name to update: ")
    found = False
    for task in tasks:
        if task["id"] == user_input or task["name"] == user_input:
            new_status = input("Enter new status (New/Completed): ").capitalize()
            task["status"] = new_status
            print("Status updated.\n")
            found = True
            break
    if not found:
        print("Task not found.\n")

def list_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        for task in tasks:
            print(task)
        print()

def filter_tasks():
    status_filter = input("Filter by Status (New/Completed/All): ").capitalize()
    tag_filter = input("Filter by Tag (High/Low/All): ").capitalize()

    filtered = False
    for task in tasks:
        if (status_filter == "All" or task["status"] == status_filter) and \
           (tag_filter == "All" or task["tag"] == tag_filter):
            print(task)
            filtered = True

    if not filtered:
        print("No matching tasks found.\n")
    print()

def show_stats():
    total = len(tasks)
    new_count = 0
    completed_count = 0
    high_count = 0
    low_count = 0

    for task in tasks:
        if task["status"] == "New":
            new_count += 1
        elif task["status"] == "Completed":
            completed_count += 1

        if task["tag"] == "High":
            high_count += 1
        elif task["tag"] == "Low":
            low_count += 1

    print("Total tasks:", total)
    print("New tasks:", new_count)
    print("Completed tasks:", completed_count)
    print("High priority tasks:", high_count)
    print("Low priority tasks:", low_count)
    print()

def main():
    while True:
        print("1 - Add a new Task")
        print("2 - Search for a task by ID or Name")
        print("3 - Delete a given task by ID or Name")
        print("4 - Update Status of a task by ID or Name")
        print("5 - List all tasks")
        print("6 - List using filtering by Tag or Status or both")
        print("7 - Show Stats")
        print("q - Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            search_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            update_status()
        elif choice == "5":
            list_tasks()
        elif choice == "6":
            filter_tasks()
        elif choice == "7":
            show_stats()
        elif choice.lower() == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

main()
