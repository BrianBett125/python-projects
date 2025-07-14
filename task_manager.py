import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            due_date=data.get("due_date"),
            completed=data.get("completed", False)
        )

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, due_date=None):
        self.tasks.append(Task(title, due_date))
        print(f"✅ Task '{title}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return

        for idx, task in enumerate(self.tasks, 1):
            status = "✔️" if task.completed else "❌"
            due = f" (Due: {task.due_date})" if task.due_date else ""
            print(f"{idx}. {status} {task.title}{due}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"✅ Task '{self.tasks[index].title}' marked as complete.")
        else:
            print("⚠️ Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"🗑️ Task '{removed.title}' deleted.")
        else:
            print("⚠️ Invalid task number.")

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task) for task in data]
        else:
            self.tasks = []

def show_menu():
    print("\n📋 Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save & Exit")

def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("👉 Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("📝 Enter task title: ").strip()
            due = input("📅 Enter due date (optional, YYYY-MM-DD): ").strip()
            due_date = due if due else None
            manager.add_task(title, due_date)

        elif choice == "2":
            print("\n🔎 Your Tasks:")
            manager.view_tasks()

        elif choice == "3":
            index = input("✅ Enter task number to complete: ").strip()
            if index.isdigit():
                manager.complete_task(int(index) - 1)
            else:
                print("⚠️ Please enter a valid number.")

        elif choice == "4":
            index = input("🗑️ Enter task number to delete: ").strip()
            if index.isdigit():
                manager.delete_task(int(index) - 1)
            else:
                print("⚠️ Please enter a valid number.")

        elif choice == "5":
            manager.save_tasks()
            print("💾 Tasks saved. Goodbye!")
            break

        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

