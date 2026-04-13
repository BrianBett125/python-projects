import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f"Task '{title}' added.")
    else:
        print("Empty task title is not allowed.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()

def mark_complete(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"Marked '{tasks[index]['title']}' as complete.")
        else:
            print("Invalid task number.")
    except ValueErr

