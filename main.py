tasks = [] # creating empty list

    while True:
    print("\nTo-Do List Menu")
    print('''1. Add Task''')
    print('''2. View Tasks''')
    print('''3. Mark Task As Complete''')
    print('''4. Delete Task''')
    print('''5. Quit''')

    choice = input("What would you like to do today? (1/2/3/4/5)")



    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task has been added successfully.")

    elif choice == "2":
        if not tasks:
            print("There are no tasks.")
        else:
            print("\nList of Tasks")
            for i, task in enumerate(tasks, 1):
                print(f"{i}.{task}")

    elif choice == "3":
        if not tasks:
            print("There are no tasks to complete.")
        else:
            while True:
                Task_Number = int(input("What task do you want to mark as done? (insert task number)"))
                if 1 <= Task_Number <= len(tasks):
                    tasks[Task_Number -1] += "(Completed)"
                    print(f"Task number {Task_Number} is completed")
                    break
                else:
                    print("Invalid task number.")

    elif choice == "5":
        print("Exiting Tab")
        break

    elif choice == "4":
        if not tasks:
            print("There are no tasks to delete.")
        else:
            delete_task = int(input("What task do you want to delete?"))
            if 1 <= delete_task <= len(tasks):
                delete = tasks.pop(delete_task -1)
                print(f"Task {delete_task} {delete} deleted successfully!")
            else:
                print("Invalid task number. Please try again.")
    else:
        print("Invalid input. Please input a number from 1 to 4")