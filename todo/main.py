from todo import ToDoList

def print_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View All Tasks")
    print("4. Delete Task")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_id = int(input("Enter the task ID to mark as completed: "))
            todo_list.mark_task_completed(task_id)
        elif choice == "3":
            todo_list.view_all_tasks()
        elif choice == "4":
            task_id = int(input("Enter the task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
