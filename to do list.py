









tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    if title == "":
        print("Task title cannot be empty!")
        return
    description = input("Enter task description: ").strip()
    task = [title, description, "Pending"]
    tasks.append(task)
    print("Task added successfully!")


def show_all_tasks():
    if len(tasks) == 0:
        print("There are no tasks!")
        return
    print("===== ALL TASKS =====")
    for i in range(len(tasks)):
        print("\nTask Number:", i + 1)
        print("Title:", tasks[i][0])
        print("Description:", tasks[i][1])
        print("Status:", tasks[i][2])
    print("=====================")


def complete_task():
    if len(tasks) == 0:
        print("There are no tasks to complete!")
        return
    show_all_tasks()
    number = input("Enter task number: ")
    if not number.isdigit():
        print("Invalid number!")
        return
    number = int(number)
    if number < 1 or number > len(tasks):
        print("Task number does not exist!")
        return
    if tasks[number - 1][2] == "Completed":
        print("This task is already completed!")
        return
    tasks[number - 1][2] = "Completed"
    print("Task completed successfully!")


def delete_task():
    if len(tasks) == 0:
        print("There are no tasks to delete!")
        return
    show_all_tasks()
    number = input("Enter task number to delete: ")
    if not number.isdigit():
        print("Invalid number!")
        return
    number = int(number)
    if number < 1 or number > len(tasks):
        print("Task number does not exist!")
        return
    tasks.pop(number - 1)
    print("Task deleted successfully!")


def search_task():
    if len(tasks) == 0:
        print("There are no tasks to search!")
        return
    word = input("Enter task title or keyword: ").strip().lower()
    if word == "":
        print("Search word cannot be empty!")
        return
    found = False
    print("===== SEARCH RESULTS =====")
    for i in range(len(tasks)):
        title = tasks[i][0].lower()
        description = tasks[i][1].lower()
        if word in title or word in description:
            print("\nTask Number:", i + 1)
            print("Title:", tasks[i][0])
            print("Description:", tasks[i][1])
            print("Status:", tasks[i][2])
            found = True
    if found == False:
        print("No matching tasks found!")


def show_pending_tasks():
    if len(tasks) == 0:
        print("There are no tasks!")
        return
    found = False
    print("===== PENDING TASKS =====")
    for i in range(len(tasks)):
        if tasks[i][2] == "Pending":
            print("\nTask Number:", i + 1)
            print("Title:", tasks[i][0])
            print("Description:", tasks[i][1])
            print("Status:", tasks[i][2])
            found = True
    if found == False:
        print("There are no pending tasks!")


while True:
    print("========== TO DO LIST ==========")
    print("1. Add New Task")
    print("2. Show All Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Show Pending Tasks")
    print("7. Exit")
    print("================================")
    choice = input("Choose: ")
    match choice:
        case "1":
            add_task()
        case "2":
            show_all_tasks()
        case "3":
            complete_task()
        case "4":
            delete_task()
        case "5":
            search_task()
        case "6":
            show_pending_tasks()
        case "7":
            print("Goodbye!")
            break
        case _:
            print("Invalid choice!")