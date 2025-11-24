#codsoft task1 to-do list
list=[]

while True:
    print("\n------ TO-Do List ------\n")
    print("1. Add task")
    print("2. View task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")


    n=int(input("enter task number:"))

    match n:
        case 1:
            item=int(input("enter item to add in list:"))
            list.append(item)
            print("Task added:", list)

        case 2:
            print("List:", list)

        case 3:
            task_number=int(input("enter task index:"))
            new_task_name=int(input("enter new task name:"))
            list[task_number]=new_task_name
            print("Updated list:", list)

        case 4:
            task_number=int(input("enter task index:"))
            list.pop(task_number)
            print("After deletion:",list)

        case 5:
            print("Exit")

        case _:
            print("Invalid Operation!")
