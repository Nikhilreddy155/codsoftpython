import pickle
import os

class ToDoList:
    def __init__(self, filename='todo.pkl'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.tasks = pickle.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully.")

    def update_task(self, task_number, updated_task):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1] = updated_task
            self.save_tasks()
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            new_task = input("Enter the new task: ")
            todo_list.add_task(new_task)
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_number, updated_task)
        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
