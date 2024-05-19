class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def mark_task_completed(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            self.tasks[task_id - 1]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def view_all_tasks(self):
        print("\n===== To-Do List =====")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{idx}. [{status}] {task['task']}")

    def delete_task(self, task_id):
        if 1 <= task_id <= len(self.tasks):
            del self.tasks[task_id - 1]
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']},{task['completed']}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task, completed = line.strip().split(",")
                    self.tasks.append({"task": task, "completed": eval(completed)})
        except FileNotFoundError:
            pass  # No tasks file found, so start with an empty list
