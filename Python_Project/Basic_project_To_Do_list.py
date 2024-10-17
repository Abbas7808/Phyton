# Define The File To Store task

# Load task form the File
def load_tasks():
    try: # Corrected indentation
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            tasks = [line.strip() for line in tasks]
    except FileNotFoundError:
        tasks = [] # Fixed assignment and indentation
    return tasks # Added return statement

# Save task to the file
def save_tasks(tasks):
    with open("task.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main Program Loop
def main():
    tasks = load_tasks()

    while True: # Starts an infinite loop to continously prompt the user for input.

        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                save_tasks(tasks)
                print("Task removed successfully!")
            else:
                print("Task not found!")
        elif choice == "3":
            print("Your tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        elif choice == "4":
            save_tasks(tasks) # Pass tasks to the save function
            print("Tasks saved successfully!...") # Corrected message
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
