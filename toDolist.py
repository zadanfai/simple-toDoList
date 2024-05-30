import os

tasks = []

def create_task():
    total_tasks = int(input('How many task do you have? '))
    for i in range(1, total_tasks + 1):
        task = input('Please enter a task: ')
        tasks.append(task)
        print(f"Task '{task}' added to the list.")

def read_task():
    if not tasks:
        print('There are no tasks currently.')
    else:
        print('Current tasks:')
        for index, task in enumerate(tasks, start=1):
            print(f'Task #{index}: {task}')

def update_task():
    read_task()
    task_name = input('Enter the task name to update: ')
    if task_name in tasks:
        new_name = input('Enter  the new task name: ')
        index = tasks.index(task_name)
        tasks[index] = new_name
        print(f'Task "{task_name}" updated to "{new_name}".')
    else:
        print('Task not found.')

def delete_task():
    read_task()
    try:
        task_index = int(input('Enter the task number to delete: '))
        if 1<= task_index <= len(tasks):
            deleted_task = tasks.pop(task_index - 1)
            print(f'Task "{deleted_task}" has been removed')
        else:
            print(f'Task "{task_index}" was not found.')
    except ValueError:
        print('Invalid Input.')

if __name__ == "__main__":
    operation_system = os.name
    while True:
        if operation_system == 'posix':
            os.system('clear')
        elif operation_system == 'nt':
            os.system('cls')
        
        print("+==============================================================+")
        print("|               Welcome To Simple To-Do List App               |")
        print("+==============================================================+")
        print("|                     1. Create Task                           |")
        print("|                     2. Read Task                             |")
        print("|                     3. Update Task                           |")
        print("|                     4. Delete Task                           |")
        print("+==============================================================+")

        def choices(choice):
            match choice:
                case '1': 
                    create_task()
                case '2': 
                    read_task()
                case '3': 
                    update_task()
                case '4': 
                    delete_task()
                case default:
                    "Invalid choice"
        
        print(choices(input("Enter your choice: ")))

        is_done = input("Are you done? (y/n): ").lower()
        if is_done == "y":
            print("Goodbye! 👋👋")
            break
